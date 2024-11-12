# Zadanie 2.
# Proszę napisać program wczytujący dwie macierze o ustalonych wymiarach m×n. 
# Dla wczytanych macierzy należy wykonać operacje: iloczynu dwóch macierzy oraz
# mnożenia przez skalar każdej z tych macierzy, gdzie skalar jest sumą wyznaczników
# wczytanych macierzy. Wymiar macierzy powinien być definiowany przez użytkownika. 

def print_matrix(matrix) -> str:
    def innergen():
        max_width = max(len(f"{item:.2f}") for row in matrix for item in row)
        
        for row in matrix:
            formatted_row = " | ".join(f"{item:.2f}".rjust(max_width) for item in row)
            yield f"| {formatted_row} |\n"
    return ''.join(innergen())

def float_prompt(x,y)->float:
    text = input(f"Podaj liczbe na miejsce [{x}, {y}]: ")
    try:
        num = float(text)
        return num
    except ValueError:
        print(f"Error!")
        return float_prompt(x,y)

def matrix_prompt()->list[list[float]]:
    rows = int(input("Podaj liczbę wierszy: "))
    cols = int(input("Podaj liczbę kolumn: "))
    return [[float_prompt(x,y) for y in range(cols)] for x in range(rows)]

def matrix_product(m1, m2) -> float:
    rows_m1 = len(m1)
    cols_m1 = len(m1[0])
    rows_m2 = len(m2)
    cols_m2 = len(m2[0])

    if cols_m1 != rows_m2:
        raise ValueError

    fin = [[0 for _ in range(cols_m2)] for _ in range(rows_m1)]

    for i in range(rows_m1):
        for j in range(cols_m2):
            for k in range(cols_m1):
                fin[i][j] += m1[i][k] * m2[k][j]

    return fin

print("Macierz 1:")
mat1 = matrix_prompt()


print("Macierz 2:")
mat2 = matrix_prompt()

try:
    print(f"Iloczyn: \n{print_matrix(matrix_product(mat1, mat2))}")
except ValueError:
    print("Macierzenie nie są wymnarzalne")



if len(mat1) != len(mat1[0]):
    print("Macierz 1 nie ma wyznacznika")
    exit()
if len(mat2) != len(mat2[0]):
    print("Macierz 2 nie ma wyznacznika")
    exit()
    


def determinant(mat) -> float:
    n = len(mat)
    if n == 1:
        return mat[0,0]
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    return sum([((-1) ** col) * mat[0][col] * determinant([row[:col] + row[col+1:] for row in mat[1:]]) for col in range(n)])

ska = determinant(mat1) + determinant(mat2)

def multiplied_matrix_rutine(no,mat):
    print(f"\nPomnorzony Macierz {no}:\n{print_matrix([[col * ska for col in row] for row in mat])}")

multiplied_matrix_rutine(1, mat1)
multiplied_matrix_rutine(2, mat2)