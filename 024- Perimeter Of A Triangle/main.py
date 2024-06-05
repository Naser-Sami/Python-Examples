
# number of decimal digits 
digits = 4

# Returns the perimeter of a triangle rounded to 4 decimal places with side 
# lengths a, b, and c
def triangle_perimeter(a, b, c):
  return round(a + b + c, digits)

# Prompt the user to enter a side length 'a' using input(), convert the string 
# returned by input() to a float using float() and assign the result to side_a
side_a = float(input("Side A: "))
# Do the same for side lengths 'b' and 'c'
side_b = float(input("Side B: "))
side_c = float(input("Side C: "))

# Compute the perimeter of the triangle using the function triangle_perimeter()
perimeter = triangle_perimeter(side_a,side_b,side_c)

# Output the computed perimeter of the triangle, prepended with "Perimeter:"
print("Perimeter:", perimeter)
