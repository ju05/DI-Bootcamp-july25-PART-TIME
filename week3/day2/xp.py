class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def run_speed(self):
        power = self.weight / self.age * 10
        return power

    def fight(self, other_dog:object):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f'{self.name} won the fight'
        else:
            return f'{other_dog.name} won the fight'
        
dog1 = Dog('Rex', 5, 20)
dog2 = Dog('Fluflu', 3, 12)

print(dog1.fight(dog2))