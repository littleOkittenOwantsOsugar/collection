from tkinter import *
from tkinter import messagebox

ro = Tk()
frames = [PhotoImage(file='4567.gif', format='gif -index %i' %(i)) for i in range(16)]


def update(ind):
    frame = frames[ind]
    ind += 1
    print(ind)
    if ind > 15:  # With this condition it will play gif infinitely
        ind = 0
    label.configure(image=frame)
    ro.after(100, update, ind)


label = Label(ro)
label.pack()
ro.after(0, update, 0)
ro.mainloop()