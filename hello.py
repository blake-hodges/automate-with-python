print("Hello there!")
print("What is your name?")
name = input("Your name: ")
hello_message = "Hello " + name + "!"
print(hello_message)
print("How old are you?")
age_str = input("Your age: ")
age_int = int(age_str)
next_year_int = age_int + 1
next_year_str = str(next_year_int)
age_message = "If you are " + age_str + ", then you will be " + next_year_str + " in a year."
print(age_message)