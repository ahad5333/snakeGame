from turtle import Turtle

class Border:
    def __init__(self):
        self.drawer = Turtle()
        self.drawer.hideturtle()
        self.drawer.color("white")
        self.drawer.penup()
        self.drawer.goto(-350, 250)
        self.drawer.pendown()
        self.drawer.pensize(3)
        for _ in range(2):
            self.drawer.forward(700)
            self.drawer.right(90)
            self.drawer.forward(500)
            self.drawer.right(90)
