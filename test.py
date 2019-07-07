import tkinter as tk

def on_click(event=None):
    if event is None:
        print("You clicked the button")
    else:
        print("You pressed enter")


root = tk.Tk()
root.bind("<Return>", on_click)
b = tk.Button(root, text='Click Me!', command=on_click)
b.pack()
root.mainloop()