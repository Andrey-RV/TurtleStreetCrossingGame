import random
from turtle import Turtle
from typing import MutableSequence

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
INITIAL_SPEED = 10
SPEED_INCREMENT = 5


class Car(Turtle):
    current_speed = 0

    def __init__(self):
        """Class responsible to create and move the cars.

        Attributes:
            current_speed (int): A class attribute that stores the current speed of the cars.
        """
        super().__init__()
        self._initial_config()

    @classmethod
    def increase_speed(cls):
        """Increase the current speed of the cars by the const SPEED_INCREMENT."""
        cls.current_speed += SPEED_INCREMENT

    @classmethod
    def move_the_cars(cls, cars: MutableSequence['Car']) -> None:
        """Move the cars forward by the current speed."""
        for car in cars:
            car.forward(INITIAL_SPEED + cls.current_speed)

    def _initial_config(self) -> None:
        """Set the geometry and color of the car and place it at the right side of the screen."""
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.goto(x=600, y=random.randint(-250, 250))
