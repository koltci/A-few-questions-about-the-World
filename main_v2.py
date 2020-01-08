#!/usr/bin/env python3
from tkinter import *
import main_v201
from tkinter import messagebox

root01 = Tk()
#root01.title(main_v201.t00)
root01.geometry("500x300")
root01.resizable(0, 0)

f00 = Frame(root01, bg='gray54', width=500, height=300)
f1 = Frame(root01, bg='gray54', width=500, height=300)
f2 = Frame(root01, bg='gray54', width=500, height=300)
f3 = Frame(root01, bg='gray54', width=500, height=300)
f4 = Frame(root01, bg='gray54', width=500, height=300)
f5 = Frame(root01, bg='gray54', width=500, height=300)
f6 = Frame(root01, bg='gray54', width=500, height=300)
f7 = Frame(root01, bg='gray54', width=500, height=300)
f8 = Frame(root01, bg='gray54', width=500, height=300)
f9 = Frame(root01, bg='gray54', width=500, height=300)
f10 = Frame(root01, bg='gray54', width=500, height=300)
f11 = Frame(root01, bg='gray54', width=500, height=300)
f12 = Frame(root01, bg='gray54', width=500, height=300)
f13 = Frame(root01, bg='gray54', width=500, height=300)
f14 = Frame(root01, bg='gray54', width=500, height=300)
f15 = Frame(root01, bg='gray54', width=500, height=300)
f16 = Frame(root01, bg='gray54', width=500, height=300)
f17 = Frame(root01, bg='gray54', width=500, height=300)

f1.place(x=0, y=0)
lang = 'EN'
lin = 34
linb = 38

# ETYKIETY
#f0
eth = "0x309f162b850b253834436a53BaC1152557D30F60"
lblDonat = Label(f00, bg='gray54', fg='white', wraplength=400, text="ETH: " + eth)
lblDonat.place(relx=0.5, rely=0.3, anchor='n')
# f1
lbl01 = Label(f1, bg='gray54', fg='white', wraplength=400)
lbl01.place(relx=0.5, rely=0.3, anchor='n')
lblLicense = Label(f1, bg='gray54', fg='white', text="MIT License", font=("Helvetica", 8), wraplength=200)
lblLicense.place(relx=0.5, rely=0.9, anchor='n')
# f2
lbl02 = Label(f2, bg='gray54', fg='white', wraplength=400)
lbl02.place(relx=0.5, rely=0.3, anchor='n')
# f3
lbl03 = Label(f3, bg='gray54', fg='white', wraplength=400)
lbl03.place(relx=0.5, rely=0.3, anchor='n')
# f4
lbl04 = Label(f4, bg='gray54', fg='white', wraplength=400)
lbl04.place(relx=0.5, rely=0.3, anchor='n')
# f5
lbl05 = Label(f5, bg='gray54', fg='white', wraplength=400)
lbl05.place(relx=0.5, rely=0.3, anchor='n')
# f6
lbl06 = Label(f6, bg='gray54', fg='white', wraplength=400)
lbl06.place(relx=0.5, rely=0.3, anchor='n')
# f7
lbl07 = Label(f7, bg='gray54', fg='white', wraplength=400)
lbl07.place(relx=0.5, rely=0.3, anchor='n')
# f8
lbl08 = Label(f8, bg='gray54', fg='white', wraplength=400)
lbl08.place(relx=0.5, rely=0.3, anchor='n')
# f9
lbl09 = Label(f9, bg='gray54', fg='white', wraplength=400)
lbl09.place(relx=0.5, rely=0.3, anchor='n')
# f10
lbl10 = Label(f10, bg='gray54', fg='white', wraplength=400)
lbl10.place(relx=0.5, rely=0.2, anchor='n')
# f11
lbl11 = Label(f11, bg='gray54', fg='white', wraplength=400)
lbl11.place(relx=0.5, rely=0.2, anchor='n')
# f12
lbl12 = Label(f12, bg='gray54', fg='white', wraplength=400)
lbl12.place(relx=0.5, rely=0.2, anchor='n')
# f13
lbl13 = Label(f13, bg='gray54', fg='white', wraplength=400)
lbl13.place(relx=0.5, rely=0.2, anchor='n')
# f14
lbl14 = Label(f14, bg='gray54', fg='white', wraplength=400)
lbl14.place(relx=0.5, rely=0.2, anchor='n')
# f15
lbl15 = Label(f15, bg='gray54', fg='white', wraplength=400)
lbl15.place(relx=0.5, rely=0.2, anchor='n')
# f16
lbl16 = Label(f16, bg='gray54', fg='white', wraplength=450)
lbl16.place(relx=0.5, rely=0.1, anchor='n')
# f17
lbl17 = Label(f17, bg='gray54', fg='white', wraplength=400)
lbl17.place(relx=0.5, rely=0.1, anchor='n')

