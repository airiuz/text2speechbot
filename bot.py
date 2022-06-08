import os
import logging
from model import get_audio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, BufferedInputFile

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
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
    await message.answer(f"Assalomu alaykum, <b>{message.from_user.full_name}!</b>\nMenga habar yuboring va men sizga gapirib beraman.")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward received message back to the sender

    By default message handler will handle all message types (like text, photo, sticker and etc.)
    """
    try:
        # Send copy of the received message
        print(message.text)
        audio = get_audio(message.text)
        audio_file = BufferedInputFile(audio, filename="file.wav")
        await message.answer_voice(audio_file)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


def main():
    # Initialize Bot instance with an default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # And the run events dispatching
    dp.run_polling(bot)


if __name__ == "__main__":
    main()