# polymers-15-03787

> **Source:** `polymers-15-03787.pdf`
> **Converted:** 2025-11-22 21:18:08
> **Method:** PyMuPDF

---

## Page 1


Citation: Zisopol, D.G.; T˘anase, M.;
Portoac˘a, A.I. Innovative Strategies
for Technical-Economical
Optimization of FDM Production.
Polymers 2023, 15, 3787. https://
doi.org/10.3390/polym15183787
Academic Editors: Vasile Cojocaru,
Gabriela Mˇarginean and Doina
Frunzăverde
Received: 23 August 2023
Revised: 13 September 2023
Accepted: 14 September 2023
Published: 16 September 2023
Copyright:
© 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
polymers
Article
Innovative Strategies for Technical-Economical Optimization of
FDM Production
Dragos, Gabriel Zisopol
, Maria Tănase *
and Alexandra Ileana Portoacă *
Mechanical Engineering Department, Petroleum-Gas University of Ploies,ti, 100680 Ploiesti, Romania;
zisopold@upg-ploiesti.ro
* Correspondence: maria.tanase@upg-ploiesti.ro (M.T.); alexandra.portoaca@upg-ploiesti.ro (A.I.P.)
Abstract: This article introduces a multi-objective optimization approach for determining the best 3D
printing parameters (layer thickness and inﬁll percentage) to efﬁciently produce PLA and ABS parts,
extensively analyzing mechanical behavior under tests for different traits such as tensile strength,
compression, ﬂexural, impact, and hardness. The value analysis method is used to optimize set-
tings that balance use value (Vi- represented by mechanical characteristics) and production cost
(Cp). Findings reveal that the inﬁll percentage signiﬁcantly inﬂuences the Vi/Cp ratio for tensile,
compression, and hardness tests, while ﬂexural tests are inﬂuenced by layer thickness. Impact
strength is inﬂuenced nearly equally by both factors, with material-speciﬁc variations. The desirabil-
ity function proved useful for optimizing processes with multiple responses, identifying the optimal
parameters for the FDM process: a layer thickness of 0.15 mm with 100% inﬁll percentage for PLA, a
layer thickness of 0.20 mm with 100% inﬁll percentage for annealed PLA, and a layer thickness of
0.15 mm with 100% inﬁll percentage for ABS. Overall, this study guides efﬁcient 3D printing parame-
ter selection through a technical-economic optimization based on value analysis.
Keywords: 3D printing; value analysis; optimization; printing parameters; PLA; ABS; annealing;
mechanical properties
1. Introduction
In the contemporary landscape of additive manufacturing, fused deposition modeling
(FDM) has emerged as a prominent technique, offering novel avenues for design innovation
and production efﬁciency. Out of all the available 3D printing methods, FDM stands out
as an economical and fast printing technique [1]. However, the optimization of FDM
extends beyond technical precision, encompassing economic considerations that underpin
sustainable manufacturing practices. The effectiveness of FDM is inﬂuenced by a range
of process parameters, which can signiﬁcantly affect both the cost and quality of the
3D-printed components [2,3].
While FDM’s capacity for intricate design realization is widely acknowledged, its
optimal implementation necessitates a holistic understanding of the multifaceted param-
eters governing the manufacturing workﬂow. Moreover, the intricate amalgamation of
material utilization, production duration, and mechanical performance within the FDM
framework underscores the signiﬁcance of pioneering strategies that harmonize technical
ﬁnesse with cost-conscious practices. The efﬁcacy of 3D printing, alongside the mechanical
characteristics of the end component, hinge on a spectrum of printing parameters including
layer thickness, printing speed, inﬁll density, ﬁlling pattern, printing material, and various
other factors [4]. The predeﬁned printing process parameters provided by manufacturers
are not guaranteed to produce high-quality printed products, as numerous variables can
inﬂuence the printing procedure. Incorrectly conﬁgured initial printing parameters can
lead to prolonged processing times, avoidable resource consumption, and diminished
tensile strength, and consequently inﬂate production expenses, generate material wastage,
Polymers 2023, 15, 3787. https://doi.org/10.3390/polym15183787
https://www.mdpi.com/journal/polymers


---


## Page 2


Polymers 2023, 15, 3787
2 of 26
and pose challenges for end-users [5–10]. In recent times, a substantial body of research
literature has emerged focused on improving the setup of these parameters.
The study detailed in [4] investigated how different printing settings affect the strength
of 3D-printed objects. Five key parameters, layer thickness, printing speed, inﬁll density,
ﬁlling pattern, and printing material, were analyzed using a design of experiment (DOE)
approach. Multi-objective optimization was applied to enhance mechanical properties
while minimizing time and material usage. The results demonstrated signiﬁcant improve-
ments, reducing printing time by 72.39% and increasing mass by 9.06% while enhancing
mechanical performance.
Maguluri et al. [11] explored the effects of three crucial printing factors—inﬁll density,
extrusion temperature, and printing speed—on the hardness of poly-lactic acid (PLA)
components. The Taguchi design of experiment (DOE) approach was applied to efﬁciently
assess the printing settings that enhance the hardness of the printed parts while minimizing
the number of experiments conducted. The analysis employed signal-to-noise (S/N) ratios
to identify the optimal parameters, and the relative contributions of these factors were
quantiﬁed using analysis of variance (ANOVA). The ﬁndings underscore the signiﬁcant
inﬂuence of extrusion temperature on the hardness of 3D-printed PLA samples, whereas
printing speeds exhibit a comparably minor impact on this property.
The research in [12] investigated the impact of different printing parameters (layer
thickness, build orientation, and raster angle) on the mechanical properties of PLA spec-
imens, using a design of experiment (DOE) approach. The ﬁndings reveal a negative
correlation between layer thickness and ultimate tensile strength (UTS). Higher layer thick-
ness leads to a decrease in mean UTS. A build orientation of 45 degrees tends to exhibit the
highest tensile strength, while the raster angle has a less signiﬁcant impact compared to
the other two process parameters. The maximum observed UTS was 46.65 MPa for a layer
thickness of 0.1 mm, a raster angle of 30 degrees, and a build orientation of 0 degrees.
In [13], the application of a multi-objective optimization was explored to reﬁne the
process parameters (inﬁll patterns, inﬁll percentage, printing speed, and layer thickness)
for FDM 3D printing of PLA components, evaluating surface roughness, printing time, and
ﬁlament length consumed as response variables.
A similar study was performed in [14], with the aim being to examine the impact of
certain input experimental factors, speciﬁcally inﬁll density, layer thickness, and support
style, on response parameters such as the build time of a part and surface roughness for an
acrylonitrile butadiene styrene (ABS) polymer using Taguchi design.
Vishwas et al. [15] focused on assessing how process parameters (model orientation,
layer thickness, and shell thickness) in FDM inﬂuence key characteristics like ultimate
tensile strength and the dimensional accuracy of ABS and nylon materials. Based on
Taguchi analysis, it was highlighted that orientation angle and shell thickness notably
impact ultimate tensile strength and moderately inﬂuence dimensional accuracy, with
a focus on achieving optimal manufacturing outcomes. Similarly, in [16], the ANOVA
analysis emphasized the nozzle diameter as the signiﬁcant factor for a PLA 3D-printed
part’s hardness, while for the tensile strength, the signiﬁcant factor was identiﬁed to be the
printing direction.
Many other studies [5,17–19] have focused on establishing the optimal setting for
printing parameters to enhance the mechanical characteristics of 3D-printed parts.
Sustainable manufacturing aims to integrate quality, environmental consequences, and
cost implications, leading to a shift in the focus of optimization objectives [20]. Therefore,
technical–economical optimization must be considered when analyzing the efﬁciency of
FDM process. In this sense, using value analysis to assess the mechanical characteristics of
3D-printed parts is an important and interesting effort in modern manufacturing. As the
adoption of additive manufacturing expands across various industrial sectors, ensuring the
optimal performance and cost-effectiveness of fabricated parts becomes increasingly imper-
ative. The studies in [21–26] have investigated the cost-effectiveness and the environmental
impact of additive manufacturing.


