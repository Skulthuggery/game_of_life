# Recreating Conway's Game of Life

import tkinter


import tkinter as tk

# import grid.py as grid


def program_start():
    """Greets user on start up and creates GUI main window and game grid, and sets all the 'cells' to 'dead'."""
    print("\nWelcome to the Game of Life!\n")
    game_of_life = tk.Tk()
    game_of_life.title("Game of Life")
    seed_button = tk.Button(game_of_life, text="Seed", width=25, command=game_of_life.destroy)
    seed_button.pack()
    start_button = tk.Button(game_of_life, text="Start", width=25)
    start_button.pack()
    stop_button = tk.Button(game_of_life, text="Stop", width=25)
    stop_button.pack()
    game_of_life.mainloop()

def main():
    running = True
    program_start()
    # while running:
    #     reset_grid()
    #     set_seed()
    #     generation_start()


if __name__ == "__main__":
    main()