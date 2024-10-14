import random


def get_numbers():
    args = list(map(lambda i: float(input(f"Cyfra {i+1}: ")), range(2)))
    return lambda op: op(*args)

def get_operation():
    print(f"dostępne operacje: {", ".join(operations.keys())}")
    return operations[input("Wybierz operacje: ")]

operations = {
    "+": lambda x, y : x + y,
    "-": lambda x, y : x - y,
    "*": lambda x, y : x * y,
    "/": lambda x, y : x / y,
    "#": lambda x, y : x ** (1 / y),
    "^": lambda x, y : x ** y,
    "x": lambda x, y : random.randrange(int(x), int(y))
}

while True:
    if input(
        f"wynik to: {get_numbers()(get_operation())}\n" +
        "Czy chcesz wprowadzić nowe dane? T/N: "
    ).upper() == "N":
        exit()

