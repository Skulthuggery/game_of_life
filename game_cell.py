"""Contains the GameCell class"""

import tkinter as tk


class GameCell:
    """models the cells used in the Game of Life."""
    max_col = 66
    max_row = 30

    def __init__(self, alive=False, color="white"):
        self.alive = alive
        self.color = color
        self.col_num = 0
        self.row_num = 0
        self.alive_neighbors = 0
        self.button = tk.Button(bg=color, command=self.set_seed)
    
    @staticmethod
    def set_grid(game_grid_dict):
        for num_c in range(GameCell.max_col):
            for num_r in range(GameCell.max_row):
                game_cell = GameCell()
                game_cell.col_num = num_c
                game_cell.row_num = num_r
                game_grid_dict[f"{game_cell.col_num}/{game_cell.row_num}"] = game_cell
                game_cell.button.grid(column=num_c, row=num_r)

    def set_seed(self):
        """Allows user to click a cell to change its color from white (dead) to black (alive) and vice versa."""
        if self.alive == False:
            self.alive = True
            self.button["bg"] = "black"
        else:
            self.alive = False
            self.button["bg"] = "white"

    @staticmethod
    def get_neighbor_status(game_grid_dict):
        """For each cell in game_cell_list, checks its neighboring cells to determine if its alive then increments alive_neighbors if so, then calls new_generation() method"""
        for game_cell in game_grid_dict.values():
            game_cell.alive_neighbors = 0
            game_cell.check_north_west(game_grid_dict)
            game_cell.check_north(game_grid_dict)
            game_cell.check_north_east(game_grid_dict)
            game_cell.check_west(game_grid_dict)
            game_cell.check_east(game_grid_dict)
            game_cell.check_south_west(game_grid_dict)
            game_cell.check_south(game_grid_dict)
            game_cell.check_south_east(game_grid_dict)

    def check_north_west(self, game_grid_dict):
        """North-West Neighbor"""
        if (self.col_num - 1) < 0 or (self.row_num - 1) < 0:
            pass
        elif game_grid_dict[f"{self.col_num - 1}/{self.row_num - 1}"].alive:
            self.alive_neighbors += 1

    def check_north(self, game_grid_dict):
        """North Neighbor"""
        if (self.row_num - 1) < 0:
            pass
        elif game_grid_dict[f"{self.col_num}/{self.row_num - 1}"].alive:
            self.alive_neighbors += 1

    def check_north_east(self, game_grid_dict):
        """North-East Neighbor"""
        if (self.col_num + 2) > GameCell.max_col or (self.row_num - 1) < 0:
            pass
        elif game_grid_dict[f"{self.col_num + 1}/{self.row_num - 1}"].alive:
            self.alive_neighbors += 1

    def check_west(self, game_grid_dict):
        """West Neighbor"""
        if (self.col_num - 1) < 0:
            pass
        elif game_grid_dict[f"{self.col_num - 1}/{self.row_num}"].alive:
            self.alive_neighbors += 1

    def check_east(self, game_grid_dict):
        """East Neighbor"""
        if (self.col_num + 2) > GameCell.max_col:
            pass
        elif game_grid_dict[f"{self.col_num + 1}/{self.row_num}"].alive:
            self.alive_neighbors += 1

    def check_south_west(self, game_grid_dict):
        """South-West Neighbor"""
        if (self.col_num - 1) < 0 or (self.row_num + 2) > GameCell.max_row:
            pass
        elif game_grid_dict[f"{self.col_num - 1}/{self.row_num + 1}"].alive:
            self.alive_neighbors += 1

    def check_south(self, game_grid_dict):
        """South Neighbor"""
        if (self.row_num + 2) >= GameCell.max_row:
            pass
        elif game_grid_dict[f"{self.col_num}/{self.row_num + 1}"].alive:
            self.alive_neighbors += 1

    def check_south_east(self, game_grid_dict):
        """South-East Neighbor"""
        if (self.col_num + 2) > GameCell.max_col or (self.row_num + 2) > GameCell.max_row:
            pass
        elif game_grid_dict[f"{self.col_num + 1}/{self.row_num + 1}"].alive:
            self.alive_neighbors += 1

    @staticmethod
    def new_generation(game_grid_dict):
        """Checks how many neighbors are alive, then sets the active cell to either 'alive' or 'dead' based on the number of alive neighbor cells.
        The active cell's button color is changed appropriately."""
        for game_cell in game_grid_dict.values():
            if game_cell.alive:
                if game_cell.alive_neighbors <= 1:
                    game_cell.alive = False
                    game_cell.button["bg"] = "white"
                elif game_cell.alive_neighbors > 1 and game_cell.alive_neighbors <= 3:
                    pass
                elif game_cell.alive_neighbors >= 4:
                    game_cell.alive = False
                    game_cell.button["bg"] = "white"
            elif not game_cell.alive:
                if game_cell.alive_neighbors == 3:
                    game_cell.alive = True
                    game_cell.button["bg"] = "black"

