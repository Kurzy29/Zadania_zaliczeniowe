print("'koniec' konczy operacje")

def netto():
    x = a * 1.389
    x = round(x, 2)
    print (x)

def brutto():
    x = a * 0.72
    x = round(x, 2)
    print (x)

def emeryt():
    b = a * 0.097
    print (b)

def rent():
    c = a * 0.015
    print(c)

def chor():
    d = a * 0.024
    print(d)

def zdrow():
    e = a * 0.077
    print(e)

def pit():
    f = a * 0.063
    print(f)

while True:
    x = input("Wybierz rodzaj wynagrodzenia: netto, brutto:")
    if x == 'koniec':
        break
    if x in ('netto' ,'brutto'):
        if x == 'netto':
            a = float(input("wielkość wynagrodzenia: "))
            netto()
            print ("Teraz wpisz tą kwotę w kalkulatorze brutto")
        if x == 'brutto':
            a = float(input("wielkość wynagrodzenia: "))
            brutto()
            emeryt()
            rent()
            chor()
            zdrow()
            pit()
    else:
        print("Nieprawidłowy znak operacji!")