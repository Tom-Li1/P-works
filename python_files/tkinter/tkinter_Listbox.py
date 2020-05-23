import tkinter as tk
window = tk.Tk()
window.title("Listbox practice")
window.geometry("500x300")

var1 = tk.StringVar()
l = tk.Label(window, bg = "green", fg = 'yellow', font = ("Arial", 12), width = 10, textvariable = var1)
l.pack()

def print_selection():
    var1.set(lb.get(lb.curselection()))

b1 = tk.Button(window, text = "print selection", width = 15, height = 2, command = print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((1,2,3,4))

lb = tk.Listbox(window, listvariable = var2)
list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end', item)

lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()

window.mainloop()
