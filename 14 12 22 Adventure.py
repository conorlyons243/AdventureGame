import colorama, random, time, sys
from colorama import Fore, Back, Style
# Shortcuts for colors
SoldC = Fore.GREEN
TankC = Fore.YELLOW
WizC = Fore.MAGENTA
s = Fore.RESET
b = Back.RESET
n = Style.NORMAL
wrong = Back.RED
count = 0
scalecount = count//10
scaling = scalecount * 0.25
playerCoins = 0
curse = False
enemyFire = False
playerFire = False
enemyPoison = False
playerPoison = False
enemyCoinSteal = False
enemyFreeze = False
playerStatusCount = 3

while True:
    print(Style.BRIGHT+"Welcome to ____!"+n, Fore.GREEN+"\n1. New game", Fore.YELLOW + "\n2. Load game", Fore.RED+"\n3. Exit \n(4 for admin)"+s)
    # asks for menu selection
    menuSelect = int(input("Menu selection: "))
    if menuSelect == 1:
        while True:
            print("Creating new game")
            name = input("Enter your name (type back to go back): ")
            if name == "Back" or name == "back":
                break
            dificulty = int(input("\nChoose your Difficulty\n1. Easy\n2. Hard\nSelect dificulty: "))
            # checks that there is not already a file with that name
            try:
                f = open(fr"{name}.csv", "r")
                f.close()
                print("\nA file with this name already exists")
                # asks user if they want to overwrite existing file
                check = int(input("Do you want to overwrite this file?\n1. Yes\n2. No\n"))
                if name == "Back" or name == "back":
                    break
                if check == 1:
                        f = open(fr"{name}.csv" , "w")
                        f.close()
                        break
                else:
                    continue
            except:
                # if file doesn't exist, creates new one
                f = open(fr"{name}.csv" , "w")
                f.close()
                break
                    
    elif menuSelect == 2:
        while True:
            try:
                name = input("Enter your name: ").strip().title()
                if name == "Back" or name == "back":
                    break
                f = open(fr"{name}.csv", "r")
                f.close
                break
            except:
                print("No file found with that name.")
                continue
    elif menuSelect == 3:
        exit()
      
    elif menuSelect == 4:
      f = open("Admin.csv", "r")
      f.close()
      name = "Admin"
      classType = 3
      maxHealth = 100
      damage = 100
      baseDamage = damage
      playerCoins = 10000
      healPotions = 3
      playerHealth = 90
      dificulty = 2
      CName = WizC + "Wizard"
      Weapon1 = Fore.RED + Style.BRIGHT + "Fireball" + s + n
      Weapon2 = Fore.WHITE + Style.BRIGHT + "Wind Spell" + n + s
      break

    else:
        print("Not a valid menu selection")
        continue
    if name == "Back" or name == "back":
        continue
    break

# Defining name for saving
namesave = name
# Class Selection
if menuSelect == 1:
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
                baseDamage = damage
                healPotions = 3
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
                baseDamage = damage
                healPotions = 3
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
                baseDamage = damage
                healPotions = 3
                break
            if confirmClass == 2:
                print("\n")
            elif confirmClass < 1 or confirmClass > 2:
                print(wrong, "Invalid Selection", b)
            
        elif classType > 3 or classType < 1:
            print(wrong, "Invalid Selection", b)

elif menuSelect == 2:
    f = open(fr"{namesave}.csv", "r")
    dataIn = f.read()
    dataList = dataIn.split(",")
    classType = int(dataList[0])
    playerHealth = int(dataList[1])
    maxHealth = int(dataList[2])
    damage = int(dataList[3])
    baseDamage = damage
    count = int(dataList[4])
    dificulty = int(dataList[5])
    playerCoins = int(dataList[6])
    healPotions = int(dataList[7])
    
    scalecount = count//10
    scaling = scalecount * 0.25
    f.close
    if classType == 1:
        CName = SoldC + "Soldier"
        Weapon1 = Fore.RED + "Sword Slash" + s
        Weapon2 = Fore.CYAN + "Shield Block" + s
        name = SoldC + name + s
    if classType == 2:
        CName = TankC + "Tank"
        Weapon1 = Fore.YELLOW + "Punch" + s
        Weapon2 = Fore.BLUE + "Kick" + s
        name = TankC + name + s
    if classType == 3:
        CName = WizC + "Wizard"
        Weapon1 = Fore.RED + Style.BRIGHT + "Fireball" + s + n
        Weapon2 = Fore.WHITE + Style.BRIGHT + "Wind Spell" + n + s
        name = WizC + name + s
    #Loads Weapons after ^ that
    Weapon1 = dataList[8]
    Weapon2 = dataList[9]
    print("File load successful")
    time.sleep(1)
