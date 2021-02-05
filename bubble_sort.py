from tkinter import *
from tkinter import messagebox
import shared_functions


def main(arr, maxm_num):
    main_window = Tk()
    lop1 = 0
    lop2 = 0
    is_sorted = False
    cur_op = 1

    def swap_lbls(element1, element2):  # a function to swap 2 labels :)
        if int(element1['text']) < int(element2['text']):
            op_lbl["text"] = f"{element1['text']} swapped with {element2['text']}"
            return element2['text'], element1['text'], element2['width'], element1['width'], element2['bg'], \
                element1['bg'], element2['fg'], element1['fg']
        op_lbl["text"] = "No swap happened"
        return element1['text'], element2['text'], element1['width'], element2['width'], element1['bg'], \
            element2['bg'], element1['fg'], element2['fg']

    def one_op():  # when next button is pressed >>
        nonlocal lop1, lop2, is_sorted, cur_op
        # if is_sorted:
        #     for k in range(arr_size - 1):  # sorting checking
        #         if int(arr_lbl[k]['text']) <= int(arr_lbl[k + 1]['text']):
        #             is_sorted = True
        #         else:
        #             is_sorted = False
        #             break
        if is_sorted:
            if int(arr_lbl[0]['text']) < 0:
                arr_lbl[0]['bg'] = '#4c035e'
                arr_lbl[0]['fg'] = "White"
            elif int(arr_lbl[0]['text']) > 0:
                arr_lbl[0]['bg'] = '#ad06d6'
                arr_lbl[0]['fg'] = "White"
            else:
                arr_lbl[0]['bg'] = '#ad63bf'
                arr_lbl[0]['fg'] = "Black"
            messagebox.showinfo("Yay :d", "The array is sorted !")
            return

        if cur_op == 1:  # comparing operation
            if lop1 < arr_size and lop2 < arr_size - 1 - lop1:  # to check if it's compare or compare check
                compr_statmnt_lbl["text"] = f"{arr_lbl[lop2]['text']} is compared with {arr_lbl[lop2 + 1]['text']}"
                op_lbl['text'] = "Comparing operation"
            else:
                op_lbl['text'] = "Compare Check operation"
                if lop1 >= arr_size - 1 and lop2 >= arr_size - 1 - lop1:
                    is_sorted = True
            cur_op = 0

        else:  # swap operation
            if lop1 < arr_size:
                if lop2 < arr_size - 1 - lop1:
                    arr_lbl[lop2 + 1]['text'], arr_lbl[lop2]['text'],\
                     arr_lbl[lop2 + 1]['width'], arr_lbl[lop2]['width'],\
                     arr_lbl[lop2 + 1]['bg'], arr_lbl[lop2]['bg'],\
                     arr_lbl[lop2 + 1]['fg'], arr_lbl[lop2]['fg'] = swap_lbls(arr_lbl[lop2 + 1], arr_lbl[lop2])
                    lop2 += 1
                else:  # loop check operation
                    op_lbl["text"] = "Loop Check operation"
                    arr_lbl[lop2] = shared_functions.sorted_color_handle(arr_lbl[lop2])
                    lop1 += 1
                    lop2 = 0

            else:
                is_sorted = True
            cur_op = 1

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
