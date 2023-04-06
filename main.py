# import
import random as ran
from termcolor import colored
import os

# set up lists & string (for the summary at the end)
names = []
stats_tot = []
stats_string = ""

# method list + input method
def method():
    print("Method Menu:")
    print("*" * 11)
    print("1: 3d6 \n")
    methodNum = input("Type the number associated with your preferred method to roll for your character stats: ")
    while methodNum != "1":
        methodNum = input("Please only write the number associated with your preferred method: ")
    if methodNum == "1":
        three_dsix()  # go to the function for method 3d6

# 3d6 per stat
def three_dsix():
    charac = input("What's you character's name?: ")
    names.append(charac)  # add the name of the character to a list for the summary at the end
    stats = []  # makes sure this list is empty again before adding stats to it
    for i in range(6):
        stat = ran.randint(1,6) + ran.randint(1,6) + ran.randint(1,6) # 3d6 for one stat
        stats.append(stat)  # at the stat to a list for this character's stats
    stats_tot.append(stats)  # put the list of the stats for this character in a list for the summary at the end


# print title
print("🎲 Character Stats Generator 🎲")
print("*" * 31)
method()  # shows the method menu


# ask for repeat or not
again = "y"
while again == "y":
    again = input("Roll for new character? \ny or n: ")
    while again != "y" and again != "n":
        again = input("Only write y for 'yes' and n for 'no' \nRoll for new character? \ny or n: ")
    if again == "y":
        method()  # shows the method menu


os.system("clear")
print("These are your characters and their stats:")
print("*" * 42, "\n")

# print a summary of names and stats
for i in range(len(names)):
    for s in range(6):  # 6 stats per character get color coded
        stats = stats_tot[i]
        if stats[s] < 10:
            color = 'red'
        elif stats[s] > 10:
            color = 'green'
        else:
            color = 'yellow'
        stats_string += f'{colored(stats[s], color)} '  # adds the color coded stat to a string

    print("Character:", names[i], "\nStats:", stats_string, "\n")
    stats_string = ""