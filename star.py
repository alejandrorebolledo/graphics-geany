import turtle
import math
import random 

Screen = turtle.Turtle()

# colors
cir= ['red','green','blue','yellow','purple']

# pensize
turtle.pensize(4)

# star pattern
turtle.penup()
turtle.setpos(-90,30)
turtle.pendown()
for i in range(5):
	turtle.pencolor(cir[i])
	turtle.forward(200)
	turtle.right(144)

turtle.penup()
turtle.setpos(80,-140)
turtle.pendown()

# pen color
turtle.pencolor("Black")
turtle.done()

if __name__ == "__main__":
	main()
	
