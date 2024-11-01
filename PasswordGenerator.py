import string
from random import randint
from tkinter import *

# Bit messy ig

def genPassword(): # Bascially the same thing as console version of this
    num = nBool.get()
    symbol = sBool.get()
    length = lInt.get()
    usable = string.ascii_letters
    if num:
        usable += string.digits
    if symbol:
        usable += string.punctuation
    x = []
    for i in range(length):
        x.append(usable[randint(0, len(usable) - 1)])
    output['text'] = "".join(x) + "\n Copied to Clipboard" # Displays the password on a label
    window.clipboard_clear()
    window.clipboard_append("".join(x)) # Automatically copies the generated password


window = Tk()
numRange = [i for i in range(5, 33)] # For Length Option Menu

nBool = BooleanVar()
sBool = BooleanVar()
lInt = IntVar()
lInt.set(5)

# Widgets mainly to config

InputNum = Checkbutton(window, text="Numbers", variable=nBool)
InputNum.grid(column=0, row=0)

InputSymbol = Checkbutton(window, text="Symbols", variable=sBool)
InputSymbol.grid(column=0, row=1)

InputLength = OptionMenu(window, lInt, *numRange)
InputLength.grid(column=0, row=2)

gen = Button(window, text="Click here", command=genPassword)
gen.grid(column=2, row=1)

output = Label(window)
output.grid(column=2, row=2)

laksh = Label(window, text="- Laksh =D") # Tis me 
laksh.place(x=245, y=80)

# Window

window.geometry("300x100")
window.resizable(False, False)
window.title("Password Generator")
window.mainloop()
