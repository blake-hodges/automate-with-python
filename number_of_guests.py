name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
number_of_guests = input()
if number_of_guests:
    print('Be sure to have enough room for all ' + number_of_guests  + ' guests!')
print('Done')