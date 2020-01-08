import main_v2
from tkinter import messagebox

#t00 = "Kilka pytań o Świat"


# NAPISY
def zm_napisow():
    try:
        f = open('text_01.txt', 'r')
        g = open('text_02.txt', 'r')
        lst_lin = f.readlines()
        n_btn = g.readlines()

        main_v2.root01.title(lst_lin[main_v2.lin])
        main_v2.lbl01.config(text=lst_lin[main_v2.lin + 1] + lst_lin[main_v2.lin + 2] + lst_lin[main_v2.lin + 3])
        main_v2.lbl02.config(text=lst_lin[main_v2.lin + 4])
        main_v2.lbl03.config(text=lst_lin[main_v2.lin + 5] + lst_lin[main_v2.lin + 6])
        main_v2.lbl04.config(text=lst_lin[main_v2.lin + 7])
        main_v2.lbl05.config(text=lst_lin[main_v2.lin + 8])
        main_v2.lbl06.config(text=lst_lin[main_v2.lin + 9])
        main_v2.lbl07.config(text=lst_lin[main_v2.lin + 10])
        main_v2.lbl08.config(text=lst_lin[main_v2.lin + 11])
        main_v2.lbl09.config(text=lst_lin[main_v2.lin + 12])
        main_v2.lbl10.config(text=lst_lin[main_v2.lin + 13])
        main_v2.lbl11.config(text=lst_lin[main_v2.lin + 14] + lst_lin[main_v2.lin + 15])
        main_v2.lbl12.config(text=lst_lin[main_v2.lin + 16])
        main_v2.lbl13.config(text=lst_lin[main_v2.lin + 17] + lst_lin[main_v2.lin + 18])
        main_v2.lbl14.config(text=lst_lin[main_v2.lin + 19] + lst_lin[main_v2.lin + 20])
        main_v2.lbl15.config(text=lst_lin[main_v2.lin + 21] + lst_lin[main_v2.lin + 22] + lst_lin[main_v2.lin + 23])
        main_v2.lbl16.config(text=lst_lin[main_v2.lin + 24] + lst_lin[main_v2.lin + 25] + lst_lin[main_v2.lin + 26] + lst_lin[main_v2.lin + 27] + lst_lin[main_v2.lin + 28] + \
              lst_lin[main_v2.lin + 29])
        main_v2.lbl17.config(text=lst_lin[main_v2.lin + 30] + lst_lin[main_v2.lin + 31] + lst_lin[main_v2.lin + 32])

        main_v2.btn01.config(text=n_btn[main_v2.linb])
        main_v2.btn02.config(text=n_btn[main_v2.linb + 1])
        main_v2.btn03.config(text=n_btn[main_v2.linb + 2])
        main_v2.btn04.config(text=n_btn[main_v2.linb + 3])
        main_v2.btn05.config(text=n_btn[main_v2.linb + 4])
        main_v2.btn06.config(text=n_btn[main_v2.linb + 5])
        main_v2.btn07.config(text=n_btn[main_v2.linb + 6])
        main_v2.btn08.config(text=n_btn[main_v2.linb + 7])
        main_v2.btn09.config(text=n_btn[main_v2.linb + 8])
        main_v2.btn10.config(text=n_btn[main_v2.linb + 9])
        main_v2.btn11.config(text=n_btn[main_v2.linb + 10])
        main_v2.btn12.config(text=n_btn[main_v2.linb + 11])
        main_v2.btn13.config(text=n_btn[main_v2.linb + 12])
        main_v2.btn14.config(text=n_btn[main_v2.linb + 13])
        main_v2.btn15.config(text=n_btn[main_v2.linb + 14])
        main_v2.btn16.config(text=n_btn[main_v2.linb + 15])
        main_v2.btn17.config(text=n_btn[main_v2.linb + 16])
        main_v2.btn18.config(text=n_btn[main_v2.linb + 17])
        main_v2.btn19.config(text=n_btn[main_v2.linb + 18])
        main_v2.btn20.config(text=n_btn[main_v2.linb + 19])
        main_v2.btn21.config(text=n_btn[main_v2.linb + 20])
        main_v2.btn22.config(text=n_btn[main_v2.linb + 21])
        main_v2.btn23.config(text=n_btn[main_v2.linb + 22])
        main_v2.btn24.config(text=n_btn[main_v2.linb + 23])
        main_v2.btn25.config(text=n_btn[main_v2.linb + 24])
        main_v2.btn26.config(text=n_btn[main_v2.linb + 25])
        main_v2.btn27.config(text=n_btn[main_v2.linb + 26])
        main_v2.btn28.config(text=n_btn[main_v2.linb + 27])
        main_v2.btn29.config(text=n_btn[main_v2.linb + 28])
        main_v2.btn30.config(text=n_btn[main_v2.linb + 29])
        main_v2.btn31.config(text=n_btn[main_v2.linb + 30])
        main_v2.btn32.config(text=n_btn[main_v2.linb + 31])
        main_v2.btn33.config(text=n_btn[main_v2.linb + 32])
        main_v2.btn34.config(text=n_btn[main_v2.linb + 33])
        main_v2.btn35.config(text=n_btn[main_v2.linb + 34])
        main_v2.btnDonat.config(text=n_btn[main_v2.linb + 35])
        main_v2.btnCopy.config(text=n_btn[main_v2.linb + 36])
    except: messagebox.showinfo("Błąd", "Złe dane lub niepoprawna akcja.")


def zm_jezyka():

    if main_v2.lang == 'PL':
        main_v2.lang = 'EN'
        main_v2.btnlang.config(text="EN")
        main_v2.lin = 34
        main_v2.linb = 38
        zm_napisow()
    else:
        main_v2.lang = 'PL'
        main_v2.btnlang.config(text="PL")
        main_v2.lin = 0
        main_v2.linb = 0
        zm_napisow()


def copy_clb():
    main_v2.root01.clipboard_clear()
    main_v2.root01.clipboard_append(main_v2.eth)
    #main_v2.root01.update()


