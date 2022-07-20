from neuralintents import GenericAssistant
from ast import If
import speech_recognition as sr
import pyttsx3
import sys

vector = ['stop', 'arrivederci', 'buongiorno', 'ciao'][0,0,1,1]

def Greeting():
    SpeakText('Ciao. Cosa posso fare per te?')

def Kill():
    SpeakText('Ciao. A presto')
    sys.exit(0)

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command, 'it')
	engine.runAndWait()

def Search(text):
	for i in vector:
        print("trovato")
	    if i[0] == text:
            if i[1] == 0:
                Kill()
            elif i[1] == 1:
                Greeting()
        else:
            print("non trovato")
            SpeakText('Non ho capito')
            break
# Loop infinitely for user to
# speak

while(1):   
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2, language='it-IT')
            MyText = MyText.lower()
 
            print("Hai detto "+MyText)
            Search(MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occured")
