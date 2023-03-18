from turtle import Turtle
from typing import MutableSequence
from .car import Car

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_POINT = 280


class Player(Turtle):
    def __init__(self) -> None:
        """Class responsible to create and move the player."""
        super().__init__()
        self.__initial_config()

    def move_up(self) -> None:
        """Move the player up by the const MOVE_DISTANCE."""
        self.forward(MOVE_DISTANCE)

    def hit_a_car(self, cars: MutableSequence[Car]) -> bool:
        """Check if the player hit a car.

        Args:
            cars (MutableSequence[Car]): A sequence containing the cars on the screen.

        Returns:
            bool: .Whether the player hit a car or not.
        """
        for car in cars:
            if self.distance(car) <= 15:
                return True
        return False

    def won(self) -> bool:
        """Check if the player reached the finish line.

        Returns:
            bool: Whether the player reached the finish line or not.
        """
        if self.ycor() == FINISH_POINT:
            self.goto(START_POSITION)
            return True
        return False

    def __initial_config(self):
        """Set the geometry and color of the player and place it at the bottom of the screen."""
        self.shape("turtle")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)
