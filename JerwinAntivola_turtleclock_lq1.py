import turtle
t=turtle.Pen()
wn=turtle.Screen()
t.shape('turtle')
t.color('blue')
wn.bgcolor('lightgreen')
t.stamp()
move=30
for i in range(12):
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(25)
    t.penup()
    t.forward(15)
    t.stamp()
    t.home()
    t.right(move)
    move=move+30
