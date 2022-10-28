# import the arcade library
import arcade
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

    numbers = set_visuals(my_number)
    numbers.append(my_number)
    text(my_number)
    draw_visuals(numbers)

    # --- Finish drawing ---
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()

def text(x):
    arcade.draw_text(x,
                      360,     # starting x
                      450,      # starting y
                      arcade.color.BLACK,   # color
                      60,       # font size
                      width = 2,    # width
                      align = "center") # alignment
def set_visuals(x):
    num1 = random.choice([i for i in range(1, 20) if i != x])
    num2 = random.choice([i for i in range(1, 20) if i != x or i != num1])
    return [num1, num2]

def draw_visuals(numbers):
    x1 = 100
    y1 = 200
    n1 = random.choice(numbers)
    for i in range(n1):
        arcade.draw_circle_filled(x1, 10 + y1, 10, arcade.color.BLACK)
        if x1 < 180:
            x1 += 30
        else:
            x1 = 100
            y1 -= 30

    numbers.remove(n1)
    x2 = 350
    y2 = 200
    n2 = random.choice(numbers)

    for i in range(n2):
        arcade.draw_circle_filled(x2, 10 + y2, 10, arcade.color.BLACK)
        if x2 < 430:
            x2 += 30
        else:
            x2 = 350
            y2 -= 30

    numbers.remove(n2)
    x3 = 600
    y3 = 200
    n3 = numbers[0]

    for i in range(n3):
        arcade.draw_circle_filled(x3, 10 + y3, 10, arcade.color.BLACK)
        if x3 < 680:
            x3 += 30
        else:
            x3 = 600
            y3 -= 30


main()
