#Write a program to find the simple interest when the value of principle,
#rate of interest and time period is give
def find_simple_interest(principle, rate, time):
    """
    Function to calculate the simple interest.
    :param principle: float, the value of the principle
    :param rate: float, the rate of interest (in percentage)
    :param time: float, the time period (in years)
    :return: float, the simple interest
    """
    # Convert the rate of interest to a decimal
    rate_decimal = rate / 100

    # Calculate the simple interest
    simple_interest = principle * rate_decimal * time

    return simple_interest


# Get the values of principle, rate of interest and time period from the user
principle = float(input("Enter the value of the principle: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculate the simple interest
simple_interest = find_simple_interest(principle, rate, time)

# Display the result
print(f"The simple interest is: {simple_interest}")