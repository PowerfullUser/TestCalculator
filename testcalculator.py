import customtkinter as tk
from tkinter import messagebox as msg

def start():
    try:
        start_date_load = start_date.get()
        plan_load = plan.get()

        percentage = round((int(start_date_load)/int(plan_load))*100)

        exact_score.configure(text=f'{start_date_load}/{plan_load}')
        show_plans.configure(text='You got approximately '+str(percentage)+'% '+'in your examination.')

        if percentage < 40:
            grade_calculator.configure(text='Grade: 4')
        elif percentage >= 40 and percentage <= 50:
            grade_calculator.configure(text='Grade: 5')
        elif percentage >= 50 and percentage <= 60:
            grade_calculator.configure(text='Grade: 6')
        elif percentage >= 60 and percentage <= 70:
            grade_calculator.configure(text='Grade: 7')
        elif percentage >= 70 and percentage <= 80:
            grade_calculator.configure(text='Grade: 8')
        elif percentage >= 80 and percentage <= 90:
            grade_calculator.configure(text='Grade: 9')
        elif percentage >= 90:
            grade_calculator.configure(text='Grade: 10')
        else:
            return
    except ValueError:
        msg.showerror('TestCalculator', 'Please enter a valid value of an whole number')


window = tk.CTk()
window.geometry('500x500')
window._set_appearance_mode('dark')
window.title('TestCalculator')


title = tk.CTkLabel(master=window, text='TestCalculator', font=('Bahnschrift', 30))
title._set_appearance_mode('dark')
title.pack()

space = tk.CTkLabel(master=window, text='', font=('Bahnschrift', 10))
space._set_appearance_mode('dark')
space.pack()

plan_label = tk.CTkLabel(master=window, text='Full Marks', font=('Bahnschrift', 16))
plan_label._set_appearance_mode('dark')
plan_label.pack()

plan = tk.IntVar()
text_box1 = tk.CTkEntry(master=window, font=('Bahnschrift', 16), textvariable=plan, width=200)
text_box1._set_appearance_mode('dark')
text_box1.pack()

space = tk.CTkLabel(master=window, text='', font=('Bahnschrift', 10))
space._set_appearance_mode('dark')
space.pack()

plan_label = tk.CTkLabel(master=window, text='Scored Marks', font=('Bahnschrift', 16))
plan_label._set_appearance_mode('dark')
plan_label.pack()

start_date = tk.IntVar()
text_box2 = tk.CTkEntry(master=window, font=('Bahnschrift', 16), textvariable=start_date, width=200)
text_box2._set_appearance_mode('dark')
text_box2.pack()

space = tk.CTkLabel(master=window, text='', font=('Bahnschrift', 10))
space._set_appearance_mode('dark')
space.pack()

ready_button = tk.CTkButton(master=window, font=('Bahnschrift', 14), text='Calculate', command=start)
ready_button.place(relx=0.5, rely=0.5, anchor='center')
ready_button._set_appearance_mode('dark')
ready_button.pack()

space = tk.CTkLabel(master=window, text='', font=('Bahnschrift', 10))
space._set_appearance_mode('dark')
space.pack()

exact_score = tk.CTkLabel(master=window, text=None, font=('Bahnschrift', 20))
exact_score._set_appearance_mode('dark')
exact_score.pack()

show_plans = tk.CTkLabel(master=window, text=None, font=('Bahnschrift', 20), wraplength=450)
show_plans._set_appearance_mode('dark')
show_plans.pack()

grade_calculator = tk.CTkLabel(master=window, text=None, font=('Bahnschrift', 20))
grade_calculator._set_appearance_mode('dark')
grade_calculator.pack()

window.mainloop()
