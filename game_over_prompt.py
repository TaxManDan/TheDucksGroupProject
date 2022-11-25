import arcade
import arcade.gui

from main import HomeView


class GameOverPrompt(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "", resizable=True)
        self.user_action = None
        arcade.set_background_color(arcade.color.WHITE)

        # Enable UI Manager for this class
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Creates group and centers the message box
        self.v_box = arcade.gui.UIBoxLayout()
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def correct(self):
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

    def incorrect(self):
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
            HomeView()
        elif self.user_action == "Retry":
            print("Retry")
