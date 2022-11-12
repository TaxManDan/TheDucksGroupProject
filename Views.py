import arcade
import arcade.gui
import random



class LoadingView(arcade.View):
    """ View to show instructions """

    def on_show_view(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        arcade.draw_text("Loading Screen", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, show the Home Screen. """
        home_view = HomeView()
        self.window.show_view(home_view)


class HomeView(arcade.View):

    def __init__(self):
        super().__init__()

        # Create and enable the UIManager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.difficulty = "Normal"

        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)

        help_button = arcade.gui.UIFlatButton(text="HELP", width=200)
        difficulty_button = arcade.gui.UIFlatButton(text="DIFFICULTY", width=200)
        play_button = arcade.gui.UIFlatButton(text="PLAY", width=200)

        button_box = arcade.gui.UIBoxLayout()  # Create a box group to align the 'open' button in the center
        button_box.add(help_button)  # Create a button. We'll click on this to open our window.
        button_box.add(difficulty_button)
        button_box.add(play_button)
        help_button.on_click = self.on_click_help  # Add a hook to run when we click on the button.
        difficulty_button.on_click = self.on_click_difficulty
        play_button.on_click = self.on_click_play

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                # Positioning for first option
                anchor_x="center",
                align_x=0,
                anchor_y="center",
                align_y=-150,


                child=help_button
            )
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                align_x=0,
                anchor_y="center",
                align_y=0,


                child=difficulty_button
            )
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                align_x=0,
                anchor_y="center",
                align_y=150,

                child=play_button
            )
        )


    def on_click_help(self, event):
        # The code in this function is run when we click the ok button.
        # The code below opens the message box and auto-dismisses it when done.
        message_box = arcade.gui.UIMessageBox(
            width=375,
            height=250,
            message_text=(
                "This is a Help Message box for giving users in game hints "
                "click ok to close."
            ),
            callback=self.on_message_box_close,
            buttons=["Ok", "Cancel"]
        )

        self.manager.add(message_box)

    def on_message_box_close(self, button_text):
        print(f"User pressed {button_text}.")

    def on_click_difficulty(self, event):
        # The code in this function is run when we click the ok button.
        # The code below opens the message box and auto-dismisses it when done.
        message_box = arcade.gui.UIMessageBox(
            width=350,
            height=125,
            message_text=(
                "Select the difficulty you want to play at."

            ),
            callback=self.on_difficulty_box_close,
            buttons=["Easy", "Normal", "Hard"]
        )

        self.manager.add(message_box)

    def on_difficulty_box_close(self, button_text):
        self.difficulty = button_text
        print(self.difficulty)

    def on_click_play(self, event):
        difficulty = self.difficulty
        if difficulty == "Easy":
            game_view = EasyView()
        elif difficulty == "Normal":
            game_view = NormalView()
        self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()


class EasyView(arcade.View):
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


class NormalView(arcade.View):
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

        # --- Finish drawing ---
        arcade.finish_render()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Ducks Matching Game"


def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    start_view = LoadingView()
    window.show_view(start_view)
    arcade.run()


