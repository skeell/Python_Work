from tkinter import *


f = Tk()


f.title("Finestra")
f.geometry("400x400")
f.configure(background="yellow")

metro = Scale(f, from_=0, to_=10)
metro.pack()

f.mainloop()
 
