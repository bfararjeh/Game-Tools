import time
from time import sleep
import random
Power = 0
Guarding = 0
Health = 0
Stamina = 0
Magic = 0
Attack = 0
Defence = 0
SkillIncrease = 0
SkillDecrease = 0
Level = 1
HP = 100*Level + Health*5
Coins = 20
XP = 0
DamageTaken = 0
NameChosen = 0
SkillPoints = 30
Name = "X"
DaggerOwn = 0
SpellbookOwn = 0
HealthCharmOwn = 0

print("Hey there!")
sleep(1)
print("Welcome newcomer!")
sleep(1)
print("Feel free to do what you want.")
sleep(1)
print("For a list of commands, type 'Help()' at anytime.")





















































































































































    
def Help():
    print("Available Commands:")
    print("")
    print("'CharacterBuild()' Lets you build and modify your character.")
    print("'Battle()' Looks for a nearby battle.")
    print("'Clear()' Clears your python shell.")
    print("'LevelUp()' Will level you up if you have enough XP.")
    print("'Gamble()' Gamble your coins for a chance to earn more.")
    print("")

def Shop():
    global Coins
    global Health
    global Power
    global Magic
    global DaggerOwn
    global SpellbookOwn
    global HealthCharmOwn
    print("Welcome to the shop!")
    sleep(1.5)
    print("Here you can buy various items using your coins.")
    sleep(2)
    InShop = 1
    
    while InShop == 1:
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
        if Selection == 1 and DaggerOwn = 1:
            print("You already own this.")
            sleep(1.5)
        if Selection == 1:
            if Coins >= 150:
                print("That will be 150 Coins. You have "+str(Coins)+".")
                print("")
                print("1 - Purchase")
                print("2 - Return")
                SelectionB = int(input(""))
                while SelectionB != 1 and SelectionB != 2:
                    print("That's not an option.")
                    sleep(1.5)
                    print("That will be 150 Coins. You have "+str(Coins)+".")
                    print("")
                    print("1 - Purchase")
                    print("2 - Return")
                    SelectionB = int(input(""))
                if SelectionB == 1:
                    print("Purchase successful.")
                    Coins = Coins - 150
                    Power = Power + 10
                    DaggerOwn = 1
                    sleep(2)
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
                    SelectionB = int(input(""))

        if Selection == 2 and SpellBookOwn = 1:
            print("You already own this.")
            sleep(1.5)
        if Selection == 2:
            if Coins >= 225:
                print("That will be 225 Coins. You have "+str(Coins)+".")
                print("")
                print("1 - Purchase")
                print("2 - Return")
                SelectionB = int(input(""))
                while SelectionB != 1 and SelectionB != 2:
                    print("That's not an option.")
                    sleep(1.5)
                    print("That will be 225 Coins. You have "+str(Coins)+".")
                    print("")
                    print("1 - Purchase")
                    print("2 - Return")
                    SelectionB = int(input(""))
                if SelectionB == 1:
                    print("Purchase successful.")
                    Coins = Coins - 225
                    sleep(2)
                    Magic = Magic + 16
                    SpellBookOwn = 1
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
                    SelectionB = int(input(""))

        if Selection == 3 and HealthCharmOwn = 1:
            print("You already own this.")
            sleep(1.5)
        if Selection == 3:
            if Coins >= 120:
                print("That will be 120 Coins. You have "+str(Coins)+".")
                print("")
                print("1 - Purchase")
                print("2 - Return")
                SelectionB = int(input(""))
                while SelectionB != 1 and SelectionB != 2:
                    print("That's not an option.")
                    sleep(1.5)
                    print("That will be 120 Coins. You have "+str(Coins)+".")
                    print("")
                    print("1 - Purchase")
                    print("2 - Return")
                    SelectionB = int(input(""))
                if SelectionB == 1:
                    print("Purchase successful.")
                    sleep(2)
                    Coins = Coins - 120
                    Health = Health + 10
                    HealthCharmOwn = 1
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
                    SelectionB = int(input(""))

        if Selection == 4:
            InShop = 0 

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


def LevelUp():
    global XP
    global Level

    if Level <= 5:
        x = 150
    else:
        x = Level*75

    if XP > x:
        print("You have enough XP to level up!")
        sleep(1)
        print("Commencing Level Up!")
        sleep(2)
        XP = 0
        Level = Level + 1
        SkillPoints = Skillpoints + 10
        print("You are now level "+Level+"!")
        sleep(1)
        print("You earned 5 skill points and your XP has been reset to 0.")
    else:
        print("You don't have enough XP to level up.")
        sleep(1)
        print("You have",XP,"XP, you need",x,"XP.")



