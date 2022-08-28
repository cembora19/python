fruits=["apple","peach","pear"]
for fruit in fruits:
    print(fruit)
    print(fruit+" pie")
#for loop with range
for number in range(1,10):
    print(number)
for number in range(1,11,3):
    print(number)
total=0
for number in range(1, 101):
    total+=number
print(total)
total=0
for number in range(1,101):
    if number%2==0:
        total+=number
print(total)