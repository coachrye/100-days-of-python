# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
#
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

# table.field_names = ["Pokemon Name", "Type"]
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
table.align["Pokemon Name"] = "l"

print(table)