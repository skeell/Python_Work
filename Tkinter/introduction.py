import tkinter as tk


window =tk.Tk()
window.geometry("400x300+500+200")
window.title("INTRODUCTION_PYTHON")
#window.resizable(False, False) #evita il ridimensionamento della finestra
#window.configure(bg="yellow")

def first_print():
    testo = "Hello World!"
    text_output = tk.Label(window, text=testo, fg="red", font=("Helvetica", 16))
    text_output.grid(row=0, column=1, sticky="W")

def second_func():
    testo = "secondo messaggio, seconda funzione"
    text_output = tk.Label(window, text=testo, fg="green", font=("Helvetica", 12))
    text_output.grid(row=1, column=1, padx=30, sticky="W")


first_button = tk.Button(text="SALUTA", command=first_print)
first_button.grid(row=0, column=0, sticky="W")

second_button = tk.Button(text="Seconda Funzione", command=second_func)
second_button.grid(row=1, column=0, pady=20, sticky="W")


if __name__=="__main__":
    window.mainloop()