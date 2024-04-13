import pandas
import random
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


# -----------get the data from csv---------------
def new_question_generate():
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    random_question_list = random.choice(data_dict)
    return random_question_list


returned_list = new_question_generate()


def new_question():
    global returned_list
    returned_list = new_question_generate()
    # canvas.itemconfigure(english_text, text=returned_list["English"])


# -----------------UI------------------

# --window setup--
window = Tk()
window.minsize(width=900, height=676)
window.config(pady=50, padx=50)
window.config(background=BACKGROUND_COLOR)

# --white canvas--
white_image = PhotoImage(file="images/card_front.png")
sky_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=white_image)
canvas.config(bg=BACKGROUND_COLOR)


# --flip image to white function--
def flip_image_to_sky():
    canvas.itemconfig(canvas_image, image=sky_image)

    canvas.itemconfigure(english_text, text=returned_list["French"])
    canvas.itemconfigure(french_text, text="french")
    # Schedule next flip to white
    window.after(3000, flip_image_to_white)


# --flip image to sky function--
def flip_image_to_white():
    canvas.itemconfig(canvas_image, image=white_image)
    # text_for_image_to_white = new_question_generate()
    canvas.itemconfigure(english_text, text=returned_list["English"])
    canvas.itemconfigure(french_text, text="english")
    # Schedule next flip to sky
    window.after(3000, flip_image_to_sky)


for i in range(30):
    # window.after(0, flip_image_to_white)
    window.after(0, flip_image_to_sky)

# --french text--
french_text = canvas.create_text(400, 150, text="french", font=("arial", 40, "italic"))

# --english text--
english_text = canvas.create_text(400, 263, text="english", font=("arial", 60, "bold"))

canvas.grid(row=0, column=0)

# wrong button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_image_button = Button(width=100, height=100, highlightthickness=0, borderwidth=0, image=wrong_image, text=".",
                            command=new_question)
wrong_image_button.config(bg=BACKGROUND_COLOR)
wrong_image_button.grid(row=1, column=0, sticky="e")

# right button
right_image = PhotoImage(file="images/right.png")
right_image_button = Button(width=100, height=100, highlightthickness=0, borderwidth=0, image=right_image, text=".",
                            command=new_question)
right_image_button.config(bg=BACKGROUND_COLOR)
right_image_button.grid(row=1, column=0, sticky="w")

window.mainloop()
