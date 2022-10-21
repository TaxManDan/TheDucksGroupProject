import arcade
import arcade.gui


class MyWindow(arcade.Window):

    def __init__(self):
        super().__init__(1000, 750, "OKMessageBox Example", resizable=True)
        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)

        # Create and enable the UIManager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a box group to align the 'open' button in the center
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a button. We'll click on this to open our window.
        # Add it v_box for positioning.
        open_message_box_button = arcade.gui.UIFlatButton(text="Open", width=250)
        self.v_box.add(open_message_box_button)

        # Add a hook to run when we click on the button.
        open_message_box_button.on_click = self.on_click_open
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_open(self, event):
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
            buttons=["Ok", "Cancel", "Test"]
        )

        self.manager.add(message_box)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_message_box_close(self, button_text):
        print(f"User pressed {button_text}.")


window = MyWindow()
arcade.run()