zakres_od = int(input("Liczba od:"))
zakrest_do = int(input("Liczba do:")) + 1

dlugosc = zakrest_do - zakres_od

zakres = list(map(lambda a: a+zakres_od, range(dlugosc)))

for i in zakres if len(zakres) <= 20 else zakres[int(dlugosc/2)-3:int(dlugosc/2)+3]:
    print(i)