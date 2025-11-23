# FDM Filament Data Analysis and Tables

> **Source:** `FDM Filament Data Analysis and Tables.pdf`
> **Converted:** 2025-11-22 21:18:11
> **Method:** PyMuPDF

---

## Page 1


An Analytical Deep-Dive into FDM
Filament Properties, Classification, and
Substitution Frameworks


Executive Summary

This report presents an exhaustive analysis of Fused Deposition Modeling (FDM) 3D printer
filaments, moving beyond marketing terminology to establish quantitative, data-driven
frameworks for material selection. It directly addresses critical research gaps in available data
by deconstructing the authority of filament datasheets, quantifying the performance impact
of anisotropy, and codifying multi-variable material substitution rules.
The analysis finds that the single most important factor governing the mechanical
performance of a 3D-printed part is anisotropy—the difference in strength between the XY
plane (along layers) and the Z-axis (between layers). Data from "gold standard" technical
datasheets (TDS) reveals that this inter-layer strength penalty can be as high as 50% 1, a
factor often obscured by manufacturer data derived from irrelevant injection molding test
methods.2
To address these data gaps, this report synthesizes data from manufacturer TDS,
independent testing, and academic literature to create a comprehensive properties database.
This database is then used to develop two key frameworks for material selection:
1.​ A performance-based taxonomy that clusters materials into logical groups (Standard,
Functional, High-Performance, and Specialty).
2.​ A Multi-Criteria Decision-Making (MCDM) matrix that allows for the quantitative
ranking of materials against application-specific requirements.
Finally, the report investigates common material substitution scenarios (e.g., PLA vs. PLA+,
ABS vs. ASA, PC vs. Nylon). It debunks common misconceptions—such as PLA+ offering
higher temperature resistance—and reveals hidden failure modes, such as creep and
hygroscopicity in nylons, that are absent from nearly all datasheets but are critical for
engineering applications.3


---


## Page 2


Part 1: Deconstructing Filament Datasheets: Authority,
Standards, and Anisotropy


1.1 The Datasheet Dilemma: Manufacturer vs. Independent Data