#Boss generation
def bossGen():
  global enemyNum, enemy, enemyHealth, enemyDamage, enemyHitMessage, coins, healPotions, curse, enemyFire, enemyPoison, enemyCoinSteal, enemyFreeze
  curse = False
  enemyFire = False
  enemyPoison = False
  enemyCoinSteal = False
  enemyFreeze = True
  enemy = Fore.CYAN + "Frost Dragon" + s
  enemyHealth = 15
  coins = enemyHealth * 2
  enemyDamage = 6
  enemyHitMessage =  "uses it's ice breath!"
  
def enemyGen():
  # Random Enemy Generation
    global enemyNum, enemy, enemyHealth, enemyDamage, enemyHitMessage, coins, healPotions, curse, playerStatusCount, enemyFire, enemyPoison, enemyCoinSteal
    enemyNum = random.randint(1,5)
    if enemyNum == 1:
        curse = False
        enemyFire = False
        enemyPoison = False
        enemyCoinSteal = True
        enemyFreeze = False
        enemy = Fore.GREEN + "Goblin" + s
        enemyHealth = 5
        coins = enemyHealth
        enemyDamage = 2
        enemyHitMessage =  "swings its club!"
        
    if enemyNum == 2:
        playerStatusCount = 4
        curse = True
        enemyFire = False
        enemyPoison = False
        enemyCoinSteal = False
        enemyFreeze = False
        enemy = Fore.WHITE + Style.BRIGHT + "Skeleton" + s + n
        enemyHealth = 6
        coins = enemyHealth
        enemyDamage = 3
        enemyHitMessage = "shoots an arrow!"
        
    if enemyNum == 3:
        curse = False
        enemyFire = False
        enemyPoison = False
        enemyCoinSteal = False
        enemyFreeze = False
        enemy = Fore.CYAN + "Slime" + s
        enemyHealth = 5
        coins = enemyHealth
        enemyDamage = 1
        enemyHitMessage = "bounces around!"
        
    if enemyNum == 4:
        playerStatusCount = 0
        enemyFire = True
        enemyPoison = False
        curse = False
        enemyCoinSteal = False
        enemyFreeze = False
        enemy = Fore.RED + "Dragon" + s
        enemyHealth = 8
        coins = enemyHealth
        enemyDamage = 5
        enemyHitMessage = "uses it's fire breath!"
        
    if enemyNum == 5:
        playerStatusCount = 0
        enemyPoison = True
        enemyFire = False
        curse = False
        enemyCoinSteal = False
        enemyFreeze = False
        enemy = Fore.YELLOW + "Serpent" + s
        enemyHealth = 7
        coins = enemyHealth
        enemyDamage = 3
        enemyHitMessage = "bites!"

# Poison for player
def playerPoisonEffect():
    global playerHealth, enemyHealth, playerStatusCount, enemyStatusCount
    playerStatusCount = 3
    if playerStatusCount > 0:
        print(Fore.GREEN + "You've been poisoned! You will lose 1 health every turn." + s)
        time.sleep(1)
        playerHealth -= 1
        playerStatusCount -= 1

# Poison for enemy
def enemyPoisonEffect():
    global playerHealth, enemyHealth, playerStatusCount, enemyStatusCount
    playerStatusCount = 3
    if enemyStatusCount > 0:
        enemyHealth -= 1
        enemyStatusCount

