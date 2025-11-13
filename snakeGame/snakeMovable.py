from snake import UP, DOWN, LEFT, RIGHT

class SnakeMovable:
    def __init__(self, snake):
        self.snake = snake

    def go_up(self):
        if self.snake.segments[0].heading() != DOWN:
            self.snake.segments[0].setheading(UP)

    def go_down(self):
        if self.snake.segments[0].heading() != UP:
            self.snake.segments[0].setheading(DOWN)

    def go_left(self):
        if self.snake.segments[0].heading() != RIGHT:
            self.snake.segments[0].setheading(LEFT)

    def go_right(self):
        if self.snake.segments[0].heading() != LEFT:
            self.snake.segments[0].setheading(RIGHT)
