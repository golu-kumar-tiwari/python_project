import pyttsx3
import speech_recognition as sr
import os

speaker = pyttsx3.init()
mic = sr.Recognizer()


with sr.Microphone() as source:
    print("Start Speaking......")
    mic.pause_threshold = 1
    audio = mic.listen(source)

try:
    text = mic.recognize_google(audio)
    text = text.lower()
    print("You said:", text)


except Exception as e:
    print("Could not understand your voice. Try again...")
