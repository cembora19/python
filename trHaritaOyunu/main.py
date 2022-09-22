import turtle
import pandas
PATH="trHaritaOyunu\\81_sehir.csv"

screen=turtle.Screen()
image="trHaritaOyunu\\tr_img.gif"
turtle.addshape(image)
turtle.shape(image)
turtle.title("Turkey city Games")

data=pandas.read_csv(PATH)
all_citys=data.city.to_list()
guessed_citys=[]

while len(guessed_citys)<81:
        
    answer_city=turtle.textinput(title=f"{len(guessed_citys)}/81 Citys Correct", prompt="What's the another city name?").title()
    if answer_city=="Exit":
        missed_citys=[]
        for city in all_citys:
            if city not in guessed_citys:
                missed_citys.append(city)
        new_data=pandas.DataFrame(missed_citys)
        new_data.to_csv("city_to_learn.csv")        
        break
    if answer_city in all_citys:
        if answer_city not in guessed_citys:
            guessed_citys.append(answer_city)
            t=turtle.Turtle()
            t.penup()
            t.hideturtle()
            city_data=data[data.city==answer_city]
            t.goto(int(city_data.x),int(city_data.y))
            t.write(answer_city)


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

# data_dict={
#     "sehir":["Adana", "Adiyaman","Afyon","Ağri","Amasya","Ankara","Antalya","Artvin","Aydin","Balikesir","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankiri","Çorum","Denizli","Diyarbakir","Edirne","Elaziğ","Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari","Hatay","Isparta","Mersin","Istanbul","Izmir","Kars","Kastamonu","Kayseri","Kirklareli","Kirşehir","Kocaeli","Konya","Kütahya","Malatya","Manisa","Kahramanmaraş","Mardin","Muğla","Muş","Nevşehir","Niğde","Ordu","Rize","Sakarya","Samsun","Siirt","Sinop","Sivas","Tekirdağ","Tokat","Trabzon","Tunceli","Şanliurfa","Uşak","Van","Yozgat","Zonguldak","Aksaray","Bayburt","Karaman","Kirikkale","Batman","Şirnak","Bartin","Ardahan","Iğdir","Yalova","Karabük","Kilis","Osmaniye","Düzce"],

#     "x":[8,149,-250,377,12,-148,-239,307,-390,-389,-272,267,348,-192,-283,-323,-441,-110,-47,-320,244,-451,204,195,299,-229,98,150,193,449,42,-232,-84,-321,-415,378,-92,15,-401,-72,-273,-155,-301,130,-374,78,285,-361,324,-43,-39,96,260,-250,28,356,-33,92,-403,56,210,202,189,-312,420,-12,-187,-83,235,-111,-91,303,375,-151,358,431,-316,-146,89,46,-213],

#     "y":[-114,-75,-21,63,111,58,-138,166,-77,53,72,18,-7,106,-100,77,76,108,105,-80,-46,155,-16,53,90,41,-125,120,97,-62,-174,-71,-157,143,-40,120,166,-17,181,22,127,-65,19,-28,-12,-72,-97,-128,17,-18,-72,125,142,112,145,-51,178,42,144,97,135,21,-114,-34,-7,38,149,-43,97,-112,52,-50,-80,167,168,91,109,135,-151,-116,125]
# }
# data=pandas.DataFrame(data_dict)
# data.to_csv("81_sehir.csv")