
import tkinter

window = tkinter.Tk()
window.title("CALCULATOR")

#CORE
expression = ""
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)

def clear():
    global expression
    #clear label result
    expression=""
    label_result.config(text=expression)


def calculate():
    global expression
    result = ""
    #if expression is empty then the following happens
    if expression != "":
        try:
            result =eval(expression)
        except:
            result = "error"
            expression = ""
    #print in label_result
    label_result.config(text=result)
#END OF CORE


#Creating GUI
#fit to frame to center all things
frame = tkinter.LabelFrame(window, width=100, text="this is my calculator...", bg='#66ffcc', padx=50, pady=50)
frame.pack(padx=300, pady=100)
label_result = tkinter.Label(frame, text="", font=10, width=7, height=3)
label_result.grid(row=-0, column=0, columnspan=4)

button_1 = tkinter.Button(frame, text="1", font=10, width=7, height=3 , command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(frame, text="2", font=10, width=7, height=3, command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(frame, text="3", font=10, width=7, height=3, command=lambda: add("3"))
button_3.grid(row=1, column=2)


button_add = tkinter.Button(frame, text="+", font=10, width=7, height=3, bg='#00cc00' , command=lambda: add("+"))
button_add.grid(row=1, column=3)

button_4 = tkinter.Button(frame, text="4", font=10, width=7, height=3, command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(frame, text="5", font=10, width=7, height=3, command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(frame, text="6", font=10, width=7, height=3, command=lambda: add("6"))
button_6.grid(row=2, column=2)


button_sub = tkinter.Button(frame, text="-", font=10, width=7, height=3, bg='#00cc00', command=lambda: add("-"))
button_sub.grid(row=2, column=3)

button_7 = tkinter.Button(frame, text="7", font=10, width=7, height=3, command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(frame, text="8", font=10, width=7, height=3, command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 = tkinter.Button(frame, text="9", font=10, width=7, height=3, command=lambda: add("9"))
button_9.grid(row=3, column=2)


button_multi = tkinter.Button(frame, text="*", font=10, width=7, height=3, bg='#00cc00', command=lambda: add("*"))
button_multi.grid(row=3, column=3)

button_clear = tkinter.Button(frame, text="C", font=10, width=7, height=3, command=lambda: clear())
button_clear.grid(row=4, column=0)

button_0 = tkinter.Button(frame, text="0", font=10, width=7, height=3, command=lambda: add("0"))
button_0.grid(row=4, column=1)

button_dot = tkinter.Button(frame, text=".", font=10, width=7, height=3, command=lambda: add("."))
button_dot.grid(row=4, column=2)


button_division = tkinter.Button(frame, text="/", font=10, width=7, height=3, bg='#00cc00', command=lambda: add("/"))
button_division.grid(row=4, column=3)

button_equals = tkinter.Button(frame, text="=", font=10, width=35, height=3, bg='#ffff00',  command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan=4)

window.mainloop()
