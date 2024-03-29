import random, math
target = math.ceil(random.random() * 20)
print("I'm thinking of a number between 1 and 10.")
print("Take a guess.")

#add list of previous guesses
#add way for user to choose which numbers to start with

while True:
    user_input = input("Your guess: ")
    if user_input == 'exit':
        break
    if not user_input.isdigit():
        print("\nPlease enter a digit between 1 and 20.")
        continue
    guess = int(user_input)
    if guess == target:
        print("\nGood guess. You are correct!")
        break
    elif guess > target:
        print("\nYour guess was too high.")
    elif guess < target:
        print("\nYour guess was too low.")
    print("Continue guessing or enter 'exit' to quit playing.")

print("Thanks for playing!")