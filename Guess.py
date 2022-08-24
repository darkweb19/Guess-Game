import random

counter = 0 
choice =random.randint(0,99)
print("You have 10 number of tries for Guesssing the Answer.....START>>>>")


n = int(input("Enter your inital Guess : "))
while(counter < 10):
    if(n == choice) :
        print("Correct")
        break
    elif(n < choice) :
        n = int(input("Guess Higher :"))
    elif (n > choice) :
        n = int(input("Guess Lower :"))

    counter += 1

if counter == 10 :
    print("Oopppsie.... YOU LOST.....")
    print("The number was : " , choice)

print("Number of tries  : ", counter)
