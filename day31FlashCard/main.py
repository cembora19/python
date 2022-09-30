from cgitb import text
import pandas
from tkinter import *
from random import *
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK="day31FlashCard\\images\\card_back.png"
CARD_FRONT="day31FlashCard\\images\\card_front.png"
RIGHT_BUTTON="day31FlashCard\\images\\right.png"
WRONG_BUTTON="day31FlashCard\\images\\wrong.png"
CSV_PATH="day31FlashCard\data\\turkish_words.csv"

data=pandas.read_csv(CSV_PATH)
to_learn=data.to_dict(orient="records")
current_card={}

def new_random_word():
   global current_card,flip_timer
   # window.after_cancel(flip_timer)
   current_card=choice(to_learn)
   canvas.itemconfig(card_title,text="English",fill="black")
   canvas.itemconfig(card_word,text=current_card["English"],fill="black")
   canvas.itemconfig(card_background,image=front_card_photo)
   flip_timer=window.after(3000,func=flip_card)

def flip_card():
   canvas.itemconfig(card_title,text="Turkish",fill="white")
   canvas.itemconfig(card_word,text=current_card["Turkish"],fill="white")
   canvas.itemconfig(card_background,image=back_card_photo)
   

window=Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)
flip_timer=window.after(4000,func=flip_card)


#canvas for turkish
canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_card_photo=PhotoImage(file=CARD_FRONT)
back_card_photo=PhotoImage(file=CARD_BACK)
card_background=canvas.create_image(400,263,image=front_card_photo)
card_title=canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2,rowspan=2)

 #button
wrong_button=PhotoImage(file=WRONG_BUTTON)
button1=Button(image=wrong_button,highlightthickness=0,command=new_random_word)
button1.grid(row=2,column=0)

right_button=PhotoImage(file=RIGHT_BUTTON)
button2=Button(image=right_button,highlightthickness=0,command=new_random_word)
button2.grid(column=1,row=2)

new_random_word()


window.mainloop()