from tkinter import *
from random import randint

root = Tk()
root.title("Reaction Speed Test")
root.geometry("500x500")

def clear():
    for x in root.slaves(): x.destroy()

fullscreen_mode = BooleanVar(root, False)

def start():
    global time
    root.unbind("<Key>")
    clear()
    if fullscreen_mode.get(): root.attributes("-fullscreen", True)
    else: root.attributes("-fullscreen", False)
    time = 0.000
    time_label = Label(root, text="0.000\nPress <Return> once it's green.", fg="red", font=("TkDefaultFont", 25, "bold"))
    time_label.pack(expand=True)
    def go():
        global time
        time_label.config(fg="green")
        GO = BooleanVar(value=True)
        def x():
            global time
            time += 0.001
            time_label.config(text=str(round(time, 3))+"\n")
            if GO.get(): root.after(1, x)
            else: root.after(3500, main_menu)
        root.bind("<Key>", lambda e: GO.set(False))
        x()
    root.after(randint(5000, 9000), go)

def main_menu():
    clear()
    root.attributes("-fullscreen", False); root.unbind("<Key>")
    x = Frame(root)
    x.pack(expand=True)
    Label(x, text="Reaction Speed Test", font=("TkDefaultFont", 25, "bold")).pack(pady=7)
    Label(x, text="Press any key to start.", font=("TkDefaultFont", 16, "normal", "italic")).pack()

    Checkbutton(root, text="Fullscreen Mode", variable=fullscreen_mode, font=("TkDefaultFont", 11, "bold")).pack(side=BOTTOM)

    root.bind("<Key>", lambda e: start())

main_menu()

mainloop()
