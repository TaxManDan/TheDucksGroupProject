import arcade
import arcade.gui


class PressableButtons:
    def __init__(self):
        self.uimanager = arcade.gui.UIManager
        self.uimanager.enable()

        # Create the three buttons for the three options the user can choose from
        first_button = arcade.gui.UIFlatButton(TEXT="", WIDTH=100)
        second_button = arcade.gui.UIFlatButton(TEXT="", WIDTH=100)
        third_button = arcade.gui.UIFlatButton(TEXT="", WIDTH=100)

        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                # Positioning for first option
                anchor_x="center_x",
                anchor_y="center_y",

                child=first_button)
            )

        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                # Positioning for second option
                anchor_x="center_x",
                anchor_y="center_y",

                child=second_button)
        )

        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                # Positioning for third option
                anchor_x="center_x",
                anchor_y="center_y",

                child=third_button)
        )


# Handles button click event when any of the three options are chosen.
def button_click(self, event):
    print("You clicked a button!")


def draw(self):
    arcade.start_render()

    self.uimanager.draw()
