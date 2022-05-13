"""Contains the GameCell class"""

import tkinter as tk


class GameCell:
    """models the cells used in the Game of Life."""
    def __init__(self, alive=False, color="white"):
        self.alive = alive
        self.color = color
        self.col_num = 0
        self.row_num = 0
        self.alive_neighbors = 0
        self.button = tk.Button(bg=color, command=self.set_seed)

    def set_grid(game_grid_list, game_grid_dict):
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

    # def start_generations(running, game_cell):
    #     if not running:
    #         print("test")
    #     elif running:
    #         game_cell.get_neighbor_status(game_cell, game_grid_list, game_grid_dict)
    #         game_cell.new_generation(game_cell, game_grid_list)
    
    def get_neighbor_status(self, game_grid_list, game_grid_dict):
        """For each cell in game_cell_list, checks its neighboring cells to determine if its alive then increments alive_neighbors if so, then calls new_generation() method"""
        for self in game_grid_list:
            self.alive_neighbors = 0
            """North-West Neighbor"""
            if game_grid_dict[f"{self.col_num - 1}/{self.row_num - 1}"] == True:
                self.alive_neighbors += 1
            else: pass
            """North Neighbor"""
            if game_grid_dict[f"{self.col_num}/{self.row_num - 1}"] == True:
                self.alive_neighbors += 1
            else: pass
            """North-East Neighbor"""
            if game_grid_dict[f"{self.col_num + 1}/{self.row_num - 1}"] == True:
                self.alive_neighbors += 1
            else: pass
            """West Neighbor"""
            if game_grid_dict[f"{self.col_num - 1}/{self.row_num}"] == True:
                self.alive_neighbors += 1
            else: pass
            """East Neighbor"""
            if game_grid_dict[f"{self.col_num + 1}/{self.row_num}"] == True:
                self.alive_neighbors += 1
            else: pass
            """South-West Neighbor"""
            if game_grid_dict[f"{self.col_num - 1}/{self.row_num + 1}"] == True:
                self.alive_neighbors += 1
            else: pass
            """South Neighbor"""
            if game_grid_dict[f"{self.col_num}/{self.row_num + 1}"] == True:
                self.alive_neighbors += 1
            else: pass
            """South-East Neighbor"""
            if game_grid_dict[f"{self.col_num + 1}/{self.row_num + 1}"] == True:
                self.alive_neighbors += 1
            else: pass

    def new_generation(self, game_grid_list):
        """Checks how many neighbors are alive, then sets the active cell to either 'alive' or 'dead' based on the number of alive neighbor cells.
        The active cell's button color is changed appropriately."""
        for self in game_grid_list:
            if self.alive == True:
                if self.alive_neighbors <= 1:
                    self.alive = False
                    self.button["bg"] = "white"
                elif self.alive_neighbors > 1 and self.alive_neighbors <= 3:
                    pass
                elif self.alive_neighbors >= 4:
                    self.alive = False
                    self.button["bg"] = "white"
            elif self.alive == False:
                if self.alive_neighbors == 3:
                    self.alive = True
                    self.button["bg"] = "black"
                else: 
                    pass
