while True:
    print("Who are you?")
    name = input()
    if name != 'Joe':
        continue
    print("Hey Joe. What's the password? (Hint: It's a fish.)")
    password = input()
    if password == "swordfish":
        break
print("Access granted.")

