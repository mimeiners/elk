<!-- !split -->
<!-- jupyter-book 01_lec.md -->
# Einleitung

<div id="sec:intro"></div>
<!-- !split -->
### Lernziele des Moduls

* Einblicke in mikroelektronische Systeme
* Analyse und Funktion von Halbleiterbauelementen
  * Halbleiterphysik
  * Modellbildung
  * Netzwerkanalyse/-synthese

* Anwendung von SPICE in der Schaltungsentwicklung
 a. Spezifikation
 b. Partitionierung
 c. Design

* Einsatz von Entwicklungsboards, Embedded Systems (SoC)
  * STEMlab von [redpitaya](https://www.redpitaya.com)


<!-- !split -->
### Wissenschaftliches Rechnen / Datenwissenschaft
* [Python](https://www.anaconda.com/download/)
* [R Project](https://www.r-project.org) 
* [Matlab](http://de.mathworks.com/?requestedDomain=de.mathworks.com)
* [Gnu Octave](https://www.gnu.org/software/octave/)
* [Gnuplot](http://www.gnuplot.info) ([Gnuplotting](http://www.gnuplotting.org))
* [Command-line tools](http://jeroenjanssens.com/2013/09/19/seven-command-line-tools-for-data-science.html) 

<!-- !split -->
### Schaltungssimulation (SPICE)
* [LTspice Linear Technology](http://www.linear.com/designtools/software/)
* [TINA-TI SPICE-Based Analog Simulation Program](http://www.ti.com/tool/tina-ti) 
* [ngspice (open-source)](http://ngspice.sourceforge.net)
* [ELDO (Mentor Graphics)](https://www.mentor.com/products/ic_nanometer_design/analog-mixed-signal-verification/eldo/)
* [Spectre (Cadence)](https://www.cadence.com/content/cadence-www/global/en_US/home/tools/custom-ic-analog-rf-design/circuit-simulation/spectre-circuit-simulator.html)
* [HSPICE (Synopsys)](https://www.synopsys.com/tools/Verification/AMSVerification/CircuitSimulation/HSPICE/Pages/default.aspx)

<!-- !split -->
### Betriebssystem (OS) - Werkzeuge (Tools)
  * [Shell](https://en.wikipedia.org/wiki/Shell_%28computing%29)
    * [oh-my-zsh](https://ohmyz.sh),
    * [bash-it](https://bash-it.readthedocs.io/en/latest/)
    * [SSH (Secure Shell)](https://de.wikipedia.org/wiki/Secure_Shell)

  * [GIT (Versionskontrolle)](https://git-scm.com)
  * [Cygwin](https://cygwin.com)

<!-- !split -->
### Code Editoren
  * [Emacs](https://www.gnu.org/software/emacs/)
  * [Vim](https://www.vim.org)
  * [Notepad++](https://notepad-plus-plus.org) (Windows)
  * [Visual Studio Code](https://code.visualstudio.com)
  * [PyCharm](https://www.jetbrains.com/pycharm/)

<!-- !split -->
### Schreibst Du noch oder TeXst Du schon?
  * [MikTeX (Windows, MacOS, Linux)](https://miktex.org/)
  * [MacTeX (MacOS)](https://www.tug.org/mactex/)
  * [TeXLive (Linux)](http://tug.org/texlive/)

<!-- !split -->
### LaTeX Editoren
  * IDE's
    * [TeXStudio](http://www.texstudio.org)
    * [TeXMaker](http://www.xm1math.net/texmaker/)
    * [TeXWorks](http://www.tug.org/texworks/)

  * Kollaborative Frameworks
    * [ShareLaTeX, Online LaTeX](https://www.sharelatex.com/)
    * [CoCalc - Online LaTeX](https://cocalc.com/doc/latex-editor.html)


<!-- !split -->
### Literaturverwaltung und LaTeX
  * [Citavi im Detail > Titel exportieren > Export nach BibTeX](https://www1.citavi.com/sub/manual5/de/exporting_to_bibtex.html)
  * [RefWorks - Library Guide Univ. Melbourne](https://unimelb.libguides.com/c.php?g=565734\&p=3912294)
  * [Benutzerdefinierte BibTex-Keys mit Zotero | nerdpause](https://nerdpause.de/benutzerdefinierte-bibtex-keys-mit-zotero/)
  * [JabRef - Library Guide Univ. Melbourne](https://unimelb.libguides.com/c.php?g=565734\&p=3897117)
  * [EndNote - Library Guide Univ. Melbourne](https://unimelb.libguides.com/latexbibtex/endnote)

<!-- !split -->
### Laborarbeit

*Charakterisierung von Bauelementen.* 
* Dioden vom Typ 1N4001 und 1N4148
* Bipolartransistoren vom Typ 2N2222A, 2N2907A
* MOSFETs vom Typ BS170, BS250
* Simulation mit [SPICE](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html)
* [Messautomatisierung mit Red Pitaya](https://www.redpitaya.com)
* Technischer Bericht
  * Berichtsvorlage DIN A4 (Word/LaTeX ) [IEEE templates](https://www.ieee.org/conferences/publishing/templates.html)
  * Gruppen mit 2-3 Studierenden
  * Elektronische Abgabe als PDF in der AULIS-Gruppe



<!-- !split -->
### Inhalte der Laborarbeit

* Literaturrecherche in Fachjournalen, Fachforen (z.B. auf den Webseiten der Halbleiterhersteller) und der Bibliothek 
  * Aufbau einer Literaturdatenbank, z.B. mit [JabRef](http://www.jabref.org), [Citavi](https://www.suub.uni-bremen.de/literatur-verwalten/refworks/citavi/) oder Ähnliches

* Einarbeitung in den Red Pitaya
  * Systemkonfiguration
  * Programmierung mit Python

* Konzeptionierung der Bauteilcharakterisierung
  * Partitionierung des Messaufbaus (Funktionen erläutern)
  * Aufgabenaufteilung (Projektmanagement)

* Entwurf, Implementierung und Bewertung
  * SPICE-Modellierung und Simulation
  * Datenanalyse

* Entwicklungsbericht (Technischer Bericht)

<!-- !split -->
### Datenspeicherung (Data Science)

* Dateisystem mit Arbeitsordner für Unterlagen und Daten 
* Daten in Tabellenformat (ASCII file, CSV format)
* Daten in Excel (.xlsx ) oder OpenDocument (.ods)
* Daten in speziellen Formaten, z.B.:
  * mat-files HDF5 (Matlab, Gnu Octave, Python Pandas)
  * Pickle (Python Serialization)

* Daten in Datenbanken, z.B.:
  * SQL (MySQL/MariaDB, PostgreSQL, SQlite)
  * noSQL (MongoDB, LevelDB, RocksDB)


<!-- !split -->
### Analyse vs. Design

* Entgegen populärwissenschaftlicher Meinungen ist Schaltungsanalyse und Schaltungsentwurf keine "Schwarze Magie"
* Schaltungsanalyse
  * ist die Fähigkeit, Schaltungen in handhabbare Teile zu zerlegen
  * basierend auf einem einfachen, aber hinreichend genauen Modell
  * "Just-in-time" Modellierung – verwende kein komplexes Modell, so lange es nicht benötigt wird ...
  * eine Schaltung $\Rightarrow$ eine Lösung

* Schaltungsentwurf
  * ist die Fähigkeit der Schaltungssynthese auf Basis von Erfahrung und intensiver Analyse
  * eine Spezifikation  $\Rightarrow$ viele Lösungen
  * Entwurfspraktiken werden am besten durch’s "Selbermachen" ausgebildet – daher ein Entwurfsprojekt ...


<!-- !split -->
### Es war einmal ...

<!-- !bslidecell 00 0.45 -->
<!-- <img src="../fig/lec_vacuum_tube.png" width="400"><p><em>1906 die Elektronenröhre</em></p> -->
![<p><em>1906 die Elektronenröhre</em></p>](../fig/lec_vacuum_tube.png)
<!-- !eslidecell -->

<!-- !bslidecell 01 0.45 -->
<!-- <img src="../fig/lec_1st_transistor.png" width="400"><p><em>1947 der erste Transistor, Bell Labs Foto</em></p> -->
![<p><em>1947 der erste Transistor, Bell Labs Foto</em></p>](../fig/lec_1st_transistor.png)
<!-- !eslidecell -->

<!-- !split -->
### Damals und heute

<!-- !bslidecell 00 0.45 -->
<!-- <img src="../fig/lec_1st_ic_kilby.png" width="400"><p><em>1958 Jack Kilby's erster IC <div id="fig:kilbyic"></div></em></p> -->
![<p><em>1958 Jack Kilby's erster IC <div id="fig:kilbyic"></div></em></p>](../fig/lec_1st_ic_kilby.png)
<!-- !eslidecell -->

<!-- !bslidecell 01 0.45 -->
<!-- <img src="../fig/lec_modern_ic.png" width="400"><p><em>Moderner IC <div id="fig:modernic"></div></em></p> -->
![<p><em>Moderner IC <div id="fig:modernic"></div></em></p>](../fig/lec_modern_ic.png)
<!-- !eslidecell -->

<!-- !split -->
### Packungsdichten

<!-- !bslidecell 00 0.85 -->
<!-- <img src="../fig/lec_wafers.png" width="600"><p><em>Wafergenerationen <div id="fig:wafer"></div></em></p> -->
![<p><em>Wafergenerationen <div id="fig:wafer"></div></em></p>](../fig/lec_wafers.png)
<!-- !eslidecell -->

<!-- !split -->
### Moore'sches Gesetz

<!-- !bslidecell -->
[50 Jahre Moore's Gesetz](https://www.intel.com/content/www/us/en/silicon-innovations/moores-law-technology.html)

<!-- !eslidecell -->

<!-- !split -->
### Halbleiterherstellung (Infineon, Dresden)
<!-- !bslidecell 00 0.9 -->


<iframe width="854" height="480" src="https://www.youtube.com/embed/_Kj58yQ67KI" frameborder="0" allowfullscreen></iframe>

<!-- !eslidecell -->

<!-- !split -->
### FinFET (Intel)
<!-- !bslidecell 00 0.9 -->


<iframe width="854" height="480" src="https://www.youtube.com/embed/_VMYPLXnd7E" frameborder="0" allowfullscreen></iframe>

<!-- !eslidecell -->

<!-- !split -->
### TSMC Fab (Next Gen 7/5 nm)
<!-- !bslidecell 00 0.9 -->


<iframe width="854" height="480" src="https://www.youtube.com/embed/Hb1WDxSoSec" frameborder="0" allowfullscreen></iframe>

<!-- !eslidecell -->

<!-- !split -->
### Reiseaussichten

Dies ist der **Beginn eines Prozesses**,

besser noch, **eines Abenteuers**.

<!-- !split -->
### Reiseziele

* Mehr über Signale wissen, die in elektronischen Systemen verarbeitet werden.
* Schaltungsdiagramme lesen können.
* Wissen über grundlegende Blöcke eines Systems aneignen.
* Wissen, wie Transistoren arbeiten und in modernen integrierten Technologien hergestellt werden.
* Eigenarten der Modellierung mikroelektronischer Bauelemente und der physikalischen und chemischen Prinzipien im Herstellungsprozess kennenlernen.

<!-- !split -->
### Reisebedingungen

*Anwendung Ihres Werkzeugkastens.* 
* Grundlagen der Elektrotechnik/Physik
* Elektromagnetische Wellen
* Angewandte Mathematik und Systemtheorie
* Trainingswille
* Pioniergeist
* Spa{\ss}



*Schnallen Sie sich an, die Reise beginnt ...*

<!-- !split -->
### Systemhierarchie

<!-- !bslidecell 00 0.85 -->
<!-- <img src="../fig/lec_system_hierarchy.png" height="400"><p><em>Funktionsblöcke eines elektronischen Systems. <div id="fig:hierarchy"></div></em></p> -->
![<p><em>Funktionsblöcke eines elektronischen Systems. <div id="fig:hierarchy"></div></em></p>](../fig/lec_system_hierarchy.png)
<!-- !eslidecell -->

<!-- !bblock -->
<!-- * Nutzen Sie Hierarchien zur Beschreibung komplexer Systeme -->
<!-- * Teile und herrsche -->
<!-- !eblock -->

<!-- !split -->
### System Assembly

<!-- <img src="../fig/lec_system_assembly.png" height="400"><p><em>Bottom-up Prozess, Integration. <div id="fig:assembly"></div></em></p> -->
![<p><em>Bottom-up Prozess, Integration. <div id="fig:assembly"></div></em></p>](../fig/lec_system_assembly.png)

Entnommen den Vorlesungsfolien von <a href="maloberti2011.html#maloberti2011">[1]</a>.

<!-- !split -->
### Schnittstellen zur Aussenwelt

<!-- <img src="../fig/lec_real_world_interface.png" width="400"><p><em>Interfacing. <div id="fig:interfaces"></div></em></p> -->
![<p><em>Interfacing. <div id="fig:interfaces"></div></em></p>](../fig/lec_real_world_interface.png)

Entnommen den Vorlesungsfolien von <a href="maloberti2011.html#maloberti2011">[1]</a>.

<!-- !split -->
### Meeting mit einem System (1)

<!-- <img src="../fig/lec_smartphone.png" width="400"><p><em>Drahtloses Kommunikationssystem. <div id="fig:smartphone"></div></em></p> -->
![<p><em>Drahtloses Kommunikationssystem. <div id="fig:smartphone"></div></em></p>](../fig/lec_smartphone.png)

Entnommen den Vorlesungsfolien von <a href="maloberti2011.html#maloberti2011">[1]</a>.

<!-- !split -->
### Meeting mit einem System (2)

<!-- <img src="../fig/lec_incubator.png" width="400"><p><em>Inkubator. <div id="fig:incubator"></div></em></p> -->
![<p><em>Inkubator. <div id="fig:incubator"></div></em></p>](../fig/lec_incubator.png)

Entnommen den Vorlesungsfolien von <a href="maloberti2011.html#maloberti2011">[1]</a>.

<!-- !split -->
### System in a Package (SiP)

<!-- <img src="../fig/lec_system_in_package.png" width="400"><p><em>Beschleunigungssensor. <div id="fig:sip"></div></em></p> -->
![<p><em>Beschleunigungssensor. <div id="fig:sip"></div></em></p>](../fig/lec_system_in_package.png)

Entnommen den Vorlesungsfolien von <a href="maloberti2011.html#maloberti2011">[1]</a>.

<!-- !split -->
### Backend Phasen

* Packaging
* Zuverlässigkeit = Qualität auf Zeit
* Testing auf Wafer Level, known good die (KGD)
  * Burn-in und Accelerated Aging (thermischer Stress, Arrhenius Gesetz)
  * Automatic Test Equipment (ATE)
    * System Probe
    * Interconnect Test
    * Build-in Self-Test (BIST)


* Statistische Datenanalyse und Yield Prognosen
  * Ausfallrate FIT (failure in time)
  * Badewannenkurve


<!-- !split -->
### Sie werden unsere Experten

*Leistungsmerkmale.* 
* Hintergrundwissen
  * Systemverständnis, Architektur, Herstellungsverfahren, Implementation

* Unterbewusste Kompetenz
  * Abgespeicherte Erfahrungen aus Erfolgsgeschichten und Misserfolgen

* Spezialwissen
  * Berufsspezifisches Wissen

* Teamwork Haltung
  * Kommunikationsfähigkeit, Berichtswesen und technische Präsentation

* Kreativität
* Tool-Kenntnisse



<!-- !split -->
### Silicon Valley - Made in Germany

<!-- !bslidecell -->

<iframe width="854" height="480" src="https://www.youtube.com/embed/UvluuAIiA50" frameborder="0" allowfullscreen></iframe>

<p><em>GLOBALFOUNDRIES From Sand to Silicon</em></p>



<!-- !eslidecell -->

<!-- !split -->
### Was man noch mit Elektronik machen kann ...

<!-- !bslidecell -->

<iframe width="854" height="480" src="https://www.youtube.com/embed/7S5IuaKiZIY" frameborder="0" allowfullscreen></iframe>

<p><em>Fettes Brot feat. Geekchester</em></p>



<!-- !eslidecell -->

<!-- !split -->
### Warum es sicht lohnt

<!-- !bslidecell -->

<iframe width="854" height="480" src="https://www.youtube.com/embed/SwPGxwBZw6I" frameborder="0" allowfullscreen></iframe>

<p><em>PartyProfs - The Circuit Song.</em></p>



<!-- !eslidecell -->

<!-- !split -->
