# CHALLENGE 4: DAYS IN A MONTH

# Given a string with a month and a year (separated by a space),
# return the number of days in that month.

# Leap years are a bit tricky. A year is a leap year if and only if:
## it is evenly divisible by 4
## except if it is divisible by 100, in which case it isn’t
## except if it is divisible by 400, in which case it is

# Test Case:
## days_in_month("02 2015"):
## >>> 28

# Pseudocode:
## Write a function that takes in a year and determines if its a leap year
## with the conditions specified above.
## Define a function that takes in a string of a month and year,
## separated by a space
## split the month and year into two variables
## if the month is 02, evaluate if the year is a leap year, 
### if so, return 29
### if not, return 28
## also evaluate if the months are odd, return 31
## if the months are even, return 30

# Code:

def is_leap_year(year):
    """
    Determine if the given year is a leap year.
    :param year: The year to check
    :return: True if the year is a leap year """

    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

def days_in_month(date):
    """
    Given a string with the month and year, determine
    how many days are in that month. """

    month, year = date.split(" ")
    month = int(month)
    year = int(year)


    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    
    if month in [1,3,5,7,8,10,12]:
        return 31

    if month in [4,6,9,11]:
        return 30
