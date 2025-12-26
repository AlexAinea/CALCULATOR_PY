import tkinter as tk

root = tk.Tk()
root.title("CALCULATOR")
root.geometry("600x600")

display_frame = tk.Frame(root)
display_frame.pack()

display = tk.Label(display_frame, text="placeholder")
display.pack()

button_frame = tk.Frame(root)
button_frame.pack()



def buttons():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    rows = 0
    
    columns = 0
    for number in numbers:
        button = tk.Button(button_frame,text = number)
        button.grid(row = rows ,column = columns)

        columns += 1
        rem = columns%3
        if rem == 0:
            columns = 0
            rows += 1

buttons()

root.mainloop()