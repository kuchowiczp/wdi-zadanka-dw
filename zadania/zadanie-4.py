# imię, nazwisko, wiek, ulubioną potrawę, ulubione zwierzę, wynik dzielenia 5 przez 7


# a
print("Piotr")
print("Kuchowicz")
print("19")
print("Pad thai")
print("Cerberus")
for i in [1, 3, 5, 10]:
    print(f"{{:.{i}f}}".format(5/7))

# b

print("Piotr "
    + "Kuchowicz "
    + "19 "
    + "Pad thai "
    + "Cerberus "
    + " ".join([f"{{:.{i}f}}".format(5/7) for i in [1,3,5,10]])
)

# d

imie = "Piotr"
nazwisko = "Kuchowicz"
wiek = "19"
ulubiona_potrawa = "Pad thai"
piesek = "Cerberus"
numerki =  " ".join([f"{{:.{i}f}}".format(5/7) for i in [1,3,5,10]])


print(imie)
print(nazwisko)
print(wiek)
print(ulubiona_potrawa)
print(piesek)
print(numerki)

print(" ".join([
    imie,
    nazwisko,
    wiek,
    ulubiona_potrawa,
    piesek,
    numerki
]))