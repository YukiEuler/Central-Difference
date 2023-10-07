import tkinter as tk
import customtkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import Image
import os
from math import *
import numpy as np
before, toolbar = None, None

def handle_click_1(event):
    f = eval(f"lambda x: {entry_f.get()}")
    x, h = float(entry_x.get()), float(entry_h.get())
    label_a.configure(text = f"Hasil turunan {entry_f.get()} di titik {entry_x.get()} adalah {count_two_point()}")
    plot(1)

def handle_click_2(event):
    f = eval(f"lambda x: {entry_f.get()}")
    x, h = float(entry_x.get()), float(entry_h.get())
    label_a.configure(text = f"Hasil turunan {entry_f.get()} di titik {entry_x.get()} adalah {count_four_point()}")
    plot(2)

def count_two_point():
    f = eval(f"lambda x: {entry_f.get()}")
    x, h = float(entry_x.get()), float(entry_h.get())
    return (f(x+h)-f(x-h))/(2*h)

def count_four_point():
    f = eval(f"lambda x: {entry_f.get()}")
    x, h = float(entry_x.get()), float(entry_h.get())
    return (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)

def get_point(f,x):
    y = np.array([])
    for i in x:
        try:
            y = np.append(y, f(i))
        except:
            y = np.append(y, np.nan)
    return y

def plot(clicked):
    global before, toolbar
    f = eval(f"lambda x: {entry_f.get()}")
    x, h = float(entry_x.get()), float(entry_h.get())
    
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 90)
  
    # list of squares
    X = np.linspace(x-5, x+5, 10000)
    y = get_point(f,X)
    y[:-1][abs(np.diff(y)) > 10] = np.nan
    # adding the subplot
    plot1 = fig.add_subplot(111)
    plot1.clear()
  
    # plotting the graph
    plot1.plot(X,y)
  
    plot1.plot(x-h,f(x-h),'go')
    plot1.plot(x+h,f(x+h),'go')
    if clicked == 2:
        plot1.plot(x-2*h,f(x-2*h),'go')
        plot1.plot(x+2*h,f(x+2*h),'go')
    grad = count_four_point() if clicked == 2 else count_two_point()
    f_diff = lambda point: grad*(point-x+h) + f(x-h)
    line = get_point(f_diff,X)
    plot1.plot(X,line)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    if before:
        before.destroy()
        toolbar.destroy()
    before = canvas.get_tk_widget()
    before.pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


customtkinter.set_appearance_mode("dark")
window = customtkinter.CTk()
window.title('Aplikasi Turunan')
window.geometry("600x400+10+20")
judul = customtkinter.CTkLabel(master=window, text="Metode Numerik Turunan Selisih Tengah")
fungsi = customtkinter.CTkLabel(master=window, text="Fungsi")
entry_f = customtkinter.CTkEntry(master=window)
x_p = customtkinter.CTkLabel(master=window, text="x")
entry_x = customtkinter.CTkEntry(master=window)
h = customtkinter.CTkLabel(master=window, text="h")
entry_h = customtkinter.CTkEntry(master=window)
judul.pack()
fungsi.pack()
entry_f.pack()
x_p.pack()
entry_x.pack()
h.pack()
entry_h.pack()

customtkinter.CTkLabel(master=window, text="", height=5).pack()
button1 = customtkinter.CTkButton(master=window, text="Hitung O(x^2)!")#,command=handle_click_1)
button1.pack()
button1.bind("<Button-1>",handle_click_1)
customtkinter.CTkLabel(master=window, text="", height=5).pack()
button2 = customtkinter.CTkButton(master=window, text="Hitung O(x^4)!")#,command=handle_click_2)
button2.pack()
button2.bind("<Button-1>",handle_click_2)

os.path.join("images.jpeg")
frame_a = tk.Frame()
label_a = customtkinter.CTkLabel(master=window, text="Masukkan fungsi, x, dan h!")
label_a.pack(ipadx=1,ipady=1)
peko = customtkinter.CTkImage(light_image=Image.open(os.path.join("images.png")),size=(190,190))
customtkinter.CTkLabel(master=window, text="", image=peko).place(x=25,y=440)
herta = customtkinter.CTkImage(light_image=Image.open("kurukuru-kururing.gif"),size=(190,190))
customtkinter.CTkLabel(master=window, text="", image=herta).place(x=1100,y=440)
logo = customtkinter.CTkImage(light_image=Image.open(os.path.join("logo-if.png")),size=(160,316/788*150))
customtkinter.CTkLabel(master=window, text="", image=logo).place(x=1100,y=25)
window.mainloop()