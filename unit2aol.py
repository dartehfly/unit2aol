from random import *
"""
=========================
Question 2: extremeTuple
=========================
"""

exampletuple = (1, 14, -5, 6, 3)  # just example values


# returns min and max values, very straightforward
def extremetuple(tup):

        return min(tup), max(tup)


# defensive coding, if there are no arguments.
if len(exampletuple) == 0:

    print("No arguments provided.")

# defensive coding, if there is no minimum or maximum.
elif min(exampletuple) == max(exampletuple):

    print("All arguments are "+str(min(exampletuple)))

# calls the function if it's valid.
else:

    print(extremetuple(exampletuple))

""" 
=============================
Question 3: Student Database
=============================
"""

# opens database, splits into a list of strings of each line.
data = open("studentInfoText.txt", "r").readlines()

# formatting data into a list filled with tuples.
# tuples are immutable, and were chosen as the info about students shouldn't ever be changed within the program.
for i in range(len(data)):

    data[i] = data[i].rstrip()  # removing formatting in text, really just "\n"s.
    data[i] = data[i].split(",")  # split strings into lists.
    data[i] = tuple(data[i])  # convert lists into tuples.

# gathering search data.
fname = input("FNAME: ")
lname = input("LNAME: ")
grade = input("GRADE: ")
house = input("HOUSE: ")
advisor = input("ADVISOR: ")

searchterms = (fname, lname, grade, house, advisor)  # consolidating search terms into a tuple.
# chose a tuple as it won't be changing within this iteration of the program.

numterms = 0
for i in range(len(searchterms)):  # scans search terms list for number of terms.
    if not searchterms[i]:  # if list index is empty, basically do nothing.
        numterms += 0
    else:  # if list index contains a term, increase term number.
        numterms += 1

results = []

# using nested for loops to search through each part of data, appending matching values to a list.
for i in range(len(data)):
    matchedterms = 0  # resets num of matched terms for this student
    for j in range(len(data[i])):
        if searchterms[j].lower() == data[i][j].lower():  # if the info matches, add 1 to matched terms.
            matchedterms += 1

    if matchedterms == numterms:  # if the correct number of terms have been matched, add student index to results.
        results.append(i)

# formatting results indexes into a list of the full student info.
if len(results) == 0:  # if there are no matching results, informs the user.
    print("No results found.")
else:
    for i in range(len(results)):
        results[i] = data[results[i]]  # converts indexes into the full strings
    print(results)

"""
================================
Question 4: Flight Dictionaries
================================
"""

# example flights dictionary
exampleflights = {"Geneva": ["Zurich", "Basel"], "Zurich": ["Zermatt", "Geneva"],
                  "Bern": ["Basel"], "Basel": ["Geneva", "Bern"], "Zermatt": ["Zurich"]}


def one_hop(flights, city1, city2):
    for step1 in flights[city1]:  # for each city that is accessible from city one,
        for step2 in flights[step1]:  # checks the cities reachable from those cities,
            if step2 == city2:  # if any of them are the destination, return true.
                return True


# filled out with example cities.
print((one_hop(exampleflights, "Geneva", "Zermatt")))

"""
=======================
Question 5: MindReader
=======================
"""


# number generator function, needs 3 (or less) number history to operate.
def numbergenerator(nums):
    if nums == [1, 2, 1] or nums == [2, 1, 2]:  # assuming 121212 or 212121 pattern.
        return nums[1]
    elif nums == [1, 1, 1] or nums == [2, 2, 2]:  # assuming 111111 or 222222 pattern.
        return nums[0]
    elif nums == [2, 1, 1] or nums == [1, 1, 2]:  # assuming 221122 or 112211 pattern.
        return 2
    elif nums == [2, 2, 1] or nums == [1, 2, 2]:  # assuming same pattern as above, but switched.
        return 1
    elif len(nums) == 2 and nums == [1, 1]:  # assuming only two numbers and they're both 1.
        return 1
    else:
        return 2  # if all else fails, 2, also if the first two are twos this will catch on.


def mindreader():

    score = {"Computer": 0, "Player": 0}  # reset score
    numbers = []  # used list here because tuples are immutable and dictionaries wouldn't make sense.

    while score["Computer"] < 30 and score["Player"] < 30:  # while nobody has won yet,
        number = int(input("Okay. I have my number. What's yours? (1 or 2)\n"))  # get user number

        # compare user number and computer guess
        if number == numbergenerator(numbers):
            print("Got it! My number was also", number)
            score["Computer"] += 1

        else:
            print("Darn. I picked", (number % 2)+1)
            score["Player"] += 1

        # prints scores every time they change
        print("Computer: ", score["Computer"], "Player: ", score["Player"], "\n")

        # add recent number to history list, if there's more than 3, pop the oldest one.
        numbers.append(number)
        if len(numbers) > 3:
            numbers.pop(0)
    """
    # Only used to tally results of the automated playtesting.
    if score["Computer"] > score["Player"]:
        return "Computer"
    else:
        return "Player"
    """


mindreader()


"""
I ran a few tests of this automated game playing script with different patterns to test the pattern recognition:

winners = [0, 0]
for i in range(1000):
    if mindreader() == "Computer":
        winners[0] += 1
    else:
        winners[1] += 1
print(winners)

After 1000 games played:

Test 1: Random Numbers
Computer - 50% 
Player - 50%
Variability - ~0.025%

Test 2: 1,2,1,2,1 pattern
Computer - 100%
Player - 0%
Variability - 0%

Test 3: All 1's or all 2's
Computer - 100%
Player - 0%
Variability - 0%

Test 4: 2,2,1,1,2,2 pattern
Computer - 100%
Player - 0%
Variability - 0%
"""
