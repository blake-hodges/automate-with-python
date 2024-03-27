import sys

while (True):
    user_input = input("Type something: ")
    if user_input == 'exit':
        print("Program exiting.")
        sys.exit()
    message = "You typed '" + user_input + "'. Continue or type 'exit' to end program."
    print(message)