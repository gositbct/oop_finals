import tkinter as tk
#TO USE COMBOBOX
from tkinter import ttk
#TO USE MESSAGEBOX
from tkinter import messagebox

#BASICS
finals3 = tk.Tk()
finals3.title("FINALS")
finals3.config(bg="teal")
finals3.geometry("700x400")

#NAMES IN COMBOBOX 
positions = [
    "Manager",
    "System Administrator",
    "System Analyst",
    "Programmer",
    "Technician",
    "Encoder",
    "Messenger"
]


#IMAGE AND POSITION (WHITE LINE)
image_path = tk.PhotoImage(file=r"C:\Users\dell\Downloads\uinobg.png") 
image_label = tk.Label(finals3, image=image_path, bg="teal")  
image_label.place(relx=0.5, rely=0.5, anchor="center") 

#"PAYSLIP" AND POSITION
payslip_label=tk.Label(finals3, text="PAYSLIP", font=("Arial", 18, "bold"), fg='black', bg='teal', padx=5, pady=5)
payslip_label.place(relx=0.48, rely=0.12, anchor="center", )  

#"POSITION" AND POSITION
position_label = tk.Label(finals3, text="Position:", bg="teal", font=("Arial", 10), fg="black")
position_label.place(relx=0.21, rely=0.37, anchor="center")

#COMBOBOX AND POSITION
position_cb = ttk.Combobox(finals3, values=positions)
position_cb.place(relx=0.36, rely=0.37, anchor="center")
position_cb.set("(Please Select)")

#"NAME" AND POSITION
name_label=tk.Label(finals3, text="Name:", bg="teal",font=("Arial", 10))
name_label.place(relx=0.20, rely=0.30, anchor="center", )

#TEXTBOX BESIDES "NAME"
name_entry = tk.Entry(finals3)
name_entry.place(relx=0.35, rely=0.3, anchor="center", )

#"OT HOURS" AND POSITION
ot_label=tk.Label(finals3, text="OT Hours (Overtime):", bg="teal",font=("Arial", 10), fg="black")
ot_label.place(relx=0.17, rely=0.44, anchor="center", )

#TEXTBOX BESIDES "OT HOURS"
ot_entry = tk.Entry(finals3)
ot_entry.place(relx=0.35, rely=0.44, anchor="center", )

#"PAY GRADE" AND POSITION
pg_label=tk.Label(finals3, text="Pay Grade:", bg="teal",font=("Arial", 10), fg="black")
pg_label.place(relx=0.23, rely=0.55, anchor="center", )

#"GROSS SALARY" AND POSITION
gs_label=tk.Label(finals3, text="Gross Salary:", bg="teal",font=("Arial", 10), fg="black")
gs_label.place(relx=0.60, rely=0.39, anchor="center", )

#TEXTBOX BESIDES "GROSS SALARY"
gs_entry = tk.Entry(finals3)
gs_entry.place(relx=0.76, rely=0.40, anchor="center", )

#"LESS" AND POSITION
less_label=tk.Label(finals3, text="Less:", bg="teal",font=("Arial", 10), fg="black")
less_label.place(relx=0.57, rely=0.45, anchor="center", )

#"TAX" AND POSITION
tax_label=tk.Label(finals3, text="Tax:", bg="teal",font=("Arial", 10), fg="black")
tax_label.place(relx=0.63, rely=0.50, anchor="center", )

#TEXTBOX BESIDES "TAX"
tax_entry = tk.Entry(finals3)
tax_entry.place(relx=0.76, rely=0.50, anchor="center", )

#"SSS" AND POSITION
sss_label=tk.Label(finals3, text="SSS:", bg="teal",font=("Arial", 10), fg="black")
sss_label.place(relx=0.63, rely=0.56, anchor="center", )

#TEXTBOX BESIDES "SSS"
sss_entry = tk.Entry(finals3, state="readonly", justify="center")
sss_entry.place(relx=0.76, rely=0.56, anchor="center", )
sss_entry.config(state="normal")  
sss_entry.insert(0, "200")  
sss_entry.config(state="readonly")

#"NET SALARY" AND POSITION
ns_label=tk.Label(finals3, text="Net Salary:", bg="teal",font=("Arial", 10), fg="black")
ns_label.place(relx=0.59, rely=0.63, anchor="center", )

#TEXTBOX BESIDES "NET SALARY"
ns_entry = tk.Entry(finals3)
ns_entry.place(relx=0.76, rely=0.63, anchor="center", )

