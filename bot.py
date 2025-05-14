import random
import time

motywacje = [
    "Nie poddawaj się, bbonbeq!",
    "Każdy dzień to nowa szansa!",
    "Twoje projekty mają potencjał.",
    "Działaj codziennie, efekty przyjdą.",
    "Twoja przyszłość jest programowalna :)",
]

def uruchom_bota():
    print("Bot motywacyjny uruchomiony!")
    while True:
        wiadomosc = random.choice(motywacje)
        print(wiadomosc)
        time.sleep(10)  # co 10 sekund

if __name__ == "__main__":
    uruchom_bota()
