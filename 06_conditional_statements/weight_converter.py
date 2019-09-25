weight = input("Please enter your weight: ")
lbsOrKg = input("(L)bs or (K)g ? ")

if lbsOrKg.upper() == 'L':
    convertedWeight = float(weight) * 0.45
    convertedUnit = 'Kg'
elif lbsOrKg.upper() == 'K':
    convertedWeight = float(weight) / 0.45
    convertedUnit = 'Lbs'

print(f"You weigh {convertedWeight} {convertedUnit}")