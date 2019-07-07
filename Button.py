import tkinter as tk



class MyButton:

    # callback_function = 0

    def div_method(self):
        print("div")

    def __init__(self, text, callback_function):
        button = tk.Button(frame, text=text, command=callback_function)
        button.pack(side=tk.LEFT)


divButton = MyButton("/", div_method)



#
# def calculator():
#     print ()
#
# def my_sum(element1):
#     element2 = input("Introduce second element: ")
#
#
# root= tk.Tk()
# frame = tk.Frame(root)
# frame.pack()
#
# button_plus = tk.Button(frame, text='+', command=my_print)
# button_plus.pack(side=tk.LEFT)
# # class Button:
# button_minus = tk.Button(frame, text='-', command=my_print)
# button_minus.pack(side=tk.LEFT)
# button_division = tk.Button(frame, text='/', command=my_print)
# button_division.pack(side=tk.LEFT)
# button_multiplication = tk.Button(frame, text='*', command=my_print)
# button_multiplication.pack(side=tk.LEFT)
#
# root.bind("<Return>", my_print())
#
# root.mainloop()