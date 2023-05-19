import tkinter as tk

def button_clicked():
    label.configure(text="Button Clicked!")

window = tk.Tk()
window.title("My GUI")
window.geometry("300x200")

label = tk.Label(window, text="Hello, World!")
label.pack()

button = tk.Button(window, text="Click Me!", command=button_clicked)
button.pack()

window.mainloop()