def Battle():
    global Level 
    global Coins 
    global XP
    global DamageTaken
    global HP
    
    print("A wild enemy appeared!")
    sleep(1)
    if random.randint(1,50) == 1:
        EnemyChosen = "Typhon"
    elif random.randint(1,10) == 1:
        EnemyChosen = "Hydra"
    else:
        EnemyChosen = "Goblin"
        
    if EnemyChosen == "Goblin":
        EnemyHealth = random.randint(25,75) * Level
    if EnemyChosen == "Hydra":
        EnemyHealth = random.randint(50,100) * Level
    if EnemyChosen == "Typhon":
        EnemyHealth = random.randint(100,200) * Level
        
    print("It's a "+EnemyChosen+"!")
    sleep(1)
    print("What will you do?")
    print("")
    print("1 - Attack")
    print("2 - Flee")
    EnemyB = int(input(""))

    while EnemyHealth > 0 and EnemyB == 1:
        if EnemyB == 1:
            print("")
            print("You chose to engage.")
            sleep(1)
            print("Would you like to use: ")
            print("")
            print("1 - Melee")
            print("2 - Magic")
            EnemyC = int(input(""))

        while EnemyC != 1 and EnemyC != 2:
            print("That's not an option")
            sleep(1)
            print("Would you like to use: ")
            print("")
            print("1 - Melee")
            print("2 - Magic")
            EnemyC = int(input(""))

        if EnemyC == 1:
            DamageDealt = 25 + Strength*3
            if EnemyChosen == "Goblin":
                EnemyHealth = EnemyHealth - DamageDealt
                print("You dealt",DamageDealt,"damage, it was effective!")
            if EnemyChosen == "Hydra":
                EnemyHealth = EnemyHealth - DamageDealt + 15
                print("You dealt",DamageDealt-15,"damage, it was okay.")
            if EnemyChosen == "Typhon":
                print("You dealt 0 damage, it was not effective.")
            sleep(1)
            
        if EnemyC == 2:
            DamageDealt = 10 + Magic*5
            if EnemyChosen == "Goblin":
                EnemyHealth = EnemyHealth - DamageDealt
                print("You dealt",DamageDealt,"damage, it was effective!")
            if EnemyChosen == "Hydra":
                EnemyHealth = EnemyHealth - DamageDealt - 25
                print("You dealt",DamageDealt+25,"damage, it was very effective!")
            if EnemyChosen == "Typhon":
                EnemyHealth = EnemyHealth - DamageDealt * 2
                print("You dealt",DamageDealt*2,"damage, it was extremely effective!")

        if EnemyHealth > 0:
            sleep(1)
            print("The enemy has",EnemyHealth,"health left!")
            sleep(1.5)
            print("The",EnemyChosen,"lashes out at you!")
            sleep(1.5)

            if EnemyChosen == "Goblin":
                DamageTaken = random.randint(25,50) - Guarding
            elif EnemyChosen == "Hydra":
                DamageTaken = random.randint(50,75) - Guarding*2
            elif EnemyChosen == "Typhon":
                DamageTaken = random.randint(75,125) - Guarding*3

            HP = HP - DamageTaken
            print("Suffered",DamageTaken,"damage.")
            print("You now have",HP,"health left.")


        if HP <= 0:
            print("Critical damage!")
            sleep(1)
            print("You're blacking out...")
            EnemyHealth = 0
            RewardGain = 2
            
        if EnemyHealth <= 0 and HP > 0:
            print("You emerge victorious, blood on your hands. You monster.")
            sleep(2)
            RewardGain = 1
                    
        if EnemyB == 2:
            print("Like a coward, you flee the scene!")
            RewardGain = 0
            EnemyHealth = 0

    if RewardGain == 1:
        print("You defeated the wild "+EnemyChosen+"!")
    if EnemyChosen == "Goblin":
        XPEarned = random.randint(50,100) 
    if EnemyChosen == "Hydra":
        XPEarned = random.randint(100,150)
    if EnemyChosen == "Typhon":
        XPEarned = random.randint(150,200)
    XP = XP + XPEarned
    Coins = Coins + XPEarned // 3
    print("You now have",XP,"XP and",Coins,"coins.")

    if RewardGain == 2:
        sleep(2)
        print("You blacked out.")
        sleep(1)
        print("You lost 10% of your coins and your XP was reduced by 25%")
        XP = XP - XP // 4
        Coins = Coins - Coins // 10

