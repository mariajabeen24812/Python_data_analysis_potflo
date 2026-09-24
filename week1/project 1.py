 #create a sanke water gun game
'''
snake = -1
water = 1
gun = 0

'''
import random


print("--------------------------------SNAKE WATER GUN GAME---------------------------------")
count = int (input(" Enter how many time you want to play : " ))

for el in range(1,count+1):
    computer = random.choice([1,-1,0])
    you = input("Enter you choice(s,w,g) for snake water game : ").lower()
    if you == 's' or   you =='g' or you =='w' :
        you_dict = {"s" : -1 ,"w" : 1,"g" : 0}
        reverse_dict = {-1 : "snake", 1 :" water",0 : "gun" }
        you = you_dict[you]
        print(f"you entered {reverse_dict[you]} \ncomputer enered {reverse_dict[computer]}")


        if you== computer:
            print("Bro its Draw!")
        else:
            if computer == -1 and you == 1:
                print(" Bro you loss")
            elif computer == -1 and you == 0:
                print(" Bro you WIN")
            elif computer == 1 and you == -1:
                print(" Bro you WIN")
            elif computer == 1 and you == 0:
                print(" Bro you loss")
            elif computer == 0 and you == 1:
                print(" Bro you WIN")
            elif computer == 0 and you == -1:
                print(" Bro you loss")
            else:
                print("something want wronge")
    else :
        print("You enter a invalid letter\nlet clear the terms.\n s for snake. \n g for gun.\nw for water")
        num = input("if you want to see the game rule than press y otherwise press n : ")
        if "Y" == num or "y"== num :
            print("Game Rules\n👉 Snake → Water ko harata hai\n👉 Water → Gun ko harata hai\n👉 Gun → Snake ko harata hai ")
        else:
            print("okay!")
   


