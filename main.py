from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    '''To start the timer as soon as the user clicks start'''
    count_down_timer(5)

# ---------------------------- COUNTDOWN MECHANISM ----------------------------- #
# window.after causes delay and it's functionality is similar to sleep function.


def count_down_timer(count):
    canvas.itemconfig(timer_count_text, text=count)
    if count > 0:
        window.after(1000, count_down_timer, count-1)


# ---------------------------- UI SETUP ------------------------------- #

# Creating a window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Creating Canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_count_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                      font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)
title_label.config(fg=GREEN, bg=YELLOW)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

tick_labels = Label(text="✔", font=(FONT_NAME, 20,))
tick_labels.grid(column=1, row=3)
tick_labels.config(fg=GREEN, bg=YELLOW)


window.mainloop()
