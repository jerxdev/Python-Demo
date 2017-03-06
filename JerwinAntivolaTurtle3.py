import turtle
wn = turtle.Screen()

wn.bgcolor(input('Enter Bg collor: '))
wn.title("Hello, Tess!")

tess = turtle.Turtle()
tess.color(input('Enter pen color: '))
tess.pensize(input('Enter pen size: '))

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()

