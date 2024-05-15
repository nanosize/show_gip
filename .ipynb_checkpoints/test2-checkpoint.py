import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.master.geometry("300x300")
        self.master.title("Tkinter with Class")

        self.create_widgets()

    # Create Widgets function
    def create_widgets(self):
        #Button
        self.button_hello = ttk.Button(self)
        self.button_hello.configure(text="Hello World")
        self.button_hello.configure(command = self.say_Hello) #do not forget to add self!
        self.button_hello.pack()

        #Label
        self.label_hello = ttk.Label(self)
        self.label_hello.configure(text='A Label')
        self.label_hello.pack()

        #Entry
        self.name = tk.StringVar()
        self.entry_name = ttk.Entry(self)
        self.entry_name.configure(textvariable = self.name)
        self.entry_name.pack()

        #Label2
        self.label_name=ttk.Label(self)
        self.label_name.configure(text = 'Please input something in Entry')
        self.label_name.pack()

    # Event Callback Function
    def say_Hello(self):
        print("Hello, World")  # on python console
        self.label_hello.configure(text="I Have benn Clicked!")
        print(self.name.get())
        self.label_name.configure(text=self.name.get())

root = tk.Tk()
app = Application(master=root)#Inheritクラスの継承！
app.mainloop()