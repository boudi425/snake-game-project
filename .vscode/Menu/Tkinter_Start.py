import tkinter as tk 
from tkinter import ttk 

# Creating tkinter window 
window = tk.Tk() 
window.geometry('350x250') 
# Label 
ttk.Label(window, text = "Select the Month :", 
		font = ("Times New Roman", 10)).grid(column = 0, 
		row = 15, padx = 10, pady = 25) 

n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, 
							textvariable = n) 

# Adding combobox drop down list 
monthchoosen['values'] = (' January', 
						' February', 
						' March', 
						' April', 
						' May', 
						' June', 
						' July', 
						' August', 
						' September', 
						' October', 
						' November', 
						' December') 
def Show_data(data):
    print(f"This is Your month {data}")
button = ttk.Button(window, text="Sumbit", command=Show_data(n.get()))
button.grid(column = 1, row = 20)
monthchoosen.grid(column = 1, row = 15) 

# Shows february as a default value 
monthchoosen.current(1) 
window.mainloop() 
