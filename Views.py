import arcade
import arcade.gui
from PressableButtons import PressableButtons


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
            callback=self.on_diffuculty_box_close,
            buttons=["Easy", "Normal", "Hard"]
        )

        self.manager.add(message_box)

    def on_diffuculty_box_close(self, button_text):
        difficulty = button_text
        print(difficulty)

    def on_click_play(self, event):
        game_view = GameView()
        self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)

        # Create and enable the UIManager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        buttons = PressableButtons(self.manager)

    def on_draw(self):
        self.clear()
        self.manager.draw()


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Ducks Matching Game"


def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    start_view = LoadingView()
    window.show_view(start_view)
    arcade.run()


