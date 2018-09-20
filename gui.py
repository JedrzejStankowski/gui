from tkinter import Tk, Label, Button
from tkColorChooser import askcolor
from bulb_controller import BulbsController

class MyFirstGUI(object):
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        
        self.color_picker_button = Button(text='Select Color', command=self.change_color)
        self.color_picker_button.pack()

        self.active_color_button = Button(bg='blue', width=50)
        self.active_color_button.pack()

    def change_color(self):
        color = askcolor()
        self.active_color_button.configure(bg=color[1])


class MainWindow(object):
    def __init__(self, master):
        self.master = master
        master.title("Yeelight Control")
        bc = BulbsController()
        for index, bulb in enumerate(bc.get_bulbs()):
            bulb_name = str(index) + ' ' + bulb.__str__()
            self.label = Label(master, text=bulb_name)
            self.label.grid(row=index, column=0)
            self.toggle_button = Button(master, text='Toggle', command=bulb.toggle)
            self.toggle_button.grid(row=index, column=1)



if __name__ == '__main__':
    root = Tk()
    #my_gui = MyFirstGUI(root)
    window = MainWindow(root)
    root.mainloop()

