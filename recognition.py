import os

import speech_recognition as sr

LANGUAGE ='uz_UZ'
recognizer = sr.Recognizer()

async def recognize(voice, bot):
    file_name = f"./voice/{voice.file_id}.ogg"
    file_name_converted = f"./result/{voice.file_id}.wav"
    await bot.download(voice, file_name)

    os.system(f"ffmpeg -i {file_name} {file_name_converted}")

    text = recognize_file(file_name_converted)

    os.remove(file_name)
    os.remove(file_name_converted)
    return text


def recognize_file(filepath):
    with sr.AudioFile(filepath) as source:
        audio_text = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio_text, language=LANGUAGE)
        except:
            return "Shovqin halaqit beryabdi..."