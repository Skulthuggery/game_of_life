# Recreating Conway's Game of Life

import tkinter as tk

import game_cell as gc

game_cell = gc.GameCell

def program_start():
    """Greets user on start up and creates GUI main window and game grid, and sets all the 'cells' to 'dead'."""
    print("\nWelcome to the Game of Life!\n")
    # Window settings
    gui = tk.Tk()
    gui.title("Game of Life")
    gui.geometry("1920x1080")
    # Main Program
    game_cell.set_grid()
    # Button settings
    start_button = tk.Button(gui, text="Start", width=25, command=lambda: game_cell.start_generations)
    start_button.place(x=600, y=950)
    stop_button = tk.Button(gui, text="Stop", width=25)
    stop_button.place(x=900, y=950)
    quit_button = tk.Button(gui, text="Quit", width=25, command=gui.destroy)
    quit_button.place(x=1200, y=950)
    gui.mainloop()


def main():
    program_start()

if __name__ == "__main__":
    main()