A primary research gap in FDM material science is the pervasive inconsistency in technical
data. The mechanical properties of a finished part are dominated by a combination of the bulk
polymer properties and the printing process parameters (e.g., layer adhesion). This creates a
spectrum of data relevance, which can be organized into a "Data Trust Hierarchy."
Red Flag (Use with Caution): Injection-Molded Data
Some manufacturers provide technical data sheets (TDS) that use properties derived from
injection molding.2 This data represents the isotropic bulk property of the polymer resin. It is
fundamentally irrelevant for predicting the performance of an FDM part, as it completely
ignores the weakest point of any print: the Z-axis layer bond.
Bronze Standard: Independent Comparative Testing
Independent testers (e.g., CNC Kitchen, Instructables) provide invaluable, application-focused
data.4 While their test methods may not always adhere to strict ASTM or ISO standards, their
comparative data is excellent for understanding relative performance (e.g., "Brand X PETG is
more brittle than Brand Y" 4). This data often uncovers critical properties missed by a TDS,
such as creep.3
Silver Standard: Manufacturer-Printed Specimen Data
Authoritative manufacturers (e.g., Polymaker, Prusament) provide a TDS that explicitly states
the data comes from 3D printed specimens.6 These datasheets are far more reliable as they
account for the FDM process. Crucially, they also provide the print settings used to achieve
the published values (e.g., layer height, infill, print speed).7 This data represents a "best-case
scenario" for that material.
Gold Standard: Anisotropic Independent or Manufacturer Data
The pinnacle of authority is data that quantifies anisotropy by providing separate values for
specimens printed in different orientations (e.g., XY and Z). This data, typically provided by
industrial suppliers like Stratasys or in formal academic studies, is the only way to perform
accurate engineering analysis, as it directly measures the "strength penalty" of layer
adhesion.1 Academic research confirms that real-world printed part properties can "differ
considerably from the values presented in the datasheets of various filament suppliers" 10,
making this anisotropic data essential.


---


## Page 3


1.2 The Criticality of Testing Standards (ASTM/ISO) and Print Settings

To compare any two datasheets, one must first verify that they use the same testing
standards. These standards define the exact shape of the test coupon and the method of
testing:
●​ Tensile Strength (Pulling): ASTM D638 or ISO 527.9
●​ Flexural Strength (Bending): ASTM D790 or ISO 178.13
●​ Impact Strength (Toughness): ASTM D256 (Izod) or ISO 179 (Charpy).4
●​ Heat Deflection Temperature (HDT): ASTM D648 or ISO 75.7
As noted in "Silver Standard" datasheets 7 and confirmed by extensive academic reviews 16,
these mechanical properties are dominated by printing process parameters. Layer thickness
is often cited as the most important factor.16 A TDS value achieved with a 0.2 mm layer height,
100% rectilinear infill, and 2 perimeters 7 is a reference point, not a universal constant. Any
change in parameters by the end-user will result in a different final part property.

1.3 Anisotropy: The Primary Factor Governing Part Performance

Anisotropy is the root cause of the discrepancies discussed above. A 3D-printed part is
inherently anisotropic: it is strong in the XY plane (where forces are applied along the
extruded lines) but weak in the Z-direction (where forces are applied between the layer
bonds).
"Gold Standard" datasheets that provide anisotropic data are the most valuable resource for
an engineer. This data allows for the quantification of the "Z-axis penalty"—the percentage
reduction in strength a designer must account for if a part cannot be oriented to place all
stresses in the XY plane.
The following table, synthesized from such datasheets, quantifies this penalty.
Table 1.1: The Anisotropic "Strength Penalty" in FDM Polymers

Material
Property
Test
Standar
XY-Orie
ntation
Z-Orient
ation
%
Reductio
Source(s
)


---


## Page 4


d
Value
Value
n (Z vs.
XY)
ABS
Tensile
Strength
ASTM
D638
30.8 MPa
27.5 MPa
-10.7%
9
PC
Tensile
Strength
ASTM
D638
57 MPa
42 MPa
-26.3%
9
ULTEM
9085
Tensile
Strength
ASTM
D638
76.2 MPa
(XZ)
54.2 MPa
(ZX)
-28.9%
19
Nylon
12CF
Tensile
Strength
ASTM
D638
77.5 MPa
(XZ)
38.3 MPa
(ZX)
-50.6%
1
ABS
Elongatio
n at
Break
ASTM
D638
8.1%
1.8%
-77.8%
9
PC
Elongatio
n at
Break
ASTM
D638
4.8%
2.5%
-47.9%
9
ULTEM
9085
Izod
Impact
(Notched
)
ASTM
D256
88.5 J/m
39.2 J/m
-55.7%
21
This data reveals that the primary research gap is not just "what is this filament's strength?"
but "what is this filament's interlayer adhesion strength?" Even an ultra-performance material
like carbon-fiber-filled Nylon (Nylon 12CF) loses over 50% of its tensile strength and 77% of
its elongation when forces are applied perpendicular to the layers. This reframes the entire
material selection problem: design must accommodate this anisotropy, or the material
selected must be one with demonstrably superior layer adhesion.

Part 2: A Quantitative Database of FDM Polymers


---


## Page 5


The following tables provide a comprehensive, import-ready database of FDM polymer
properties. This data is synthesized from a wide range of sources 7 to provide a typical
performance range. As established in Part 1, these values are highly dependent on brand,
testing method, and print settings. All values are standardized to metric units (MPa, °C, g/cm³,
kJ/m²).
Table 2.1: Properties of Standard Polymers
Material
Tensile
Strength
(MPa)
Tensile
Modulus
(MPa)
Elongati
on at
Break
(%)
HDT /
Max
Service
Temp
(°C)
Impact
Strength
(kJ/m²)
Density
(g/cm³)
PLA
55 - 75
2100 -
3600
2 - 12
52 - 60
4 - 9
1.21 - 1.25
PETG
45 - 53
1675 -
2150
25 - 130
69 - 80
7 - 14
1.23 - 1.27
ABS
40 - 46
1800 -
2400
10 - 25
87 - 100
10 - 39
1.04 -
1.05
ASA
44 - 55
1900 -
2400
10 - 25
90 - 100
41
1.05 -
1.07
Table 2.2: Properties of Engineering Polymers
Material
Tensile
Strength
(MPa)
Tensile
Modulus
(MPa)
Elongati
on at
Break
(%)
HDT /
Max
Service
Temp
(°C)
Impact
Strength
(kJ/m²)
Density
(g/cm³)
Nylon
(PA)
45 - 85
2000 -
2400
8 - 50
80 - 100
> 40
(often
unnotche
d)
1.05 -
1.15


---


## Page 6


PC
60 - 72
2300 -
2400
8 - 100+
117 - 138
9 - 35
1.20 -
1.21
Tough
PLA /
PLA+
60 - 65
2000 -
2200
12 - 30
50 - 60
8 - 20
1.23 -
1.25
Table 2.3: Properties of High-Performance Polymers
Material
Tensile
Strength
(MPa)
Tensile
Modulus
(MPa)
Elongati
on at
Break
(%)
HDT /
Max
Service
Temp
(°C)
Glass
Transitio
n (Tg)
(°C)
Density
(g/cm³)
PEI
(ULTEM
9085)
55 - 77
2410 -
2520
1.9 - 5.4
153 - 177
177
1.27
PEKK
105
3205
9.5
165 - 329
162
1.28
PEEK
101
3720
27
143 - 290
143
1.31
Table 2.4: Properties of Flexible Polymers (Elastomers)
Material
Shore
Hardness
Tensile
Strength
(MPa)
Elongation
at Break
(%)
Key
Feature(s)
Density
(g/cm³)
TPE (e.g.,
85A)
85A
~8
> 350
Very soft,
rubber-like
1.00
TPU (e.g.,
95A)
95A
26 - 43
300 - 600
More
common,
stiffer,
better
abrasion
resistance
1.19 - 1.23


---


## Page 7


Part 3: Analysis of Composite Filaments:
Fiber-Reinforced Polymers


3.1 Reinforcement Principles: Chopped vs. Continuous Fiber

FDM composites primarily use reinforcing fibers like carbon, glass, or Kevlar (Aramid).28 This
report focuses on chopped fiber composites, which are standard thermoplastic filaments
impregnated with short (~0.1-0.4 mm) fibers.29 These can be printed on most FDM printers,
provided a hardened-steel nozzle is used to prevent extreme abrasion.
The addition of these fibers primarily increases stiffness (Tensile and Flexural Modulus) and
dimensional stability (by lowering the coefficient of thermal expansion).30 They also improve
HDT.
A common misconception is that these fibers universally increase "strength" (i.e., tensile
strength). In reality, the chopped fibers can act as stress-concentration points and interfere
with the polymer's ability to form strong interlayer bonds, which can negatively impact Z-axis
strength and toughness.32

3.2 Quantitative Comparison: The Matrix-Dominant Property

The effect of chopped fibers is critically matrix-dependent. The data, which can appear
contradictory, reveals this important principle.
●​ In a Brittle Matrix (e.g., PLA): The base polymer is already stiff and brittle. Adding stiff,
brittle fibers can further increase stiffness (modulus) but may decrease tensile strength
and impact strength. The fibers disrupt the polymer matrix and provide points for cracks
to initiate.
●​ In a Ductile Matrix (e.g., Nylon, PETG): The base polymer is softer and tougher. The
stiff fibers become the primary load-bearing element. This dramatically increases both
stiffness and tensile strength, transforming the material's properties.


---


## Page 8


The table below, synthesized from independent academic studies, illustrates this effect.
Table 3.1: Comparative Properties of Base vs. Chopped Fiber Composites

Base
Mater
ial
Reinf
orced
Mater
ial
Tensil
e
Stren
gth
(MPa)
%
Chan
ge
Flexur
al
Modul
us
(MPa)
%
Chan
ge
Impac
t
Stren
gth
%
Chan
ge
Sourc
e(s)
Basic
PLA
Glass
Fiber
PLA
60
$\right
arrow
$
59.27
-1.2%
3800
$\right
arrow
$ 4414
+16.2
%
16 J/m
$\right
arrow
$
10.16
kJ/m²
Varies
¹
27
Basic
PLA
Carbo
n
Fiber
PLA
60
$\right
arrow
$ 39
-35%
3800
$\right
arrow
$
5003
+31.7
%
16 J/m
$\right
arrow
$ 5.08
kJ/m²
Varies
¹
27
PETG
CF-PE
TG
(10
wt%)
~45²
$\right
arrow
$
50.14
~+11.4
%
~2150²
$\right
arrow
$ N/A
N/A
~85
J/m²
$\right
arrow
$ N/A
N/A
27
Nylon
(PA)
CF-N
ylon
~45³
$\right
arrow
$
283.5
**+53
0%**³
~2100
³
$\right
arrow
$
10,50
0
**+40
0%**³
N/A
N/A
22
¹ Impact strength units in 27 are inconsistent (J/m vs kJ/m²); however, a separate study 14
notes Glass Fiber PLA (20 wt%) achieved a tensile strength of 80 MPa and tensile modulus of
8 GPa, showing significant variation based on fiber concentration.


---


## Page 9


² PETG base values are from.27 CF-PETG value is from.33
³ Nylon base values are from.22 Reinforced values are calculated from the 6.3x and 5x
improvements reported in.34
The data clearly shows that adding carbon fiber to PLA decreased its tensile strength by 35%,
while adding it to nylon increased its tensile strength by over 500%. This demonstrates that
composites are not a universal upgrade; they are a tool for modifying a base polymer's
properties, and the outcome depends entirely on the base polymer's chemistry.

Part 4: Developing Material Clustering and Similarity
Frameworks

To address the user's request for similarity metrics, it is necessary to move from
marketing-based clusters 35 to quantitative, performance-based frameworks. "Similarity" is
not a fixed property; it is a measure of a material's suitability for a specific, defined
application.

4.1 From Marketing to Engineering: A Logical FDM Taxonomy

The most logical classification system clusters materials by their measurable performance in
key engineering metrics, primarily Heat Deflection Temperature (HDT).
1.​ Cluster 1: Standard / Prototyping (HDT < 80°C):
○​ Materials: PLA, PLA+, Tough PLA, HIPS, PVA, TPE/TPU.
○​ Use Case: Form and fit prototypes, aesthetic models, low-stress applications where
heat and UV light are not factors.
2.​ Cluster 2: Functional / Durable (HDT 80-120°C or High Toughness):
○​ Materials: PETG, ABS, ASA, Nylon (PA), PP.
○​ Use Case: End-use functional parts, jigs, fixtures, and components that require good
toughness, wear resistance, or moderate heat resistance (e.g., parts for inside a 3D
printer enclosure).
3.​ Cluster 3: High-Performance (HDT > 120°C):
○​ Materials: Polycarbonate (PC), PEI (ULTEM), PEKK, PEEK.
○​ Use Case: High-demand engineering applications in aerospace, automotive, and
manufacturing. Used for high-temperature tooling, FST (Flame, Smoke, Toxicity)
rated parts, and metal replacement.37
4.​ Cluster 4: Modifiers (Composites):


---


## Page 10


○​ Materials: Carbon Fiber (CF), Glass Fiber (GF), ESD.
○​ Use Case: These are not base polymers but additives that are applied to Clusters 2
and 3 (e.g., PA-CF, PETG-CF, PC-CF) to enhance specific properties like stiffness,
dimensional stability, and conductivity.

4.2 A Weighted Multi-Criteria Decision-Making (MCDM) Framework

The most robust "similarity metric" is a decision framework that allows a user to rank materials
based on their specific application's needs. Based on academic MCDM methodologies 39, a
weighted decision matrix can be constructed.
This framework is the similarity metric. "Similarity" is defined as the two materials that receive
the highest final score for a given application.
How to Use the MCDM Framework:
1.​ Define KPIs: Identify the Key Performance Indicators (KPIs) critical for the application,
such as those drawn from research: Stiffness (Modulus), Toughness (Impact), Heat
Resistance (HDT), UV Resistance, Printability (Warping), and Cost.41
2.​ Assign Weights: Assign a weight (e.g., 1-10) to each KPI based on its importance to the
project.
3.​ Normalize Data: Populate the matrix with data from Part 2, normalizing each value to a
common scale (e.g., 0-1 or 1-10).
4.​ Calculate Score: The final score for each material is the sum of (KPI_Normalized_Score
$\times$ KPI_Weight).
The following table serves as a template for this process.
Table 4.1: Weighted Decision Matrix for FDM Material Selection
Material
KPI 1:
Stiffness
KPI 2:
Toughne
ss
KPI 3:
HDT
KPI 4:
Printabili
ty
KPI 5:
Cost
Applicati
on Score
Applicati
on
Weights
$\rightar
row$
(e.g., 3)
(e.g., 8)
(e.g., 6)
(e.g., 5)
(e.g., 9)
(Sum of
Scores)


---


## Page 11


PLA
Score
(1-10)
Score
(1-10)
Score
(1-10)
Score
(1-10)
Score
(1-10)
=
$Sum(Sc
ore
\times
Weight)$
PETG
Score
(1-10)
Score
(1-10)
Score
(1-10)
Score
(1-10)
Score
(1-10)
=
$Sum(Sc
ore
\times
Weight)$
ASA
Score
(1-10)
Score
(1-10)
Score
(1-10)
Score
(1-10)
Score
(1-10)
=
$Sum(Sc
ore
\times
Weight)$
PC
Score
(1-10)
Score
(1-10)
Score
(1-10)
Score
(1-10)
Score
(1-10)
=
$Sum(Sc
ore
\times
Weight)$
...etc.







4.3 Visualizing Engineering Trade-offs: Ashby Plots for FDM Polymers

As a visual alternative to the MCDM matrix, the data from Part 2 can be plotted on Ashby-style
charts 45 to visualize engineering trade-offs.
●​ Figure 4.1: Strength vs. Toughness (Tensile Strength vs. Impact Strength): This plot
visually separates materials. PLA would cluster in a "High Strength, Low Toughness"
quadrant. PETG and Nylon would be in the "Moderate Strength, High Toughness"
quadrant. PC would be in the "High Strength, High Toughness" quadrant. This plot
immediately visualizes why one would substitute PLA for PETG.
●​ Figure 4.2: Stiffness vs. Density (Tensile Modulus vs. Density): This plot is essential
for lightweighting applications. It would show composites like PA-CF in the desirable


---


## Page 12


high-stiffness, low-density quadrant, demonstrating their value for aerospace and
automotive applications.37
●​ Figure 4.3: Heat Resistance vs. Cost (HDT vs. $/kg): This plot clearly illustrates the
"pay-for-performance" curve. It would show a large cluster of standard polymers (PLA,
PETG, ABS) in the low-cost/low-temp corner, with an exponential "knee" leading to
high-performance polymers (PEEK, ULTEM) in the high-cost/high-temp region.38

Part 5: A Practical Investigation of Material
Substitution Rules

This section synthesizes all data to codify logical, evidence-based substitution rules,
addressing the specific "research gaps" identified in the user query.

5.1 Substitution for Toughness: PLA $\rightarrow$ PLA+ / Tough PLA
$\rightarrow$ PETG

Investigation: PLA vs. PLA+
The user's premise ("PLA+ $\approx$ PLA with higher temp resistance") is a common
misconception that is not supported by technical data.
●​ An eSun TDS, for example, shows identical tensile strength (65 MPa) for both PLA and
PLA+.25
●​ The primary difference is in toughness. The same datasheet shows PLA+ has an IZOD
Impact Strength of 8.5 kJ/m², more than double the 4.0 kJ/m² of standard PLA.25
●​ This is confirmed by independent tests 48 and marketing from other brands, which
highlight "impact modifiers" 49 and "durability" 50, not static strength or heat resistance.
Rule 1 (PLA $\rightarrow$ PLA+): SUBSTITUTE(PLA, PLA+) IF (Part_Failure_Mode =
'Shattering' / Brittle Fracture) AND (Static_Strength_is_Sufficient). This is a substitution for
Toughness (Impact Resistance), not Strength or Temperature.
Investigation: PLA+ vs. PETG
When PLA+ is not tough enough, or when heat resistance is needed, PETG is the next logical
step.
●​ Trade-off: PETG often has a lower tensile strength (45-50 MPa) than PLA (55-75 MPa).51
●​ Benefit: PETG has vastly superior elongation at break (~130% vs. ~4% for PLA 52),


---


## Page 13


making it far less brittle. It also has a higher HDT (~80°C vs. ~60°C for PLA).53
●​ Variable: Independent testing shows PETG layer adhesion can be highly variable, with
Z-axis impact resistance sometimes lower than that of PLA, suggesting high sensitivity to
moisture and brand.4
Rule 2 (PLA+ $\rightarrow$ PETG): SUBSTITUTE(PLA+, PETG) IF
(Toughness_is_Still_Insufficient) OR (Application_Temp > 60°C).

5.2 Substitution for Heat Resistance: PLA $\rightarrow$ HTPLA
(Annealed) $\rightarrow$ ABS/ASA

Investigation: The Annealing Post-Processing Path
Annealing is a post-print process of heating a part in an oven (e.g., at 110°C for 30-60
minutes) to induce a change in the polymer's internal structure from amorphous to more
crystalline.55
●​ Benefit: This process can dramatically increase the heat resistance of specialized HTPLA
(High-Temp PLA). The HDT can jump from ~58°C to over 150°C 15, far surpassing ABS.
●​ Trade-off (The "Catch"): This structural change causes significant, non-uniform
dimensional changes. The part will shrink in the X and Y axes and grow in the Z-axis.57
This requires the user to pre-scale the model and iterate, making it unsuitable for
high-precision parts without significant tuning.
Rule 3 (PLA $\rightarrow$ Annealed HTPLA): SUBSTITUTE(PLA, Annealed_HTPLA) IF
(Application_Temp > 80°C) AND (Dimensional_Accuracy_is_Controllable_or_Non-Critical).
Investigation: The ABS/ASA Substitution Path
This is the traditional substitution for heat resistance.
●​ Benefit: ABS and ASA offer a higher HDT (~100°C) than PETG (~80°C) 22 and are
generally stiffer.58
●​ Trade-off: Both require an enclosure to manage the high coefficient of thermal
expansion and prevent warping.59 They also release potentially harmful fumes (Styrene).59
Rule 4 (PETG $\rightarrow$ ABS): SUBSTITUTE(PETG, ABS) IF (Application_Temp > 80°C)
AND (Higher_Stiffness_is_Required) AND (Enclosure_is_Available).
Rule 5 (ABS $\rightarrow$ ASA): SUBSTITUTE(ABS, ASA) IF (Application_is_Outdoors). This
is a near "drop-in" substitution. ASA (Acrylonitrile Styrene Acrylate) is chemically a modified
ABS designed for superior UV resistance and weatherability.59 Printing parameters are nearly
identical.61


---


## Page 14


5.3 Substitution for Engineering Applications: The "Nylon Trap" (Nylon
vs. PC)

This is a classic trade-off between two "engineering" workhorses, and it highlights a critical
research gap where TDS data fails.
●​ Polycarbonate (PC): Known for its "comical" strength, high rigidity, excellent
dimensional accuracy, and high heat resistance (~130°C).63
●​ Nylon (Polyamide / PA): Known for its superior toughness (flexibility), low coefficient of
friction (slipperiness), and superior chemical resistance.63
The "Nylon Trap": The TDS data for Nylon (e.g., Table 2.2) is misleading. Independent testing
reveals that Nylon's real-world performance is dominated by two properties never listed on a
TDS 3:
1.​ Hygroscopicity (Moisture): Nylon (especially PA6) is extremely hygroscopic and can
absorb up to 3% water by weight.3 This moisture acts as a plasticizer, drastically reducing
performance. Tests show moisture-conditioned PA6 loses nearly two-thirds of its
stiffness and 44% of its tensile strength.3
2.​ Creep: Nylon parts under constant load (even a load well within their elastic range) will
slowly deform, or "creep," over time. This makes it unsuitable for structural brackets or
parts that are constantly under tension.3
Rule 6 (PC vs. Nylon): IF (Goal = 'Stiffness', 'Dimensional_Stability', 'Heat_Resistance') THEN
(SELECT PC). IF (Goal = 'Toughness', 'Chemical_Resistance', 'Low_Friction / Wear_Parts') THEN
(SELECT Nylon).
Rule 7 (Nylon Sub-Rule): IF (SELECT Nylon) THEN (Must_Dry_Filament_Thoroughly). AND IF
(Application_has_Constant_Load) THEN (Must_Use_PA12 OR Must_Anneal_PA6).3
●​ PA12 is less sensitive to moisture (absorbing ~0.5%) and less prone to creep than PA6.3
●​ Annealing PA6 (as described in 5.2) induces crystallization, which significantly reduces
the creep problem.3

5.4 Substitution for Ultra-Performance Applications

This substitution path is for applications that exceed the thermal or chemical limits of PC and


---


## Page 15


Nylon.
Rule 8 (PC $\rightarrow$ ULTEM 9085): SUBSTITUTE(PC, ULTEM) IF (Application_Temp >
130°C) AND (FST_Rating_is_Required).
●​ Benefit: ULTEM (PEI) is the next step up from PC. It offers higher continuous-use
temperatures (~170°C) and HDT (153-217°C) 67 and is inherently flame retardant (UL
94-V0).67
●​ Trade-off: Requires an extreme-temperature printer: nozzle >350°C, bed >110°C, and an
actively heated chamber.69
Rule 9 (ULTEM vs. PEEK): SUBSTITUTE(ULTEM, PEEK) IF (Application_Temp > 220°C) OR
(Extreme_Chemical_Resistance_is_Required).
●​ PEEK (Polyetheretherketone): The pinnacle of FDM polymers. Qualified for stable
thermal conditions up to 250°C 67 and has superior resistance to aggressive chemicals.71
It is also the most expensive.47
●​ ULTEM (PEI): While having a lower thermal limit, it has a competitive advantage in
electrical insulation, possessing one of the highest dielectric strengths among
thermoplastics.67

Part 6: Conclusion and Future Research Gaps

This analysis has systematically deconstructed the FDM filament landscape, providing a clear
methodology for navigating material selection. The primary finding is that a "Data Trust
Hierarchy" is essential. An engineer must prioritize data from 3D-printed specimens that
quantifies anisotropy (Z-axis vs. XY strength) and reject simplistic data from injection-molded
samples.
The development of a performance-based taxonomy and a Multi-Criteria Decision-Making
(MCDM) framework provides a quantitative and application-specific "similarity metric" to
replace ambiguous marketing terms. The investigation of substitution rules has debunked
common myths (PLA+ for heat) and identified critical, un-documented failure modes (Nylon
creep).
This report also illuminates several clear research gaps that remain:
1.​ Z-Axis (Interlayer) Data: The single greatest gap is the lack of Z-axis mechanical data
from most filament manufacturers. This data is the most important factor for part design
and failure analysis, and it should be the primary advocacy target for end-users.
2.​ Creep and Hygroscopicity Data: As demonstrated by the "Nylon Trap," time- and


---


## Page 16


environment-dependent properties (creep, moisture absorption) are critical for
engineering applications but are almost never included in a TDS.
3.​ Standardized Composite Characterization: The conflicting data on composite
performance (e.g., PLA-CF) highlights a need for a standardized methodology to
characterize how different polymer matrices and fiber concentrations interact.
The final recommendation is a shift in perspective: The search should not be for the "best
filament," but for the "best data." By implementing a rigorous framework like the MCDM, an
engineer can select the "right material" for a specific application based on a weighted,
quantitative analysis of its true, anisotropic properties.
Works cited
1.​ FDM Nylon 12CF | Stratasys, accessed November 6, 2025,
https://www.stratasys.com/contentassets/fd47e7ef3b284c3e8485338bc7fc75b2/
mds_fdm_nylon-12cf_0824a.pdf?v=4a4ac7
2.​ ePA - eSUN, accessed November 6, 2025,
https://www.esun3d.com/uploads/eSUN_ePA-Filament_TDS_V4.01.pdf
3.​ Everyone gets this Wrong when 3D Printing Carbon Fiber Nylon - YouTube,
accessed November 6, 2025, https://www.youtube.com/watch?v=u8dIpwd6tzo
4.​ Comparing Impact Resistance of 21 Filaments for 3D Printing. : 15 ..., accessed
November 6, 2025,
https://www.instructables.com/Comparing-Impact-Resistance-of-21-Filaments-f
or-3D/
5.​ Which is the MOST RIGID 3D printing material? - YouTube, accessed November 6,
2025, https://www.youtube.com/watch?v=te0Wwf7Dxj4
6.​ Introducing Polymaker's New Technical Data Sheet (TDS), accessed November 6,
2025,
https://polymaker.com/introducing-polymakers-new-technical-data-sheet-tds/
7.​ Technical datasheet - Prusament PLA by Prusa Polymers Identification, accessed
November 6, 2025,
https://prusament.com/wp-content/uploads/2022/10/PLA_Prusament_TDS_2021_1
0_EN.pdf
8.​ Prusament PETG V0 by Prusa Polymers - Technical datasheet, accessed
November 6, 2025,
https://prusament.com/wp-content/uploads/2023/07/PETG_V0_ENG.pdf
9.​ Fused Deposition Modeling | FDM 3D Printing - RapidMade, accessed November
6, 2025, https://rapidmade.com/3d-printing/filament-fdm-guidelines/
10.​Investigation of the Mechanical Properties of a Carbon Fibre-Reinforced Nylon
Filament for 3D Printing - ResearchGate, accessed November 6, 2025,
https://www.researchgate.net/publication/344221492_Investigation_of_the_Mech
anical_Properties_of_a_Carbon_Fibre-Reinforced_Nylon_Filament_for_3D_Printin
g
11.​Investigation of the Mechanical Properties of a Carbon Fibre-Reinforced Nylon
Filament for 3D Printing - MDPI, accessed November 6, 2025,


---


## Page 17


https://www.mdpi.com/2075-1702/8/3/52
12.​Analysis of the Mechanical Properties of 3D-Printed Plastic Samples Subjected to
Selected Degradation Effects - NIH, accessed November 6, 2025,
https://pmc.ncbi.nlm.nih.gov/articles/PMC10146359/
13.​Untitled - Polymaker, accessed November 6, 2025,
https://polymaker.com/wp-content/uploads/lana-downloads/PolySmooth_TDS_V5
.1.pdf
14.​Glass fiber reinforced PLA composite with enhanced mechanical properties,
thermal behavior, and foaming ability | Request PDF - ResearchGate, accessed
November 6, 2025,
https://www.researchgate.net/publication/335793095_Glass_fiber_reinforced_PL
A_composite_with_enhanced_mechanical_properties_thermal_behavior_and_foa
ming_ability
15.​Technical Data Sheets - the Polymaker Wiki!, accessed November 6, 2025,
https://wiki.polymaker.com/polymaker-products/more-about-our-products/docu
ments/technical-data-sheets
16.​Optimisation of Strength Properties of FDM Printed Parts—A Critical Review -
MDPI, accessed November 6, 2025, https://www.mdpi.com/2073-4360/13/10/1587
17.​Optimisation of Strength Properties of FDM Printed Parts—A Critical Review -
PMC, accessed November 6, 2025,
https://pmc.ncbi.nlm.nih.gov/articles/PMC8157110/
18.​Process Design and Parameters Interaction in Material Extrusion 3D Printing: A
Review, accessed November 6, 2025,
https://pmc.ncbi.nlm.nih.gov/articles/PMC10221300/
19.​ULTEM™ 9085 Resin - Stratasys, accessed November 6, 2025,
https://www.stratasys.com/siteassets/materials/materials-catalog/fdm-materials/u
ltem-9085/h2-model-updates/mds_fdm_ultem9085_0924a.pdf?v=4ab5da
20.​FDM Nylon 12CF | Stratasys, accessed November 6, 2025,
https://www.stratasys.com/siteassets/materials/materials-catalog/fdm-materials/n
ylon-12cf/mds_fdm_nylon-12cf_0325a.pdf?v=493d90
21.​ULTEM™ 9085 Resin - Stratasys, accessed November 6, 2025,
https://www.stratasys.com/contentassets/898e7825e3e7492ab8c0370499521596/
mds_fdm_ultem9085_0923a.pdf?v=497d96
22.​3D Printing Filament Guide - 3DMaker Engineering, accessed November 6, 2025,
https://www.3dmakerengineering.com/blogs/3d-printing/3d-printer-filament-gui
de
23.​3D Printer Filament Comparison Guide - MatterHackers, accessed November 6,
2025, https://www.matterhackers.com/3d-printer-filament-compare
24.​3D Printer Filament Comparison Guide | Bambu Lab US, accessed November 6,
2025, https://bambulab.com/en-us/filament/guide
25.​eSUN 3D Printing Material Datasheet - MatterHackers, accessed November 6,
2025, https://www.matterhackers.com/r/oqRtJt
26.​eSUN 3D Filament Properties Guide | PDF - Scribd, accessed November 6, 2025,
https://www.scribd.com/document/391790451/Data-Sheet-for-ESUN-3D-Filamen
t-201411


---


## Page 18


27.​Deformation Characterization of Glass Fiber and Carbon Fiber-Reinforced 3D
Printing Filaments Using Digital Image Correlation - PMC - PubMed Central,
accessed November 6, 2025, https://pmc.ncbi.nlm.nih.gov/articles/PMC11991370/
28.​Deformation Characterization of Glass Fiber and Carbon Fiber-Reinforced 3D
Printing Filaments Using Digital Image Correlation - MDPI, accessed November 6,
2025, https://www.mdpi.com/2073-4360/17/7/934
29.​3D Printing Carbon Fiber and Other Composites - Markforged, accessed
November 6, 2025,
https://markforged.com/resources/learn/design-for-additive-manufacturing-plast
ics-composites/understanding-3d-printing-strength/3d-printing-carbon-fiber-an
d-other-composites
30.​Types of 3D Printer Filaments - Dassault Systèmes, accessed November 6, 2025,
https://www.3ds.com/make/solutions/blog/types-3d-printer-filaments
31.​Glass Fiber vs. Carbon Fiber Filled Filaments: Which Should You Choose -
3DXTech, accessed November 6, 2025,
https://www.3dxtech.com/blogs/featured/glass-fiber-vs-carbon-fiber-filled-filam
ents-which-should-you-choose
32.​How STRONG is 3d printed CARBON FIBER? - YouTube, accessed November 6,
2025, https://www.youtube.com/watch?v=-Qpb0UTywko
33.​Development of Fiber-Reinforced Polymer Composites for Additive
Manufacturing and Multi-Material Structures in Sustainable Applications - MDPI,
accessed November 6, 2025, https://www.mdpi.com/2227-9717/12/10/2217
34.​Carbon fibers prove stronger than Kevlar and glass in FDM 3D prints, accessed
November 6, 2025,
https://3dprintingindustry.com/news/carbon-fibers-prove-stronger-kevlar-glass-
fdm-3d-prints-116852/
35.​All 3D Printing Filament Types Explained – Properties, Printing & Best Uses (2025
Update), accessed November 6, 2025,
https://all3dp.com/1/3d-printer-filament-types-3d-printing-3d-filament/
36.​Complete Guide to 3D Printing Filament Types (PLA, ABS, PETG, TPU & More) -
The BabaBuilds.com Blog, accessed November 6, 2025,
https://bababuilds.com/blog/3d-printer-filament-types-guide/
37.​High-Performance 3D Printing Filaments for Aerospace and Defense - 3DXTech,
accessed November 6, 2025,
https://www.3dxtech.com/blogs/3d-printing-materials/high-performance-3d-prin
ting-filaments-for-aerospace-and-defense
38.​3DGence F420 - Your Guide to PEEK, PEKK and ULTEM Filaments - Additive-X,
accessed November 6, 2025,
https://www.additive-x.com/blog/3dgence-f420-your-guide-to-peek-pekk-and-
ultem-filaments
39.​(PDF) Strategic selection of filament material and print orientation for FDM 3D
printing using integrated evaluation techniques - ResearchGate, accessed
November 6, 2025,
https://www.researchgate.net/publication/396178493_Strategic_selection_of_fila
ment_material_and_print_orientation_for_FDM_3D_printing_using_integrated_eva


---


## Page 19


luation_techniques
40.​Weighting Methods and their Effects on Multi-Criteria Decision Making Model
Outcomes in Water Resources Management | Request PDF - ResearchGate,
accessed November 6, 2025,
https://www.researchgate.net/publication/316081372_Weighting_Methods_and_th
eir_Effects_on_Multi-Criteria_Decision_Making_Model_Outcomes_in_Water_Reso
urces_Management
41.​A decision-making strategy for selection of FDM-based additively manufactured
thermoplastics for industrial applications based on material attributes - DOAJ,
accessed November 6, 2025,
https://doaj.org/article/f7d640cf17954f97952035ac71da28e8
42.​View of A Multi-Criteria Decision-Making Approach for Enhancing Mechanical
Properties of FDM 3D-Printed Part, accessed November 6, 2025,
https://ijiemjournal.uns.ac.rs/index.php/atm/article/view/ATM-2024-1-004/ATM-20
24-1-004
43.​Beyond Datasheets: A Comparative Evaluation of Standard and Technical
Filaments in High-Speed FDM 3D Printing - ResearchGate, accessed November 6,
2025,
https://www.researchgate.net/publication/393112814_Beyond_Datasheets_A_Co
mparative_Evaluation_of_Standard_and_Technical_Filaments_in_High-Speed_FD
M_3D_Printing
44.​Innovative Approaches to Material Selection and Testing in Additive
Manufacturing - NIH, accessed November 6, 2025,
https://pmc.ncbi.nlm.nih.gov/articles/PMC11722173/
45.​Ashby Maps: Evaluating Properties and Cost for Material Selection - Weerg,
accessed November 6, 2025,
https://www.weerg.com/guides/how-to-choose-the-right-material-for-your-pro
duct
46.​Ashby Plot demonstrating the fracture toughness vs. strength of... | Download
Scientific Diagram - ResearchGate, accessed November 6, 2025,
https://www.researchgate.net/figure/Ashby-Plot-demonstrating-the-fracture-tou
ghness-vs-strength-of-polymers6667_fig6_383529701
47.​PEEK vs PEKK vs ULTEM: Choosing the Right Ultra-Polymer for 3D Printing -
3DXTech, accessed November 6, 2025,
https://www.3dxtech.com/blogs/3d-printing-materials/peek-vs-pekk-vs-ultem-ch
oosing-the-right-ultra-polymer-for-3d-printing
48.​The difference of PLA and PLA+ tested! (feat. Polymaker) - CNC Kitchen,
accessed November 6, 2025,
https://www.cnckitchen.com/blog/the-difference-of-pla-and-pla-tested-feat-pol
ymaker
49.​The Benefits of Tough PLA Over Standard PLA Filament - Filamatrix, accessed
November 6, 2025,
https://filamatrix.com/blogs/blogs/the-benefits-of-tough-pla-over-standard-pla-
filament
50.​PolyMax™ PLA - Polymaker, accessed November 6, 2025,


---


## Page 20


https://polymaker.com/product/polymax-pla/
51.​PETG vs PLA vs ABS: 3D Printing Strength Comparison - UltiMaker, accessed
November 6, 2025,
https://ultimaker.com/learn/petg-vs-pla-vs-abs-3d-printing-strength-comparison
/
52.​PETG vs. PLA: What's the Difference? - Xometry, accessed November 6, 2025,
https://www.xometry.com/resources/3d-printing/petg-vs-pla-3d-printing/
53.​PETG vs PLA: Which Filament Is Best for 3D Printing? - Siraya Tech, accessed
November 6, 2025, https://siraya.tech/blogs/news/petg-vs-pla
54.​PLA vs. ABS vs. PETG: A Comprehensive Comparison - Unionfab, accessed
November 6, 2025, https://www.unionfab.com/blog/2024/05/pla-vs-abs-vs-petg
55.​Better performing 3D prints with annealing, but... - Part 1: PLA - CNC Kitchen,
accessed November 6, 2025,
https://www.cnckitchen.com/blog/better-performing-3d-prints-with-annealing-b
ut-part-1-pla
56.​What's the temperature resistance of annealed PLA, PETG and ABS? - YouTube,
accessed November 6, 2025, https://www.youtube.com/watch?v=vLrISrkg46g
57.​How To: Anneal Tough PLA and HTPLA - YouTube, accessed November 6, 2025,
https://www.youtube.com/watch?v=n_bIXgjY-KM
58.​Ultimate 3D Printing Material Properties Table - Simplify 3D, accessed November
6, 2025, https://www.simplify3d.com/resources/materials-guide/properties-table/
59.​Ultimate Materials Guide - Tips for 3D Printing with ASA, accessed November 6,
2025, https://www.simplify3d.com/resources/materials-guide/asa/
60.​3D printer filament types and uses: A comprehensive guide - UltiMaker, accessed
November 6, 2025,
https://ultimaker.com/learn/3d-printer-filament-types-and-uses-a-comprehensiv
e-guide/
61.​The Best ASA 3D Printing Settings Achieving Optimal Results | IN3DTEC |
Prototyping & On-demand manufacturing services, accessed November 6, 2025,
https://www.in3dtec.com/the-best-asa-3d-printing-settings-achieving-optimal-r
esults/
62.​Understanding the Distinctive Properties of ABS and ASA in 3D Printing -
MatterHackers, accessed November 6, 2025,
https://www.matterhackers.com/articles/abs-vs-asa-filament-in-3d-printing
63.​Nylon vs. Polycarbonate filaments - 3D Printing - Rapid Prototyping, accessed
November 6, 2025,
https://www.rapidprototyping.nl/en/3d-printing/materials-and-filaments/nylon-vs-
polycarbonate/
64.​Polycarbonate: Here's how to print it without warping, delamination, or an
enclosure, with better-than-ABS results. - Prusa Forum, accessed November 6,
2025,
https://forum.prusa3d.com/forum/original-prusa-i3-mk3s-mk3-print-tips-archive/
polycarbonate-here-s-how-to-print-it-without-warping-delamination-or-an-enc
losure-with-better-than-abs-results./
65.​Strongest 3D Printer Filament: Choosing Between PC, Nylon, TPU, and Others -


---


## Page 21


Wevolver, accessed November 6, 2025,
https://www.wevolver.com/article/strongest-3d-printer-filament
66.​Need Advice on Polycarbonate vs Nylon : r/3Dprinting - Reddit, accessed
November 6, 2025,
https://www.reddit.com/r/3Dprinting/comments/15abweq/need_advice_on_polyc
arbonate_vs_nylon/
67.​ULTEM vs. PEEK: Comparison of High Performance Technical Polymers - Weerg,
accessed November 6, 2025, https://www.weerg.com/guides/ultem-vs-peek
68.​3D Printing PEEK, PEI and ULTEM - Beamler, accessed November 6, 2025,
https://www.beamler.com/3d-printing-peek-pei-ultem/
69.​K2 Plus Combo - Anyone tried printing with Ultem 9085 ? : r/Creality_k2 - Reddit,
accessed November 6, 2025,
https://www.reddit.com/r/Creality_k2/comments/1iiwl0q/k2_plus_combo_anyone_
tried_printing_with_ultem/
70.​TOPIC FOR PRINTING HT FILAMENTS ( PEEK/ULTEM 1010/ULTEM 9085/PPSU/PSU)
ON UM2+ - Page 2 - Ultimaker forum, accessed November 6, 2025,
https://community.ultimaker.com/topic/20118-topic-for-printing-ht-filaments-pee
kultem-1010ultem-9085ppsupsu-on-um2/page/2/
71.​PEEK vs. Ultem: Choosing the Right High-Performance Plastic for Your
Application, accessed November 6, 2025,
https://www.americanadditive.com/post/peek-vs-ultem


---
