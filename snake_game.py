import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
CELL_SIZE = 20   # size of each block

# Screen Setup #
ws = turtle.Screen()
ws.title("Snake Game - Minecraft Style")
ws.bgcolor("black")
ws.setup(width=600, height=600)
ws.tracer(0)
ws.colormode(255)  # allow RGB colors

# Draw Minecraft-like Background #
bg = turtle.Turtle()
bg.speed(0)
bg.penup()
bg.hideturtle()

def draw_background():
    grass_shades = [(85,168,44), (97,184,46), (106,190,48)]
    for y in range(-300, 300, CELL_SIZE):
        for x in range(-300, 300, CELL_SIZE):
            color = random.choice(grass_shades)
            bg.goto(x, y)
            bg.fillcolor(color)
            bg.begin_fill()
            for _ in range(4):
                bg.forward(CELL_SIZE)
                bg.left(90)
            bg.end_fill()
            bg.setheading(0)

draw_background()

# Snake Head #
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("brown")
head.penup()
head.goto(0, 0)
head.direction = "stop"   

# Food #
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake Segments #
segments = []

# Score Display #
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0 High Score : 0", align="center", font=("Courier", 24, "normal"))

line_pen = turtle.Turtle()
line_pen.hideturtle()
line_pen.speed(0)
line_pen.pensize(3)
line_pen.color("dark green") 
line_pen.penup()
line_pen.goto(-300, 240) 
line_pen.pendown()
line_pen.forward(600)

# Movement Functions #
def go_up():
    if head.direction != "down": 
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "stop":
        return
    if head.direction == "up":
        head.sety(head.ycor() + CELL_SIZE)
    if head.direction == "down":
        head.sety(head.ycor() - CELL_SIZE)
    if head.direction == "left":
        head.setx(head.xcor() - CELL_SIZE)
    if head.direction == "right":
        head.setx(head.xcor() + CELL_SIZE)

ws.listen()
ws.onkeypress(go_up, "w")
ws.onkeypress(go_down, "z")
ws.onkeypress(go_left, "a")
ws.onkeypress(go_right, "s")

# Game Loop #
while True:
    ws.update()

    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for seg in segments:
            seg.goto(1000, 1000)
        segments.clear()

        score = 0
        pen.clear()
        pen.write(f"Score : {score} High Score : {high_score}", align="center", font=("Courier", 24, "normal"))

    # Food Collision #
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color((139, 90, 43))
        new_seg.penup()
        segments.append(new_seg)

        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score : {score} High Score : {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move Segments #
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self-Collision #
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for s in segments:
                s.goto(1000, 1000)
            segments.clear()

    time.sleep(delay)

ws.mainloop()