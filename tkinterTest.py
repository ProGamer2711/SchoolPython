from tkinter import Tk, Frame, Label, Button, StringVar

ARIAL_FONT24 = ("Arial", 24)

root = Tk()

frame = Frame(master=root, width=1280, height=720)
frame.pack(fill="both")

textVar = StringVar()

label = Label(master=frame, textvariable=textVar, font=ARIAL_FONT24)
label.place(relx=0.5, rely=0.5, anchor="center")

button = Button(master=frame, text="Click Me!", bg="red",
                fg="white", command=lambda: textVar.set("Thank you!"),
                font=ARIAL_FONT24)
button.place(relx=0.5, rely=0.4, anchor="center")

root.mainloop()
