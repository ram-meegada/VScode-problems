from chatbot import chatbot_func, train_data


training = train_data()
while True:
    newMessage = input("You(Type 'wrong' if i give wrong input): ").lower()
    x = chatbot_func(newMessage, training[0], training[1], training[2], training[3])
    print(x)
    