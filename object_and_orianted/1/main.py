# from turtle import Turtle, Screen

# timmy=Turtle() #object class
# print(timmy)
# timmy.shape("turtle") #object method
# timmy.color("blue") #object method
# timmy.forward(100) #object method

# my_screen=Screen()
# print(my_screen.canvheight) #object attribute
# my_screen.exitonclick() #object method

from prettytable import PrettyTable

table=PrettyTable()#object class
table.add_column("pokemon name", ["pikachu", "squrite", "charmander"])#object method
table.add_column("type", ["electric", "water", "fire"])#object method
table.align="r"#object attribute
print(table)