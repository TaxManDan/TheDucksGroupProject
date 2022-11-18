# import the arcade library
import arcade
import arcade.gui
# import random library
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Math Game"


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

        self.numbers = self.set_numbers()
        self.numbers.append(self.my_number)
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
        arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.CORN)
        x1 = 100
        y1 = 200
        n1 = random.choice(self.numbers)
        self.draw_visuals(n1, x1, y1)

        self.numbers.remove(n1)
        x2 = 350
        y2 = 200
        n2 = random.choice(self.numbers)

        self.draw_visuals(n2, x2, y2)

        self.numbers.remove(n2)
        x3 = 600
        y3 = 200
        n3 = self.numbers[0]

        self.draw_visuals(n3, x3, y3)

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



class Addition(arcade.View):
    def __init__(self):
        super().__init__()
        # set a background color
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
        self.clear()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # there can be addition or subtraction
        self.symbols = ['+', '-']
        self.s = random.choice(self.symbols)

        # this empty list will hold the answers
        self.a = []

        # set the first value
        self.n1 = random.randrange(0, 100)

        # I used an if statement because we don't want negative numbers when we subtract
        if self.s == '+':
            self.n2 = random.randrange(0, 100)
            self.ans = self.n1 + self.n2
            # add the answer to the list
            self.a.append(self.ans)

        else:
            self.n2 = random.randrange(0, self.n1)
            self.ans = self.n1 - self.n2
            self.a.append(self.ans)

        # draw the board
        arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.BABY_BLUE_EYES)
        self.answers()
        self.draw_problem()
        self.draw_answers()
        arcade.finish_render()

    def draw_problem(self):
        # draw the problem
        arcade.draw_text(self.n1, 200, 450,
                         arcade.color.WHITE, font_size=60, anchor_x="center")
        arcade.draw_text(self.s, 300, 450,
                         arcade.color.WHITE, font_size=60, anchor_x="center")
        arcade.draw_text(self.n2, 400, 450,
                         arcade.color.WHITE, font_size=60, anchor_x="center")
        arcade.draw_text("=  ?", 550, 450,
                         arcade.color.WHITE, font_size=60, anchor_x="center")

    def answers(self):
        # randomly set the answers in range 0, 200 max is 100 + 100
        ans = self.ans
        a = self.a
        ans2 = random.choice([i for i in range(0, 200) if i != ans])
        ans3 = random.choice([i for i in range(0, 200) if i != ans and i != ans2])
        a.append(ans2)
        a.append(ans3)

    def draw_answers(self):
        # use random.choice and remove to randomly place the 3 answers
        a = self.a
        n1 = random.choice(a)
        a.remove(n1)
        n2 = random.choice(a)
        a.remove(n2)
        n3 = a[0]
        arcade.draw_text(n1, 150, 200,
                         arcade.color.BANANA_MANIA, font_size=60, anchor_x="center")
        arcade.draw_text(n2, 400, 200,
                         arcade.color.BANANA_MANIA, font_size=60, anchor_x="center")
        arcade.draw_text(n3, 670, 200,
                         arcade.color.BANANA_MANIA, font_size=60, anchor_x="center")


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

        # set the answer and add to a list
        self.ans = self.n1 * self.n2
        self.a = [self.ans]

        # draw the game
        arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.BURNT_ORANGE)
        self.answers()
        self.draw_problem()
        self.draw_answers()
        arcade.finish_render()

    def draw_problem(self):
        # draw the problem
        arcade.draw_text(self.n1, 200, 450,
                         arcade.color.BLACK, font_size=60, anchor_x="center")
        arcade.draw_text('x', 300, 450,
                         arcade.color.BLACK, font_size=60, anchor_x="center")
        arcade.draw_text(self.n2, 400, 450,
                         arcade.color.BLACK, font_size=60, anchor_x="center")
        arcade.draw_text("=  ?", 550, 450,
                         arcade.color.BLACK, font_size=60, anchor_x="center")

    def answers(self):
        # add the answers to list a in range 0,144 because max is 12*12
        ans = self.ans
        a = self.a
        ans2 = random.choice([i for i in range(0, 144) if i != ans])
        ans3 = random.choice([i for i in range(0, 144) if i != ans and i != ans2])
        a.append(ans2)
        a.append(ans3)

    def draw_answers(self):
        # using random and remove draw the answers in a random order
        a = self.a
        n1 = random.choice(a)
        a.remove(n1)
        n2 = random.choice(a)
        a.remove(n2)
        n3 = a[0]
        arcade.draw_text(n1, 150, 200,
                         arcade.color.BLACK, font_size=60, anchor_x="center")
        arcade.draw_text(n2, 400, 200,
                         arcade.color.BLACK, font_size=60, anchor_x="center")
        arcade.draw_text(n3, 670, 200,
                         arcade.color.BLACK, font_size=60, anchor_x="center")
