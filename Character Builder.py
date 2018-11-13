import time
Repeat = 1

print("Welcome to build a character!")
time.sleep(1.5)

Name = input("What's your name? ")
Correct = input("You chose "+Name+", is this correct? YES or NO ")

while Correct != "YES" and Correct != "NO":
    print("I didn't understand that,")
    time.sleep(1)
    Tutorial = input("You chose "+Name+", is this correct? YES or NO ")

while Correct == "NO":
    Name = input("What's your name? ")
    Correct = input("You chose "+Name+", is this correct? YES or NO ")

print("Hey there "+Name+"!")
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

SkillPoints = 20
Attack = 0
Defence = 0
Power = 0
Guarding = 0
Health = 0
Stamina = 0
Magic = 0
Attack = 0
Defence = 0

while Repeat == 1:

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
        time.sleep(5)
