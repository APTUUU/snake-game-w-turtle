import time

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Setting up the screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("THE SNAKE GAME")

# Creating instances of ScoreBoard, Snake, and Food
scoreboard = ScoreBoard()
snake = Snake()
food = Food()

screen.tracer(0)  # Turning off-screen updates to manually update later

# Reset function to reset the game elements
def reset():
    time.sleep(0.5)
    scoreboard.reset_score()
    snake.reset_snake()
    snake.move()
    snake.shed_skin()

game_on = True

while game_on:
    screen.update()  # Manually updating the screen
    time.sleep(0.1)  # Controlling the game speed

    snake.move()  # Moving the snake
    screen.listen()  # Listening for keyboard inputs
    # Setting up keyboard bindings for snake movement
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    # Handling collision with food
    if snake.head.distance(food) <= 15:
        scoreboard.add()
        snake.extend()
        food.random_position()

    # Checking for collision with the wall
    if (
        snake.head.xcor() < -290
        or snake.head.xcor() > 290
        or snake.head.ycor() < -290
        or snake.head.ycor() > 290
    ):
        reset()  # Resetting the game elements in case of collision with the wall

    # Checking collision with itself
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            reset()  # Resetting the game elements in case of collision with itself

screen.exitonclick()  # Exiting the game when the window is clicked
