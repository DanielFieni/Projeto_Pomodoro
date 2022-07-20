from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_after = None


# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    global timer_after
    window.after_cancel(timer_after)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_counter():
    global reps
    reps += 1
    work_seg = WORK_MIN * 60
    short_break_seg = SHORT_BREAK_MIN * 60
    long_break_seg = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        counter(long_break_seg)
        timer.config(text="Break", fg=YELLOW)
    elif reps % 2 == 0:
        counter(short_break_seg)
        timer.config(text="Break", fg=PINK)
    else:
        timer.config(text="Work", fg=GREEN)
        counter(work_seg)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    count_min = math.floor(count / 60)
    count_seg = count % 60
    if count_seg < 10:
        count_seg = f"0{count_seg}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seg}")
    if count > 0:
        global timer_after
        timer_after = window.after(1000, counter, count - 1)
    else:
        start_counter()
        mark = ""
        interval = math.floor(reps / 2)
        for _ in range(interval):
            mark += "✔"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=RED)

canvas = Canvas(width=200, height=224, bg=RED, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)


timer = Label(text="Timer", bg=RED, fg=PINK, font=(FONT_NAME, 50, "normal"))
timer.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_counter)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset.grid(column=2, row=2)

check = Label(bg=RED, fg=GREEN)
check.grid(column=1, row=3)

window.mainloop()
