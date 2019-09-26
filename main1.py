#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines
"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade #telling the computer to access the arcade library installed into python, the program needed to run the code

SCREEN_WIDTH = 640 #setting the width of the display screen
SCREEN_HEIGHT = 480 #setting the height of the display screen
SCREEN_TITLE = "Move Mouse Example" #giving the display screen a title in the top corner


class Ball: #establishing that there will be an object created on screen
    def __init__(self, position_x, position_y, radius, color): #establishing how that object will be defined and placed on screen

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x #telling the computer the x postion of the ball will be mouse tracking
        self.position_y = position_y #telling the computer the y postion of the ball will be mouse tracking
        self.radius = radius #establishing the physical size of the ball
        self.color = color #establishing the color of the ball

    def draw(self): #drawing the ball with specific variables
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color) #actually telling arcade to create the ball with specific coordinates and qualities


class MyGame(arcade.Window): #establishing a game object in the arcade library 

    def __init__(self, width, height, title): #establishing what qualities will be defined 

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY) #sets the background for the display screen from a list in the arcade libray

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self): #function needed to draw the display window 
        """ Called whenever we need to draw the window. """
        arcade.start_render() #begins the render which must happen before things can be drawn on screen
        self.ball.draw() #draws the ball with the specific variables we have set

    def on_mouse_motion(self, x, y, dx, dy): #function to make the ball track mouse movements
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x #establishes tracking in the x coordinate plane 
        self.ball.position_y = y #establishes tracking in the y coordinate plane

    def on_mouse_press(self, x, y, button, modifiers): #establishes something that will happen when the mouse is pressed
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}") #prints a message when the mouse is clicked
        if button == arcade.MOUSE_BUTTON_LEFT: #outlines that there is an action to take when the left mouse button is pressed
            self.ball.color = arcade.color.BLACK #the action of turning the ball black on mouse click

    def on_mouse_release(self, x, y, button, modifiers): #establishing there will be a function when the mouse is released
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT: #outlines there is an action when the button is released
            self.ball.color = arcade.color.AUBURN #defining this action and getting the color from the arcade library 


def main(): #defines the entry point for the program 
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #establishing some variables for the display window
    arcade.run() #the main game loop in the arcade library 


if __name__ == "__main__": #action to take if this module is not the main file
    main() #makes this module the main file to execute