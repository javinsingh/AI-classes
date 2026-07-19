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
print("what are your hobbies?")
hobbies = input()
print(f"Oh nice! {hobbies} is very fun isn't it!")
print("how old are you?")
age = input(int)
if age < 18:
    print(f"Nice! you are still a child, you have got a lot to learn at {age}")
elif age < 18 and age > 40:
    print(f"Nice! You are still very young at the age of {age}, but you are growing!")
elif age > 40:
    print(f"Nice! People at the age of {age} have a lot of experience!")
print(f"it was great talking to you {name}, Bye!")

