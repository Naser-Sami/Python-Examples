
# number of decimal digits 
digits = 4

# Returns the area of a rectangle rounded to (n) decimal places for a length 'l'
# and a width 'w'
def rectangle_area(l, w):
    """Returns the area of a rectangle rounded to (n) decimal places for a length 'l' and a width 'w'"""
    return round(l, w, digits)

# Prompt the user to enter a length using input(), convert the string 
# returned by input() to a float using float() and assign the result to 
# length
length = float(input("Length: "))

# Do the same as the above for the rectangle's width
width = float(input("Width: "))

# Compute the area of a rectangle using the function rectangle_area()
area = rectangle_area(length,width)

# Output the computed area of the rectangle, prepended with the text "Area:"
print("Area:", area)
