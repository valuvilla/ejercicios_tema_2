import turtle

from colorama import Fore
t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("black")
t.speed(2)

t.penup()
t.goto(-50,60)
t.pendown()
t.color("cyan")

t.begin_fill()
t.goto(100,100)
t.goto(100,-100)
t.goto(-50,-60)
t.goto(-50,60)

t.end_fill()

t.color("black")
t.goto(15,100)
t.write("SALIENDO",font=("Arial",20,"normal"))
t.width(10)
t.goto(15,-100)

t.penup()
t.goto(100,0)
t.pendown()
t.goto(-100,0)
