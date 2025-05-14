import random
import time
import sys

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
    print(f"[{count}] {message} {emoji}")

def motivation_bot():
    print("Motivation bot started! Press Ctrl+C to stop.\n")
    count = 1
    try:
        while True:
            show_message(count)
            time.sleep(10)
            count += 1
    except KeyboardInterrupt:
        print("\nBot stopped. Keep going, you're doing great! 💖")
        sys.exit()

if __name__ == "__main__":
    motivation_bot()
