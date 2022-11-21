array=[1,19,23,6,85,4,3,17]
size=len(array)
count1="count1"
count2="count2"
for i in range(size):
    for j in range(0,size-1-i):
        print(count1)
        if array[j]>array[j+1]:
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp
            print(count2)
print(array)