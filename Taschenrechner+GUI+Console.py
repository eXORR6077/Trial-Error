from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Calculator")
root.geometry("370x530")
#root.geometry("320x450")
root.resizable(width=False, height=False)
root.iconbitmap("TaschenrechnerTKINTER/calculatorICO.ico")

calculation_list = ["", "", ""]

var1 = 0
var2 = 0
result = 0

def update_window_calc():
    window_calc.config(text=calculation_list)
    return

def click_button_0():
    print(calculation_list)
    if calculation_list[1] == "":
        if calculation_list[0] == "":
            calculation_list[0] = "0"
        elif calculation_list[0] != "":
            calculation_list[0] += "0"
    elif calculation_list[1] != "":
        if calculation_list[2] == "":
            calculation_list[2] = "0"
        elif calculation_list[2] != "":    
            calculation_list[2] += "0"
    update_window_calc()
    print(calculation_list)
    return

def click_button_multiply():
    print(calculation_list)
    if calculation_list[1] == "":
        calculation_list[1] = "*"
    else:
        click_button_clear
    update_window_calc()
    print(calculation_list)
    return

def click_button_divide():
    print(calculation_list)
    if calculation_list[1] == "":
        calculation_list[1] = "/"
    else:
        click_button_clear
    update_window_calc()
    print(calculation_list)
    return

def click_button_add():
    print(calculation_list)
    if calculation_list[1] == "":
        calculation_list[1] = "+"
    else:
        click_button_clear
    update_window_calc()
    print(calculation_list)
    return

def click_button_minus():
    print(calculation_list)
    if calculation_list[1] == "":
        calculation_list[1] = "-"
    else:
        click_button_clear
    update_window_calc()
    print(calculation_list)
    return

def click_button_1():
    print(calculation_list)
    if calculation_list[1] == "":
        if calculation_list[0] == "":
            calculation_list[0] = "1"
        elif calculation_list[0] != "":
            calculation_list[0] += "1"
    elif calculation_list[1] != "":
        if calculation_list[2] == "":
            calculation_list[2] = "1"
        elif calculation_list[2] != "":    
            calculation_list[2] += "1"
    update_window_calc()
    print(calculation_list)
    return

def click_button_2():
    print(calculation_list)
    if calculation_list[1] == "":
        if calculation_list[0] == "":
            calculation_list[0] = "2"
        elif calculation_list[0] != "":
            calculation_list[0] += "2"
    elif calculation_list[1] != "":
        if calculation_list[2] == "":
            calculation_list[2] = "2"
        elif calculation_list[2] != "":    
            calculation_list[2] += "2"
    update_window_calc()
    print(calculation_list)
    return

def click_button_3():
    print(calculation_list)
    if calculation_list[1] == "":
        if calculation_list[0] == "":
            calculation_list[0] = "3"
        elif calculation_list[0] != "":
            calculation_list[0] += "3"
    elif calculation_list[1] != "":
        if calculation_list[2] == "":
            calculation_list[2] = "3"
        elif calculation_list[2] != "":    
            calculation_list[2] += "3"
    update_window_calc()
    print(calculation_list)
    return

def click_button_4():
    print(calculation_list)
    if calculation_list[1] == "":
        if calculation_list[0] == "":
            calculation_list[0] = "4"
        elif calculation_list[0] != "":
            calculation_list[0] += "4"
    elif calculation_list[1] != "":
        if calculation_list[2] == "":
            calculation_list[2] = "4"
        elif calculation_list[2] != "":    
            calculation_list[2] += "4"
    update_window_calc()
    print(calculation_list)       
    return

def click_button_5():
    print(calculation_list)
    if calculation_list[1] == "":
        if calculation_list[0] == "":
            calculation_list[0] = "5"
        elif calculation_list[0] != "":
            calculation_list[0] += "5"
    elif calculation_list[1] != "":
        if calculation_list[2] == "":
            calculation_list[2] = "5"
        elif calculation_list[2] != "":    
            calculation_list[2] += "5"
    update_window_calc()
    print(calculation_list)
    return

def click_button_6():
    print(calculation_list)
    if calculation_list[1] == "":
        if calculation_list[0] == "":
            calculation_list[0] = "6"
        elif calculation_list[0] != "":
            calculation_list[0] += "6"
    elif calculation_list[1] != "":
        if calculation_list[2] == "":
            calculation_list[2] = "6"
        elif calculation_list[2] != "":    
            calculation_list[2] += "6"
    update_window_calc()
    print(calculation_list)
    return

def click_button_7():
    print(calculation_list)
    if calculation_list[1] == "":
        if calculation_list[0] == "":
            calculation_list[0] = "7"
        elif calculation_list[0] != "":
            calculation_list[0] += "7"
    elif calculation_list[1] != "":
        if calculation_list[2] == "":
            calculation_list[2] = "7"
        elif calculation_list[2] != "":    
            calculation_list[2] += "7"
    update_window_calc()
    print(calculation_list)
    return

