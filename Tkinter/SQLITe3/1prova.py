from tkinter import * 
import sqlite3

def add_new_user():

    newUsername = username.get()
    newPassword = password.get()

    cursor.execute("SELECT COUNT(*) from user WHERE username = '"+
    newUsername = "' ")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        error["text"]="Errore username esistente"
    else:
        error["text"]="username aggiunto"    


with sqlite3.connect("dettagli.db") as db:
    cursor = db.cursor()

cursor.execute (""" CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT,
 username text NOT NULL, password text NOT NULL );""")

window = Tk()
window.geometry("450x180")
#
error = Message(text="", width=160)
error.place(x=30, y=10)
error.config(padx=0)
#
label1 = Label(text = "Enter Username: -> ")
label1.place(x = 30, y = 40)
label1.config(bg = 'lightgreen', padx = 0)
#
username = Entry(text =" ")
username.place(x=150, y=40, width=250, height=25)
#
label2 = Label(text = "Enter Password: -> ")
label2.place(x = 30, y = 80)
label2.config(bg = 'lightgreen', padx = 0)
#
password = Entry(text =" ")
password.place(x=150, y=80, width=250, height=25)
#
button = Button(text="Add", command=add_new_user)
button.place(x=150, y=120, width=75,height=35)

window.mainloop()  
