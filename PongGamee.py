import turtle
wn = turtle.Screen()
wn.title("Pong Game by AbhisekVrt ")
wn.setup(width=800,height=600)
wn.bgcolor("red")
wn.tracer(0)

#main Game Code
# Score board
score_a = 0
score_b = 0

# paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=7, stretch_len=1)

paddle_a.penup()
paddle_a.goto(-350.0, 0.0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=7, stretch_len=1)

paddle_b.penup()
paddle_b.goto(350.0, 0.0)

# ball B
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")

ball.penup()
ball.goto(0, 0.0)
ball.dx = 0.3
ball.dy = -0.3

# Let's make a pannel for the Game
pan = turtle.Turtle()
pan.speed(0)
pan.color("white")
pan.penup()
pan.hideturtle()
pan.goto(0 , 260)
pan.write("Player A: 0 Player B: 0" , align ="center" , font =("courier", 26, "normal"))

# stick moving code for A
def paddleAup():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

wn.listen()
wn.onkeypress(paddleAup, "q")   

def paddleAdown():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

wn.listen()
wn.onkeypress(paddleAdown, "z")   

# stick moving code for B
def paddleBup():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddleBup, "p")   

def paddleBdown():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddleBdown, "m")   

while True:
    wn.update()
    #move the Ball
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1    

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pan.clear()
        pan.write("Player A: {} Player B: {}".format(score_a, score_b) , align ="center" , font =("courier", 26, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pan.clear()
        pan.write("Player A: {} Player B: {}".format(score_a, score_b) , align ="center" , font =("courier", 26, "normal"))

    # paddle and Bole moving Combination 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+70 and ball.ycor() > paddle_b
    .ycor() -70):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+70 and ball.ycor() > paddle_a
    .ycor() -70):
        ball.setx(-340)
        ball.dx *= -1    

