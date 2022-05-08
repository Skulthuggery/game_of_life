"""Contains functions for the game grid."""

import game_cell as gc

def set_grid():
    for num_c in range(66):
        for num_r in range(30):
            game_cell = gc.GameCell()
            game_cell.button.grid(column=num_c, row=num_r)

