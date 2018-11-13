Coins = 10000
import time
import random

print("Type 'Gamble()' to gamble.")

def Gamble():
    global Coins

    print("Welcome to the daily horse race!")
    time.sleep(1.5)
    print("Everyone is placing their bets now!")
    time.sleep(1.5)
    print("How much would you like to bet? You have",Coins,"coins.")
    Bet = int(input(""))

    while Bet > Coins:
        print("You don't have enough money for that bet.")
        time.sleep(1.5)
        print("How much would you like to bet? You have",Coins,"coins.")
        Bet = int(input(""))

    Coins = Coins - Bet
    print("Now what horse would you like to bet on? Here are your chances:")
    print("")
    HO = random.randint(3,5)
    print("Horse 1:",HO,"/ 1")
    HT = random.randint(2,8)
    print("Horse 2:",HT,"/ 1")
    HTH = random.randint(4,10)
    print("Horse 3:",HTH,"/ 1")
    HF = random.randint(8,14)
    print("Horse 4:",HF,"/ 1")
    Horse = int(input(""))

    print("Great! Looks like the riders are in their docks. Get ready!")
    time.sleep(2.5)
    Distance = random.randint(2,10)
    print("Distance is",Distance*50,"meters")
    time.sleep(1.5)
    print("RIDERS ON YOUR MARKS")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!")

    time.sleep(2)
    LeadHorse = 0

    while LeadHorse == 0:
        if random.randint(1,HF) == 1:
            LeadHorse = 4
        elif random.randint(1,HTH) == 1:
            LeadHorse = 3
        elif random.randint(1,HT) == 1:
            LeadHorse = 2
        elif random.randint(1,HO) == 1:
            LeadHorse = 1 
                
    for Counter in range(1,Distance+1):
        print("Horse",LeadHorse,"is in the lead!")

        if random.randint(1,5) == 1:
            Loop = 1
            while Loop == 1:
                if random.randint(1,HF) == 1 and LeadHorse != 4:
                    SecondHorse = 4
                    time.sleep(1.5)
                    print("Horse",SecondHorse,"has overtaken Horse "+str(LeadHorse)+"!")
                    X = LeadHorse
                    LeadHorse = SecondHorse
                    SecondHorse = X
                    X = 0
                    Loop = 0

                elif random.randint(1,HTH) == 1 and LeadHorse != 3:
                    SecondHorse = 3
                    time.sleep(1.5)
                    print("Horse",SecondHorse,"has overtaken Horse "+str(LeadHorse)+"!")
                    X = LeadHorse
                    LeadHorse = SecondHorse
                    SecondHorse = X
                    X = 0
                    Loop = 0

                elif random.randint(1,HT) == 1 and LeadHorse != 2:
                    SecondHorse = 2
                    time.sleep(1.5)
                    print("Horse",SecondHorse,"has overtaken Horse "+str(LeadHorse)+"!")
                    X = LeadHorse
                    LeadHorse = SecondHorse
                    SecondHorse = X
                    X = 0
                    Loop = 0

                elif random.randint(1,HO) == 1 and LeadHorse != 1:
                    SecondHorse = 1
                    time.sleep(1.5)
                    print("Horse",SecondHorse,"has overtaken Horse "+str(LeadHorse)+"!")
                    X = LeadHorse
                    LeadHorse = SecondHorse
                    SecondHorse = X
                    X = 0
                    Loop = 0

        else:
            if random.randint(1,HF) == 1 and LeadHorse != 4:
                SecondHorse = 4
                time.sleep(1.5)
                print("Horse",SecondHorse,"has overtaken Horse "+str(LeadHorse)+"!")
                X = LeadHorse
                LeadHorse = SecondHorse
                SecondHorse = X
                X = 0

            elif random.randint(1,HTH) == 1 and LeadHorse != 3:
                SecondHorse = 3
                time.sleep(1.5)
                print("Horse",SecondHorse,"has overtaken Horse "+str(LeadHorse)+"!")
                X = LeadHorse
                LeadHorse = SecondHorse
                SecondHorse = X
                X = 0

            elif random.randint(1,HT) == 1 and LeadHorse != 2:
                SecondHorse = 2
                time.sleep(1.5)
                print("Horse",SecondHorse,"has overtaken Horse "+str(LeadHorse)+"!")
                X = LeadHorse
                LeadHorse = SecondHorse
                SecondHorse = X
                X = 0

            elif random.randint(1,HO) == 1 and LeadHorse != 1:
                SecondHorse = 1
                time.sleep(1.5)
                print("Horse",SecondHorse,"has overtaken Horse "+str(LeadHorse)+"!")
                X = LeadHorse
                LeadHorse = SecondHorse
                SecondHorse = X
                X = 0

        time.sleep(2)

    print("The race is over!")
    time.sleep(1.5)
    print("Horse",LeadHorse,"has won!")
    time.sleep(1.5)
    if LeadHorse == Horse:
        if Horse == 1:
            print("You earned",Bet*3,"coins.")
            Coins = Coins + Bet*3
        if Horse == 2:
            print("You earned",Bet*HT,"coins.")
            Coins = Coins + Bet*HT
        if Horse == 3:
            print("You earned",Bet*HTH,"coins.")
            Coins = Coins + Bet*HTH
        if Horse == 4:
            print("You earned",Bet*HF,"coins.")
            Coins = Coins + Bet*HF
    else:
        print("You won nothing.")
