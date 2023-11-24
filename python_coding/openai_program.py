import openai

from decouple import config

openai.api_key = config("api_key_latest1")
# openai.api_key = "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"

def open_ai_chat(input_text):
    if input_text:
        messages = [{"role": "system", "content": "You are a helpful assistant that talks about food only"}]
        messages.append({"role": "user", "content": input_text})
        chatbot = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chatbot.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply
    
while True:
    input_text = input('enter:- ')    
    if input_text == "stop":
        break
    result = open_ai_chat(input_text)
    print(result) 