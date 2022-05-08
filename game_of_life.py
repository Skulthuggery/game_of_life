# Recreating Conway's Game of Life

import tkinter as tk
from tkinter.tix import COLUMN

import game_grid as grd

def program_start():
    """Greets user on start up and creates GUI main window and game grid, and sets all the 'cells' to 'dead'."""
    print("\nWelcome to the Game of Life!\n")
    # Window settings
    gui = tk.Tk()
    gui.title("Game of Life")
    gui.geometry("1920x1080")
    # Grid settings
    grd.set_grid()
    # Button settings
    seed_button = tk.Button(gui, text="Seed", width=25)
    seed_button.place(x=300, y=950)
    start_button = tk.Button(gui, text="Start", width=25)
    start_button.place(x=600, y=950)
    stop_button = tk.Button(gui, text="Stop", width=25)
    stop_button.place(x=900, y=950)
    quit_button = tk.Button(gui, text="Quit", width=25, command=gui.destroy)
    quit_button.place(x=1200, y=950)
    gui.mainloop()

def main():
    running = True
    program_start()
    # while running:
    #     gd.reset_grid()
    #     gd.set_seed()
    #     generation_start()


if __name__ == "__main__":
    main()