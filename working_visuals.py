# import the arcade library
import arcade
import arcade.gui
# import random library
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Math Game"


class InstructionView(arcade.View):
    """ View to show instructions """

    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.color.BLUE)
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)


    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_text("Welcome to the Math Game", self.window.width / 2, self.window.height / 1.5,
                         arcade.color.WHITE, font_size=40, anchor_x="center")
        # arcade.draw_text("Click to Start", self.window.width / 2, self.window.height / 2-75,
                         # arcade.color.WHITE, font_size=20, anchor_x="center")
        start_button = arcade.gui.UIFlatButton(text="Click Here To Start",
                                               width=200)
        instruction_button = arcade.gui.UIFlatButton(text="Click Here For Instructions",
                                               width=200)

        # Assigning our on_buttonclick() function
        start_button.on_click = self.on_startclick
        instruction_button.on_click = self.on_instructionclick


        # Adding button in our uimanager
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=-200,
                anchor_y="center_y",
                align_y=-100,
                child=start_button)
        )
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=200,
                anchor_y="center_y",
                align_y=-100,
                child=instruction_button)
        )
        self.uimanager.draw()

    def on_startclick(self, event):
        """ If the user presses the mouse button, start the game. """
        self.uimanager.clear()
        main_game = MainGame()
        # main_game.set_visuals()
        self.window.show_view(main_game)

    def on_instructionclick(self, event):
        # The code in this function is run when we click the ok button.
        # The code below opens the message box and auto-dismisses it when done.
        message_box = arcade.gui.UIMessageBox(
            width=375,
            height=150,
            message_text=(
                "When you click start you will see a number at the top center screen "
                "Below there will be three visuals. Click on the visual that matches "
                "the number. Good Luck!"
            ),
            callback=self.on_message_box_close,
            buttons=["Close"]
        )

        self.uimanager.add(message_box)

    def on_message_box_close(self, button_text):
        print(f"User pressed {button_text}.")

class MainGame(arcade.View):
    def __init__(self):
        super().__init__()
        # set a background color
        arcade.set_background_color(arcade.color.CITRON)

        self.clear()
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        
        # x and y are needed to initialize the mouse class
        self.x = 100
        self.y = 100
        
        # These are the numbers I need later on make sure to initialize them to be passed between functions
        # set a random number between 1-20
        self.my_number = random.randrange(1, 20)
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0

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
        arcade.draw_lrtb_rectangle_filled(80, 210, 230, 70, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(330, 460, 230, 70, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(580, 710, 230, 70, arcade.color.WHITE)
        x1 = 100
        y1 = 200
        self.n1 = random.choice(self.numbers)
        self.draw_visuals(self.n1, x1, y1)

        self.numbers.remove(self.n1)
        x2 = 350
        y2 = 200
        self.n2 = random.choice(self.numbers)

        self.draw_visuals(self.n2, x2, y2)

        self.numbers.remove(self.n2)
        x3 = 600
        y3 = 200
        self.n3 = self.numbers[0]

        self.draw_visuals(self.n3, x3, y3)

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

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.x = x
        self.y = y

    # Creating function to check the mouse clicks
    def on_mouse_press(self, x, y, button, modifiers):
        # the first variable is from set_visuals n1 is the first square etc. my_number is the correct answer
        # may not even need a function could jsut say if n1 == my_number
        if 80 < x < 210 and 70 < y < 230:
            if correct(self.n1, self.my_number):
                print("Y")
            else:
                print("N")

        elif 330 < x < 460 and 70 < y < 230:
            if correct(self.n2, self.my_number):
                print("Y")
            else:
                print("N")

        elif 580 < x < 710 and 70 < y < 230:
            if correct(self.n3, self.my_number):
                print("Y")
            else:
                print("N")


def correct(x, a):
    if x == a:
        return True
    else:
        return False


def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()