---


## Page 3


Polymers 2023, 15, 3787
3 of 26
Refocusing on the relationship between production costs and printed component
production, the current emphasis [21] lies on optimizing energy efﬁciency and reducing
expenses in the manufacturing process, particularly in material-extrusion additive manu-
facturing. This is crucial for achieving sustainability and cost-effectiveness in production.
Notably, MEX 3D printing consistently delivers high-quality parts, especially when em-
ploying costly high-performance polymers, which ﬁnd applications in the biomedical,
automotive, and aerospace sectors. In this context, [21] delves into the examination of two
vital parameters, namely energy consumption, which can be translated into production
costs and tensile strength.
The study in [22] used statistical modeling tools to assess various metrics related to
compression and energy consumption in 3D printing. These metrics included printing time,
weight, printing energy consumption, speciﬁc printing energy, speciﬁc printing power,
compression strength, compression modulus of elasticity, and toughness. Among the
factors examined, the layer thickness emerged as the most signiﬁcant control parameter,
while nozzle temperature and raster deposition angle had less impact on the outcomes.
The work detailed in [23] extensively explored the inﬂuence of seven universal and
machine-agnostic 3D-printing conﬁgurations on both the energy usage and mechanical
properties of parts made from PLA using the MEX 3D-printing method. The results
showed that the printing speed and layer thickness had the most signiﬁcant impact on
energy consumption in the study. Additionally, the inﬁll density and orientation angle
were identiﬁed as the primary factors affecting compressive strength.
The investigation performed in [26] found that layer thickness and inﬁll density are
the ﬁrst and the second most important factors in energy consumption, respectively, when
manufacturing 3D-printed parts.
In specialized works, both the term “Value Engineering” and “Value Analysis” are
used, both reﬂecting the same content but at different stages of the product’s existence [27].
Value engineering/analysis represents a method of systematic and creative research and
design that, through a functional approach, aims to design and achieve the functions of the
studied object with minimal expense, in quality conditions that meet the users’ needs, in
line with socio-economic requirements [27].
Starting from social needs and based on the latest advancements in science and
technology, value engineering/analysis studies aim to establish an optimal relationship
between the use value of the analyzed product (Vi) and the direct and indirect production
costs it generates (Cp).
The fundamental relationship that validates the design of a product in the presented
context is [27]:
Vi
Cp
→max
(1)
where Vi is measured in performance units and Cp is expressed in monetary units.
The value of the Vi/Cp ratio can be increased through [27]:
✓
Increasing product performance while maintaining a constant price;
✓
Reducing the price while maintaining constant performance;
✓
Increasing performance more than cost;
✓
Increasing performance levels while reducing costs;
✓
Reducing performance, but with an even greater reduction in cost.
This study brings a novel perspective to this area by applying the value-analysis
concept to enhance the mechanical characteristics of 3D-printed parts through the opti-
mization of process parameters. In the ﬁeld of additive manufacturing research, where the
pursuit of optimal performance and cost-efﬁciency is essential, this approach stands out for
its comprehensive consideration of multiple factors. Existing literature often focuses on
isolated aspects of 3D printing, such as material properties or speciﬁc process parameters.
This study bridges the gap by encompassing a comprehensive evaluation that investigates
mechanical behavior established based on experimental testing (tensile, compression, bend-


---


## Page 4


Polymers 2023, 15, 3787
4 of 26
ing, resilience, hardness) in correlation with the production cost, both for as-built and for
annealed specimens, made from different materials (PLA and ABS).
2. Materials and Methods
The printing parameters affecting the mechanical properties and production cost of 3D-
printed samples are the layer thickness (0.10 mm/0.15 mm/0.20 mm) and inﬁll percentage
(50%/75%/100%). The mechanical properties investigated were previously determined by
the authors of the present work, namely tensile strength [6,9,28], compression strength [8],
ﬂexural strength [7,9], impact strength [29], and hardness [28,30].
A Raise E2 3D printer (Irvine, CA, USA), having a volume capacity of 330 × 240 × 240 mm,
was used for the printing process.
The speciﬁc printing options used in the mentioned studies (Table 1) were: build
orientation X-Y, model lines, and 45◦orientation.
Table 1. The printing parameters described.
Printing Options for 1 Set of Samples
ABS
PLA
Shell width (mm)
1
1
Inﬁll speed (mm/s)
40
70
Estimated print time (min)
60
46
Estimated ﬁlament used (g)
10.60
10.60
Extruder temperature (◦C)
240
210
Bed temperature (◦C)
110
60
Platform addition
Raft only
Raft only
Table 2 presents the provider characteristics extracted from data sheets for the PLA
and ABS ﬁlaments used in the investigation. ABS and PLA ﬁlaments were supplied by
Polymaker (Utrecht, The Netherlands).
Table 2. Characteristics of ﬁlaments from providers’ data sheets.
Materials
Extrusion
Temperature
(◦C)
Bed Temperature
(◦C)
Density
(g/cm3)
Tensile
Strength (MPa)
Speciﬁc
Deformation
(%)
Charpy Impact
Strength (kJ/m2)
PLA
210 ± 10
25–60
1.31 ± 0.02
15.5–72
34.5 ± 8.1
5.7 ± 0.4
ABS
210 + 40
110 ± 10
1.10
33.9
4.8
10.5
For the annealing heat treatment, the samples were kept for a period of 3 h at a
temperature of 75 ◦C, with slow cooling in an oven.
For each investigated mechanical property, a design of experiments (DOE) full factorial
design method was used through Minitab 19 software to optimize the ratio between the
use value and production cost of PLA and ABS 3D-printed samples. For each printing
parameter, three levels were considered, as can be seen in Table 3.
Table 3. Parameters and levels used in DOE analysis.
Parameter
Level
1
2
3
Inﬁll percentage, %
50
75
100
Layer thickness, mm
0.10
0.15
0.20


