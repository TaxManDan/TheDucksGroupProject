# Import the arcade library
import arcade
import arcade.gui
# Import random library
import random

class Multiplication(arcade.View):
    def __init__(self):
        super().__init__()
        # set a background color
        arcade.set_background_color(arcade.color.ALABAMA_CRIMSON)
        self.clear()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # set the 2 numbers
        self.n1 = random.randrange(0, 12)
        self.n2 = random.randrange(0, 12)

        # Set the answer and add to a list
        self.answer = self.n1 * self.n2
        self.answers = [self.answer]

        # draw the game
        arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.BURNT_ORANGE)
        self.set_answers()
        self.draw_problem()
        self.draw_answers()
        arcade.finish_render()

    def draw_problem(self):
        # Draw the problem
        # x, y, text
        coords = [
            (200, 450, self.n1),
            (300, 450, "x"),
            (400, 450, self.n2),
            (550, 450, "=  ?")
        ]

        for (x, y, text) in coords:
            arcade.draw_text(
                text, x, y,
                arcade.color.BLACK,
                font_size=60,
                anchor_x="center"
            )

    def set_answers(self):
        # add the answers to list a in range 0,144 because max is 12*12
        ans1 = self.answers[0]
        ans2 = random.choice([i for i in range(0, 144) if i != ans1])
        ans3 = random.choice([i for i in range(0, 144) if i != ans1 and i != ans2])

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
                else:
                    print("N")