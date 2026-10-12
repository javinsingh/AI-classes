import requests
def get_random_joke():
   url = "https://official-joke-api.appspot.com/random_joke"
   response = requests.get(url)

   if response.status_code == 200:
      print(f"full JSON response: {response.json()}")
      joke_data = response.json()
      return f"{joke_data['setup']} - {joke_data['punchline']}"
   else:
      return "Failed to retrieve joke"

def main():
   print("Welcome to jokes!")

   while True:
      user_input = input("Enter Enter to continue the jokes \n Enter q to stop").strip().lower()
      if user_input == "q":
         print("Alright, bye!")
         break
     
      joke = get_random_joke()
      print(joke)

if "name" == "__main__":
   main()


