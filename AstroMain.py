import sqlite3
import tkinter as tk

from sqlparse.filters import output

# Create the database and table
conn = sqlite3.connect('astronomy.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS planets
             (name text Primary Key, mass real, diameter real, density real,
             gravity real, escape_velocity real, rotation_period real,
             length_of_day real, distance_from_sun real, orbital_period real,
             orbital_velocity real, moons integer, ring_system text,
             global_magnetic_field text, about Text)''')

# Insert sample data into the table
data1 = [('Mercury', 0.330, 4879, 5427, 3.7, 4.3, 1407.6, 4222.6, 57.9, 88.0, 47.4, 0, 'No', 'Yes', 'Mercury is the smallest planet in the Solar System\nand the closest planet to the Sun. It has a rocky,\ncratered surface, with a heavily cratered highland\nregion and smoother, younger plains. It has no moons,\nno atmosphere to speak of, and no magnetic field. \nDue to its proximity to the Sun, its surface temperature\ncan reach up to 800 degrees Fahrenheit during the day\nand drop to -290 degrees Fahrenheit at night. It takes\nMercury 88 Earth days to orbit the Sun and rotates on\nits axis once every 59 Earth days.\n'),
         ('Venus', 4.87, 12104, 5243, 8.9, 10.4, -5832.5, 2802.0, 108.2, 224.7, 35.0, 0, 'No', 'No', 'Venus is the second planet from the Sun and is similar in\nsize and structure to Earth. It is sometimes referred to as\nthe Earth sister planet. Venus has a thick atmosphere made\nprimarily of carbon dioxide, which causes a strong greenhouse\neffect that makes it the hottest planet in the solar system\nwith surface temperatures that can reach over 460 degrees Celsius\n(860 degrees Fahrenheit). It is also the brightest planet in the\nsky and can be seen with the naked eye. Venus has a slow rotation\nthat takes longer than its orbit around the Sun, causing the sun\nto rise in the west and set in the east.\n'),
         ('Earth', 5.97, 12756, 5514, 9.8, 11.2, 23.9, 24.0, 149.6, 365.2, 29.8, 1, 'No', 'Yes', 'Earth is the third planet from the Sun and the only known\nplanet that harbors life. It has a diameter of 12,742 kilometers\nand a mass of approximately 5.97 x 10^24 kg. Earth has one natural\nsatellite, the Moon, and its rotation on its axis creates the 24-hour\nday and night cycle. Its orbit around the Sun takes approximately\n365.25 days, creating the concept of a year. Earth atmosphere is\ncomposed mainly of nitrogen and oxygen, which is essential for\nsupporting life. Its surface is mostly covered with water, which\nmakes up about 71% of its total surface area. Earth is also home\nto a wide variety of plants and animals.\n'),
         ('Mars', 0.642, 6792, 3933, 3.7, 5.0, 24.6, 24.7, 227.9, 687.0, 24.1, 2, 'No', 'No', 'Mars is the fourth planet from the Sun in our solar system,\nand is commonly referred to as the "Red Planet" due to its\nreddish appearance. It is a rocky, terrestrial planet with\na thin atmosphere, and is similar in many ways to Earth.\nIt has a diameter of about 6,792 kilometers, making it roughly\nhalf the size of Earth, and a mass of 0.642 times that of Earth.\nIt has two small moons, Phobos and Deimos.\nMars is known for its distinctive geological features, including\nthe largest volcano in the solar system, Olympus Mons, and the\ndeepest canyon in the solar system, Valles Marineris. It also has\npolar ice caps that are composed of frozen carbon dioxide and water.\nEvidence suggests that liquid water may have existed on the surface\nof Mars in the past, and there is ongoing research to investigate the\npossibility of microbial life on the planet.\n'),
         ('Jupiter', 1898, 142984, 1326, 23.1, 59.5, 9.9, 9.9, 778.6, 4331, 13.1, 79, 'Yes', 'Yes', 'Jupiter is the largest planet in our solar system and the fifth\nplanet from the Sun. It is a gas giant, which means that it is\ncomposed mainly of hydrogen and helium, with small amounts of\nother elements. Jupiter has a diameter of about 86,881 miles\n(139,822 kilometers) at its equator, which is more than 11 times\nthe diameter of Earth.\nJupiter has a very strong magnetic field, which is more than 20,000\ntimes stronger than Earth magnetic field. This field creates\npowerful radiation belts around the planet, which can be hazardous\nfor spacecraft.\nJupiter is known for its colorful cloud bands, which are caused\nby strong winds in the planet upper atmosphere. The Great Red Spot,\na giant storm that has been raging for at least 350 years, is also a\nnotable feature of Jupiter atmosphere.\nJupiter has 79 known moons, including the four largest moons, which\nare known as the Galilean moons: Io, Europa, Ganymede, and Callisto.\nThese moons are of great interest to scientists because they are\nthought to have subsurface oceans, which could potentially harbor life.\nJupiter is named after the king of the Roman gods, and it is one of\nthe brightest objects in the night sky. It is visible to the naked eye,\nand has been known since ancient times.\n'),
         ('Saturn', 568, 120536, 687, 9.0, 35.5, 10.7, 10.7, 1433.5, 10747, 9.7, 82, 'Yes', 'Yes', 'Saturn is the sixth planet from the sun and the second-largest planet\nin our solar system, with a diameter of about 116,000 kilometers.\nIt is known for its distinctive ring system, which is composed of\nnumerous small particles of ice and rock.\nSaturn is a gas giant, with a composition of primarily hydrogen and\nhelium, and it has no solid surface. The planet atmosphere is\ncharacterized by strong winds, with the fastest winds reaching speeds\nof up to 1,800 kilometers per hour. Saturn has numerous moons, with at\nleast 82 confirmed satellites, the largest of which is Titan.\nSaturn takes about 29.5 Earth years to complete one orbit around the sun,\nand its axis is tilted at an angle of about 27 degrees, causing it to\nhave seasons like Earth. Saturn has been visited by several spacecraft,\nincluding the Cassini-Huygens mission, which orbited the planet for over\n13 years, studying its atmosphere, rings, and moons.\n'),
         ('Uranus', 86.8, 51118, 1271, 8.7, 21.3, -17.2, 17.2, 2872.5, 30589, 6.8, 27, 'Yes', 'Yes', 'Uranus is the seventh planet from the Sun and the third largest planet\nin the solar system. It has a diameter of approximately 51,118 km and\na mass of 8.68 × 10^25 kg. Uranus is classified as an ice giant, and\nlike the other gas giants in our solar system, it has no solid surface.\nUranus has a very tilted axis of rotation, which means that it essentially\nrolls around the Sun on its side. This gives Uranus very unusual seasonal\nvariations - its polar regions experience long periods of darkness and extreme\ncold, while its equatorial regions experience long periods of sunlight and heat.\nUranus has 27 known moons, the largest of which is Miranda. Uranus also has\na set of thin, dark rings that were first discovered in 1977. The rings are\ncomposed of rock and ice particles and are thought to be relatively young\ncompared to the rings of other gas giants.\nUranus was first discovered in 1781 by William Herschel, and it was the\nfirst planet to be discovered using a telescope.\n'),
         ('Neptune', 102, 49528, 1638, 11.0, 23.5, 16.1, 16.1, 4495.1, 59800, 5.4, 14, 'Yes', 'Yes', 'Neptune is the eighth and farthest known planet from the sun in the\nsolar system. It is a gas giant, and has the fourth-largest planetary\nradius and the third-largest planetary mass in the solar system.\nNeptune atmosphere is composed primarily of hydrogen and helium,\nwith traces of methane that give it its blue color. The planet has\n14 known moons, including the largest one called Triton, which is\nbelieved to be a captured Kuiper Belt object. Neptune has a strong\nmagnetic field, which is tilted at an angle of 47 degrees relative\nto its rotational axis. It has a relatively long orbital period of\n164.8 Earth years, and takes almost 165 Earth years to complete a\nsingle rotation on its axis. Neptune was first observed by Galileo\nGalilei in 1612 and was later identified as a planet by Johann Galle in 1846.\n')]

c.executemany('INSERT INTO planets VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data1)
conn.commit()

# Create the GUI
root = tk.Tk()
root.title("Astronomy Database")

# Search function


def search(search_box=None):
    planet = search_box.get().capitalize()
    c.execute(f"SELECT * FROM planets WHERE name =? '{planet}'")
    result = c.fetch()
    if result:
        output.delete('1.0', tk.END)
        output.insert(tk.END, f"Name: {result[0]}\n")
        output.insert(tk.END, f"Mass (10^24 kg): {result[1]}\n")
        output.insert(tk.END, f"Diameter (km): {result[2]}\n")
        output.insert(tk.END, f"Density (kg/m^3): {result[3]}\n")
        output.insert(tk.END, f"Gravity (m/s^2): {result[4]}\n")
        output.insert(tk.END, f"Escape Velocity (km/s): {result[5]}\n")
        output.insert(tk.END, f"Rotation Period (hours): {result[6]}\n")
        output.insert(tk.END, f"Length of Day (hours): {result[7]}\n")
        output.insert(tk.END, f"Distance from Sun (10^6 km): {result[8]}\n")
        output.insert(tk.END, f"Orbital Period (days): {result[9]}\n")
        output.insert(tk.END, f"Orbital Velocity (km/s): {result[10]}\n")
        output.insert(tk.END, f"Number of Moons: {result[11]}\n")
        output.insert(tk.END, f"Ring System?: {result[12]}\n")
        output.insert(tk.END, f"Global Magnetic Field?: {result[13]}\n")
        output.insert(tk.END, f"About: {result[14]}\n")
    else:
        output.delete('1.0', tk.END)
        output.insert(tk.END, "No planet found with that name.")