# Curse
def curseEffect():
    global playerHealth, enemyHealth, playerStatusCount, enemyStatusCount
    if playerStatusCount == 4:
        print(Fore.MAGENTA + Style.DIM + "You have been cursed!" +n+s)
        time.sleep(1)
    if playerStatusCount > 0:
        playerStatusCount -= 1
    if playerStatusCount == 0:
        print(Fore.MAGENTA + Style.DIM + "You have died from curse..."+s+n)
        time.sleep(1)
        playerHealth = 0
    if playerStatusCount >= 1:
        print(Fore.MAGENTA + Style.DIM + "You will die from curse in", str(playerStatusCount), "turn(s)." +s+n)
        time.sleep(1)

# Fire for player
def playerFireEffect():
    global playerHealth, enemyHealth, playerStatusCount, enemyStatusCount, maxHealth
    playerStatusCount = 3
    if playerStatusCount > 0:
        print(Fore.RED + Style.BRIGHT +"You've been Burned! You lost 2 health and your max health has been reduced by 1!" + s + n)
        time.sleep(1)
        #maybe dont remove health, just reduce max health to be less op
        playerHealth -= 2
        maxHealth -= 1
        #playerStatusCount -= 1

# Fire for enemy
def enemyFireEffect():
    global playerHealth, enemyHealth, playerStatusCount, enemyStatusCount, maxHealth
    enemyStatusCount = 3
    if enemyStatusCount > 0:
        enemyHealth -= 2
        enemyStatusCount -= 1

# Coin steal for player
def playerCoinStealEffect():
    global playerCoins
    playerCoins -= 2
    print(Fore.YELLOW + Style.BRIGHT + "The Goblin stole 2 of your coins!" + s + n)
    time.sleep(1)

def playerFreezeEffect():
    global damage
    if damage > 1:
      damage -= 1
      print(Fore.BLUE + "You've been Frozen! Your damage has been reduced by 1!" + s)
      time.sleep(1)

