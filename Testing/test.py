def print_hello ():
    """ This function prints hello. """
    print("Hello!")


def goodbye():
    print("Goodbye!")


def main():
    print_hello()
    goodbye()


main()


# Add two numbers and return the results
def sum_two_numbers(a, b):
    result = a + b
    return result

sum of two = sum_two_numbers(5, 6)
print(sum_two_numbers)

def volume_cylinder(radius, height):
    pi = 3.141592653
    volume = pi * radius ** 2 * height
    return volume

my_volume = volume_cylinder(2.5, 5) * 6
print(my_volume)

# This function will print the result
def sum_print(a, b):
    result = a + b
    print(result)


# This function will return the result
def sum_return(a, b):
    result = a + b
    return result


# This code prints the sum of 4+4, because the function has a print
sum_print(4, 4)

# This code prints nothing, because the function returns, and doesn't print
sum_return(4, 4)

# This code will not set x1 to the sum.
# The sum_print function does not have a return statement, so it returns
# nothing!
# x1 actually gets a value of 'None' because nothing was returned
x1 = sum_print(4, 4)
print("x1 =", x1)

# This will set x2 to the sum and print it properly.
x2 = sum_return(4, 4)
print("x2 =", x2)


def calculate_average(a, b):
    """ Calculate an average of two numbers """
    result = (a + b) / 2
    return result


# Pretend you have some code here
x = 45
y = 56

# Wait, how do I print the result of this?
z = calculate_average(x, y)
print(z)