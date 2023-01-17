from turtle import Turtle

SEGMENT_STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
MOVE_STEP_SIZE = 15
RIGHT = 0
LEFT = 180
DOWN = 270
UP = 90


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in SEGMENT_STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.turtlesize(1)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.head.forward(MOVE_STEP_SIZE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(to_angle=UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(to_angle=DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(to_angle=LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(to_angle=RIGHT)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def head_collides_with_tail(self):
        for segment in self.segments[1::1]:
            if self.head.heading() != segment.heading() and self.head.distance(segment) < 5:
                return True

