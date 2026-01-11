import tkinter as tk
from tkinter import messagebox

# Function to calculate bill split
def calculate_split():
    try:
        rent = float(rent_entry.get())
        food = float(food_entry.get())
        electricity_units = float(electricity_units_entry.get())
        electricity_rate = float(electricity_rate_entry.get())
        num_residents = int(residents_entry.get())

        if num_residents <= 0:
            messagebox.showerror("Error", "Number of residents must be greater than 0.")
            return

        # Calculate electricity bill
        electricity_bill = electricity_units * electricity_rate
        total_expenses = rent + food + electricity_bill

        # Calculate per person
        rent_per_person = rent / num_residents
        food_per_person = food / num_residents
        electricity_per_person = electricity_bill / num_residents
        total_per_person = total_expenses / num_residents

        # Display results
        result_text = (
            f"--- Monthly Bill Split ---\n"
            f"Total Rent: ₹{rent:.2f}\n"
            f"Total Food Expenses: ₹{food:.2f}\n"
            f"Total Electricity Bill: ₹{electricity_bill:.2f}\n"
            f"Total Expenses: ₹{total_expenses:.2f}\n\n"
            f"Each Resident Pays:\n"
            f"  Rent: ₹{rent_per_person:.2f}\n"
            f"  Food: ₹{food_per_person:.2f}\n"
            f"  Electricity: ₹{electricity_per_person:.2f}\n"
            f"  Total: ₹{total_per_person:.2f}"
        )
        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create main window
root = tk.Tk()
root.title("Hostel/Flat Bill Split Application")
root.geometry("450x500")
root.resizable(False, False)

# Input fields
tk.Label(root, text="Total Rent (₹):").pack(pady=(10, 0))
rent_entry = tk.Entry(root)
rent_entry.pack()

tk.Label(root, text="Total Food Expenses (₹):").pack(pady=(10, 0))
food_entry = tk.Entry(root)
food_entry.pack()

tk.Label(root, text="Electricity Units Consumed:").pack(pady=(10, 0))
electricity_units_entry = tk.Entry(root)
electricity_units_entry.pack()

tk.Label(root, text="Electricity Rate per Unit (₹):").pack(pady=(10, 0))
electricity_rate_entry = tk.Entry(root)
electricity_rate_entry.pack()

tk.Label(root, text="Number of Residents:").pack(pady=(10, 0))
residents_entry = tk.Entry(root)
residents_entry.pack()

# Calculate Button
tk.Button(root, text="Calculate Split", command=calculate_split, bg="lightblue").pack(pady=20)

# Result Display
result_label = tk.Label(root, text="", justify="left", font=("Arial", 10))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
