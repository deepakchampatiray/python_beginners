numbers = [23, 34, 51, 21, 24, 35, 61, 28, 7, 24]
largest = 0
for number in numbers:
    largest = number if number > largest else largest
print(largest)
print(numbers.index(largest))