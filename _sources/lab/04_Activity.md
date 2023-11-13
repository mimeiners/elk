<!-- !split -->
<!-- jupyter-book 04_Activity.md -->
# Der MOSFET als Diode

<div id="proj:mosfet"></div>

### Zielsetzung

Ziel dieses Versuches ist die Untersuchung der Strom- und Spannungscharakteristik von
n-Kanal und p-Kanal MOS Feldeffekttransistoren (kurz nMOS und pMOS), die jeweils als Diode geschaltet sind. 

*Notice.* 
Die STEMlab-Ausgänge können Spannungssignale mit einem maximalen Ausgangsbereich von $\pm$ 1 V (2 Vpp) erzeugen. Für
diesen Versuch werden höhere Signalamplituden benötigt. Aus diesem Grund wird wieder ein OP27 als invertierenden
Verstärker benötigt, um die Signalverstärkung von OUT1 und OUT2 für einen Spannungshub von +4,7V bis -3,2V zu
erreichen. Ein OP27 wird vom STEMlab über die +5 V und -3.3 V Spannungsschienen versorgt. Der Verstärkungfaktor des
invertierenden Verstärkers wird auf $\approx$ 5 gesetzt, wobei $R_1$ = 2,2 k $\Omega$ und $R_2$ = 10 k $\Omega$ eingesetzt
werden.



### Materialien

* Red Pitaya STEMlab
* OP27 Operationsverstärker
* 1 $k\Omega$ Widerstand
* BS170 Kleinsignal-nMOS-Transistor
* BS250 Kleinsignal-pMOS-Transistor
* Platine

### nMOS als Diode

