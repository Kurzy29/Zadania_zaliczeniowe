import datetime

date=str(input('Podaj date(Format:DD MM RRRR):'))
day_name= ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota','Niedziela']
day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
print("Urodziłeś się w",day_name[day])


def calcEasterDate(year):

    special_years = ['1954', '1981', '2049', '2076']
    special2 = 7
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7

    if year in special_years:
        dateofeaster = (22 + d + e) - special2
    else:
        dateofeaster = 22 + d + e
    return dateofeaster


def main():
    year = int(input("Podaj rok: "))

    if (year >= 1900) and (year <= 2099):
        dateofeaster = calcEasterDate(year)
        if dateofeaster > 31:
            print("Kwiecień {}".format(dateofeaster - 31))
        else:
            print("Marzec {}".format(dateofeaster))
    else:
        print("Błąd: Podany rok jest poza zasiegiem programu")


if __name__ == main():
    main()