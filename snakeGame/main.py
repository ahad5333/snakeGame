from turtle import Screen
import time
from snake import Snake
from snakeMovable import SnakeMovable
from food import Food
from scoreboard import ScoreBoard
import pygame

# Initialize Pygame for sound
pygame.mixer.init()

# Function to start the game
def game():
    screen = Screen()
    screen.setup(width=700, height=500)
    screen.title("My Snake Game")
    screen.bgcolor("black")
    screen.tracer(0)

    # Create game objects
    snake = Snake()
    food = Food()
    scoreBoard = ScoreBoard()
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

        # Snake eats food
        if snake.head.distance(food) < 15:
            snake.extend()
            food.refresh()
            scoreBoard.increase_score()

            # Play MP3 sound every time the snake eats
            pygame.mixer.music.load("eat.mp3")
            pygame.mixer.music.play()

        # Collision with wall
        if abs(snake.head.xcor()) > 348 or abs(snake.head.ycor()) > 248:
            is_game_on = False
            scoreBoard.game_over()

        # Collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                scoreBoard.game_over()

    # Ask to restart
    answer = screen.textinput("Game Over", "Do you want to restart? (yes/no)").lower()
    if answer == "yes":
        screen.clearscreen()  # Clear the previous game
        game()  # Restart the game
    else:
        screen.bye()

# Start the first game
game()