#Defining battle()
def battle():
    global count, scaling, scalecount
    global enemyNum, enemy, enemyHealth, enemyDamage, enemyHitMessage, playerCoins, healPotions, curse, enemyStatusCount, playerStatusCount, curseCount, enemyPoisonCount, enemyFireCount, enemyCoinSteal, damage, Weapon1
    #pre-battle constants
    global playerHealth
    enemyStun = 0

    #Opening Battle text
    print("\n")
    print("A", enemy, "appears!")
    time.sleep(1)
    
    # Scaling
    count += 1
    scalecount = count//10
    scaling = scalecount * 0.25
    if dificulty == 2:
        enemyHealth += enemyHealth * scaling
    # Battle System
    while enemyHealth > 0 or playerHealth > 0:
        # Player Selection
        print("\n\n", name, "Health:", Fore.GREEN + str(playerHealth) + s, "      ", enemy, "'s Health:", Fore.RED + str(enemyHealth) + s,"\n", 39*"-", "\n 1.", Weapon1, "(75% damage chance) \n",  "2.", Weapon2, "(50% stun chance)", "\n 3.", Fore.GREEN + "Heal" + s, healPotions, "left", "\n 4. Run", "\n 5. Save and Quit")
        selection = int(input("What will "+ name + " do? "))
        # Damage Attack
        if selection == 1:
          damageChance = random.randint(1,4)
          if damageChance == 1:
            print(name, "missed!\n")
            time.sleep(1)
          else:
              print("\n" + name, "used", Weapon1, "to damage the", enemy, "for", damage, "health!")
              enemyHealth -= damage
              if enemyHealth < 0:
                  enemyHealth = 0
              print(enemy, "'s health is at", enemyHealth, "\n")
              time.sleep(1)
          if enemyHealth <= 0:
                break
        # Stun Attack
        if selection == 2:
            print("\n", name, "used", Weapon2, "to knock back the", enemy, "!")
            time.sleep(1)
            stunChance = random.randint(1,2)
            if stunChance == 1:
                print(enemy, "is stunned! \n")
                time.sleep(1)
                print( enemy, "'s health is at", enemyHealth)
                enemyStun = 2
                
            if stunChance == 2:
                print(Fore.RED + "Stun failed!", "\n" + s)
                enemyStun = 0
            time.sleep(1)
        # Heal System
        global maxHealth
        if selection == 3:
            if playerHealth == maxHealth:
                print(Fore.RED + "Can't heal any more!" + s)
                time.sleep(1)
            if playerHealth < maxHealth:
                if healPotions > 0:
                  healNum = random.randint(1,3)
                  if healNum > (maxHealth - playerHealth):
                      healNum = maxHealth - playerHealth
                  print(Fore.GREEN + "\nHealed", healNum, "health points!" + s)
                  time.sleep(1)
                  playerHealth += healNum
                  if playerHealth > maxHealth:
                      playerHealth = maxHealth
                  healPotions -= 1
                  print(name, "'s health is at", playerHealth, "\n")
                  time.sleep(1)
                if healPotions == 0:
                  print(Fore.RED + "No Potions Remaining! \n" + s)
                  time.sleep(1) 
            
        # Run Chance
        if selection == 4:
          runChance = random.randint(1,2)
          if runChance == 1:
              print("\n")
              break
          if runChance == 2:
              print("Run failed!")
              time.sleep(1)
        
        # Save and exit system
        if selection == 5:
            save = int(input("1. Save\n2. Don't Save\nMenu selection: "))
            if save == 1:
                f = open(f"{namesave}.csv", "w")
                f.write(str(classType) + "," + str(playerHealth) + "," + str(maxHealth) + "," + str(damage) + "," + str(count) + "," + str(dificulty) + "," + str(playerCoins) + "," + str(healPotions) + "," + Weapon1 + "," + Weapon2)
                f.close()
                print("Progress saved")
                time.sleep(1)
                exit()
            if save == 2:
              print("Exited without Saving")
              time.sleep(1)
              exit()
              
        # Enemy hit system
        if enemyStun == 0:
            print(enemy, enemyHitMessage)
            hitChance = random.randint(1,2)
            if hitChance == 1:
                print(enemy, "damages", name, "for", enemyDamage, "health!\n")
                if curse == True:
                    curseCount = 1
                if enemyFire == True:
                    enemyPoisonCount = 1
                if enemyPoison == True:
                    enemyPoisonCount = 1
                if enemyCoinSteal == True:
                    playerCoinStealEffect()
                if enemyFreeze == True:
                    playerFreezeEffect()
                time.sleep(1)
                playerHealth -= enemyDamage
                if playerHealth < 0:
                    playerHealth = 0
                print(name, "'s health is at", playerHealth)
                time.sleep(1)
            if hitChance == 2:
                print(enemy, "misses the attack!")
                time.sleep(1)
            if playerHealth <= 0:
                break
        if enemyStun > 0:
            print(enemy, "is stunned and can't move!")
            enemyStun -= 1
            time.sleep(1)
        time.sleep(1)
        if curse == True and curseCount == 1:
            curseEffect()
        if enemyPoison == True and enemyPoisonCount == 1:
            playerPoisonEffect()
        if enemyFire == True and enemyFireCount == 1:
            playerFireEffect()
        if playerHealth <= 0:
            break
    # ↓ not sure what this is for, but it was breaking stuff
    #damage = baseDamage
    if enemyHealth <= 0 and playerHealth <= 0:
        print("You both died!")
    elif enemyHealth <= 0:
        print("\n\n" + name, "defeated the", enemy, "!")
        playerCoins += coins
        print(name, "gained", coins, "coins! \n")
        time.sleep(1)
    elif playerHealth <= 0:
        print(name, "lost...")
    else:
        print("\n Run Sucessful!")
        
