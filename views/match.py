# Import the arcade library
import arcade
import arcade.gui
# Import random library
import random


class Matching(arcade.View):    
    def __init__(self, HomeView):
        """Matching view, it is the game where you match the number.
        
        Structure:
            Starts by calling draw_board which makes background colors and general stuff in it then calls draw_question
                draw_question calls create_question then draw_problem and draw_answers
                    create_question creates the question ex. 17 and the answers ex. 3 dots, 17 dots, 9 dots and randomizes the answers
                    draw_problem only draws the problem
                    draw_answers only draws the answers and calls draw_circles
                        draw_circles draws each circle
            
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
        """
        super().__init__()
        self.HomeView = HomeView
        self.answered = False
        self.draw_board()
    
    def draw_board(self):
        """Draws the entire screen and creates the question"""
        # Set a background color
        arcade.set_background_color(arcade.color.CITRON)
        
        self.clear()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        # Draw the board
        arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.CORN)
        
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

        # This empty list will hold the answers
        self.answers = []

        # Set the answer
        self.answer = random.randrange(1, 20)
        self.answers.append(self.answer)
        
        # Creates the extra solutions
        # Randomly set the answers in range 1, 20
        self.answers.append(
            random.choice(
                [i for i in range(1, 20) if i not in self.answers]
            )
        )
        
        self.answers.append(
            random.choice(
                [i for i in range(1, 20) if i not in self.answers]
            )
        )

        # Use random.shuffle and to randomize the 3 options
        random.shuffle(self.answers)
    
    def draw_problem(self):
        """Draws the problem"""
        arcade.draw_text(self.answer,
            360, # starting x
            450, # starting y
            arcade.color.BLACK, # color
            60, # font size
            width=2, # width
            align="center" # alignment
        )
    
    def draw_answers(self):
        """Draws the 3 potential answers"""
        # Draw background of options
        arcade.draw_lrtb_rectangle_filled(80, 210, 230, 70, arcade.color.CITRON)
        arcade.draw_lrtb_rectangle_filled(330, 460, 230, 70, arcade.color.CITRON)
        arcade.draw_lrtb_rectangle_filled(580, 710, 230, 70, arcade.color.CITRON)

        # x, y, n
        answers = [
            (100, 200, self.answers[0]),
            (350, 200, self.answers[1]),
            (600, 200, self.answers[2])
        ]

        for (x, y, n) in answers:
            self.draw_circles(n, x, y)

    def draw_circles(self, n, x, y):
        """Draws the circles for an answer
        
        Arguments:
            n (int): answer/total amount of circles
            x (int): x to start at
            y (int): y to start at
        """
        # Split the Screen
        # Rectangle (left, right, top, bottom)
        c = x
        z = x + 80
        for i in range(n):
            arcade.draw_circle_filled(x, 10 + y, 10, arcade.color.BLACK)
            if x < z:
                x += 30
            else:
                x = c
                y -= 30

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
            (80, 210, 70, 230, self.answers[0]),
            (330, 460, 70, 230, self.answers[1]),
            (580, 710, 70, 230, self.answers[2])
        ]
        
        # Check if the player's mouse click is within the coordinates of a potential answer and call create_message_box.
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
