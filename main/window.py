from tkinter import *
from tkinter import ttk
import requests 

#window作成
root = Tk()
root.title('グローバルIP表示')
root.geometry('300x200')

#タイトル
Label = ttk.Label(root,text='現在のグローバルIP',padding = (5,10),font = ('gothic',20))
Label.pack()

#メインコードの実装
def get_gip():
    global gip
    gip = requests.get('http://api.ipify.org/') 
    #print(gip.text)
get_gip()
print("line20" + gip.text)

#gip表示
frame_1 = Frame(root, bd=4, relief=GROOVE,pady=10, padx=80)
GIP_label = ttk.Label(frame_1, text=gip.text)
frame_1.pack()
GIP_label.pack()

button = ttk.Button(root,text = 'OK')
#button.pack()

#windowの表示
root.mainloop()