---


## Page 5


Polymers 2023, 15, 3787
5 of 26
The total number of experiments required is determined by the function of the number
of input factors (n) and the number of levels (k). This resulted, therefore, in an orthogonal
array of 32 values (see Table 4).
Table 4. DOE array.
Experiment
no.
Layer
Thickness,
mm
Inﬁll
Percentage,
%
1
0.10
50
2
75
3
100
4
0.15
50
5
75
6
100
7
0.20
50
8
75
9
100
To calculate the production cost, we used the relation [27]:
Cp = Cmat + Ce
(2)
Cmat = Qmat × Pm
(3)
Ce = Te × Cen × Pen
(4)
where: Cp is the production cost [Euro], Cmat is the cost of material [Euro], Ce is the
cost of energy [Euro], Qmat—material consumption [g] for a single sample, Pm—price of
material [Euro/g], Te—printing time [h], Cen—energy consumption [kW], Pen—the price of
electricity [Euro/kWh].
For the annealed samples, the production cost Cpa was calculated with the formula:
Cpa = Cp + (Ta × Cena × Pen)/ns
(5)
where Cp is the production cost calculated with Formula (1) for the as-built samples, Ta is
the annealing time [h], Cena is the energy consumption of the annealing device [kW], and
ns is the number of samples annealed simultaneously in the oven.
In the calculations, the following values were considered: Cen = 0.35 kW (the en-
ergy consumption of the Raise E2 3D printer), Pm = 0.022 Euro/g (for PLA [31]) and
Pm = 0.021 Euro/g (for ABS [31]), Pen = 0.28 Euro/kWh [32], Ta = 3 h, Cena = 1 kW, ns = 45.
The material consumption and printing time for each 3D-printed sample was taken from
the software of the 3D printer, and the energy consumption for the 3D-printing process and
for annealing, respectively, were taken from the devices’ speciﬁcations.
Testing conditions, such as the shape and dimension of the samples for each experi-
mental investigation performed, are presented in Table 5.


---


## Page 6


Polymers 2023, 15, 3787
6 of 26
Table 5. Testing conditions and types of samples used in the experimental investigation.
Mechanical Test
Testing Conditions
Shape and Dimensions of Specimen
Tensile testing
- electro-mechanical machine
- force cell of 2.5 kN,
- speed of 5 mm/min
- with extensometer
- ambient temperature 20 ◦C
- humidity 40%
Compression testing
MU 400 Kn universal machine
20 N preload
10 mm/min the speed test
ambient temperature 20 ◦C
humidity 40%
Flexural strength testing
Lloyd LRX Force Tester
electro-mechanical
- force cell of 2.5 kN,
- speed of 5 mm/min
- ambient temperature 20 ◦C
humidity 40%
Impact testing
Instron Pendulum Charpy tester
Impact velocity 2.9 m/s
- ambient temperature 20 ◦C
humidity 40%
Hardness testing
Shore D type durometer
ambient temperature 20 ◦C
humidity 40%


---


## Page 7


Polymers 2023, 15, 3787
7 of 26
3. Results and Discussion
3.1. Application of Value Analysis for Analyzing the Mechanical Behavior of ABS and PLA
3D-Printed Materials
3.1.1. Tensile Testing
Tables 6 and 7 show the results of calculations performed using relations (2. . .5), to
determine the production cost for PLA (as-built and annealed PLA A) and ABS samples,
respectively, used for tensile testing.
Table 6. Cost calculation for PLA samples used for tensile testing.
Experiment No.
Cmat, Euro
Ce, Euro
Cp, Euro
Cpa, Euro
1
0.35
0.18
0.52
0.54
2
0.41
0.22
0.62
0.64
3
0.47
0.20
0.67
0.69
4
0.36
0.14
0.50
0.52
5
0.42
0.16
0.58
0.60
6
0.47
0.15
0.63
0.65
7
0.38
0.12
0.50
0.52
8
0.43
0.14
0.56
0.58
9
0.48
0.13
0.61
0.63
Table 7. Cost calculation for ABS samples used for tensile testing.
Experiment No.
Cmat, Euro
Ce, Euro
Cp, Euro
1
0.29
0.21
0.50
2
0.34
0.26
0.60
3
0.39
0.26
0.64
4
0.29
0.16
0.45
5
0.34
0.19
0.52
6
0.38
0.18
0.57
7
0.31
0.13
0.44
8
0.35
0.15
0.50
9
0.48
0.13
0.61
Similar to their impact on mechanical properties, the 3D-printing parameters were
observed to signiﬁcantly inﬂuence the production cost due to energy consumption [25].
Figure 1 illustrates a visual representation that highlights the ratios between use values
(ultimate tensile strength) and production costs, based on the results obtained from tensile
testing conducted on 3D-printed PLA and ABS materials.
Although the heat treatment adds supplementary costs to the production, the results
from Figure 1 shows that, in all analyzed cases, the annealed PLA consistently exhibits
the highest ratios, because of its improved mechanical performance, followed by as-built
PLA and then ABS, indicating that annealed PLA might provide the best balance between
functional performance and production cost, in the case of tensile characteristics. The
highest ratio is obtained for 0.15 mm layer thickness and 100% inﬁll percentage for all the
considered materials.
The data from Table 8 indicate that, in the case of tensile specimens, the ratio Vi/Cp
increased from 11.65% to 32.29%, based on increasing performance more than cost (the
production cost of annealed specimens increased from 2.79% to 3.74%, but the ultimate
tensile strength increased from 15.80% to 36.25%).


---


## Page 8


Polymers 2023, 15, 3787
8 of 26

