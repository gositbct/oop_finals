import tkinter as tk 
from tkinter import messagebox

#BASICS
finals2 = tk.Tk()
finals2.title("FINALS")
finals2.geometry("900x600")
finals2.config(bg="purple")  

# IMAGES
image_path = tk.PhotoImage(file=r"C:\Users\dell\Downloads\beige.png") 
image_path2=tk.PhotoImage(file=r"C:\Users\dell\Downloads\urs.png") 
image_path3=tk.PhotoImage(file=r"C:\Users\dell\Downloads\python.png") 
image_path4=tk.PhotoImage(file=r"C:\Users\dell\Downloads\guinobg.png") 

#PLACEMENT OF IMAGES
image_label = tk.Label(finals2, image=image_path, bg="purple")  
image_label.place(relx=0.5, rely=0.5, anchor="center")  
image_label.lower()  
image2_label = tk.Label(finals2, image=image_path2, bg="purple")  
image2_label.place(relx=0.1, rely=0.15, anchor="se")
image3_label = tk.Label(finals2, image=image_path3, bg="purple")  
image3_label.place(relx=0.98, rely=0.15, anchor="se")
image4_label = tk.Label(finals2, image=image_path4, bg="beige")  
image4_label.place(relx=0.90, rely=0.85, anchor="se")

#"REQUIRED GUI DESIGN" AND POSITION
GUI_label = tk.Label(finals2, text="Sample Program Run", font=("Times New Roman", 28, "bold"),fg='white', bg="purple", padx=10, pady=5)        
GUI_label.place(relx=0.5, rely=0.1, anchor="center")  

#"CANDLELINE CORPORATION" AND POSITION
candleline_label = tk.Label(finals2, text="CandleLine Corporation", font=("Times New Roman", 18, "bold"), fg='black', bg='beige', padx=5, pady=5)
candleline_label.place(relx=0.5, rely=0.19, anchor="center", )  

#PARENTHESIS UNDER STANDARD RAD BUTTON
seventyfive_dolla=tk.Label(finals2, text="($0.00 if order amt>$75.00)", bg="beige",font=("Times New Roman", 8))
seventyfive_dolla.place(relx=0.35, rely=0.50, anchor="center", )

#TEXTS AND POSITION (HINT AND TEXTS UNDER OF IT)
hint_label=tk.Label(finals2, text="HINT: ", bg="purple",font=("Arial Rounded MT", 17, "bold italic" ), fg="white")
hint_label.place(relx=0.14, rely=0.88, anchor="center", )
amt1_label=tk.Label(finals2, text="•  Amt payable = 1.12*(100+14.95) = 128.74 (overnight shipping) ", bg="purple",font=("Arial Rounded MT", 9, "bold"  ), fg="white")
amt1_label.place(relx=0.28, rely=0.92, anchor="center", )
amt2_label=tk.Label(finals2, text="•  Amt payable = 1.12*(100+11.95) = 125.38 (express shipping) ", bg="purple",font=("Arial Rounded MT", 9, "bold"  ), fg="white")
amt2_label.place(relx=0.277, rely=0.95, anchor="center", )
amt3_label=tk.Label(finals2, text="•  Amt payable = 1.12*(100+0) = 112 (standard shipping since amt > $75) ", bg="purple",font=("Arial Rounded MT", 9, "bold"  ), fg="white")
amt3_label.place(relx=0.308, rely=0.98, anchor="center", )

#ORDER INPUT
total_label=tk.Label(finals2, text="Total amount of your order (in $)?:", bg="beige", font=("Times New Roman", 10))
total_label.place(relx=0.5, rely=0.25, anchor="center", )

#TEXTBOX
order_entry = tk.Entry(finals2)
order_entry.place(relx=0.5, rely=0.3, anchor="center", )

#MOS AND POSITION
mos_label=tk.Label(finals2, text="Pls. give your method of shipping", bg="beige", font=("Times New Roman", 10))
mos_label.place(relx=0.5, rely=0.35, anchor="center", )

#HOLDS AND UPDATES THE RADIO BUTTON DEPENDING ON THE USER INPUT
modeof_shipment = tk.StringVar()
modeof_shipment.set("Priority")

#BUTTONS AND POSITIONS
radbutton1=tk.Radiobutton(finals2, text="Priority (overnight) @ $14.95", variable=modeof_shipment, value="Priority", bg="beige",font=("Times New Roman", 10))
radbutton1.place(relx=0.35, rely=0.42, anchor="center", )
radbutton2=tk.Radiobutton(finals2, text="Express (2 days) @ $11.95", variable=modeof_shipment, value="Express", bg="beige",font=("Times New Roman", 10))
radbutton2.place(relx=0.65, rely=0.42, anchor="center", )
radbutton3=tk.Radiobutton(finals2, text="Standard (5 to 7 working days) @ $5.95", variable=modeof_shipment, value="Standard", bg="beige",font=("Times New Roman", 10))
radbutton3.place(relx=0.38, rely=0.47, anchor="center", )

#"TAX" AND POSITION
tax_label=tk.Label(finals2, text="Amount Payable (12% VAT included):", bg="beige", font=("Times New Roman", 10))
tax_label.place(relx=0.39, rely=0.65, anchor="center", )

#TEXTBOX (TABI NG VAT)
tax_entry = tk.Entry(finals2, state='readonly', font=("Times New Roman", 10))
tax_entry.place(relx=0.58, rely=0.65, anchor="center", )

#COMPUTE AND CLEAR BUTTONS
compute_button = tk.Button(finals2, text="Compute", font=("Times New Roman", 10))
compute_button.place(relx=0.49, rely=0.75)
clear_button = tk.Button(finals2, text="Clear", font=("Times New Roman", 10))
clear_button.place(relx=0.44, rely=0.75)

#COMMAND OF COMPUTE AND CLEAR BUTTONS
compute_button.config(command=lambda: (lambda: (tax_entry.config(state='normal'),tax_entry.delete(0, tk.END),tax_entry.insert(0, f"${1.12 * (float(order_entry.get()) + (0 if modeof_shipment.get() == 'Standard' and float(order_entry.get()) > 75 else {'Priority': 14.95, 'Express': 11.95, 'Standard': 5.95}[modeof_shipment.get()])):.2f}"),tax_entry.config(state='readonly')
))() if order_entry.get().replace('.', '', 1).isdigit() else messagebox.showerror("Input Error", "Please enter a valid number for the order amount."))

clear_button.config(command=lambda: (order_entry.delete(0, tk.END),tax_entry.config(state='normal'),tax_entry.delete(0, tk.END),tax_entry.config(state='readonly'),modeof_shipment.set("Priority")))

#THE END:))
finals2.mainloop()