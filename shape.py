import turtle


s = turtle.getscreen()
t1 = turtle.Turtle()
# circle
t1.circle(100)
#dot
t1.goto(0, 100)
t1.dot(100)

# rectangle
t1.goto(200, 0)
t1.goto(200, 100)
t1.goto(0, 100)
t1.goto(0, 0)

# triangle
t1.fd(200)
t1.goto(100, 200)
t1.goto(0, 0)
