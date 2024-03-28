import random, math
target = math.ceil(random.random() * 20)
print("I'm thinking of a number between 1 and 10.")
print("Take a guess.")

while True:
    guess = int(input("Your guess: "))
    if (guess == target):
        print("\nGood guess. You are correct!")
        break
    else:
        print("\nSorry. That isn't correct.")
        print("Do you want to guess again?")
        keep_playing = input("Press 'Enter' to continue. Type anything else and press 'Enter' to quit playing.\n")
        if (keep_playing == ""):
            continue
        else:
            break

print("Thanks for playing!")