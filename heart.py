from turtle import *
title("Love")
# hideturtle()
color("#ff0000")
# pencolor("blue")
pensize(3)
begin_fill()
left(50)
forward(133)
circle(50, 200)

right(140)
circle(50, 200)
forward(133)
end_fill()

# pinting I
penup()
goto(-150, -50)
pendown()
left(50)
fd(20)
bk(10)
left(-90)
fd(30)
right(90)
fd(10)
bk(20)

# printing L
penup()
goto(-100, -50)
pendown()
left(90)
forward(30)
left(90)
forward(25)
# printing O
penup()
goto(-55, -50-30)
pendown()
circle(15)

# printing V
penup()
goto(-34, -50)
pendown()
goto(-22, -50-30)
goto(-10, -50)

# printing E


penup()
goto(23, -50)
pendown()
goto(0, -50)
goto(0, -50-30)
goto(23, -50-30)
penup()
goto(0, -50-15)
pendown()
goto(23, -50-15)

# printing Y
penup()
goto(23+35, -50)
pendown()

goto(58+15, -50-15)
goto(58+30, -50)
goto(58+15, -50-15)
goto(58+15, -50-30)

# printing o
penup()
goto(58+30+20, -50-30)
pendown()
circle(15)

# printing U
penup()
goto(133, -50)
pendown()
goto(133, -50-25)
left(-50)
# fd(5)
circle(20, 90)
left(50)
fd(27)
pendown()

hideturtle()
exitonclick()
