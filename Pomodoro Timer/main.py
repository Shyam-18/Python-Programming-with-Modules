from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#03c03c"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
reps = 0
current_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    windows.after_cancel(current_timer)
    canvas.itemconfig(timer, text="00:00")
    my_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    seconds_for_work = WORK_MIN * 60
    seconds_for_longbreak = LONG_BREAK_MIN * 60
    seconds_for_shortbreak = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(seconds_for_longbreak)
        my_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(seconds_for_shortbreak)
        my_label.config(text="Short Break", fg=PINK)
    else:
        count_down(seconds_for_work)
        my_label.config(text="On Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:    # Remove this "if statement" and see the difference if you don't understand what's going on.
        seconds = f"0{seconds}"  # Used Dynamic Typing, in this case string("00") overwrites integer(0).
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global current_timer
        current_timer = windows.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        total_work_sesh = math.floor(reps/2)
        for _ in range(total_work_sesh):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro")
windows.config(bg=YELLOW, padx=100, pady=50)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer = canvas.create_text(150, 170, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(column=1, row=1)

my_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
my_label.grid(column=1, row=0)

start_button = Button(text="Start", height=2, width=8, font=(FONT_NAME, 12), command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", height=2, width=8, font=(FONT_NAME, 12), command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_marks.grid(column=1, row=2)

windows.mainloop()
