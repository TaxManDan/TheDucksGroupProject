# import the arcade library
import arcade
import arcade.gui
# import random library
import random

class Game(arcade.View):
    def __init__(self):
        super().__init__()
        # set a background color
        arcade.set_background_color(arcade.color.CITRON)
        self.clear()
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # set a random number between 1-20
        self.my_number = random.randrange(1, 20)

        self.numbers = self.set_numbers()
        self.numbers.append(self.my_number)
        self.text()
        self.set_visuals()
        # --- Finish drawing ---
        arcade.finish_render()
        # Keep the window up until someone closes it.

        self.p = []  # Used for player input

    def text(self):
        arcade.draw_text(self.my_number,
                         360,  # starting x
                         450,  # starting y
                         arcade.color.BLACK,  # color
                         60,  # font size
                         width=2,  # width
                         align="center")  # alignment

    def set_numbers(self):
        num1 = random.choice([i for i in range(1, 20) if i != self.my_number])
        num2 = random.choice([i for i in range(1, 20) if i != self.my_number and i != num1])

        return [num1, num2]

    def set_visuals(self):
        arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.CORN)
        coords = [(100, 200), (350, 200), (600, 200)]

        arcade.draw_lrtb_rectangle_filled(80, 210, 230, 70, arcade.color.CITRON)
        arcade.draw_lrtb_rectangle_filled(330, 460, 230, 70, arcade.color.CITRON)
        arcade.draw_lrtb_rectangle_filled(580, 710, 230, 70, arcade.color.CITRON)

        for (x, y) in coords:
            n = random.choice(self.numbers)
            self.draw_visuals(n, x, y)

    def draw_visuals(self, n, x, y):
        # Split the Screen
        # Rectangle (left, right, top, bottom)
        c = x
        z = x + 80
        for i in range(n):
            arcade.draw_circle_filled(x, 10 + y, 10, arcade.color.BLACK)
            if x < z:
                x += 30
            else:
                x = c
                y -= 30

    def on_mouse_press(self, x, y, button, modifiers):
        # checks the square and passes input to the answer function to get checked
        if 80 < x < 210 and 70 < y < 230:
            # First choice (left)
            self.p.append("1")  # Might need to remove from array once click is deemed correct or not
            print("You chose" + str(self.p))

        elif 330 < x < 460 and 70 < y < 230:
            # Second choice (Middle)
            self.p.append("2")  # Might need to remove from array once click is deemed correct or not
            print("You chose" + str(self.p))

        elif 580 < x < 710 and 70 < y < 230:
            # Third choice (right)
            self.p.append("3")  # Might need to remove from array once click is deemed correct or not
            print("You chose" + str(self.p))