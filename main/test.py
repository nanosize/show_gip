from tkinter import *
# メインウィンドウの設定
root = Tk()              #ウィンドウを定義
root.title("window")     #ウィンドウタイトルを設定
root.geometry("300x300") #ウィンドウサイズを設定

frame_1 = Frame(root, bd=4, relief=GROOVE)
button_1 = Label(frame_1, text='test')

frame_1.pack()
button_1.pack()

root.mainloop()
