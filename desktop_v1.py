# from tkinter import *
from tkinter import simpledialog
import customtkinter as ctk
from CTkListbox import *
from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()
root.geometry("400x500")
root.title("To-Do List")
root.resizable(width=0, height=0)

FONT = ctk.CTkFont(
  family="Lato",
)

def add_item():
  if item_input.get() != "":
    item = item_input.get()
    todo_list_box.insert(ctk.END, item)
    item_input.delete(0, ctk.END)
  else:
    CTkMessagebox(title="Info", message="Please input the task first")

def edit_item():
  selected_index = todo_list_box.curselection()
  if selected_index is None:
    CTkMessagebox(title="Info", message="Please select an item to delete")
    return
  
  new_value_dialog = ctk.CTkInputDialog(title="Edit Item", text="Enter new value:")
  new_value_text = new_value_dialog.get_input()
  if new_value_text == "":
    CTkMessagebox(title="Error", message="Value cannot be empty", icon="cancel")
  
  todo_list_box.insert(ctk.END, new_value_text)
  todo_list_box.delete(selected_index)

def delete_item():
  selected_index = todo_list_box.curselection()
  if selected_index is None:
    CTkMessagebox(title="Info", message="Please select an item to delete")
    return
  
  ask_delete = CTkMessagebox(title="Are you sure?", message="Do you want to delete the item?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
  if ask_delete.get() == "Yes":
    todo_list_box.delete(selected_index)

def clear_items():
  ask_clear = CTkMessagebox(title="Are you sure?", message="Do you want to clear all items?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
  if ask_clear.get() == "Yes":
    todo_list_box.delete(0, ctk.END)

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
  text="ADD", 
  text_color="#FFF", 
  font=(FONT, 16), 
  width=173/2, 
  height=53/2,
  fg_color="#338647",
  hover_color="#1C4225",
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

# button frame
button_frame = ctk.CTkFrame(
  root,
  fg_color="#242424"
)
button_frame.pack()

# edit and delete button
edit_button = ctk.CTkButton(
  button_frame,
  text="EDIT", 
  text_color="#FFF", 
  font=(FONT, 16), 
  width=173/2, 
  height=53/2,
  fg_color="#ACB24B",
  hover_color="#6E7231",
  command=edit_item
)
edit_button.grid(row=0, column=0)

delete_button = ctk.CTkButton(
  button_frame,
  text="DELETE", 
  text_color="#FFF", 
  font=(FONT, 16), 
  width=173/2, 
  height=53/2,
  fg_color="#863333",
  hover_color="#572222",
  command=delete_item
)
delete_button.grid(row=0, column=1, padx=30, pady=10)

clear_button = ctk.CTkButton(
  button_frame,
  text="CLEAR", 
  text_color="#FFF", 
  font=(FONT, 16), 
  width=173/2, 
  height=53/2,
  fg_color="#427196",
  hover_color="#28455B",
  command=clear_items
)
clear_button.grid(row=0, column=2)

root.mainloop()