# dibujar un rect
# draw Rectangle in Python Turtle
import turtle
import ejercicio2 as ej2
  
t = turtle.Turtle()
 
punto1_x=2
y_1=2
x_2=5
y_2=5
l = int(abs(y_2-y_1)*50)
w = int(abs(x_2-punto1_x)*50)
 
# drawing first side
t.forward(l) # Forward turtle by l units
t.left(90) # Turn turtle by 90 degree
 
# drawing second side
t.forward(w) # Forward turtle by w units
t.left(90) # Turn turtle by 90 degree
 
# drawing third side
t.forward(l) # Forward turtle by l units
t.left(90) # Turn turtle by 90 degree
 
# drawing fourth side
t.forward(w) # Forward turtle by w units
t.left(90) # Turn turtle by 90 degree
