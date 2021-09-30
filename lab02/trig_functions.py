import math
def main():
    degree = float(input('Enter an angle: '))
    rads = math.radians(degree)
    trig1 = math.cos(rads)
    trig2 = math.sin(rads)
    print("The cosine of", degree, "is", trig1)
    print("The sine of", degree, "is", trig2)
main()