#RADIOBUTTON "A" AND POSITION
pay_grade = tk.StringVar(value="A")
a_button=tk.Radiobutton(finals3, text="A", variable=pay_grade, value="A", bg="teal")
a_button.place(relx=0.27, rely=0.64, anchor="center", )

#RADIOBUTTON "B" AND POSITION
b_button=tk.Radiobutton(finals3, text="B", variable=pay_grade, value="B", bg="teal")
b_button.place(relx=0.34, rely=0.64, anchor="center", )

#COMPUTE BUTTON AND POSITION
compute_button = tk.Button(finals3, text="Compute")
compute_button.place(relx=0.40, rely=0.95, anchor="center", )

#CLEAR BUTTON AND POSITION
clear_button = tk.Button(finals3, text="Clear")
clear_button.place(relx=0.48, rely=0.95, anchor="center", )

#PRINT BUTTON AND POSITION
print_button = tk.Button(finals3, text="Print")
print_button.place(relx=0.545, rely=0.95, anchor="center", )


#FUNCTION ON GETTING USER'S INPUT
def compute():
    try:
        name = name_entry.get()
        position = position_cb.get()
        ot_hours = float(ot_entry.get()) if ot_entry.get() else 0
        pay_grade_value = pay_grade.get()
        
        #IF USER SKIPS ANY ENTRY (TEXTBOX) OR DID NOT INPUT, IT PRINTS MESSAGEBOX
        if not name or not position or not ot_hours:
            messagebox.showerror("Input Error", "Please fill in all required fields.")
            return
        
        
        #BASIC PAY OF EMPLOYEES (A, B, TAX RATE)
        pay_rates = {
            "Manager": (25000, 28000, 20),
            "System Administrator": (20000, 23000, 15),
            "System Analyst": (15000, 17000, 12),
            "Programmer": (10000, 12000, 10),
            "Technician": (8000, 9000, 7),
            "Encoder": (6000, 6600, 5),
            "Messenger": (5000, 5500, 4)
        }
        
        #IF STATEMENT FOR PAY GRADE A AND B
        basic_pay, _, tax_rate = pay_rates[position]
        if pay_grade_value == "A":
                return
        if pay_grade_value == "B":
            basic_pay = pay_rates[position][1]
        

        #CALCULATE OT PAY, GROSS PAY, AND WITHHOLDING TAX
        overtime_pay = ot_hours * (0.01 * basic_pay)
        gross_pay = basic_pay + overtime_pay
        withholding_tax = gross_pay * (tax_rate / 100)
        
        # CALCULATE SSS (FIXED AS 200), TOTAL DEDUCTIONS, AND NET PAY
        sss = 200  
        total_deductions = sss + withholding_tax
        net_pay = gross_pay - total_deductions
        
        # DISPLAY RESULTS IN TEXTBOXES AFTTER USER CLICKS COMPUTE BUTTON
        gs_entry.delete(0, tk.END)
        gs_entry.insert(0, f"{gross_pay:.2f}")
        tax_entry.delete(0, tk.END)
        tax_entry.insert(0, f"{withholding_tax:.2f}")
        ns_entry.delete(0, tk.END)
        ns_entry.insert(0, f"{net_pay:.2f}")
        
        # GLOBAL SCOPE TO BE ACCESSED BY OTHER FUNCTIONS AND STORE VALUE OF INFOS FOR PRINTING
        global computed_values
        computed_values = {
            "name": name,
            "position": position,
            "pay_grade": pay_grade_value,
            "ot_hours": ot_hours,
            "overtime_pay": overtime_pay,
            "basic_pay": basic_pay,
            "sss": sss,
            "withholding_tax": withholding_tax,
            "total_deductions": total_deductions,
            "net_pay": net_pay
        }

    #IF USER INPUTS NON-NUMERIC VALUES IN TEXTBOXES, IT PRINTS MESSAGEBOX 
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Please enter numeric values where required.")

#FUNCTION FOR CLEARING TEXTBOXES AND COMBOBOX
def clear():
    name_entry.delete(0, tk.END)
    position_cb.set("")
    ot_entry.delete(0, tk.END)
    gs_entry.delete(0, tk.END)
    tax_entry.delete(0, tk.END)
    ns_entry.delete(0, tk.END)

