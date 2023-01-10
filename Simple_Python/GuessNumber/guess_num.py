import random as rd
from math import sqrt

def check_snt(num):
    if num<2: return 0
    elif num==2 or num==3: return 1
    else:
        for i in range(2,int(sqrt(num))):
            if num%i==0: return i
        return 1

def set_up():
    x=int(input("Input Random number: "))
    print(f"The game: Guess a Random Number from 0 to {x}")
    print("Race Start: ")
    return int(rd.randint(1,x))

def hint(answer,count):
    temp=check_snt(int(answer))
    if temp==1 and count<=3: print("This one is Prime Number")
    elif temp>1 and count==6: print(f"It's multiples of {temp}")
    elif temp<1 and count==9: print("Oh, It's lower than 2")
    else: print("Sorry, next time")

def feed_back(user,comp):   
    if user==comp:
        checker=1
        print("You win!! Congratuation")
    elif user>comp:
        print("Higher!!, Try again")
    else:
        print("Lower!!, Try again")    
    
def game():
    result=set_up()
    answer=""
    count=0
    while answer!=result:
        answer=int(input("Your turn, let guess: "))
        feed_back(answer,result)
        count+=1
        if count%3==0 and answer!=result: 
            temp=input("Do you want some hints (y/n) ").lower()
            if (temp=="y"): hint(result,count)
        if count>9: print("Loserrrrrrrrrrrrrrrrrrrrrr")

game()


