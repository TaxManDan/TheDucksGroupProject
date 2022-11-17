# import the arcade library
import arcade
import arcade.gui
# import random library
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Math Game"


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
