import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def km_to_miles(km): return km * 0.621371
def miles_to_km(miles): return miles / 0.621371
def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def m_to_ft(m): return m * 3.28084
def ft_to_m(ft): return ft / 3.28084
def kg_to_lb(kg): return kg * 2.20462
def lb_to_kg(lb): return lb / 2.20462
def l_to_gal(l): return l * 0.264172
def gal_to_l(gal): return gal / 0.264172

# Conversion options mapping
conversions = {
    "Kilometers → Miles": km_to_miles,
    "Miles → Kilometers": miles_to_km,
    "Celsius → Fahrenheit": c_to_f,
    "Fahrenheit → Celsius": f_to_c,
    "Meters → Feet": m_to_ft,
    "Feet → Meters": ft_to_m,
    "Kilograms → Pounds": kg_to_lb,
    "Pounds → Kilograms": lb_to_kg,
    "Liters → Gallons": l_to_gal,
    "Gallons → Liters": gal_to_l,
}

# Convert function
def convert():
    try:
        value = float(entry.get())
        func = conversions[combo.get()]
        result = func(value)
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Tkinter GUI setup
app = tk.Tk()
app.title("🌍 Unit Converter")
app.geometry("700x500")
app.resizable(True, True)

# Widgets
title = tk.Label(app, text="🌍 Unit Converter", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

combo = ttk.Combobox(app, values=list(conversions.keys()), font=("Helvetica", 12), state="readonly")
combo.current(0)
combo.pack(pady=10)

entry = tk.Entry(app, font=("Helvetica", 14), justify="center")
entry.pack(pady=10)

convert_btn = tk.Button(app, text="Convert", font=("Helvetica", 14, "bold"), bg="cyan", command=convert)
convert_btn.pack(pady=10)

result_label = tk.Label(app, text="Result: ", font=("Helvetica", 16), fg="blue")
result_label.pack(pady=10)

app.mainloop()
