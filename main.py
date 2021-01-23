from tkinter import *
import random


main_window = Tk()
lop1 = 0
lop2 = lop1 + 1
is_sorted = False
cont = 0


def comp_check(element1, element2):
    if int(element1['text']) < int(element2['text']):
        return element2['text'], element1['text'], element2['width'], element1['width']
    return element1['text'], element2['text'], element1['width'], element2['width']


def one_op():
    global lop1, lop2, is_sorted, cont
    cont += 1
    if lop1 < arr_size:
        if lop2 < arr_size:
            arr_lbl[lop2]['text'], arr_lbl[lop1]['text'], arr_lbl[lop2]['width'], arr_lbl[lop1]['width'] =\
                comp_check(arr_lbl[lop2], arr_lbl[lop1])
            lop2 += 1
        else:
            lop1 += 1
            lop2 = lop1 + 1
    else:
        for k in arr_lbl:
            print(k['text'])
        is_sorted = True
    if lop2 == arr_size-1:
        arr_lbl[lop2]['text'], arr_lbl[lop1]['text'], arr_lbl[lop2]['width'], arr_lbl[lop1]['width'] = \
            comp_check(arr_lbl[lop2], arr_lbl[lop1])
        lop1 += 1
        lop2 = lop1 +1
    if lop1 == arr_size-1 and lop2 == arr_size-1:
        arr_lbl[lop2]['text'], arr_lbl[lop1]['text'], arr_lbl[lop2]['width'], arr_lbl[lop1]['width'] = \
            comp_check(arr_lbl[lop2], arr_lbl[lop1])
        for k in arr_lbl:
            print(k['text'])
        is_sorted = True
    if is_sorted:
        print("sorted")
        print(cont)


# array initialization
arr = []
arr_size = int(input("Enter the size of the array : "))
for i in range(arr_size):
    arr.append(random.randint(0, arr_size*10))
    # arr.append(int(input("> ")))

#  Labels initialization and printing
arr_lbl = []
for i in range(len(arr)):
    arr_lbl.append(Label(text=str(arr[i]), width=arr[i], bg='blue'))
for i in range(len(arr_lbl)):
    arr_lbl[i].grid(row=i, column=0)
btn_1 = Button(text="Next", command=one_op)
btn_1.grid(row=10, column=10)
main_window.geometry("600x600")
main_window.mainloop()
