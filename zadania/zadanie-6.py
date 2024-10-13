
# tutaj mamy pobieranie danych
pierwsza = float(input("Liczba 1:"))
druga = float(input("Liczba 2:"))

if pierwsza < 0 and druga < 0:
    print("sorka, ale nie można tak obie ujemne")
    exit()

if pierwsza < 0:
    pierwsza = abs(pierwsza)

if druga < 0:
    pierwsza = abs(druga)


# tutaj drukujemy wyniki
print(f"suma: {pierwsza + druga}")
print(f"różnica: {pierwsza - druga}")
print(f"iloczyn: {pierwsza / druga}")
print(f"kwadrat pierwszej: {pierwsza**2}")
print(f"kwadrat drugiej: {druga**2}")
print(f"pierwiastek pierwszej: {pierwsza**.5}")
print(f"pierwiastek drugiej: {druga**.5}")


# tutaj wieloliniowy kometarz
"""
Ciekawostka: Python ma najbrzydsze wieloliniowe komentarze
nie wiem jak ludzie je używają
po prostu kilka jednoliniowych jest dużo estetyczniejsze
"""

if pierwsza * druga == 10:
    print("Yay!")