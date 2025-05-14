import random
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

motivations = [
    "Don't give up, bbonbeq!",
    "Every day is a new opportunity!",
    "Your projects have great potential.",
    "Consistency brings results – keep going!",
    "Your future is programmable :)",
    "Believe in the process, and trust yourself.",
    "Small steps every day lead to big achievements.",
    "You are improving, even if it doesn’t feel like it.",
    "Discipline beats motivation – but you’ve got both!",
]

emojis = ["💪", "🚀", "🔥", "🌟", "🎯", "📈", "🧠", "⚡", "✅"]

def show_message(count):
    message = random.choice(motivations)
    emoji = random.choice(emojis)
    color = random.choice([Fore.RED, Fore.GREEN, Fore.CYAN, Fore.MAGENTA, Fore.YELLOW])
    print(f"{color}[{count}] {message} {emoji}{Style.RESET_ALL}")

def motivation_bot():
    print(Fore.BLUE + "Motivation bot started! Press Ctrl+C to stop.\n" + Style.RESET_ALL)
    count = 1
    try:
        while True:
            show_message(count)
            time.sleep(10)
            count += 1
    except KeyboardInterrupt:
        print(Fore.RED + "\nBot stopped. Keep going, you're doing great! 💖" + Style.RESET_ALL)
        sys.exit()

if __name__ == "__main__":
    motivation_bot()
