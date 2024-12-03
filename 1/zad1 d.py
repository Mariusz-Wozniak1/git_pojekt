a = int(input("podaj liczbę a"))
b = int(input("podaj liczbę b"))

if a > b:
    suma_nieparzyste = 0
else:
    suma_nieparzyste = sum(i for i in range(a, b+1) if i %2 != 0)

print(F"suma wszystkich liczb nieparzystych między {a} a {b} wynosi: {suma_nieparzyste}")