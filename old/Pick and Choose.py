import colorama, random, time
from colorama import Fore, Back, Style
# Shortcuts for colors
SoldC = Fore.GREEN
TankC = Fore.YELLOW
WizC = Fore.MAGENTA
s = Fore.RESET
b = Back.RESET
n = Style.NORMAL
wrong = Back.RED

# Name
name = input("Enter your name: ")
name = name.capitalize()

# Class Selection
while True:
    classType = input(Fore.CYAN + "\n Pick your class: \n " + SoldC + "1. Soldier (Health: 10, Damage: 3) \n" + TankC + " 2. Tank (Health: 15, Damage: 2) \n" + WizC + " 3. Wizard (Health: 7, Damage: 4) \n \n" + Fore.WHITE + "Pick a Number: " + Fore.RESET)
    try:
        classType = int(classType)
    except:
        print(wrong, "Invalid Selection", b)
        continue
    #Soldier
    if classType == 1:
        print(SoldC + "The Soldier is equipped with a Sword and Shield \n" + s)
        confirmClass = int(input("Do you want to pick this class? (1 for Yes, 2 for No) \n"))
        if confirmClass == 1:
            CName = SoldC + "Soldier"
            Weapon1 = Fore.RED + "Sword Slash" + s
            Weapon2 = Fore.CYAN + "Shield Block" + s
            name = SoldC + name + s
            playerHealth = 10
            maxHealth = 10
            damage = 3
            break
        if confirmClass == 2:
            print("\n")
        elif confirmClass < 1 or confirmClass > 2:
            print(wrong, "Invalid Selection", b)
    #Tank
    if classType == 2:
        print(TankC + "The Tank is equipped only with his Fists and Feet \n" + s)
        confirmClass = int(input("Do you want to pick this class? (1 for Yes, 2 for No) \n"))
        if confirmClass == 1:
            CName = TankC + "Tank"
            Weapon1 = Fore.YELLOW + "Punch" + s
            Weapon2 = Fore.BLUE + "Kick" + s
            name = TankC + name + s
            playerHealth = 15
            maxHealth = 15
            damage = 2
            break
        if confirmClass == 2:
            print("\n")
        elif confirmClass < 1 or confirmClass > 2:
            print(wrong, "Invalid Selection", b)
    #Wizard
    if classType == 3:
        print(WizC + "The Wizard is equipped with Spellbook \n" + s)
        confirmClass = int(input("Do you want to pick this class? (1 for Yes, 2 for No) \n"))
        if confirmClass == 1:
            CName = WizC + "Wizard"
            Weapon1 = Fore.RED + Style.BRIGHT + "Fireball" + s + n
            Weapon2 = Fore.WHITE + Style.BRIGHT + "Wind Spell" + n + s
            name = WizC + name + s
            playerHealth = 7
            maxHealth = 7
            damage = 4
            break
        if confirmClass == 2:
            print("\n")
        elif confirmClass < 1 or confirmClass > 2:
            print(wrong, "Invalid Selection", b)
            
    elif classType > 3 or classType < 1:
        print(wrong, "Invalid Selection", b)
        
