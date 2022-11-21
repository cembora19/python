from tkinter import *
import requests
BACKGROUND_PATH="day33ISS\\kanye-quotes-start\\background.png"
KANYE_PATH="day33ISS\\kanye-quotes-start\\kanye.png"


def get_quote():
    response=requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data=response.json()
    quote=data["quote"]
    canvas.itemconfig(quote_text,text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=BACKGROUND_PATH)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=KANYE_PATH)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()