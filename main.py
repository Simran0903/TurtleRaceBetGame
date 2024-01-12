from turtle import Turtle,Screen
import random
list=[]
screen=Screen()
screen.setup(height=500,width=500)
screen.title('Racing Game')
colors=["blue","green","red","purple","orange","yellow","black"]
yaxis=[150,100,50,0,-50,-100,-150]
userinp= screen.textinput("bet","place your bet on 'blue','green', 'red', 'purple', 'orange' or 'yellow': ")
screen.bgcolor("black")
for i in range(7):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-200,y=yaxis[i])
    list.append(turtle)

if userinp:
    ison=True
while ison:
    for i in list:
        dist=random.randint(1,10)
        i.forward(dist)
        if i.xcor()>230:
            color=i.pencolor()
            if userinp==color:
                turtle.penup()
                turtle.hideturtle()
                turtle.goto(-70,0)
                turtle.speed(1)
                turtle.pencolor("white")
                turtle.write(f"{color} is the winner.You won.",align='left', font=('Arial', 8, 'bold'))
            else:
                turtle.penup()
                turtle.hideturtle()
                turtle.speed(1)
                turtle.goto(-70, 0)
                turtle.pencolor("white")
                turtle.write(f"{color} is the winner.You lost.",align='left', font=('Arial', 8, 'bold'))
            ison=False

screen.exitonclick()