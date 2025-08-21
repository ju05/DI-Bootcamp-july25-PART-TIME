#FUNCTIONS 

# A function is a reusable block of code that runs when you “call” it. 

#Syntax

def func_name():
    '''prints a string on the console''' #doc string
    print('I am a function')


# func_name()

#create a function that prints "hello there!", then call the function to see the output

def greetings():
    '''prints a greeting in English'''
    print('Hello there!')

# greetings()

# Passing ARGUMENTS to the function
def greetings_adv(language, name):
    '''prints a greeting to a name, depending on the language'''
    if language == 'PT':
        print(f'Ola {name}, tudo bem?')

    elif language == 'ES':
        print(f'Hola {name}, que tal?')
    
    else:
        print('Unkown language')

# greetings_adv('Dolores', 'ES')

#Key word arguments
def greetings_adv(language, name):
    '''prints a greeting to a name, depending on the language'''
    if language == 'PT':
        print(f'Ola {name}, tudo bem?')

    elif language == 'ES':
        print(f'Hola {name}, que tal?')
    
    else:
        print('Unkown language')

# greetings_adv(name = 'Pedro', language = 'PT')


#Default value arguments
def greetings_adv(language = 'EN', name = 'John'):
    '''prints a greeting to a name, depending on the language'''
    if language == 'PT':
        print(f'Ola {name}, tudo bem?')

    elif language == 'ES':
        print(f'Hola {name}, que tal?')

    elif language == 'EN':
        print(f'Hi {name}, how are you?')
    
    else:
        print('Unkown language')


# greetings_adv()


#returning values from a function
def calculation(num1, num2)-> int:
    '''sums two inputed numbers'''
    result = num1 + num2
    return result

def multiply(calc)->int:
    '''takes a number and multiply by 5'''
    result = calc * 5
    return result

calc = calculation(5, 3)
print(multiply(calc))


def greetings_adv(language = 'EN', name = 'John')-> str:
    '''prints a greeting to a name, depending on the language'''
    if language == 'PT':
        return f'Ola {name}, tudo bem?'

    elif language == 'ES':
        return f'Hola {name}, que tal?'

    elif language == 'EN':
        return f'Hi {name}, how are you?'
    
    else:
        return 'Unkown language'


greetings_adv()

# create a function called country_info that receives a country name as argument
# and prints the capital of that country. Make the country name argument default
# Naboo (star wars planet). Its capital is Theed

def country_info(country = 'Naboo')-> str:
    '''returns the capital of a given country'''
    if country == 'Russia':
        capital = 'Moscow'
        population = 143800000
        return capital, population
    
    elif country == 'Brazil':
        capital = 'Brasilia'
        population = 211000000
        return capital, population
    elif country == 'Naboo':
        capital = 'Theed'
        population = 211000000
        return capital, population
    else:
        return 'unknown country'

print(country_info('Brazil'))

br_capital, br_pop = country_info('Brazil')
print(br_capital)
print(br_pop)




#Global and Local Scope

age = 25

def current_age():
    print(age)
    my_age = 35
    my_age += 1

current_age()

def happy_birthday():
    # global age
    # age += 1
    if age > 12:
        print('you have bat-mitzva')
        age += 1


happy_birthday()