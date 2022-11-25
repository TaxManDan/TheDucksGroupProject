# Import the arcade library
import arcade
import arcade.gui
# Import random library
import random


class Matching(arcade.View):
    def __init__(self):
        super().__init__()
        # set a background color
        self.user_action = None
        arcade.set_background_color(arcade.color.CITRON)
        self.clear()
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # set a random number between 1-20
        self.my_number = random.randrange(1, 20)

        # Create self.numbers and randomize it
        self.numbers = self.set_numbers()
        self.numbers.append(self.my_number)
        random.shuffle(self.numbers)

        self.text()
        self.set_visuals()
        # --- Finish drawing ---
        arcade.finish_render()
        # Keep the window up until someone closes it.

        # Creates group and centers the message box
        self.v_box = arcade.gui.UIBoxLayout()
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

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
        # Draw background
        arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.CORN)
        # Draw background of options
        arcade.draw_lrtb_rectangle_filled(80, 210, 230, 70, arcade.color.CITRON)
        arcade.draw_lrtb_rectangle_filled(330, 460, 230, 70, arcade.color.CITRON)
        arcade.draw_lrtb_rectangle_filled(580, 710, 230, 70, arcade.color.CITRON)

        # x, y, n
        coords = [
            (100, 200, self.numbers[0]),
            (350, 200, self.numbers[1]),
            (600, 200, self.numbers[2])
        ]

        for (x, y, n) in coords:
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

    # Creating function to check the mouse clicks
    def on_mouse_press(self, x, y, button, modifiers):
        # x_low, x_high, y_low, y_high, number
        coords = [
            (80, 210, 70, 230, self.numbers[0]),
            (330, 460, 70, 230, self.numbers[1]),
            (580, 710, 70, 230, self.numbers[2])
        ]

        for (x_low, x_high, y_low, y_high, number) in coords:
            if x_low < x < x_high and y_low < y < y_high:
                if number == self.my_number:
                    print("Y")
                    message_box = arcade.gui.UIMessageBox(
                        width=400,
                        height=300,
                        message_text=(
                            "Correct! You got it right."
                            "Would you like to play again?"
                        ),
                        callback=self.on_message_box_close,
                        buttons=["Home", "Retry"]
                    )

                    self.manager.add(message_box)
                else:
                    print("N")
                    message_box = arcade.gui.UIMessageBox(
                        width=400,
                        height=300,
                        message_text=(
                            "Sorry! That wasn't correct."
                            "Would you like to try again?"
                        ),
                        callback=self.on_message_box_close,
                        buttons=["Home", "Retry"]
                    )

                    self.manager.add(message_box)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_message_box_close(self, button_text):
        self.user_action = button_text

        if self.user_action == "Home":
            print("Home")
        elif self.user_action == "Retry":
            print("Retry")
