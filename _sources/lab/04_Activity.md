<!-- !split -->
<!-- jupyter-book 04_Activity.md -->
# Der MOSFET als Diode

<div id="proj:mosfet"></div>

### Zielsetzung

Ziel dieses Versuches ist die Untersuchung der Strom- und Spannungscharakteristik von
n-Kanal und p-Kanal MOS Feldeffekttransistoren (kurz nMOS und pMOS), die jeweils als Diode geschaltet sind. 

*Notice.* 
Die STEMlab-Ausgänge können Spannungssignale mit einem maximalen Ausgangsbereich von $\pm$ 1 V (2 Vpp) erzeugen. Für
diesen Versuch werden höhere Signalamplituden benötigt. Aus diesem Grund wird wieder ein OP484 als invertierenden
Verstärker benötigt, um die Signalverstärkung von OUT1 und OUT2 für einen Spannungshub von +4,7V bis -3,2V zu
erreichen. Ein OP484 wird vom STEMlab über die +5 V und -3.3 V Spannungsschienen versorgt. Der Verstärkungfaktor des
invertierenden Verstärkers wird auf $\approx$ 5 gesetzt, wobei $R_1$ = 2,2 k $\Omega$ und $R_2$ = 10 k $\Omega$ eingesetzt
werden.



### Materialien

* Red Pitaya STEMlab
* OP484 Quad-Rail-to-Rail-Operationsverstärker
* 1 k $\Omega$ Widerstand
* Kleinsignal-nMOS-Transistor (BS170)
* Kleinsignal-pMOS-Transistor (BS250)
* Platine

### nMOS als Diode

Die Schaltung des nMOS in Diodenkonfiguration ist in [Figure](23_fig_02.html#23_fig_02) gezeigt. In Diodenkonfiguration arbeitet
ein nMOS vergleichbar zu einem npn-Transistor. 

Die Schwellspannung (Threshold Voltage, $V_{Tn,p}, V_{th}, V_{TH}$) liegt nicht zwingend bei $\approx$ 0,7 V wie bei
einem Bipolartransistor. Bei einem unipolaren Transistor hängt sie von der Technologie und der Kanalgröße des
Transistors ab. Für den ausgewählten nMOS-Transistor liegt die Schwellenspannung $V_{Tn}$ bei etwa 2,0 V nominal.
Das bedeutet, wenn die vom Gate-Kontakt zum Source-Kontakt anliegende Spannung ($V_{GS}$) die Schwellspannung $V_{Tn}$
überschreiten, schaltet der nMOS Transistor ein und beginnt zu leiten. Da bei der Diodenkonfiguration des nMOS sein
Drain-Kontakt schalttechnisch mit seinem Gate-Kontakt verbunden ist, ist die Drain-Source-Spannung gleich der
Gate-Source-Spannung. 

*Hint.* 
Diese Konfiguration des nMOS erzeugt effektiv eine Diode mit einer Durchlassspannung, die der Schwellenspannung $V_{Tn}$
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

Da sich ein nMOS wie eine Diode mit einer Durchlassspannung entsprechend der $V_{Tn}$ verhalten kann (Konfiguration in
[Figure](23_fig_02.html#23_fig_02)), können wir ihre IV-Charakteristik wie bei der pn-Diodenschaltung messen. Führen Sie wie im
entsprechenden Experiment beschrieben die Messungen mit angepassten SCPI-Skripten durch.




<!-- <img src="../fig/Activity_23_Fig_06.png" width="400"><p><em>nMOS IV-Kennlinie gemessen mit Jupyter Notebook. <div id="23_fig_06"></div></em></p> -->
![<p><em>nMOS IV-Kennlinie gemessen mit Jupyter Notebook. <div id="23_fig_06"></div></em></p>](../fig/Activity_23_Fig_06.png)


### pMOS als Diode

Die selben Messungen können auch mit einem pMOS-Transistor durchgeführt werden. Beim pMOS-Transistor wird allerdings die
Polarität der Spannung umgekehrt, so dass die Konfiguration der pMOS-Diode anders sein muss als bei der nMOS. 
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
* Stellen Sie sicher, dass IN1, IN2 und MATH V/div auf der linken unteren Seite des Bildschirms auf 1 V/div eingestellt sind (V/div kann im gewünschten Kanal mit den vertikalen +/- Butten einstellt werden).
* Setzen Sie t/div Wert auf 200 us/div (t/div wird mit den horizontalen +/- Button eingestellt).
* Stellen Sie unter MATH-Kanaleinstellungen die Differenz IN1-IN2 ein und wählen Sie ENABLE.
* Stellen Sie unter den Menueinstellungen IN1 und IN2 den Messtaster auf x10 und den vertikalen Offset auf 0.
* Stellen Sie unter Einstellungen des MATH-Menüs den vertikalen Offset auf 0 ein.
* Stellen Sie unter TRIGER-Einstellungen den Triggerpegel auf 1 V ein.

<!-- <img src="../fig/Activity_23_Fig_08.png" width="400"><p><em>pMOS Diodenmessung.  <div id="23_fig_08"></div></em></p> -->
![<p><em>pMOS Diodenmessung.  <div id="23_fig_08"></div></em></p>](../fig/Activity_23_Fig_08.png)

Wie in [Figure](23_fig_08.html#23_fig_08) zu sehen, verhält sich der pMOS in der Diodenkonfiguration wie eine Diode mit einer
Durchlassspannung gleich der pMOS Schwellenspannung $V_{Tp}$.

Vergleichen Sie [Figure](23_fig_08.html#23_fig_08) mit [Figure](23_fig_04.html#23_fig_04) und versuchen Sie, den Unterschied zwischen nMOS- und
pMOS-Diodenkonfigurationen zu erklären.