Die Schaltung des nMOS in Diodenkonfiguration ist in [Figure](23_fig_02.html#23_fig_02) gezeigt. In Diodenkonfiguration arbeitet
ein nMOS vergleichbar zu einem npn-Transistor. 

Die Schwellspannung (Threshold Voltage, $V_{Tn,p}$, $V_{th}$, $V_{TH}$) liegt nicht zwingend bei $\approx$ 0,7 V wie bei
einem Bipolartransistor. Bei einem unipolaren Transistor hängt sie von der Technologie und der Kanalgröße des
Transistors ab. Für den ausgewählten nMOS-Transistor liegt die Schwellenspannung $V_{Tn}$ bei etwa 2,0 V nominal.
Das bedeutet, wenn die vom Gate-Kontakt zum Source-Kontakt anliegende Spannung ($V_{GS}$) die Schwellspannung $V_{Tn}$
überschreiten, schaltet der nMOS Transistor ein und beginnt zu leiten. Da bei der Diodenkonfiguration des nMOS sein
Drain-Kontakt schalttechnisch mit seinem Gate-Kontakt verbunden ist, ist die Drain-Source-Spannung gleich der
Gate-Source-Spannung. 

*Hint.* 
Diese Konfiguration des nMOS erzeugt effektiv eine Diode mit einer Durchlaßspannung, die der Schwellenspannung $V_{Tn}$
entspricht.



<!-- <img src="../fig/Activity_23_Fig_01a.png" width="400"><p><em>BS170 Spezifikation. <div id="23_fig_01"></div></em></p> -->
![<p><em>BS170 Spezifikation. <div id="23_fig_01"></div></em></p>](../fig/Activity_23_Fig_01a.png)

Auf dem Steckbrett die Schaltung aus [Figure](23_fig_02.html#23_fig_02) aufbauen und mit den Messungen fortfahren.

<!-- <img src="../fig/Activity_23_Fig_02.png" width="400"><p><em>Anschlussdiagramm nMOS-Messung. <div id="23_fig_02"></div></em></p> -->
![<p><em>Anschlussdiagramm nMOS-Messung. <div id="23_fig_02"></div></em></p>](../fig/Activity_23_Fig_02.png)

### Verfahren

Für Sie ist die Schaltung aus [Figure](23_fig_01.html#23_fig_01) auf einer Platine aufgebaut; $R_1$ = 2,2 k $\Omega$,
$R_2$ = 10 k $\Omega$ und $R_3$ = 1 k $\Omega$, Transistor M1 ist der nMOS Transistor vom Typ BS170.


<!-- <img src="../fig/Activity_23_Fig_03a.png" width="400"><p><em>nMOS-Schaltung auf der Platine. <div id="23_fig_03"></div></em></p> -->
![<p><em>nMOS-Schaltung auf der Platine. <div id="23_fig_03"></div></em></p>](../fig/Activity_23_Fig_03a.png)

*Warning.* 
Bevor Sie die Schaltung an die STEMlab-Pins -3,3 V und +3,3 V anschließen, überprüfen Sie Ihre Schaltung nochmal. Die
Spannungsversorgungsstifte -3,3 V und +3,3 V haben keine Schutzschaltung und können im Falle eines Kurzschlusses
beschädigt werden.



* Starten Sie die Oszilloskop und Signalgenerator-App
* Stellen Sie im Menü OUT1-Einstellungen den Amplitudenwert auf 0,45 V, den DC-Offset auf -0,45 V und die Frequenz auf 1 kHz ein, um die Eingangsspannung anzulegen. Wählen Sie im Wellenform-Menü TRIANGLE, deaktivieren Sie SHOW und wählen Sie ENABLE.
* Stellen Sie sicher, dass IN1, IN2 und MATH V/div auf der linken unteren Seite des Bildschirms auf 1 V/div eingestellt sind (Sie können V/div einstellen, indem Sie den gewünschten Kanal auswählen und mit dem vertikalen +/- Regler einstellen).
* Setzen Sie t/div Wert auf 200 us/div (Sie können t/div mit dem horizontalen +/- Reglern einstellen).
* Stellen Sie unter MATH-Kanaleinstellungen IN1-IN2 ein und wählen Sie ENABLE.
* Stellen Sie unter den Menueinstellungen IN1 und IN2 den Messtaster auf x10 und den vertikalen Offset auf 0.
* Stellen Sie unter Einstellungen des MATH-Menüs den vertikalen Offset auf 0 ein.
* Stellen Sie unter TRIGGER-Einstellungen den Triggerpegel auf 1 V ein

<!-- <img src="../fig/Activity_23_Fig_04.png" width="400"><p><em>nMOS Diodenmessung. <div id="23_fig_04"></div></em></p> -->
![<p><em>nMOS Diodenmessung. <div id="23_fig_04"></div></em></p>](../fig/Activity_23_Fig_04.png)

### IV-Kurvenmessungen

Da sich ein nMOS wie eine Diode mit einer Durchlaßspannung entsprechend der $V_{Tn}$ verhalten kann (Konfiguration in
[Figure](23_fig_02.html#23_fig_02)), können sie die IV-Charakteristik wie bei der Diodenschaltung messen. Sie können die
Oszilloskop-App, ein Jupyter Notebook oder ein SCPI-Skript verwenden.

Wie Sie Jupyter Notebook starten und ein neues Projekt erstellen, ist in [Figure](23_fig_05.html#23_fig_05) dargestellt. 

k
<!-- <img src="../fig/Activity_19_Fig_07.png" width="400"><p><em>Erstellen eines neuen Jupyter Notbooks. <div id="23_fig_05"></div></em></p> -->
![<p><em>Erstellen eines neuen Jupyter Notbooks. <div id="23_fig_05"></div></em></p>](../fig/Activity_19_Fig_07.png)

Wenn Sie erfolgreich ein neues Jupyter Notebook erstellt haben, kopieren Sie den untenstehenden Code und führen Sie ihn aus.

Der unten stehende Code erzeugt das gleiche Signal wie in [Figure](23_fig_04.html#23_fig_04), aber er plotet dieses in einem XY-Diagramm.

Für die Messung der IV-Kurve ist ein XY-Plot erforderlich, wobei die x-Achse die Diodenspannung $IN_2$ und die y-Achse
den Diodenstrom (Drainstrom) ) $I_D = (IN_1 - IN_2)/R_3$ darstellen. 

Kopieren Sie den unten stehenden Code in Zelle 1:


~~~{.Python}
# Import libraries
from redpitaya.overlay.mercury import mercury as overlay
from bokeh.io import push_notebook, show, output_notebook
from bokeh.models import HoverTool, Range1d, LinearAxis, LabelSet, Label
from bokeh.plotting import figure, output_file, show
from bokeh.resources import INLINE
output_notebook(resources=INLINE)
import numpy as np

# Initialize fpga modules
fpga = overlay()
gen0 = fpga.gen(0)
osc = [fpga.osc(ch, 1.0) for ch in range(fpga._MNO)]

# Configure OUT1 generator channel
gen0.amplitude = 0.45
gen0.offset = -0.45
gen0.waveform = gen0.sawtooth(0.5)
gen0.frequency = 1000
gen0.start()
gen0.enable = True
gen0.trigger()

# Resistor value
R3 = 1000

# Configure IN1 and IN2 oscilloscope input channels
for ch in osc:
    ch.filter_bypass = True

    # data rate decimation
    ch.decimation = 10

    # trigger timing [sample periods]
    N = ch.buffer_size
    ch.trigger_pre = 0
    ch.trigger_post = N

    # osc0 is controlling both channels
    ch.sync_src = fpga.sync_src["osc0"]
    ch.trig_src = fpga.trig_src["osc0"]

    # trigger level [V], edge ['neg', 'pos'] and holdoff time [sample periods]
    ch.level = 0.01
    ch.edge = 'pos'
    ch.holdoff = 0

    
# Initialize diode current and voltage
V = np.zeros(N)
I = np.zeros(N)

# Plotting
hover = HoverTool(mode='vline', tooltips=[("V", "@x"), ("I", "@y")])
tools = "wheel_zoom, box_zoom, reset,pan"
p = figure(plot_height=500,
           plot_width=900,
           title="XY Plot der NMOS Transistor IV Charakteristik",
           toolbar_location="right",
           tools=(tools, hover))
p.xaxis.axis_label = 'Spannung in V'
p.yaxis.axis_label = 'Strom in mA'
r = p.line(V, I, line_width=1, line_alpha=0.7, color="blue")

# get and explicit handle to update the next show cell
target = show(p, notebook_handle=True)
~~~

Erstelle eine neue Zelle (Einfügen -> Zelle darunter) und kopieren Sie den unten stehenden Code.


~~~{.Python}
# Measuring I, V and re-plotting
while True:
    # reset and start
    osc[0].reset()
    osc[0].start()

    # wait for data
    while (osc[0].status_run()):
        pass

    V0 = osc[0].data(N-100)*10  # IN1 signal
    V1 = osc[1].data(N-100)*10  # IN2 signal
    I = ((V0-V1)/R3)*1E3        # 1E3 convert to mA
    r.data_source.data['x'] = V0
    r.data_source.data['y'] = I
    push_notebook(handle=target)
~~~

Führen Sie Zelle 1 und Zelle 2 aus. Hinweis Zelle 2 ist eine Hauptschleife für die Erfassung und Neuaufnahme. Wenn Sie
die Erfassung stoppen, führen Sie einfach nur Zelle 2 aus, um die Messungen erneut zu starten.

Nach dem Ausführen der Jupyter Notebook Zelle sollten Sie die IV-Charakteristik der Diode erhalten, wie in [Figure](23_fig_06.html#23_fig_06) dargestellt.

<!-- <img src="../fig/Activity_23_Fig_06.png" width="400"><p><em>nMOS IV-Kennlinie gemessen mit Jupyter Notebook. <div id="23_fig_06"></div></em></p> -->
![<p><em>nMOS IV-Kennlinie gemessen mit Jupyter Notebook. <div id="23_fig_06"></div></em></p>](../fig/Activity_23_Fig_06.png)


### pMOS als Diode

Die selben Messungen können auch mit einem pMOS-Transistor durchgeführt werden. Beim pMOS-Transistor wird allerdings die
Polarität der Spannung umgekehrt, so dass die Konfiguration der pMOS-Diode anders sein muss als bei einem nMOS. 
Die Konfiguration der pMOS-Diode ist in [Figure](23_fig_07.html#23_fig_07) dargestellt.

<!-- <img src="../fig/Activity_23_Fig_07.png" width="400"><p><em>pMOS Anschlussdiagramm. <div id="23_fig_07"></div></em></p> -->
![<p><em>pMOS Anschlussdiagramm. <div id="23_fig_07"></div></em></p>](../fig/Activity_23_Fig_07.png)

### Verfahren

Für Sie ist die Schaltung aus [Figure](23_fig_07.html#23_fig_07) auf einer Platine aufgebaut; $R_1$ = 2,2 k $\Omega$, $R_2$ = 10 k $\Omega$
und für $R_3$ = 1 k $\Omega$, der Transistor M1 ist ein pMOS Transistor vom Typ BS250.

*Warning.* 
Bevor Sie die Schaltung an die STEMlab-Pins -3,3V und +3,3V anschließen, überprüfen Sie Ihre Schaltung nochmal. Die
Spannungsversorgungsstifte -3,3V und +3,3V haben keine Schutzschaltung und können im Falle eines Kurzschlusses
beschädigt werden.




* Starten Sie die Anwendung Oszilloskop und Signalgenerator-App
* Stellen Sie im Menü OUT1-Einstellungen den Amplitudenwert auf 0,45 V, den DC-Offset auf -0,45 V und die Frequenz auf 1 kHz ein, um die Eingangsspannung anzulegen. Wählen Sie im Wellenform-Menü TRIANGLE, deaktivieren Sie SHOW und wählen Sie ENABLE. 
* Stellen Sie sicher, dass IN1 und IN2 auf der linken unteren Seite des Bildschirms auf 1 V/div eingestellt sind (V/div kann im gewünschten Kanal mit den vertikalen +/- Butten einstellt werden) und MATH auf 0.5 V/div.
* Setzen Sie t/div Wert auf 200 us/div (t/div wird mit den horizontalen +/- Button eingestellt).
* Stellen Sie unter MATH-Kanaleinstellungen die Differenz IN1-IN2 ein und wählen Sie ENABLE.
* Stellen Sie unter den Menueinstellungen IN1 und IN2 den Messtaster auf x10 und den vertikalen Offset auf 0.
* Stellen Sie unter Einstellungen des MATH-Menüs den vertikalen Offset auf 0 ein.
* Stellen Sie unter TRIGGER-Einstellungen den Triggerlevel auf 4 V ein.

<!-- <img src="../fig/Activity_23_Fig_08.png" width="400"><p><em>pMOS Diodenmessung.  <div id="23_fig_08"></div></em></p> -->
![<p><em>pMOS Diodenmessung.  <div id="23_fig_08"></div></em></p>](../fig/Activity_23_Fig_08.png)

Wie in [Figure](23_fig_08.html#23_fig_08) zu sehen, verhält sich der pMOS in der Diodenkonfiguration wie eine Diode mit einer
Durchlaßspannung gleich der pMOS Schwellenspannung $V_{Tp}$.

Vergleichen Sie [Figure](23_fig_08.html#23_fig_08) mit [Figure](23_fig_04.html#23_fig_04) und versuchen Sie, den Unterschied zwischen nMOS- und
pMOS-Diodenkonfigurationen zu erklären.


