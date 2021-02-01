x = input("Podaj zarobki brutto")

emerytalne = float(x)*0.0976
rentowe = float(x)*0.065
wypadkowe = float(x)*0.0167
fp = float(x)*0.0245
FGSP = float(x)*0.001

print("Emerytalne",emerytalne)
print("Rentowe: ",float(rentowe))
print("Wypadkowe: ",float(wypadkowe))
print("FP: ",float(fp))
print("FGSP: ",float(FGSP))

suma = emerytalne + rentowe + wypadkowe + fp + FGSP

print("Twój pracodawa przy pensji ",x,"zł. Płaci w sumie ",suma,"zł")
