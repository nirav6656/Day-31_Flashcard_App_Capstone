BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
# -----------------UI------------------

# --window setup--
window = Tk()
window.minsize(width=900, height=676)
window.config(pady=50,padx=50)
window.config(background=BACKGROUND_COLOR)


# --white canvas--
white_image = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800,height=526,highlightthickness=0)
canvas.create_image(400,263, image=white_image)
canvas.config(bg=BACKGROUND_COLOR)

# --french text--
canvas.create_text(400,150,text="french", font=("arial",40,"italic"))

# --english text--
canvas.create_text(400,263,text="english", font=("arial",60,"bold"))

canvas.grid(row=0,column=0)

# wrong button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_image_button = Button(width=100,height=100,highlightthickness=0,borderwidth=0,image=wrong_image)
wrong_image_button.config(bg=BACKGROUND_COLOR)
wrong_image_button.grid(row=1,column=0,sticky="e")

# right button
right_image = PhotoImage(file="images/right.png")
right_image_button = Button(width=100,height=100,highlightthickness=0,borderwidth=0,image=right_image)
right_image_button.config(bg=BACKGROUND_COLOR)
right_image_button.grid(row=1,column=0,sticky="w")







# -----------get the data from csv---------------
def new_question():
    pass









window.mainloop()

