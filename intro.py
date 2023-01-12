import turtle

# tut = turtle.Turtle()
# tut.shape("turtle")
s = turtle.getscreen()
t1 = turtle.Turtle()

# moving
# forward(distance) or fd(distance)
# backward(distance) or bk(distance)

# t1.forward(200)
# t1.backward(300)

# left(angle) or lt(angle)
# right(angle) or rt(angle)
# got0(x,y)
# home()
for _ in range(4):
    t1.forward(200)
    t1.left(90)

t1.left(45)
t1.forward(282.8)

t1.goto(200, 0)

t1.left(90)
t1.forward(282.8)
t1.home()
