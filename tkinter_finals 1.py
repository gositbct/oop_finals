import tkinter as tk

#BASICS
finals1 = tk.Tk()
finals1.title("User Information System")
finals1.geometry("250x200")

# "NAME", TEXTBOX AND POSITION
name_label=tk.Label(finals1, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
name_entry = tk.Entry(finals1)
name_entry.grid(row=0, column=1, padx= 3, pady=1)

#"ADDRESS", TEXTBOX AND POSITION
address_label=tk.Label(finals1, text="Address:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
address_entry = tk.Entry(finals1)
address_entry.grid(row=1, column=1, padx=5, pady=2)

#"CONTACT NUMBER", TEXTBOX AND POSITION
conteactnumber_label=tk.Label(finals1, text="Contact Number:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
contact_entry = tk.Entry(finals1)
contact_entry.grid(row=2, column=1, padx=5, pady=2)

#"EMAIL", TEXTBOX AND POSITION
email_label=tk.Label(finals1, text="Email:").grid(row=3, column=0, sticky="w", padx=5, pady=2)
email_entry = tk.Entry(finals1)
email_entry.grid(row=3, column=1, padx=5, pady=2)

#SUBMIT BUTTON
submit_button = tk.Button(finals1, text="Submit", command=lambda: [
    
    #NEW WINDOW OF THE USER'S INPUTTED INFOS
    (new_window := tk.Toplevel(finals1)),
    new_window.title("User Information System"),
    new_window.geometry("200x100"),
    tk.Label(new_window, text=f"Name: {name_entry.get()}\nAddress: {address_entry.get()}\n"
                              f"Contact Number: {contact_entry.get()}\nEmail: {email_entry.get()}",
             padx=10, pady=10).pack()
])

#POSITION OF "SUBMIT"
submit_button.grid(row=4, column=0, padx=5, pady=5)

#"CLEAR"
clear_button = tk.Button(finals1, text="Clear", 
                         
        #ALL INFOS WILL BE DELETED IF USER CLICK CLEAR BUTTON              
        command=lambda: (name_entry.delete(0, tk.END), 
        address_entry.delete(0, tk.END), 
        contact_entry.delete(0, tk.END), 
        email_entry.delete(0, tk.END)))

#POSITION OF "CLEAR"
clear_button.grid(row=4, column=1, padx=5, pady=5)

#THE END:))
finals1.mainloop()
