import time

gold=0
apples=0
def start():
    print ("Hello and welcome!")
    name = input("Whats your name:")
    print ("welcome, "+name+"!")
    print ("The objective of this game is to collect apples.")
    print ("After collecting the apples you will sell them.")
    choice = input("Do you want to play Y/N? ")
    if choice.upper() == "Y":
        begin()
    if choice.upper() == "N":
        print ("Okay, bye...")
        

def begin():
    global apples
    global gold
    print ("Let's get started!")

    if gold > 99:
        print ("You've Won the game!")
        play = input("Do you want to play again?")
        if play.upper() == "Y":
            gold=0
            apples=0
            begin()
        if play.upper() == "N":
            print ("congrats again! ")
    pick = input("Do you want to pick an apple Y/N? ")             
            
    if pick.upper() == "Y":
        time.sleep(1)
        print ("You pick an apple.")
        apples=apples+1
        print("You currently have, " +str(apples)+ " apples")
        begin()
    if pick.upper() == "N":
        sell = input("Do you want to sell your apples Y/N?")
        if sell.upper() == "Y":
            print ("You currently have, " +str(apples)+ " apples")
            print ("You've have sold your apples.")
            gold=apples*10
            apples=0
            print ("Your gold is now: ",gold)
            begin()
    
start()
