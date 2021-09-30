"""
Random Number Guessing Game
"""
import random

def main():
    print("Welcome to Thunder Chaser!")
    print("""You have stolen a computer from the Art Studio.
Prof Nostrala wants the computer back to save the day and get you expelled! 
Survive your campus trek and outrun the professor.""")
print()
main()

# Variables
milestraveled = 0
thirst = 0
thunderfatigue = 0
justintraveled = -20
canteen = 3
justinbehind = 10
oasis = 0
done = False


# Start main loop
while not done:
    fullspeed = random.randrange(11, 22)
    moderatespeed = random.randrange(6, 14)
    print("""
    A. Drink from canteen.
    B. Ahead at moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check.
    F. Quit.""")
    user_choice = input("Your choice? ").upper()
    if user_choice.lower() == "f":
        done = True
        print("Bye!")

    elif user_choice.lower() == "e":
        print("Miles traveled: ", milestraveled)
        print("Drinks from canteen: ", canteen)
        print("Your elephant has: ", thunderfatigue, "amount of fatigue.")
        print("The professor is ", justinbehind, "miles behind you.")

    elif user_choice.lower() == "d":
        thunderfatigue *= 0
        print("Thunder feels refreshed and happy his fatigue is now ", thunderfatigue)
        justintraveled += random.randrange(8, 20)

    elif user_choice.lower() == "c":
        print("You traveled ", fullspeed,"miles!")
        milestraveled += random.randrange(2, 5)
        thirst += 2
        thunderfatigue += random.randrange(2, 5)
        justintraveled += random.randrange(8, 16)
        oasis = random.randrange(2,22)

    elif user_choice.lower() == "b":
        print("You traveled ", moderatespeed, "miles!")
        justintraveled += moderatespeed
        thirst += 2
        thunderfatigue += 2
        justintraveled += random.randrange(8, 16)
        oasis = random.randrange(2, 22)

    elif user_choice.lower() == "a":
        if canteen == 0:
            print("You are out of water.")
        else:
            canteen -= 1
            thirst *= 0
            print("You have ",canteen, "drinks left and you are no longer thirsty.")

    if oasis == 21:
        thunderfatigue *= 0
        thirst *= 0
        canteen = 3
        print("You found an oasis! After taking a drink you filled you canteen and Thunder is refreshed.")

    if  justinbehind <= 16:
        print("The professor is drawing near.")

    if milestraveled >= 210 and not done:
        print("You made it across campus, you win!")
        done = True

    if justintraveled >= milestraveled:
        print("The professor gave you detention.")
        print("You're dead!")
        done = True
    if thirst > 7:
        print("You died of dehydration!")
        done = True

    if thunderfatigue > 6 and thunderfatigue >= 9 and not done:
        print ("Thunder is getting tired.")

    if thunderfatigue > 9:
        print("Your camel is dead.")
        done = True
