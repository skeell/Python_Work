from tkinter import *
from tkinter import messagebox

def test():
    #messagebox.showinfo("Occhio!", "Studia Tkinter!")
    #messagebox.showwarning("Minchia", "Studia Tkinter!")
    #messagebox.showerror("el ghe no!", "Studia Tkinter!")
    value = messagebox.askyesno("Domanda", "Vuoi Inviare una mail?")
    print(value)
    
f = Tk()

t = Button(f, text="PREMI QUI", command=test)
t.grid()




f.mainloop()
 

