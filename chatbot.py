import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN} Welcome to the spy game!{Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA} Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "mystery agent"

conversation_history = []

print(f"\n {Fore.CYAN} hello agent {user_name} !")
print(f"Type a sentence and i will detect it's setiment using textblob.")
print(f"{Fore.BLUE} type reset history or exit to quit")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.GREEN} Please enter a real command. {Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print(f"{Fore.BLUE} Bye agent, see you next time.")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.BLUE} History deleted")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW} no conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} conversation history {Style.RESET_ALL}")

            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "positive":
                    color = Fore.GREEN
                    emoji = "🙂"
                elif sentiment_type == "negative":
                    color = Fore.RED
                    emoji = "😔"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                
                print(f"{idx}. {color}{emoji} {text} "
                    f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😭"

    # Store in history
    conversation_history.append((user_input, polarity, sentiment_type))

    # Print result with color, emojis, and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
        f"Polarity: {polarity:.2f}")


    
