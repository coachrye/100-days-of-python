import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
us_states = data.state.to_list()

prompt_title = "Guess the state"
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=prompt_title,
                                    prompt="What's another state's name?")

    if answer_state is None:
        # missing_states = []
        # for state in us_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        #     missing_data = pandas.DataFrame(missing_states)
        #     missing_data.to_csv("states_to_learn.csv")

        missing_states = [state for state in us_states if state not in guessed_states]
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("states_to_learn.csv")

        break

    answer_state = answer_state.title()
    if answer_state in us_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state)
        # t.write(answer_state)
        t.write(state_data.state.item())
        guessed_states.append(answer_state)
        prompt_title = f"{len(guessed_states)}/50 states."

        # check_answer = us_states[us_states.state.str.lower() == answer_state.lower()]
        # if len(check_answer) == 1:
        #     write_state = turtle.Turtle()
        #     write_state.penup()
        #     write_state.goto(int(check_answer.x), int(check_answer.y))
        #     write_state.write(str(check_answer.state))
        #     # print(check_answer.state)
        #     # print(check_answer.x)
        #     # print(check_answer.y)

