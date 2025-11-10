#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Messautomatisierung - RedPitaya STEMlab SCPI

@author: T. Ziemann, M. Meiners
"""

# %% Init
import time
import datetime
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import redpitaya_scpi as scpi

LABDESK = {
        "ELIE1": "192.168.111.181",
        "ELIE2": "192.168.111.182",
        "ELIE3": "192.168.111.183",
        "ELIE4": "192.168.111.184",
        "ELIE5": "192.168.111.185",
        "ELIE6": "192.168.111.186"
}

IP = LABDESK["ELIE1"]  # IP des Laborplatzes
rp_s = scpi.scpi(IP)


# %% Messung / Datenverarbeitung
TSTAMP = datetime.datetime.now()
DEVICE = {
    "d1": "1N4001",
    "d2": "1N4148",
    "npn": "2N3904",
    "pnp": "2N3906",
    "nmos": "BS170",
    "pmos": "BS250"
}


# Init Dataframes
DF_IN1 = pd.DataFrame()
DF_IN2 = pd.DataFrame()



# Konfiguration des Signalgenerators
func = 'TRIANGLE'  # Signalform (SINE, SQUARE, TRIANGLE)
ampl = 0.5  # Amplitude (-1 V ... 1 V)
freq = 1000  # Frequenz (0 Hz ... 62.5e6 Hz)
offset = 0.5  # Offset (-1 V ... 1 V)
t = np.linspace(0, 2.097e-3, 16384)  # Skalierung der Zeitachse (Sampling)


rp_s.tx_txt('GEN:RST')  # Signal Generator reset
rp_s.tx_txt('SOUR1:FUNC ' + str(func))  # Wellenform
rp_s.tx_txt('SOUR1:VOLT ' + str(ampl))  # Amplitude
rp_s.tx_txt('SOUR1:VOLT:OFFS ' + str(offset))  # Offset
rp_s.tx_txt('SOUR1:FREQ:FIX ' + str(freq))  # Frequenz
rp_s.tx_txt('OUTPUT1:STATE ON')  # Output
rp_s.tx_txt('SOUR1:TRIG:INT')

time.sleep(1)  # in Sekunden


# Trigger
rp_s.tx_txt('ACQ:RST ')  # Input reset
rp_s.tx_txt('ACQ:DEC 16')  # Decimation (1, 8, 16, 64, 1024, 8192)
rp_s.tx_txt('ACQ:AVG ON')  # Averaging (OFF, ON)
rp_s.tx_txt('ACQ:TRIG:LEV 0.5')  # Trigger level
rp_s.tx_txt('ACQ:TRIG:DLY 8192')  # Delay
rp_s.tx_txt('ACQ:START')  # Start der Messung
rp_s.tx_txt('ACQ:TRIG NOW')  # Trigger setzen


for meas in range(0, 4):

    # Input IN1
    time.sleep(0.1)  # in seconds
    rp_s.tx_txt('ACQ:SOUR1:DATA?')  # Readout buffer IN1
    IN1str = rp_s.rx_txt()
    IN1str = IN1str.strip('{}\n\r').replace("  ", "").split(',')
    IN1 = np.array(list(map(float, IN1str)))
    DF_IN1[str(meas)] = IN1

    # Input IN2
    time.sleep(0.1)  # in seconds
    rp_s.tx_txt('ACQ:SOUR2:DATA?')  # Readout buffer IN2
    IN2str = rp_s.rx_txt()
    IN2str = IN2str.strip('{}\n\r').replace("  ", "").split(',')
    IN2 = np.array(list(map(float, IN2str)))
    DF_IN2[str(meas)] = IN2


# Stopp des Generators
rp_s.tx_txt('OUTPUT1:STATE OFF')


# %% Daten als Datei speichern
Data_IN1 = 'data/IN1_' + DEVICE["d1"] + "_ELIE1"  # + str(TSTAMP.strftime('_%Y-%m-%d_%H-%M'))
Data_IN2 = 'data/IN2_' + DEVICE["d1"] + "_ELIE1"  # + str(TSTAMP.strftime('_%Y-%m-%d_%H-%M'))


# %% Speichern als CSV/TSV (comma/tab-seperated-values)
DF_IN1.to_csv(Data_IN1 + '.csv', index=False)
DF_IN2.to_csv(Data_IN2 + '.csv', index=False)

# %% Speichern als Excel-Worksheet
# with pd.ExcelWriter(Data_IN + '.xlsx') as writer:
#     DF_IN1.to_excel(writer, sheet_name='IN1', index=False)
#     DF_IN2.to_excel(writer, sheet_name='IN2', index=False)

# DF_IN1.to_excel(Data_IN1 + '.xlsx', index=False)
# DF_IN2.to_excel(Data_IN2 + '.xlsx', index=False)

# %% Speichern als Apache parquet
DF_IN1.to_parquet(Data_IN1 + ".parquet", index=False)
DF_IN2.to_parquet(Data_IN2 + ".parquet", index=False)
