from tkinter import *
from PIL import ImageTk, Image
"""A module for the functions that run the game."""


def compare_throws(window, player, cpu):
    """A function that compares the player and computer throws."""
    winner = ""

    if player == "rock":
        if cpu == "rock":
            winner = "draw"
        elif cpu == "paper":
            winner = "cpu"
        elif cpu == "scissors":
            winner = "player"
    if player == "paper":
        if cpu == "rock":
            winner = "player"
        elif cpu == "paper":
            winner = "draw"
        elif cpu == "scissors":
            winner = "cpu"
    if player == "scissors":
        if cpu == "rock":
            winner = "cpu"
        elif cpu == "paper":
            winner = "player"
        elif cpu == "scissors":
            winner = "draw"

    display_winner(window, winner)


def display_throw(window, throw):
    """A function that displays what throw the player and CPU made."""
    img_throw = ImageTk.PhotoImage(Image.open(f"images/{throw}.png"))
    display = Label(window, image=img_throw)
    display.pack()


def display_winner(window, winner):
    """A function that creates a frame to displays the winner of a game."""
    frm_winner = LabelFrame(window, text="Result:")
    frm_winner.grid(row=1, column=1)

    display = Label()

    if winner == "player":
        display = Label(frm_winner, text="Player wins!", width=10, height=3)
    elif winner == "cpu":
        display = Label(frm_winner, text="CPU wins!\nPlayer loses.", width=10, height=3)
    elif winner == "draw":
        display = Label(frm_winner, text="The game\nis a draw!", width=10, height=3)

    display.pack()


def refresh(fun_window, window):
    """A function that destroys and then re-makes a window."""
    window.destroy()
    fun_window()
