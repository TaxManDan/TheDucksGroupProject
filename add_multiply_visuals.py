# import the arcade library
import arcade
import arcade.gui
# import random library
import random

# CHANGE on_mouse_press COORDS FOR ADDITION

class Matching(arcade.View):
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

        # Create self.numbers and randomize it
        self.numbers = self.set_numbers()
        self.numbers.append(self.my_number)
        random.shuffle(self.numbers)

        self.text()
        self.set_visuals()
        # --- Finish drawing ---
        arcade.finish_render()
        # Keep the window up until someone closes it.

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
                else:
                    print("N")


class Addition(arcade.View):
    def __init__(self):
        super().__init__()
        # Set a background color
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
                else:
                    print("N")

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