Figure 1. Ratios between use values and production costs in the case of tensile testing of 3D-printed
materials.
Table 8. Percentage differences between as-built and annealed samples for PLA tensile specimens.
Experiment
No.
Difference, %
Ultimate Tensile Strength
Cp
Vi/Cp
1
25.82
3.56
21.50
2
36.25
2.99
32.29
3
31.04
2.79
27.48
4
15.80
3.71
11.65
5
24.01
3.22
20.15
6
19.91
2.97
16.45
7
15.52
3.74
11.35
8
18.47
3.31
14.67
9
17.00
3.07
13.51
It was found from Figure 2 that for all analyzed materials, the highest Vi/Cp ratio was
obtained at 100% inﬁll percentage and 0.15 mm layer thickness (for as-built and annealed
PLA) and 0.20 mm (for ABS, where it can also be observed that the ratio Vi/Cp increased
with the increase in inﬁll percentage). The ANOVA analysis (performed with Minitab 19
software and setting the p-value at the conventional threshold of 0.05) revealed that the
statistically signiﬁcant factor inﬂuencing the ratio Vi/Cp for tensile strength is the inﬁll
percentage. The same conclusion can be drawn from Pareto charts presented in Figure 3.
In contrast to the ﬁndings reported in [24], where layer thickness exhibited the primary
inﬂuence on energy consumption, followed by inﬁll density, the current study identiﬁes
that the ratio Vi/Cp is notably more inﬂuenced by variations in inﬁll percentage.


---


## Page 9


Polymers 2023, 15, 3787
9 of 26


(a)
(b)

(c)
Figure 2. Main effect plots for tensile strength: (a) PLA; (b) PLA A; (c) ABS.
3.1.2. Compression Testing
Tables 9 and 10 show the results of calculations performed using relations (2. . .5), to
determine the production cost for PLA and ABS samples, respectively, used for compression
testing.
Compared with [22], where energy consumption was evaluated and it was found that
the energy is drastically reduced with an increase in layer thickness, in Table 10 the same
trend is found in the costs calculated.


(a)
(b)
Figure 3. Cont.


---


## Page 10


Polymers 2023, 15, 3787
10 of 26

(c)
Figure 3. Pareto charts for tensile strength: (a) PLA; (b) PLA A; (c) ABS.
Table 9. Cost calculation for PLA samples used for compression testing.
Experiment No.
Cmat, Euro
Ce, Euro
Cp, Euro
Cpa, Euro
1
0.05
0.04
0.09
0.11
2
0.06
0.04
0.10
0.12
3
0.07
0.04
0.11
0.12
4
0.05
0.03
0.08
0.10
5
0.06
0.03
0.09
0.11
6
0.07
0.03
0.09
0.11
7
0.05
0.02
0.07
0.09
8
0.06
0.02
0.08
0.10
9
0.07
0.02
0.09
0.11
Table 10. Cost calculation for ABS samples used for compression testing.
Experiment No.
Cmat, Euro
Ce, Euro
Cp, Euro
1
0.04
0.04
0.08
2
0.05
0.05
0.10
3
0.05
0.05
0.10
4
0.04
0.03
0.07
5
0.05
0.03
0.08
6
0.05
0.03
0.09
7
0.04
0.02
0.06
8
0.05
0.03
0.07
9
0.05
0.03
0.08
Figure 4 represents a graphical image showcasing the ratios between use values (com-
pressive stress) and production costs, speciﬁcally focusing on the outcomes of compression
testing for PLA and ABS 3D-printed materials.
The data in Table 11 reveals that, when constructing compression specimens, the
ratio of Vi (performance) to Cp (production cost) decreased by 6.14% to 25.1%. This
decrease occurred because the increase in performance was less pronounced than the rise in
production costs. Speciﬁcally, for annealed specimens, production costs increased between
17.74% and 25.52%, while compressive stress increased by 5.78% to 13.84%. Notably, the
only exception was observed in the case of specimens with a 0.1 mm layer thickness


---


## Page 11


Polymers 2023, 15, 3787
11 of 26
and 100% inﬁll percentage, where the compressive stress was 5.88% lower for annealed
specimens compared to the as-built ones.

Figure 4. Ratios between use values and production costs in the case of compression testing of
3D-printed materials.
Table 11. Percentage differences between as-built and annealed samples for PLA compression
specimens.
Experiment no.
Difference, %
Compressive Stress
Cp
Vi/Cp
1
5.78
20.84
−14.24
2
9.36
18.04
−7.93
3
−5.88
17.74
−25.10
4
13.84
23.33
−8.34
5
13.60
20.57
−6.14
6
13.02
19.98
−6.16
7
13.07
25.52
−11.01
8
9.72
22.25
−11.42
9
10.29
20.57
−9.33
The graphs from Figure 5 show that for all analyzed materials, the highest Vi/Cp
ratio was obtained at 100% inﬁll percentage and 0.20 mm layer thickness (for as-built
PLA and ABS) and 0.15 mm (for annealed PLA). Also, for all analyzed materials, the ratio
Vi/Cp increased with the increase in inﬁll percentage. The ANOVA analysis and Pareto
charts (Figure 6) reveal that the statistically signiﬁcant factor inﬂuencing the Vi/Cp ratio for


---


## Page 12


Polymers 2023, 15, 3787
12 of 26
compression strength is the inﬁll percentage. The same observation was formulated in [26],
where it was found that, in terms of compressive strength, the inﬁll density emerged as the
primary inﬂuencing factor.


(a)
(b)

(c)
Figure 5. Main effect plots for compression strength: (a) PLA; (b) PLA A; (c) ABS.
3.1.3. Flexural Strength Testing
Tables 12 and 13 show the results of calculations performed using relations (2. . .5), to
determine the production cost for PLA and ABS samples, respectively, used for ﬂexural
strength testing.
Table 12. Cost calculation for PLA samples used for ﬂexural strength testing.
Experiment No.
Cmat, Euro
Ce, Euro
Cp, Euro
Cpa, Euro
1
0.12
0.05
0.17
0.19
2
0.13
0.06
0.19
0.21
3
0.13
0.06
0.19
0.21
4
0.12
0.04
0.17
0.18
5
0.13
0.05
0.18
0.19
6
0.13
0.05
0.18
0.20
7
0.13
0.04
0.16
0.18
8
0.13
0.04
0.17
0.19
9
0.13
0.04
0.17
0.19


---


## Page 13


Polymers 2023, 15, 3787
13 of 26
Figure 7 provides a comparative visualization of the ratios between use values (ﬂexural
strength) and production costs, speciﬁcally in the context of ﬂexural testing for PLA and
ABS 3D-printed materials.


(a)
(b)

(c)
Figure 6. Pareto charts for compression strength: (a) PLA; (b) PLA A; (c) ABS.
Table 13. Cost calculation for ABS samples used for ﬂexural strength testing.
Experiment No.
Cmat, Euro
Ce, Euro
Cp, Euro
1
0.09
0.06
0.15
2
0.10
0.08
0.17
3
0.11
0.08
0.18
4
0.09
0.05
0.14
5
0.10
0.06
0.15
6
0.11
0.06
0.16
7
0.09
0.04
0.13
8
0.10
0.05
0.14
9
0.11
0.05
0.15


