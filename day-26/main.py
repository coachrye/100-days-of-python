# Dictionary Comprehension
# import re
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# def convert(the_sentence):
#     return re.sub("[^\w]", " ",  the_sentence).split()
#
# # Driver code
# converted_sentence = convert(sentence)
# # or simply sentence.split()
#
# result = {word:len(word) for word in converted_sentence}
#
# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
#
# weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
#
#
# print(weather_f)














# # List comprehension
# # Conditional List Comprehension
#
# # Get name
# # Put name in list
# #
#
# # numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # # 🚨 Do Not Change the code above 👆
# #
# # #Write your 1 line code 👇 below:
# #
# # squared_numbers = [num**2 for num in numbers]
# # squared_numbers2 = [num*num for num in numbers]
# # even_numbers = [num for num in numbers if num % 2 == 0]
# # #Write your code 👆 above:
# #
# # print(squared_numbers)
# # print(squared_numbers2)
# # print(even_numbers)
#
#
# with open("file1.txt") as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# file1 = [x.strip() for x in content]
#
# with open("file2.txt") as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# file2 = [x.strip() for x in content]
#
# print(file1)
# print(file2)
#
# same_numbers = [int(same) for same in file1 if same in file2]
#
# print(same_numbers)