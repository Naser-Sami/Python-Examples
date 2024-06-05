
# number of decimal digits 
digits = 4

# Returns the area of a triangle rounded to (n) decimal places for a base 'b' and
# a height 'h'
def triangle_area(b,h):
  """Returns the area of a triangle rounded to (n) decimal places for a base 'b' and a height 'h'"""
  return round(0.5 * b * h, 4)

# Prompt the user to enter a base using input(), convert the string 
# returned by input() to a float using float() and assign the result to 
# base
base = float(input("Base: "))

# Do the same as the above for the triangle's height
height = float(input("Height: "))

# Compute the area of the triangle using the function triangle_area()
area = triangle_area(base,height)

# Output the computed area of the triangle, prepended with the text "Area:"
print("Area:", area)
