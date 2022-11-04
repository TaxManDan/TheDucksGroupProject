# import the arcade library
import arcade
import arcade.gui
# import random library
import random


def main():
    # open a window to draw in
    arcade.open_window(800, 600, "Math Game")

    # set a background color
    arcade.set_background_color(arcade.color.CITRON)
    # Get ready to draw
    arcade.start_render()

    # Split the Screen
    # Rectangle (left, right, top, bottom)
    arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.CORN)
    # set a random number between 1-20
    my_number = random.randrange(1, 20)

    numbers = set_numbers(my_number)
    numbers.append(my_number)
    text(my_number)
    set_visuals(numbers)

    # --- Finish drawing ---
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()


def text(x):
    arcade.draw_text(x,
                     360,  # starting x
                     450,  # starting y
                     arcade.color.BLACK,  # color
                     60,  # font size
                     width=2,  # width
                     align="center")  # alignment


def set_numbers(x):
    num1 = random.choice([i for i in range(1, 20) if i != x])
    num2 = random.choice([i for i in range(1, 20) if i != x or i != num1])
    return [num1, num2]


def set_visuals(numbers):
    x1 = 100
    y1 = 200
    n1 = random.choice(numbers)
    draw_visuals(n1, x1, y1)

    numbers.remove(n1)
    x2 = 350
    y2 = 200
    n2 = random.choice(numbers)

    draw_visuals(n2, x2, y2)

    numbers.remove(n2)
    x3 = 600
    y3 = 200
    n3 = numbers[0]

    draw_visuals(n3, x3, y3)


def draw_visuals(n, x, y):
    c = x
    z = x + 80
    for i in range(n):
        arcade.draw_circle_filled(x, 10 + y, 10, arcade.color.BLACK)
        if x < z:
            x += 30
        else:
            x = c
            y -= 30


main()
