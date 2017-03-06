import turtle

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():

    window = turtle.Screen()
    window.bgcolor("lightgreen")


    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(6)


    for i in range (0, 20):
        draw_square(brad)
        brad.right(18)


    window.exitonclick()


draw_art()
