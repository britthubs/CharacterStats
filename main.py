# import
import random as rand
from termcolor import colored
import os
import curses

# set up lists & string (for the summary at the end)
names = []
stats_tot = []
stats_string = ""

def initialise():
    stdscr = curses.initscr()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)
    curses.start_color()
    return stdscr

stdscr = initialise()

# Define colors for highlighting selected option
curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
highlight = curses.color_pair(1)

# Define method menu options
methods = [
    "1: roll 3d6 and add them",
    "2: roll 3d6 and add them 3 times, pick the highest",
    "3: roll 4d6, drop lowest number and add them",
]
selected_method = 0

# Disable input buffering
stdscr.nodelay(1)

# Set a timeout for getch()
stdscr.timeout(100)


def print_menu(stdscr, selected_idx):  # Function to print menu options
    stdscr.clear()  # Clear the screen
    stdscr.addstr(0, 0, "Method Menu:\n", curses.A_UNDERLINE)
    for i, option in enumerate(methods):
        if i == selected_idx:
            stdscr.addstr(option + "\n", highlight)
        else:
            stdscr.addstr(option + "\n")
    stdscr.refresh()  # Refresh the screen
    curses.doupdate()  # Manually flush the console buffer


def navigate_menu(stdscr):  # Function to handle arrow key navigation
    global selected_method
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_UP:
            selected_method = (selected_method - 1) % len(methods)
        elif key == curses.KEY_DOWN:
            selected_method = (selected_method + 1) % len(methods)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            callFunc(selected_method)  # Call the selected method
        print_menu(stdscr, selected_method)


def callFunc(selected_method):
    if selected_method == 0:
        three_dsix()
    elif selected_method == 1:
        three_dsix_drop()
    elif selected_method == 2:
        four_dsix_drop()
    return  # return control to the main loop


def nameAndClear():  # Ask character name and clear stats list
    curses.endwin()
    charac = input("What's you character's name?: ")
    names.append(charac)  # add the name of the character to a list for the summary at the end
    stats = []  # makes sure this list is empty again before adding stats to it

    # Re-initialize curses mode
    stdscr = initialise()
    return stats, stdscr


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
    stats, stdscr = nameAndClear()
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
    stats, stdscr = nameAndClear()
    for i in range(6):
        stat = rand.randint(1, 6) + rand.randint(1, 6) + rand.randint(1, 6)  # 3d6 for one stat
        stats.append(stat)  # add the stat to a list for this character's stats
    stats_tot.append(stats)  # put the list of the stats for this character in a list for the summary at the end
    print("Stats completed! \n")


def four_dsix_drop():  # 4d6 drop the lowest
    stats, stdscr = nameAndClear()
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

# Display menu and handle user input
navigate_menu(stdscr)
callFunc()


# ask for repeat or not
while True:
    curses.endwin()
    again = input("Roll for new character? \ny or n: ")
    while again != "y" and again != "n":
        again = input("Only write y for 'yes' and n for 'no' \nRoll for new character? \ny or n: ")
    if again == "n":
        break
    stdscr = initialise()
    navigate_menu(stdscr)
    callFunc(selected_method)

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

# End curses
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()