import GUI
from tkinter import messagebox

# NAPISY
def zm_napisow():
    try:
        f = open('text_01.txt', 'r')
        g = open('text_02.txt', 'r')
        lst_lin = f.readlines()
        n_btn = g.readlines()

        GUI.root01.title(lst_lin[GUI.lin])
        GUI.lbl01.config(text=lst_lin[GUI.lin + 1] + lst_lin[GUI.lin + 2] + lst_lin[GUI.lin + 3])
        GUI.lbl02.config(text=lst_lin[GUI.lin + 4])
        GUI.lbl03.config(text=lst_lin[GUI.lin + 5] + lst_lin[GUI.lin + 6])
        GUI.lbl04.config(text=lst_lin[GUI.lin + 7])
        GUI.lbl05.config(text=lst_lin[GUI.lin + 8])
        GUI.lbl06.config(text=lst_lin[GUI.lin + 9])
        GUI.lbl07.config(text=lst_lin[GUI.lin + 10])
        GUI.lbl08.config(text=lst_lin[GUI.lin + 11])
        GUI.lbl09.config(text=lst_lin[GUI.lin + 12])
        GUI.lbl10.config(text=lst_lin[GUI.lin + 13])
        GUI.lbl11.config(text=lst_lin[GUI.lin + 14] + lst_lin[GUI.lin + 15])
        GUI.lbl12.config(text=lst_lin[GUI.lin + 16])
        GUI.lbl13.config(text=lst_lin[GUI.lin + 17] + lst_lin[GUI.lin + 18])
        GUI.lbl14.config(text=lst_lin[GUI.lin + 19] + lst_lin[GUI.lin + 20])
        GUI.lbl15.config(text=lst_lin[GUI.lin + 21] + lst_lin[GUI.lin + 22] + lst_lin[GUI.lin + 23])
        GUI.lbl16.config(text=lst_lin[GUI.lin + 24] + lst_lin[GUI.lin + 25] + lst_lin[GUI.lin + 26] + lst_lin[GUI.lin + 27] + lst_lin[GUI.lin + 28] + \
                              lst_lin[GUI.lin + 29])
        GUI.lbl17.config(text=lst_lin[GUI.lin + 30] + lst_lin[GUI.lin + 31] + lst_lin[GUI.lin + 32])

        GUI.btn01.config(text=n_btn[GUI.linb])
        GUI.btn02.config(text=n_btn[GUI.linb + 1])
        GUI.btn03.config(text=n_btn[GUI.linb + 2])
        GUI.btn04.config(text=n_btn[GUI.linb + 3])
        GUI.btn05.config(text=n_btn[GUI.linb + 4])
        GUI.btn06.config(text=n_btn[GUI.linb + 5])
        GUI.btn07.config(text=n_btn[GUI.linb + 6])
        GUI.btn08.config(text=n_btn[GUI.linb + 7])
        GUI.btn09.config(text=n_btn[GUI.linb + 8])
        GUI.btn10.config(text=n_btn[GUI.linb + 9])
        GUI.btn11.config(text=n_btn[GUI.linb + 10])
        GUI.btn12.config(text=n_btn[GUI.linb + 11])
        GUI.btn13.config(text=n_btn[GUI.linb + 12])
        GUI.btn14.config(text=n_btn[GUI.linb + 13])
        GUI.btn15.config(text=n_btn[GUI.linb + 14])
        GUI.btn16.config(text=n_btn[GUI.linb + 15])
        GUI.btn17.config(text=n_btn[GUI.linb + 16])
        GUI.btn18.config(text=n_btn[GUI.linb + 17])
        GUI.btn19.config(text=n_btn[GUI.linb + 18])
        GUI.btn20.config(text=n_btn[GUI.linb + 19])
        GUI.btn21.config(text=n_btn[GUI.linb + 20])
        GUI.btn22.config(text=n_btn[GUI.linb + 21])
        GUI.btn23.config(text=n_btn[GUI.linb + 22])
        GUI.btn24.config(text=n_btn[GUI.linb + 23])
        GUI.btn25.config(text=n_btn[GUI.linb + 24])
        GUI.btn26.config(text=n_btn[GUI.linb + 25])
        GUI.btn27.config(text=n_btn[GUI.linb + 26])
        GUI.btn28.config(text=n_btn[GUI.linb + 27])
        GUI.btn29.config(text=n_btn[GUI.linb + 28])
        GUI.btn30.config(text=n_btn[GUI.linb + 29])
        GUI.btn31.config(text=n_btn[GUI.linb + 30])
        GUI.btn32.config(text=n_btn[GUI.linb + 31])
        GUI.btn33.config(text=n_btn[GUI.linb + 32])
        GUI.btn34.config(text=n_btn[GUI.linb + 33])
        GUI.btn35.config(text=n_btn[GUI.linb + 34])
        GUI.btnDonat.config(text=n_btn[GUI.linb + 35])
        GUI.btnCopy.config(text=n_btn[GUI.linb + 36])
    except: messagebox.showinfo("Warning!", "Incorrect input or wrong action.")


def zm_jezyka():

    if GUI.lang == 'PL':
        GUI.lang = 'EN'
        GUI.btnlang.config(text="EN")
        GUI.lin = 34
        GUI.linb = 38
        zm_napisow()
    else:
        GUI.lang = 'PL'
        GUI.btnlang.config(text="PL")
        GUI.lin = 0
        GUI.linb = 0
        zm_napisow()


def copy_clb(window, ethad):
    window.clipboard_clear()
    window.clipboard_append(ethad)
    #main_v2.root01.update()


