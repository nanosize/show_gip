import requests
from ping3 import ping

import tkinter as tk
from tkinter import ttk
from tkinter import GROOVE
import pyperclip

'''
def get_gip():
    global gip
    try:
        gip = requests.get('http://api.ipify.org/')
        #print(gip.text)
    except requests.exceptions.RequestException as e:
        print("noconnection")
'''

class main(tk.Frame):
    def __init__(self,gip=None,gip2=None):
        self.gip = gip 
    def get_gip(self):
        target = 'example.com' 
        result = ping(target)

        if result == False:
            gip="No Internet Connection"
            print(gip)
        else:
            gip_requests = requests.get('http://api.ipify.org/')
            gip = gip_requests.text
            print(gip)
        
        '''
        try:
            gip = requests.get('http://api.ipify.org/')
        except requests.exceptions.RequestException as e:
            print("No Internet Connection")
        '''
class window(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.window_config()
        self.make_widget()

    def window_config(self):
        self.master.title('ShowGip')
        self.master.geometry('400x300')

    def make_widget(self):
        self.label()
        #self.gip_Label()
        #self.button_copy()
        #self.button_reload()
        
    def label(self):
        self.label = master.Label(
            root,
            text='現在のグローバルIP',
            padding = (5,10),
            font = ('gothic',20)
        )
        self.label.pack()
    def gip_Label(self):
        self.frame_1 = tk.Frame(
        root,
        bd=5,
        relief=GROOVE,
        pady=15,padx=60
        )
        gip_Label = ttk.Label(
        self.frame_1, 
        text="test",
        font=('', 20)
        )
        self.frame.pack()
        self.gip_Label.pack()

    def button_copy(self):
        self.button_copy = ttk.Button(
            self,
            text = "クリップボードにコピー",
        )
        self.button_copy.pack()
    def button_reload(self):
        self.button_reload = ttk.Button(
            self,
            text = '更新'
            )
        self.button_reload.pack()

class copy():
    def copy(gip):
        pyperclip.copy(gip)

gip="test"
pyperclip.copy(gip) 
root = tk.Tk()
win = window(master=root)
win.mainloop()


'''
        self.root.title('ShowGip')
        self.root.geometry('400x300')
        self.root.configure(bg='white')

my_global_ip = main()
my_global_ip.get_gip()
'''