# PRZYCISKI
#f0
btnBack = Button(f00, text="<-", command=lambda: ramki_zamiana(f00, f1))
btnBack.place(relx=0.5, rely=0.7, anchor='n')
btnCopy = Button(f00, command=lambda: main_v201.copy_clb())
btnCopy.place(relx=0.5, rely=0.5, anchor='n')
# f1
btnDonat = Button(f1, command=lambda: ramki_zamiana(f1, f00))
btnDonat.place(relx=0.75, rely=0.02, anchor='n')
btnlang = Button(f1, text=lang, command=lambda: main_v201.zm_jezyka())
btnlang.place(relx=0.05, rely=0.02, anchor='n')
btn01 = Button(f1, command=lambda: ramki_zamiana(f1, f2))
btn01.place(relx=0.25, rely=0.7, anchor='n')
btn02 = Button(f1, command=lambda: root01.destroy())
btn02.place(relx=0.75, rely=0.7, anchor='n')
# f2
btn03 = Button(f2, command=lambda: ramki_zamiana(f2, f4))
btn03.place(relx=0.25, rely=0.7, anchor='n')
btn04 = Button(f2, command=lambda: ramki_zamiana(f2, f5))
btn04.place(relx=0.75, rely=0.7, anchor='n')
btn05 = Button(f2, command=lambda: ramki_zamiana(f2, f3))
btn05.place(relx=0.50, rely=0.7, anchor='n')
# f3
btn06 = Button(f3, command=lambda: root01.destroy())
btn06.place(relx=0.25, rely=0.7, anchor='n')
btn07 = Button(f3, command=lambda: ramki_zamiana(f3, f5))
btn07.place(relx=0.75, rely=0.7, anchor='n')
# f4
btn08 = Button(f4, command=lambda: root01.destroy())
btn08.place(relx=0.25, rely=0.7, anchor='n')
btn09 = Button(f4, command=lambda: ramki_zamiana(f4, f2))
btn09.place(relx=0.75, rely=0.7, anchor='n')
# f5
btn10 = Button(f5, command=lambda: ramki_zamiana(f5, f6))
btn10.place(relx=0.25, rely=0.7, anchor='n')
btn11 = Button(f5, command=lambda: ramki_zamiana(f5, f2))
btn11.place(relx=0.75, rely=0.7, anchor='n')
# f6
btn12 = Button(f6, command=lambda: ramki_zamiana(f6, f7))
btn12.place(relx=0.25, rely=0.7, anchor='n')
btn13 = Button(f6, command=lambda: ramki_zamiana(f6, f8))
btn13.place(relx=0.75, rely=0.7, anchor='n')
# f7
btn14 = Button(f7, command=lambda: root01.destroy())
btn14.place(relx=0.25, rely=0.7, anchor='n')
btn15 = Button(f7, command=lambda: ramki_zamiana(f7, f6))
btn15.place(relx=0.75, rely=0.7, anchor='n')
# f8
btn16 = Button(f8, command=lambda: ramki_zamiana(f8, f6))
btn16.place(relx=0.25, rely=0.7, anchor='n')
btn17 = Button(f8, command=lambda: ramki_zamiana(f8, f9))
btn17.place(relx=0.75, rely=0.7, anchor='n')
# f9
btn18 = Button(f9, command=lambda: ramki_zamiana(f9, f11))
btn18.place(relx=0.25, rely=0.7, anchor='n')
btn19 = Button(f9, command=lambda: ramki_zamiana(f9, f10))
btn19.place(relx=0.75, rely=0.7, anchor='n')
# f10
btn20 = Button(f10, command=lambda: ramki_zamiana(f10, f11))
btn20.place(relx=0.25, rely=0.7, anchor='n')
btn21 = Button(f10, command=lambda: root01.destroy())
btn21.place(relx=0.75, rely=0.7, anchor='n')
# f11
btn22 = Button(f11, command=lambda: ramki_zamiana(f11, f13))
btn22.place(relx=0.25, rely=0.7, anchor='n')
btn23 = Button(f11, command=lambda: ramki_zamiana(f11, f12))
btn23.place(relx=0.75, rely=0.7, anchor='n')
# f12
btn24 = Button(f12, command=lambda: ramki_zamiana(f12, f11))
btn24.place(relx=0.25, rely=0.7, anchor='n')
btn25 = Button(f12, command=lambda: ramki_zamiana(f12, f14))
btn25.place(relx=0.75, rely=0.7, anchor='n')
# f13
btn26 = Button(f13, command=lambda: root01.destroy())
btn26.place(relx=0.25, rely=0.7, anchor='n')
btn27 = Button(f13, command=lambda: ramki_zamiana(f13, f11))
btn27.place(relx=0.75, rely=0.7, anchor='n')
# f14
btn28 = Button(f14, command=lambda: ramki_zamiana(f14, f15))
btn28.place(relx=0.25, rely=0.7, anchor='n')
btn29 = Button(f14, command=lambda: ramki_zamiana(f14, f16))
btn29.place(relx=0.75, rely=0.7, anchor='n')
# f15
btn30 = Button(f15, command=lambda: ramki_zamiana(f15, f17))
btn30.place(relx=0.25, rely=0.7, anchor='n')
btn31 = Button(f15, command=lambda: ramki_zamiana(f15, f17))
btn31.place(relx=0.75, rely=0.7, anchor='n')
# f16
btn32 = Button(f16, command=lambda: root01.destroy())
btn32.place(relx=0.25, rely=0.7, anchor='n')
btn33 = Button(f16, command=lambda: ramki_zamiana(f16, f1))
btn33.place(relx=0.75, rely=0.7, anchor='n')
# f17
btn34 = Button(f17, command=lambda: root01.destroy())
btn34.place(relx=0.25, rely=0.7, anchor='n')
btn35 = Button(f17, command=lambda: ramki_zamiana(f17, f16))
btn35.place(relx=0.75, rely=0.7, anchor='n')


def ramki_zamiana(frame1, frame2):
    frame1.place_forget()
    frame2.place(x=0, y=0)


def dzialanie_gui():
    root01.mainloop()
