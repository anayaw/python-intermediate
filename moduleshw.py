c = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "pink","magenta", "light green", "light blue"]
import turtle
import random as r
ell = turtle.Turtle()
steps = r.randrange(10,70)
degrees = r.randrange(10,350)
while True:
    colour = r.choice(c)
    print(colour)
    ell.forward(steps)
    ell.left(degrees)
    ell.color(colour)
