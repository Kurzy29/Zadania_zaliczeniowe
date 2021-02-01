def CelFar(cel):
    wynik = float(cel)*1.8+32
    print(wynik)
    if wynik>=212:
        print("Woda w tej temperaturze wrze")
    elif wynik<=32:
        print("Woda zamarza w tej temperaturze")
    return wynik

def FarCel(Far):
    wynik = (float(Far)-32)/1.8
    print(wynik)
    if wynik>=100:
        print("Woda w tej temperaturze wrze")
    elif wynik<=0:
        print("Woda zamarza w tej temperaturze")
    return wynik

def CelKel(Cel):
    wynik = float(Cel)+273.15
    print(wynik)
    if wynik>=373:
        print("Woda w tej temperaturze wrze")
    elif wynik<=273:
        print("Woda zamarza w tej temperaturze")
    return wynik

def KelCel(Kel):
    wynik = float(Kel)-273.15
    print(wynik)
    if wynik>=100:
        print("Woda w tej temperaturze wrze")
    elif wynik<=0:
        print("Woda zamarza w tej temperaturze")
    return wynik

def KelFar(Kel):
    wynik= (float(Kel)-273.15)*1.8
    print(wynik)
    if wynik>=212:
        print("Woda w tej temperaturze wrze")
    elif wynik<=32:
        print("Woda zamarza w tej temperaturze")
    return wynik

def FarKel(Far):
    wynik = (float(Far)-32)/1.8
    print(wynik)
    if wynik>=373:
        print("Woda w tej temperaturze wrze")
    elif wynik<=273:
        print("Woda zamarza w tej temperaturze")
    return wynik

print("Wybierz konwersje: ")
print("1 - Cel -> Far ")
print("2 - Far -> Cel ")
print("3 - Cel -> Kel ")
print("4 - Kel -> Cel ")
print("5 - Kel -> Far ")
print("6 - Far -> Kel ")

op = input("Wybierz opcje: ")

if op == "1":
    Cel = input("Podaj liczbe stopni")
    CelFar(Cel)
elif op == "2":
    Far = input("Podaj liczbę stopni")
    FarCel(Far)
elif op == "3":
    Cel = input("Podaj liczbę stopni")
    CelKel(Cel)
elif op == "4":
    Kel = input("Podaj liczbę stopni")
    KelCel(Kel)
elif op == "5":
    Kel = input("Podaj liczbę stopni")
    KelFar(Kel)
elif op == "6":
    Far = input("Podaj liczbę stopni")
    FarKel(Far)
else:
    print("Zakres programu obejmuje liczby 1-6")