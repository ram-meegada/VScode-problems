import speech_recognition as sr
import pyttsx3
import wikipedia
from myOpenAi import chat

listener = sr.Recognizer()
player = pyttsx3.init()

def listen():
    with sr.Microphone() as input_device:
        print('iam ready to here')
        voice_content = listener.listen(input_device)
        text_input = listener.recognize_google(voice_content)
        print('input text:- ',text_input)
    return text_input    

def talk(text):
    response = chat(text)
    print('bot response:- ', response)
    player.say(response)
    player.runAndWait()    

while True:
    try:
        command = listen()
        if 'bye' in command:
            player.say("ok bye see you")
            player.runAndWait()            
            break
        talk(command.lower())    
    except:
        pass