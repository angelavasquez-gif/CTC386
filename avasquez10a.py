#Angela Vasquez
#lab 10 (Final Project)

#User will choose 1 of 6 options from a menu.

#function definitions

def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    print("The temperature in Celsius is", celsius)

def boost_energy(level):
    return level * level

#main program portion

name = input("Enter your name.")

print("Menu")
print("-------------------")
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("Option 6")
print("-------------------")

print("Hello " , name)

option = float(input("What option would you like to choose?"))

if(option == 1):
    print("How do you make a tissue dance? Put a little boogie in it!")

if(option ==2):
    print("What is your name?")

    for i in range(15):
        print(name)

if(option == 3):
    x = int(input("Enter the number of times you would like an inspirational quote."))

    for h in range(x):
        print("You're only given on little spark of madness. You mustn't lose it.-Robin Williams")

if(option == 4):

    x = 0

    while(x != 33):
        x = int(input("Guess a number between 0 and 100 inclusive."))

        while(x < 0) or (x > 100):
            print("Please enter a number within the range 0 to 100.")
            x = int(input("Guess a number between 0 and 100 inclusive: "))

        if(x < 33):
            print("Your number is too low. Guess again.")
        elif(x > 33):
            print("Your number is too high. Guess again.")
        else:
            print("You won! You are amazing!", x)

if(option == 5):
    fahrenheit_to_celsius()

if(option == 6):

    choice = "y"

    print("Welcome to the Tired Teacher Energy Booster Machine!")

    while choice == "y": 
        energy = int(input("Enter the teacher's current energy level as a number between 1 and 10: "))
        boosted = boost_energy(energy)

        print("After coffee and chocolate, the teacher's energy is now:", boosted)

        choice = input("Would you like to give more coffee and chocolate? (y/n): ")

        if choice != "y":
            print("Thanks for supporting teachers! You have saved the day!!")
