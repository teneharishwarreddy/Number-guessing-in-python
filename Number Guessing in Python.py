import random
import math
guess_number = (random.randint(1,100))
x = True
t = 0
print("Guess the number between 1-100 !!!\n")
while x:
    try :
     t=t+1
     your_number = int(input("Enter your number :"))
     if guess_number == your_number :
      print ("WINNER WINNER CHICKEN DINNER !!\nYour GUESS is Correct : " +str(your_number))
      x = False
     elif guess_number >= your_number :
      print("Your number is Smaller\n")
     elif guess_number <= your_number :
      print("Your number is Bigger\n")
    except ValueError :
     print("This is not a integer")
