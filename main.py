import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    new_window.after_cancel(timer)
    title_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="BREAK", fg=RED)
        count_down(long_break_time)
    elif reps % 2 == 0:
        title_label.config(text="BREAK", fg=PINK)
        count_down(short_break_time)
    else:
        title_label.config(text="WORK", fg=GREEN)
        count_down(work_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = new_window.after(1000, count_down, count - 1)
    else:
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
new_window = tkinter.Tk()
new_window.config(padx=50, pady=50, bg=YELLOW)
new_window.title("Pomodoro")

title_label = tkinter.Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW, highlightthickness=0)
title_label.grid(column=1, row=0)

canvas = tkinter.Canvas(height=224, width=200, background=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)

new_window.mainloop()
