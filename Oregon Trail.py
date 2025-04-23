import os
import random
import sys
import time

distance = 0
progress = 0



def dayCycle():
  global distance
  global progress
  global water
  global food
  global wood
  global tires
  global randomDisaster
  global hunt
  global river
  global crossing
  ### all the options for what you do without the random events
  print(" 1. Travel")
  print(" 2. Check Supplies")
  print(" 3. See Progress")
  print(' 4. Hunt')
  print(' 5. Chop Down Trees')
  dayCycleInput = input("")
  os.system('cls' if os.name == 'nt' else 'clear')
  if dayCycleInput == "1":
    distance += 100
    progress += 1
    food -= 50
    water -= 50
    print("You have traveled", distance,
          "M in total, and lost 50 food and water")
    ### Random Event Stuff
    randomDisaster = random.randint(1, 13)
    ### Nothing
    if randomDisaster == 1:
      print("Nothing of note happened")
    ### Loss of food
    if randomDisaster == 2:
      print("You encountered a wild animal that stole some of your food")
      food -= 100
    ### Loss of water
    if randomDisaster == 3:
      print("You and your party got thirsty and drank extra water")
      water -= 100
    ### River
    if randomDisaster == 4:
      print(
          "You enconutered a river and it took some of your supplies to cross it"
      )
      wood -= 150
      water -= 50
      food -= 50
    ### Extra Food
    if randomDisaster == 5:
      print('Your party found some food lying aronud')
      food += 50
    ### Water Near River
    if randomDisaster == 6:
      print('Your party got some water by a nearby river')
      water += 100
      wood -= 50
    ### No Progress
    if randomDisaster == 7:
      print(
          'Your group found some trouble moving forward halting your progress')
      distance -= 100
      progress -= 1
    ### Trail lengthened
    if randomDisaster == 8:
      print('Trail get lengthened')
      progress -= 1
    ### Short Cut
    if randomDisaster == 9:
      print('Your group found a short cut')
      progress += 1
    ### Nothing
    if randomDisaster == 10:
      print('Nothing notable happened')
    ### Popped Wheels
    if randomDisaster == 11:
      if tires < 2:
        print('You dont have enough wheels to make repairs and your wagon breaks down')
        sys.exit()
      print('Your wheels pop')
      tires -= 2
    ### Actual River Crossing
    if randomDisaster == 12:
      print('You have encountered a river, how would you like to dea with it?')
      print(' 1. Float wagon over, 50% chance of success takes 100 wood')
      print(' 2. Keep on going, 25% chance of success doesnt take anything.')
      print(' 3. Throwaway food then float, lose food, water, and wood, 75% of working')
      river = input('')
      if river == '1':
        crossing = random.randint(1,2)
        if crossing == 1:
          os.system('cls' if os.name == 'nt' else 'clear')
          print('You failed to cross, you lose')
          sys.exit()
        else:
          os.system('cls' if os.name == 'nt' else 'clear')
          print('you successfully crossed!')
          wood -= 100
      if river == '2':
        crossing = random.randint(1,4)
        if crossing == 1:
          os.system('cls' if os.name == 'nt' else 'clear')
          print('You have successfully crossed')
        else:
          os.system('cls' if os.name == 'nt' else 'clear')
          print('You failed to cross, you lose')
          sys.exit()
      if river == '3':
        crossing = random.randint(1,4)
        if crossing == 1:
          os.system('cls' if os.name == 'nt' else 'clear')
          print('You failed to cross')
          sys.exit()
        else:
          os.system('cls' if os.name == 'nt' else 'clear')
          print('You successfuly crossed')
          food -= 50
          water -= 50
          wood -= 50
    if randomDisaster == 13:
      print(
          'You use the wagon to cross a river and it gets damaged in the process'
      )
      wood -= 200
    # End of Random Event logic
  if dayCycleInput == "2":
    print(" You have ", food, "Food")
    print(" You have ", water, "water")
    print(" You have ", tires, "wheels")
    print(" You have ", wood, "wood")
  if dayCycleInput == "3":
    print("Your progress is ", progress, ", you need 20 in order to finish")
  if dayCycleInput == "4":
    print('Everytime you go hunting you lose water!')
    # Start of hunting logic
    hunt = random.randint(0, 10)
    if hunt == 0:
      print('You failed to hunt')
      water -= 50
    if hunt == 1:
      print('You barely got anything')
      food += 50
      water -= 50
    if hunt == 2:
      print('You barely got anything')
      food += 100
      water -= 50
    if hunt == 3:
      print('You barely got anything')
      food += 100
      water -= 50
    if hunt == 4:
      print('You had a decent hunt')
      food += 150
      water -= 50
    if hunt == 4:
      print('You had a decent hunt')
      food += 200
      water -= 50
    if hunt == 5:
      print('You had a decent hunt')
      food += 250
      water -= 50
    if hunt == 6:
      print('You had a decent hunt')
      food += 300
      water -= 50
    if hunt == 7:
      print('Amazing Hunt')
      food += 350
      water -= 50
    if hunt == 8:
      print('Amazing Hunt')
      food += 400
      water -= 50
    if hunt == 9:
      print('Amazing Hunt')
      food += 400
      water -= 50
    if hunt == 10:
      print('Amazing Hunt')
      food += 500
      water -= 50
  if dayCycleInput == "5":
    print('Everytime you chop down trees you lose food!')
    # Start of hunting logic
    chop = random.randint(0, 10)
    if chop == 0:
      print('You failed to cut down trees')
      food -= 50
    if chop == 1:
      print('You barely got anything')
      wood += 15
      food -= 50
    if chop == 2:
      print('You barely got anything')
      wood += 20
      food -= 50
    if chop == 3:
      print('You barely got anything')
      wood += 25
      food -= 50
    if chop == 4:
      print('You did a decent job')
      wood += 50
      food -= 50
    if chop == 4:
      print('You did a decent job')
      wood += 75
      food -= 50
    if chop == 5:
      print('You did a decent job')
      wood += 100
      food -= 50
    if chop == 6:
      print('You did a decent job')
      wood += 150
      food -= 50
    if chop == 7:
      print('Amazing job')
      wood += 200
      food -= 50
    if chop == 8:
      print('Amazing job')
      wood += 250
      food -= 50
    if chop == 9:
      print('Amazing job')
      wood += 300
      food -= 50
    if chop == 10:
      print('Amazing job')
      food -= 50
      wood += 350
  ### Lose coditions
  if food <= 0:
    print("You ran out of food!")
    sys.exit()
  if water <= 0:
    print("You ran out of water!")
    sys.exit()
  if wood <= 0:
    print('Your wagon broke down, You Lose')
    sys.exit()
  ### Winning Conditions
  if progress >= 20:
    print("You have made it to the end of the Oregon Trail Congratulations")
    sys.exit()


