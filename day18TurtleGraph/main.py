import colorgram
import turtle as t
import random
# rgb_colors=[]
# colors=colorgram.extract("python/day18TurtleGraph/image.jpg", 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color
# print(rgb_colors)
#TODO renklerin listesini yukarıdaki kodaan çıkartıp listeye koyduk. sürekli fonksiyonun çalışmasını istemeyiz
color_list=[(211, 154, 98), (236, 241, 245), (53, 107, 131), (177, 78, 34), (199, 142, 34), (116, 156, 171), (123, 80, 98), (124, 175, 157), (226, 197, 130), (190, 88, 110), (55, 38, 19), (12, 49, 63), (43, 168, 128), (51, 126, 121), (197, 124, 143), (166, 21, 31), (222, 93, 79), (243, 163, 160), (38, 32, 35), (4, 25, 24), (80, 147, 168), (161, 26, 23), (19, 79, 92), (233, 167, 172), (175, 207, 187), (101, 127, 158), (165, 203, 210)]
t.colormode(255)
tim=t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
screen=t.Screen()
number_of_dots=273
tim.setheading(225)
tim.forward(500)
tim.setheading(0)
for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    while dot_count%17==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(850)
        tim.setheading(0)
        break
     
screen.exitonclick()