#Write a program that will tell whether the given year is a leap year or not.
# Get input from user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(" is a leap year.")
else:
    print("is not a leap year.")

