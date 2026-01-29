#Angela Vasquez
#Final Exam

#User will enter a number in order to receive a "Happy New Year!"

#function definitions

def celebrate(count): 
    for i in range(count):
        print("Happy New Year!")

num = int(input("Enter a number between 1 and 10: "))

celebrate(num)
