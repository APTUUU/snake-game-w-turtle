from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.random_position()

    def random_position(self):
        """Set a random position for the food within the screen boundaries."""
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.setpos(x, y)
