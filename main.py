from tkinter import *
from tkinter import messagebox
import implemented_algorithms

# Initializations ;
start_window = Tk()
hola_lbl_frm = Frame(master=start_window, borderwidth=2, relief=SUNKEN)
hola_lbl = Label(master=hola_lbl_frm, text="~<< Welcome to Algorithms Visualizer >>~", font=("bold", 16))
choose_lbl = Label(text="Choose the algorithm you want to Visualize")
choosen_algo_val = StringVar()
algo_rdio_frm = Frame(master=start_window)
bbl_sort_rdio = Radiobutton(master=algo_rdio_frm, text="Bubble Sort", variable=choosen_algo_val, value="bubble_sort"
                            , selectcolor="grey")


def ok_btn_comm():  # when ok button is pressed in the start window
    if choosen_algo_val.get() != "none":  # validation if nothing is selected
        # Initializations ;
        size_enter_window = Toplevel()
        rand_choice = BooleanVar(master=size_enter_window)
        array_sz = IntVar(master=size_enter_window)
        size_entry_frm = Frame(master=size_enter_window, borderwidth=1)
        size_entry = Entry(master=size_entry_frm, width=5, textvariable=array_sz)
        size_entry_lbl = Label(master=size_entry_frm, text="Enter the array size (20 is maximum)")
        rand_choice_chk = Checkbutton(master=size_enter_window, text="Random Array", onvalue=True, offvalue=False
                                      , variable=rand_choice, selectcolor="grey")

        def choosen_ok_btn_comm():  # when ok button is pressed in size enter window
            try:
                nonlocal array_sz, rand_choice
                if int(array_sz.get()) > 0:  # validation for range of the size
                    if int(array_sz.get()) > 20:  # validation for range of the size
                        messagebox.showerror(title="size exceeded", message="20 is the maximum size !")
                    else:  # The entered size is right and the algorithms is ready to be called
                        rand_choice = bool(rand_choice.get())  # random or not
                        array_sz = int(array_sz.get())         # array size
                        size_enter_window.destroy()            # close size enter window
                        start_window.destroy()                 # close start window
                        # call the selected algorithm
                        if choosen_algo_val.get() == "bubble_sort":
                            implemented_algorithms.bubble_sort(array_sz, rand_choice)
                else:
                    messagebox.showerror(master=size_enter_window, title="Wrong Entry"
                                         , message="Negative or zero size entered")
            except TclError:
                messagebox.showerror(master=size_enter_window, title="Wrong Entry", message="Wrong size entered !")

        # Data elements settings for size enter window;
        rand_choice.set(True)
        choosen_ok_btn = Button(master=size_enter_window, text="OK", command=choosen_ok_btn_comm, width=10)
        size_entry_frm.grid(row=1, column=1, padx=5, pady=5)
        size_entry_lbl.grid(row=1, column=0, padx=5)
        size_entry.grid(row=1, column=1)
        rand_choice_chk.grid(row=1, column=2)
        choosen_ok_btn.grid(row=2, column=2)
        size_enter_window.mainloop()
    else:
        messagebox.showerror(title="Wrong entry", message="You did not choose anything !")


# Data elements settings for start window ;
hola_lbl_frm.grid(row=0, column=2, padx=10, pady=10)
hola_lbl.grid(row=0, column=2, sticky="nesw")
choose_lbl.grid(row=1, column=2)
choosen_algo_val.set("none")
algo_rdio_frm.grid(row=2, column=2)
bbl_sort_rdio.grid(row=2, column=1)
ok_btn = Button(text='OK', command=ok_btn_comm)
ok_btn.grid(row=3, column=2)
start_window.mainloop()


