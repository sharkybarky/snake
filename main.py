import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

HEIGHT_PIXELS = 600
WIDTH_PIXELS = 600
MAX_X = WIDTH_PIXELS / 2
MAX_Y = HEIGHT_PIXELS / 2
MIN_X = - MAX_X
MIN_Y = - MAX_Y

screen = Screen()
screen.setup(width=WIDTH_PIXELS, height=HEIGHT_PIXELS)
screen.bgcolor("black")
screen.title("Snake 3310 Throwback")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
run_game = True


def end_game():
    global run_game
    run_game = False


screen.listen()
screen.onkeypress(fun=snake.turn_up, key="Up")
screen.onkeypress(fun=snake.turn_down, key="Down")
screen.onkeypress(fun=snake.turn_left, key="Left")
screen.onkeypress(fun=snake.turn_right, key="Right")
screen.onkeypress(fun=end_game, key="Escape")


while run_game:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) <= 14:
        print("Chomp chomp!")
        food.position_randomly()
        score.update()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() >= MAX_X \
            or snake.head.xcor() <= MIN_X \
            or snake.head.ycor() >= MAX_Y \
            or snake.head.ycor() <= MIN_Y:
        run_game = False

    # detect collision with wall
    if snake.head_collides_with_tail():
        run_game = False

score.game_ended()
screen.exitonclick()
