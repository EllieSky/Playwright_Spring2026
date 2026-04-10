# 1. Write a function greet_user(name) that prints a personalized greeting when called.
# call the function and pass required argument.

def greet_user(name):
    """
    Prints a personalized greeting.
    """
    # Using an f-string to inject the name variable directly into the string
    print(f"Hello, {name}! It's great to see you today.")

# Calling the function and passing the required argument
greet_user("Alex")


# 2. Write a function calculate_tip(bill, percentage=15) that returns the tip amount when called.

def calculate_tip(bill, percentage=15):
    """
    Calculates the tip amount based on a bill and a percentage.

    Args:
        bill (float): The total cost of the bill.
        percentage (int/float): The tip percentage (default is 15).

    Returns:
        float: The calculated tip amount.
    """
    # Formula: (Bill * Percentage) / 100
    tip_amount = (bill * percentage) / 100
    return tip_amount


# Test it out:
# with required parameter only
standard_tip = calculate_tip(100)  # Returns 15.0
print("Expected: 15, Actual: ", standard_tip)

# with overwritten parameter
higher_tip = calculate_tip(100, 20)  # Returns 20.0
print("Expected: 20, Actual: ", higher_tip)

# with named parameters
generous_tip = calculate_tip(percentage = 25, bill = 20)  # Returns 5.0
print("Expected: 5, Actual: ", generous_tip)


# 3. Fix this function:
#
# ￼def multiply(a, b)
#     return a * b


def multiply(a, b):
    return a * b

print("Expected: 12, Actual: ", multiply(3, 4))


# pythonic way to "Test"
expected = 12
actual = multiply(3, 4)
assert actual == expected, f"My actual value '{actual}' did not match my expected value of {expected}"
