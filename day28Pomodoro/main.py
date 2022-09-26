import math
from time import time
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
GREY = "#EFEFEF"
BLACK = "#181818"
PURPLE = "#D2DAFF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
PHOTO_PATH="day28Pomodoro\\cem_seval.png"
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    word_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=PINK)
    elif reps%2==1:
        count_down(word_sec)
        timer_label.config(text="Work",fg=BLACK)
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=GREY)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min=math.floor(count/60)
    count_sec=count%60

    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}") 
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_mark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Working Timer")
window.config(padx=100,pady=100,bg= PURPLE)

#canvas

canvas=Canvas(width=240,height=240, bg=PURPLE,highlightthickness=0)
img=PhotoImage(file=PHOTO_PATH)
canvas.create_image(120,120, image=img)
timer_text=canvas.create_text(120,120, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#label
timer_label=Label(text="Timer",fg=BLACK,bg=PURPLE)
timer_label.config(font=(FONT_NAME,50))
timer_label.grid(column=1, row=0)

check_mark_label=Label(bg=PURPLE,fg="green")
check_mark_label.grid(column=1,row=3)

#button

start_button=Button(text="Start",fg=BLACK,highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset", fg=BLACK,highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)


window.mainloop()