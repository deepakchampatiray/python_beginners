def greet_user(firstName, lastName):
    print(f"Hello {firstName} {lastName} !")


greet_user('Deepak', 'Champatiray')

# Using keyword arguments
greet_user(firstName='Deepak', lastName='Champatiray')
greet_user(lastName='Champatiray', firstName='Deepak')