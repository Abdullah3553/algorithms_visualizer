from tkinter import *
from tkinter import messagebox
import random
import bubble_sort
import selection_sort


def element_enter(arr_size, rand_choice, choosen_algo):  # first algorithm is bubble sort ...
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
        if choosen_algo == "bubble_sort":
            bubble_sort.main(arr, maxm_num)
        elif choosen_algo == 'selection_sort':
            selection_sort.main(arr, maxm_num)
