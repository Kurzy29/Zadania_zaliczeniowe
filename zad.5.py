print("'koniec' konczy operacje")
print("Dostepne waluty: Baht Tajski(thb), Bitcoin(btc), Ngultrum bhutański(btn), Ugija mauretańska(mro), Ethereum(eth), Dolary amerykańskie (usd)")
def liczba():
    e=b*c
    e = round(e, 5)
    print (b, a, "to", e, d)
while True:
    x = input("Jakie waluty chcesz przeliczyc? (thb-usd, btc-usd, btn-usd, mro-usd, eth-usd): ")
    if x == 'koniec':
        break
    if x in ('thb-usd' ,'btc-usd', 'btn-usd', 'mro-usd', 'eth-usd'):
        if x == 'thb-usd':
            a = (input("Wybierz walute początkową: thb, usd:"))
            if a in ('thb', 'usd'):
                if a == 'thb':
                    d = 'usd'
                    b = float(input("Podaj ilosc waluty: "))
                    c = 0.033
                    liczba()
                elif a == 'usd':
                    d = 'thb'
                    b = float(input("Podaj ilosc waluty: "))
                    c = 29.97
                    liczba()
        elif x == 'btc-usd':
            a = (input("Wybierz walute początkową: btc, usd:"))
            if a in ('btc', 'usd'):
                if a == 'btc':
                    d = 'usd'
                    b = float(input("Podaj ilosc waluty: "))
                    c = 34406.1
                    liczba()
                elif a == 'usd':
                    d = 'btc'
                    b = float(input("Podaj ilosc waluty: "))
                    c = 0.000029
                    liczba()
        elif x == 'btn-usd':
            a = (input("Wybierz walute początkową: btn, usd:"))
            if a in ('btn', 'usd'):
                if a == 'btn':
                    d = 'usd'
                    b = float(input("Podaj ilosc waluty: "))
                    c = 0.014
                    liczba()
                elif a == 'usd':
                    d = 'btn'
                    b = float(input("Podaj ilosc waluty: "))
                    c = 72.91
                    liczba()
        elif x == 'mro-usd':
            a = (input("Wybierz walute początkową: mro, usd:"))
            if a in ('mro', 'usd'):
                if a == 'mro':
                    d = 'usd'
                    b = float(input("Podaj ilosc waluty: "))
                    c = 0.028
                    liczba()
                elif a == 'usd':
                    d = 'mro'
                    b = float(input("Podaj ilosc waluty: "))
                    c = 36.08
                    liczba()
        elif x == 'eth-usd':
            a = (input("Wybierz walute początkową: eth, usd:"))
            if a in ('eth', 'usd'):
                if a == 'eth':
                    d = 'usd'
                    b = float(input("Podaj ilosc waluty: "))
                    c = 1330.49
                    liczba()
                elif a == 'usd':
                    d = 'eth'
                    b = float(input("Podaj ilosc waluty: "))
                    c = 0.00075
                    liczba()
                    print()

    else:
        print("Nieprawidłowy znak ")