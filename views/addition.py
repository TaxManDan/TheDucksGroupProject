# Import the arcade library
import arcade
import arcade.gui
# Import random library
import random

class Addition(arcade.View):
    def __init__(self, HomeView):
        """Addition view, it is the game with addition.
        
        Structure:
            Starts by calling draw_board which makes background colors and general stuff in it then calls draw_question
                draw_question calls create_question then draw_problem and draw_answers
                    create_question creates the question ex. 25 + 9 and the answers ex. 3 34 28 and randomizes the answers
                    draw_problem only draws the problem
                    draw_answers only draws the answers

            on_mouse_press gets called after the user clicks, if the prompt is up (check self.answered) returns otherwise
            it calls create_message_box
                create_message_box creates a message box that either sends the user home or lets them play again
                    It calls on_message_box_close when the buttons get picked and does the action.
        
        Variables:
            manager (UIManager): Instance of arcade's UI Manager
            HomeView (HomeView): HomeView to be called when user wants to go back
            answer (int): The correct answer
            answers (list): List of all 3 potential answers
            answered (boolean): If the user has the prompt open
            n1 (int): The first part of the problem
            symbol (string): Will either be a + or a - and determines type of problem
            n2 (int): The second part of the problem
        """
        super().__init__()
        self.HomeView = HomeView
        self.answered = False
        self.draw_board()
    
    def draw_board(self):
        """Draws the entire screen and creates the question"""
        # Set a background color
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.on_draw()
        
        # Draw the board
        arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.BABY_BLUE_EYES)
        
        self.draw_question() # Creates and draws the question
        
        arcade.finish_render()
    
    def draw_question(self):
        """Creates and draws the problem/solution"""
        self.create_question() # This will create the problem and potential solutions        
        self.draw_problem() # This will draw the problem shown at the top
        self.draw_answers() # This will draw the 3 potential answers
    
    def create_question(self):
        """Creates the info for the question including the problem and the solution"""
        # Creates the problem
        # There can be addition or subtraction
        self.symbol = random.choice(['+', '-'])

        # This empty list will hold the answers
        self.answers = []

        # Set the first value
        self.n1 = random.randrange(0, 100)

        # I used an if statement because we don't want negative numbers when we subtract
        if self.symbol == '+':
            self.n2 = random.randrange(0, 100)
            # Create the answer
            self.answer = self.n1 + self.n2
        else:
            self.n2 = random.randrange(0, self.n1)
            # Create the answer
            self.answer = self.n1 - self.n2
        self.answers.append(self.answer)
        
        
        # Creates the extra solutions
        # Randomly set the answers in range 0, 200 max is 100 + 100
        self.answers.append(
            random.choice(
                [i for i in range(0, 200) if i not in self.answers]
            )
        )
        
        self.answers.append(
            random.choice(
                [i for i in range(0, 200) if i not in self.answers]
            )
        )

        # Use random.shuffle and to randomize the 3 options
        random.shuffle(self.answers)

    def draw_problem(self):
        """Draws the problem"""
        part = [
            (200, 450, self.n1),
            (300, 450, self.symbol),
            (400, 450, self.n2),
            (550, 450, "=  ?")
        ]

        for (x, y, text) in part:
            arcade.draw_text(
                text, x, y,
                arcade.color.WHITE,
                font_size=60,
                anchor_x="center"
            )

    def draw_answers(self):
        """Draws the 3 potential answers"""
        # Draw the boxes behind the options
        arcade.draw_lrtb_rectangle_filled(70, 230, 300, 150, arcade.color.LIGHT_BLUE)
        arcade.draw_lrtb_rectangle_filled(330, 470, 300, 150, arcade.color.LIGHT_BLUE)
        arcade.draw_lrtb_rectangle_filled(600, 740, 300, 150, arcade.color.LIGHT_BLUE)

        # x, y, n
        answers = [
            (150, 200, self.answers[0]),
            (400, 200, self.answers[1]),
            (670, 200, self.answers[2])
        ]

        for (x, y, n) in answers:
            arcade.draw_text(
                n, x, y,
                arcade.color.BANANA_MANIA,
                font_size=60,
                anchor_x="center"
            )

    def on_mouse_press(self, x, y, button, modifiers):
        """Checks the area of mouse click to see if it is in the answers zones then displays the appropriate message.
        
        Arguments:
            x (int): The x of the position where the user clicked
            y (int): The y of the position where the user clicked
            button (int): Button that is pressed
            modifiers (int: All modifiers (shift, ctrl, num lock) pressed during this event
        """
        # Ends if the play again or go home prompt is up
        if self.answered:
            return
        
        # x_low, x_high, y_low, y_high, number
        coords = [
            (70, 230, 150, 300, self.answers[0]),
            (330, 470, 150, 300, self.answers[1]),
            (600, 740, 150, 300, self.answers[2])
        ]
        
        for (x_low, x_high, y_low, y_high, number) in coords:
            if x_low < x and x < x_high and y_low < y and y < y_high:
                correct = number == self.answer
                print(correct)
                self.create_message_box(correct)
    
    def create_message_box(self, correct):
        """Creates a message box with telling the user if they got it right and
        letting them go back to the game or go home
        
        Arguments:
            correct (boolean): If the user was right or not
        """
        self.answered = True # For if this is up.
        
        # Set a background color
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
        
        # Sets text
        if correct:
            text = f"Correct! It indeed was {self.answer}.\nDo you want to play again or go home?"
        else:
            text = f"Sorry! The correct answer was {self.answer}.\nDo you want to play again or go home?"
        
        # Create the message box
        message_box = arcade.gui.UIMessageBox(
            width=375,
            height=250,
            message_text=text,
            callback = self.on_message_box_close,
            buttons=["Play again!", "Go home"]
        )

        # Add the message box to the UI manager
        self.manager.add(message_box)
        
        # Draw the screen
        self.manager.draw()
        arcade.finish_render()

    def on_message_box_close(self, button_text):
        """Called when message box is closed and either sends user home or back
        to their game.

        Arguments:
            button_text (string): The text for the button pressed
        """
        self.answered = False # To say this prompt is gone
        
        if button_text == "Play again!":
            # Call the draw_question method to show the next problem
            self.draw_board()
        else:
            # Create an instance of the HomeView class
            home_view = self.HomeView()
            self.window.show_view(home_view)

    def on_draw(self):
        """Starts the drawing process"""
        self.clear()
        self.manager.draw()