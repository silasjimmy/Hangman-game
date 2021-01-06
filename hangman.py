#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 20:05:49 2021

@author: silasjimmy
"""

import tkinter as tk

class UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hangman")
        self.resizable(False, False)
        self.geometry("800x600")
        self.game_screen()
        
    def game_screen(self):
        self.game_screen = tk.Frame(self, width=800, height=600, bg="white")
        self.game_screen.pack_propagate(0)
        
        self.gl_label = tk.Label(self.game_screen, text="Guesses left:", font="Arial 12 bold")
        self.al_label = tk.Label(self.game_screen, text="Available letters:", font="Arial 12 bold")
        self.wl_label = tk.Label(self.game_screen, text="Warnings left:", font="Arial 12 bold")
        self.gw_label = tk.Label(self.game_screen, text="Guessed word", font="Arial 12 bold")
        self.guess_entry = tk.Entry(self.game_screen, width=3)
        self.guess_button = tk.Button(self.game_screen, text="Enter guess")
        self.hints_section = tk.Scrollbar(self.game_screen)
        
        widget_spacing = 90
        game_screen_width = self.widget_width(self.game_screen)
        al_label_width = self.widget_width(self.al_label)
        gw_label_width = self.widget_width(self.gw_label)
        guess_entry_width = self.widget_width(self.guess_entry)
        guess_button_width = self.widget_width(self.guess_button)
        
        self.gl_label.pack(anchor=tk.NE, side=tk.LEFT)
        self.wl_label.pack(anchor=tk.NW, side=tk.RIGHT)
        self.gw_label.place(x=(game_screen_width - gw_label_width) / 2, y=widget_spacing)
        self.al_label.place(x=(game_screen_width - al_label_width) / 2, y=widget_spacing * 2)
        self.guess_entry.place(x=((game_screen_width - guess_entry_width) / 2) - (guess_button_width / 3), y=widget_spacing * 3)
        self.guess_button.place(x=((game_screen_width - guess_button_width) / 2) + (guess_button_width / 2), y=widget_spacing * 3)
        self.hints_section.place(x=(game_screen_width - guess_button_width) / 2, y=widget_spacing * 4)
        
        self.game_screen.pack(anchor=tk.N, side=tk.LEFT)
        
    def widget_width(self, widget):
        return widget.winfo_reqwidth()
        
if __name__ == "__main__":
    game = UI()
    game.mainloop()