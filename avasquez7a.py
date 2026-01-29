#Angela Vasquez
#lab Final Exam

#User will choose 1 of 4 options from a menu. 

name = input("Enter your name.")

print("Menu")
print("-------------------")
print("Option 1")
print("Option 2")
print("Option 3")
print("___________________")


print("Hello " , name)

option = float(input("What option would you like to choose?"))

if(option == 1):
    print("How do you make a tissue dance? Put a little boogie in it!" , name)

if(option ==2):

    food = input("Enter your favorite food.")

    print("What is your favorite food?")

    for i in range(20):
        print(food)

if(option == 3):

    x = -1

    while(x != 0):
        x = int(input("Guess a number between -10 and 10 inclusive."))
            
        while(x < -10) or (x > 10):
            print("Please enter a number within the range -10 to 10.")
            x = int(input("Guess a number between 0 and 100 inclusive: "))

        if(x < 0):
            print("Your number is too low. Guess again.")
        elif(x > 0):
            print("Your number is too high. Guess again.")
        else:
            print("You won! You are amazing!", x)
            
