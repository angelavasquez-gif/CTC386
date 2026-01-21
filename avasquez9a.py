#Angela Vasquez
#GitHub test comment

#User will choose 1 of 3 options from a menu.

def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    print("The temperature in Celsius is", celsius)

name = input("Enter your name.")

print("Menu")
print("-------------------")
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
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

if(option == 5):
    fahrenheit_to_celsius()