---


## Page 14


Polymers 2023, 15, 3787
14 of 26
The obtained results indicating the notable inﬂuence of the 3D-printing conﬁgura-
tions on the ﬂexural strength of 3D-printed components are in good agreement with the
observations from [25].
The information extracted from Table 14 reveals that in the context of ﬂexural speci-
mens, the ratio Vi/Cp shows remarkable similarity between annealed and as-built specimens.
This similarity is demonstrated by minimal ﬂuctuations, with slight increases ranging from
1.59% to 4.63%, or decreases spanning from 0.95% to 7.68%. This phenomenon arises
because the increase in ﬂexural strength for annealed samples closely parallels the corre-
sponding rise in their production costs. Essentially, the incremental cost of production for
annealed specimens corresponds closely with their enhanced ﬂexural strength, resulting in
a ﬁnely balanced Vi/Cp ratio between the two specimen types.

Figure 7. Ratios between use values and production costs in the case of ﬂexural testing of 3D-printed
materials.
Table 14. Percentage differences between as-built and annealed samples for PLA ﬂexural specimens.
Experiment No.
Difference, %
Flexural Strength
Cp
Vi/Cp
1
9.88
10.93
−0.95
2
11.66
9.91
1.59
3
8.10
9.57
−1.34
4
16.37
11.29
4.57
5
2.12
10.61
−7.68
6
10.20
10.36
−0.14
7
16.72
11.55
4.63
8
8.05
11.17
−2.81
9
15.23
10.89
3.92


---


## Page 15


Polymers 2023, 15, 3787
15 of 26
Analyzing the graphs shown in Figure 8, it can be observed that the highest ratio Vi/Cp
was obtained at 0.20 mm layer thickness (for as-built and annealed PLA, where the ratio
Vi/Cp increased with the increase in layer thickness) and at 0.20 mm layer thickness (for ABS,
where the ratio Vi/Cp decreased with the increase in layer thickness). The ANOVA analysis
and Pareto charts (Figure 9) revealed that the statistically signiﬁcant factor inﬂuencing the
ratio Vi/Cp for ﬂexural strength is the layer thickness.


(a)
(b)

(c)
Figure 8. Main effect plots for ﬂexural strength: (a) PLA; (b) PLA A; (c) ABS.
3.1.4. Impact Testing
Tables 15 and 16 show the results of calculations performed using relations (2. . .5) to
determine the production cost for PLA and ABS samples, respectively, used for impact
testing.
Figure 10 illustrates the contrast in use value (impact energy) to production cost ratios
for the analyzed parts built for impact testing. This visual representation provides insight
into the cost-effectiveness and performance balance of these three materials.
The data in Table 17 reveal a signiﬁcant increase in the Vi/Cp ratio for impact testing
specimens, ranging from 91.05% to 247.66%. This substantial rise results from the notable
improvement in performance outweighing cost increments. Speciﬁcally, the production
cost for annealed specimens rose moderately, between 9.67% and 12.11%, whereas their
impact energy surged signiﬁcantly, ranging from 114.11% to 283.73%.


---


## Page 16


Polymers 2023, 15, 3787
16 of 26

(a)
(b)

(c)
Figure 9. Pareto charts for ﬂexural strength: (a) PLA; (b) PLA A; (c) ABS.
Table 15. Cost calculation for PLA samples used for impact testing.
Experiment No.
Cmat, Euro
Ce, Euro
Cp, Euro
Cpa, Euro
1
0.11
0.06
0.16
0.18
2
0.12
0.07
0.19
0.21
3
0.13
0.06
0.19
0.21
4
0.11
0.04
0.15
0.17
5
0.12
0.05
0.17
0.19
6
0.13
0.05
0.18
0.20
7
0.12
0.04
0.15
0.17
8
0.13
0.04
0.17
0.18
9
0.14
0.04
0.18
0.19
In the case of impact strength analysis, both layer thickness and infill percentage influence
the Vi/Cp ratio almost equally, with a slightly higher contribution of layer thickness (for PLA
and ABS) and, respectively, infill percentage (for annealed PLA)—see Figures 11 and 12. The
inﬁll percentage increase results in increasing the ratio Vi/Cp in the case of annealed PLA,
while for as-built PLA specimens, the ratio decreases with the increase in inﬁll percentage.
For both as-built PLA and ABS materials, the increase in the ratio Vi/Cp is obtained by
increasing layer thickness.


---


## Page 17


Polymers 2023, 15, 3787
17 of 26
Table 16. Cost calculation for ABS samples used for impact testing.
Experiment No.
Cmat, Euro
Ce, Euro
Cp, Euro
1
0.09
0.06
0.15
2
0.10
0.08
0.18
3
0.11
0.08
0.19
4
0.09
0.05
0.14
5
0.10
0.06
0.16
6
0.11
0.06
0.17
7
0.09
0.04
0.13
8
0.10
0.05
0.15
9
0.11
0.05
0.16

Figure 10. Ratios between use values and production costs in the case of impact testing of 3D-printed
materials.


(a)
(b)
Figure 11. Cont.


---


## Page 18


Polymers 2023, 15, 3787
18 of 26

(c)
Figure 11. Main effect plots for impact strength: (a) PLA; (b) PLA A; (c) ABS.
Table 17. Percentage differences between as-built and annealed samples for PLA impact testing
specimens.
Experiment No.
Difference, %
Impact Energy
Cp
Vi/Cp
1
125.08
11.43
101.99
2
157.63
10.02
134.17
3
181.30
9.67
156.49
4
114.11
12.07
91.05
5
213.64
10.84
182.96
6
283.73
10.37
247.66
7
148.98
12.11
122.09
8
152.84
11.23
127.32
9
238.83
10.63
206.27
3.1.5. Hardness Testing
Tables 18 and 19 show the results of calculations performed using relations (2. . .5) to
determine the production cost for PLA and ABS samples, respectively, used for hardness
testing.
Table 18. Cost calculation for PLA samples used for hardness testing.
Experiment No.
Cmat, Euro
Ce, Euro
Cp, Euro
Cpa, Euro
1
0.35
0.18
0.52
0.54
2
0.41
0.22
0.62
0.64
3
0.05
0.20
0.25
0.69
4
0.36
0.14
0.50
0.52
5
0.42
0.16
0.58
0.60
6
0.47
0.15
0.63
0.65
7
0.38
0.12
0.50
0.52
8
0.43
0.14
0.56
0.58
9
0.48
0.13
0.61
0.63


---


## Page 19


