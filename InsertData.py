import tkinter as tk
import sqlite3

# Create a database connection
conn = sqlite3.connect('../A123/astronomy.db')
c = conn.cursor()

# Create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS space_data
             (name TEXT PRIMARY KEY,
             mass REAL,
             diameter REAL,
             density REAL,
             gravity REAL,
             escape_velocity REAL,
             rotation_period REAL,
             length_of_day REAL,
             distance_from_sun REAL,
             orbital_period REAL,
             orbital_velocity REAL,
             moons INTEGER,
             ring_system TEXT,
             global_magnetic_field TEXT,
             about TEXT)''')

# Function to insert data into table


def submit():
    name = name_entry.get()
    mass = mass_entry.get()
    diameter = diameter_entry.get()
    density = density_entry.get()
    gravity = gravity_entry.get()
    escape_velocity = escape_velocity_entry.get()
    rotation_period = rotation_period_entry.get()
    length_of_day = length_of_day_entry.get()
    distance_from_sun = distance_from_sun_entry.get()
    orbital_period = orbital_period_entry.get()
    orbital_velocity = orbital_velocity_entry.get()
    moons = moons_entry.get()
    ring_system = ring_system_entry.get()
    global_magnetic_field = global_magnetic_field_entry.get()
    about = about_entry.get()

    # Insert data into table
    c.execute("INSERT INTO planets VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (name, mass, diameter, density, gravity, escape_velocity, rotation_period, length_of_day,
               distance_from_sun, orbital_period, orbital_velocity, moons, ring_system, global_magnetic_field, about))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    # Clear the form fields after submission
    name_entry.delete(0, tk.END)
    mass_entry.delete(0, tk.END)
    diameter_entry.delete(0, tk.END)
    density_entry.delete(0, tk.END)
    gravity_entry.delete(0, tk.END)
    escape_velocity_entry.delete(0, tk.END)
    rotation_period_entry.delete(0, tk.END)
    length_of_day_entry.delete(0, tk.END)
    distance_from_sun_entry.delete(0, tk.END)
    orbital_period_entry.delete(0, tk.END)
    orbital_velocity_entry.delete(0, tk.END)
    moons_entry.delete(0, tk.END)
    ring_system_entry.delete(0, tk.END)
    global_magnetic_field_entry.delete(0, tk.END)
    about_entry.delete(0, tk.END)


# Create a GUI window
root = tk.Tk()
root.title("Insert Planet Data")
root.geometry("1400x700")
root.configure(bg="green")

# Create form labels
name_label = tk.Label(root, text="Name", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
mass_label = tk.Label(root, text="Mass", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
diameter_label = tk.Label(root, text="Diameter", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
density_label = tk.Label(root, text="Density", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
gravity_label = tk.Label(root, text="Gravity", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
escape_velocity_label = tk.Label(root, text="Escape Velocity", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
rotation_period_label = tk.Label(root, text="Rotation Period", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
length_of_day_label = tk.Label(root, text="Length of Day", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
distance_from_sun_label = tk.Label(root, text="Distance from Sun", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
orbital_period_label = tk.Label(root, text="Orbital Period", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
orbital_velocity_label = tk.Label(root, text="Orbital Velocity", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
moons_label = tk.Label(root, text="Moons", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
ring_system_label = tk.Label(root, text="Ring System", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
global_magnetic_field_label = tk.Label(root, text="Global Magnetic Field", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")
about_label = tk.Label(root, text="About", width=20, borderwidth=2, foreground="Red", bg="Skyblue", font="Strong")

# Create form inputs
name_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
mass_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
diameter_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
density_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
gravity_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
escape_velocity_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
rotation_period_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
length_of_day_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
distance_from_sun_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
orbital_period_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
orbital_velocity_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
moons_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
ring_system_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
global_magnetic_field_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")
about_entry = tk.Entry(root, width=110, borderwidth=2, foreground="Black", bg="Yellow", font="Strong")

# Add form elements to window
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
mass_label.grid(row=1, column=0)
mass_entry.grid(row=1, column=1)
diameter_label.grid(row=2, column=0)
diameter_entry.grid(row=2, column=1)
density_label.grid(row=3, column=0)
density_entry.grid(row=3, column=1)
gravity_label.grid(row=4, column=0)
gravity_entry.grid(row=4, column=1)
escape_velocity_label.grid(row=5, column=0)
escape_velocity_entry.grid(row=5, column=1)
rotation_period_label.grid(row=6, column=0)
rotation_period_entry.grid(row=6, column=1)
length_of_day_label.grid(row=7, column=0)
length_of_day_entry.grid(row=7, column=1)
distance_from_sun_label.grid(row=8, column=0)
distance_from_sun_entry.grid(row=8, column=1)
orbital_period_label.grid(row=9, column=0)
orbital_period_entry.grid(row=9, column=1)
orbital_velocity_label.grid(row=10, column=0)
orbital_velocity_entry.grid(row=10, column=1)
moons_label.grid(row=11, column=0)
moons_entry.grid(row=11, column=1)
ring_system_label.grid(row=12, column=0)
ring_system_entry.grid(row=12, column=1)
global_magnetic_field_label.grid(row=13, column=0)
global_magnetic_field_entry.grid(row=13, column=1)
about_label.grid(row=14, column=0)
about_entry.grid(row=14, column=1)

# Create Submit button
submit_btn = tk.Button(root, text='Submit', command=submit)
submit_btn.grid(row=15, column=1)

# Start the main loop
root.mainloop()
