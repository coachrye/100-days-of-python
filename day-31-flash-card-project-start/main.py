from tkinter import *
import pandas as pd
import random

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}


def remove_card():
    # to_learn[:] = [d for d in to_learn if d.get('French') != current_card["French"]]
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    pick_next_card()


def pick_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card_canvas.itemconfig(card_background, image=card_front)
    card_canvas.itemconfig(canvas_lang, text="French", fill="black")
    card_canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card_canvas.itemconfig(card_background, image=card_back)
    card_canvas.itemconfig(canvas_lang, text="English", fill="white")
    card_canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")


BACKGROUND_COLOR = "#B1DDC6"
FONT_FAMILY = "Arial"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_canvas = Canvas(width=800, height=586, highlightthickness=0,  bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = card_canvas.create_image(400, 293, image=card_front)
card_canvas.grid(row=0, column=0, columnspan=2)

canvas_lang = card_canvas.create_text(400, 150, text="Title", font=(FONT_FAMILY, 40, "italic"))
canvas_word = card_canvas.create_text(400, 263, text="trouve", font=(FONT_FAMILY, 60, "bold"))

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=pick_next_card)
image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=remove_card)
button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)

pick_next_card()

window.mainloop()