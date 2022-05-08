"""Contains the GameCell class"""

from random import seed
import tkinter as tk

class GameCell:
    """models the cells used in the Game of Life."""
    def __init__(self, alive=False, color="white"):
        self.alive = alive
        self.color = color
        self.button = tk.Button(bg=color, command=self.seed)

    def seed(self):
        if self.alive == False:
            self.alive = True
            self.button["bg"] = "black"
        else:
            self.alive = False
            self.button["bg"] = "white"
    