### Beginning
def beginning():
  global distance
  global progress
  global water
  global food
  global wood
  global tires
  global mainMenu1
  global gameStart
  global info_screen
  print("Welcome to the oregon trail.")
  print(" 1. Play")
  print(" 2. More Information on the Trail")
  mainMenu1 = input("")
  os.system('cls' if os.name == 'nt' else 'clear')
  if mainMenu1 == "2":
    print(
        "The Oregon Trail was a trail stretching over 2k miles, many people sought land."
    )
    print("While also getting rich off of new territorys in the west")
    print('1. Back')
    info_screen = input('')
    if info_screen == "1":
      os.system('cls' if os.name == 'nt' else 'clear')
      beginning()

### Upbringing
  if mainMenu1 == "1":
    print("What are your family upbringings?")
    print(" 1. Bank Owner")
    print(" 2. Ambitious Land Seeker")
    print(" 3. Farmer")
    upbringing = input("")
    gameStart = 1
    ### SUpply def
    if upbringing == "1":
      wood = 500
      tires = 10
      food = 1000
      water = 2000
    if upbringing == "2":
      wood = 500
      tires = 5
      food = 750
      water = 1500
    if upbringing == "3":
      wood = 400
      tires = 2
      food = 500
      water = 1000
    if upbringing == "Axier":
      wood = 1000
      tires = 1000
      food = 100000
      water = 1000000
    ### Game Start
    if gameStart == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Who are you taking with on your trip?")
      print("1. ")
      print("2. ")
      print("3. ")
      print("4. ")
      friend1 = input("")
      friend2 = input("")
      friend3 = input("")
      friend4 = input("")
      os.system('cls' if os.name == 'nt' else 'clear')
      print("1. " + friend1)
      print("2. " + friend2)
      print("3. " + friend3)
      print("4. " + friend4)
      print("Are you ready? y/n")
      readyOrNot = input("")
      os.system('cls' if os.name == 'nt' else 'clear')
      if readyOrNot == "n":
        beginning()
      else:
        for i in range(99):
          dayCycle()
      print('Secret ending')
### Running code
beginning()