Polymers 2023, 15, 3787
19 of 26

(a)
(b)

(c)
Figure 12. Pareto charts for impact strength: (a) PLA; (b) PLA A; (c) ABS.
Table 19. Cost calculation for ABS samples used for hardness testing.
Experiment No.
Cmat, Euro
Ce, Euro
Cp, Euro
1
0.29
0.21
0.50
2
0.34
0.26
0.60
3
0.39
0.26
0.64
4
0.29
0.16
0.45
5
0.34
0.19
0.52
6
0.38
0.18
0.57
7
0.31
0.13
0.44
8
0.35
0.15
0.50
9
0.39
0.15
0.55
The Vi/Cp ratio is visually emphasized in Figure 13, aiding in the comprehensive
evaluation of these materials based on their hardness characteristics (the use value is
represented in this case by Shore D hardness).


---


## Page 20


Polymers 2023, 15, 3787
20 of 26
Figure 13. Ratios between use values and production costs in the case of hardness testing of 3D-
printed materials.
The information from Table 20 reveals that, in the context of hardness testing specimens
for PLA, the Vi/Cp ratio exhibited a decline ranging from 8.34% to 15.57%. This reduction
is attributed to the fact that the Shore D hardness values of annealed PLA specimens
were consistently lower, decreasing by 5.08% to 12.86%. Concurrently, the production cost
increased marginally, by 2.79% to 3.74%.
Table 20. Percentage differences between as-built and annealed samples for PLA hardness testing
specimens.
Experiment No.
Difference, %
Shore D Hardness
Cp
Vi/Cp
1
−5.08
3.56
−8.34
2
−7.23
2.99
−9.92
3
−9.73
2.79
−12.17
4
−8.71
3.71
−11.98
5
−12.86
3.22
−15.57
6
−12.73
2.97
−15.25
7
−6.49
3.74
−9.86
8
−6.82
3.31
−9.80
9
−8.38
3.07
−11.11
The main effect plots from Figure 14 and Pareto charts from Figure 15 show that
the main factor inﬂuencing the ratio Vi/Cp is the inﬁll percentage, for all the analyzed


---


## Page 21


Polymers 2023, 15, 3787
21 of 26
materials. For PLA the highest ratio is obtained with 0.15 mm layer thickness and 50% inﬁll
percentage, for annealed PLA at 0.20 mm layer thickness and 50% inﬁll percentage and for
ABS at 0.20 mm layer thickness and 50% inﬁll percentage.


(a)
(b)

(c)
Figure 14. Main effect plots for hardness: (a) PLA; (b) PLA A; (c) ABS.

(a)
(b)
Figure 15. Cont.


---


## Page 22


Polymers 2023, 15, 3787
22 of 26
(c)
Figure 15. Pareto charts for hardness: (a) PLA; (b) PLA A; (c) ABS.
3.2. Multi-Response Optimization Using Desirability Function Based on Value Analysis for
Enhancing the 3D-Printing Efﬁciency of PLA and ABS Materials
The objectives of optimization typically involve maximizing, minimizing, or setting
target values for a response in order to identify the most favorable processing parameters.
In the context of desirability analysis, the objective of the present investigation (for each
analyzed material) was to maximize the response desirability, namely the ratio between the
use value and production cost (see Table 21), simultaneously for all mechanical characteris-
tics determined previously. Using the process parameters and responses investigated in
this study, an optimization approach was applied utilizing the desirability function through
Minitab 19 software. Speciﬁc optimization goals have been set for the various responses, all
of which are aimed maximizing their values. Hence, optimization objectives are established
to attain the maximal values for these responses.
Table 21. Optimization Goals for analyzed materials.
Response,
Vi/Cp
Goal
Lower
Target
Weight
Importance
PLA
PLA A
ABS
PLA
PLA A
ABS
Hardness,
[Shore D
hardness/Euro]
Maximum
125.37
110.111
91.73
171.92
151.33
140.94
1
1
Impact,
[J/Euro]
0.40
0.889
1.32
0.50
1.56
2.08
Flexural,
[MPa/Euro]
553.49
546.066
363.17
653.72
673.24
486.46
Compression,
[MPa/Euro]
386.33
338.179
268.93
678.70
635.11
653.83
Tensile,
[MPa/Euro]
42.26
53.132
27.06
63.82
74.32
62.35
Desirability analysis provides values within a range of zero to one, with one indicating
the highest level of suitability.
For the case when the importance is the same for each response, the composite desir-
ability D is calculated with the formula [3]:
D = (d1 · d2 · . . . · dn)1/n
(6)


---


## Page 23


Polymers 2023, 15, 3787
23 of 26
where n is the number of responses, di represents the desirability for each individual
response, calculated (for the case when the goal is to maximize the response desirability) as
in [3]:
di = 0, i f yi < Li
di = (yi−Li)·ri
(Ti−Li) , i f Li ≤yi ≤Ti
di = 1, i f yi > Ti
(7)
yi, Ti, Li represent the predicted value, target value, and lowest value, respectively, of
the analyzed response of response. To maintain simplicity, the authors treated all responses
as equally signiﬁcant within the optimization procedure (both weight and importance val-
ues were set to one, which means all the variables are equally relevant for the optimization
process, as seen in Table 21).
Table 22 displays the rankings assigned to various options concerning the printing
parameters for the three materials. The top-ranked option represents the most suitable
choice for conﬁguring these parameters to achieve the highest possible ratio between use
value and production cost across all responses, as deﬁned in [2,26].
Table 22. Composite Desirability and Ranks.
Printing
Parameters
Material
PLA
PLA A
ABS
Layer
Thickness,
mm
Inﬁll
Percentage,
%
Composite
Desirability
Rank
Composite
Desirability
Rank
Composite
Desirability
Rank
0.10
50
0.0092
7
0.0000
9
0.0000
7
75
0.0000
9
0.2664
5
0.0252
6
100
0.0000
9
0.0002
7
0.0000
7
0.15
50
0.3302
6
0.2528
6
0.3840
4
75
0.4318
4
0.3681
3
0.0000
7
100
0.6026
1 *
0.6121
2
0.6187
1 *
0.20
50
0.4298
5
0.0000
9
0.5058
2
75
0.5093
3
0.3209
4
0.4674
3
100
0.5909
2
0.6213
1 *
0.3690
5
* the highlighted lines correspond to the optimal values (having Rank 1) of printing parameters.
The optimization plot (Figure 16) illustrates how each factor (columns) inﬂuences
the responses or composite desirability (rows). Vertical red lines on the graph indicate
the current factor settings, while the numbers at the top of each column, displayed in
red, denote the current factor level settings. The horizontal blue lines and accompanying
numbers represent the responses corresponding to the current factor level.
In the case of PLA material, the optimization process yielded speciﬁc parameter
values, namely a layer thickness of 0.15 mm and a 100% inﬁll percentage, which are visually
depicted in red on the optimization plot in Figure 16. Meanwhile, for annealed PLA
material, the optimal parameters consist of a 0.20 mm layer thickness and a 100% inﬁll
percentage. Lastly, for ABS material, the optimized parameters encompass a 0.15 mm layer
thickness and a 100% inﬁll percentage. A similar investigation was performed in [3], and,
based on desirability analysis, established the optimal FDM process parameters (layer
thickness, speed, and inﬁll percentage) corresponding to minimal values of responses
(time, weight of product, and ﬁlament length). Regarding the multiobjective optimization,
distinct combinations of printing parameters were established in [20] to enhance various
aspects such as dimensional accuracy, carbon dioxide emissions, material cost, labor cost,
and electricity cost.


