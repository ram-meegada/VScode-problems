import speech_recognition as sr
import pyttsx3
import wikipedia
from chatbot import chatbot_func, train_data

listener = sr.Recognizer()
player = pyttsx3.init()

def listen():
    with sr.Microphone() as input_device:
        print('iam ready to here')
        voice_content = listener.listen(input_device)
        text_input = listener.recognize_google(voice_content)
        print(text_input)
    return text_input    

def talk(text):
    x = chatbot_func(text, training[0], training[1], training[2], training[3])
    player.say(x)
    player.runAndWait()    

training = train_data()
while True:
    try:
        command = listen()
        if command == 'stop':
            player.say("see you")
            player.runAndWait()            
            break
        talk(command)    
    except:
        pass