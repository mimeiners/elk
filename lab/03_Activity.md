<!-- !split -->
<!-- jupyter-book 03_Activity.md -->
# Der BJT als Diode

<div id="proj:bjt"></div>

### Zielsetzung

Der Zweck dieses Versuchs ist es, die Strom- und Spannungseigenschaften eines als Diode geschalteten Bipolartransistors
(engl. Bipolar Junction Transistor, BJT) zu untersuchen.

*Hinweise.*

Die für die Versorgungsspannungen von +5 V, -3,3 V und +3,3 V verwendeten Steckerstifte des STEMLab's sind
in der Dokumentation aufgeführt.

Die STEMlab-Ausgänge können Spannungssignale mit einem maximalen Ausgangsbereich von $\pm$ 1 V (2 Vpp) erzeugen. Für
diesen Versuch sind höhere Signalamplituden erforderlich. Aus diesem Grund wird ein Operationsverstärker (Opamp) als
invertierender Verstärker eingesetzt, um die Signale der Ausgänge OUT1 und OUT2 für einen Spannungshub von +4,7 V bis
-3,2 V zu verstärken. Der Opamp wird vom STEMlab aus mit +5 V und -3,3 V versorgt. Die Verstärkung des Opamps wird auf
$\approx$ 5 gesetzt, wobei $R_i$ = 2,2 k $\Omega$ und $R_f$ = 10 k $\Omega$.  

### Materialien

* Red Pitaya STEMlab
* OP484
* 1 k $\Omega$ Widerstand
* 10 k $\Omega$ Widerstand
* 2,2 k $\Omega$ Widerstand
* Kleinsignal npn-Transistor (2N3904)
* Kleinsignal pnp-Transistor (2N3906)
* Platine
* Labornetzteil

Ein npn-Transistor, der wie in [Figure](22_fig_01.html#22_fig_01) gezeigt angeschlossen ist, verhält sich wie eine Diode.
Dies kann durch die Verwendung der Oszilloskop- und Signalgenerator-App gezeigt werden.

<!-- <img src="../fig/Activity_22_Fig_01.png" width="400"><p><em>npn-Transistor als Diode. <div id="22_fig_01"></div></em></p> -->
![<p><em>npn-Transistor als Diode. <div id="22_fig_01"></div></em></p>](../fig/Activity_22_Fig_01.png)


*Hint.* 
Beachten Sie, dass die in [Figure](22_fig_01.html#22_fig_01) (links) gezeigte Verstärkerschaltung nicht das Hauptthema dieses
Versuchs ist. Diese Schaltung wird nur hinzugefügt, um das Signal OUT1 zu verstärken.

Von hier an können Sie den Punkt -5 $\times V_{OUT1}$ als Bezugspotenzial betrachten.



### Verfahren

Im Labor in Raum E 507 ist an jedem Messplatz eine Platine, wie in [Figure](22_fig_02.html#22_fig_02) gezeigt, an ein STEMlab
angeschlossen, wobei $R_1$ = 2,2 k $\Omega$, $R_2$ = 10 k $\Omega$ und $R_3$ = 1 k $\Omega$. 

<!-- <img src="../fig/Activity_22_Fig_02a.png" width="400"><p><em>Platine mit Transistorschaltung. <div id="22_fig_02"></div></em></p> -->
![<p><em>Platine mit Transistorschaltung. <div id="22_fig_02"></div></em></p>](../fig/Activity_22_Fig_02a.png)


* Starten Sie die Oszilloskop- und Signalgenerator-App
* Stellen Sie im Menü OUT1-Einstellungen den Amplitudenwert auf 0,8 V, den DC-Offset auf -0,12 V und die Frequenz auf 1 kHz ein, um die Eingangsspannung anzulegen. Wählen Sie im Wellenform-Menü TRIANGLE, deaktivieren Sie SHOW und wählen Sie ENABLE.
* Stellen Sie sicher, dass IN1, IN2 und MATH V/div auf der linken unteren Seite des Bildschirms auf 1 V/div eingestellt sind. Sie können V/div einstellen, indem Sie den gewünschten Kanal auswählen und die vertikalen +/- Button rechts unten verwenden. 
* Setzen Sie den t/div Wert auf 200 us/div. Sie können t/div mit den horizontalen +/- Button einstellen.
* Stellen Sie unter MATH-Kanaleinstellungen folgendes ein: IN1-IN2 und wählen Sie ENABLE.
* Stellen Sie unter den Menüeinstellungen IN1 und IN2 den Messtaster auf x10 und den vertikalen Offset auf 0.

<!-- <img src="../fig/Activity_22_Fig_03.png" widht="400"><p><em>npn-Transistor als Diode, Messungen. <div id="22_fig_03"></div></em></p> -->
![<p><em>npn-Transistor als Diode, Messungen. <div id="22_fig_03"></div></em></p>](../fig/Activity_22_Fig_03.png)


Aus [Figure](22_fig_03.html#22_fig_03) ist ersichtlich, dass der npn-Transistor in der in [Figure](22_fig_01.html#22_fig_01) gezeigten
Konfiguration sich wie eine Diode verhält. Vergleichen Sie die Ergebnisse mit den Diodenmessungen aus dem
Diodenversuch.

### IV-Kurvenmessungen

Da sich ein Bipolartransistor wie eine Diode verhalten kann (vgl. Konfiguration in [Figure](22_fig_01.html#22_fig_01)), können sie
die IV-Charakteristik genauso messen, wie es im pn-Diodenexperiment getan wird.




<!-- <img src="../fig/Activity_22_Fig_05.png" width="400"><p><em>BJT IV-Charakteristik gemessen mit Jupyter Notebook. <div id="22_fig_05"></div></em></p> -->
![<p><em>BJT IV-Charakteristik gemessen mit Jupyter Notebook. <div id="22_fig_05"></div></em></p>](../fig/Activity_22_Fig_05.png)

In [Figure](22_fig_05.html#22_fig_05) ist die in einer Diodenkonfiguration gemessene IV-Charakteristik eines BJT dargestellt.
Vergleichen sie diese Ergebnisse mit der IV-Charakteristik der pn-Diode. Es sollte eine Hysterese sichtbar sein.
Überlegen sie, warum Bipolartransistoren als Dioden verwendet werden sollen. 

7














