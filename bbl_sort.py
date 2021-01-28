from tkinter import *
from tkinter import messagebox
import random


def main(arr_size, rand_choice):
    # array initialization
    arr = []
    maxm_num = -1
    if rand_choice:
        for i in range(arr_size):
            arr.append(random.randint(0, 50))
            if arr[len(arr) - 1] > maxm_num:
                maxm_num = arr[len(arr) - 1]
    else:
        numbers_window = Tk()

        def numbers_ok_btn_comm():

            def str_to_int(strng):
                num = 0
                tens = 1
                negative_num = False
                for strng_char in strng:
                    if strng_char != '-':
                        num += (int(strng_char)*tens)
                        tens *= 10
                    else:
                        negative_num = True
                if negative_num:
                    num *= -1
                return num

            numbers = numbers_entry.get()
            tmp_str = ""
            loop_sz = len(numbers)
            for char in range(loop_sz):
                if numbers[char] == ' ' and tmp_str != "":
                    arr.append(str_to_int(reversed(tmp_str)))
                    tmp_str = ""
                elif (numbers[char] < '0' or numbers[char] > '9') and numbers[char] != '-':
                    messagebox.showerror(title="Wrong Entry", message="Wrong numbers !")
                else:
                    tmp_str += numbers[char]
                    # print("Else worked")
                    if char+1 == loop_sz:
                        # print("if inside else worked")
                        arr.append(str_to_int(reversed(tmp_str)))
            numbers_window.destroy()

        btn_entry_frm = Frame()
        txt_enter_lbl = Label(text=f"Enter {arr_size} numbers separated by spaces ", font=("bold", 13))
        txt_enter_lbl.grid(row=0, column=0, padx=5, pady=5)
        numbers_entry = Entry(master=btn_entry_frm, width=20)
        numbers_entry.grid(row=1, column=0)
        numbers_ok_btn = Button(master=btn_entry_frm, text="OK", command=numbers_ok_btn_comm)
        numbers_ok_btn.grid(row=1, column=1, padx=10)
        btn_entry_frm.grid(row=1, column=0)

        numbers_window.mainloop()
        for i in range(arr_size):
            pass

    main_window = Tk()
    lop1 = 0
    lop2 = lop1 + 1
    is_sorted = False
    cur_op = 1

    def comp_check(element1, element2):
        if int(element1['text']) < int(element2['text']):
            op_lbl["text"] = f"{element1['text']} swapped with {element2['text']}"
            return element2['text'], element1['text'], element2['width'], element1['width']
        op_lbl["text"] = "No swap happened"
        return element1['text'], element2['text'], element1['width'], element2['width']

    def one_op():
        nonlocal lop1, lop2, is_sorted, cur_op
        if is_sorted:
            for k in range(arr_size-1):
                if int(arr_lbl[k]['text']) <= int(arr_lbl[k+1]['text']):
                    is_sorted = True
                else:
                    is_sorted = False
                    break
            if is_sorted:
                messagebox.showinfo("Yay :d", "The array is sorted !")
                return

        if cur_op == 1:
            if lop1 < arr_size and lop2 < arr_size:
                compr_statmnt_lbl["text"] = f"{arr_lbl[lop1]['text']} is compared with {arr_lbl[lop2]['text']}"
                op_lbl['text'] = "Comparing operation"
            else:
                op_lbl['text'] = "Compare Check operation"
                if lop1 >= arr_size-1 and lop2 >= arr_size-1:
                    is_sorted = True
            cur_op = 0

        else:
            if lop1 < arr_size:
                if lop2 < arr_size:
                    arr_lbl[lop2]['text'], arr_lbl[lop1]['text'], arr_lbl[lop2]['width'], arr_lbl[lop1]['width'] =\
                        comp_check(arr_lbl[lop2], arr_lbl[lop1])
                    lop2 += 1
                else:
                    op_lbl["text"] = "Loop Check operation"
                    lop1 += 1
                    lop2 = lop1 + 1
            else:
                is_sorted = True
            cur_op = 1

    #  Labels initialization and printing
    arr_lbl = []
    for i in range(arr_size):
        arr_lbl.append(Label(text=str(arr[i]), width=abs(arr[i]), bg='blue'))
    for i in range(arr_size):
        arr_lbl[i].grid(row=i, column=0, pady=1)
    btn_1 = Button(text="Next", command=one_op)
    btn_1.grid(row=arr_size+2, column=0, sticky="nwse")
    op_lbl = Label(text='No Operation ...')
    op_lbl.grid(row=arr_size+1, column=0)
    compr_statmnt_lbl = Label(text='1st element is compared with 2nd element')
    compr_statmnt_lbl.grid(row=arr_size, column=0)
    main_window.columnconfigure(0, minsize=maxm_num)
    main_window.mainloop()
