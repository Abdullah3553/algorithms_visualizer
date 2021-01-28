from tkinter import *
from tkinter import messagebox
import bbl_sort

# Initializations ;
start_window = Tk()
hola_lbl_frm = Frame(master=start_window, borderwidth=2, relief=SUNKEN)
hola_lbl = Label(master=hola_lbl_frm, text="~<< Welcome to Algorithms Visualizer >>~", font=("bold", 16))
choose_lbl = Label(text="Choose the algorithm you want to Visualize")
choosen_algo_val = StringVar()
algo_rdio_frm = Frame(master=start_window)
bbl_sort_rdio = Radiobutton(master=algo_rdio_frm, text="Bubble Sort", variable=choosen_algo_val, value="bbl_sort"
                            , selectcolor="grey")
# bbl_sort_rdio2 = Radiobutton(master=algo_rdio_frm, text="None", variable=choosen_algo_val, value="none"
#                              , selectcolor="grey")
array_sz = 0
rand_choice = ""


def ok_btn_comm():
    if choosen_algo_val.get() != "none":
        size_enter_window = Tk()
        rand_choice_in = BooleanVar(master=size_enter_window)
        array_sz_in = IntVar(master=size_enter_window)
        size_entry_frm = Frame(master=size_enter_window, borderwidth=1)
        size_entry = Entry(master=size_entry_frm, width=5, textvariable=array_sz_in)
        size_entry_lbl = Label(master=size_entry_frm, text="Enter the array size")

        def choosen_ok_btn_comm():
            try:
                global array_sz, rand_choice
                rand_choice = bool(rand_choice_in.get())
                array_sz = int(array_sz_in.get())
                size_enter_window.destroy()
                start_window.destroy()
                bbl_sort.main(array_sz, rand_choice)
            except ValueError:
                messagebox.showerror(master=size_enter_window, title="Wrong Entry", message="Wrong size entered !")

        rand_choice_chk = Checkbutton(master=size_enter_window, text="Random Array", onvalue=True, offvalue=False
                                      , variable=rand_choice_in, selectcolor="grey")
        choosen_ok_btn = Button(master=size_enter_window, text="OK", command=choosen_ok_btn_comm, width=10)
        size_entry_frm.grid(row=1, column=1, padx=5, pady=5)
        size_entry_lbl.grid(row=1, column=0, padx=5)
        size_entry.grid(row=1, column=1)
        rand_choice_chk.grid(row=1, column=2)
        choosen_ok_btn.grid(row=2, column=2)
        size_enter_window.mainloop()
    else:
        messagebox.showerror(title="Wrong entry", message="You did not choose anything !")


# setting Variables ;
hola_lbl_frm.grid(row=0, column=2, padx=10, pady=10)
hola_lbl.grid(row=0, column=2, sticky="nesw")
choose_lbl.grid(row=1, column=2)
choosen_algo_val.set("none")
algo_rdio_frm.grid(row=2, column=2)
bbl_sort_rdio.grid(row=2, column=1)
# bbl_sort_rdio2.grid(row=2, column=0)
ok_btn = Button(text='OK', command=ok_btn_comm)
ok_btn.grid(row=3, column=2)


start_window.mainloop()


