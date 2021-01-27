from tkinter import *

# Initializations ;
start_window = Tk()
hola_lbl_frm = Frame(master=start_window, borderwidth=2, relief=SUNKEN)
hola_lbl = Label(master=hola_lbl_frm, text="~<< Welcome to Algorithms Visualizer >>~", font=("bold", 16))
choose_lbl = Label(text="Choose the algorithm you want to Visualize")
choosen_algo_val = StringVar()
algo_rdio_frm = Frame(master=start_window)
bbl_sort_rdio = Radiobutton(master=algo_rdio_frm, text="Bubble Sort", variable=choosen_algo_val, value="bbl_sort"
                            , selectcolor="grey")


def ok_btn_comm():
    print(choosen_algo_val.get())


hola_lbl_frm.grid(row=0, column=2, padx=10, pady=10)
hola_lbl.grid(row=0, column=2, sticky="nesw")
choose_lbl.grid(row=1, column=2)
choosen_algo_val.set("none")
algo_rdio_frm.grid(row=2, column=2)
bbl_sort_rdio.grid(row=2, column=1)
# bbl_sort_rdio2 = Radiobutton(master=algo_rdio_frm, text="None", variable=choosen_algo_val, value="none"
#                              , selectcolor="grey")
# bbl_sort_rdio2.grid(row=2, column=0)
ok_btn = Button(text='OK', command=ok_btn_comm)
ok_btn.grid(row=3, column=2)


start_window.mainloop()
