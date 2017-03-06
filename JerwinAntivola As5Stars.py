import turtle

def drawStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

wn = turtle.Screen()
wn.bgcolor('lightgreen')

corrie = turtle.Turtle()
corrie.color('hotpink')
corrie.speed(6)

for i in range(5):
    drawStar(corrie)
    corrie.penup()
    corrie.forward(350)
    corrie.right(144)
    corrie.pendown()


wn.exitonclick()
