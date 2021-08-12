# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader((data_file))
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
#
# print(temp_list)
# print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)


# Get Data in Row
# print(data[data.temp == data.temp.max()])

# Get Monday's Temperature
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp) * 9/5 + 32
# print(monday_temp)

# Create a dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores" : [76, 75, 65]
# }
#
# data_create = pandas.DataFrame(data_dict)
# print(data_create)
# data_create.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = data_create = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
