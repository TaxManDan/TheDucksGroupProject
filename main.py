import arcade
import arcade.gui
from add_multiply_visuals import Addition, Multiplication, Matching


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

        buttons = [
            (0, -150, help_button),
            (0, 0, difficulty_button),
            (0, 150, play_button)
        ]

        for (x, y, button) in buttons:
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    # Positioning
                    anchor_x="center",
                    align_x=x,
                    anchor_y="center",
                    align_y=y,

                    child=button
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
            game_view = Matching()
        elif difficulty == "Normal":
            game_view = Addition()
        else:
            game_view = Multiplication()
        self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ducks Matching Game"

def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    start_view = HomeView()
    window.show_view(start_view)
    arcade.run()

main()
