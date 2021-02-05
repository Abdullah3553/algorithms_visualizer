def sorted_color_handle(arr_lbl):
    if int(arr_lbl['text']) < 0:
        arr_lbl['bg'] = '#4c035e'
        arr_lbl['fg'] = "White"
    elif int(arr_lbl['text']) > 0:
        arr_lbl['bg'] = '#ad06d6'
        arr_lbl['fg'] = "White"
    else:
        arr_lbl['bg'] = '#ad63bf'
        arr_lbl['fg'] = "Black"
    return arr_lbl

