# #FileNotFound
#
# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     # print(a_dict["what"])
# except FileNotFoundError:
#     print("There was an error")
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"Key {error_message} does not exist.")
# else: #if no error
#     content = file.read()
#     print(content)
# finally: #no matter what happens
#     # file.close()
#     # print("File was closed.")
#     raise KeyError("made up error")

height = float(input("H: "))
weight = int(input("W: "))

if height > 3:
    raise ValueError("Human height should be less than 3 meters.")

bmi = weight / height ** 2
print(bmi)