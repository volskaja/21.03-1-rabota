from tkinter import *
from turtle import width


raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="#0a090d")
k=10
x1=550
y1=550
for i in range(k):
    x1-=50
    y1-=50
    tahvel.create_rectangle(0,0,x1,y1,width=1,outline="blue", fill="#03fff7")
    tahvel.create_oval(10,10,x1,y1,width=1, outline="blue", fill="#0329ff")
tahvel.grid()

raam.mainloop()