def click_button_8():
    print(calculation_list)
    if calculation_list[1] == "":
        if calculation_list[0] == "":
            calculation_list[0] = "8"
        elif calculation_list[0] != "":
            calculation_list[0] += "8"
    elif calculation_list[1] != "":
        if calculation_list[2] == "":
            calculation_list[2] = "8"
        elif calculation_list[2] != "":    
            calculation_list[2] += "8"
    update_window_calc()
    print(calculation_list)
    return

def click_button_9():
    print(calculation_list)
    if calculation_list[1] == "":
        if calculation_list[0] == "":
            calculation_list[0] = "9"
        elif calculation_list[0] != "":
            calculation_list[0] += "9"
    elif calculation_list[1] != "":
        if calculation_list[2] == "":
            calculation_list[2] = "9"
        elif calculation_list[2] != "":    
            calculation_list[2] += "9"
    update_window_calc()
    print(calculation_list)
    return

def click_button_clear():
    print(calculation_list)
    calculation_list[0] = ""
    calculation_list[1] = ""
    calculation_list[2] = ""
    update_window_calc()
    print(calculation_list)
    return

def click_button_calc():
    global var1
    global var2
    var1 = int(calculation_list[0])
    var2 = int(calculation_list[2])
    
    print(calculation_list, var1, var2)
    if calculation_list[0] == "" and calculation_list[1] == "" and calculation_list[2] == "":
        click_button_clear()
    elif calculation_list[1] == "+":
        global result
        result = var1 + var2
    elif calculation_list[1] == "-":
        result = var1 - var2
    elif calculation_list[1] == "/":
        result = var1 / var2
    elif calculation_list[1] == "*":
        result = var1 * var2
    else:
        click_button_clear()
    print(calculation_list, result)
    change_window_calc()
    
    return result

def change_window_calc():
    window_calc.config(text=result)
    return

#GUI
window_calc = Label(root, bg="white", text=result, height=5, width=46)
window_calc.grid(row=0, column=0, columnspan=4, sticky=W)

button_multiply = Button(root, text="*", height=5, width=10, command=click_button_multiply)
button_multiply.grid(row=4, column=1, padx=1, pady=1, sticky=W)

button_divide = Button(root, text="/", height=5, width=10, command=click_button_divide)
button_divide.grid(row=4, column=2, padx=1, pady=1, sticky=W)

button_sum = Button(root, text="=", height=5, width=10, command=click_button_calc)
button_sum.grid(row=4, column=3, padx=1, pady=1, sticky=W)

button_add = Button(root, text="+", height=5, width=10, command=click_button_add)
button_add.grid(row=2, column=3, padx=1, pady=1, sticky=W)

button_minus = Button(root, text="-", height=5, width=10, command=click_button_minus)
button_minus.grid(row=3, column=3, padx=1, pady=1, sticky=W)

button_0 = Button(root, text="0", height=5, width=10, command=click_button_0)
button_0.grid(row=4, column=0, padx=1, pady=1, sticky=W)

button_1 = Button(root, text="1", height=5, width=10, command=click_button_1)
button_1.grid(row=3, column=0, padx=1, pady=1, sticky=W)

button_2 = Button(root, text="2", height=5, width=10, command=click_button_2)
button_2.grid(row=3, column=1, padx=1, pady=1, sticky=W)

button_3 = Button(root, text="3", height=5, width=10, command=click_button_3)
button_3.grid(row=3, column=2, padx=1, pady=1, sticky=W)

button_4 = Button(root, text="4", height=5, width=10, command=click_button_4)
button_4.grid(row=2, column=0, padx=1, pady=1, sticky=W)

button_5 = Button(root, text="5", height=5, width=10, command=click_button_5)
button_5.grid(row=2, column=1, padx=1, pady=1, sticky=W)

button_6 = Button(root, text="6", height=5, width=10, command=click_button_6)
button_6.grid(row=2, column=2, padx=1, pady=1, sticky=W)

button_7 = Button(root, text="7", height=5, width=10, command=click_button_7)
button_7.grid(row=1, column=0, padx=1, pady=1, sticky=W)

button_8 = Button(root, text="8", height=5, width=10, command=click_button_8)
button_8.grid(row=1, column=1, padx=1, pady=1, sticky=W)

button_9 = Button(root, text="9", height=5, width=10, command=click_button_9)
button_9.grid(row=1, column=2, padx=1, pady=1, sticky=W)

button_clear = Button(root, text="C", height=5, width=10, command=click_button_clear)
button_clear.grid(row=1, column=3, padx=1, pady=1, sticky=W)


root.mainloop()


