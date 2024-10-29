import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator
import pygame
import os
import time

recognizer = sr.Recognizer()

def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    audio_file = "output.mp3"
    tts.save(audio_file)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    time.sleep(1)
    os.remove(audio_file)

def translate_and_speak(text, src_lang, target_lang):
    translation = GoogleTranslator(source=src_lang, target=target_lang).translate(text)
    print(f'Traducere: {translation}')
    text_to_speech(translation, target_lang)

def speech_to_text(lang):
    with sr.Microphone() as source:
        print("Ascultare... Vorbește acum!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language=lang)
            print(f"Text recunoscut: {text}")
            return text
        except sr.UnknownValueError:
            print("Nu am înțeles ce ai spus.")
            return ""
        except sr.RequestError:
            print("Nu pot accesa serviciul de recunoaștere vocală.")
            return ""

while True:
    choice = input("Alegeți: (1) Text-to-speech, (2) Speech-to-text, (3) Exit: ")

    if choice == '3':
        break
    elif choice == '1':
        user_input = input("Introduceți textul pentru traducere: ")
        src_lang = input("Introduceți limba sursă (en pentru engleză, ro pentru română): ")
        target_lang = input("Introduceți limba țintă (en pentru engleză, ro pentru română): ")

        if src_lang not in ['en', 'ro'] or target_lang not in ['en', 'ro']:
            print("Limbile trebuie să fie 'en' (engleză) sau 'ro' (română).")
            continue

        translate_and_speak(user_input, src_lang, target_lang)
    elif choice == '2':
        src_lang = input("Introduceți limba sursă pentru recunoașterea vocală (en pentru engleză, ro pentru română): ")
        target_lang = input("Introduceți limba țintă pentru traducere (en pentru engleză, ro pentru română): ")

        if src_lang not in ['en', 'ro'] or target_lang not in ['en', 'ro']:
            print("Limbile trebuie să fie 'en' (engleză) sau 'ro' (română).")
            continue

        recognized_text = speech_to_text(src_lang)
        if recognized_text:
            translate_and_speak(recognized_text, src_lang, target_lang)
    else:
        print("Opțiune invalidă. Încearcă din nou.")
