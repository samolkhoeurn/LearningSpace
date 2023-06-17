"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simluation, as long as all birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364)) # help(datetime.timedelta): Difference between two datetime values.
        #print('randomNumberOfDays:{}'.format(randomNumberOfDays))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)): # help(set): Build an unordered collection of unique elements
        return None # All birthdays are unique, so return None. 
    
    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA # Return the match birthday.
            

# Display the intro:
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

the Birthday paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large.
this program does a Monte Carl simulation 9that i, repeated random simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)

''')


# Set up a tupple of month names in order:

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount.

print()

# Generate and display the birthdays: 

print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
#print('birthdays: {}'.format(birthdays))
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday. 
        print(', ', end='')
    monthName = MONTHS[birthday.month -1]
    #print('monthName:{}'.format(monthName))
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')

print()
print()

# Determine if there are two birthdays that match. 
match = getMatch(birthdays)
#print('match:{}'.format(match))
# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month -1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matchin birthdays.')
print()

# Run through 100,100 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0 # How many simulations had matching birthdays in them. 

for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

print('100,000 simulations run.')

# Display simulations results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times.this means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')