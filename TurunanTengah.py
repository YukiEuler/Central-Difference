import customtkinter
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import Image
from math import *
import numpy as np

def central_difference_two_points(f,x,h):
    return (f(x+h)-f(x-h))/(2*h)

def central_difference_four_points(f,x,h):
    return (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)

def get_point(f,x):
    try: return f(x)
    except: return np.nan
    
class GUI:
    def __init__(self,window):
        self.window = window
        self.label_judul = customtkinter.CTkLabel(master=window, text='Metode Numerik Turunan Selisih Tengah')
        self.label_fungsi = customtkinter.CTkLabel(master=window, text='Fungsi')
        self.entry_fungsi = customtkinter.CTkEntry(master=window)
        self.label_x = customtkinter.CTkLabel(master=window, text='x')
        self.entry_x = customtkinter.CTkEntry(master=window)
        self.label_h = customtkinter.CTkLabel(master=window, text='h')
        self.entry_h = customtkinter.CTkEntry(master=window)
        self.button1 = customtkinter.CTkButton(master=window, text='Hitung O(h^2)!')
        self.button2 = customtkinter.CTkButton(master=window, text='Hitung O(h^4)!')
        self.label_hasil = customtkinter.CTkLabel(master=window, text='Masukkan fungsi, x, dan h!')
        self.peko = customtkinter.CTkImage(light_image=Image.open('images.png'),size=(190,190))
        self.herta = customtkinter.CTkImage(light_image=Image.open('kurukuru-kururing.gif'),size=(190,190))
        self.logo = customtkinter.CTkImage(light_image=Image.open('logo-if.png'),size=(160,316/788*150))
        self.kelompok = customtkinter.CTkImage(light_image=Image.open('kelompok.png'),size=(562/2,246/2))
        self.f = None
        self.x = None
        self.h = None
        self.mode = None
        self.canvas = None
        self.toolbar = None
        self.show()
        
    def show(self):
        self.window.title('Aplikasi Turunan Selisih Tengah')
        self.window.geometry('600x400+10+20')
        self.label_judul.pack()
        self.label_fungsi.pack()
        self.entry_fungsi.pack()
        self.label_x.pack()
        self.entry_x.pack()
        self.label_h.pack()
        self.entry_h.pack()
        customtkinter.CTkLabel(master=self.window, text='', height=5).pack()
        self.button1.pack()
        self.button1.bind('<Button-1>', self.handle_click_1)
        customtkinter.CTkLabel(master=self.window, text='', height=5).pack()
        self.button2.pack()
        self.button2.bind('<Button-1>', self.handle_click_2)
        self.label_hasil.pack()
        customtkinter.CTkLabel(master=self.window, text='', image=self.peko).place(x=25,y=440)
        customtkinter.CTkLabel(master=self.window, text='', image=self.herta).place(x=1100,y=440)
        customtkinter.CTkLabel(master=self.window, text='', image=self.logo).place(x=1100,y=25)
        customtkinter.CTkLabel(master=self.window, text='', image=self.kelompok).place(x=980,y=100)

    def handle_click_1(self,event):
        try:
            self.f = eval(f'lambda x: {self.entry_fungsi.get()}')
            self.x, self.h = float(self.entry_x.get()), float(self.entry_h.get())
            self.mode = 1
        except:
            self.label_hasil.configure('Terdapat masukan yang tidak valid')
            return
        try:
            self.label_hasil.configure(text = f'Hasil turunan {self.entry_fungsi.get()} di titik {self.entry_x.get()} adalah {central_difference_two_points(self.f,self.x,self.h)}')
            self.plot()
        except:
            self.label_hasil.configure(text='Titik diluar domain dari fungsi')

    def handle_click_2(self,event):
        try:
            self.f = eval(f'lambda x: {self.entry_fungsi.get()}')
            self.x, self.h = float(self.entry_x.get()), float(self.entry_h.get())
            self.mode = 2
        except:
            self.label_hasil.configure('Terdapat masukan yang tidak valid')
            return
        try:
            self.label_hasil.configure(text = f'Hasil turunan {self.entry_fungsi.get()} di titik {self.entry_x.get()} adalah {central_difference_four_points(self.f,self.x,self.h)}')
            self.plot()
        except:
            self.label_hasil.configure(text='Titik diluar domain dari fungsi')

    def plot(self):
        fig = Figure(figsize = (5, 5), dpi = 90)

        x = np.linspace(self.x-5, self.x+5, 10000)
        y = np.array([get_point(self.f,i) for i in x])
        y[:-1][abs(np.diff(y)) > 10] = np.nan

        plot1 = fig.add_subplot(111)
        plot1.clear()
        plot1.plot(x,y)
    
        plot1.plot(self.x - self.h, self.f(self.x - self.h), 'go')
        plot1.plot(self.x + self.h, self.f(self.x + self.h), 'go')
        if self.mode == 2:
            plot1.plot(self.x - 2*self.h, self.f(self.x - 2*self.h), 'go')
            plot1.plot(self.x + 2*self.h, self.f(self.x + 2*self.h),'go')

        grad = central_difference_four_points(self.f,self.x,self.h) if self.mode == 2 else central_difference_two_points(self.f,self.x,self.h)
        f_diff = lambda point: grad*(point-self.x+self.h) + self.f(self.x-self.h)
        line = np.array([get_point(f_diff,i) for i in x])
        plot1.plot(x,line)

        canvas = FigureCanvasTkAgg(fig, master=window)  
        canvas.draw()
        if self.canvas:
            self.canvas.destroy()
            self.toolbar.destroy()
        self.canvas = canvas.get_tk_widget()
        self.canvas.pack()
    
        self.toolbar = NavigationToolbar2Tk(canvas, self.window)
        self.toolbar.update()
    
        canvas.get_tk_widget().pack()

customtkinter.set_appearance_mode('dark')
window = customtkinter.CTk()
gui = GUI(window)
window.mainloop()