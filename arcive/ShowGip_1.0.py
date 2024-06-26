import tkinter as tk 
from tkinter import *
from tkinter import ttk
import requests
import pyperclip

#window作成
root = Tk()
root.title('show-gip')
root.geometry('300x180')

data='''R0lGODlhQABAANUAAP///0SKytjk8vb4/MPV683c7vD1+5O23aC+4KzG5LfO5+Lr
9VeTzmid0nel1YWu2ezy+EWKykiMy0iNy0mNy0yPzE2QzE6QzU+RzWSe02Wf02af
1Gag1Gig1J3C45/D5KDD5MHY7sLZ7vD2++/1+v///wAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAACH5BAUAACUALAAAAABAAEAAAAb/wJJwSCwaj8ikcslsOp/Q
qHRKrVqv2Oxw5NFQAuCweEwum8UUDmj0FGHO8LhcfBE1RZG5fk+O2JUGF3yDgxck
SiCEinseShyLkHEaSl+RlmQTSpebY5qcn55lDAkQAKanCWEKp6ymCmECraYFDmah
ZLGyAK9guboCYbqntWS3YgjCAMC9ycsByQALZcZhpcLOvrLO0ADEYtQBDdDYzcHQ
qZ1JZcjlzNfmyQXF6mQJ47Dtz/fpSGWr+dlabeM2rx8uaLwCBGQ1EFrBI2UWskIX
4J+uhKwgJEgwgNVDIxEnymlFhiEYAh75QTx4isHIlGJMBrB36mORkDVf5ox5ahlN
/1M2ieAEqpMoT1M+YYYBl20OyTEyfwIIOmTo1KJXjyoDI5WqEKtOlYKRuUBsAKYw
HWxMcACqWW5Zl9Ib0xRMgVMD3O6El8xrCbDujI59u+/bXDF1FYp9qvWXX8CK9+qT
PFkYRbkG6cJMPJgyt7YqQbI0yrly3M668j4enbU0Y76yEEw7jG+na8KyBlw2nBkx
K2K3PZ9a8KA4HLSnIAgQ0DFnguUCBVCUGQe5w8iOUTs7Tvsk3MDa+G4/A06qMPAC
xc8Bx+66RKTq5YATRxB7eO3ru4Ox1td+evzy6TdTfe9tBWB1AgZQVn8FNmQggr2N
wYACzf1nkSwJ+bKbLQl+QkEIJR5eYoEjIVqyASIlRtJIEiQIkiIhhiyBx4t8+NFE
CC7SGEcdT3CRgQQ6klFBBx+wocWRSCap5JJMNunkk1YEAQA7'''

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(data=data))

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
    try:
        gip = requests.get('http://api.ipify.org/')
        #print(gip.text)
    except requests.exceptions.RequestException as e:
        gip = "00"
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
