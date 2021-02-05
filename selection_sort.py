from tkinter import *
from tkinter import messagebox
import shared_functions


def main(arr, maxm_num):
    main_window = Tk()
    lop1 = 0
    lop2 = 1
    is_sorted = False
    cur_op = 1
    text = True

    def swap_lbls(element1, element2):  # a function to swap 2 labels :)
        return element2['text'], element1['text'], element2['width'], element1['width'], element2['bg'], \
            element1['bg'], element2['fg'], element1['fg']

    def one_op():  # when next button is pressed >>
        nonlocal lop1, lop2, minm, cur_op, text, is_sorted
        if is_sorted:
            messagebox.showinfo("Yay :d", "The array is sorted !")
            return
        if text:
            if cur_op == 1 and lop2 < arr_size:
                if op_lbl['text'] != "Finding Minimum":
                    op_lbl['text'] = "Finding Minimum"
                compr_statmnt_lbl['text'] = f"Comparing {arr_lbl[lop2]['text']} with {arr_lbl[minm]['text']}"
                if lop2 + 1 == arr_size:
                    cur_op = 2
            elif cur_op == 2:
                op_lbl['text'] = f"Swapping Current Minimum({arr_lbl[minm]['text']}) with {arr_lbl[lop1]['text']}" \
                                 f" in index {lop1}"
            text = False
        else:
            if lop1 < arr_size:
                if lop2 < arr_size:
                    if int(arr_lbl[lop2]['text']) < int(arr_lbl[minm]['text']):
                        minm = lop2
                        cur_min_lbl['text'] = f"Current Minimum is {arr_lbl[minm]['text']} at index {minm}"
                        op_lbl['text'] = "Minimum has been Updated"
                    else:
                        op_lbl['text'] = "Minimum Remains the same"
                    lop2 += 1
                    text = True
                    return
                else:
                    arr_lbl[lop1]['text'], arr_lbl[minm]['text'], \
                     arr_lbl[lop1]['width'], arr_lbl[minm]['width'], \
                     arr_lbl[lop1]['bg'], arr_lbl[minm]['bg'], \
                     arr_lbl[lop1]['fg'], arr_lbl[minm]['fg'] = swap_lbls(arr_lbl[lop1], arr_lbl[minm])
                    arr_lbl[lop1] = shared_functions.sorted_color_handle(arr_lbl[lop1])
                    lop1 += 1
                    lop2 = lop1 + 1
                    minm = lop1
                    cur_op = 1
                    if minm >= arr_size:
                        is_sorted = True
                        return
                    cur_min_lbl['text'] = f"Current Minimum is {arr_lbl[minm]['text']} at index {minm}"
            text = True

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
    btn_1.grid(row=arr_size + 3, column=0, sticky="nwse")
    op_lbl = Label(text='No Operation ...')
    op_lbl.grid(row=arr_size + 1, column=0)
    compr_statmnt_lbl = Label(text='1st element is compared with 2nd element')
    compr_statmnt_lbl.grid(row=arr_size, column=0)
    cur_min_lbl = Label(text=f"Current Minimum is {arr_lbl[minm]['text']} at index {minm}", borderwidth=2,
                        relief=RAISED)
    cur_min_lbl.grid(row=arr_size + 2, column=0)
    main_window.columnconfigure(0, minsize=maxm_num)
    main_window.resizable(False, False)
    main_window.mainloop()
