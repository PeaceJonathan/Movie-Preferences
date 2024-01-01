#Jonathan Peace

#Source Code


import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
window = tk.Tk()


class moviePreferences:
    def __init__(self, window):
        self.window = window
        self.window.title("Movie Preferences")
        
        # GIF
        self.photoImage = tk.PhotoImage(file="Spongebob.gif")
        self.imageLabel = tk.Label(window, image=self.photoImage)
        self.imageLabel.grid(row=0, column=0, columnspan=3, pady=10)

        #Name and Email
        tk.Label(window, text="Customer Name:").grid(row=1, column=0)
        self.nameEntry = tk.Entry(window)
        self.nameEntry.grid(row=1, column=1)

        tk.Label(window, text="Customer Email:").grid(row=2, column=0, pady=10)
        self.emailEntry = tk.Entry(window)
        self.emailEntry.grid(row=2, column=1)

        # Movie Types
        tk.Label(window, text="Movie Types:", font=("Arial", 12, "bold")).grid(row=3, column=0)
        self.comedyVar = tk.IntVar()
        
        tk.Checkbutton(window, text="Comedy", variable=self.comedyVar).grid(row=4, column=0, sticky=tk.W)
        self.romanceVar = tk.IntVar()
        
        tk.Checkbutton(window, text="Romance", variable=self.romanceVar).grid(row=5, column=0, sticky=tk.W)
        self.documentaryVar = tk.IntVar()
        
        tk.Checkbutton(window, text="Documentary", variable=self.documentaryVar).grid(row=6, column=0, sticky=tk.W)
        self.dramaVar = tk.IntVar()
        
        tk.Checkbutton(window, text="Drama", variable=self.dramaVar).grid(row=4, column=1, sticky=tk.W)
        self.sciFiVar = tk.IntVar()
        
        tk.Checkbutton(window, text="Sci Fi", variable=self.sciFiVar).grid(row=5, column=1, sticky=tk.W)
        self.westernVar = tk.IntVar()
        
        tk.Checkbutton(window, text="Western", variable=self.westernVar).grid(row=6, column=1, sticky=tk.W)
        self.adventureVar = tk.IntVar()
        
        tk.Checkbutton(window, text="Adventure", variable=self.adventureVar).grid(row=4, column=2, sticky=tk.W)
        self.foreignVar = tk.IntVar()
        
        tk.Checkbutton(window, text="Foreign", variable=self.foreignVar).grid(row=5, column=2, sticky=tk.W)
        self.sportsVar = tk.IntVar()
        
        tk.Checkbutton(window, text="Sports", variable=self.sportsVar).grid(row=6, column=2, sticky=tk.W)

        # Format
        tk.Label(window, text="Media Format:", font=("Arial", 12, "bold")).grid(row=7, column=0)
        self.mediaFormatVar = tk.StringVar(value="Streaming")
        tk.Radiobutton(window, text="Streaming", variable=self.mediaFormatVar, value="Streaming").grid(row=8, column=0, sticky=tk.W)
        tk.Radiobutton(window, text="DVD", variable=self.mediaFormatVar, value="DVD").grid(row=8, column=1, sticky=tk.W)
        tk.Radiobutton(window, text="Blu-ray", variable=self.mediaFormatVar, value="Blu-ray").grid(row=8, column=2, sticky=tk.W)

        # Payment Method
        tk.Label(window, text="Payment Method:", font=("Arial", 12, "bold")).grid(row=9, column=1, columnspan=1)
        self.paymentMethodVar = tk.StringVar()
        paymentOptions = ["American Express", "Visa", "MasterCard"]
        self.paymentMethodCombobox = ttk.Combobox(window, values=paymentOptions, textvariable=self.paymentMethodVar)
        self.paymentMethodCombobox.grid(row=10, column=1, columnspan=1)

        # Buttons
        tk.Button(window, text="Submit", command=self.writeToFile).grid(row=11, column=0, pady=10, columnspan=2)
        tk.Button(window, text="Clear", command=self.resetFields).grid(row=11, column=1, pady=10, columnspan=2)

    def writeToFile(self):
        name = self.nameEntry.get()
        if not name:
            messagebox.showerror("Error", "Customer Name cannot be empty!")
            return

        email = self.emailEntry.get()
        selectedMovieTypes = [typ for typ, var in [("Comedy", self.comedyVar), ("Romance", self.romanceVar), ("Documentary", self.documentaryVar),
                                           ("Drama", self.dramaVar), ("Sci Fi", self.sciFiVar), ("Western", self.westernVar),
                                           ("Adventure", self.adventureVar), ("Foreign", self.foreignVar), ("Sports", self.sportsVar)] if var.get()]
        mediaFormat = self.mediaFormatVar.get()
        paymentMethod = self.paymentMethodVar.get()

        timestamp = datetime.now().strftime("%m/%d/%Y %I:%M %p")

        with open("orders.txt", "a") as file:
            file.write(f"Customer Name: {name}\n")
            file.write(f"Customer Email: {email}\n")
            file.write("Movie Types:\n")
            for movieType in selectedMovieTypes:
                file.write(f"{movieType}\n")
            file.write(f"Media Format: {mediaFormat}\n")
            file.write(f"Payment Method: {paymentMethod}\n")
            file.write(f"Time: {timestamp}\n")
            file.write("=" * 50 + "\n")

        messagebox.showinfo("Success", "Your order processed")
        self.resetFields()

    def resetFields(self):
        self.nameEntry.delete(0, tk.END)
        self.emailEntry.delete(0, tk.END)
        self.comedyVar.set(0)
        self.romanceVar.set(0)
        self.documentaryVar.set(0)
        self.dramaVar.set(0)
        self.sciFiVar.set(0)
        self.westernVar.set(0)
        self.adventureVar.set(0)
        self.foreignVar.set(0)
        self.sportsVar.set(0)
        self.mediaFormatVar.set("Streaming")
        self.paymentMethodCombobox.set("")
        
app = moviePreferences(window)
window.mainloop()

