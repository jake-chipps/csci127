import math

###############################################

def getRadius():
    return int(input("Radius: "))

def getArea(radius):
    return math.pi * (radius ** 2)

def getCircumference(radius):
    return 2 * math.pi * radius

###############################################

def main():
    r = getRadius()
    print("The circle with radius:", r, "has\n"
          "Area:", getArea(r),"\n"
          "Circumference:", getCircumference(r))

###############################################

main()
