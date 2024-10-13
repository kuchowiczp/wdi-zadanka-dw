import time
import sys
import random
from typing import Callable

random.seed(15310)
SUPER_SECRET_PIN: str = f"{random.randrange(0,9999):04d}" # oczywisty

# tak dla realizmu
separator = "-" * 20
def slow_print(text: str, speed = .03):
    sys.stdout.flush()
    for i in text:
        time.sleep(speed)
        print(i, end="")
        sys.stdout.flush()
def slow_lines(lines: list[str], speed = .3):
    for l in lines:
        time.sleep(speed)
        print(l)


def enterprise_software_runner(app_compactflash: list[(str, Callable[[int], int])]):
    account_state = 0

    print("BOOTING UP WINDOWS ENTERPRISE EMBEDDED EDITION PRO", end="")
    slow_print("."*5, .5)
    slow_lines([
        "BOOT COMPLEATED",
        separator,
        "WELCOME TO",
        "    BANK  OF  ALEXANDRIA"
    ])
    while True:
        slow_lines([
            separator,
            "DOSTĘPNE FUNKCJE: "
        ] + list(map(lambda i: f"{i[0] + 1}. {i[1][0]}", enumerate(app_compactflash))) + [
            separator,
            "Którą opcje wybrać?: "
        ])

        choice = int(input())
        if choice > 0 and choice <= len(app_compactflash):
            action = app_compactflash[choice-1]
            if action[2]:
                slow_lines([
                    separator,
                    "SECURITY PROTOCOL!",
                    "PODAJ KOD PIN: "
                ])
                pin_atempt = input()
                if pin_atempt != SUPER_SECRET_PIN:
                    slow_lines([
                        separator,
                        "INTRUDER DETECTED",
                        "BŁĘDNY PIN",
                        "CYBERATAK UDAREMNIONY",
                    ])
                    continue

            account_state = action[1](account_state)
            continue
        slow_print("." * 4, .5)
        slow_lines([
            "CRITICAL ERROR",
            "FUNKCJA NIE ZNALEZIONA"
        ])
        slow_print("." * 4, .5)
        
        
        


def wplata(stan: int) -> int:
    slow_lines([
        separator,
        "ILE CHCESZ WPLACIC?"
    ])
    amount = int(input())
    slow_lines([
        separator,
        "Wsadz banknoty do bankomatu"
    ])
    for i in range(10):
        time.sleep(.2)
        print(f"{" " * (10-i)}[=$=]{" "*10}", end="\r")
    print("")
    slow_print("." * 4, .3)
    slow_lines([
        separator,
        "WPLATA PRZYJENTA!"
    ])
    return stan + amount


def wyplata(stan: int) -> int:
    slow_lines([
        separator,
        "ILE CHCESZ WYPLACIC?"
    ])
    amount = int(input())
    slow_print("." * 4, .3)
    if stan < amount:
        slow_lines([
            separator,
            "ERROR!",
            "NIEWYSTARCZAJĄCE ŚRODKI!"
        ])
        return stan
    
    slow_lines([
        separator,
        "WYPLACANIE PIENIĘDZY",
        separator
    ])

    for i in range(10):
        time.sleep(.2)
        print(f"{" " * (i)}[=$=]", end="\r")
    print("")

    return stan - amount

def stan_konta(stan: int) -> int:
    slow_lines([
        separator,
        "Sprawdzanie stanu konta"
    ])
    slow_print("." * 10, .3)
    slow_lines([
        separator,
        F"POSIADASZ {stan} $"
    ])
    slow_print("." * 3, .4)
    return stan

def pozagnanie():
    slow_lines([
        separator,
        "  BANK  OF  ALEXANDRIA",
        "THANKS YOU FOR YOUR SERVICE",
        separator,
        " SEE YOU LATER",
        separator
    ])
    exit()


def storyline(stan):
    slow_lines([
        separator,
        "*przyglądasz się bankomatowi*",
        "*jest duży i niebieski, wbudowany w ściane obok biedronki*",
        "*nad bankomatem widnieje napis \"BANK OF ALEXANDRIA! Wypłaty bez prowizji\"*"
    ], 1.2)
    time.sleep(4)
    print("""
   /----------\\
   |  .....   |
   |  .....   |
   |__________|
  /  [][][]  /|
 / [][][]   / |
|----------/  |
|          |  |
|          |  |
|----------|-/                  
""")
    time.sleep(1)
    return stan


enterprise_software_runner([
    ("Wplata na konto", wplata, True),
    ("Wypłać pieniądze", wyplata, True),
    ("Sprawdź saldo konta", stan_konta, True),
    ("Przyjrzyj się bankomatowi", storyline, False),
    ("Odejdż od bankomatu", lambda _: pozagnanie(), False)
])