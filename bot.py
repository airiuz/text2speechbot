import os
import logging
from model import get_audio
from recognition import recognize
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, BufferedInputFile
from IPython.display import Audio

DEFAULT_TOKEN = "5181625043:AAG2bG4MnLrTMinBcCT2oHpErOOgrIN5acs"
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", DEFAULT_TOKEN)

dp = Dispatcher()

logger = logging.getLogger(__name__)


@dp.message(commands=["start"])
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    # Most of event objects has an aliases for API methods to be called in event context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage` method automatically
    # or call API method directly via Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`

    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>\nMenga habar yuboring va men sizga gapirib beraman.\bMenga ovoz yuboring va men text qilib beraman.")

    data = get_audio(f"Assalomu alaykum, {message.from_user.full_name}. Menga ovoz yuborsez text qilib beraman. Agar text yuborsez gapirib beraman.")
    audio = Audio(data=data, rate=48000).data
    audio_file = BufferedInputFile(audio, filename="file.wav")
    await message.answer_voice(audio_file)


@dp.message()
async def echo_handler(message: types.Message, bot: Bot) -> None:
    """
    Handler will forward received message back to the sender

    By default message handler will handle all message types (like text, photo, sticker and etc.)
    """

    if message.voice:
        print('Got voice message')
        text = await recognize(message.voice, bot)
        print(f'Recognized text: {text}')
        await message.answer(text)

        data = get_audio(text)
        audio = Audio(data=data, rate=48000).data
        audio_file = BufferedInputFile(audio, filename="file.wav")
        await message.answer_voice(audio_file)
    if message.text:
        print(f'Got text message: {message.text}')
        data = get_audio(message.text)
        audio = Audio(data=data, rate=48000).data
        audio_file = BufferedInputFile(audio, filename="file.wav")
        await message.answer_voice(audio_file)



def main():
    # Initialize Bot instance with an default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # And the run events dispatching
    dp.run_polling(bot)


if __name__ == "__main__":
    main()