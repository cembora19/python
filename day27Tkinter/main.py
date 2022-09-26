from tkinter import *


#window

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=100)
window.config(padx=10,pady=10)
#label

label=Label(text="is equal to")
label.grid(column=0,row=1)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

km_label=Label(text="Km")
km_label.grid(column=2,row=1)

sum_label=Label(text="0")
sum_label.grid(column=1,row=1)

#entry

miles_entry=Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)

#button

def calculate():
    new_value=round(float(miles_entry.get())*1.609)
    sum_label.config(text=new_value)

button=Button(text="Calculate", command=calculate)
button.grid(column=1,row=2)

window.mainloop()