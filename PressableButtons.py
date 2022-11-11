import arcade
import arcade.gui


class PressableButtons:
    def __init__(self, uimanager):
        self.uimanager = uimanager

        self.add_button("center_x", 250, "top", -100, True, 'Option A')
        self.add_button("center_x", 0, "top", -100, False, 'Option B')
        self.add_button("center_x", -250, "top", -100, False, 'Option C')

        self.draw()
    
    def add_button(self, anchor_x, align_x, anchor_y, align_y, correct, text = ""):
        button = arcade.gui.UIFlatButton(text=text, WIDTH=100)

        button_box = arcade.gui.UIBoxLayout() # Create a box group to align the 'open' button in the center
        button_box.add(button) # Create a button. We'll click on this to open our window.
        button.on_click = self.on_click_open_correct if correct else self.on_click_open_incorrect # Add a hook to run when we click on the button.

        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                # Positioning for first option
                anchor_x=anchor_x,
                align_x=align_x,
                anchor_y=anchor_y,
                align_y=align_y,

                child=button
            )
        )
    
    def on_click_open_incorrect(self, event):
        # The code in this function is run when we click the ok button.
        # The code below opens the message box and auto-dismisses it when done.
        message_box = arcade.gui.UIMessageBox(
            width=375,
            height=250,
            message_text=(
                "Incorrect, try again next time."
            ),
            callback=self.on_message_box_close,
            buttons=["Ok", "Cancel", "Test"]
        )

        self.uimanager.add(message_box)
    
    def on_click_open_correct(self, event):
        # The code in this function is run when we click the ok button.
        # The code below opens the message box and auto-dismisses it when done.
        message_box = arcade.gui.UIMessageBox(
            width=375,
            height=250,
            message_text=(
                "Congratulations! You got it right!"
            ),
            callback=self.on_message_box_close,
            buttons=["Ok", "Cancel", "Test"]
        )

        self.uimanager.add(message_box)
    
    def on_message_box_close(self, button_text):
        print(f"User pressed {button_text}.")

    def draw(self):
        arcade.start_render()

        self.uimanager.draw()
