import random

def display1():
    print("*********")
    print("         ")
    print("    *    ")
    print("         ")
    print("*********")

def display2():
    print("*********")
    print("         ")
    print("  *   *  ")
    print("         ")
    print("*********")

def display3():
    print("*********")
    print("         ")
    print("*   *   *")
    print("         ")
    print("*********")

def display4():
    print("*********")
    print("  *   *  ")
    print("         ")
    print("  *   *  ")
    print("*********")

def display5():
    print("*********")
    print("  *   *  ")
    print("    *    ")
    print("  *   *  ")
    print("*********")

def display6():
    print("*********")
    print("*   *   *")
    print("         ")
    print("*   *   *")
    print("*********")


roll_status = True

while (roll_status == True):
    roll_dice_input = input("Do you want to roll the dice (y/n)")

    if (roll_dice_input == 'y'):
        dice_roll_num = random.randint(1,6)
        print("You rolled an " , dice_roll_num , "." )
        if(dice_roll_num == 1):
            display1()
        elif(dice_roll_num == 2):
            display2()
        elif(dice_roll_num == 3):
            display3()
        elif(dice_roll_num == 4):
            display4()
        elif(dice_roll_num == 5):
            display5()
        elif(dice_roll_num == 6):
            display6()

    elif (roll_dice_input == 'n'):
        roll_status = False
        print("Thanks for playing!")
    else:
        print("Invalid input, try again")