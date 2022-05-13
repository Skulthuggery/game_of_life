# Recreating Conway's Game of Life

import tkinter as tk

import game_cell as gc


def start_running():
    running = True


def stop_running(): 
    running = False

def program_start(gui, game_cell, game_grid_list, game_grid_dict):
    """Greets user on start up and creates GUI main window and game grid, and sets all the 'cells' to 'dead'."""
    set_up_window(gui)
    set_up_buttons(gui)
    game_cell.set_grid(game_grid_list, game_grid_dict)
    # game_cell.start_generations(running, game_cell)

def set_up_window(gui):
    gui.title("Game of Life")
    gui.geometry("1920x1080")

def set_up_buttons(gui):
    start_button = tk.Button(gui, text="Start", width=25, command=start_running)
    start_button.place(x=600, y=950)
    stop_button = tk.Button(gui, text="Stop", width=25, command=stop_running)
    stop_button.place(x=900, y=950)
    quit_button = tk.Button(gui, text="Quit", width=25, command=gui.destroy)
    quit_button.place(x=1200, y=950)

def main():
    gui = tk.Tk()
    running = False
    game_cell = gc.GameCell
    game_grid_list = []
    game_grid_dict = {}
    program_start(gui, game_cell, game_grid_list, game_grid_dict)
    # if not running:
    #     pass
    # else:
    game_cell.get_neighbor_status(game_cell, game_grid_list, game_grid_dict)
    game_cell.new_generation(game_cell, game_grid_list)

    gui.mainloop()

if __name__ == "__main__":
    main()