def Clear():
    print(" \n"*100)
    
def CharacterBuild():
    global Power
    global Guarding 
    global Health 
    global Stamina 
    global Magic 
    global Attack 
    global Defence 
    global SkillIncrease 
    global SkillDecrease 
    global NameChosen  
    global SkillPoints
    global Name
    
    print("Welcome to build a character!")
    time.sleep(1.5)
    
    if NameChosen == 0:
        Name = input("What's your name? Make sure you choose wisely, your name is permanent! ")
        Correct = input("You chose "+Name+", is this correct? YES or NO ")

        while Correct != "YES" and Correct != "NO":
            print("I didn't understand that,")
            time.sleep(1)
            Tutorial = input("You chose "+Name+", is this correct? YES or NO ")

        while Correct == "NO":
            Name = input("What's your name? ")
            Correct = input("You chose "+Name+", is this correct? YES or NO ")

    print("Hey there "+Name+"!")
    NameChosen = 1
    Tutorial = input("Would you like a tutorial? YES or NO ")

    while Tutorial != "YES" and Tutorial != "NO":
        print("I didn't understand that,")
        time.sleep(1)
        Tutorial = input("Would you like a tutorial? YES or NO ")
        
    if Tutorial == "YES":
        time.sleep(1.5)
        print("You start with 20 skill points.")
        time.sleep(1.5)
        print("You can spend your skill points to upgrade your individual skills.")
        time.sleep(1.5)
        print("There are 5 skills,")
        time.sleep(0.5)

        print("Power")
        time.sleep(0.5)
        print("Guarding")
        time.sleep(0.5)
        print("Health")
        time.sleep(0.5)
        print("Stamina")
        time.sleep(0.5)
        print("Magic")
        time.sleep(2)

        time.sleep(1.5)
        print("You have two main stats, Attack and Defence.")
        time.sleep(1.5)
        print("Upgrading certain skills will upgrade the corresponding stat.")
        time.sleep(1.5)
        print("For example, upgrading Stamina will increase your Defence stat greatly,")
        time.sleep(1.5)
        print("But your Attack stat lightly.")
        time.sleep(1.5)
        print("That is all there is to explain,")
        time.sleep(1.5)
        print("Sending you to the character lab!")
        time.sleep(0.5)
        print("...")
        time.sleep(2)

    if Tutorial == "NO":
        print("Sending you to the character lab!")
        time.sleep(0.5)
        print("...")
        time.sleep(2)



    print("Welcome!")
    time.sleep(1)
    print("What would you like to upgrade?")
    print("")
    print("1 - Power")
    print("2 - Guarding")
    print("3 - Health")
    print("4 - Stamina")
    print("5 - Magic")
    print("6 - View Stats")
    Choose = int(input(""))

    while Choose >6 or Choose <1:
        print("That's not an option.")
        time.sleep(1)
        print("What would you like to upgrade?")
        print("")
        print("1 - Power")
        print("2 - Guarding")
        print("3 - Health")
        print("4 - Stamina")
        print("5 - Magic")
        print("6 - View Stats")
        Choose = int(input(""))

    if Choose == 1:
        print("What would you like to do to Power?")
        print("1 - Increase")
        print("2 - Decrease")
        print("3 - Return")
        ChooseB = int(input(""))

        if ChooseB == 1 and SkillPoints > 0:
            print("You have",SkillPoints,"Skill points left, how much would you like to spend?")
            SkillIncrease = int(input(""))
            if SkillIncrease > SkillPoints:
                print("Count is too high.")
                time.sleep(1.5)
                print("Reducing to",SkillPoints)
                time.sleep(1.5)
                SkillIncrease = SkillPoints
            if SkillIncrease < 0:
                print("Count is too low.")
                time.sleep(1.5)
                print("Reducing to 1")
                time.sleep(1.5)
                SkillIncrease = 1


            Power = Power + SkillIncrease
            print("Your Power is now",Power)
            time.sleep(1.5)
            AttackChange = Power * 80
            Attack = Attack + AttackChange
            SkillPoints = SkillPoints - SkillIncrease
            
        if ChooseB == 2 and Power > 0:
            print("You Power is",Power,", by how much would you like to decrease?")
            SkillDecrease = int(input(""))
            if SkillDecrease > Power:
                print("Count is too high.")
                time.sleep(1.5)
                print("Reducing to",Power)
                time.sleep(1.5)
                SkillDecrease = Power
            if SkillDecrease < 0:
                print("Count is too low.")
                time.sleep(1.5)
                print("Reducing to 1")
                time.sleep(1.5)
                SkillDecrease = 1
                
            Power = Power - SkillDecrease
            print("Your Power is now",Power)
            time.sleep(1.5)
            AttackChange = Power * 80
            Attack = Attack - AttackChange
            SkillPoints = SkillPoints + SkillDecrease

        if ChooseB == 3:
            print("Returning...")
            time.sleep(2)

    if Choose == 2:
        print("What would you like to do to Guarding?")
        print("1 - Increase")
        print("2 - Decrease")
        print("3 - Return")
        ChooseB = int(input(""))

        if ChooseB == 1 and SkillPoints > 0:
            print("You have",SkillPoints,"Skill points left, how much would you like to spend?")
            SkillIncrease = int(input(""))
            if SkillIncrease > SkillPoints:
                print("Count is too high.")
                time.sleep(1.5)
                print("Reducing to",SkillPoints)
                time.sleep(1.5)
                SkillIncrease = SkillPoints
            if SkillIncrease < 0:
                print("Count is too low.")
                time.sleep(1.5)
                print("Reducing to 1")
                time.sleep(1.5)
                SkillIncrease = 1


            Guarding = Guarding + SkillIncrease
            print("Your Guarding is now",Guarding)
            time.sleep(1.5)
            DefenceChange = Guarding * 85 
            Defence = Defence + DefenceChange
            SkillPoints = SkillPoints - SkillIncrease
            
        if ChooseB == 2 and Power > 0:
            print("You Guarding is",Guarding,", by how much would you like to decrease?")
            SkillDecrease = int(input(""))
            if SkillDecrease > Guarding:
                print("Count is too high.")
                time.sleep(1.5)
                print("Reducing to",Guarding)
                time.sleep(1.5)
                SkillDecrease = Guarding
            if SkillDecrease < 0:
                print("Count is too low.")
                time.sleep(1.5)
                print("Reducing to 1")
                time.sleep(1.5)
                SkillDecrease = 1
                
            Guarding = Guarding - SkillDecrease
            print("Your Gurading is now",Guarding)
            time.sleep(1.5)
            DefenceChange = Guarding * 85
            Defence = Defence - DefenceChange
            SkillPoints = SkillPoints + SkillDecrease

        if ChooseB == 3:
            print("Returning...")
            time.sleep(2)

    if Choose == 3:
        print("What would you like to do to Health?")
        print("1 - Increase")
        print("2 - Decrease")
        print("3 - Return")
        ChooseB = int(input(""))

        if ChooseB == 1 and SkillPoints > 0:
            print("You have",SkillPoints,"Skill points left, how much would you like to spend?")
            SkillIncrease = int(input(""))
            if SkillIncrease > SkillPoints:
                print("Count is too high.")
                time.sleep(1.5)
                print("Reducing to",SkillPoints)
                time.sleep(1.5)
                SkillIncrease = SkillPoints
            if SkillIncrease < 0:
                print("Count is too low.")
                time.sleep(1.5)
                print("Reducing to 1")
                time.sleep(1.5)
                SkillIncrease = 1


            Health = Health + SkillIncrease
            print("Your Health is now",Health)
            time.sleep(1.5)
            DefenceChange = Health * 50
            AttackChange = Health * 10
            Attack = Attack + AttackChange
            Defence = Defence + DefenceChange
            SkillPoints = SkillPoints - SkillIncrease
            
        if ChooseB == 2 and Health > 0:
            print("You Health is",Health,", by how much would you like to decrease?")
            SkillDecrease = int(input(""))
            if SkillDecrease > Health:
                print("Count is too high.")
                time.sleep(1.5)
                print("Reducing to",Health)
                time.sleep(1.5)
                SkillDecrease = Health
            if SkillDecrease < 0:
                print("Count is too low.")
                time.sleep(1.5)
                print("Reducing to 1")
                time.sleep(1.5)
                SkillDecrease = 1
                
            Health = Health - SkillDecrease
            print("Your Health is now",Health)
            time.sleep(1.5)
            DefenceChange = Health * 50
            AttackChange = Health * 10
            Attack = Attack - AttackChange
            Defence = Defence - DefenceChange
            SkillPoints = SkillPoints + SkillDecrease

        if ChooseB == 3:
            print("Returning...")
            time.sleep(2)

    if Choose == 4:
        print("What would you like to do to Stamina?")
        print("1 - Increase")
        print("2 - Decrease")
        print("3 - Return")
        ChooseB = int(input(""))

        if ChooseB == 1 and SkillPoints > 0:
            print("You have",SkillPoints,"Skill points left, how much would you like to spend?")
            SkillIncrease = int(input(""))
            if SkillIncrease > SkillPoints:
                print("Count is too high.")
                time.sleep(1.5)
                print("Reducing to",SkillPoints)
                time.sleep(1.5)
                SkillIncrease = SkillPoints
            if SkillIncrease < 0:
                print("Count is too low.")
                time.sleep(1.5)
                print("Reducing to 1")
                time.sleep(1.5)
                SkillIncrease = 1


            Stamina = Stamina + SkillIncrease
            print("Your Stamina is now",Stamina)
            time.sleep(1.5)
            DefenceChange = Stamina * 35
            AttackChange = Stamina * 40
            Attack = Attack + AttackChange
            Defence = Defence + DefenceChange
            SkillPoints = SkillPoints - SkillIncrease
            
        if ChooseB == 2 and Stamina > 0:
            print("You Stamina is",Stamina,", by how much would you like to decrease?")
            SkillDecrease = int(input(""))
            if SkillDecrease > Stamina:
                print("Count is too high.")
                time.sleep(1.5)
                print("Reducing to",Stamina)
                time.sleep(1.5)
                SkillDecrease = Stamina
            if SkillDecrease < 0:
                print("Count is too low.")
                time.sleep(1.5)
                print("Reducing to 1")
                time.sleep(1.5)
                SkillDecrease = 1
                
            Stamina = Stamina - SkillDecrease
            print("Your Stamina is now",Stamina)
            time.sleep(1.5)
            DefenceChange = Stamina * 35
            AttackChange = Stamina * 40
            Attack = Attack - AttackChange
            Defence = Defence - DefenceChange
            SkillPoints = SkillPoints + SkillDecrease

        if ChooseB == 3:
            print("Returning...")
            time.sleep(2)

    if Choose == 5:
        print("What would you like to do to Magic?")
        print("1 - Increase")
        print("2 - Decrease")
        print("3 - Return")
        ChooseB = int(input(""))

        if ChooseB == 1 and SkillPoints > 0:
            print("You have",SkillPoints,"Skill points left, how much would you like to spend?")
            SkillIncrease = int(input(""))
            if SkillIncrease > SkillPoints:
                print("Count is too high.")
                time.sleep(1.5)
                print("Reducing to",SkillPoints)
                time.sleep(1.5)
                SkillIncrease = SkillPoints
            if SkillIncrease < 0:
                print("Count is too low.")
                time.sleep(1.5)
                print("Reducing to 1")
                time.sleep(1.5)
                SkillIncrease = 1


            Magic = Magic + SkillIncrease
            print("Your Magic is now",Magic)
            time.sleep(1.5)
            DefenceChange = Magic * 20
            AttackChange = Magic * 50
            Attack = Attack + AttackChange
            Defence = Defence + DefenceChange
            SkillPoints = SkillPoints - SkillIncrease
            
        if ChooseB == 2 and Magic > 0:
            print("You Magic is",Magic,", by how much would you like to decrease?")
            SkillDecrease = int(input(""))
    if SkillDecrease > Magic:
        print("Count is too high.")
        time.sleep(1.5)
        print("Reducing to",Magic)
        time.sleep(1.5)
        SkillDecrease = Magic
        if SkillDecrease < 0:
            print("Count is too low.")
            time.sleep(1.5)
            print("Reducing to 1")
            time.sleep(1.5)
            SkillDecrease = 1

        Magic = Magic - SkillDecrease
        print("Your Magic is now",Magic)
        time.sleep(1.5)
        DefenceChange = Magic * 20
        AttackChange = Magic * 50
        Attack = Attack - AttackChange
        Defence = Defence - DefenceChange
        SkillPoints = SkillPoints + SkillDecrease

    if ChooseB == 3:
        print("Returning...")
        time.sleep(2)

    if Choose == 6:
        print("Here are your stats as of now.")
        print("")
        print("Attack:",Attack)
        print("Defence:",Defence)
        time.sleep(1)
