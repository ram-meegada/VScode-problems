import openai

openai.api_key = "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"

def chat(input_text):
    if input_text:
        messages = [{"role": "system", "content": input_text}]
        chatbot = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chatbot.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply