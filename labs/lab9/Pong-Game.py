import turtle

from PIL.ImageQt import align8to32

window = turtle.Screen()
window.title("ping pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.color("white")
madrab1.penup()
madrab1.goto(-350, 0)
madrab1.shape("square")
madrab1.shapesize(stretch_len=1, stretch_wid=5)

madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.color("blue")
madrab2.penup()
madrab2.goto(350, 0)
madrab2.shape("square")
madrab2.shapesize(stretch_len=1, stretch_wid=5)

ball = turtle.Turtle()
ball.speed(0)
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.shape("square")
ball.dx = 0.1
ball.dy = 0.1

score=turtle.Turtle()
score1=0
score2=0
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
#score.write("player1:0  player2:0 " ,align="center",font=("Courier",24,"normal"))
def madrab1_up():
    y = madrab1.ycor()
    y += 30
    madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    y -= 30
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 30
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 30
    madrab2.sety(y)

window.listen()
window.onkeypress(madrab1_up, "w")
window.onkeypress(madrab1_down, "s")
window.onkeypress(madrab2_up, "Up")
window.onkeypress(madrab2_down, "Down")

def update_score():
    remain=5-max(score1,score2)
    print(f"{remain} is left")
    score.clear()
    score.write(f"player1:{score1} player2:{score2} | left:{remain}",
                align="center", font=("Courier", 24, "normal"))


while True:

    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 +=1
        update_score()
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        update_score()
    if (ball.xcor() > 340) and (ball.xcor() < 350) and \
       (ball.ycor() < madrab2.ycor() + 60) and \
       (ball.ycor() > madrab2.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and \
       (ball.ycor() < madrab1.ycor() + 60) and \
       (ball.ycor() > madrab1.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1
    if score1 == 5:
        print("player1 is winner")
        break
    elif score2 == 5:
        print("player2 is winner")
        break





