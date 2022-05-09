"""Contains the GameCell class"""

import tkinter as tk

class GameCell:
    """models the cells used in the Game of Life."""
    def __init__(self, alive=False, color="white"):
        self.alive = alive
        self.color = color
        self.col_num = 0
        self.row_num = 0
        self.button = tk.Button(bg=color, command=self.set_seed)

    def set_grid():
        game_grid_list = []
        game_grid_dict = {}
        for num_c in range(66):
            for num_r in range(30):
                game_cell = GameCell()
                game_cell.col_num = num_c
                game_cell.row_num = num_r
                game_grid_list.append(game_cell)
                game_grid_dict[f"{game_cell.col_num}/{game_cell.row_num}"] = game_cell.alive
                game_cell.button.grid(column=num_c, row=num_r)


    def set_seed(self):
        """Allows user to click a cell to change its color from white (dead) to black (alive) and vice versa."""
        if self.alive == False:
            self.alive = True
            self.button["bg"] = "black"
        else:
            self.alive = False
            self.button["bg"] = "white"

    def get_neighbor_status(self):
        print("test")
        # for self.button in gui:
    