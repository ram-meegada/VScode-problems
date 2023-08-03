data = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi", "Hello", "Hey"],
            "responses": [
                "Hi there!",  
                "Hello! How can I assist you?", 
                "Hey,how can I help?"
            ],
            "options": ["Option 1", "Option 2", "Option 3"],
            "links": ["https://example.com/link1", "https://example.com/link2"]
        },
        {
            "tag": "greeting2",
            "patterns": [ "How are you?"],
            "responses": [
                "I'm fine, What about you.",
                "I'm doing well, How its going on."
            ],
            "options": ["Option 1", "Option 2", "Option 3"],
            "links": ["https://example.com/link1", "https://example.com/link2"]
        },
        {
            "tag": "fine",
            "patterns": ["i'm fine", "i'm good", "good", "i'm fine, What about you?"],
            "responses": [
                "That's great to hear"
            ]
        },
        {
            "tag": "name",
            "patterns": ["what is your name?", "who are you?"],
            "responses": [
                "My name is AI Bot",
                "Hey, i'm AI Bot. What's your name?",
                "I'm sorry, bit i dont have a name. You can call me whatever you want, through"
            ]
        },
        {
            "tag": "goodbye",
            "patterns": ["Goodbye", "See you later", "Farewell"],
            "responses": [
                "Goodbye! Have a great day!", 
                "Take care and see you soon!", 
                "Farewell!"
            ]
        },
        {
            "tag": "search",
            "patterns": ["Search for hotels", "Find flights", "Look for restaurants"],
            "responses": [
                "Sure! I can help you with that.", 
                "What specifically are you searching for?", 
                "Tell me more about your search."
            ]
        },
        {
            "tag": "weather",
            "patterns": ["What's the weather like?", "Will it rain tomorrow?", "Temperature in New York"],
            "responses": [
                "Let me check the weather for you.", 
                "Weather forecast coming right up!", 
                "The current temperature in New York is 20°C."
            ]
        },
        {
            "tag": "product_info",
            "patterns": ["Tell me about your products", "What do you offer?", "Product catalog"],
            "responses": [
                "We offer a variety of products. Can you specify what you're interested in?", 
                "Our products range from electronics to fashion.", 
                "Please check our product catalog on our website."
            ]
        },
        {
            "tag": "complaint",
            "patterns": ["I'm not satisfied with the service", "This is unacceptable", "I want to file a complaint"],
            "responses": [
                "I'm sorry to hear that. Let me escalate your concern to our support team.", 
                "We apologize for the inconvenience. Please share more details.", 
                "Your feedback is valuable to us. We will address this promptly."
            ]
        },
        {
            "tag": "booking",
            "patterns": ["Book a table", "Reserve a room", "Schedule an appointment"],
            "responses": [
                "Certainly! Please provide me with the necessary details.", 
                "Sure, I can help you make a booking.", 
                "Let's proceed with the booking process."
            ],
            "options": ["One seater", "Two seater", "Two bhk"],
            "links": ["https://example.com/link1", "https://example.com/link2"]
        },
        {
            "tag": "payment",
            "patterns": ["How can I pay?", "Accepted payment methods", "Do you accept credit cards?"],
            "responses": [
                "We accept various payment methods, including credit cards and online payments.", 
                "Credit cards, debit cards, and online transfers are accepted.", 
                "Payment options will be available during checkout."
            ]
        },
        {
            "tag": "delivery",
            "patterns": ["What are the delivery options?", "Delivery time", "Can I track my order?"],
            "responses": [
                "We offer multiple delivery options with varying delivery times.", 
                "Delivery time depends on your location and chosen delivery method.", 
                "Order tracking is available for registered customers."
            ]
        },
        {
            "tag": "contact",
            "patterns": ["How can I contact you?", "contact", "Contact information", "Phone number"],
            "responses": [
                "You can reach us at 1-800-123456 for any inquiries.", 
                "Feel free to call us at 1-800-123456."
            ]
        },
        {
            "tag": "thanks",
            "patterns": ["Thank you", "Thanks a lot"],
            "responses": [
                "You're welcome!", 
                "No problem, happy to help!", 
                "Glad I could assist you."
            ]
        }
    ]
}
# def data_func(data):
#     return data

# for i in range(1, 23, 3):
#     print(i, end=" ")
# print()
# for i in range(2, 24, 3):
#     print(i, end=" ")
# print()
# for i in range(3, 25, 3):
#     print(i, end=" ")
# print()

# num = [1,2,3]
# for i in num:
#     iterate = 0
#     while iterate <= 8:
#         print(i, end=" ")
#         i += 3
#         iterate += 1
#     print() 