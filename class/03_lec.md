<!-- !split -->
<!-- jupyter-book 03_lec.md -->
# Halbleiterphysik

<div id="sec:phy"></div>
<!-- !split -->
### Elektrische Ladung

*Quantitatives und Einheiten.* 
* Ladung $Q$, Einheit $[Q]$ = 1 Coulomb = 1C = 1 As
* Ladung $q$ von Ladungsträgern, elektrische Ladung ist eine Eigenschaft von Elementarteilchen.



<!-- !split -->
### Elektrische Feldstärke

*Coulomb'sches Gesetz.* 
Ladungen erzeugen Kraftfelder und üben Kräfte aufeinander aus.

$$
\begin{align}
\mathbf{F} &=  \frac{1}{4 \pi \varepsilon} \frac{Q_1 Q_2}{r^2} \frac{\vec{r}}{r} \\
[F] &= 1N = 1 \frac{kg \, m}{s^2} = 1 \frac{Ws}{m}
\end{align}
$$



*Elektrische Feldstärke.* 
$$
\begin{align}
\mathbf{E} &= \frac{\mathbf{F}}{Q} \\
[E] & = \frac{[F]}{[Q]} = 1 \frac{N}{As} = 1 \frac{kg\,m}{A s^3} = 1 \frac{V}{m}
\end{align}
$$



<!-- !split -->
### Grundlagen der Elektrotechnik

Als weitere Vorbereitung für ein besseres Verständnis der Halbleiterphysik, sollten die Grundbegriffe aus den
Grundlagenvorlesungen der ersten beiden Semester aufgefrischt werden.\n

Rufen Sie sich folgende physikalische Größen und Gesetze in Erinnerung: 

* Elektrische Stromstärke
* Elektrische Spannung
* Kirchhoff'schen Gesetze
* Elektrische Energie
* Elektrische Leistung.

<!-- !split -->
### Einführung in die Halbleiterphysik

*Notice.* 
Die hier präsentierten Inhalte zur Halbleiterphysik sind den Kap. 8, Atom- und Kernphysik und Kap. 9, Festkörperphysik, 
des Buches *Physik für Ingenieure* von Hering, Martin und Stohrer, sowie Kap. 12, Halbleiter, des Buches *Elektronische
Bauelemente* von Reisch entnommen. <a href="hering2012.html#hering2012">[2]</a> <a href="reisch2007.html#reisch2007">[3]</a>



* Quantentheorie
  * Welle-Teilchen Dualismus
  * Schrödinger-Gleichung

* Elektronengas
  * Zustände und Aufenthaltswahrscheinlichkeiten
  * Zustandsdichten: $\int D(E)$ bzw. $\int N(E)$
  * Fermi-Dirac-Verteilung

* Dotierung
  * Donatoren und Akzeptoren


<!-- !split -->
### Elektronen im Festkörper

<!-- <img src="fig/lec3_bandstruktur.png" width="400"> -->
![](fig/lec3_bandstruktur.png)

* **Leiter** mit $\rho < 10^{-5} \Omega m$
* **Halbleiter** mit $10^{-5} \Omega m < \rho < 10^{7} \Omega m$
* **Isolator** mit  $\rho > 10^{7} \Omega m$

<!-- !split -->
### Energiebänder-Modell (1)

* **Modell gebundener Elektronen:** Das Bohr'sche Atommodell beschreibt, "dass sich Elektronen, die an isolierte Atome gebunden sind, nur auf diskreten Energieniveaus aufhalten können."
* "Die Aufenthaltswahrscheinlichkeit der Elektronnen um die Kerne wird durch das *Quadrat der Wellenfunktion* $\lvert \Psi \lvert^2$ beschrieben."

<!-- !split -->
### Wellenfunktion

Die Lösung für die Wellenfunktion $\Psi$ liefert räumlich stehende
Wellen. "Nach *de Brogli* kann dem Teilchen eine Welle $\Psi$ mit dem 
Wellenvektor $\mathbf{k}=\mathbf{p}/\hbar$ und der Kreisfrequenz
$\omega$ zugeordnet werden:"

