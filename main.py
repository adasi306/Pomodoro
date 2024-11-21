from tkinter import *
import math

PINK: str = "#e2979c"
RED: str = "#e7305b"
GREEN: str = "#9bdeac"
YELLOW: str = "#f7f5dd"
FONT_NAME: str = "Courier"
WORK_MIN: int = 25
SHORT_BREAK_MIN: int = 5
LONG_BREAK_MIN: int = 20
reps: int = 0
timer: int | None = None


def reset() -> None:
    global timer
    if timer:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    a_label.config(text="Timer")
    b_label.config(text="")
    global reps
    reps = 0


def start_timer() -> None:
    global reps, timer
    if timer:
        window.after_cancel(timer)

    reps += 1

    work: int = WORK_MIN * 60
    short_break: int = SHORT_BREAK_MIN * 60
    long_break: int = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        a_label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        a_label.config(text="SHORT BREAK", fg=PINK)
    else:
        countdown(work)
        a_label.config(text="WORK", fg=GREEN)


def countdown(count: int) -> None:
    count_min: int = math.floor(count / 60)
    count_sec: int = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark: str = ""
        work_sessions: int = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
        b_label.config(text=mark)


window: Tk = Tk()
window.title("pomidor")
window.config(padx=100, pady=50, bg=YELLOW)

a_label: Label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 35, "bold"))
a_label.grid(column=1, row=0)

button2: Button = Button(text="reset", highlightthickness=0, command=reset)
button2.grid(column=3, row=2)

b_label: Label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
b_label.grid(column=1, row=2)

button1: Button = Button(text="start", highlightthickness=0, command=start_timer)
button1.grid(column=0, row=2)

canvas: Canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img: PhotoImage = PhotoImage(file="pomodoro/tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text: int = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=0, row=1, columnspan=3)

window.mainloop()
