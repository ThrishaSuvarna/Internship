import tkinter as tk
from tkinter import messagebox, ttk
import random

# ---------------- Logic Variables ----------------
remaining_distance = 0
total_distance = 0
speed = 0
checkpoints = []
robot_name = ""

# ---------------- Animation Function ----------------
def animate_robot():
    current_x = robot_label.winfo_x()
    if current_x < 400:
        robot_label.place(x=current_x + 20, y=260)

# ---------------- Start Robot ----------------
def start_robot():
    global remaining_distance, total_distance, speed, checkpoints, robot_name

    try:
        robot_name = name_entry.get()
        total_distance = float(distance_entry.get())
        remaining_distance = total_distance

        if total_distance > 150:
            speed = 30
        elif 80 <= total_distance <= 150:
            speed = 20
        else:
            speed = 10

        checkpoints = ["Start"]
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, "🤖 Robot started moving...\n\n")

        robot_label.place(x=20, y=260)
        progress["maximum"] = total_distance
        progress["value"] = 0

        step_button.config(state="normal")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid distance")

# ---------------- Move Step ----------------
def move_step():
    global remaining_distance

    if remaining_distance <= 0:
        output_box.insert(tk.END, "\n🎯 Target Reached!\n")
        checkpoints.append("Target Reached")
        show_summary()
        step_button.config(state="disabled")
        return

    obstacle = obstacle_var.get()
    output_box.insert(tk.END, f"Remaining Distance: {remaining_distance} meters\n")

    if obstacle == "human":
        output_box.insert(tk.END, "👤 Human detected! Waiting...\n")
        checkpoints.append("Waited for Human")

    elif obstacle == "wall":
        turn = random.choice(["Left", "Right", "Forward", "Backward"])
        output_box.insert(tk.END, f"🧱 Wall detected! Turned {turn}\n")
        checkpoints.append(f"Turned {turn}")

    else:
        output_box.insert(tk.END, "No obstacle. Moving forward...\n")
        checkpoints.append("Moved Forward")

    remaining_distance -= speed
    if remaining_distance < 0:
        remaining_distance = 0

    progress["value"] = total_distance - remaining_distance
    animate_robot()

    output_box.insert(tk.END, "-" * 40 + "\n")

# ---------------- Summary ----------------
def show_summary():
    output_box.insert(tk.END, "\n=== FINAL TRIP SUMMARY ===\n")
    output_box.insert(tk.END, f"Robot Name: {robot_name}\n")
    output_box.insert(tk.END, f"Total Distance: {total_distance} meters\n")
    output_box.insert(tk.END, f"Speed per Move: {speed} meters\n")
    output_box.insert(tk.END, "Checkpoints:\n")
    for cp in checkpoints:
        output_box.insert(tk.END, f" - {cp}\n")

# ---------------- GUI ----------------
window = tk.Tk()
window.title("🤖 RoboController 2.0 (Animated)")
window.geometry("600x600")
window.configure(bg="#f0f8ff")

tk.Label(window, text="RoboController 2.0", font=("Arial", 18, "bold"), bg="#f0f8ff").pack(pady=10)

tk.Label(window, text="Robot Name", bg="#f0f8ff").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Distance to Target (meters)", bg="#f0f8ff").pack()
distance_entry = tk.Entry(window)
distance_entry.pack()

tk.Label(window, text="Obstacle Type", bg="#f0f8ff").pack()
obstacle_var = tk.StringVar(value="none")
tk.OptionMenu(window, obstacle_var, "none", "human", "wall").pack()

tk.Button(window, text="Start Robot", bg="lightblue", command=start_robot).pack(pady=8)

step_button = tk.Button(window, text="Move Step ▶", bg="lightgreen", command=move_step, state="disabled")
step_button.pack(pady=5)

# Progress Bar
progress = ttk.Progressbar(window, length=450)
progress.pack(pady=10)

# Robot Emoji (Animated)
robot_label = tk.Label(window, text="🤖", font=("Arial", 30), bg="#f0f8ff")

# Output Box
output_box = tk.Text(window, height=15, width=70)
output_box.pack(pady=10)

window.mainloop()