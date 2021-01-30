from tkinter import *
from tkinter import messagebox
import random


def bubble_sort(arr_size, rand_choice):  # first algorithm is bubble sort ...
    # array initialization
    arr = []
    maxm_num = -1
    right_entry = False
    if rand_choice:  # means that the user want the elements to be randomly generated
        for i in range(arr_size):  # Random numbers entry...
            arr.append(random.randint(-50, 50))
            if arr[len(arr) - 1] > maxm_num:
                maxm_num = arr[len(arr) - 1]
        right_entry = True  # for validation
    else:  # in case that user want to enter the numbers ...
        numbers_window = Tk()  # the window that allow the user to enter the numbers

        def numbers_ok_btn_comm():  # When ok button is numbers window is pressed
            nonlocal maxm_num, right_entry
            right_entry = True

            def str_to_int(strng):  # a function to convert a string to a number
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
                # str_to_int end

            numbers = numbers_entry.get()
            tmp_str = ""
            loop_sz = len(numbers)
            for char in range(loop_sz):  # a loop to process the entered numbers by the user
                if numbers[char] == ' ' and tmp_str != "":
                    # a case that means a number has been stored in tmp_str variable
                    arr.append(str_to_int(reversed(tmp_str)))
                    tmp_str = ""
                elif numbers[char] == ' ':  # for skipping whitespaces
                    continue
                elif (numbers[char] < '0' or numbers[char] > '9') and numbers[char] != '-':
                    # validation for right numbers entry
                    messagebox.showerror(title="Wrong Entry", message="Wrong numbers !")
                    right_entry = False
                    arr.clear()
                    return
                else:
                    # constructing the tmp_str variable
                    # each number will be separated by two white spaces
                    tmp_str += numbers[char]
                    if char+1 == loop_sz:  # to enter the last number in the entry string
                        arr.append(str_to_int(reversed(tmp_str)))
            # validations area ;
            for numb2 in arr:  # validation loop that checks if numbers in range or not
                if numb2 > 50 or numb2 < -50:
                    messagebox.showerror(title="Out of range",
                                         message="You entered a number that exceeds the range [-50,50]")
                    arr.clear()
                    right_entry = False
                    return
            if len(arr) == arr_size:  # Right entry
                numbers_window.destroy()
            elif len(arr) > arr_size:  # More elements than the specified size
                if len(arr)-arr_size == 1:
                    messagebox.showerror(title="unmatched sizes", message=f'you did not enter {arr_size} elements!!\n'
                                                                          f'Delete {len(arr)-arr_size} element...')
                else:
                    messagebox.showerror(title="unmatched sizes", message=f'you did not enter {arr_size} elements!!\n'
                                                                          f'Delete {len(arr) - arr_size} elements...')
                arr.clear()
                right_entry = False
            else:   # less elements than the the specified size
                if arr_size-len(arr) == 1:
                    messagebox.showerror(title="unmatched sizes", message=f'you did not enter {arr_size} elements!!\n'
                                                                          f'Add {arr_size-len(arr)} element...')
                else:
                    messagebox.showerror(title="unmatched sizes", message=f'you did not enter {arr_size} elements!!\n'
                                                                          f'Add {arr_size-len(arr)} elements...')
                arr.clear()
                right_entry = False
        # data elements settings in numbers entry window ;
        btn_entry_frm = Frame()
        txt_enter_lbl = Label(text=f"Enter {arr_size} numbers separated by spaces [-50, 50]", font=("bold", 13))
        txt_enter_lbl.grid(row=0, column=0, padx=5, pady=5)
        numbers_entry = Entry(master=btn_entry_frm, width=20)
        numbers_entry.grid(row=1, column=0)
        numbers_ok_btn = Button(master=btn_entry_frm, text="OK", command=numbers_ok_btn_comm)
        numbers_ok_btn.grid(row=1, column=1, padx=10)
        btn_entry_frm.grid(row=1, column=0)

        numbers_window.mainloop()
        for numb in arr:
            if numb > maxm_num:
                maxm_num = numb
        if not right_entry:  # Check if the entry is accepted
            return  # return from numbers_ok_btn_comm function
    # The end of the "else" statement that allows the user to enter the array numbers...

    if right_entry:
        main_window = Tk()
        lop1 = 0
        lop2 = lop1 + 1
        is_sorted = False
        cur_op = 1

        def swap_lbls(element1, element2):  # a function to swap 2 labels :)
            if int(element1['text']) < int(element2['text']):
                op_lbl["text"] = f"{element1['text']} swapped with {element2['text']}"
                return element2['text'], element1['text'], element2['width'], element1['width'], element2['bg'], \
                    element1['bg'], element2['fg'], element1['fg']
            op_lbl["text"] = "No swap happened"
            return element1['text'], element2['text'], element1['width'], element2['width'], element1['bg'],\
                element2['bg'], element1['fg'], element2['fg']

        def one_op():  # when next button is pressed >>
            nonlocal lop1, lop2, is_sorted, cur_op
            if is_sorted:
                for k in range(arr_size-1):  # sorting checking
                    if int(arr_lbl[k]['text']) <= int(arr_lbl[k+1]['text']):
                        is_sorted = True
                    else:
                        is_sorted = False
                        break
                if is_sorted:
                    messagebox.showinfo("Yay :d", "The array is sorted !")
                    return

            if cur_op == 1:  # comparing operation
                if lop1 < arr_size and lop2 < arr_size:  # to check if it's compare or compare check
                    compr_statmnt_lbl["text"] = f"{arr_lbl[lop1]['text']} is compared with {arr_lbl[lop2]['text']}"
                    op_lbl['text'] = "Comparing operation"
                else:
                    op_lbl['text'] = "Compare Check operation"
                    if lop1 >= arr_size-1 and lop2 >= arr_size-1:
                        is_sorted = True
                cur_op = 0

            else:  # swap operation
                if lop1 < arr_size:
                    if lop2 < arr_size:
                        arr_lbl[lop2]['text'], arr_lbl[lop1]['text'], arr_lbl[lop2]['width'], arr_lbl[lop1]['width'], \
                            arr_lbl[lop2]['bg'], arr_lbl[lop1]['bg'], arr_lbl[lop2]['fg'], arr_lbl[lop1]['fg'] =\
                            swap_lbls(arr_lbl[lop2], arr_lbl[lop1])
                        lop2 += 1
                    else:  # loop check operation
                        op_lbl["text"] = "Loop Check operation"
                        lop1 += 1
                        lop2 = lop1 + 1
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
                arr_lbl.append(Label(text=str(arr[i]), width=(-1*arr[i]), bg='red'))
            else:
                arr_lbl.append(Label(text=str(arr[i]), width=(-1 * arr[i]), bg='white', fg="black"))
        for i in range(arr_size):
            arr_lbl[i].grid(row=i, column=0, pady=1)
        btn_1 = Button(text="Next", command=one_op)
        btn_1.grid(row=arr_size+2, column=0, sticky="nwse")
        op_lbl = Label(text='No Operation ...')
        op_lbl.grid(row=arr_size+1, column=0)
        compr_statmnt_lbl = Label(text='1st element is compared with 2nd element')
        compr_statmnt_lbl.grid(row=arr_size, column=0)
        main_window.columnconfigure(0, minsize=maxm_num)
        main_window.resizable(False, False)
        main_window.mainloop()
