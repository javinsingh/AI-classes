import requests

url = f"https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know, that {fact_data}?")
    else:
        print("Sorry! Can't fetch fact")

while True:
    user_input = input("Welcome to the fact machine.\n Enter 'Enter' to continue and enter q to quit")
    if user_input == 'q':
        print("Ok, bye!")
        break
    else:
        get_random_technology_fact()