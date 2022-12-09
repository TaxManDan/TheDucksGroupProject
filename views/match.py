# Import the arcade library
import arcade
import arcade.gui
# Import random library
import random


class Matching(arcade.View):    
    def __init__(self):
        """Matching view, it is the game where you match the number.
        
        Starts by calling draw_board which makes background colors and general stuff in it then calls draw_question
            draw_question calls create_question then draw_problem and draw_answers
                create_question creates the question ex. 17 and the answers ex. 3 dots, 17 dots, 9 dots and randomizes the answers
                draw_problem only draws the problem
                draw_answers only draws the answers and calls draw_circles
                    draw_circles draws each circle
        
        Variables:
            manager (UIManager): Instance of arcade's UI Manager
            answer (int): The correct answer
            answers (list): List of all 3 potential answers
        """
        super().__init__()
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
        # x_low, x_high, y_low, y_high, number
        coords = [
            (80, 210, 70, 230, self.answers[0]),
            (330, 460, 70, 230, self.answers[1]),
            (580, 710, 70, 230, self.answers[2])
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