---


## Page 24


Polymers 2023, 15, 3787
24 of 26



(a)
(b)
(c)
Figure 16. Optimization plots for 3D-printed materials: (a) PLA; (b) PLA A; (c) ABS.
4. Conclusions
This study introduced a multi-objective optimization approach aimed at identifying
the optimal 3D-printing parameters (layer thickness and inﬁll percentage) for achieving
the highly efﬁcient production of PLA and ABS 3D-printed parts, based on a complex
characterization of their main mechanical properties (tensile strength, compression strength,
ﬂexural strength, impact strength, and hardness). The investigation used an innovative
solution involving value analysis to establish the optimal printing settings that result in
maximizing the ratio between the use value (associated with mechanical characteristics)
and the production cost of 3D-printed products. In this way, a technical-economical
optimization can be performed.
Based on the obtained results, the following conclusions can be drawn:
✓
For the FDM process under investigation, taking into account the mechanical char-
acteristics (tensile strength, compression strength, ﬂexural strength, impact strength,
hardness) and the use value and production cost of specimens made of different
materials, the optimum parameters were found.
✓
The ANOVA analysis demonstrated that the inﬁll percentage is the signiﬁcant factor
with statistical inﬂuence on the Vi/Cp ratio in the case of tensile, compression, and
hardness testing specimens, while for ﬂexural testing specimens, the layer thickness
makes the most important contribution. When analyzing impact strength, both
layer thickness and inﬁll percentage exhibit nearly equal inﬂuence on the Vi/Cp ratio.
However, for PLA and ABS materials, layer thickness holds a slightly greater impact,
while for annealed PLA, the inﬁll percentage has a slightly higher inﬂuence.
✓
Annealing has been proven to signiﬁcantly enhance some mechanical characteristics
of PLA 3D-printed parts. In order to obtain a favorable ratio between mechanical
performance and production cost, a certain number of samples must be heat-treated
simultaneously for an efﬁcient use of energy. The gains in mechanical strength per
piece, combined with the efﬁcient use of energy and time during annealing, contribute
positively to the cost-effectiveness of the process.


---


## Page 25


Polymers 2023, 15, 3787
25 of 26
✓
Prospective investigations within this domain necessitate a targeted assessment of
value, centered on the speciﬁc applications demanded, with a keen focus on enhancing
both utility and production-cost efﬁciency for industry-speciﬁc components. To
enhance the rigor of future studies, it would be useful to use precise measurements
for factors such as energy consumption and labor costs.
Author Contributions: Conceptualization, D.G.Z., A.I.P. and M.T.; methodology, D.G.Z., M.T. and
A.I.P.; validation, D.G.Z.; formal analysis, D.G.Z.; investigation, D.G.Z., M.T. and A.I.P.; resources,
D.G.Z., M.T. and A.I.P.; writing—original draft preparation, A.I.P. and M.T.; writing—review and
editing, A.I.P. and M.T.; visualization A.I.P., M.T. and D.G.Z.; supervision, D.G.Z. All authors have
read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data are contained within the article.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Kumar, K.; Singh, H. Multi-Objective Optimization of Fused Deposition Modeling for Mechanical Properties of Biopolymer Parts
Using the Grey-Taguchi Method. Chin. J. Mech. Eng. 2023, 36, 30. [CrossRef]
2.
Wang, S.; Daelemans, L.; Fiorio, R.; Gou, M.; D’hooge, D.R.; De Clerck, K.; Cardon, L. Improving Mechanical Properties
for Extrusion-Based Additive Manufacturing of Poly(Lactic Acid) by Annealing and Blending with Poly(3-Hydroxybutyrate).
Polymers 2019, 11, 1529. [CrossRef]
3.
D’Addona, D.M.; Raykar, S.J.; Singh, D.; Kramar, D. Multi Objective Optimization of Fused Deposition Modeling Process
Parameters with Desirability Function. Procedia CIRP 2021, 99, 707–710. [CrossRef]
4.
Pereira, R.J.R.; de Almeida, F.A.; Gomes, G.F. A multiobjective optimization parameters applied to additive manufacturing:
DOE-based approach to 3D printing. Structures 2023, 55, 1710–1731. [CrossRef]
5.
Nguyen, V.H.; Huynh, T.N.; Nguyen, T.P.; Tran, T.T. Single and Multi-objective Optimization of Processing Parameters for Fused
Deposition Modeling in 3D Printing Technology. Int. J. Automot. Mech. Eng. 2020, 17, 7542–7551. [CrossRef]
6.
Portoaca, A.; Nae, I.; Zisopol, D.G.; Ramadan, I. Studies on the inﬂuence of FFF parameters on the tensile properties of samples
made of ABS. IOP Conf. Ser. Mater. Sci. Eng. 2022, 1235, 012008. [CrossRef]
7.
Zisopol, D.G.; Nae, I.; Portoaca, A.I.; Ramadan, I. A Statistical Approach of the Flexural Strength of PLA and ABS 3D Printed
Parts. Eng. Technol. Appl. Sci. Res. 2022, 12, 8248–8252. [CrossRef]
8.
Zisopol, D.G.; Nae, I.; Portoaca, A.I. Compression Behavior of FFF Printed Parts Obtained by Varying Layer Height and Inﬁll
Percentage. Eng. Technol. Appl. Sci. Res. 2022, 12, 9747–9751. [CrossRef]
9.
Zisopol, D.G.; Portoaca, A.I.; Nae, I.; Ramadan, I. A Comparative Analysis of the Mechanical Properties of Annealed PLA. Eng.
Technol. Appl. Sci. Res. 2022, 12, 8978–8981. [CrossRef]
10.
Frunzaverde, D.; Cojocaru, V.; Ciubotariu, C.-R.; Miclosina, C.-O.; Ardeljan, D.D.; Ignat, E.F.; Marginean, G. The Inﬂuence of
the Printing Temperature and the Filament Color on the Dimensional Accuracy, Tensile Strength, and Friction Performance of
FFF-Printed PLA Specimens. Polymers 2022, 14, 1978. [CrossRef]
11.
Maguluri, N.; Suresh, G.; Guntur, S.R. Effect of printing parameters on the hardness of 3D printed poly-lactic acid parts using
DOE approach. IOP Conf. Ser. Mater. Sci. Eng. 2022, 1248, 012004. [CrossRef]
12.
Lokesh, N.; Praveena, B.A.; Sudheer Reddy, J.; Vasu, V.K.; Vijaykumar, S. Evaluation on effect of printing process parameter
through Taguchi approach on mechanical properties of 3D printed PLA specimens using FDM at constant printing temperature.
Mater. Today Proc. 2022, 52, 1288–1293. [CrossRef]
13.
Patil, P.; Singh, D.; Raykar, S.J.; Bhamu, J. Multi-objective optimization of process parameters of Fused Deposition Modeling
(FDM) for printing Polylactic Acid (PLA) polymer components. Mater. Today Proc. 2021, 45, 4880–4885. [CrossRef]
14.
Wankhede, V.; Jagetiya, D.; Joshi, A.; Chaudhari, R. Experimental investigation of FDM process parameters using Taguchi analysis.
Mater. Today Proc. 2020, 27, 2117–2120. [CrossRef]
15.
Vishwas, M.; Basavaraj, C.K.; Vinyas, M. Experimental Investigation using Taguchi Method to Optimize Process Parameters of
Fused Deposition Modeling for ABS and Nylon Materials. Mater. Today Proc. 2018, 5, 7106–7114. [CrossRef]
16.
Tamas,ag, I.; Bes,liu-Băncescu, I.; Severin, T.-L.; Dulucheanu, C.; Cerlincă, D.-A. Experimental Study of In-Process Heat Treatment
on the Mechanical Properties of 3D Printed Thermoplastic Polymer PLA. Polymers 2023, 15, 2367. [CrossRef] [PubMed]
17.
Jackson, B.; Fouladi, K.; Eslami, B. Multi-Parameter Optimization of 3D Printing Condition for Enhanced Quality and Strength.
Polymers 2022, 14, 1586. [CrossRef]


