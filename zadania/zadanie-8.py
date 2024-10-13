import random

random.seed(781) # Tak żeby pasowało do tej choinki z zadania :)

dlugosc = int(input("Jak wysoka ma być choinka?: "))

for i in range(dlugosc):
    grubosc = i * 2 + 1
    bombka = random.randrange(0, grubosc)
    def genchar(k):
        if i == 0:
            return "X"
        if k == bombka:
            return "o"
        return "*"

    print(f"{" " * (dlugosc - 1 - i)}{"".join(map(genchar, range(grubosc)))}")

print(f"{" " * (dlugosc - 1)}U")