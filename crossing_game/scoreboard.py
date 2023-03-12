from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        """_Class responsible for creating the scoreboard and updating it_

        Attributes:
            level (int): _The current level of the game_
        """
        super().__init__()
        self.level = 0
        self.__initial_config()

    def show_level(self) -> None:
        """_Show the current level of the game on the screen_"""
        self.write(f"Level: {self.level}", font=FONT)

    def go_to_next_level(self) -> None:
        """_Update the level shown on the screen_"""
        self.level += 1
        self.clear()
        self.show_level()

    def game_over(self) -> None:
        """_Show the game over message on the screen_"""
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

    def __initial_config(self) -> None:
        """_Set the initial configuration (such as position) of the scoreboard_"""
        self.hideturtle()
        self.penup()
        self.goto(x=-400, y=280)
        self.show_level()