---


## Page 26


Polymers 2023, 15, 3787
26 of 26
18.
John, J.; Devjani, D.; Ali, S.; Abdallah, S.; Pervaiz, S. Optimization of 3D printed polylactic acid structures with different inﬁll
patterns using Taguchi-grey relational analysis. Adv. Ind. Eng. Polym. Res. 2023, 6, 62–78. [CrossRef]
19.
Camposeco-Negrete, C. Optimization of printing parameters in fused deposition modeling for improving part quality and
process sustainability. Int. J. Adv. Manuf. Technol. 2020, 108, 2131–2147. [CrossRef]
20.
Yang, C.-J.; Wu, S.-S. Sustainable Manufacturing Decisions through the Optimization of Printing Parameters in 3D Printing. Appl.
Sci. 2022, 12, 10060. [CrossRef]
21.
Vidakis, N.; Petousis, M.; Mountakis, N.; Karapidakis, E. Box-Behnken modeling to quantify the impact of control parameters on
the energy and tensile efﬁciency of PEEK in MEX 3D-printing. Heliyon 2023, 9, e18363. [CrossRef] [PubMed]
22.
Petousis, M.; Vidakis, N.; Mountakis, N.; Karapidakis, E.; Moutsopoulou, A. Compressive response versus power consumption of
acrylonitrile butadiene styrene in material extrusion additive manufacturing: The impact of seven critical control parameters. Int.
J. Adv. Manuf. Technol. 2023, 126, 1233–1245. [CrossRef]
23.
Vidakis, N.; Petousis, M.; Karapidakis, E.; Mountakis, N.; David, C.; Sagris, D. Energy consumption versus strength in MEX 3D
printing of polylactic acid. Adv. Ind. Manuf. Eng. 2023, 6, 100119. [CrossRef]
24.
Vidakis, N.; Petousis, M.; Mountakis, N.; Moutsopoulou, A.; Karapidakis, E. Energy Consumption vs. Tensile Strength of
Poly[methyl methacrylate] in Material Extrusion 3D Printing: The Impact of Six Control Settings. Polymers 2023, 15, 845.
[CrossRef] [PubMed]
25.
Petousis, M.; Vidakis, N.; Mountakis, N.; Karapidakis, E.; Moutsopoulou, A. Functionality Versus Sustainability for PLA in MEX
3D Printing: The Impact of Generic Process Control Factors on Flexural Response and Energy Efﬁciency. Polymers 2023, 15, 1232.
[CrossRef]
26.
Vidakis, N.; Petousis, M.; David, C.N.; Sagris, D.; Mountakis, N.; Karapidakis, E. Mechanical Performance over Energy
Expenditure in MEX 3D Printing of Polycarbonate: A Multiparametric Optimization with the Aid of Robust Experimental Design.
J. Manuf. Mater. Process. 2023, 7, 38. [CrossRef]
27.
Zisopol, D.G. Ingineria valorii; Editura Universităt,ii Petrol-Gaze din Ploies,ti: Ploie¸sti, Romania, 2004; ISBN 973-7965-96-5.
28.
Zisopol, D.G.; Nae, I.; Portoaca, A.I.; Ramadan, I. A Theoretical and Experimental Research on the Inﬂuence of FDM Parameters
on Tensile Strength and Hardness of Parts Made of Polylactic Acid. Eng. Technol. Appl. Sci. Res. 2021, 11, 7458–7463. [CrossRef]
29.
Zisopol, D.G.; Ion, N.; Portoaca, A.I. Comparison of the Charpy Resilience of Two 3D Printed Materials: A Study on the Impact
Resistance of Plastic Parts. Eng. Technol. Appl. Sci. Res. 2023, 13, 10781–10784. [CrossRef]
30.
Portoacă, A.I.; Ripeanu, R.G.; Dinit,ă, A.; Tănase, M. Optimization of 3D Printing Parameters for Enhanced Surface Quality and
Wear Resistance. Polymers 2023, 15, 3419. [CrossRef]
31.
Homepage. Available online: https://formwerk.ro/ (accessed on 7 September 2023).
32.
Eurostat Statistics Explained. Electricity Price Statistics. Available online: https://ec.europa.eu/eurostat/statistics-explained/
index.php?title=Electricity_price_statistics (accessed on 5 September 2023).
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.


---
