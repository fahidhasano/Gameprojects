from random import randint

c= int(input("Guess a number between 1 to 5:"))
d=randint(1,5)
if (c==d):
    print("You're winner!! Chicken dinner")
else:
    print("You lose\nThe number is:",d)







