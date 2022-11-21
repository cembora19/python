from cgitb import text
from email.mime import image
from tkinter import *
from turtle import title
import pandas
from random import *
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_PATH="FlashCard\\images\\card_back.png"
CARD_FRONT_PATH="FlashCard\\images\\card_front.png"
RIGHT_BUTTON_PATH="FlashCard\\images\\right.png"
WRONG_BUTTON_PATH="FlashCard\\images\\wrong.png"
WORDS_PATH="FlashCard\\data\\turkish_words.csv"

current_card={}
to_learn={}
try:
    data=pandas.read_csv("FlashCard\\data\\words_to_learn.csv")
except FileNotFoundError:
    orginal_data=pandas.read_csv(WORDS_PATH)
    to_learn=orginal_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=choice(to_learn)
    canvas.itemconfig(card_image,image=front_image)
    canvas.itemconfig(card_title,text="Turkish")
    canvas.itemconfig(card_word,text=current_card["Turkish"])
    flip_timer=window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(card_image,image=back_image)
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word,text=current_card["English"])

def is_know():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("FlashCard\\data\\words_to_learn.csv",index=False)
    next_card()

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,flip_card)

#canvas
canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
back_image=PhotoImage(file=CARD_BACK_PATH)
front_image=PhotoImage(file=CARD_FRONT_PATH)
card_image=canvas.create_image(400,263,image=front_image)
card_title=canvas.create_text(400,150,font=("Arial",40,"italic"),text="EYYO",fill="black")
card_word=canvas.create_text(400,253,font=("Arial",60,"bold"),text="Radio Checkkkkkkkk",fill="black")
canvas.grid(row=0,column=0,columnspan=2)

wrong_image=PhotoImage(file=WRONG_BUTTON_PATH)
button_wrong=Button(image=wrong_image,highlightthickness=0,padx=50,command=next_card)
button_wrong.grid(row=1,column=0)
right_image=PhotoImage(file=RIGHT_BUTTON_PATH)
button_right=Button(image=right_image,highlightthickness=0,padx=50,command=is_know)
button_right.grid(row=1,column=1)
next_card()

window.mainloop()