import pyttsx3
import speech_recognition
import pyaudio
import webbrowser
import os
import vosk

TTS = pyttsx3.init()
sr = speech_recognition.Recognizer()

#comment


def voice(text):
    TTS.say(text)
    TTS.runAndWait()

def cfg():
    TTS.setProperty('volume', 0.7)

def voicefound():
    with speech_recognition.Microphone() as source:
        audio = sr.listen(source)
    try:
        #text_micro = sr.recognize_google_cloud(audio, language="ru")
        text_micro = sr.recognize_vosk(audio, language="ru")
        print(text_micro)
        return text_micro
    except speech_recognition.UnknownValueError:
        print('speech error')
        return 'speech error'
    except speech_recognition.RequestError:
        print('request error')
        return 'request error'


def voice_commands(text):
    text = text.lower()
    if 'привет' in text:
        voice('Здравствуйте!')
    elif 'замолчи' in text:
        voice('Пока')
        exit()
    elif 'открой браузер' in text:
        voice('Открываю')
        webbrowser.open('https://google.com')
    elif 'открой проводник' in text:
        os.startfile('''C:/Users/kusne/AppData/Local/Programs/Microsoft VS Code/Code.exe''')






cfg()
#voice('Привет. Как дела?')
while True:
    t = voicefound()
    voice_commands(t)


