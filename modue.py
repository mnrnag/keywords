import random
playing=True
number=str(random.randint(10,20))

print("I will generate a number from 0 to 9,and you have to gess the number one digit at a time")
print("This game ends when you get one hero")

while playing:
    guess=input("Give me your best guess\n")
    if number==guess:
        print("Youwin the game")
        print("The number was",number)
        break
    else:
        print("your guess ist quite right\n")




    
