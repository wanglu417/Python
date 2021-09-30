import turtle
import math
STAR_LONG = 500
"""
calculate radius of the circle based on length of star's segment
"""
DEGREE_OF_STAR = 72
radius = (STAR_LONG*(1/2))/math.sin(math.radians(DEGREE_OF_STAR))


def main():
    """
    Define my main()
    """
    turtle.bgcolor('white')
    draw_circle()
    draw_star()
    ts = turtle.getscreen()
    turtle.hideturtle()
    turtle.done()


def draw_circle():
    """
    Draws the circle using radius calculated above
    Fills in the circle with color
    """
    turtle.pencolor('blue')
    turtle.fillcolor('cyan')
    turtle.home()
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()
    turtle.setheading(90)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()


def draw_star():
    """
    Draws the star and fills it in color
    """
    turtle.penup()
    turtle.home()
    turtle.goto(-STAR_LONG/2, radius * math.cos(math.radians(DEGREE_OF_STAR)))
    turtle.pencolor('red')
    turtle.fillcolor('yellow')
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(500)
        turtle.right(144)
    turtle.end_fill()
    turtle.setheading(90)
    turtle.penup()


main()
