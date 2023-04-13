# import
import random as rand
from termcolor import colored
import os

# set up lists & string (for the summary at the end)
names = []
stats_tot = []
stats_string = ""


def nameAndClear():  # Ask character name and clear stats list
    charac = input("What's you character's name?: ")
    names.append(charac)  # add the name of the character to a list for the summary at the end
    stats = []  # makes sure this list is empty again before adding stats to it
    return stats


def method():  # method list + input method
    print("Method Menu:")
    print("*" * 11)
    print("1: roll 3d6 and add them \n"
          "2: roll 3d6 and add them 3 times, pick the highest\n"
          "3: roll 4d6, drop lowest number and add them")
    methodNum = input("Type the number associated with your preferred method to roll for your character stats: ")
    while methodNum not in {"1", "2", "3"}:
        methodNum = input("Please only write the number associated with your preferred method: ")
    if methodNum == "1":
        three_dsix()  # call the right function according to the chosen method
    elif methodNum == "2":
        three_dsix_drop()
    elif methodNum == "3":
        four_dsix_drop()


def three_dsix_drop():  # 3 times 3d6, pick highest
    stats = nameAndClear()
    for i in range(6):
        dice = [rand.randint(1, 6) + rand.randint(1, 6) + rand.randint(1, 6),
                rand.randint(1, 6) + rand.randint(1, 6) + rand.randint(1, 6),
                rand.randint(1, 6) + rand.randint(1, 6) + rand.randint(1, 6)
                ]  # 3 times 3d6 for one stat
        stat = max(dice)  # take the highest number from the list
        stats.append(stat)  # add the stat to a list for this character's stats
    stats_tot.append(stats)  # put the list of the stats for this character in a list for the summary at the end
    print("Stats completed! \n")


def three_dsix():  # 3d6 per stat
    stats = nameAndClear()
    for i in range(6):
        stat = rand.randint(1, 6) + rand.randint(1, 6) + rand.randint(1, 6)  # 3d6 for one stat
        stats.append(stat)  # add the stat to a list for this character's stats
    stats_tot.append(stats)  # put the list of the stats for this character in a list for the summary at the end
    print("Stats completed! \n")


def four_dsix_drop():  # 4d6 drop the lowest
    stats = nameAndClear()
    for i in range(6):
        dice = [rand.randint(1, 6), rand.randint(1, 6), rand.randint(1, 6), rand.randint(1, 6)]  # 4d6 in a list
        dice.remove(min(dice))  # remove the lowest value from the list
        stat = 0
        for number in dice:
            stat += number  # add all the remaining numbers from the list
        stats.append(stat)  # add the stat to a list for this character's stats
    stats_tot.append(stats)  # put the list of the stats for this character in a list for the summary at the end
    print("Stats completed! \n")


# print title
print("🎲 Character Stats Generator 🎲")
print("*" * 31)
method()  # show the method menu


# ask for repeat or not
while True:
    again = input("Roll for new character? \ny or n: ")
    while again != "y" and again != "n":
        again = input("Only write y for 'yes' and n for 'no' \nRoll for new character? \ny or n: ")
    if again == "n":
        break
    method()  # show the method menu

# print a summary of names and stats
os.system('cls' if os.name == 'nt' else 'clear')  # clear console
print("These are your characters and their stats:")
print("*" * 42, "\n")
for i in range(len(names)):
    for s in range(6):  # 6 stats per character get color coded
        stats = stats_tot[i]
        if stats[s] < 10:
            color = 'red'
        elif stats[s] > 10:
            color = 'green'
        else:
            color = 'yellow'
        stats_string += f'{colored(stats[s], color)} '  # add the color coded stat to a string
    print("Character:", names[i], "\nStats:", stats_string, "\n")
    stats_string = ""
