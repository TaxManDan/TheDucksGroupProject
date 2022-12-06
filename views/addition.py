# Import the arcade library
import arcade
import arcade.gui
# Import random library
import random

class Addition(arcade.View):
    def __init__(self):
        """Addition view, it is the game with addition.
        
        Starts by calling draw_board which makes background colors and general stuff in it then calls draw_question
            draw_question calls create_question then draw_problem and draw_answers
                create_question creates the question ex. 25 + 9 and the answers ex. 3 34 28 and randomizes the answers
                draw_problem only draws the problem
                draw_answers only draws the answers
        
        Variables:
            manager (UIManager): Instance of arcade's UI Manager
            answer (int): The correct answer
            answers (list): List of all 3 potential answers
            n1 (int): The first part of the problem
            symbol (string): Will either be a + or a - and determines type of problem
            n2 (int): The second part of the problem
        """
        super().__init__()
        self.draw_board()
    
    def draw_board(self):
        """Draws the entire screen and creates the question"""
        # Set a background color
        arcade.set_background_color(arcade.color.AFRICAN_VIOLET)
        
        self.clear()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
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
            button (string): Button that is pressed
            modifiers (string: All modifiers (shift, ctrl, num lock) pressed during this event
        """
        # x_low, x_high, y_low, y_high, number
        coords = [
            (70, 230, 150, 300, self.answers[0]),
            (330, 470, 150, 300, self.answers[1]),
            (600, 740, 150, 300, self.answers[2])
        ]

        for (x_low, x_high, y_low, y_high, number) in coords:
            if x_low < x < x_high and y_low < y < y_high:
                if number == self.answer:
                    print("Y")
                    self.draw_board()
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
                else:
                    print("N")
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
        """Starts the drawing process"""
        self.clear()
        self.manager.draw()

    def on_message_box_close(self, button_text):
        """Checks what the user chose while closing the message box
        
        Arguments:
            button_text (string): The text of the button clicked
        """
        if button_text == "Home":
            print("Home")
        elif button_text == "Retry":
            print("Retry")
