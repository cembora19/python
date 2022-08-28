# #scope

# from turtle import position


# enemies=1
# def increase_enemies():
#     enemies=2
#     print(f"Enemies inside function: {enemies}")
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# #local scope
# def drink_potion():
#     potion_strength=2
#     print(potion_strength)
# drink_potion()
# # print(potion_strength) bunu printleyemeyiz çünkü fonksiyon içerisinde oluşturuldu ve outside da kullanılamaz.

# #global scope
# player_health=10
# def drink_potion2():
#     potion_strength=2
#     print(player_health)
# drink_potion2()
# print(player_health)

# def game():
#     def drink_potion3():
#         position_strength=2
#         print(player_health)
#     drink_potion3()
# print(player_health)

# game_level=3
# enemy=["Skeleton", "Zombie", "Alien"]
# if game_level<5:
#     new_enemy=enemy[0]
# print(new_enemy)

# game_level=3
# def create_enemy():
#     enemy=["Skeleton", "Zombie", "Alien"]
#     if game_level<5:
#         new_enemy=enemy[0]
        
#     print(new_enemy)
# # print(new_enemy) new enemy fonksiyon içinde olduğu için local değer

#modifying global scope
# enemies=1

# def increase_enemies():
#     global enemies
#     enemies+=1
#     print(f"enemies inside function: {enemies}")
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies+1
# enemies=increase_enemies()
# print(f"enemies outsite function: {enemies}")

# #global constant
# PI=3.14159
# URL="https://www.google.com"
# TWITTER_HANDLE="@otakubora"
# def deneme():
#     new_pi=PI*3

