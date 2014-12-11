import turtle, random

window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor('grey')

colors = ['white','orange','yellow','green','purple','red']

t.penup()
t.forward(90)
t.left(45)
t.pendown()

def branch():
    for i in range (3):
        for i in range (3):
            t.forward(30)
            t.backward(30)
            t.right(45)
        t.left(90)
        t.backward(30)
        t.left(45)
    t.right(90)
    t.forward(90)

for i in range(8):
    branch()
    t.left(45)


window.exitonclick()

            
