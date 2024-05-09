from tkinter import *
# メインウィンドウの設定
root = Tk()              #ウィンドウを定義
root.title("window")     #ウィンドウタイトルを設定
root.geometry("300x300") #ウィンドウサイズを設定

frame_1 = Frame(root, bd=4, relief=GROOVE)
frame_2 = Frame(root, bd=4, relief=GROOVE)
frame_3 = Frame(root, bd=4, relief=GROOVE)
 
# ボタンwidgetを設定
button_1 = Button(frame_1, text='Button1-a')
button_2 = Button(frame_1, text='Button2-bb')
button_3 = Button(frame_1, text='Button3-ccc')
button_4 = Button(frame_2, text='Button4-dddd')
button_5 = Button(frame_2, text='Button5-eeeee')
button_6 = Button(frame_3, text='Button6-ffffff')
 
# widgetの配置を設定
frame_1.grid(row=0, column=0)
frame_2.grid(row=1, column=1)
frame_3.grid(row=2, column=2)
button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()
button_5.pack()
button_6.pack()

root.mainloop()
