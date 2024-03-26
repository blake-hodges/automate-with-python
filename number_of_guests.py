name = ''
while not name:
    print("Welcome! Please enter your name:")
    name = input()
question = f"Hello {name}. How many guests will you have tonight?"
print(question)
number_of_guests = input("Number of guests: ")
if number_of_guests:
    guest_list = "GUEST LIST:\n"
    print("\nPlease enter the names of all your guests.")
    for i in range(int(number_of_guests)):
        guest = input(f"Guest {i + 1}: ")
        guest_list += guest + "\n"
    message = f"\nWe will be sure to have enough room for all {number_of_guests} guests! Here is your guest list:\n\n{guest_list}"
    print(message)
print('Thank you!')