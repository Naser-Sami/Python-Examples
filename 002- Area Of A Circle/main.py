from math import pi

def circle_area(r) -> float:
    return round(pi * r ** 2, 4)

radius = float(input("Radius: "))
area = circle_area(radius)
print('Area: ' + str(area))
