import random as rd
import tkinter as tk
import algorithm as al

root = tk.Tk()
player_progress = [] * al.list_size
difficulty_setting = tk.StringVar(root)
difficulty_setting.set(4)


def reset_game(delete_player_progress):
    for i in range(0, al.list_size):
        delete_entry = delete_player_progress[i]
        delete_entry.delete(0)


def new_game():
    global player_progress, new_game_button
    new_game_button.config(state='disable')
    delete_entries()
    select_difficulty()
    al.reset_sudoku_numbers()
    enter_numbers()


def get_entry_values(update_values):
    entry_values = [] * al.list_size
    for index in range(0, al.list_size):
        entry_values.insert(index, update_values[index].get())
    return entry_values


def create_new_window():
    new_window = tk.Toplevel(root, background='blue')
    you_win_label = tk.Label(new_window, text="You Win!", background='blue', foreground='gold', font="Calibri 30")
    you_win_label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)


def create_you_lose():
    new_window_lose = tk.Toplevel(root, background='red')
    you_lose_label = tk.Label(new_window_lose, text="Incorrect", background='red', foreground='gold', font="Calibri 30")
    you_lose_label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)


def submit(final_answer):
    store_entry_values = get_entry_values(final_answer)
    for i in range(0, al.list_size):
        al.sudoku_numbers[i] = str(al.sudoku_numbers[i])
    if store_entry_values == al.sudoku_numbers:
        create_new_window()
    else:
        create_you_lose()


def setup_buttons():
    global root, player_progress, new_game_button
    reset_button = tk.Button(root, text='Reset', command=lambda: reset_game(player_progress))
    reset_button.place(relx=0.1, rely=0.01, relwidth=0.15, relheight=0.08)
    new_game_button = tk.Button(root, text='New Game', command=new_game)
    new_game_button.place(relx=0.3, rely=0.01, relwidth=0.15, relheight=0.08)
    submit_button = tk.Button(root, text='Submit', command=lambda: submit(player_progress))
    submit_button.place(relx=0.5, rely=0.01, relwidth=0.15, relheight=0.08)


def select_difficulty():
    global root, difficulty_setting
    difficulty_menu = tk.OptionMenu(root, difficulty_setting, 1, 2, 3, 4, 5, 6, 7, 8)
    difficulty_menu.place(relx=0.7, rely=0.01, relwidth=0.08, relheight=0.08)
    for i in range(1,9):
        if int(difficulty_setting.get()) == i:
            difficulty_value = i + 1
    difficulty_value = 11 - difficulty_value
    return difficulty_value


def setup_border():
    global frame
    start_point = 0.00
    while start_point < 1:
        border_colour = tk.Label(frame, bg='black')
        border_colour.place(relx=start_point, rely=0.0, relwidth=0.01, relheight=1) # y axis
        border_colour = tk.Label(frame, bg='black')
        border_colour.place(relx=0, rely=start_point, relwidth=1, relheight=0.01) # x axis
        start_point += 0.33


def delete_entries():
    global player_progress
    i = 0
    while i < al.list_size:
        get_entry = player_progress[i]
        get_entry.destroy()
        i += 1


def enter_numbers():
    global frame, entry, player_progress, current_number
    x_position = 0.01 # 0.01 = 1 percent
    y_position = 0.01
    current_number = 0
    while x_position < 0.99:
        entry = tk.Entry(frame, justify = 'center', font= "Calibri 30")
        entry.place(relx=x_position, rely=y_position, relwidth=0.1, relheight=0.1)
        r = rd.randrange(1, 10)
        difficulty = select_difficulty()
        if r < difficulty:
            entry.insert(0, al.sudoku_numbers[current_number])
            entry.configure(state='disable')  # user can't edit number
        player_progress.insert(current_number, entry)
        current_number += 1
        x_position += 0.11
        if x_position > 0.99:
            x_position = 0.01
            y_position += 0.11
        if y_position > 0.99:
            x_position = 1
    new_game_button.config(state='normal')


def setup_window():
    global frame, root
    height = 600
    width = 600
    canvas = tk.Canvas(root, height=height, width=width)
    canvas.pack()
    background_colour = tk.Label(root, bg='#3841a3')
    background_colour.place(relwidth=1, relheight=1)
    frame = tk.Frame(root, bg='grey')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    setup_border()
    setup_buttons()
    enter_numbers()


def setup_gui():
    global root
    setup_window()
    root.mainloop()

