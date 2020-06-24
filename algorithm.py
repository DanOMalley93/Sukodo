import random as rd

list_size = 81
x_axis_start = 0
x_axis_end = 9
y_axis_check = 9
index = 0
rd_number = 0
y_check_list_size = list_size // y_axis_check
sudoku_numbers = [] * list_size
y_check_list = [] * y_check_list_size
y_check_list_compare = [] * y_check_list_size


def config_first_row():
    global index, x_axis_start, x_axis_end, rd_number, sudoku_numbers
    while index < x_axis_end:
        rd_number = rd.randrange(1, 10)
        if rd_number not in sudoku_numbers[x_axis_start:x_axis_end]:
            sudoku_numbers.insert(index, rd_number)
            index += 1
    x_axis_start += 9
    x_axis_end += 9


def config_xaxis():
    global index, x_axis_start, x_axis_end, rd_number, sudoku_numbers
    rd_number = rd.randrange(1, 10)
    if rd_number not in sudoku_numbers[x_axis_start:x_axis_end]:
        sudoku_numbers.insert(index, rd_number)
        config_yaxis()


def last_loop_hole():
    global index, sudoku_numbers
    compare_index = index - 44
    i = 0
    increment = 1
    index_check_1 = index - 16
    index_check_2 = index - 14
    if index == 44 or index == 47 or index == 50:
        while i < 3:
            if sudoku_numbers[compare_index+i] not in sudoku_numbers[index_check_1:index_check_2:increment]\
                    and sudoku_numbers[compare_index+i] not in sudoku_numbers[index_check_1+9:index_check_2+9:increment]\
                    and sudoku_numbers[compare_index+i+9] not in sudoku_numbers[index_check_1:index_check_2:increment]\
                    and sudoku_numbers[compare_index+i+9] not in sudoku_numbers[index_check_1+9:index_check_2+9:increment]\
                    and sudoku_numbers[compare_index+i+18] not in sudoku_numbers[index_check_1:index_check_2:increment]\
                    and sudoku_numbers[compare_index+i+18] not in sudoku_numbers[index_check_1+9:index_check_2+9:increment]:
                reset_sudoku_numbers()
            if i == 0:
                index_check_1 -= 1
                increment += 1
            if i == 1:
                index_check_2 -= 1
                increment -= 1
            i += 1


def config_yaxis():
    global index, x_axis_start, x_axis_end, rd_number, sudoku_numbers,\
        y_axis_check, y_check_list_compare, y_check_list_size, y_check_list
    y_check_list = sudoku_numbers[::-y_axis_check]
    if y_check_list == y_check_list_compare:
        del sudoku_numbers[x_axis_start:]
        index = x_axis_start - 1
        rd_number = 0
    y_check_list_compare = y_check_list.copy()
    del y_check_list[0]
    if rd_number in y_check_list:
        del sudoku_numbers[index]
        index += -1
    else:
        config_sudoku_box()
    index += 1


def config_sudoku_box():  # Might be a way to turn this into a loop or shorten the if statements
    global index, rd_number, sudoku_numbers
    if index == 9 or index == 12 or index == 15 or index == 36 or index == 39 \
            or index == 42 or index == 63 or index == 66 or index == 69:
        if rd_number == sudoku_numbers[index-7] or rd_number == sudoku_numbers[index-8]:
            del sudoku_numbers[index]
            index += -1
    if index == 10 or index == 13 or index == 16 or index == 37 or index == 40 \
            or index == 43 or index == 64 or index == 67 or index == 70:
        if rd_number == sudoku_numbers[index-8] or rd_number == sudoku_numbers[index-10]:
            del sudoku_numbers[index]
            index += -1
    if index == 11 or index == 14 or index == 17 or index == 38 or index == 41 \
            or index == 44 or index == 65 or index == 68 or index == 71:
        if rd_number == sudoku_numbers[index-10] or rd_number == sudoku_numbers[index-11]:
            del sudoku_numbers[index]
            index += -1
    if index == 18 or index == 21 or index == 24 or index == 45 or index == 48 \
            or index == 51 or index == 72 or index == 75 or index == 78:
        if rd_number == sudoku_numbers[index-7] or rd_number == sudoku_numbers[index-8] \
                or rd_number == sudoku_numbers[index-16] or rd_number == sudoku_numbers[index-17]:
            del sudoku_numbers[index]
            index += -1
    if index == 19 or index == 22 or index == 25 or index == 46 or index == 49 \
            or index == 52 or index == 73 or index == 76 or index == 79:
        if rd_number == sudoku_numbers[index-8] or rd_number == sudoku_numbers[index-10] \
                or rd_number == sudoku_numbers[index-17] or rd_number == sudoku_numbers[index-19]:
            del sudoku_numbers[index]
            index += -1
    if index == 20 or index == 23 or index == 26 or index == 47 or index == 50 \
            or index == 53 or index == 74 or index == 77 or index == 80:
        if rd_number == sudoku_numbers[index-10] or rd_number == sudoku_numbers[index-11] \
                or rd_number == sudoku_numbers[index-19] or rd_number == sudoku_numbers[index-20]:
            del sudoku_numbers[index]
            index += -1


def print_sudoku_numbers():
    global index, list_size, sudoku_numbers
    index = 9
    while index < list_size:
        print(sudoku_numbers[index])
        index += 1


def reset_sudoku_numbers():
    global index, x_axis_start, x_axis_end, sudoku_numbers, y_check_list, y_check_list_compare, rd_number
    index = 0
    rd_number = 0
    x_axis_start = 0
    x_axis_end = 9
    sudoku_numbers.clear()
    y_check_list.clear()
    y_check_list_compare.clear()
    generate_sudoku_numbers()


def generate_sudoku_numbers():
    global index, x_axis_start, x_axis_end, list_size
    config_first_row()
    while index < list_size:
        while index < x_axis_end:
            config_xaxis()
            last_loop_hole()
            if x_axis_end == 90: # stops x_axis_end from equaling 90 which causes the program to be trap in a loop
                x_axis_end = 81
        x_axis_start += 9
        x_axis_end += 9


generate_sudoku_numbers()
#print_sudoku_numbers()
