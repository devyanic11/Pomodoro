from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#ffa36c"
RED = "#e7305b"
GREEN = "#799351"
YELLOW = "#f6eec9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_ori = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer_ori)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    tick_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    if reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer_ori
    count_min = math.floor(count/60)
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_sec = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer_ori = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            tick_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(150, 180, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 36, "bold"))
timer.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer, font=(12,))
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset, font=(12,))
reset.grid(column=2, row=2)

tick_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
tick_mark.grid(column=1, row=3)

window.mainloop()