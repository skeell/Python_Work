from tkinter import *


f = Tk()


f.title("Finestra")
f.geometry("400x400")
f.configure(background="yellow")


tela = Canvas(f, width=300, height=300)
tela.pack(pady=50)

tela.create_line(0, 0, 145, 275, dash=3)#dash e la distanza del trattegio
tela.create_line(145, 275, 18, 75, fill="red", width=4)
tela.create_rectangle(20, 20, 80 ,80, fill="green", outline="red")
tela.create_oval(120,120, 260,180, fill="yellow")
tela.create_polygon(270, 270, 135, 248, 175, 190, 288, 200)
tela.create_text(50, 230, text="Ciao Mondo!", fill="cyan",
                 width=90, font=("Courier", 18))



f.mainloop()
 

