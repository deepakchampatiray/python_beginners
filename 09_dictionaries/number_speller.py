phone = input("Please type your phone number: ")
spellKeys = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

spelledOut = ""
for num in phone:
    spelledOut += (spellKeys[num] + " ")
print(spelledOut)
