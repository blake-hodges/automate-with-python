name = ''
while not name:
    print("Welcome! Please enter your name:")
    name = input()
    question = f"Hello {name}. How many guests will you have tonight?"
    print(question)
number_of_guests = input()
if number_of_guests:
    message = f"We will be sure to have enough room for all {number_of_guests} guests!"
    print(message)
print('Thank you!')