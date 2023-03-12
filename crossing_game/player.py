from turtle import Turtle
from typing import MutableSequence
from .car import Car

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_POINT = 280


class Player(Turtle):
    def __init__(self) -> None:
        """_Class responsible for creating the player and moving it up_"""
        super().__init__()
        self.__initial_config()

    def move_up(self) -> None:
        """_Move the player up by the const MOVE_DISTANCE_"""
        self.forward(MOVE_DISTANCE)

    def hit_a_car(self, cars: MutableSequence[Car]) -> bool:
        """_Check if the player hit a car_

        Args:
            cars (MutableSequence[Car]): _A sequence containing the cars on the screen_

        Returns:
            bool: _Whether the player hit a car or not_
        """
        for car in cars:
            if self.distance(car) <= 15:
                return True
        return False

    def won(self) -> bool:
        """_Check if the player reached the finish line_

        Returns:
            bool: _Whether the player reached the finish line or not_
        """
        if self.ycor() == FINISH_POINT:
            self.goto(START_POSITION)
            return True
        return False

    def __initial_config(self):
        """_Set the geometry and color of the player and place it at the bottom of the screen_"""
        self.shape("turtle")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)
