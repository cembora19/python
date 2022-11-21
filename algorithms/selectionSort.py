array=[1,19,23,6,85,4,3,17]
size=len(array)
count1="count1"
count2="count2"
for step in range(size):
    min=step
    print(count1)
    for i in range(step+1,size):
        if array[i]<array[min]:
            min=i
            print(count2)
    (array[step],array[min])=(array[min],array[step])
print(array)