#Defining battle()
def battle():
    # Random Enemy Generation
    enemyNum = random.randint(1,5)
    if enemyNum == 1:
        enemy = Fore.GREEN + "Goblin" + s
        enemyHealth = 5
        enemyDamage = 2
        enemyHitMessage =  "swings its club at you!"
        
    if enemyNum == 2:
        enemy = Back.WHITE + Fore.BLACK + "Skeleton" + s + b
        enemyHealth = 6
        enemyDamage = 3
        enemyHitMessage = "shoots an arrow at you!"
        
    if enemyNum == 3:
        enemy = Fore.CYAN + "Slime" + s
        enemyHealth = 5
        enemyDamage = 1
        enemyHitMessage = "bounces on you!"
        
    if enemyNum == 4:
        enemy = Fore.RED + "Dragon" + s
        enemyHealth = 8
        enemyDamage = 5
        enemyHitMessage = "uses it's fire breath on you!"
        
    if enemyNum == 5:
        enemy = Fore.YELLOW + "Serpent" + s
        enemyHealth = 7
        enemyDamage = 3
        enemyHitMessage = "bites you!"

    #pre-battle constants
    global playerHealth
    enemyStun = 0
    healPotions = 3

    #Opening Battle text
    print("\n")
    print("A", enemy, "appears!")
    time.sleep(2)


    # Battle System
    while enemyHealth > 0 or playerHealth > 0:
        # Player Selection
        print("\n\n", name, "Health:", Fore.GREEN + str(playerHealth) + s, "      ", enemy, "'s Health:", Fore.RED + str(enemyHealth) + s,"\n", 39*"-", "\n 1.", Weapon1, "(100% damage chance) \n",  "2.", Weapon2, "(50% stun chance)", "\n 3.", Fore.GREEN + "Heal" + s, healPotions, "left", "\n 4. Run")
        selection = int(input("What number will you do? "))
        # Damage Attack
        if selection == 1:
            print("\n", name, "used", Weapon1, "to damage the", enemy, "for", damage, "health!")
            time.sleep(2)
            enemyHealth -= damage
            print(enemy, "'s health is at", enemyHealth, "\n")
            time.sleep(2)
            if enemyHealth <= 0:
                break
        # Stun Attack
        if selection == 2:
            print("\n", name, "used", Weapon2, "to knock back the", enemy, "!")
            time.sleep(2)
            stunChance = random.randint(1,2)
            if stunChance == 1:
                print(enemy, "is stunned! \n")
                time.sleep(2)
                print( enemy, "'s health is at", enemyHealth)
                enemyStun = 2
                
            if stunChance == 2:
                print(Fore.RED + "Stun failed!", "\n" + s)
                enemyStun = 0
            time.sleep(2)
        # Heal System
        if selection == 3:
            if playerHealth == maxHealth:
                print(Fore.RED + "Can't heal any more!" + s)
                time.sleep(2)
            if playerHealth < maxHealth:
                if healPotions > 0:
                  healNum = random.randint(1,3)
                  print(Fore.GREEN + "\nHealed", healNum, "health points!" + s)
                  time.sleep(2)
                  playerHealth += healNum
                  if playerHealth > maxHealth:
                      playerHealth = maxHealth
                  healPotions -= 1
                  print(name, "'s health is at", playerHealth, "\n")
                  time.sleep(2)
                if healPotions == 0:
                  print(Fore.RED + "\n No Potions Remaining! \n" + s)
                  time.sleep(2) 
            
        # Run Chance
        if selection == 4:
          runChance = random.randint(1,2)
          if runChance == 1:
              print("\n")
              break
          if runChance == 2:
              print("Run failed!")
              time.sleep(2)
              
        # Enemy hit system
        if enemyStun == 0:
            print(enemy, enemyHitMessage)
            hitChance = random.randint(1,2)
            if hitChance == 1:
                print(enemy, "damages", name, "for", enemyDamage, "health!")
                time.sleep(2)
                playerHealth -= enemyDamage
                print(name, "'s health is at", playerHealth)
                time.sleep(2)
            if hitChance == 2:
                print(enemy, "misses the attack!")
                time.sleep(2)
            if playerHealth < 0:
                break
        if enemyStun > 0:
            print(enemy, "is stunned and can't move!")
            enemyStun -= 1
            time.sleep(1)
        time.sleep(2)
    if enemyHealth <= 0 and playerHealth <= 0:
        print("You both died!")
    elif enemyHealth <= 0:
        print("\n\nCongratulations! You defeated the", enemy, "!")
    elif playerHealth <= 0:
        print(name, "lost...")
    else:
        print("\n Run Sucessful!")

#story begins
print("\n" * 20)
print(" Name:  ", name, "\n Class: ", CName, s)
print("On a bright summers day,", name, "is walking home, when suddenly...")
time.sleep(2)
battle()
time.sleep(2)
print("And then...")
battle()