**Wellenfunktion (eindimensional)** 

$$
\begin{equation}
\Psi (x,t) = a \exp\left(i k_x x - i \omega t \right) = a \exp\left(\frac{i}{\hbar}\left( p_x x - E t \right) \right)   
\end{equation}
$$

mit $E=\hbar \omega$,  $p_x=\hbar k_x$ und $i=\sqrt{-1}$.

<!-- !split -->
### Newton Mechanik vs. Quantentheorie

* "In der klassischen Physik (Newton Mechanik) wird das Teilchen durch seine *Bahnkurve* $\mathbf{r}(t)$ beschrieben, in der Quantentheorie dagegen nur durch seine *Aufenthaltswahrscheinlichkeit* $\lvert \Psi \lvert^2 dV$."
* ``Die Fundamentalgleichung der Quantentheorie, die die Bestimmung von $\Psi$ ermöglicht, ist die Schrödinger-Gleichung (E. Schrödinger, 1887 bis 1961). Sie ist vergleichbar mit der Newton'schen Bewegungsgleichung, aus der die Bahnkurve $\mathbf{r}(t)$ bestimmt wird.'' 

<!-- !split -->
### Schrödinger-Gleichung  (zeitabhängig)

$$
\begin{equation}
\left( -\frac{\hbar^2}{2 m} \Delta + V(\mathbf{r}) \right) \Psi (\mathbf{r},t) = i \hbar \frac{\partial}{\partial t} \Psi (\mathbf{r},t)
\end{equation}
$$

wobei

* $m$, Masse des Teilchens,
* $V(\mathbf{r})$, potentielle Energie; $\mathbf{r} = (x, y, z)$
* $\Delta$, Laplace-Operator:

$$
\begin{equation}
\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}
= \left( \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right)^2
= \nabla^2
\end{equation}
$$

<!-- !split -->
### Energiebänder-Modell (2)

* **Modell freier Elektronen**: "Nach der Quantentheorie wird die Aufenthaltswahrscheinlichkeit der Elektronen im Kristall durch das *Quadrat der Wellenfunktion* $\lvert \Psi \lvert^2$ beschrieben." 
* **De-Broglie-Beziehung** (Teilchenbild / Wellenbild)

$$
\begin{equation}
p = \frac{h}{\lambda} = \frac{h}{2 \pi} \frac{2 \pi}{\lambda} = \hbar k
\end{equation}
$$

* **Kinetische Energie der Elektronen** : Der Physiker schreibt hier $E$ anstelle von $W$. In der Elektrotechnik ist der Buchstabe $E$ allerdings mit dem elektrischen Feld verknüpft.

$$
\begin{equation}
E_{kin} = \frac{p^2}{2 m} = \frac{\hbar^2 k^2}{2 m}
\end{equation}
$$

<!-- !split -->
### Energiebandstruktur (1)
<div id="sl:energieband"></div>

<!-- <img src="fig/lec3_energiebandstruktur.png" width="400"> -->
![](fig/lec3_energiebandstruktur.png)

<!-- !split -->
### Energiebandstruktur (2)

* Die kinetische Energie $E_{kin}$ als Funktion der Wellenzahl $k$ ergibt eine Parabel.
* Für Elektronen in Kristallen ergeben sich *verbotene* Energiebereiche.
* Stehende Wellen durch Reflexionen am Kristallgitter mit der Gitterkonstanten $a$.
* Elektronen- bzw. Materiewellen mit der Wellenlänge $\lambda$ erfüllen die **Bragg'sche Reflexionsbedingung**

$$
\begin{align}
\lambda_n &= \frac{2 a}{\pi}, \quad n=1,2,3,... \\
k_n &= \frac{2 \pi}{\lambda_n} = \frac{\pi}{a} n
\end{align}
$$

<!-- !split -->
### Aufenthaltswahrscheinlichkeit

<!-- <img src="fig/lec3_aufenthaltswahrscheinlichkeit.png" width="400"> -->
![](fig/lec3_aufenthaltswahrscheinlichkeit.png)

