import os


def save_best_try(current_level: int) -> None:
    """Save the best try in a file.

    Args:
        current_level (int): The current level of the player.
    """
    if not os.path.isfile("best_try.txt"):
        with open("best_try.txt", "w") as f:
            f.write("0")

    with open("best_try.txt", "r+") as f:
        if not f.read().isdigit():
            f.seek(0)
            f.truncate(0)
            f.write("0")

        f.seek(0)
        best_try = int(f.read())
        if current_level > best_try:
            f.seek(0)
            f.write(str(current_level))
