import arcade
import arcade.gui
from PressableButtons import PressableButtons


class MyWindow(arcade.Window):

    def __init__(self):
        super().__init__(1000, 750, "OKMessageBox Example", resizable=True)
        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)

        # Create and enable the UIManager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        buttons = PressableButtons(self.manager)

    def on_draw(self):
        self.clear()
        self.manager.draw()

window = MyWindow()
arcade.run()