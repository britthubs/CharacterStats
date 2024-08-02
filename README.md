# CharacterStats
A program that rolls stats for D&D characters. Currently it only supports three roll methods,
but eventually more methods will be added.

## Table of contents
- [Overview](#overview)
  - [The goal](#the-goal)
  - [Usage](#usage)
- [Roll Methods](#roll-methods)
  - [Method 1](#method-1)
  - [Method 2](#method-2)
  - [Method 3](#method-3)
  - [More to come...](#more-to-come...)
- [Process](#process)
  - [Built with](#built-with)
  - [Useful resources](#useful-resources)
- [Author](#author)

## Overview

### The goal

Building a script to automate stat rolling, learning how to make a gui

### Usage
To make sure the right packages are installed, in the terminal write: ```pip install -r requirements.txt```

The user can choose the method that will be used to roll stats, 
add the name of their character and decide if they want to roll for other characters. 
After this, they can decide if they want to add another character or not. When all characters are added,
the user chooses to not add any more characters and a summary of all characters and stats (colour coded)
is given.

## Roll Methods
The included methods for rolling stats:
### Method 1
3d6 is rolled and the results are added for each stat (for example for strength the results are 2,5,4 - the strength stat is 11)

### Method 2
Same as method 1, but repeated 3 times for each stat and the highest is picked (for example for strength the three stats are 11, 16, 10 - the strength stat is 16)

### Method 3
4d6 is rolled, the lowest result is dropped and the rest is added for each stat (for example for strength the results are 2,5,4,6 - the strength stat is 15)

### More to come...

## Process

### Built with

- Python 3.9
- termcolor package

### Useful resources

- [Replit's 100 days of python](https://replit.com/learn/100-days-of-python/) - Not only did this help freshen up my memory, it also gave me the idea for a D&D stats program.

## Author
britthubs
