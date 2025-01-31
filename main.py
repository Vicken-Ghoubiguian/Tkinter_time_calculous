# Import all necessary Python built-in modules
from tkinter import *
from tkinter import ttk

# Import all Python project-internal modules
from configuration import configurationTimeCalculous

#
time_calculous_functions = configurationTimeCalculous()

#
root = Tk()

# Definition of the window's title
root.title("Time calculous")

#
root.iconbitmap('logo.ico')

# Definition of the window's size
root.geometry("1000x700")

# Make the window not resizable
root.resizable(False, False)

#
tabs = ttk.Notebook(root)

#
tabl = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tab3 = ttk.Frame(tabs)

#
tabs.add(tabl, text="Wished weekday in a choosen month")
tabs.add(tab2, text="Calculations on date and time")
tabs.add(tab3, text="Number of weeks in a year according to the iso norm")

# Later for 'tab1'
l1=ttk.Label(tabl,text="I am tab-1", width=10).grid(column=0, row=0, padx=30, pady=30)

# 
s1 = ttk.Separator(tabl, orient='horizontal').place(relx=0, rely=0.47, relwidth=1, relheight=1)

# Later for 'tab2'
l2=ttk.Label(tab2,text="I am tab-2", width=10).grid(column=0, row=0, padx=30, pady=30)

# 
s2 = ttk.Separator(tab2, orient='horizontal').place(relx=0, rely=0.47, relwidth=1, relheight=1)

# Later for 'tab3'
l3=ttk.Label(tab3,text="Please enter the year you want the number of weeks for :", width=50).grid(column=0, row=0, padx=150, pady=50)

#
s3 = ttk.Separator(tab3, orient='horizontal').place(relx=0, rely=0.47, relwidth=1, relheight=1)

#
tabs.pack(expand=1, fill='both')

#
root.mainloop()