import openai
from decouple import config

openai.api_key = config("api_key_latest2") 

def chat(input_text):
    if input_text:
        messages = [{"role": "system", "content": input_text}]
        chatbot = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chatbot.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply
    
x = chat("hiiiiiii")
print(x)    