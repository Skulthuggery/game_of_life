"""Contains functions for the game grid."""

import tkinter as tk


def set_grid(gui):
    def seed():
        if game_cell(bg="white"):
            game_cell(bg="black")
        else:
            game_cell(bg="white")
    for num_c in range(66):
        for num_r in range(30):
            game_cell = tk.Button(gui, bg='white', command=seed)
            game_cell.grid(column=num_c, row=num_r)

