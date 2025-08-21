from tkinter import Label, Tk
import time, random

app = Tk()
app.title("🕒 Neon Digital Clock")
app.geometry("700x500")
app.resizable(True,True)
app.configure(bg="black")

# Neon colors list
colors = ["cyan", "lime", "magenta", "yellow", "orange", "red"]

# Big glowing label
clock_label = Label(
    app,
    bg="black",
    fg="cyan",
    font=("DS-Digital", 80, "bold"),   # Try DS-Digital font for real digital effect
    relief='flat'
)
clock_label.pack(expand=True)

def update_time():
    current_time = time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    neon_color = random.choice(colors)  # Pick random glowing color
    clock_label.config(text=current_time, fg=neon_color)

    # Neon "glow effect" by changing window border color
    app.configure(bg=neon_color if random.randint(0, 1) else "black")

    clock_label.after(1000, update_time)

update_time()
app.mainloop()
