from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        """Class responsible to create and update the scoreboard.

        Attributes:
            level (int): The current level of the game.
        """
        super().__init__()
        self.level = 0
        self.__initial_config()

    def show_level(self) -> None:
        """Show the current level of the game on the screen."""
        self.write(f"Level: {self.level}", font=FONT)

    def go_to_next_level(self) -> None:
        """Update the level shown on the screen."""
        self.level += 1
        self.clear()
        self.show_level()

    def game_over(self) -> None:
        """Show the game over message on the screen."""
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

    def __initial_config(self) -> None:
        """Set the initial configuration (such as position) of the scoreboard."""
        self.hideturtle()
        self.penup()
        self.goto(x=-400, y=280)
        self.show_level()
