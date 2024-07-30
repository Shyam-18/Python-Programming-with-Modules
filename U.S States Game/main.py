import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Quiz")
us_image = "blank_states_img.gif"
ind_image = "india-outline-map.gif"

screen.addshape(us_image)
screen.setup(720, 485)
turtle.shape(us_image)


data = pandas.read_csv("50_states.csv")
correct_count = 0
guess_list = []
all_states = data.state.to_list()

while len(guess_list) < 50:
    input_state = screen.textinput(title=f"Progress = {correct_count}/50 ", prompt="Enter a State name").title()

    if input_state == "Exit":
        missing_states = [i for i in all_states if i not in guess_list]
        """ used list comprehension above, we can also use general loop"""
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_you_need_to_learn.csv")
        break

    if input_state in all_states:
        if input_state not in guess_list:
            correct_count += 1
        guess_list.append(input_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data.state == input_state]
        t.goto(x=int(row.x.iloc[0]), y=int(row.y.iloc[0]))
        t.write(input_state)  # we can also use "t.write(row.state.item())", item() just returns the first element

# screen.exitonclick() - no need of this because it automatically ends if guessed all states or if entered "exit"
