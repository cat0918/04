import turtle
turtle.penup()
turtle.goto(-250,300)
turtle.pendown()
count = 5
down = 1
while(count>=0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-250,300-(down*100))
    turtle.pendown()
    count = count-1
    down = down+1
turtle.penup()
turtle.goto(-250,300)
turtle.pendown()
count = 5
down = 1
turtle.right(90)
while(count>=0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-250+(down*100),300)
    turtle.pendown()
    count = count-1
    down = down+1

    
