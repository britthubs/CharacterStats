# import
import random as ran
import time as t
from termcolor import colored
import os

# set up list
names = []
stats = []

# 6 and 8-sided dice
def six_eight():
    charac = input("What's you character's name?: ")
    six = ran.randint(1, 6)
    eight = ran.randint(1, 8)
    health = six * eight
    names.append(charac)
    stats.append(health)
    print("Their health is:", health, "hp")

# print title
print("🎲 Character Stats Generator 🎲")
print("*" * 31)
six_eight()

# ask for repeat or not
again = "y"
while again == "y":
    again = input("Roll for new character? \ny or n: ")
    while again != "y" and again != "n":
        again = input("Only write y for 'yes' and n for 'no' \nRoll for new character? \ny or n: ")
    if again == "y":
        six_eight()

os.system("clear")
print("These are your characters and their stats:")
print("*" * 42, "\n")

# print a summary of names and stats
for i in range(len(names)):
    if stats[i] < 24:
        color = 'red'
    elif stats[i] > 24:
        color = 'green'
    else:
        color = 'orange'
    print("Character:", names[i], "\nHealth:", colored(stats[i], color), "hp \n")