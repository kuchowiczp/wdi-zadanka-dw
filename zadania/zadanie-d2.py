# Zadanie 15.
# Wykorzystując odwzrowanie słowników stwórz słowniki, w którym kluczami 
# są kolejne liczby pierwsze a wartościami liczba znaków potrzebnych do 
# zaprezentowania tych liczb w systemie dwójkowym, ósemkowym i szesnastkowym 
# (w zależności od wyboru użytkownika). Na koniec stwórz słownik, który przechowuje 
# informację o tym, ile liczb wymagających konkretnej liczby znaków (w danym systemie) jest. 

def num_system_prompt() -> int:
    system = int(input("W jakim systemie? dwójkowym, ósemkowym i szesnastkowym? (2/8/16) "))

    if system not in [2,8,16]:
        print("Błędny system!")
        return system()
    return system

def num_prime_amount_prompt() -> int:
    num = input("Ile liczb pierwszych? (100) ").strip()

    if num == "":
        return 100
    else:
        return int(num)

def primes(limit) -> list[int]:
    pierwsze = list(range(2, limit))
    i = 2
    while i <= limit**(1/2):
        if i in pierwsze:
            for j in range(i * 2, limit, i):
                if j in pierwsze:
                    pierwsze.remove(j)
        i = i + 1
    return(pierwsze)

def to_base(n, base):
    return to_base(n // base, base) + str(n % base) if n > 0 else ''

base =  num_system_prompt()
amount = num_prime_amount_prompt()

lengths = { n:len(to_base(n, base)) for n in primes(amount) }

amount_per_length ={ n:len(list(filter(lambda val: val == n, lengths.values()))) for n in range(min(lengths.values()),max(lengths.values())) }


print("\n numer: długość w systemie:")
print(lengths)
print("\n długość: ile liczb pierwszych w zakresie:")
print(amount_per_length)