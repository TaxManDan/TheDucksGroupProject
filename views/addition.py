# import the arcade library
import arcade
import arcade.gui
# import random library
import random


class Addition(arcade.View):
    def __init__(self):
        super().__init__()
        # Set a background color
        self.user_action = None
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
        self.clear()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # there can be addition or subtraction
        self.symbol = random.choice(['+', '-'])

        # This empty list will hold the answers
        self.answers = []

        # Set the first value
        self.n1 = random.randrange(0, 100)

        # I used an if statement because we don't want negative numbers when we subtract
        if self.symbol == '+':
            self.n2 = random.randrange(0, 100)
            # Add the answer to the list
            self.answer = self.n1 + self.n2
        else:
            self.n2 = random.randrange(0, self.n1)
            self.answer = self.n1 - self.n2
        self.answers.append(self.answer)

        # Draw the board
        arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.BABY_BLUE_EYES)
        self.set_answers()
        self.draw_problem()
        self.draw_answers()
        arcade.finish_render()

        # Creates group and centers the message box
        self.v_box = arcade.gui.UIBoxLayout()
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def draw_problem(self):
        # Draw the problem
        coords = [
            (200, 450, self.n1),
            (300, 450, self.symbol),
            (400, 450, self.n2),
            (550, 450, "=  ?")
        ]

        for (x, y, text) in coords:
            arcade.draw_text(
                text, x, y,
                arcade.color.WHITE,
                font_size=60,
                anchor_x="center"
            )

    def set_answers(self):
        # randomly set the answers in range 0, 200 max is 100 + 100
        ans1 = self.answers[0]
        ans2 = random.choice([i for i in range(0, 200) if i != ans1])
        ans3 = random.choice([i for i in range(0, 200) if i != ans1 and i != ans2])
        self.answers.append(ans2)
        self.answers.append(ans3)

        # Use random.shuffle and to randomize the 3 options
        random.shuffle(self.answers)

    def draw_answers(self):
        # Draw the boxes behind the options
        arcade.draw_lrtb_rectangle_filled(70, 230, 300, 150, arcade.color.LIGHT_BLUE)
        arcade.draw_lrtb_rectangle_filled(330, 470, 300, 150, arcade.color.LIGHT_BLUE)
        arcade.draw_lrtb_rectangle_filled(600, 740, 300, 150, arcade.color.LIGHT_BLUE)

        # x, y, n
        coords = [
            (150, 200, self.answers[0]),
            (400, 200, self.answers[1]),
            (670, 200, self.answers[2])
        ]

        for (x, y, n) in coords:
            arcade.draw_text(
                n, x, y,
                arcade.color.BANANA_MANIA,
                font_size=60,
                anchor_x="center"
            )

    # Creating function to check the mouse clicks
    def on_mouse_press(self, x, y, button, modifiers):
        # x_low, x_high, y_low, y_high, number
        coords = [
            (70, 230, 150, 300, self.answers[0]),
            (330, 470, 150, 300, self.answers[1]),
            (600, 740, 150, 300, self.answers[2])
        ]

        for (x_low, x_high, y_low, y_high, number) in coords:
            if x_low < x < x_high and y_low < y < y_high:
                if number == self.answer:
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
