def listaA():
    list = []
    for i in range(1, 11):
        list.append(i)
    print(list)


def listaB():
    list = []
    for i in range(0, 21, 2):
        list.append(i)
    print(list)


def listaC():
    list = []
    for i in range(1, 11):
        x = i ** 2
        list.append(x)
    print(list)


def listaD():
    list = []
    for i in range(10):
        list.append(0)
    print(list)


def listaE():
    list = []
    for i in range(5):
        list.append(0)
        list.append(1)
    print(list)


def listaF():
    list = []
    for i in range(2):
        for j in range(5):
            list.append(j)
    print(list)


def listaWA():
    list = []
    i = 0
    while i < 11:
        list.append(i)
        i += 1
    print(list)


def listaWB():
    list = []
    i = 0
    while i < 21:
        list.append(i)
        i += 2
    print(list)


def listaWC():
    list = []
    i = 0
    while i < 11:
        x = i ** 2
        list.append(x)
        i += 1
    print(list)


def listaWD():
    list = []
    i = 0
    while i < 11:
        list.append(0)
        i += 1
    print(list)


def listaWE():
    list = []
    i = 0
    while i < 6:
        list.append(0)
        list.append(1)
        i += 1
    print(list)


def listaWF():
    list = []
    i = 0
    while i < 2:
        j = 0
        i += 1
        while j < 5:
            list.append(j)
            j += 1
    print(list)


def ile_ujemnych(A):
    ujemne = 0
    for i in A:
        if i < 0:
            ujemne += 1
    print(ujemne)


def iloczyn(A):
    wynik = A[0]
    A.pop(0)
    for i in A:
        wynik *= i
    print(wynik)


def minmax(A):
    min = A[0]
    max = A[0]
    for i in A:
        if i > max:
            max = i
        if i < min:
            min = i
    minmax = (min, max)
    print(minmax)


def suma(A):
    wynik = 0
    index = 0
    for i in A:
        if index == 0 or index % 2 == 0:
            wynik += i
        else:
            wynik -= i
        index += 1
    print(wynik)


def zd7():
    list = []
    while int(len(list)) != 10:
        a = int(input("podaj liczbę: "))
        czy_niema = 0
        for i in list:
            if a == i:
                czy_niema += 1
        if czy_niema == 0:
            list.append(a)
    print(list)


def zd8():
    list = []
    for i in range(2, 10001):
        list.append(i)
    for i in list:
        for j in range(2, 101):
            if i != j and i % j == 0:
                list.remove(i)
    print(list)


def main():
    # listaWA()
    # listaWB()
    # listaWC()
    # listaWD()
    # listaWE()
    # listaWF()
    # ile_ujemnych([1,-2,3,3,-5,-7,-4])
    # iloczyn([1,2,3,4,5,6])
    # minmax([31,28,31,30,31,30,31,31,30,31,30,31])
    # suma([1,2,3,4,5,6])
    # zd7()
    zd8()


main()
