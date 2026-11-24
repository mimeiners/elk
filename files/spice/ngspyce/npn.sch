v {xschem version=3.4.6 file_version=1.2}
G {}
K {}
V {}
S {}
E {}
N 5300 -4670 5400 -4670 {lab=Vc }
N 5220 -4620 5250 -4620 {lab=Vb }
C {npn-1.sym} 5250 -4570 0 0 {name=Q1
device=NPN_TRANSISTOR
model-name=QBC337AP
}
C {gnd-1.sym} 5290 -4540 0 0 {}
C {gnd-1.sym} 5390 -4520 0 0 {}
C {gnd-1.sym} 5210 -4470 0 0 {}
C {vdc-1.sym} 5370 -4550 0 0 {name=Vcc
device=VOLTAGE_SOURCE
footprint=none
value=DC\\\\ 10V
}
C {spice-include-1.sym} 5300 -4450 0 0 {name=A1
device=include
file=bc337.cir
}
C {vdc-1.sym} 5250 -4500 0 1 {name=Vbb
device=VOLTAGE_SOURCE
footprint=none
value=DC\\\\ 0V
}
C {lab_wire.sym} 5400 -4670 0 1 {lab=Vc }
C {lab_wire.sym} 5220 -4620 0 1 {lab=Vb }
