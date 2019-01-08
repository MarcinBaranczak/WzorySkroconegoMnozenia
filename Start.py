# ----- dwumian Newtona do łańcucha -----
def dwumianNewtonaLancuch(n):
    wynik = ""

    for i in range(n + 1):
        if 0 < i < n:
            wynik += str(dwumianNewtona(n, i))
        if n - i > 0:
            wynik += "x"
            if n - i > 1:
                wynik += "^" + str(n - i)
        if 0 < i < n:
            wynik += "*"
        if i > 0:
            wynik += "y"
            if i > 1:
                wynik += "^" + str(i)
        if i < n:
            wynik += " + "
    # end for

    return wynik


# ----- definicja dwumianu Newtona n po k -----
def dwumianNewtona(n, k):
    return int(silnia(n) / (silnia(k) * silnia(n - k)))


# ----- definicja silni -----
def silnia(wartosc):
    wynik = 1

    for x in range(1, wartosc + 1):
        wynik = wynik * x
    # end for

    return wynik


# ----- Program główny -----
print("Tworzenie wzorów skróconego mnożenia(x+y)^n za pomocą dwumianu Newtona.")
pobierzP = int(input("podaj potęgę n: "))
print("wynik: ", dwumianNewtonaLancuch(pobierzP))
