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
RESET = False
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady =50, bg=YELLOW)
# window.minsize(width = 200, height = 200)#



# window.after(5000, say_something(1,2,3))

def increase_tick(pomos):
    tick_counter = pomos * "✔"
    tick_label.config(text=tick_counter, fg=PINK, bg=YELLOW)



timer_label = Label()
timer_label.config(text = "Timer", bg = YELLOW, font = (FONT_NAME, 50), fg = GREEN)
timer_label.grid(row = 0, column = 1)

# time_label = Label()
# time_label.config(text = "timer_text", bg = YELLOW, font = (FONT_NAME, 50), fg = GREEN)
# time_label.grid(row = 1, column = 1)

canvas = Canvas(width = 200, height = 224, highlightthickness = 0, bg=YELLOW)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100,112, image = tomato_img)
counter = canvas.create_text(100, 130, text = "00:00", font = (FONT_NAME, 35, "bold"))

canvas.grid(row = 1, column = 1)

def start_timer():
    global reps
    reps +=1
    if reps%2 == 0:
        pomos = int(reps/2)
        increase_tick(pomos)

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60-1)
        timer_label.config(text="Long Break", fg=GREEN)
    elif reps % 2 == 1:
        count_down(WORK_MIN*60-1)
        timer_label.config(text="WORK", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN*60-1)
        timer_label.config(text="Short Break", fg=PINK)

def reset_timer():
    global timer
    global reps
    tick_label.config(text="", fg=PINK, bg=YELLOW)
    canvas.itemconfig(counter, text="00:00")
    window.after_cancel(timer)
    timer_label.config(text="Timer", bg=YELLOW, font=(FONT_NAME, 50), fg=GREEN)
    reps = 0
    # stop the function that is counting




def count_down(count):
    global timer
    count_sec = count % 60

    if count > 0:
        timer = window.after(10, count_down, count -1)
        count_min = math.floor(count / 60)

        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(counter, text=f"{str(count_min)}:{str(count_sec)}")
    else:
        start_timer()
    #if count_sec == 0 and count_min < 1:
        #print("both 0")
        #start_timer()
        #return



start_button = Button(text = "Start", bg = YELLOW, command = start_timer, highlightthickness = 0, bd = 0, relief= "flat")
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "Reset", bg = YELLOW, command = reset_timer, bd = 0, highlightthickness = 0, relief = "flat")
reset_button.grid(row = 2, column = 2)

tick_label = Label()
tick_label.config(fg = PINK, bg = YELLOW)
tick_label.grid(row = 3, column = 1)


window.mainloop()
