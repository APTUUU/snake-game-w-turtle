import turtle as t
import random

# Constants for initial positions and colors
POSITIONS = [(0, 0), (20, 0), (40, 0)]
COLORS = ['white', 'yellow', 'green', 'pink', 'brown', 'blue']

class Snake:
    def __init__(self):
        # List to hold segments of the snake
        self.segments = []
        self.color = "white"  # Default color of the snake
        self.create()
        self.head = self.segments[0]  # Head of the snake is the first segment

    def create(self):
        # Creating initial segments of the snake
        for position in POSITIONS:
            self.add_segment(position)

    def extend(self):
        # Adding a new segment to the snake
        pos = self.segments[-1].position()
        self.add_segment(pos)

    def add_segment(self, position):
        # Adding a new segment to the snake
        segment = t.Turtle("square")
        segment.color(self.color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def reset_snake(self):
        # Resetting the snake to its initial state
        for segment in self.segments:
            segment.clear()
            segment.goto(1000, 1000)  # Move segments out of the screen
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def move(self):
        # Moving the snake by updating positions of segments
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(20)

    def shed_skin(self):
        # Changing color of the snake randomly
        self.color = random.choice(COLORS)
        for segment in self.segments:
            segment.color(self.color)

    # Functions to control the direction of the snake
    def up(self):
        if not (self.head.heading() == 270):
            self.head.setheading(90)

    def right(self):
        if not (self.head.heading() == 180):
            self.head.setheading(0)

    def left(self):
        if not (self.head.heading() == 0):
            self.head.setheading(180)

    def down(self):
        if not (self.head.heading() == 90):
            self.head.setheading(270)
