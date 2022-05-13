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
    def set_grid(game_grid_list, game_grid_dict):
        for num_c in range(GameCell.max_col):
            for num_r in range(GameCell.max_row):
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

    # def start_generations(running, game_cell):
    #     if not running:
    #         print("test")
    #     elif running:
    #         game_cell.get_neighbor_status(game_cell, game_grid_list, game_grid_dict)
    #         game_cell.new_generation(game_cell, game_grid_list)
    
    @staticmethod
    def get_neighbor_status(game_grid_list, game_grid_dict):
        """For each cell in game_cell_list, checks its neighboring cells to determine if its alive then increments alive_neighbors if so, then calls new_generation() method"""
        for game_cell in game_grid_list:
            game_cell.alive_neighbors = 0
            """North-West Neighbor"""
            if game_grid_dict[f"{game_cell.col_num - 1}/{game_cell.row_num - 1}"] == True:
                game_cell.alive_neighbors += 1
            """North Neighbor"""
            if game_grid_dict[f"{game_cell.col_num}/{game_cell.row_num - 1}"] == True:
                game_cell.alive_neighbors += 1
            """North-East Neighbor"""
            if game_grid_dict[f"{game_cell.col_num + 1}/{game_cell.row_num - 1}"] == True:
                game_cell.alive_neighbors += 1
            """West Neighbor"""
            if game_grid_dict[f"{game_cell.col_num - 1}/{game_cell.row_num}"] == True:
                game_cell.alive_neighbors += 1
            """East Neighbor"""
            if game_grid_dict[f"{game_cell.col_num + 1}/{game_cell.row_num}"] == True:
                game_cell.alive_neighbors += 1
            """South-West Neighbor"""
            if game_grid_dict[f"{game_cell.col_num - 1}/{game_cell.row_num + 1}"] == True:
                game_cell.alive_neighbors += 1
            """South Neighbor"""
            if game_grid_dict[f"{game_cell.col_num}/{game_cell.row_num + 1}"] == True:
                game_cell.alive_neighbors += 1
            """South-East Neighbor"""
            if game_grid_dict[f"{game_cell.col_num + 1}/{game_cell.row_num + 1}"] == True:
                game_cell.alive_neighbors += 1

    @staticmethod
    def new_generation(game_grid_list):
        """Checks how many neighbors are alive, then sets the active cell to either 'alive' or 'dead' based on the number of alive neighbor cells.
        The active cell's button color is changed appropriately."""
        for game_cell in game_grid_list:
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

