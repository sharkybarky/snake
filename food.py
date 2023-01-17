from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.pencolor("blue")
        self.fillcolor("blue")
        self.speed("fastest")
        self.position_randomly()

    @staticmethod
    def generate_random_pos():
        rand_x = int(random.randint(-280, 280) / 10) * 10
        rand_y = int(random.randint(-280, 280) / 10) * 10
        return rand_x, rand_y

    def position_randomly(self):
        rand_x, rand_y = self.generate_random_pos()
        self.goto(rand_x, rand_y)

