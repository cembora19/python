# PATH="\\Users\\cembora\\Desktop\\python\\day25CSVdata\\weather_data.csv"
PATH="day25CSVdata\\weather_data.csv"
print(r"\n")
# import csv

# with open(PATH) as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data=pandas.read_csv(PATH)
# print(type(data)) # tümü = data frame
# print(type(data["temp"])) #tek tek her bir column = series

# data_dict=data.to_dict()
# # print(data_dict)

# temp_list=data["temp"].to_list()
# # print(len(temp_list))

# # average=sum(temp_list) / len(temp_list)
# # print(average)

# print(data["temp"].mean())
# print(data["temp"].max())

# #Get Data in Column
# print(data["condition"])
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Monday"])

# print(data[data.temp==data.temp.max()])

# monday=data[data.day=="Monday"]
# monday_temp=int((monday.temp))
# monday_temp_F=monday_temp*9/5+32
# print(monday_temp_F)

#Create a dataframe from stratch

data_dict={
    "students": ["cem", "bora", "seval"],
    "scores": [19,91,78]
}

data=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")