# Defining store()
def store():
    global damage
    global maxHealth, playerCoins, healPotions, damage
    while True:
          print("\nBalance:", Fore.YELLOW + str(playerCoins) +s,"\n" + 39*"-","\n1.", Fore.BLUE + "Stat Upgrades" +s, "\n2.", Fore.GREEN + "Potions"+s, "\n3.", Fore.RED + "New Weapons" + s,"\n4. Exit")
          purchase = int(input("Enter desired purchase: "))
      #Stat Upgrade section
          #while True:
          if purchase == 1:
            print(Fore.BLUE + "\nStat Upgrades" +s, "\n" + 39*"-","\n1. +1", Fore.BLUE + "Max Health" +s, "(5 coins)\n2. +1",Fore.RED + "Damage" + s, "(5 coins) \n3. Exit")
            purchase2 = int(input("Enter desired purchase: "))
              #max health
            if purchase2 == 1:
                  if playerCoins < 5:
                      print("You do not have enough coins")
                      time.sleep(1)
                  if playerCoins >= 5:
                      maxHealth += 1
                      playerCoins -= 5
                      print(name, "'s max health is now", maxHealth)
                      time.sleep(1)
            if purchase2 == 2:
                #damage
              if playerCoins < 5:
                      print("You do not have enough coins")
                      time.sleep(1)
              if playerCoins >= 5:
                  damage += 1
                  baseDamage = damage
                  playerCoins -= 5
                  print(name,"'s new damage is", damage)
                  time.sleep(1)
            if purchase2 == 3:
                print("\n")
          
                #potion secton
            
          #while True:
          if purchase == 2:
            print(Fore.GREEN + "\nPotions" + s, "\n" + 39*"-","\n1.", Fore.GREEN + "Health Potions" + s, "(3 coins,", str(healPotions), "in your inventory)", "\n2. Exit")
            purchase3 = int(input("Enter desired purchase: "))
            if purchase3 == 1:
              if playerCoins < 5:
                      print("You do not have enough coins")
                      time.sleep(1)
              if playerCoins >= 3:
                if healPotions >= 3:
                    print(Fore.RED +"You already have max potions!"+s)
                    time.sleep(1)
                else:
                    healPotions += 1
                    playerCoins -= 3
                    print(name,"now has", healPotions, "health potions")
                    time.sleep(1)
            if purchase3 == 2:
              print("\n")
              
          #New Weapon
          if purchase == 3:
            print(Fore.RED + "\nNew Weapons" + s, "\n" + 39*"-", "\n1. New Primary Weapon: ", Fore.BLUE + Style.BRIGHT + "Spear" + s + n," (20 Coins, +2 damage)", "\n2. New Secondary Weapon: ", Fore.RED + "Wall of Flames" +s, "(15 Coins *WORK IN PROGRESS*)", "\n3. Exit")
            purchase4 = int(input("Enter desired purchase: "))
            #Spear
            if purchase4 == 1:
              if playerCoins < 20:
                    print("You do not have enough coins")
                    time.sleep(1)
              if playerCoins >= 20:
                global Weapon1
                playerCoins -= 20
                damage += 2
                Weapon1 = Fore.BLUE + Style.BRIGHT + "Spear" + s + n
                print(name, "equiped the", Weapon1)
                time.sleep(1)
            # Wall of Flames
            if purchase4 == 2:
              if playerCoins < 15:
                    print("You do not have enough coins")
                    time.sleep(1)
              if playerCoins >= 15:
                global Weapon2
                playerCoins -= 15
                Weapon2 = Fore.RED + "Wall of Flames" + s
                print(name, "equiped the", Weapon2)
                time.sleep(1)
              #exit weapon
            if purchase4 == 3:
              print("\n")
              
              
          #Exit
          elif purchase == 4:
            print("\n")
            break
# Defining rest()
def rest():
    global playerHealth
    # Heal while resting
    print(name, "finds a camp to rest and heal their wounds at.")
    playerHealth += 3
    if playerHealth >= maxHealth:
        playerHealth = maxHealth
    print(name, "'s health is now", playerHealth)
    time.sleep(1)

