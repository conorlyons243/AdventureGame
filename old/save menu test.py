import colorama
from colorama import Fore, Back, Style

file = open("saveGame.csv", "r")
saveData = list(file.read())
file.close()

while True:
    try:
        save = int(input("Welcome to ___!\n 1. Load Saved Game \n 2. New Game\n\n Which Number? "))
    
    #Load the save game
        if save == 1:
            # Try split the list into variables, and assign indexed item into variable, eg Health = myList[1]
            print(Back.RED + "unfinished\n\n"+ Back.RESET)
        
        #Deletes save and creates new game
        if save == 2:
            confirm = input("\nAre you sure you want to start a New Game? \n Yes or No? ")
            confirm = confirm.capitalize()
            
            if confirm == "Yes":
                file = open("saveGame.csv", "w")
                file.write("")
                file.close()
                break
            if confirm == "No":
                print("\n\n")
                continue
            else:
                print(Back.RED + "Invalid Option\n\n" + Back.RESET)
    except:
        print(Back.RED + "Invalid Option" + Back.RESET + "\n\n")
        