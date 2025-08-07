from random import choice
import turtle
import time

def task_func(colors):
    # Set up the Turtle Graphics window
    window = turtle.Screen()
    window.title("Random Color Squares")
    
    # Create a Turtle object
    t = turtle.Turtle()
    t.speed(1)  # Set the drawing speed
    
    # Function to draw a square
    def draw_square(color):
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(100)
            t.right(90)
        t.end_fill()
        t.penup()
        t.forward(120)  # Move to the next position
        t.pendown()
    
    # Draw five squares with random colors
    for _ in range(5):
        color = choice(colors)
        draw_square(color)
        time.sleep(1)  # Pause for 1 second between squares
    
    # Keep the window open
    window.mainloop()

# Example usage
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
task_func(colors)