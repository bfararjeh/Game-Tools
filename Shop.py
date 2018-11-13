Coins = 100
from time import sleep

def Shop()
    global Coins
    global Health
    global Power
    global Magic
    print("Welcome to the shop!")
    sleep(1.5)
    print("Here you can buy various items using your coins.")
    sleep(2)
    InShop = 1
    
    while InShop = 1:
        print("What would you like to purchase?")
        print("")
        print("1 - Dual Daggers")
        print("2 - Spellbook")
        print("3 - Health Charm")
        print("4 - Nothing")
        Selection = int(input(""))
        while Selection > 4 or Selection <= 0:
            print("That's not a valid option.")
            sleep(2)
            print("What would you like to purchase?")
            print("")
            print("1 - Dual Daggers")
            print("2 - Spellbook")
            print("3 - Health Charm")
            print("4 - Nothing")      
        if Selection = 1:
            if Coins >= 120
                print("That will be 150 Coins. You have "+str(Coins)+".")
                print("")
                print("1 - Purchase")
                print("2 - Return")
                while SelectionB != 1 and SelectionB != 2:
                    print("That's not an option.")
                    sleep(1.5)
                    print("That will be 150 Coins. You have "+str(Coins)+".")
                    print("")
                    print("1 - Purchase")
                    print("2 - Return")
                if SelectionB = 1
                    print("Purchase successful.")
                    Coins = Coins - 150
                    Power = Power + 10
            if Coins < 150:
                print("That will be 150 Coins. You have "+str(Coins)+".")
                print("")
                print("1 - Return")
                SelectionB = int(input(""))
                while SelectionB != 1:
                    print("That's not an option.")
                    sleep(1.5)
                    print("That will be 150 Coins. You have "+str(Coins)+".")
                    print("")
                    print("1 - Return")

        if Selection = 2:
            if Coins >= 225
                print("That will be 225 Coins. You have "+str(Coins)+".")
                print("")
                print("1 - Purchase")
                print("2 - Return")
                while SelectionB != 1 and SelectionB != 2:
                    print("That's not an option.")
                    sleep(1.5)
                    print("That will be 225 Coins. You have "+str(Coins)+".")
                    print("")
                    print("1 - Purchase")
                    print("2 - Return")
                if SelectionB = 1
                    print("Purchase successful.")
                    Coins = Coins - 225
                    Magic = Magic + 16
            if Coins < 225:
                print("That will be 225 Coins. You have "+str(Coins)+".")
                print("")
                print("1 - Return")
                SelectionB = int(input(""))
                while SelectionB != 1:
                    print("That's not an option.")
                    sleep(1.5)
                    print("That will be 225 Coins. You have "+str(Coins)+".")
                    print("")
                    print("1 - Return")

        if Selection = 3:
            if Coins >= 120
                print("That will be 120 Coins. You have "+str(Coins)+".")
                print("")
                print("1 - Purchase")
                print("2 - Return")
                while SelectionB != 1 and SelectionB != 2:
                    print("That's not an option.")
                    sleep(1.5)
                    print("That will be 120 Coins. You have "+str(Coins)+".")
                    print("")
                    print("1 - Purchase")
                    print("2 - Return")
                if SelectionB = 1
                    print("Purchase successful.")
                    Coins = Coins - 120
                    Health = Health + 10
            if Coins < 120:
                print("That will be 120 Coins. You have "+str(Coins)+".")
                print("")
                print("1 - Return")
                SelectionB = int(input(""))
                while SelectionB != 1:
                    print("That's not an option.")
                    sleep(1.5)
                    print("That will be 120 Coins. You have "+str(Coins)+".")
                    print("")
                    print("1 - Return")

        if Selection = 4:
            InShop = 0 
