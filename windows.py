from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from random import choice
from game_functions import compare_throws, refresh

"""A module for GUI windows."""

# Global variables for throw images because they will not work unless they are global functions
img_player = ""
img_cpu = ""


def main_window():
    """The first window that opens upon starting the application."""
    root = Tk()
    root.title("Rock, Paper, Scissors!")
    root.geometry("600x400")

    lbl_title = Label(root, text="Welcome to Rock, Paper, Scissors!"
                                 "\nPlease select either Rock, Paper, or Scissors to begin.")
    lbl_title.grid(row=0, column=0, columnspan=3, padx=166, pady=20)

    # The buttons that let the player choose their throw.
    btn_rock = Button(root, text="Rock", command=lambda: result_screen(root, "rock"))
    btn_rock.grid(row=1, column=0)
    btn_paper = Button(root, text="Paper", command=lambda: result_screen(root, "paper"))
    btn_paper.grid(row=1, column=1)
    btn_scissors = Button(root, text="Scissors", command=lambda: result_screen(root, "scissors"))
    btn_scissors.grid(row=1, column=2)

    # A button that closes and re-opens root to clear results.
    btn_reset = Button(root, text="Clear", command=lambda: refresh(main_window, root))
    btn_reset.grid(row=10, column=1)

    # A button that exits the game.
    btn_exit = Button(root, text="Exit", command=lambda: box_exit(root), bg="#b72a2a", fg="#ffffff", relief="solid")
    btn_exit.grid(row=10, column=2, pady=12)

    # A button to display the game instructions.
    btn_instructions = Button(root, text="Instructions", command=box_instructions)
    btn_instructions.grid(row=10, column=0)

    # End of function.
    root.mainloop()


def result_screen(window, player_throw):
    """A LabelFrame that displays the results of a game in main_window."""

    # Accessing the global variables so that the images can be displayed out of scope (once the function completes).
    global img_player
    global img_cpu

    # Generating the computers throw.
    cpu_throw = choice(["rock", "paper", "scissors"])

    # A frame to hold the results of the game and other frame elements.
    results = LabelFrame(window, text="Result!")
    results.grid(row=2, column=0, columnspan=3)

    # A collection of frames that display what each player has thrown.
    frm_player = LabelFrame(results, text="Player Throw")
    frm_player.grid(row=0, column=0, sticky=NW)

    img_player = ImageTk.PhotoImage(Image.open(f"images/{player_throw}.png"))
    lbl_player = Label(frm_player, image=img_player)
    lbl_player.pack()

    frm_vs = LabelFrame(results)
    frm_vs.grid(row=0, column=1)
    Label(frm_vs, text="VS").pack()

    frm_cpu = LabelFrame(results, text="CPU Throw")
    frm_cpu.grid(row=0, column=2, sticky=NE)

    img_cpu = ImageTk.PhotoImage(Image.open(f"images/{cpu_throw}.png"))
    lbl_cpu = Label(frm_cpu, image=img_cpu)
    lbl_cpu.pack()

    # Calls a function to compare the results and then display the winner.
    compare_throws(results, player_throw, cpu_throw)


def box_exit(window):
    """A confirmation box that confirms if the player wants to quit the game."""
    confirm = messagebox.askyesno("Exit The Game?", "You are about to exit the game,\n"
                                                    "are you sure you want to do this?")
    if confirm == 1:
        window.destroy()


def box_instructions():
    """A message box that displays game instructions."""
    instructions = messagebox.showinfo("Instructions", "Welcome to Rock, Paper, Scissors"
                                                       "\n"
                                                       "\nTo play, simply press a button for either Rock, Paper, or"
                                                       "\nScissors. This will determine your throw."
                                                       "\n"
                                                       "\nOnce you have selected, the computer will throw and the"
                                                       "\nresults will be displayed and the winner will be declared."
                                                       "\nThe Clear button will refresh the page and clear any existing"
                                                       "\nresults. However, this is not required to start another game,"
                                                       "\nas the new results will replace the old ones."
                                                       "\n"
                                                       "\nTo exit the game, press the exit button."
                                                       "\n"
                                                       "\nThank you for playing Rock, Paper, Scissors.")
