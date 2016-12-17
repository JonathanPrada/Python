import turtle

start = 50
number = 100

#Window settings
def window():
    window = turtle.Screen()
    window.bgcolor("white")

#Draw lines           
def draw_lines(some_turtle):

        global start
        some_turtle.forward(start)
        some_turtle.right(90)
        some_turtle.forward(number)
        some_turtle.right(90)
        some_turtle.forward(number)
        some_turtle.right(90)
        some_turtle.forward(number)
        some_turtle.right(90)
        global number
        number = number + (number*2)
        start = start + 20
        
def draw_art():

    #Create the window
    window()
    #Create the turtle brad - draw square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(4)
    for i in range (1,5):
        draw_lines(brad)
 
    window.exitonclick()
    
draw_art()


