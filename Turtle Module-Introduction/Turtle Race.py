from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(1080, 820)
user_choice = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

participants = ["red", "green", "blue", "black", "orange", "pink"]
y = 240
x = -500
turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2, 2, 2)
    new_turtle.color(participants[i])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y -= 80
    turtles.append(new_turtle)

if user_choice:
    race = True

while race:
    for i in turtles:
        if i.xcor() > 500:
            race = False
            color_won = i.pencolor()
            if color_won == user_choice:
                print(f"You've won! {color_won} turtle is the winner")
            else:
                print(f"You've lost! {color_won} turtle is the winner")
        i.forward(random.randint(0, 25))

screen.exitonclick()





