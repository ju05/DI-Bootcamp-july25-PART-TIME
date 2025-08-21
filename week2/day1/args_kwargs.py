#ARGS AND KWARGS
#ARGS = ARGUMENTS = LISTS, TUPLES, SETS
#KEY, WOKRD ARGUMENTS = DICTIONARY

students = ['Harry', 'Ron', 'Hermione']

def welcome(*args):
    print(args)
    if args:
        for name in args:
            print(f'{name}, welcome!')
    else:
        print('you didn`t pass names')

# welcome(students)
welcome('Camila', 'Niv', "Michal", 'David', 'Flavia')

def user_info(**kwargs):
    print(kwargs)
    for value in kwargs.values():
        print(value)

user_info(name = 'Juliana', email = 'ju@gmail.com', age = 35, is_online = True, pets = ['cat', 'dog'])

numbers = [
            [1,2,3],
           [4,5,6],
           [7,8,9]
           ]
print(numbers[0][1])
