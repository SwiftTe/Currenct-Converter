import tkinter as tk
from tkinter import ttk, messagebox
from currency_converter import convert_currency, get_exchange_rates

# Create main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x350")

# Title label
label_title = tk.Label(root, text="Currency Converter", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Amount entry
tk.Label(root, text="Amount:").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

# From currency selection
tk.Label(root, text="From Currency:").pack()
from_currency = ttk.Combobox(root, values=["USD", "EUR", "INR", "GBP", "JPY"])
from_currency.pack()
from_currency.set("USD")

# To currency selection
tk.Label(root, text="To Currency:").pack()
to_currency = ttk.Combobox(root, values=["USD", "EUR", "INR", "GBP", "JPY"])
to_currency.pack()
to_currency.set("INR")

# Convert function
def perform_conversion():
    try:
        amount = float(entry_amount.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        
        result = convert_currency(amount, from_curr, to_curr)
        if result:
            messagebox.showinfo("Conversion Result", f"{amount} {from_curr} = {result} {to_curr}")
        else:
            messagebox.showerror("Error", "Conversion failed!")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")

# Refresh exchange rates
def refresh_rates():
    rates = get_exchange_rates()
    if rates:
        messagebox.showinfo("Success", "Exchange rates updated successfully!")
    else:
        messagebox.showerror("Error", "Failed to update exchange rates.")

# Clear all inputs
def clear_inputs():
    entry_amount.delete(0, tk.END)
    from_currency.set("USD")
    to_currency.set("INR")

# Convert button
btn_convert = tk.Button(root, text="Convert", command=perform_conversion)
btn_convert.pack(pady=5)

# Refresh rates button
btn_refresh = tk.Button(root, text="Refresh Rates", command=refresh_rates)
btn_refresh.pack(pady=5)

# Clear button
btn_clear = tk.Button(root, text="Clear", command=clear_inputs)
btn_clear.pack(pady=5)

# Run GUI
root.mainloop()
