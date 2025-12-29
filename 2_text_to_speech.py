# pip install pyttsx3
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, this is a text to speech conversion example.")
engine.runAndWait()