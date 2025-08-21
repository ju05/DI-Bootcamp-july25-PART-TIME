# # A movie theater charges different ticket prices depending on a person’s age.
# # if a person is under the age of 3, the ticket is free.
# # if they are between 3 and 12, the ticket is $10.
# # if they are over the age of 12, the ticket is $15.
# # Ask a family the age of each person who wants a ticket.
# # Store the total cost of all the family’s tickets and print it out.



ticket_cost = 0

while True:
    age = input('Enter the age of the person or "done" to finish:')
    if age == 'done' or age == '':
        break
    elif int(age) < 3:
        print('this age is free')
        continue
    elif int(age) >=3 and int(age) <=12:
        print('this age is 10 dollars')
        ticket_cost += 10
    else:
        print('this age is 15 dollars')
        ticket_cost += 15

print(ticket_cost)

#game example

#flag
winner = False

while not winner:
    postion = input('enter the position between 1 to 9')




