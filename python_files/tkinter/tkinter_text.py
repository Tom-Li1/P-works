import tkinter as tk
window = tk.Tk()
window.title("Entry")
window.geometry("500x300")

e = tk.Entry(window, show = None)
e.pack()

def insert_point():
    var = e.get()
    t1.insert('insert', var)

def insert_end():
    var = e.get()
    t1.insert('end', var)

b1 = tk.Button(window, text = 'Insert point', width = 10\
    , height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text = 'End point', width = 10,\
    height = 2, command = insert_end)
b2.pack()

t1 = tk.Text(window, height = 3)
t1.pack()

window.mainloop()