#game begins
#print("\n" * 20)
print("\n\nName:", name, "\nMax Health:", Fore.GREEN + str(maxHealth)+s, "\nDamage:", Fore.RED + str(damage)+s, "\nCoins:", Fore.YELLOW + str(playerCoins)+s, "\nCurrent Health:", Fore.GREEN + str(playerHealth)+s, "\nPotions:", Fore.GREEN + str(healPotions) +s, "\nBattles Completed:", Fore.CYAN + str(count) +s, "\nCurrent Weapons:", Weapon1, ",", Weapon2)

'''
# Picks random choices for different paths and allows choice between two random paths
while True:
    choice1 = random.randint(0, 4)
    choice2 = random.randint(0, 4)
    if choice1 == 0 or choice1 == 1 or choice1 == 2:
        print("1. Battle")
    if choice1 == 3:
        print("1. Store")
    if choice1 == 4:
        print("1. Rest")
    if choice2 == 0 or choice2 == 1 or choice2 == 2:
        print("2. Battle")
    if choice2 == 3:
        print("2. Store")
    if choice2 == 4:
        print("2. Rest")
    choice = int(input("What option do you want: "))
    '''
while True:
  print("\n\nWhat should", name, "do?", "\n1.", Fore.RED + "Battle" +s, "\n2.",  Fore.YELLOW + Style.BRIGHT + "Store" +s+n, "\n3.", Fore.BLUE + "Rest"+s, "\n4.", Fore.MAGENTA + "Profile" +s, "\n5.", Fore.BLACK + "Save and Quit" +s)
  choice = int(input("Which number? "))
  if choice == 1:
        bossCheck = count % 5
        if bossCheck == 0 and count > 0:
          bossGen()
          battle()
        else:
          curseCount = 0
          enemyPoisonCount = 0
          enemyFireCount = 0
          enemyGen()
          battle()
  elif choice == 2:
          store()
  elif choice == 3:
          rest()
  elif choice == 4:
        print("\n\nName:", name, "\nMax Health:", Fore.GREEN + str(maxHealth)+s, "\nDamage:", Fore.RED + str(damage)+s, "\nCoins:", Fore.YELLOW + str(playerCoins)+s, "\nCurrent Health:", Fore.GREEN + str(playerHealth)+s, "\nPotions:", Fore.GREEN + str(healPotions) +s, "\nBattles Completed:", Fore.CYAN + str(count) +s, "\nCurrent Weapons:", Weapon1, ",",Weapon2)
        wait = input("\nType anything to Continue: ")
  elif choice == 5:
    print("\n")
    save = int(input("1. Save\n2. Don't Save\nMenu selection: "))
    if save == 1:
        f = open(f"{namesave}.csv", "w")
        f.write(str(classType) + "," + str(playerHealth) + "," + str(maxHealth) + "," + str(damage) + "," + str(count) + "," + str(dificulty) + "," + str(playerCoins) + "," + str(healPotions) + "," + Weapon1 + "," + Weapon2)
        f.close()
        print("Progress saved")
        time.sleep(1)
        sys.exit()
    if save == 2:
        print("Exited without Saving")
        time.sleep(1)
        sys.exit()
    # Makes sure user is not dead
  if playerHealth <= 0:
        break
      # Autosave
  f = open(f"{namesave}.csv", "w")
  f.write(str(classType) + "," + str(playerHealth) + "," + str(maxHealth) + "," + str(damage) + "," + str(count) + "," + str(dificulty) + "," + str(playerCoins) + "," + str(healPotions) + "," + Weapon1 + "," + Weapon2)
  f.close()
    
save = int(input("1. Save\n2. Don't Save\nMenu selection: "))
if save == 1:
    f = open(f"{namesave}.csv", "w")
    f.write(str(classType) + "," + str(playerHealth) + "," + str(maxHealth) + "," + str(damage) + "," + str(count) + "," + str(dificulty) + "," + str(playerCoins) + "," + str(healPotions) + "," + Weapon1 + "," + Weapon2)
    f.close()
    print("Progress saved")
    time.sleep(1)
    sys.exit()
if save == 2:
    print("Exited without Saving")
    time.sleep(1)
    sys.exit()