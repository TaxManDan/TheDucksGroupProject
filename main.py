# Import the arcade library
import arcade
import arcade.gui
# Import the views
from views.match import Matching
from views.addition import Addition
from views.multiplication import Multiplication


class HomeView(arcade.View):
    def __init__(self):
        """Main view, it is where you can navigate the actual game.
        
        Starts by calling draw_board which makes background colors and general stuff in it then calls draw_buttons
            draw_buttons draws each button and attaches their individual functions for when they are clicked
        
        Variables:
            manager (UIManager): Instance of arcade's UI Manager
            difficulty (string): Will either be Easy, Normal, or Hard to determine the difficulty
        """
        super().__init__()
        self.difficulty = "Normal"
        
        # Set a background color
        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.on_draw()
        
        self.draw_board()
        self.manager.draw()
        
        arcade.finish_render()
    
    def draw_board(self):
        """Draws the entire screen and creates the question"""
        # Set a background color
        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)
                
        self.draw_buttons() # Creates and draws the buttons
    
    def draw_buttons(self):
        """Creates and draws the buttons"""
        help_button = arcade.gui.UIFlatButton(text="HELP", width=200)
        difficulty_button = arcade.gui.UIFlatButton(text="DIFFICULTY", width=200)
        play_button = arcade.gui.UIFlatButton(text="PLAY", width=200)

        # Attaches their individual function to them
        help_button.on_click = self.on_click_help
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

    def on_click_play(self, _):
        """Gets called when the user clicks the play button, starts the game depending on difficulty"""
        if self.difficulty == "Easy":
            game_view = Matching(HomeView)
        elif self.difficulty == "Normal":
            game_view = Addition(HomeView)
        else:
            game_view = Multiplication(HomeView)
        self.window.show_view(game_view)

    def on_click_difficulty(self, _):
        """Gets called when the user clicks the difficulty button, shows options and let's them pick"""
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
        
        self.manager.draw()
        arcade.finish_render()

    def on_click_help(self, _):
        """Gets called when the user clicks the help button, shows a description of the game"""
        # The code below opens the message box and auto-dismisses it when done.
        message_box = arcade.gui.UIMessageBox(
            width=375,
            height=250,
            message_text=(
                "This is a math game that helps kids improve their arithmetic skills. The game has three difficulty levels: Easy, Normal, and Hard. In the Easy level, the game will show a number and the player has to match it with the correct amount of dots. In the Normal level, the game will show two numbers and the player has to either add or subtract them and select the correct answer. In the Hard level, the game will show two numbers and the player has to multiply them and select the correct answer. Good luck!"
            ),
            callback=self.on_help_box_close,
            buttons=["Ok"]
        )

        self.manager.add(message_box)
        
        self.manager.draw()
        arcade.finish_render()

    def on_difficulty_box_close(self, button_text):
        """Gets called when the difficulty box closes, sets the difficulty based on the button pressed
        
        Arguments:
            button_text (string): The text for the button pressed
        """
        self.difficulty = button_text
        print(self.difficulty)
        
        self.on_draw()
        self.draw_board()
        self.manager.draw()
        arcade.finish_render()
    
    def on_help_box_close(self, _):
        self.on_draw()
        self.draw_board()
        self.manager.draw()
        arcade.finish_render()

    def on_draw(self):
        """Starts the drawing process"""
        self.clear()
        self.manager.draw()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ducks Matching Game"

if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
    start_view = HomeView()
    window.show_view(start_view)
    arcade.run()
