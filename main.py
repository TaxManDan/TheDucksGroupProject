# import the arcade library
import arcade
import arcade.gui
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Math Game"

class StartMenu(arcade.View):
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
        self.clear()
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
        main_game = Game()
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


if __name__ == "__main__":
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    start_view = StartMenu()
    window.show_view(start_view)
    arcade.run()