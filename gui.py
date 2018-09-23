from tkinter import Tk, Label, Button, Frame, Menu, Scale, HORIZONTAL
from tkColorChooser import askcolor
from bulb_controller import BulbsController
from yeelight import BulbType
import utils


def donothing():
    pass


class MainWindow(object):

    def __init__(self, master):
        self.master = master
        master.title("Yeelight Control")
        self.bc = BulbsController()
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Load_from_file", command=self.bc.load_bulbs_from_file)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)
        self._draw_frame()

    def _draw_frame(self):
        self.frame = Frame(self.master).grid(row=0)
        for index, bulb in enumerate(self.bc.get_bulbs()):
            print bulb
            bulb_name = str(index) + ' ' + bulb.__str__()
            label = Label(self.frame, text=bulb_name)
            label.grid(row=index, column=0)
            toggle_button = Button(self.frame, text='Toggle', command=bulb.toggle)
            toggle_button.grid(row=index, column=1)
            slider_brightness = Scale(self.frame, from_=1, to=100, orient=HORIZONTAL)
            slider_brightness.grid(row=index, column=2)
            slider_brightness.bind("<ButtonRelease-1>", lambda event, bulb_param=bulb, slider=slider_brightness:
                                   self.__class__.change_brightness(bulb_param, slider.get()))
            slider_temperature = Scale(self.frame, from_=1700, to=6500, orient=HORIZONTAL)
            slider_temperature.grid(row=index, column=3)
            slider_temperature.bind("<ButtonRelease-1>", lambda event, bulb_param=bulb, slider=slider_temperature:
                                    self.__class__.change_temperature(bulb_param, slider.get()))


            if bulb.bulb_type == BulbType.Color:
                set_color_button = Button(self.frame, text='Choose Color')
                set_color_button.__dict__['bulb'] = bulb
                set_color_button.grid(row=index, column=4)
                set_color_button['command'] = lambda bulb_param=bulb, button=set_color_button:\
                    self.__class__.change_color(button, bulb_param)

        #self.file_load = Button(self.master, text='Load_from_file', command=self._draw_frame)
        #self.file_load.grid(row=2, column=0)

    @staticmethod
    def change_color(button, bulb):
        color = askcolor()
        button.configure(bg=color[1])
        bulb.set_rgb(* utils.str_color_to_rgb_tuple(color[1]))

    @staticmethod
    def change_brightness(bulb, value):
        bulb.set_brightness(value)

    @staticmethod
    def change_temperature(bulb, value):
        bulb.set_color_temp(value)

if __name__ == '__main__':

    root = Tk()
    window = MainWindow(root)
    root.mainloop()

