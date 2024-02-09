# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:26:04 2024

@author: Dega, Meiners
"""

# %% Import der Module und Funktionen

import numpy as np
import matplotlib.pyplot as plt

# %% Dateiname für Red Pitaya

#1N4001: rpScopeData_elie1_Diode_1N4001.txt
#1N4148: rpScopeData_elie1_Diode_1N4148.txt
#2N3904: rpScopeData_elie3_npn-Transistor_2n3904.txt
#2N3906: rpScopeData_elie3_npn-Transistor_2n3906.txt
#BS170:  rpScopeData_elie4_nMos_BS170.txt
#BS250:  rpScopeData_elie4_nMos_BS250.txt

# %% Dateiname für Spice

#1N4001: Draft_Diode_1N4001.txt"
#1N4148: Draft_Diode_1N4148.txt"
#2N3904: Draft_npn-Transistor_als_Diode.txt
#2N3906: Draft_pnp-Transistor_als_Diode.txt
#BS170:  Draft_nMos-Schaltung_auf_Spice.txt
#BS250:  Draft_pMos-Schaltung_auf_Spice.txt


# %% Red Pitaya Daten laden
Data_elie = np.loadtxt("../data/rpScopeData_elie1_Diode_1N4001.txt",
                       delimiter=",", skiprows=1)  # je nach Versuch den Pfad(Dateiname) anpassen
TIME_elie = Data_elie[:, 0]  # Time in ms
IN1_elie = np.round((1/5) * np.array(Data_elie[:, 1]), 3)  # Eingangspannung in V
IN2_elie = np.round((1/5) * np.array(Data_elie[:, 2]), 3)  # Diodenspannung in V
# Der Strom kann intern berechnet werden von IN1 und IN2 !!!
MATH_elie = np.round(5 * np.array(Data_elie[:, 3]), 3)  # Diodenstrom in mA
# MATH_elie = np.round(5 * (IN1_elie - IN2_elie)/10, 3)

# Rundung der Red Pitaya Daten
# TIME_elie_gerundet = []
# IN1_elie_gerundet = []
# IN2_elie_gerundet = []
# MATH_elie_gerundet = []
# for i in range(0, len(TIME_elie)):
#     TIME_elie_gerundet.append(round((TIME_elie[i]), 3))
#     IN1_elie_gerundet.append(round((IN1_elie[i]), 3))
#     IN2_elie_gerundet.append(round((IN2_elie[i]), 3))
#     MATH_elie_gerundet.append(round((MATH_elie[i]), 3))

# %% Spice Daten laden
Data_Spice = np.loadtxt("../data/Draft_Diode_1N4001.txt",
                        delimiter="\t", skiprows=1)  
TIME_Spice = np.round(1000 * np.array(Data_Spice[:, 0]), 3)  # Time in ms
IN1_Spice = np.round(Data_Spice[:, 1], 3)  # Eingangspannung in V
IN2_Spice = np.round(Data_Spice[:, 2], 3)  # Diodenspannung in V
# Der Strom kann intern berechnet werden von IN1 und IN2 !!!
MATH_Spice = np.round(1000 * np.array(Data_Spice[:, 3]), 3)  # Diodenstrom in mA
#MATH_Spice = np.round(1000 * (IN1_Spice - IN2_Spice)/10, 3)

# Warum runden?
# Rundung der Spice-Daten vektororientiert !!!
# TIME_Spice_gerundet = []
# IN1_Spice_gerundet = []
# IN2_Spice_gerundet = []
# MATH_Spice_gerundet = []
# for i in range(0, len(TIME_Spice)):
#     TIME_Spice_gerundet.append(round((TIME_Spice[i]), 3))
#     IN1_Spice_gerundet.append(round((IN1_Spice[i]), 3))
#     IN2_Spice_gerundet.append(round((IN2_Spice[i]), 3))
#     MATH_Spice_gerundet.append(round((MATH_Spice[i]), 3))


# %% Datenbearbeitung
# Wozu abgrenzen?

# Abgrenzung des Simulationsbereichs in Spice
TIME_Spice_abgegrenzt = []
IN1_Spice_abgegrenzt = []
IN2_Spice_abgegrenzt = []
MATH_Spice_abgegrenzt = []
for n in range(TIME_Spice_gerundet.index(0), TIME_Spice_gerundet.index(1) + 1):
    TIME_Spice_abgegrenzt.append(TIME_Spice_gerundet[n])
    IN1_Spice_abgegrenzt.append(IN1_Spice_gerundet[n])
    IN2_Spice_abgegrenzt.append(IN2_Spice_gerundet[n])
    MATH_Spice_abgegrenzt.append(MATH_Spice_gerundet[n])

# Abgrenzung des Simulationsbereichs in Red Pitaya
TIME_elie_abgegrenzt = []
IN1_elie_abgegrenzt = []
IN2_elie_abgegrenzt = []
MATH_elie_abgegrenzt = []
for m in range(TIME_elie_gerundet.index(1), TIME_elie_gerundet.index(0) + 1):
    TIME_elie_abgegrenzt.append(TIME_elie_gerundet[m])
    IN1_elie_abgegrenzt.append(IN1_elie_gerundet[m])
    IN2_elie_abgegrenzt.append(IN2_elie_gerundet[m])
    MATH_elie_abgegrenzt.append(MATH_elie_gerundet[m])

# Auswahl der Spice-Werte, die wir vergleichen werden
TIME_fuer_den_Vergleich = []
IN1_Spice_fuer_den_Vergleich = []
IN2_Spice_fuer_den_Vergleich = []
MATH_Spice_fuer_den_Vergleich = []
for j in range(0, len(TIME_Spice_gerundet)):
    if TIME_Spice_gerundet[j] in TIME_elie_gerundet and TIME_Spice_gerundet[
            j] != TIME_Spice_gerundet[j - 1]:
        TIME_fuer_den_Vergleich.append(TIME_Spice_gerundet[j])
        IN1_Spice_fuer_den_Vergleich.append(IN1_Spice_gerundet[j])
        IN2_Spice_fuer_den_Vergleich.append(IN2_Spice_gerundet[j])
        MATH_Spice_fuer_den_Vergleich.append(MATH_Spice_gerundet[j])

# Auswahl der Red Pitaya Werte, die wir vergleichen werden
IN1_elie_fuer_den_Vergleich = []
IN2_elie_fuer_den_Vergleich = []
MATH_elie_fuer_den_Vergleich = []
for k in TIME_fuer_den_Vergleich:
    IN1_elie_fuer_den_Vergleich.append(
        IN1_elie_gerundet[(list(TIME_elie).index(k))])
    IN2_elie_fuer_den_Vergleich.append(
        IN2_elie_gerundet[(list(TIME_elie).index(k))])
    MATH_elie_fuer_den_Vergleich.append(
        MATH_elie_gerundet[(list(TIME_elie).index(k))])

# %% Berechnung der Abweichungen über die Zeit
Abweichung_in_IN1 = 1000 * np.array(
    IN1_Spice_fuer_den_Vergleich) - 1000 * np.array(
        IN1_elie_fuer_den_Vergleich)
Abweichung_in_IN2 = 1000 * np.array(
    IN2_Spice_fuer_den_Vergleich) - 1000 * np.array(
        IN2_elie_fuer_den_Vergleich)
Abweichung_in_MATH = np.array(MATH_Spice_fuer_den_Vergleich) - np.array(
    MATH_elie_fuer_den_Vergleich)

print("max(Abweichung in IN1)=", round((max(Abweichung_in_IN1)), 3), "mV")
print("max(Abweichung in IN2)=", round((max(Abweichung_in_IN2)), 3), "mv")
print("max(Abweichung in MATH)=", round((max(Abweichung_in_MATH)), 3), "mA")

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

# %% Plot IN1, IN2 und MATH mit Spice und Red Pitaya Werte in einem gleichen Fernster

# Plot Eingangs- und Diodenspanungen (IN1_Spice, IN2_Spice, IN1_elie, IN2_elie)
fig, ax1 = plt.subplots(figsize=(12, 6))
plt.title("Diode 1N4001 erzeugende Signale mit Spices und Red Pitayas Werte"
          )  #Titel je nach Versuch anpsassen
plt.xlabel("Zeit in ms")
plt.grid()
ax1.plot(TIME_Spice_abgegrenzt,
         IN1_Spice_abgegrenzt,
         "purple",
         label="IN1 mit Spice-Werte")
ax1.plot(TIME_Spice_abgegrenzt,
         IN2_Spice_abgegrenzt,
         "black",
         label="IN2 mit Spice-Werte")
ax1.plot(TIME_elie_abgegrenzt,
         IN1_elie_abgegrenzt,
         "orange",
         label="IN1 mit Red Pitayas Werte")
ax1.plot(TIME_elie_abgegrenzt,
         IN2_elie_abgegrenzt,
         "red",
         label="IN2 mit Red Pitayas Werte")
ax1.set_ylabel(r"Spannung in V", fontsize=14)
for label in ax1.get_yticklabels():
    label.set_color("black")
plt.legend(loc="upper left")

# Plot Diodenstroeme (MATH_Spice und MATH_elie)
ax2 = ax1.twinx()
ax2.plot(TIME_Spice_abgegrenzt,
         MATH_Spice_abgegrenzt,
         "yellow",
         label="MATH mit Spice-Werte")
ax2.plot(TIME_elie_abgegrenzt,
         MATH_elie_abgegrenzt,
         "green",
         label="MATH mit Red Pitayas Werte")
ax2.set_ylabel(r"Strom in mA", fontsize=14)
for label in ax2.get_yticklabels():
    label.set_color("black")
plt.legend(loc="upper right")
plt.show()

# PLot IV-Kennlinie mit Spices und Red Pitayas Werte in einer Figur
plt.figure(6)
plt.figure(figsize=(12, 6))
plt.title("Dioden (1N4001) IV-Charakteristik mit Spices und Red Pitayas Werte"
          )  #Titel je nach Versuch anpsassen
plt.plot(IN2_Spice_abgegrenzt,
         MATH_Spice_abgegrenzt,
         label="IV-Kennlinie mit Spice-Werte")
plt.plot(IN2_elie_abgegrenzt,
         MATH_elie_abgegrenzt,
         label="IV-Kennlinie mit Red Pitayas Werte")
plt.xlabel("Diodenspannung (IN2) in V")
plt.ylabel("Diodenstrom (MATH) in mA")
plt.grid()
plt.legend(loc="upper left")
plt.show()

# %% Plot Abweichungen über die Zeit zwischen Spices und Red Pitayas Werte

# Plot Abweichungen der Eingangs- und Diodenspanung
fig, ax1 = plt.subplots(figsize=(12, 6))
plt.title(
    "Diode 1N4001 Abweichungen über die Zeit zwischen Spices und Red Pitayas Werte"
)  #Titel je nach Versuch anpsassen
plt.xlabel("Zeit in ms")
plt.grid()
ax1.plot(TIME_fuer_den_Vergleich,
         Abweichung_in_IN1,
         "yellow",
         label="Abweichung in IN1")
ax1.plot(TIME_fuer_den_Vergleich,
         Abweichung_in_IN2,
         "green",
         label="Abweichung in IN2")
ax1.set_ylabel(r"Spannung in mV", fontsize=14)
for label in ax1.get_yticklabels():
    label.set_color("black")
plt.legend(loc="upper left")

# Plot Abweichungen des Diodenstrom
ax2 = ax1.twinx()
ax2.plot(TIME_fuer_den_Vergleich,
         Abweichung_in_MATH,
         "purple",
         label="Abweichung in MATH")
ax2.set_ylabel(r"Strom in mA", fontsize=14)
for label in ax2.get_yticklabels():
    label.set_color("black")
plt.legend(loc="upper right")
plt.show()
