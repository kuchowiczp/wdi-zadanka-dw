# Zadanie 1.
# Napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.


# bez tej kluczowej optymalizacji program wykonuje się przez aż 0.6s
# przy obsłudze klientów na skale światową jest to straszny bottleneck
# Gdyby google postanowł wyświetlać liczby z ciągu fibonacziego
# puki nie osiągnie miliona dla każdego klienta, wymagało by to aż
# 1425600 CPU*h pracy na procesorze klasy Intel Xeon Platinum 8370C
# co skutkowało by wydzieleniem 2490 kg CO2 do atmosfery!
# dzięki optymalizacji, wykonanie programu trwa tylko 0.02s, co 
# skutkuje uratowanymi drzewami i możlwością napisania na stronie
# że dzięki innowacji naszej firmy oszczędzamy ileśtam CO2 🌳
def zkaszowane(func):
    cache = {}
    def wykonywalna(i:int):
        if i in cache.keys():
            return cache[i]
        else:
            cache[i] = func(i)
            return wykonywalna(i)
    return wykonywalna

@zkaszowane
def fajbonaczi(i: int) -> int:
    return fajbonaczi(i-1) + fajbonaczi(i-2) if i > 1 else [0,1][i]


def enterprice_iterative_printer_service(callable, limit):
    i = 0
    while True:
        value = callable(i)
        if value >= limit:
            return
        print(f"{i} element: {value}")
        i+=1


enterprice_iterative_printer_service(fajbonaczi, 1_000_000)