import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle brad - draw square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(100)
    #calls the draw_square function
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #create the turtle angie - draw circle
    angie = turtle.Turtle()
    angie.color("blue")
    angie.shape("turtle")
    angie.circle(100) 

    window.exitonclick()
    
draw_art()
