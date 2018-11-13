from time import sleep
import random
Level = 1
XP = 0
Coins = 0
Enemy = ['Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Goblin', 'Hydron', 'Hydron', 'Hydron', 'Hydron', 'Typhon']

print("A wild enemy appeared!")
sleep(1)
EnemyChosen = random.choice(Enemy)

if EnemyChosen == Goblin:
    EnemyHealth = random.randint(25,75) * Level
if EnemyChosen == Hydron:
    EnemyHealth = random.randint(50,100) * Level
if EnemyChosen == Typhon
    EnemyHealth = random.randint(100,200) * Level
    
print("It's a "+EnemyChosen+"!")
sleep(1)
print("What will you do?")
print("")
print("1 - Attack")
print("2 - Flee")
EnemyB = int(input(""))

while EnemyHealth >= 0:
    while EnemyB != 1 and EnemyB != 2:
        print("That's not an option")
        sleep(1)
        print("What will you do?")
        print("")
        print("1 - Attack")
        print("2 - Flee")
        EnemyB = int(input(""))

    if EnemyB == 1:
        print("")
        print("You chose to attack.")
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
            if EnemyChosen == Goblin:
                EnemyHealth = EnemyHealth - DamageDealt
                print("You dealt",DamageDealt," damage, it was effective!")
            if EnemyChosen == Hydra:
                EnemyHealth = EnemyHealth - DamageDealt - 25
                print("You dealt",DamageDealt-25," damage, it was okay.")
            if EnemyChosen == Typhon:
                EnemyHealth = EnemyHealth - DamageDealt // 0
                print("You dealt",DamageDealt//0," damage, it was not very effective!")

        if EnemyC == 2:
            DamageDealt = 10 + Magic*5
            if EnemyChosen == Goblin:
                EnemyHealth = EnemyHealth - DamageDealt
                print("You dealt",DamageDealt," damage, it was effective!")
            if EnemyChosen == Hydra:
                EnemyHealth = EnemyHealth - DamageDealt + 25
                print("You dealt",DamageDealt-25," damage, it was very effective!")
            if EnemyChosen == Typhon:
                EnemyHealth = EnemyHealth - DamageDealt * 2
                print("You dealt",DamageDealt*2," damage, it was extremely effective!")

        sleep(1)
        print("The enemy has",EnemyHealth," health left!")

    if EnemyB == 2:
        print("Like a coward, you flee the scene!")

if EnemyHealth >= 0:
    print("You defeated the wild"+EnemyChosen+"!")
    if EnemyChosen == Goblin:
        XPEarned = 100
    if EnemyChosen == Hydra:
        XPEarned = 150
    if EnemyChosen == Typhon:
        XPEarned = 200
