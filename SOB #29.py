age = 30
name = 'James'

age = int(input("How old are you? "))

if age < 18:
    print("You have not reach the age requirement")
else:
    print("You are an adult capable of doing 18+ things")

name = input("What's your name? ")

if name == 'James':
    print("Welcome back, James")
else:
    print("Wrong person, Next!")
