import turtle
e = turtle.Turtle()
while True:
    side = int(input("how many sides do you want?: "))
    size= int(input("the length of forward: "))
    angle= 360/side
    for i in range(side):
        e.forward(size)
        e.left(angle)
    print("check the turtle tab to see the turtle move!")
    choice = input("y to continue: ")
    if choice != "y":
        print("bye ig")
        break
        

