import tkinter as tk
import customtkinter as ctk
from CTkListbox import *
from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()
root.geometry("400x500")
root.resizable(width=0, height=0)

FONT = ctk.CTkFont(
  family="Lato"
)

def add_item():
  if item_input.get() != "":
    item = item_input.get()
    todo_list_box.insert(ctk.END, item)
    item_input.delete(0, ctk.END)
  else:
    CTkMessagebox(title="Info", message="Please input some task first")

def edit_item():
  pass

def delete_item():
  pass

main_frame = ctk.CTkFrame(
  root, 
  fg_color="#242424"
)
main_frame.pack(padx=10, pady=10)

title_label = ctk.CTkLabel(
  main_frame, 
  text="To-Do List", 
  text_color="#FFF", 
  font=(FONT, 32)
)
title_label.grid(row=0, column=0, columnspan=4, sticky="news", pady=10)

# row 2 input and add item button
item_input = ctk.CTkEntry(
  main_frame, 
  placeholder_text="Enter item...", 
  width=420/2, 
  height=53/2,
  font=(FONT, 16)
)
item_input.grid(row=1, column=0, columnspan=3, sticky='w')

add_button = ctk.CTkButton(
  main_frame,
  text="Add", 
  text_color="#FFF", 
  font=(FONT, 16), 
  width=173/2, 
  height=53/2,
  fg_color="#338647",
  hover_color="#2C693B",
  command=add_item
)
add_button.grid(row=1, column=3, padx=20, pady=10, sticky='e')

todo_list_box = CTkListbox(
  root,
  width=350,
  height=270,
  text_color="#FFF",
  hover_color="#3e3e3e",
  highlight_color="#333",
)
todo_list_box.pack(padx=20, pady=10)

root.mainloop()