import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "cities": ["amsterdam", "tokyo", "new York"],
    "nature": ["alps", "himalayas", "amazon forest"],
    "beaches": ["Brazil", "calafornia", "Spain"]

}
jokes = [
    "why are programmers scared of nature? too many bugs!",
    "Why did the computer go to the doctor? Too many viruses!"
    "Why do travellers always feel warm? Because of all their hotspots!"
]

def normalise_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "Chatbot: Cities, nature or beaches?")
    preference = input(Fore.YELLOW + "You:")
    preference = normalise_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.CYAN + f"Chatbot: How about {suggestion}?")
        print(Fore.CYAN + "Chatbot: would you like that yes/no?")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes" or "yeah" or "ye":
            print(Fore.GREEN + f"Chatbot: Awesome! Enjoy your {suggestion}!")
        elif answer == "no" or "nah":
            print(Fore.RED + "Chatbot: Oh. Want me to recommend you something else?")
            recommend()
        else:
            print(Fore.RED + "Chatbot: Oh. Want me to recommend something else?")
            recommend()
    else:
        print(Fore.RED + "Chatbot: Sorry, i don't have that type of destination.")
        recommend()

def tell_joke():
    print(Fore.CYAN + f"Chatbot: {random.choice(jokes)}")

def packing_tips():
    print(Fore.CYAN + "Chatbot: Where are you going?")
    location = normalise_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "For how many days?")
    days = input(Fore.YELLOW + "You: ")
    print(Fore.CYAN + f"Chatbot: if you are going to {location} for {days} days, then i will recommend you:")
    print(Fore.CYAN + "\n- Pack versatile clothes.")
    print(Fore.CYAN + "\n- Take a charger/powerbank.")
    print(Fore.CYAN + "\n- Check the weather forecast.")

def show_help():
    print(Fore.CYAN + "\n I can:")
    print(Fore.CYAN + "\n -give you packing tips.")
    print(Fore.CYAN + "\n -Give you suggestions on where to go.")
    print(Fore.CYAN + "\n Tell jokes.")

#mainloop
def chat():
    print(Fore.CYAN + "Hello! I am a travel-based Chatbot.")
    name = input(Fore.YELLOW + "What's your name? ")
    print(Fore.CYAN + f"Hello, {name}! Nice to meet you!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}")
        user_input = normalise_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        else:
            print(Fore.RED + "Chatbot: Could you please rephrase? I don't understand what you are telling me")
            continue

if __name__ == "__main__":
    chat()

        