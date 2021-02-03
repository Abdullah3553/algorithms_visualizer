from tkinter import *
from tkinter import messagebox


def main(arr, maxm_num):
    main_window = Tk()
    lop1 = 0
    lop2 = 0
    # is_sorted = False
    # cur_op = 1

    def swap_lbls(element1, element2):  # a function to swap 2 labels :)
        return element2['text'], element1['text'], element2['width'], element1['width'], element2['bg'], \
            element1['bg'], element2['fg'], element1['fg']

    def one_op():  # when next button is pressed >>
        nonlocal lop1, lop2, minm  # , is_sorted, cur_op
        print("pressed")
        if lop1 < arr_size:
            print(f"lop1 {lop1}")
            if lop2 < arr_size:
                print(f"lop2 {lop2}, minimum {minm}")
                if int(arr_lbl[lop2]['text']) < int(arr_lbl[minm]['text']):
                    minm = lop2
                    print(f"minimum is {minm}")
                lop2 += 1
                return
            else:
                arr_lbl[lop1]['text'], arr_lbl[minm]['text'], \
                 arr_lbl[lop1]['width'], arr_lbl[minm]['width'], \
                 arr_lbl[lop1]['bg'], arr_lbl[minm]['bg'], \
                 arr_lbl[lop1]['fg'], arr_lbl[minm]['fg'] = swap_lbls(arr_lbl[lop1], arr_lbl[minm])
                lop1 += 1
                lop2 = lop1
                minm = lop1
        else:
            pass

    #  data elements of the main window settings ;
    arr_lbl = []
    arr_size = len(arr)
    for i in range(arr_size):
        if arr[i] > 0:
            arr_lbl.append(Label(text=str(arr[i]), width=arr[i], bg='green'))
        elif arr[i] < 0:
            arr_lbl.append(Label(text=str(arr[i]), width=(-1 * arr[i]), bg='red'))
        else:
            arr_lbl.append(Label(text=str(arr[i]), width=(-1 * arr[i]), bg='white', fg="black"))
    minm = lop1
    for i in range(arr_size):
        arr_lbl[i].grid(row=i, column=0, pady=1)
    btn_1 = Button(text="Next", command=one_op)
    btn_1.grid(row=arr_size + 2, column=0, sticky="nwse")
    op_lbl = Label(text='No Operation ...')
    op_lbl.grid(row=arr_size + 1, column=0)
    compr_statmnt_lbl = Label(text='1st element is compared with 2nd element')
    compr_statmnt_lbl.grid(row=arr_size, column=0)
    main_window.columnconfigure(0, minsize=maxm_num)
    main_window.resizable(False, False)
    main_window.mainloop()
