import turtle
import random

t = turtle.Turtle()

def draw_rectangle():
    for i in range(2):
        t.forward(100)
        t.left(50)
        
def draw_color_triangle(color:str):
    t.penup()
    t.forward(100)
    t.pendown()
    t.pencolor(color) 
    for i in range(3):
        t.forward(100)
        t.left(120)
def get_random_color():
    COLOR = ["red", 'blue', 'green', 'yellow', 'orange', 'purple']
    color = random.choice(COLOR)
    return color

draw_color_triangle(get_random_color())

while True:
    t.speed('fastest')
    color = get_random_color()
    draw_color_triangle(color)
    t.left(5)
    draw_rectangle()
    
