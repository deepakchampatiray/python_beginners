numbers = [23, 34, 51, 21, 24, 35, 61, 28, 7, 24];
deDup = [];
for num in numbers:
    if not(num in deDup):
        deDup.append(num)
numbers = deDup
print(numbers)