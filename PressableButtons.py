import arcade
import arcade.gui


class PressableButtons:
    def __init__(self):
        self.uimanager = arcade.gui.UIManager
        self.uimanager.enable()

        first_button = arcade.gui.UIFlatButton(TEXT="", WIDTH=100)

        second_button = arcade.gui.UIFlatButton(TEXT="", WIDTH=100)

        third_button = arcade.gui.UIFlatButton(TEXT="", WIDTH=100)

        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=first_button)
            )

        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=second_button)
        )

        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=third_button)
        )


def button_click(self, event):
    print("You clicked a button!")


def draw(self):
    arcade.start_render()

    self.uimanager.draw()
