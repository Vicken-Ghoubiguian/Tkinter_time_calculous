# Import all necessary Python built-in modules
from tkinter import *
from tkinter import ttk
from customized_python_modules import tooltip
from enum import Enum

# Import all Python project-internal modules
from configuration import configurationTimeCalculous

#
class numeral(Enum):
    FIRST = 0
    SECOND= 1
    THIRD = 2
    BEFORE_LAST = 3
    LAST = 4

#
class weekDay(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

#
if __name__ == "__main__" :

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
    tab4 = ttk.Frame(tabs)
    tab5 = ttk.Frame(tabs)
    tab6 = ttk.Frame(tabs)

    #
    tabs.add(tabl, text="number_of_days_in_choosen_month_in_choosen_year")
    tabs.add(tab2, text="number_of_weeks_in_a_year_according_to_the_iso_norm")
    tabs.add(tab3, text="wished_wday_in_choosen_year")
    tabs.add(tab4, text="wished_number_in_year_is_day_in_choosen_year")
    tabs.add(tab5, text="wished_wday_in_choosen_month")

    #
    tooltip = tooltip.Tooltip(tabs, "This is a custom tooltip")

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
    s4 = ttk.Separator(tab4, orient='horizontal').place(relx=0, rely=0.47, relwidth=1, relheight=1)

    #
    s5 = ttk.Separator(tab5, orient='horizontal').place(relx=0, rely=0.47, relwidth=1, relheight=1)

    #
    tabs.pack(expand=1, fill='both')

    #
    root.mainloop()