#IF USER DIDN'T PRESS COMPUTE BUTTON, IT PRINTS MESSAGEBOX
def print_payslip():
    if not computed_values:
        messagebox.showerror("Error", "Please compute the salary first.")
        return
    

    #NEW WINDOW FOR PAYSLIP
    finals3_window = tk.Toplevel(finals3)
    finals3_window.title("FINALS")
    finals3_window.geometry("500x300")
    
    
    name_frame = tk.Frame(finals3_window)
    name_frame.pack(anchor="center", padx=5)
    name_label=tk.Label(name_frame, text="Employee Name:", fg="blue", font=("Arial", 12)).pack(side=tk.LEFT)
    name_label=tk.Label(name_frame, text=f"{computed_values['name']}", fg="black", font=("Arial", 12)).pack(side=tk.LEFT)

    
    position_frame = tk.Frame(finals3_window)
    position_frame.pack(anchor="center", pady=2)
    position_label=tk.Label(position_frame, text="Position:", fg="blue", font=("Arial", 12, )).pack(side=tk.LEFT)
    position_label=tk.Label(position_frame, text=f"{computed_values['position']}", fg="black", font=("Arial", 12, "italic")).pack(side=tk.LEFT)


    paygrade_frame = tk.Frame(finals3_window)
    paygrade_frame.pack(anchor="center", pady=1)
    tk.Label(paygrade_frame, text="Pay Grade Type:", fg="blue", font=("Arial", 12, )).pack(side=tk.LEFT)
    tk.Label(paygrade_frame, text=f"{computed_values['pay_grade']}", fg="black", font=("Arial", 12)).pack(side=tk.LEFT)


    ot_frame = tk.Frame(finals3_window)
    ot_frame.pack(anchor="center", pady=0)
    othours=tk.Label(ot_frame, text="OT Hours:", fg="blue", font=("Arial", 12, )).pack(side=tk.LEFT)
    othours=tk.Label(ot_frame, text=f"{computed_values['ot_hours']}", fg="black", font=("Arial", 12)).pack(side=tk.LEFT)


    otamt_frame = tk.Frame(finals3_window)
    otamt_frame.pack(anchor="center", pady=0)
    otamt_label=tk.Label(otamt_frame, text="OT Amount:", fg="blue", font=("Arial", 12, )).pack(side=tk.LEFT)
    otamt_label=tk.Label(otamt_frame, text=f"{computed_values['overtime_pay']}", fg="black", font=("Arial", 12)).pack(side=tk.LEFT)

    
    salary_frame = tk.Frame(finals3_window)
    salary_frame.pack(anchor="center", pady=0)
    salary_label=tk.Label(salary_frame, text="Basic Salary:", fg="blue", font=("Arial", 12, )).pack(side=tk.LEFT)
    salary_label=tk.Label(salary_frame, text=f"{computed_values['basic_pay']}", fg="black", font=("Arial", 12)).pack(side=tk.LEFT)


    sss_frame = tk.Frame(finals3_window)
    sss_frame.pack(anchor="center", pady=0)
    sss_label=tk.Label(sss_frame, text="SSS Contribution:", fg="blue", font=("Arial", 12, )).pack(side=tk.LEFT)
    sss_label=tk.Label(sss_frame, text=f"{computed_values['sss']}", fg="red", font=("Arial", 12)).pack(side=tk.LEFT)


    wth_frame = tk.Frame(finals3_window)
    wth_frame.pack(anchor="center", pady=0)
    wthtax_label=tk.Label(wth_frame, text="Withholding Tax:", fg="blue", font=("Arial", 12, )).pack(side=tk.LEFT)
    wthtax_label=tk.Label(wth_frame, text=f"{computed_values['withholding_tax']}", fg="red", font=("Arial", 12)).pack(side=tk.LEFT)


    td_frame = tk.Frame(finals3_window)
    td_frame.pack(anchor="center", pady=0)
    td_label=tk.Label(td_frame, text="Total Deductions:", fg="blue", font=("Arial", 12, )).pack(side=tk.LEFT)
    td_label=tk.Label(td_frame, text=f"{computed_values['total_deductions']}", fg="red", font=("Arial", 12)).pack(side=tk.LEFT)

    
    netincome_label=tk.Label(finals3_window, text=f"Net Income: {computed_values['net_pay']:.2f}", fg="blue", font=("Arial", 12)).pack()
    back_button=tk.Button(finals3_window, text="Back", command=finals3_window.destroy)
    back_button.pack(pady=15)  

#TO BE ABLE TO PERFORM FUNCTIONS OF BUTTONS IF USER PRESS WHETHER COMPUTE, CLEAR, OR PRINT BUTTONS
compute_button.config(command=compute)
clear_button.config(command=clear)
print_button.config(command=print_payslip)

#THE END:))
finals3.mainloop()

