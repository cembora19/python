from tkinter import *
#yıldızı ekledikten sonra
#window için window=tkinter.Tk() yazmamız gerekiyordu 
#yıldız ekleyince direkt Tk() yazdık
#my_label için = tkinter.Label(...)
#yapmamız gerekiyordu ama biz direkt Label(...) yapabildik
#geri kalan hepsi için böyle

window=Tk()
window.title("eyyo")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)

#label

my_label=Label(text="Eyyo Radio Cheeech", font=("Arial",24,"bold"))
my_label["text"]="New Text"
my_label.config(text="new text v2")
my_label.config(fg="brown", bg="green",font="Calibri")
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)

#Button

def button_clicked():
    print("eyyo got clicked")
    new_text=input.get()
    my_label.config(text=new_text)

button=Button(text="eyyo click me", command=button_clicked)
button.grid(column=1,row=1)

#Entry

input=Entry(width=20)
input.grid(column=3,row=3)

#New Button

button_2=Button(text="eyyo new button")
button_2.grid(column=2, row=0)

window.mainloop()