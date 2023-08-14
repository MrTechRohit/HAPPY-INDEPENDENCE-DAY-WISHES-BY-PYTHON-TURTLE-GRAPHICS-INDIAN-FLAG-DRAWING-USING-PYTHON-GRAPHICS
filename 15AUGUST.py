#________________ WELCOME ALL OF YOU ON COMPUTER SOFT SKILLS CHANNEL __________
#..................................... INDIAN FLAG DRAWING USING PYHON TURTLE GRAPHICS .....................................


import turtle
from turtle import *

wn = turtle.Screen()
wn.setup(width=900, height=700)
wn.title("COMPUTER SOFT SKILLS :- HAPPY INDEPENDENCE DAY")
turtle.bgcolor('KHAKI')

t = turtle.Turtle()
hideturtle()
speed(0)

#............................. WRITE TEXT   ................................................................

def pos(x,y):
    penup()
    goto(x,y)
    pendown()
pos(270, -130)
pencolor("darkorange")
write("𝓗𝓐𝓟𝓟𝓨", font=("Arial", 40, "bold"))
pos(140, -200)
pencolor("DARKBLUE")
write("𝟩𝟩𝓉𝒽 𝐼𝒩𝒟𝐸𝒫𝐸𝒩𝒟𝐸𝒩𝒞𝐸", font=("Arial", 40, "bold"))
pos(290, -270)
pencolor("darkgreen")
write("𝓓𝓐𝓨", font=("Arial", 40, "bold"))

def pos2(x,y):
    penup()
    goto(x,y)
    pendown()
pos(-500, 275)
pencolor("darkorange")
write("𝓙𝓐𝓘 𝓗𝓘𝓝𝓓", font=("Arial", 40, "bold"))
pos(-550, 215)
pencolor("darkblue")
write("𝓙𝓐𝓘 𝓑𝓗𝓐𝓡𝓐𝓣", font=("Arial", 40, "bold"))
pos(-570, 155)
pencolor("darkgreen")
write("𝐕𝐀𝐍𝐃𝐄 𝐌𝐀𝐓𝐀𝐑𝐀𝐌", font=("Arial", 40, "bold"))


#...................................................................................

t.penup()
t.goto(-200, 125)
t.pendown()

#>>>>>>>>>>>>>>>>>>>>>.

t.color("orangered")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(84)
t.right(90)
t.forward(400)
t.end_fill()

#>>>>>>>>>>>>>>>>>>>>>.

t.color("white")
t.begin_fill()
t.left(90)
t.forward(84)
t.left(90)
t.forward(400)
t.left(90)
t.forward(84)
t.left(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(85)

#>>>>>>>>>>>>>>>>>>>>>

t.color("darkgreen")
t.begin_fill()
t.forward(84)
t.left(90)
t.forward(400)
t.left(90)
t.forward(84)
t.end_fill()

#>>>>>>>>>>>>>>>>>>>>>.

t.penup()
t.goto(35, 0)
t.pendown()
t.color("darkblue")
t.begin_fill()
t.circle(35)
t.end_fill()

t.penup()
t.goto(30, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-27, -4)
t.pendown()
t.color("darkblue")
for i in range(24):
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.forward(7)
    t.right(15)
    t.pendown()

t.color("darkblue")
t.penup()
t.goto(10, 0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(1)
for i in range(24):
    t.forward(30)
    t.backward(30)
    t.left(15)

#>>>>>>>>>>>>>>>>>>>>>.
    
t.color("FIREBRICK")
t.pensize(10)
t.penup()
t.goto(-200,125)
t.right(180)
t.pendown()
t.forward(800)

turtle.done()




