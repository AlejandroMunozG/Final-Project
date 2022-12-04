import tkinter as tk

root = tk.Tk()
root.title("Eazy Phonez")
# 1000x400
root.geometry("500x300")
root.resizable(False, False)

name = ""

def pageOne():
    #resizes window
    root.geometry('900x500')

    #gets any data from before deletes thigns
    name = name_entry.get()

    #deletes past things
    title_label.destroy()
    name_entry.destroy()
    name_label.destroy()
    name_btn.destroy()

    #name + welcome
    welcome_label = tk.Label(root,text = "Welcome "+name+". What are you buying?",font=("Helvetica",15))
    welcome_label.place(relx=0,rely=0)

    #phone label
    sam22Ultra_label = tk.Label(root,text = "Samsung 22 Ultra",font=("Helvetica",10))
    sam22Ultra_label.place(relx=0,rely=0.1)

    sam22Plus_label = tk.Label(root,text = "Samsung 22+",font=("Helvetica",10))
    sam22Plus_label.place(relx=0.19,rely=0.1)

    pixel7Pro_label = tk.Label(root,text = "Pixel 7 Pro",font=("Helvetica",10))
    pixel7Pro_label.place(relx=0.35,rely=0.1)

    pixel7_label = tk.Label(root,text='Pixel 7',font=("Helvetica",10))
    pixel7_label.place(relx=0.49,rely=0.1)

    i14ProMax_label = tk.Label(root,text='iPhone 14 Pro Max',font=("Helvetica",10))
    i14ProMax_label.place(relx=0.6,rely=0.1)

    i14Pro_label = tk.Label(root,text="iPhone 14 Pro",font=("Helvetica",10))
    i14Pro_label.place(relx=0.78,rely=0.1)

    i14_label = tk.Label(root,text="iPhone 14",font=("Helvetica",10))
    i14_label.place(relx=0.93,rely=0.1)

    #phone pics


    #phone button

    #specs button

#title label
title_label = tk.Label(root,text="Eazy Phonez Online",font=("Helvetica",20))
title_label.place(relx=0.5,rely=0.2,anchor='center')
# Start Label
name_label = tk.Label(root,text = "Enter your name to continue",font=("Helvetica",10))
name_label.place(relx=0.5,rely=0.4,anchor='center')
# Start Entry
name_entry = tk.Entry(root, textvariable=name)
name_entry.place(relx=0.5, rely=0.5, anchor='center')
# Start Button
name_btn = tk.Button(root, text='Enter', command=pageOne)
name_btn.place(relx=0.5, rely=0.6, anchor='center')


tk.mainloop()
