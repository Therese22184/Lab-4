#Authors' names are Therese Burns and Allison Macrowski
import turtle
dan=turtle.Turtle()
dan.color("yellow")
for side in range(4):
    if side==0:
        dan.color("green")
    elif side==1:
        dan.color("blue")
    elif side==2:
        dan.color("purple")
    elif side==3:
        dan.color("pink")
    dan.forward(100)
    dan.right(90)
    
