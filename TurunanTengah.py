import tkinter as tk
import customtkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import math

customtkinter.set_appearance_mode("dark")
window = customtkinter.CTk()
window.title('Aplikasi Turunan')
window.geometry("600x400+10+20")
fungsi = customtkinter.CTkLabel(master=window, text="Fungsi")
entry_f = customtkinter.CTkEntry(master=window)
x_p = customtkinter.CTkLabel(master=window, text="x")
entry_x = customtkinter.CTkEntry(master=window)
h = customtkinter.CTkLabel(master=window, text="h")
entry_h = customtkinter.CTkEntry(master=window)
fungsi.pack()
entry_f.pack()
x_p.pack()
entry_x.pack()
h.pack()
entry_h.pack()

def handle_click(event):
    f = eval(f"lambda x: {entry_f.get()}")
    x, h = float(entry_x.get()), float(entry_h.get())
    label_a.configure(text = f"Hasil turunan {entry_f.get()} di titik {entry_x.get()} adalah {(f(x+h)-f(x-h))/(2*h)}")

def plot():
    f = eval(f"lambda x: {entry_f.get()}")
    x, h = float(entry_x.get()), float(entry_h.get())
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
  
    # list of squares
    X = np.linspace(x-1, x+1, 100)
    y = [f(i) for i in X]
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(X,y)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

button = customtkinter.CTkButton(master=window,text="Hitung!",command=plot)
button.pack()
button.bind("<Button-1>", handle_click)

frame_a = tk.Frame()
label_a = customtkinter.CTkLabel(master=window, text="Masukkan fungsi, x, dan h!")
label_a.pack()

window.mainloop()