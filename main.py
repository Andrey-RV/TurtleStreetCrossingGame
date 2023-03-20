import time
from turtle import Screen
from crossing_game import Player, Car, Scoreboard, save_best_try


def main() -> None:
    screen = Screen()
    screen.setup(width=1366, height=768)
    screen.tracer(0)

    turtle = Player()
    scoreboard = Scoreboard()
    cars: list[Car] = []

    screen.listen()
    screen.onkey(turtle.move_up, "Up")

    current_loop = 0
    game_is_on = True

    while game_is_on:
        if current_loop % 6 == 0:
            cars.append(Car())
        Car.move_the_cars(cars)

        if turtle.hit_a_car(cars):
            scoreboard.game_over()
            game_is_on = False
            save_best_try(scoreboard.level)

        if turtle.won():
            Car.increase_speed()
            scoreboard.go_to_next_level()

        current_loop += 1
        time.sleep(0.1)
        screen.update()


if __name__ == "__main__":
    main()
