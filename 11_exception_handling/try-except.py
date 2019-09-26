try:
    age = int(input("Age: "))
    income = float(input("Annual income: "))
    print(age)
    print(income/age)
except ValueError:
    print("Invalid number !")
except Exception:
    print("Invalid data !")
