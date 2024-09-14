import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_palestine_flag():
    # Set up the turtle
    turtle.speed(1)
    turtle.title("Palestine Flag")
    
    # Draw black rectangle (top)
    draw_rectangle("black", -150, 100, 300, 50)
    
    # Draw white rectangle (middle)
    draw_rectangle("white", -150, 50, 300, 50)
    
    # Draw green rectangle (bottom)
    draw_rectangle("green", -150, 0, 300, 50)
    
    # Draw red triangle
    turtle.penup()
    turtle.goto(-150, 100)  # Start at the top left
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.goto(-150, -50)    # Move to bottom left
    turtle.goto(-75, 25)    # Move to the center (top point of triangle)
    turtle.goto(-150, 100)   # Return to top left
    turtle.end_fill()

    # Finish
    turtle.hideturtle()
    turtle.done()

# Draw the flag
draw_palestine_flag()