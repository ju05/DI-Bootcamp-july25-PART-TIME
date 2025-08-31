from datetime import datetime as dt, date
from faker import Faker

class Person:

    id_number = 1

    def __init__(self, name, last_name, birth_date):
        self.name = self.format_name(name)
        self.last_name = self.format_name(last_name)
        self.birth_date = self.parse_birthdate(birth_date)
        Person.id_number += 1
        self._email = None #protected attribute

    @staticmethod
    def parse_birthdate(date_str):
        return dt.strptime(date_str, '%d-%m-%Y').date()
    
    @staticmethod
    def format_name(name):
        return name.capitalize()
        
    @classmethod
    def from_age(cls, name, last_name, age):
        current_year = dt.today().year
        birth_year = current_year - age
        birth_date = f'1-1-{birth_year}'
        return cls(name, last_name,birth_date)
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age
    
    @property
    def email(self):
        return self._email


    @email.setter
    def email(self, new_email):
        self._email = new_email.lower()


    def __str__(self):
        return f'\n name: {self.name} \n last_name: {self.last_name} \n age: {self.age}'
    
    def __repr__(self):
        return f'{self.__dict__}'
    
    def __lt__(self, other):
        return self.age < other.age 
    
    def __eq__(self, other):
        return self.age == other.age 


p1 = Person('jon', 'snow', '21-08-1990')
print(type(p1.age))
# print(p1)

p2 = Person.from_age('Arya', 'stark', 18)
p3 = Person.from_age('Lisa', 'stark', 18)
# print(p2.birth_date)

print(p2 == p3)

# print(p1.age)
# p2 = Person('John', 'Doe', '01-05-1990')
# print(Person.id_number)



# create a static method that format the name and last name 
# in case the first letter is not upper case. 
# check that it works:
# print(Person.format_name('lise'))

#create a property method that generates an gmail with initial of the first name. a dot and last name complete
# print(p1.email)

p2.email = 'the.choosen@gmail.com'
print(p2.email)

#if we want this to work we need a setter

#Modules - Faker
fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
birth_date = dt.strftime(fake.date_of_birth(), '%d-%m-%Y')
print(first_name)

p4 = Person(first_name, last_name, birth_date)
print(p4.age)