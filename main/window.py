from tkinter import *
from tkinter import ttk
import requests
import pyperclip

#window作成
root = Tk()
root.title('グローバルIP表示')
root.geometry('300x180')

#タイトル
Label = ttk.Label(
    root,
    text='現在のグローバルIP',
    padding = (5,10),
    font = ('gothic',20)
)
Label.pack()

#gipの取得
def get_gip():
    global gip
    gip = requests.get('http://api.ipify.org/') 
    #print(gip.text)
get_gip()

#reloadボタンが押された時
def reload():
    get_gip()
    GIP_label.config(text=gip.text)
    Label.update
    print("dev_point reload")

#gip表示
frame_1 = Frame(
    root,
    bd=5,
    relief=GROOVE,
    pady=15,padx=60
    )
GIP_label = ttk.Label(
    frame_1, 
    text=gip.text,
    font=('', 20)
    )
frame_1.pack()
GIP_label.pack()

#copyボタン
def copy():
    pyperclip.copy(gip.text)

copy_button =ttk.Button(
    root,
    text = "クリップボードにコピー",
    command= copy
)
copy_button.pack()


reload_button = ttk.Button(
        root,
        text = '更新',
        command= reload
        )
reload_button.pack()

#windowの表示
root.mainloop()