import random
from turtle import Turtle
from typing import MutableSequence

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
INITIAL_SPEED = 10
SPEED_INCREMENT = 5


class Car(Turtle):
    current_speed = 0

    def __init__(self):
        """_The car class is responsible for creating the cars and moving them_

        Attributes:
            current_speed (int): _A class attribute that stores the current speed of the cars_
        """
        super().__init__()
        self.__initial_config()

    @classmethod
    def increase_speed(cls):
        """_Increase the current speed of the cars by the const SPEED_INCREMENT_"""
        cls.current_speed += SPEED_INCREMENT

    @classmethod
    def move_the_cars(cls, cars: MutableSequence['Car']) -> None:
        """_Move the cars forward by the current speed_"""
        for car in cars:
            car.forward(INITIAL_SPEED + cls.current_speed)

    def __initial_config(self) -> None:
        """_Set the geometry and color of the car and place it at the right side of the screen_"""
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.goto(x=600, y=random.randint(-250, 250))
