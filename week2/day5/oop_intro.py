#OOP = Object Oriented Programing


# classes and objects 
#how to create a class 

# class Dog:
    
#     #the constructor 
#     def __init__(self, name, color, age, is_trained = False):
#         self.name = name
#         self.color = color
#         self.age = age
#         self.is_trained = is_trained

# dog1 = Dog('Rex', 'brown', 10)
# print(dog1.name)
# print(dog1.color)
# print(dog1.age)
# print(dog1.__dict__)
# dog1.breed = 'puddle'
# print(dog1.name)
# print(dog1.breed)

# #create the second object of Dog, call it dog2

# dog2 = Dog('Moshu', 'brown', 5)
# print(dog2.is_trained)

# dog3 = Dog('Flufy', 'white', 7, True)
# print(dog3.__dict__)

# print(dog3.age)
# print(type(dog3))

#create a new attribute to the Dog class called "is_trained" the value is a boolean and the default is False
#then run the code again. What happens with the objects that were created before this new attribute was added?

#BEHAVIOURS = METHODS

#functions > methods 
#methods = functions related to a certain class


class Dog:
    
    #the constructor 
    #self = the object that will be created
    def __init__(self, name, color, age, is_trained = False):
        self.name = name
        self.color = color
        self.age = age
        self.is_trained = is_trained

    def bark(self):
        print(f'{self.name} is barking!!!')

    def run(self):
        if self.age <= 5:
            print(f"{self.name} is running really fast")
        elif self.age >= 6 and self.age <= 9:
            print(f"{self.name} is running")
        else:
            print(f"{self.name} don't want to run")

    def walk(self, meters):
        print(f'{self.name} is  walking {meters} meters')

    def rename(self, new_name):
        self.name = new_name
        return self

 
    #create a method for the Dog class called run() and if the dog's age is <= 5 print "dog's name is running really fast"
    # if the age is between 6 and 9 print "dog's name is running", otherwise print "dog's name don't want to run"

    #create a method called walk() that takes a parameter (meters: int) and prints "dog's name is walking {meters} meters"

dog1 = Dog('Rex', 'brown', 10)
dog1.bark()
dog1.run()

dog2 = Dog('Moshu', 'brown', 5)
dog2.run()

dog3 = Dog('Flufy', 'white', 7, True)
dog3.run()
Dog.run(dog3)

dog3.walk(500)
Dog.walk(dog3, 200)

dog3.rename('Xuxa')
print(dog3.name)