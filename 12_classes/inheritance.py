class Mammal:
    def __init__(self, species):
        self.species = species

    def walk(self):
        print('walk ' + self.species)


class Dog(Mammal):
    def __init__(self, breed):
        super().__init__('Dog')
        self.breed = breed

    def bark(self):
        print('bark ' + self.breed)

    def fetch(self):
        self.walk();
        print('collect')


class Cat(Mammal):
    def purr(self):
        print('purr')


dog1 = Dog('Hound');
dog1.bark();
dog1.fetch();