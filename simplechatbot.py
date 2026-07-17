print("Hello! I am a chatbot. What's your name?")
name = input()
print(f"Hello {name}! It's nice to meet you! How are you feeling today?")
mood = input().lower()
if mood == 'good':
    print(f"That's great to hear, {name}")
elif mood == 'bad':
    print("oh that's not good. Can i make you feel better?")
elif mood == ' ':
    print("I get that. Sometimes feelings can't be put in words.")
else:
    print("im not sure what you are telling me.")
print(f"it was great talking to you {name}, Bye!")

