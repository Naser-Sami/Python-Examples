
# number of decimal digits 
digits = 4

# Returns the perimeter of a rectangle rounded to (n) decimal places for a length 
# 'l' and a width 'w'
def rectangle_perimeter(l,w):
  """Returns the perimeter of a rectangle rounded to (n) decimal places for a length 'l' and a width 'w'"""
  return round(2 * (l + w), digits)

# Prompt the user to enter a length using input(), convert the string 
# returned by input() to a float using float() and assign the result to 
# length
length = float(input("Length: "))

# Do the same as the above for the rectangle's width
width = float(input("Width: "))

# Compute the perimeter of a rectangle using the function rectangle_perimeter()
perimeter = rectangle_perimeter(length,width)

# Output the computed perimeter of the rectangle, prepended with the text 
# "Perimeter:"
print("Perimeter:", perimeter)
