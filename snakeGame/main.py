from turtle import Screen
import time
from snake import Snake
from snakeMovable import SnakeMovable
from food import Food
from scoreboard import ScoreBoard
from border import Border

# Screen setup
screen = Screen()
screen.setup(width=700, height=500)
screen.title("🐍 My Snake Game 🐍")
screen.bgcolor("black")
screen.tracer(0)

# Draw border and initialize game objects
border = Border()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
snake_controls = SnakeMovable(snake)

# Keyboard controls
screen.listen()
screen.onkey(snake_controls.go_up, "Up")
screen.onkey(snake_controls.go_down, "Down")
screen.onkey(snake_controls.go_left, "Left")
screen.onkey(snake_controls.go_right, "Right")

# Main game loop
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
