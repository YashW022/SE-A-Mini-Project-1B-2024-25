
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/arjun/Organ_GUI/build/assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    716.0,
    360.0,
    image=image_image_1
)

canvas.create_text(
    52.0,
    28.0,
    anchor="nw",
    text="TRANSPLANT CARE",
    fill="#000000",
    font=("Sora ExtraBold", 48 * -1)
)

canvas.create_rectangle(
    -4.0,
    84.0,
    1283.0,
    88.00000000000013,
    fill="#000000",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    639.0,
    405.0,
    image=image_image_2
)

canvas.create_text(
    335.0,
    217.0,
    anchor="nw",
    text="Patient’s Name:- Patient’s Name",
    fill="#000000",
    font=("Sora Regular", 24 * -1)
)

canvas.create_text(
    335.0,
    562.0,
    anchor="nw",
    text="You have been Matched with:- Donar’s name",
    fill="#000000",
    font=("Sora Regular", 24 * -1)
)

canvas.create_text(
    335.0,
    519.0,
    anchor="nw",
    text="Organ to be Received:- Patient’s Organ",
    fill="#000000",
    font=("Sora Regular", 24 * -1)
)

canvas.create_text(
    335.0,
    259.0,
    anchor="nw",
    text="Age:- Patient’s Age",
    fill="#000000",
    font=("Sora Regular", 24 * -1)
)

canvas.create_text(
    335.0,
    301.0,
    anchor="nw",
    text="Gender :- Patient’s Gender",
    fill="#000000",
    font=("Sora Regular", 24 * -1)
)

canvas.create_text(
    335.0,
    343.0,
    anchor="nw",
    text="Phone no:- Patient’s Phone",
    fill="#000000",
    font=("Sora Regular", 24 * -1)
)

canvas.create_text(
    335.0,
    386.0,
    anchor="nw",
    text="Address:- Patient’s Address",
    fill="#000000",
    font=("Sora Regular", 24 * -1)
)

canvas.create_text(
    335.0,
    477.0,
    anchor="nw",
    text="Blood Group:- Patient’s Blood Group",
    fill="#000000",
    font=("Sora Regular", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
