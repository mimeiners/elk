# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## Post-processing der LTspice Simulationsdaten

# %%
import ltspice
import matplotlib.pyplot as plt

# %% [markdown]
# ## LTspice als Batch-Job in der Shell/CMD ausführen
# Der Aufruf "!LTspice" muss je Betriebssystem angepasst werden!

# %%
# !LTspice -b Transistor-Thermometer.cir

# %% [markdown]
# ## Laden der raw LTspice-Datei in die Python-Arbeitsumgebung

# %%
file = "./Transistor-Thermometer.raw"
raw = ltspice.Ltspice(file)
raw.parse()
raw.getVariableNames()

# %% [markdown]
# ## Extraktion von Temperatur und Spannungen

# %%
T = raw.get_data('temperature')
v_a = raw.get_data('V(va)')
v_c = raw.get_data('V(vc)')
v_p = raw.get_data('V(vp)')

# %% [markdown]
# ## Plots

# %%
plt.xlabel(r'Temperatur T in $^{\circ}$C')
plt.ylabel('Spannung in V')
plt.plot(T, v_a, label=r'$v_{a}(T)$')
plt.plot(T, v_c, label=r'$v_{c}(T)$')
plt.plot(T, v_p, label=r'$v_{p}(T)$')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# %%
