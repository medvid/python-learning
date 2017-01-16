import tkinter
from tkinter import messagebox, font

dim = 3

app = tkinter.Tk()

data = [[tkinter.StringVar() for x in range(dim)] for y in range(dim)]
player_var = tkinter.StringVar()
font36 = font.Font(size=36, weight=font.BOLD)
counter = 0

def reset():
    global data, counter
    [[data[x][y].set("") for x in range(dim)] for y in range(dim)]
    counter = 0
    player_var.set("Player 1 movement")

def check_values(values):
    if len(values) == 1:
        s = values.pop()
        if s:
            return True
    return False

def win(player):
    messagebox.showinfo("Congratulations", "Player {} wins!".format("1" if player else "2"))
    reset()

def solve(data):
    # check columns
    for i in range(dim):
        j_values = set()
        for j in range(dim):
            j_values.add(data[i][j].get())
        if check_values(j_values):
            return True

    # check rows
    for j in range(dim):
        i_values = set()
        for i in range(dim):
            i_values.add(data[i][j].get())
        if check_values(i_values):
            return True

    # check diagonals
    k_values = set()
    for k in range(dim):
        k_values.add(data[k][k].get())
    if check_values(k_values):
        return True

    l_values = set()
    for l in range(dim):
        l_values.add(data[l][dim - l - 1].get())
    if check_values(l_values):
        return True

# event handler

def on_click(event, arg):
    global data, buttons, counter
    x=arg[0]
    y=arg[1]
    isplayer1 = counter % 2 == 0
    result = "X" if isplayer1 else "O"
    data[x][y].set(result)
    if solve(data):
        win(isplayer1)
    else:
        counter += 1
        player_var.set("Player {} movement".format("2" if isplayer1 else "1"))

# Create GUI

def create_reset_button():
    b = tkinter.Button(app, text = "Reset", command = reset, width = 10, height = 2)
    b.place(x = 5, y = 5)

def create_status_label(player_var):
    l = tkinter.Label(app, textvariable = player_var, width = 20, height = 2)
    l.place(x = 100, y = 10)

def create_cell_button(x, y, var):
    b = tkinter.Button(app, textvariable=var, width = 3, height = 1, font = font36)
    b.bind("<Button-1>", lambda event, arg=[x, y]: on_click(event, arg))
    b.place(x = x * 100 + 5 , y = y * 100 + 5 + 50)

def create_cell_buttons():
    [[create_cell_button(x, y, data[x][y]) for x in range(dim)] for y in range(dim)]

# Main program

def TicTacToe():
    reset()

    create_reset_button()
    create_status_label(player_var)
    create_cell_buttons()

    app.title("TicTacToe")
    app.geometry("{}x{}+200+200".format(100 * dim + 10, 100 * dim + 60))
    app.mainloop()

if __name__ == "__main__":
    TicTacToe()
