from tkinter import *
from tkinter import ttk

root = Tk()
root.title('グローバルIP表示')
root.geometry('300x200')

Label = ttk.Label(root,text='現在のGIP',padding = (5,10),font = ('gothic',20))
button = ttk.Button(root,text = 'OK')

Label.pack()
button.pack()

frame = ttk.Frame(root,padding=10)
frame2 = ttk.Frame(
    frame, width=200, height=100,
    borderwidth=10, relief='sunken')
Label_frame = ttk.Label(root,text= "aaa")
frame.pack()
frame2.pack()



#windowの表示
root.mainloop()