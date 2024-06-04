
# number of decimal digits 
digits = 4

# Returns the area of a square rounded to 4 decimal places for a given side 
# length 'l'
def square_area(l):
    # (l * l) or (l ** 2)
    return round(l ** 2, digits)


# Prompt the user to enter a side length using input(), convert the string 
# returned by input() to a float using float() and assign the result to 
# side_length
side_length = float(input("Side length: "))


# Compute the area of a square using the function square_area()
area = square_area(side_length)

# Output the square area, use str() to convert the area numeric value to a 
# string and concatenate that string to "Area: " with +
print("Area: " + str(area))
