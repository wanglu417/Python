import math
def main():
    x1 = int(input('Enter value x1: '))
    x2 = int(input('Enter value x2: '))
    y1 = int(input('Enter value y1: '))
    y2 = int(input('Enter value y2: '))
    p1 = [x1, y1]
    p2 = [x2, y2]
    distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
    print("The Euclidean distance between the two points is", distance)
main()