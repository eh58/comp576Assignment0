# Python program to check if year is a leap year or not
# Eddy Huang (eh58)

# Prompt the user to input the year integer
year = int(input("Enter the year you want to check: "))

# If a year is divisible by both 100 and 400, then it is a leap year
# source: https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
if year % 4 == 0:
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

# year is not leap year
else:
    print("{0} is not a leap year".format(year))