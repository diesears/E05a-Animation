"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade #making the arcade library accessable for this code 

SCREEN_WIDTH = 640 #setting the width of the display screen
SCREEN_HEIGHT = 480 #setting the height of the display screen 
SCREEN_TITLE = "Move Keyboard Example" #setting the title of the display screen
MOVEMENT_SPEED = 3 #determining how fast the ball will move on screen 


class Ball: #establishing the object that will be on the display screen
    def __init__(self, position_x, position_y, change_x, change_y, radius, color): #establishing what variables of this object will be defined 

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x #variable for the x coordinate 
        self.position_y = position_y #variable for the y coordinate 
        self.change_x = change_x #sets how much change there is in the x coordinate after an event 
        self.change_y = change_y #sets how much change there is in the y coordinate after an event
        self.radius = radius #determines the size of the ball
        self.color = color #determines the color of the ball 

    def draw(self): #draws the object with the variables we have outlined 
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color) #lets the computer know the specifc variables and take them into account while creating the ball

    def update(self): #the computer needs to update the postion of the object 
        # Move the ball
        self.position_y += self.change_y #how much an event affects the y coordinate 
        self.position_x += self.change_x #how much an event affects the x coordinate

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius: #if the x postion is smaller than the radius 
            self.position_x = self.radius #then the x postion equals the radius 

        if self.position_x > SCREEN_WIDTH - self.radius: #if the x postion is larger than the screen width i.e. on the edge of the screen
            self.position_x = SCREEN_WIDTH - self.radius #its x postion will stop there on the very edge of the screen

        if self.position_y < self.radius: #if the y postion is smaller than the radius
            self.position_y = self.radius #then the y postion equals the radius

        if self.position_y > SCREEN_HEIGHT - self.radius: #if the y postion is larger than the screen width i.e. on the edge of the screen
            self.position_y = SCREEN_HEIGHT - self.radius #its y postion will stop there on the very edge of the screen


class MyGame(arcade.Window): #establishing a game object in the arcade library 

    def __init__(self, width, height, title): #establishes the variables for this game object

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY) #sets the background to a color in the arcade library 

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self): #in order to draw the display window
        """ Called whenever we need to draw the window. """
        arcade.start_render() #first step before anything can be rendered on the screen
        self.ball.draw() #draws the ball with our specific variables 

    def update(self, delta_time): #function to update the postion over time
        self.ball.update() #establishes that the ball is the object being updated 

    def on_key_press(self, key, modifiers): #function for a key press event 
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT: #if the left key is pressed 
            self.ball.change_x = -MOVEMENT_SPEED #there is a negative effect on the x coordinate postion 
        elif key == arcade.key.RIGHT: #if the right key is pressed 
            self.ball.change_x = MOVEMENT_SPEED #there is a positve effect on the x coordinate postion 
        elif key == arcade.key.UP: #if the up key is pressed 
            self.ball.change_y = MOVEMENT_SPEED #there is a postive effect on the y coordinate postion
        elif key == arcade.key.DOWN: #if the down key is pressed 
            self.ball.change_y = -MOVEMENT_SPEED #there is a negative effect on the y coordinate postion 

    def on_key_release(self, key, modifiers): #function for a released key event
        """ Called whenever a user releases a key. """ 
        if key == arcade.key.LEFT or key == arcade.key.RIGHT: #if the left or right key is released 
            self.ball.change_x = 0 #the postion will not change 
        elif key == arcade.key.UP or key == arcade.key.DOWN: #if the up or down key is released 
            self.ball.change_y = 0 #the postion will not change 


def main(): #defines the entry point for the program
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #establishing some variables for the display window
    arcade.run() #the main game loop in the arcade library 


if __name__ == "__main__": #action to take if this module is not the main file
    main() #makes this module the main file to execute