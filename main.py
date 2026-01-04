import tkinter as tk

root = tk.Tk()
root.title("CALCULATOR")
root.geometry("600x600")

display_frame = tk.Frame(root)
display_frame.pack()

prev_string = ''
display = tk.Label(display_frame, text=prev_string)
display.pack()

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.pack(fill='x')

def value_entry(n):
    global prev_string
    print(n)
    n_string = str(n)
    prev_string += n_string
    display.config(text = prev_string)

def equal():
    global prev_string

    try:
        result = eval(str(prev_string))
        display.config(text = result)
    except Exception:
        display.config(text = "ERROR")
    
def delete():
    global prev_string
    prev_string = prev_string[:-1]
    display.config(text = prev_string)

def clear():
    pass


def buttons():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    rows = 0
    columns = 0

    for number in numbers:
        button = tk.Button(button_frame,text = number ,height= 3 , width= 3, command=lambda n=number: value_entry(n))
        button.grid(row = rows ,column = columns, padx=0, pady=0, sticky="W,E")

        columns += 1
        rem = columns%3
        if rem == 0:
            columns = 0
            rows += 1

    addition = tk.Button(button_frame, text = '+',height= 3 , width= 3, command = lambda: value_entry('+') )
    addition.grid(row= 3, column= 1,sticky="W,E")

    multiply = tk.Button(button_frame, text = '*',height= 3 , width= 3, command = lambda: value_entry('*'))
    multiply.grid(row= 3, column= 2,sticky="W,E")

    divide = tk.Button(button_frame, text = '/',height= 3 , width= 3, command = lambda: value_entry('/'))
    divide.grid(row= 4, column= 0,sticky="W,E")

    modulus = tk.Button(button_frame, text = '%',height= 3 , width= 3, command = lambda: value_entry('%'))
    modulus.grid(row= 4, column= 1,sticky="W,E")

    exponent = tk.Button(button_frame, text = '**',height= 3 , width= 3, command = lambda: value_entry('**'))
    exponent.grid(row= 4, column= 2,sticky="W,E")

    s_root = tk.Button(button_frame, text = "√",height= 3 , width= 3, command = lambda: value_entry('√'))
    s_root.grid(row= 5, column= 0,sticky="W,E")

    subtract = tk.Button(button_frame, text = '-',height= 3 , width= 3, command = lambda: value_entry('-'))
    subtract.grid(row= 5, column= 1,sticky="W,E")

    delete_btn = tk.Button(button_frame, text = 'DELETE',height= 3 , width= 3 , command = delete)
    delete_btn.grid(row= 5, column= 2,sticky="W,E")

    clear_btn = tk.Button(button_frame, text = 'CLEAR',height= 3 , width= 3)
    clear_btn.grid(row= 6, column= 0,sticky="W,E")

    equal_btn = tk.Button(button_frame, text = '=',height= 3 , width= 3 ,command= equal)
    equal_btn.grid(row= 6, column= 1,sticky="W,E")

buttons()

root.mainloop()