<!-- !split -->
### Reduziertes Zonenschema

* "Durch Überlagerung der laufenden mit den reflektierten Wellen entstehen stehende Elektronenwellen mit ortsfesten Knoten und Bäuchen."
* "Die $E(k)$-Parabel bekommt daher an der Stelle $k_1 = \pm \pi/a$ Unstetigkeitsstellen." Dieses sind die sog. *verbotenen Zonen* oder *Energielücken*.
* Aufgrund er Periodizität des $k$-Raumes kann die Parabel durch ein *reduziertes Zonenschema* dargestellt werden, vgl. The section [Energiebandstruktur (1)](#sl:energieband).

<!-- !split -->
### Besetzungswahrscheinlichkeit (1)

* Die Berechnung der Ladungsträgerdichten von Elektronen (n) und Löchern (p) erfolgt mithilfe der Fermi-Dirac-Statistik.
* **Modell des freien Elektronengases**: "Dieses wurde von A. Sommerfeld (1868 bis 1951) vorgeschlagen und von E. Fermi (1901 bis 1954) erweitert. Es beschreibt die Leitungselektronen der Metalle so wie die frei beweglichen Moleküle eines Gases, vernachlässigt also die Wechselwirkung der Elektronen mit den ortsfesten Atomkernen und damit auch das Auftreten von Energielücken."

<!-- !split -->
### Besetzungswahrscheinlichkeit (2)

* "Befinden sich die Elektronen in einem Würfel der Kantenlänge $L$, dann ist ihre Aufenthaltswahrscheinlichkeit durch das Quadrat der Wellenfunktion $\Psi$ gegeben, die als Lösung aus der Schrödinger-Gleichung folgt."
* Streng genommen gilt das Modell des freien Elektronengases nur für $T=0$. "Nur am absoluten Nullpunkt besetzen die Elektronen alle Energieniveaus von Null bis $E_F$."
* Bei endlicher Temperatur nimmt die kinetische Energie des Elektronengases zu, sodass einige Energieniveaus oberhalb der Fermi-Kante besetzt werden und eine gleiche Anzahl unterhalb leer bleibt.

<!-- !split -->
### Fermi-Dirac-Verteilungsfunktion

* "Die Wahrscheinlichkeit, mit der ein bestimmter Energiezustand $E$ mit Elektronen besetzt ist, wird beschrieben durch die *Fermi-Dirac-Verteilungsfunktion*"

$$
\begin{equation}
f_{FD}(E) = \frac{1}{1 + \exp\left( \frac{E - E_F}{k_B T}\right)}
\end{equation}
$$

<!-- !split -->
### Fermi-Dirac-Statistik (1)

<!-- <img src="fig/lec3_fermidirac.png" width="400"> -->
![](fig/lec3_fermidirac.png)

<!-- !split -->
### Fermi-Dirac-Statistik (2)

* "Die Fermi-Dirac-Statistik ist anwendbar auf Teilchen mit halbzahligem Spin, zu denen die Elektronen gehören."
* "Bei $T=0$ sind alle Zustände unterhalb der Fermi-Energie $E_F$ besetzt, oberhalb $E_F$ leer: $f_{FD}(E)=1$ für $0 \leq E < E_F$, $f_{FD}(E)=0$ für $E > E_F$."
* "Bei endlicher Temperatur sind entsprechend den schraffierten Flächen Zustände unterhalb der Fermi-Energie leer und oberhalb besetzt. Die Besetzungswahrscheinlichkeit nimmt von 90% auf 10% ab innerhalb eines Energiebereiches von $\Delta E \approx 4.4 k T$. Die bei tiefen Temperaturen scharfe Fermi-Kante weicht also mit zunehmender Temperatur immer mehr auf."

<!-- !split -->
### Halbleiter im thermischen Gleichgewicht

* Ladungsträgerkonzentration Elektronen $n_0 \approx N_C \exp\left( \frac{E_F - E_C}{kT} \right)$
* Ladungsträgerkonznetration Löcher $p_0 \approx N_V \exp\left( \frac{E_V - E_F}{kT} \right)$
* *Massenwirkungsgesetz* $ n_i^2(T) = n_0 \cdot p_0 = N_C N_V \exp\left( -\frac{(E_C - E_V)}{kT} \right) $
* *Neutralitätsbedingung* der Raumladung $N_A^{-} + n = N_D^{+} + p$

<!-- !split -->
### Intrinsischer Halbleiter

<!-- <img src="fig/lec3_intrinsischer_hl.png" width="600"> -->
![](fig/lec3_intrinsischer_hl.png)

<!-- !split -->
### Dotierter Halbleiter

<!-- <img src="fig/lec3_pn_hl.png" width="600"> -->
![](fig/lec3_pn_hl.png)

<!-- !split -->
### Stromgleichung

* **Ohmsches Gesetz für Halbleiterphysiker**
* Allgem. Ansatz (vektoriell)

$$
\begin{align}
\mathbf{J}_n &= \overbrace{e \mu_n n \mathbf{E}}^{\text{Feldanteil}}
+ \overbrace{e D_n \nabla n}^{\text{Diffusionsanteil}}
&
D_n &= \mu_n \frac{kT}{q} \quad \text{Einstein-Relation} \\
\mathbf{J}_p &= \underbrace{e \mu_p n \mathbf{E}}_{\text{Feldanteil}}
- \underbrace{e D_p \nabla p}_{\text{Diffusionsanteil}}
&
D_p &= \mu_p \frac{kT}{q} \quad \text{Einstein-Relation}
\end{align}
$$

<!-- !split -->
### Stromgleichung 1D

**Vereinf. eindimensionaler Fall**

$$
\begin{align}
J_n &= \overbrace{e \mu_n n E}^{\text{Feldanteil}}
+ \overbrace{e D_n \frac{\partial n}{\partial x}}^{\text{Diffusionsanteil}}
&
D_n &= \mu_n \frac{kT}{q} \quad \text{Einstein-Relation}\\
J_p &= \underbrace{e \mu_p n E}_{Feldanteil}
- \underbrace{e D_p \frac{\partial p}{\partial x}}_{Diffusionsanteil}
&
D_p &= \mu_p \frac{kT}{q} \quad \text{Einstein-Relation}
\end{align}
$$

<!-- !split -->
### Kontinuitätsgleichung

**Allgem. Ansatz**

$$
\begin{align}
\frac{\partial n}{\partial t}
&= \frac{1}{e} \nabla \cdot \mathbf{J}_n
- (\mathcal{R} - \mathcal{G})
&
\frac{\partial p}{\partial t}
&= \frac{1}{e} \nabla \cdot \mathbf{J}_p
- (\mathcal{R} - \mathcal{G})
\end{align}
$$

<!-- !split -->
### Kontinuitätsgleichung 1D

**Vereinf. eindimensionaler Fall**

$$
\begin{align}
\frac{\partial n}{\partial t}
&= \frac{1}{e} \frac{\partial J_n}{\partial x}
- (\mathcal{R} - \mathcal{G})
&
\frac{\partial p}{\partial t}
&= \frac{1}{e} \frac{\partial J_p}{\partial x}
- (\mathcal{R} - \mathcal{G})
\end{align}
$$

<!-- !split -->
### Poisson-Gleichung

* "Für eine vollständige Beschreibung der Vorgänge im Halbleiter unter Nichtgleichgewichtsbedingungen sind die Strom- und Kontinuitätsgleichungen durch eine Beziehung zu ergänzen, die es erlaubt, die elektrische Feldstärke bzw. das elektrostatische Potential aus der Verteilung der Ladungen zu berechnen."

$$
\begin{equation}
\nabla \cdot \mathbf{E} = -\nabla^2 \varphi =
\frac{\varrho}{\varepsilon_0 \varepsilon_r}
\end{equation}
$$

* Hierbei bezeichnet $\varrho$ die Raumladung

$$
\begin{equation}
\varrho = e \left( p - n + N_D^{+} - N_A^{-} \right)
\label{eq:rho}
\end{equation}
$$

<!-- !split -->
