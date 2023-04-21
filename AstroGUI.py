import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import Font

# Define the GUI
root = tk.Tk()
root.title("Astronomy Database Search")
root.geometry("1400x700")
root.configure(bg="green")


# Define the database connection
conn = sqlite3.connect("astronomy.db")
c = conn.cursor()

# Define the function to search the database


def search_database():
    # Get the search query from the search box
    search_query = search_box.get()

    # Execute the SQL query to search for the data
    c.execute("SELECT * FROM planets WHERE name LIKE ?", ('%' + search_query + '%',))
    results = c.fetchall()

    # Clear the previous results from the results treeview
    for i in result_treeview.get_children():
        result_treeview.delete(i)

    # Display the new results in the results treeview
    for result in results:
        result_treeview.insert('', tk.END, values=result)

# Define the search box
search_label = tk.Label(root, text="Enter Name Astronomical Object(Planet):", borderwidth=5, foreground="Red", bg="skyblue", font="Bold")
search_label.pack(pady=20)

search_box = tk.Entry(root, width=130, borderwidth=5, foreground="Red", bg="Skyblue", font="Strong")
search_box.pack()

# Define the search button
search_button = tk.Button(root, text="Search", bg="Black", foreground="White", font="Strong", command=search_database)
search_button.pack(pady=20)


# Define the results treeview
result_treeview = ttk.Treeview(root, height=20,  columns=(
    "Planet", "Mass (10^24 kg)", "Diameter (km)", "Density (kg/m^3)", "Gravity (m/s^2)",
    "Escape Velocity (km/s)", "Rotation Period (hours)", "Length of Day (hours)",
    "Distance from Sun (10^6 km)", "Orbital Period (days)", "Orbital Velocity (km/s)",
    "Number of Moons", "Ring System?", "Global Magnetic Field?", "About"), show='headings', style='Treeview', selectmode='browse')

# root.tk_setPalette(background='Red')
header_font = Font(family='Times New Roman', size=12, weight='bold')
style = ttk.Style(root)
style.configure('Treeview.Heading', font=header_font)
result_treeview.heading("Planet", text="Planet")
result_treeview.heading("Mass (10^24 kg)", text="Mass(10^24 kg)")
result_treeview.heading("Diameter (km)", text="Diameter(km)")
result_treeview.heading("Density (kg/m^3)", text="Density(kg/m^3)")
result_treeview.heading("Gravity (m/s^2)", text="Gravity(m/s^2)")
result_treeview.heading("Escape Velocity (km/s)", text="Escape Velocity(km/s)")
result_treeview.heading("Rotation Period (hours)", text="Rotation Period(hours)")
result_treeview.heading("Length of Day (hours)", text="Length of Day(hours)")
result_treeview.heading("Distance from Sun (10^6 km)", text="Distance from Sun(10^6 km)")
result_treeview.heading("Orbital Period (days)", text="Orbital Period(days)")
result_treeview.heading("Orbital Velocity (km/s)", text="Orbital Velocity(km/s)")
result_treeview.heading("Number of Moons", text="Number of Moons")
result_treeview.heading("Ring System?", text="Ring System?")
result_treeview.heading("Global Magnetic Field?", text="Global Magnetic Field?")
result_treeview.heading("About", text="About")

result_treeview.pack(pady=10)


# Start the GUI main loop
root.mainloop()

# Close the database connection when the GUI is closed
conn.close()
