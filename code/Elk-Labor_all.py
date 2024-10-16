# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:26:04 2024

@author: Dega, Meiners
"""

# %% Import der Module und Funktionen

import numpy as np
import matplotlib.pyplot as plt

# %% Dateiname für Red Pitaya

#1N4001: rpScopeData_elie3_Diode_1N4001.csv
#1N4148: rpScopeData_elie3_Diode_1N4148.csv
#2N3904: rpScopeData_elie3_npn-Transistor_2n3904.csv
#2N3906: rpScopeData_elie3_npn-Transistor_2n3906.csv
#BS170:  rpScopeData_elie3_nMos_BS170.csv
#BS250:  rpScopeData_elie3_nMos_BS250.csv

# %% Dateiname für Spice

#1N4001: Draft_Diode_1N4001.txt"
#1N4148: Draft_Diode_1N4148.txt"
#2N3904: Draft_npn-Transistor_als_Diode.txt
#2N3906: Draft_pnp-Transistor_als_Diode.txt
#BS170:  Draft_nMos-Schaltung_auf_Spice.txt
#BS250:  Draft_pMos-Schaltung_auf_Spice.txt


# %% Red Pitaya Daten laden
Data_elie = np.loadtxt("../data/rpScopeData_elie3_Diode_1N4001.csv",
                       delimiter=",", skiprows=1)  # je nach Versuch den Pfad(Dateiname) anpassen
TIME_elie = Data_elie[:, 0]  # Time in ms
IN1_elie = np.round((1/5) * np.array(Data_elie[:, 1]), 3)  # Eingangspannung in V
IN2_elie = np.round((1/5) * np.array(Data_elie[:, 2]), 3)  # Diodenspannung in V
MATH_elie = np.round(5 * np.array(Data_elie[:, 3]), 3)  # Diodenstrom in mA
# Oder der Strom kann intern berechnet werden von IN1 und IN2 !!!
# MATH_elie = np.round(5 * (IN1_elie - IN2_elie)/10, 3)   Diodenstrom in mA

# %% Spice Daten laden
Data_Spice = np.loadtxt("../data/Draft_Diode_1N4001.txt",
                        delimiter="\t", skiprows=1)  
TIME_Spice = np.round(1000 * np.array(Data_Spice[:, 0]), 3)  # Time in ms
IN1_Spice = np.round(Data_Spice[:, 1], 3)  # Eingangspannung in V
IN2_Spice = np.round(Data_Spice[:, 2], 3)  # Diodenspannung in V
MATH_Spice = np.round(1000 * np.array(Data_Spice[:, 3]), 3)  # Diodenstrom in mA
# Oder der Strom kann intern berechnet werden von IN1 und IN2 !!!
# MATH_Spice = np.round(1000 * (IN1_Spice - IN2_Spice)/10, 3)

# %% Plot IN1, IN2, MATH, IV-Kennlinie mit Spice-Werte

# Plot Eingangs- und Diodenspanung als funktion der Zeit
fig, ax1 = plt.subplots(figsize=(12, 6))
plt.title("Diode 1N4001 erzeugende Signale in Spice"
          )  # Titel je nach Versuch anpsassen
plt.xlabel("Zeit in ms")
plt.grid()
ax1.plot(TIME_Spice, IN1_Spice, "yellow", label="Eingangsspannung (IN1)")
ax1.plot(TIME_Spice, IN2_Spice, "green", label="Diodenspannung (IN2)")
ax1.set_ylabel(r"Spannung in V", fontsize=14)
for label in ax1.get_yticklabels():
    label.set_color("black")
plt.legend(loc="upper left")

# Plot Diodenstrom als Funktion der Zeit
ax2 = ax1.twinx()
ax2.plot(TIME_Spice, MATH_Spice, "purple", label="Diodenstrom (MATH)")
ax2.set_ylabel(r"Strom in mA", fontsize=14)
for label in ax2.get_yticklabels():
    label.set_color("black")
plt.legend(loc="upper right")
plt.show()

# PLot IV-Kennlinie (Diodenstrom als Funktion der Diodenspannung)
plt.figure(2)
plt.figure(figsize=(12, 6))
plt.title("Dioden (1N4001) IV-Charakteristik in Spice"
          )  # Titel je nach Versuch anpsassen
plt.plot(IN2_Spice, MATH_Spice, "blue")
plt.xlabel("Diodenspannung (IN2) in V")
plt.ylabel("Diodenstrom (MATH) in mA")
plt.grid()
plt.show()

# %% Plot IN1, IN2, MATH, IV-Kennlinie mit Red Pitaya Werte

# Plot Eingangs- und Diodenspanung als funktion der Zeit
fig, ax1 = plt.subplots(figsize=(12, 6))
plt.title("Diode 1N4001 erzeugende Signale im Labor (Red Pitaya)"
          )  #Titel je nach Versuch anpsassen
plt.xlabel("Zeit in ms")
plt.grid()
ax1.plot(TIME_elie, IN1_elie, "yellow", label="Eingangsspannung (IN1)")
ax1.plot(TIME_elie, IN2_elie, "green", label="Diodenspannung (IN2)")
ax1.set_ylabel(r"Spannung in V", fontsize=14)
for label in ax1.get_yticklabels():
    label.set_color("black")
plt.legend(loc="upper left")

# Plot Diodenstrom als Funktion der Zeit
ax2 = ax1.twinx()
ax2.plot(TIME_elie, MATH_elie, "purple", label="Diodenstrom (MATH)")
ax2.set_ylabel(r"Strom in mA", fontsize=14)
for label in ax2.get_yticklabels():
    label.set_color("black")
plt.legend(loc="upper right")
plt.show()

# PLot IV-Kennlinie (Diodenstrom als Funktion der Diodenspannung)
plt.figure(4)
plt.figure(figsize=(12, 6))
plt.title("Dioden (1N4001) IV-Charakteristik mit Red Pitayas Werte"
          )  #Titel je nach Versuch anpsassen
plt.plot(IN2_elie, MATH_elie, "blue")
plt.xlabel("Diodenspannung (IN2) in V")
plt.ylabel("Diodenstrom (MATH) in mA")
plt.grid()
plt.show()

