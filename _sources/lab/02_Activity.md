<!-- !split -->
<!-- jupyter-book 02_Activity.md -->


# Dioden IV-Charakterisierung

<div id="proj:diode"></div>

### Zielsetzung
<div id="sec:zielsetzung"></div>
Ziel dieser Übung ist es, Strom- und Spannungseigenschaften zwei verschiedener Silizium-Diode vom Typ 1N4001 und 1N4148 zu
untersuchen. Parallel zu Messungen am Red Pitaya STEMlab muss die Schaltung vollständig in LTSpice simuliert werden, so
dass die Messdaten aus dem STEMLab auf dem eigenen Rechner validiert werden können.

*Hinweis.*
In diesem Laborversuch wird die Terminologie aus der [Dokumentation](https://redpitaya.readthedocs.io/en/latest/index.html)
verwendet, wenn es um Verbindungen zum 
[Red Pitaya STEMlab](https://redpitaya.readthedocs.io/en/latest/developerGuide/hardware/125-14/top.html) geht.

Die Erweiterungsstecker-Pins für die Spannungsversorgung -3.3 V und +3.3 V sind in der
[Dokumentation](https://redpitaya.readthedocs.io/en/latest/developerGuide/hardware/125-14/extent.html)
dargestellt.

Die [Oszilloskop und Signalgenerator App](https://redpitaya.readthedocs.io/en/latest/appsFeatures/applications/oscSigGen/osc.html)
wird zum Erzeugen und Beobachten von Signalen in der Schaltung verwendet, wenn der Web-Server des STEMLab's aktiviert
ist.

### Hintergrund
<div id="sec:hintergrund"></div>

Eine Halbleiterdiode ist ein elektronisches Bauelement, welches häufig in Schaltungsanwendungen, bei denen der Strom nur
in eine Richtung fliessen darf, als Gleichrichtung eingesetzt wird.

Wenn die Diode aus Silizium hergestellt wird, liegt die Durchlaßspannung typischerweise bei $\approx$ 0.7 V und die
IV-Charakteristik im Bezug auf Diodenstrom und -spannung kann durch eine exponentielle Beziehung beschrieben werden:

<div id="19_eq_01"></div>
$$
\begin{equation}
I_D = I_S \left( e^{\frac{V_D }{N V_T}} - 1 \right)
\end{equation}
$$

wobei $I_{S}$ der Sättigungssperrstrom ist und $N$ ein Skalierungsfaktoren (Emissionskoeffizient), $V_T = kT / q$ ist
die sogenannte thermische Spannung und beträgt 25,4 mV bei Raumtemperatur ($T$=300 K). 

### Schematische Symbole der Diode

Jeder Diodentyp hat ein spezifisches Schaltsymbol, welches vom herkömmlichen Diodensymbol der Siliziumdiode abgeleitet
ist, [Figure](19_fig_01.html#19_fig_01). Eine etwa "Z"-förmige Kathode bezeichnet eine Zener-Diode, wie im zweiten Symbol von links
in [Figure](19_fig_01.html#19_fig_01) zu sehen ist. Eine "S"-förmige Kathode bezeichnet eine Schottky-Diode und Pfeile, die von der
Diode wegzeigen, kennzeichnen eine LED (engl. Light Emitting Diode), wie im rechten Symbol dargestellt. Pfeile, die auf
die Diode zeigen, kennzeichnen eine Photodiode. 

<!-- <img src="../fig/Activity_19_Fig_01a.png" width="400"><p><em>Diodensymbole. <div id="19_fig_01"></div></em></p> -->
![<p><em>Diodensymbole. <div id="19_fig_01"></div></em></p>](../fig/Activity_19_Fig_01a.png)

### Materialien

* Red Pitaya STEMlab
* 10 $\Omega$ Widerstand
* Diode 1N4148
* Diode 1N4001
* Platine

### pn-Übergangsdiode IV-Charakteristik

Die Strom-/Spannungseigenschaften der pn-Übergangsdiode können mit dem STEMlab und den folgenden in [Figure](19_fig_04.html#19_fig_04)
dargestellten Anschlüssen gemessen werden. Richten Sie die Steckplatine mit dem Generator OUT1-Kanalausgang an einem
Ende des Widerstandes ein. Das andere Ende des Widerstandes ist mit einem Ende der zu messenden Diode verbunden, wie im
Diagramm dargestellt. Die Eingangskanäle IN1 und IN2 sind ebenfalls unterschiedlich angeschlossen, daher werden
Diodenstrom und -spannung:

$$
\begin{align}
I_D &= (IN_1 - IN_2) / R_1 \\
V_D &= IN_2
\end{align}
$$

<!-- <img src="../fig/Activity_19_Fig_04a.png" width="400"><p><em>Anschlussplan für Dioden IV-Kurven. <div id="19_fig_04"></div></em></p> -->
![<p><em>Anschlussplan für Dioden IV-Kurven. <div id="19_fig_04"></div></em></p>](../fig/Activity_19_Fig_04a.png)

Zur Messung der Strom- und Spannungseigenschaften einer pn-Übergangsdiode sollte der OUT1-Generator als 1 kHz-Dreieckssignal
mit einer maximalen Amplitude von 1 V und einer minimalen Amplitude von 0 V konfiguriert werden. Für die Messung der
IV-Kurve ist ein zweidimensionaler (xy) Graph (Plot) erforderlich, wobei die x-Achse die Diodenspannung IN2 und die
y-Achse den Diodenstrom $I_D=(IN1-IN2)/R1$ darstellen.

*Warning.* 
BITTE NIEMALS UNTERSCHIEDLICHE ZUGRIFFSARTEN PARALLEL VERWENDEN.

Deaktivieren Sie die Oszilloskop-App (OFF-Button), bevor Sie den Zugriff mit Jupyter Notebook oder SCPI erproben.



### Zeitbereichsmessungen

<!-- <img src="../fig/Activity_19_Fig_05a.png" width="400"><p><em>Verbindungen auf dem Steckbrett. <div id="19_fig_05"></div></em></p> -->
![<p><em>Verbindungen auf dem Steckbrett. <div id="19_fig_05"></div></em></p>](../fig/Activity_19_Fig_05a.png)

* Die Schaltung aus [Figure](19_fig_04.html#19_fig_04) ist für Sie auf einer Platine aufgebaut und angeschlossen.
* Starten Sie die Oszilloskop- und Signalgenerator-App auf einem Red Pitaya.
* Stellen Sie im Menü OUT1-Einstellungen den Amplitudenwert auf 0,5 V und den DC-Offset auf 0,5 V ein, um ein Dreieckssignal als Eingangsspannung anzulegen. Im Waveform-Menü das Signal "TRIANGLE" auswählen und den Ausgang mit "ON" aktivieren. Der "SHOW"-Button dient zum Anzeigen des Signals in der Oszilloskop-App.
* Stellen Sie sicher, dass sowohl IN1 V/div als auch IN2 V/div am linken unteren Bildschirmrand auf 200 mV/div eingesetellt sind. V/div können Sie im jeweiligen Kanal über die +/- Schaltflächen rechts unten kontrollieren.
* Setzen Sie den t/div-Wert auf 200 us/div. Auch hier können Sie t/div mit den +/- Schaltflächen einstellen.
* Im Menü "MATH settings" die Differenz IN1-IN2 einstellen und "enable" auswählen. Die mathematische Kurve skaliert mit dem Faktor R1 und stellt den Diodenstrom dar.

<!-- <img src="../fig/Activity_19_Fig_06.png" width="400"><p><em>Spannung und Strom einer Siliziumdiode (zeitabhängig). <div id="19_fig_06"></div></em></p> -->
![<p><em>Spannung und Strom einer Siliziumdiode (zeitabhängig). <div id="19_fig_06"></div></em></p>](../fig/Activity_19_Fig_06.png)

Aus [Figure](19_fig_06.html#19_fig_06) kann man sehen, dass die Diode zu leiten beginnt, wenn die Diodenspannung die
Schwellenspannung von ca. 0.7 V erreicht.  

Außerdem sollte der mit "MATH-Trace" dargestellte Diodenstrom beobachtet werden. Man sollte deutlich erkennen, dass der
Diodenstrom 0 A beträgt, sobald die Diodenspannung unter 0.7 V liegt. Ab einem Zeitpunkt, ab dem die Diodenspannung
$> 0.7\,\text{V}$ ist, beginnt die Diode zu leiten und der Pfadstrom wird nur durch den Widerstand $R_1$ begrenzt.

### Vorgehensweise - Messung der I/V-Charakteristik

Für diese Aufgabe verwenden Sie die Steuerung des STEMLabs mittels SCPI-Server und Python aus dem VPN der Hochschule am zugewiesenen
Laborplatz.

Die IP-Adressen der STEMLabs:

* Laborplatz ELIE1: 192.168.111.181
* Laborplatz ELIE2: 192.168.111.182
* Labroplatz ELIE3: 192.168.111.183
* Laborplatz ELIE4: 192.168.111.184
* Laborplatz ELIE5: 192.168.111.185
* Laborplatz ELIE6: 192.168.111.186

Die Web-Adressen der STEMLabs:

* [Laborplatz ELIE1](http://elie1redpi.fk4.hs-bremen.de)
* [Laborplatz ELIE2](http://elie2redpi.fk4.hs-bremen.de)
* [Labroplatz ELIE3](http://elie3redpi.fk4.hs-bremen.de)
* [Laborplatz ELIE4](http://elie4redpi.fk4.hs-bremen.de)
* [Laborplatz ELIE5](http://elie5redpi.fk4.hs-bremen.de)
* [Laborplatz ELIE6](http://elie6redpi.fk4.hs-bremen.de)

