BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
# -----------------UI------------------

# --window setup--
window = Tk()
window.minsize(width=800, height=526)
window.config(pady=50,padx=50)
window.config(background=BACKGROUND_COLOR)


# --white canvas--
white_image = PhotoImage(file="images/wrong.png")
canvas = Canvas(width=600,height=426)
canvas.create_image(50,50, image=white_image)
canvas.pack()




window.mainloop()