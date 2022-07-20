from email import message
from fileinput import filename
from turtle import done
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

task_list = ['qualcosa', 'qualcosa di diverso', 'qualcosa di diverso di diverso']

def create_note():
    global recognizer

    speaker.say('Quale nota vuoi creare?')
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio, language='it-IT')
                note = note.lower()
                
                speaker.say('Schegli il  nome del file')
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio, language='it-IT')
                filename = filename.lower()
            with open(filename + '.txt', 'w') as f:
                f.write(note)
                done = True
                speaker.say('Nota creata {filename}')
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say('Non ho capito, riprova')
            speaker.runAndWait()

def add_tasks():
    global recognizer

    speaker.say('Quale compito vuoi aggiungere?')
    speaker.runAndWait()

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio, language='it-IT')
                item = item.lower()

                task_list.append(item)
                done = True

                speaker.say('Compito {item} aggiunto')
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say('Non ho capito, riprova')
            speaker.runAndWait()

def show_tasks():
    speaker.say('I compiti sono:')
    for item in task_list:
        speaker.say(item)
    speaker.runAndWait()

def greeting():
    speaker.say('Ciao. Cosa posso fare per te?')
    speaker.runAndWait()

def exit():
    speaker.say('Ciao. A presto')
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    'greeting': greeting,
    'create_note': create_note,
    'add_tasks': add_tasks,
    'show_tasks': show_tasks,
    'exit': exit
    }


assistant = GenericAssistant('intents.json', intents_metod=mappings)
assistant.train_model()
print("test")

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio, language='it-IT')
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()