#ongoing-working on functions

import sys
from tkinter import *

def clear():
    #txtDisplay.delete(0,END)
    #return
#def add():
 #   txt

root = Tk()
frame = Frame(root).pack()

#def number

numb = StringVar()

topframe = Frame(root).pack( side = TOP)

txtDisplay = Entry(frame,textvariable = numb, bd = 10, insertwidth = 2, font = 44).pack(side = TOP)

#first frame

frame1 = Frame(root).pack(side = TOP)
for a in range(1,4):
    buttona = Button(frame1, padx = 16, pady = 16, bd = 6, text = a).pack(side = LEFT)
buttona = Button(frame1, padx = 16, pady = 16, bd = 5, text = "C", command=clear).pack(side = LEFT)


#second frame

frame2 = Frame(root).pack(side = TOP)

for b in range(4,7):
    buttonb = Button(frame2, padx = 16, pady = 16, bd = 6, text = b).pack(side = LEFT)
buttonb= Button(frame2, padx = 16, pady = 16, bd = 6, text = "-").pack()

#third frame

frame3 = Frame(root).pack(side = TOP)

for c in range(7,10):
    buttonc = Button(frame3, padx = 16, pady = 16, bd = 6, text = c).pack(side = LEFT)
buttonc= Button(frame3, padx = 16, pady = 16, bd = 6, text = "+").pack()

# final frame

frame4 = Frame(root).pack(side = TOP)

buttond = Button(frame4, padx = 16, pady = 16, bd = 6, text = "/").pack(side=LEFT)
buttond = Button(frame4, padx = 16, pady = 16, bd = 6, text = "0").pack(side=LEFT)
buttond = Button(frame4, padx = 44, pady = 16, bd = 6, text = "=").pack(fill = X)

root.mainloop()

