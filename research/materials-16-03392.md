# materials-16-03392

> **Source:** `materials-16-03392.pdf`
> **Converted:** 2025-11-22 21:18:06
> **Method:** PyMuPDF

---

## Page 1


Citation: Mushtaq, R.T.; Iqbal, A.;
Wang, Y.; Rehman, M.; Petra, M.I.
Investigation and Optimization of
Effects of 3D Printer Process
Parameters on Performance
Parameters. Materials 2023, 16, 3392.
https://doi.org/10.3390/
ma16093392
Academic Editors: Angelos P.
Markopoulos, Muthuramalingam
Thangaraj, Luca Sorrentino,
Panagiotis Karmiris-Obrata´nski
and Beata Leszczy´nska-Madej
Received: 24 March 2023
Revised: 19 April 2023
Accepted: 23 April 2023
Published: 26 April 2023
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
materials
Article
Investigation and Optimization of Effects of 3D Printer Process
Parameters on Performance Parameters
Ray Tahir Mushtaq 1,†
, Asif Iqbal 2,*
, Yanen Wang 1,*,†, Mudassar Rehman 1
and Mohd Iskandar Petra 2
1
Bio-Additive Manufacturing University-Enterprise Joint Research Center of Shaanxi Province,
Department of Industry Engineering, Northwestern Polytechnical University, Xi’an 710072, China;
tahirmushtaqray@mail.nwpu.edu.cn (R.T.M.); mudassar@mail.nwpu.edu.cn (M.R.)
2
Faculty of Integrated Technologies, Universiti Brunei Darussalam, Jalan Tungku Link,
Gadong BE 1410, Brunei; iskandar.petra@ubd.edu.bn
*
Correspondence: wangyanen@126.com (Y.W.); asif.asiﬁqbal@gmail.com (A.I.)
†
These authors contributed equally to this work.
Abstract: Professionals in industries are making progress in creating predictive techniques for evalu-
ating critical characteristics and reactions of engineered materials. The objective of this investigation
is to determine the optimal settings for a 3D printer made of acrylonitrile butadiene styrene (ABS)
in terms of its conﬂicting responses (ﬂexural strength (FS), tensile strength (TS), average surface
roughness (Ra), print time (T), and energy consumption (E)). Layer thickness (LT), printing speed
(PS), and inﬁll density (ID) are all quantiﬁable characteristics that were chosen. For the experimental
methods of the prediction models, twenty samples were created using a full central composite design
(CCD). The models were veriﬁed by proving that the experimental results were consistent with
the predictions using validation trial tests, and the signiﬁcance of the performance parameters was
conﬁrmed using analysis of variance (ANOVA). The most crucial element in obtaining the desired Ra
and T was LT, whereas ID was the most crucial in attaining the desired mechanical characteristics.
Numerical multi-objective optimization was used to achieve the following parameters: LT = 0.27 mm,
ID = 84 percent, and PS = 51.1 mm/s; FS = 58.01 MPa; TS = 35.8 MPa; lowest Ra = 8.01 m; lowest
T = 58 min; and E = 0.21 kwh. Manufacturers and practitioners may proﬁt from using the produced
numerically optimized model to forecast the necessary surface quality for different aspects before
undertaking trials.
Keywords: additive manufacturing; fused ﬁlament fabrication; parametric optimization; mechanical
properties; energy efﬁciency
1. Introduction
Additive manufacturing (AM), also known as 3D printing, signiﬁes constructing a
physical object by adding material layer upon layer based on a digital model [1,2]. This
is accomplished using desktop design (CAD) software. The AM methods are based on
the concepts of starting with a modeled contains simple, slicing the created ﬁles into two-
dimensional sectors, and transporting them to the Am platform. The implementation of
AM has progressed beyond the prototyping stage and is now a highly adaptable man-
ufacturing process. AM relies entirely on rapid prototyping to construct intricate and
substantial structures using 3D CAD software [3]. Sheet lamination, deposition, selective
laser [4–8], fused deposition modeling, and stereolithography are only some of the additive
manufacturing (AM) techniques that may be utilized to produce the material element layer
by layer [9–11]. Parts built by Laser-Powder Bed Fusion offered signiﬁcant advantages for
aerospace applications; the validation of their mechanical properties remains an important
research area to ensure their safety and effectiveness in critical applications [12].
In 1988, under the name fused deposition modeling (FDM), Crump [13] registered
the fused ﬁlament fabrication (FFF) process of 3D printing. This laid the groundwork for
Materials 2023, 16, 3392. https://doi.org/10.3390/ma16093392
https://www.mdpi.com/journal/materials


---


## Page 2


Materials 2023, 16, 3392
2 of 22
establishing the late-20th-century Stratasys business in 1989. FFF is unique in its ability
to create complex shapes. Electrical motors power the feeding of a ﬁlament into a molten
pool in this additive manufacturing technology. Stepper motors then drive the printer head
over a platform. Ink is deposited in the “X” and “Y” planes [14] after being liqueﬁed and
pushed through the printer nozzle. The printer platform is lowered into the “Z” track as
each successive cross-section is carefully put. As a result, the 3D-printed design is built up
in layers [15]. To complete the sample, just repeat the procedure [10]. The FFF printer’s
operational scheme is shown in Figure 1 [16].
Figure 1. Schematic of FFF-based 3D printer (ﬁgure reprinted from [16] under the license CC-BY 4.0).
When quick manufacturing of devices was needed as part of the emergency reac-
tion to COVID-19, three-dimensional printing (3DP) was employed as a transportable
factory [17]. Among the many ﬁelds that can beneﬁt from technology, we ﬁnd the medi-
cal/dental/aviation/refrigeration/automotive sectors [18,19]. Dental models using AM
techniques such as FFF and Poljet are precise and accurate [20,21]. Individualized prosthetic
devices, improved manufacturing processes, ﬁber-reinforced structures for automobiles
and airplanes, conductive structures and implants, biological and construction tools, phys-
iochemical health products, the ﬁne jewelry and gemstone industries, soot particle ﬁlters
and lightweight heating devices, and investment artifacts are all examples of uses for
FFF that have been studied by the authors [22–26]. FFF 3DP has several potential uses,
such as increasing the tensile strength of materials [27,28], making automobile parts [29],
making research prototypes [30–32], analyzing microstructures [33,34], and combating the
COVID-19 virus [35–37].
Thermoplastic polymer ﬁlaments made with the FFF feedstock method are the most
widely used printing materials. There are many challenges that the FFF method is always
up against. Because it has limitations in terms of mechanical strength, i.e., ﬂexural strength
(FS) and tensile strength (TS), print time (T), average surface roughness (Ra), and energy
consumption (E) [38]. To improve the FDM process, a lot of work has gone into developing
new FFF feedstock materials, honing the process parameters, and studying various parts’
mechanical, thermal, and rheological properties. Only thermoplastics may be used as
input materials when using the FFF’s heating and extruded ﬁlament through the extruded
nozzle. Polypropylene, polylactic acid, poly-phenyl-sulfone, nylon, polyethylene, and
polycarbonate are just some of the polymers composite that FDM can print [39]. This
research aims to determine what inﬂuences the Fabrication technique parameters the most
so that better mechanical characteristics, Ra, T, and E, may be achieved in 3D-printed objects.
Acrylonitrile butadiene styrene (ABS) has been used in the medical ﬁeld [40], in tissue
engineering [41], in the airline industry [42], and in the car industry [25]. The automotive
sector requires more robust 3D-printed products, molds, and ﬁxtures. However, problems
such as subpar mechanical qualities, subpar surface ﬁnish, and a lengthy production
time still need to be ﬁxed. It is envisaged that the ﬁndings of this investigation would
be applicable in ensuring that 3D-printed ABS components achieve the required tensile
strength in a reasonable amount of time. Additive manufacturing technologies must
reduce lead and production times to compete with traditional manufacturing processes.
Since improved surface and mechanical properties are required to manufacture functional


---


## Page 3


Materials 2023, 16, 3392
3 of 22
components, the construction time must also be decreased. Unchecked “failures”, such
as blocked nozzles, might signiﬁcantly lengthen the construction schedule. The process
parameters also affect the time spent building FFF parts; selecting the right set of values
might help. Thus, there is a lack of investigation into how energy usage affects energy
efﬁciency, carbon pollution, and the price of producing an item.
The relationships between print quality (PS), layer thickness (LT), and inﬁll density
(ID) have been studied [43,44]. LT is one of the most studied properties of FFF 3D-printed
items [45]. The overall mechanical characteristics of FFF parts in 100% ID have been
demonstrated to be improved by the LT mid-level [46]. Mechanical response measurements
and other 3D printing features are less visible. The LT is impacted by changes in heat
transfer between the freshly deposited material and older, previously placed material [30].
At the highest PS, surface quality deteriorates and mechanical characteristics decrease, but
with the interactions of high ID, PS acquires substantial stiffness [47]. The ﬁnal product’s
porosity is established by the ID [48]. The FS and TS of the components improves with
increasing ID [49]. It is projected that the 100% ID will have a higher mechanical response.
Existing research [48] indicates that PS, LT, and other control parameters affect the porosity
and dynamic response in 100% ID.
Although there are very important optimization techniques, such as numerical analysis
using ﬁnite elemental analysis for simulations [50], RSM multi-objective optimization
has become one of the most used optimization methods due to the need for physical
optimization and because it is a useful instrument for adjusting AM procedure settings.
The RSM method is used for optimization in several contexts, most notably in computer
numeric control, with various techniques, such as [51] “laser processing” [52], “electric
discharge machining” [53], etc. Grifﬁths et al. mentioned that a small experimental error
rate makes the RSM a great optimization tool. [54]. The RSM method may be better for
optimizing multi-response 3D printers, because it can be modeled with higher ﬁtting and
multi-objectivity [55]. The FFF processing settings were examined and adjusted by Selvam
ani et al. [56], who used RSM analysis. The highest mechanical property values observed
in experiments were 0.333 GPa for elastic modulus, 7.758 MPa for ultimate tensile strength,
and 4.539 MPa for yield strength.
Therefore, to ﬁll the gaps, this research examines the in-depth effect, ID, and PS (by
taking minimum to maximum levels) on the FS, TS, Ra, T, and E performance parameters of
the FFF-3DP ABS subcomponents. This investigation thoroughly explores several conﬂict-
ing performance parameters important for industrial applications, including mechanical
characteristics, power efﬁciency, and surface quality enhancement. According to its propo-
nents, ABS K5 ﬁlament is superior to its commodity counterpart in printability, ease of use,
and lack of shrinkage, wrapping, warpage, mechanical characteristics, and printability. To
complete the research, the authors will follow these procedures:
i.
Analyze the regression analysis and the magnitude of the parametric inﬂuence on
performance parameters using ANOVA;
ii.
Investigate how changing LT, ID, and PS values affect ABS’s FS, TS, Ra, T, and E;
iii.
We can achieve optimal performance by applying RSM’s multi-objective numerical
optimization technique to the FFF 3DP’s parameters;
iv.
Conduct trials and analyze the results using an SEM to verify the optimum sam-
ple preparation.
2. Materials and Methods
2.1. Materials
The investigations were conducted using an industrial, professional 3D printer called
“CR-5” manufactured by Creality, Shenzhen, China, whose properties are shown in Table 1,
and industrial ABS (ABSK5) polymer with 1.75 mm diameter ﬁlament procured from the
KEXCELLED ﬁrm, Suzhou, China. Table 2 contains ABS material speciﬁcations.


---


## Page 4


Materials 2023, 16, 3392
4 of 22
Table 1. Speciﬁcations of CR5-3D printer (credit: the3dstore.com, accessed on 10 April 2023).
Speciﬁcation
Details
Layer Thickness
0.05–0.4 mm
Nozzle Diameter
Standard 0.4 mm (can be changed to 0.3/0.2 mm)
Filaments
1.75 mm PLA, ABS, PA6, TPU, Copper, Wood, Carbon Fiber
Print Speed
Normal: 60 mm/s, high: 100 mm/s
Printing Method
TF card/Online/Ofﬂine
Software Supporting
PROE, Solidworks, UG, 3D Max, Rhino 3D design
File Format
STL/OBJ/G-Code
Layers Software
Cura/Repetier-Host
Printing Size
300 × 225 × 320 mm
Print Temperature
Up to 270 ◦C
Power supply
230V
Bed Temperature
Up to 120 ◦C
Table 2. Comparison of standard ABS (credit: Kexcelled).
Properties
Values
Unit
Density
1.04
g/cm3
Flexural modulus
2000–3000
MPa
TS
30–40
MPa
Impact strength
Good
Heat resistance
95–105 ◦C
◦C
2.2. Response Surface Methodology
The methodology and experimental design (DOE) are described in this section. The
studies were designed and conducted using a full RSM-central composite design (RSM-
CCD). Several printing process parameters substantially inﬂuence the diverse performance
parameters that are researched, mainly with respect to FFF 3D printing. After thoroughly
reviewing the relevant literature, LT, PS, and ID were determined to be the most important
quantitative input factors. Material, mechanical properties, the design process, and sample
geometries affect the selected range. Therefore, the printing parameters were determined
based on previous academic data and early tests [46,48].
The experimental parameters and factors were determined using the statistical soft-
ware, Design-Expert version 13, which is widely recognized for its advanced features in
experimental design and analysis. Quantitative parameter settings (LT, PS, and ID), for
a thorough analysis, comprise ﬁve parametric levels each. To avoid decimal values in
the maximum and lowest parameters, L20 DOE was designed with a full CCD and alpha
1.5. After sending the STL ﬁle to the slicer, establishing the parameters, and slicing the
model, it was produced on a 3D printer. After calculating the performance parameters, the
values were placed into a CCD table created by a design expert. Table 3 shows the detailed
parametric experimental design for the ABS polymer.
Figure 2 demonstrates the manufactured ABS sample models for ISO 527 and ISO178,
respectively. The authors printed three samples for each test, conducted FS and TS tests on
each of the three ISO 527 and ISO 178 samples, calculated the mean, and measured three
Ra values before calculating the mean.
The authors determined the minimum PS to be 47 mm/s and the maximum PS to be
75 mm/s. CCD measured a lower value of 40 mm/s and a higher parameter of 82 mm/s.
At a PS of less than 40 mm/s, obtaining three samples needed more than 10 h, which
was inefﬁcient. Due to insufﬁcient cooling time, a high PS results in poor layer adhesion.
When the PS is reduced to extremely low levels, part distortion occurs. Thus, the minimum
and maximum speeds would be 47 mm/s and 75 mm/s, respectively. The line thickness
was often measured between 0.14 mm and 0.3 mm, but CCD measured one parameter as
0.1 mm and another as 0.34 mm. As the nozzle was 0.4 mm, LT’s maximum 3D printing
range was limited to 0.34 mm, while ABS printing was impossible below 0.1 mm. Thus,


---


## Page 5


Materials 2023, 16, 3392
5 of 22
the authors chose 0.1 as the minimum ABS value. To thoroughly comprehend the ID, the
authors used a lower limit of 20 percent and an upper bound of 84 percent. In comparison,
CCD used a lower parameter of 4 percent and a higher parameter of 100 percent.
Table 3. Detailed parametric experimental design for the ABS polymer.
Exp #
LT
(mm)
ID
(%)
PS
(mm/s)
1
0.22
52
61
2
0.14
20
47
3
0.14
84
47
4
0.22
100
61
5
0.22
52
61
6
0.22
52
61
7
0.22
52
61
8
0.22
52
82
9
0.22
52
61
10
0.22
4
61
11
0.34
52
61
12
0.3
84
47
13
0.22
52
40
14
0.3
20
75
15
0.14
84
75
16
0.3
84
75
17
0.22
52
61
18
0.1
52
61
19
0.14
20
75
20
0.3
20
47
Figure 2. FFF fabricated experimental samples for the ABS polymer.
Measurement Procedure
The FS and TS tests were complemented by a GTM 2500 Equipment with a 5-KN
weight cell, as shown in Figure 3a,b. Following ISO 527: 1997, TS tests were accompanied
on plastics at a cross-head speed of 5 mm/min [57]. ISO 178:2006 (plastics: calculating
FS characteristics) was used to determine FS. The prescribed standards for TS specimen
dimensions in testing demand precise attention to detail, requiring an overall length of


---


## Page 6


Materials 2023, 16, 3392
6 of 22
115 mm, a gauge length of 25 mm, a width of 19 mm, a thickness of 4 mm, and a length
of the narrow section of 33 mm. Meanwhile, the standards for the TS test were a width
of 10 mm, a length of 80 mm, and a thickness of 4 mm. The specimen is held in situ by
two supports 64 mm apart and subjected to a central weight until it fractures. The 5-mm
radius spherical equipment is the loading head. The tests employed 25 ◦C and 2 mm/min
cross-head speed [58,59].
As illustrated in Figure 3b The Ra value of the FFF-fabricated component was eval-
uated using a ‘JITAI KEYI’ Ra tester (JD520 model). In Equation (1), the Ra value can be
deﬁned as the arithmetic average of all actual values of variations in the surface proﬁle
measured along the whole distance from the centerline. The ISO 16610-211 standard was
employed for analysis, with sample lengths (Ls) of 4.8 mm and cut-off wavelengths of
0.8 mm [60].
Ra = 1
La
Z La
0
|Z(x)|dx
(1)
where La is the sampling length and Z(x) organizes the proﬁle curve.
Figure 3. FFF experimentation. (a) TS and FS testing, (b) Ra testing.
3. Results and Discussion
3.1. ANOVA for Performance Parameters
A design expert analyzed the present investigation’s regression model and the ANOVA
approach (version 13). Following the computation of the regression analysis, the ﬁnal
regressions regarding the actual values for FS, TS, Ra, T, and E were created as follows:
FS = 29.512 + 342.237 × LT −0.045 × ID + 1.276 × PS + 0.550 × LT × ID −1.828 × LT × PS
+ 0.004 × ID × PS −521.833 × LT2 −0.001 × ID2 −0.009 × PS2
(2)
TS = 40.031 −23.622 × LT + 0.004 × ID −0.383 × PS −0.437 × LT × ID + 0.648 × LT × PS
+ 0.001 × ID × PS + 48.307 × LT2 + 0.002 × ID2 + 0.002 × PS2
(3)
Ra = −6.340 + 41.196 × LT −0.038 × ID + 0.205 × PS + 0.075 × LT × ID −0.126 × LT × PS
+ 0.000 × ID × PS −37.243 × LT2 −0.000 × ID2 −0.001 × PS2
(4)
T = 234.365 −817.515 × LT + 0.551 × ID −2.142 × PS −1.562 × LT × ID + 2.232 × LT × PS
−0.001 × ID × PS + 1177.510 × LT2 + 0.001 × ID2 + 0.009 × PS2
(5)
E = 0.863 −3.100 × LT + 0.003 × ID −0.008 × PS −0.006 × LT × ID + 0.010 × LT × PS
−0.000 × ID × PS + 4.295 × LT2 + 0.000 × ID2 + 0.00003 × PS2
(6)
ANOVA was used to approximate and assess the regression coefﬁcients to determine
which process characteristics signiﬁcantly inﬂuence the dynamic qualities. Tables 4–6
summarizes the ANOVA results for all performance parameters. Table 4 shows the mean
and standard deviation for the sum of performance parameters, and Table 5 shows the
standard deviation at each point. The F-statistics for FS = 46.09, TS = 25.45, Ra = 89.64,
T = 196.35, and E = 150.26, respectively, and the p-values in all performance parameters


---


## Page 7


Materials 2023, 16, 3392
7 of 22
were less than 0.05 for the second-order regression model as seen in Table 6. The p-values
for the lack-of-ﬁt were calculated for FS = 0.004, TS = 0.556, and Ra = 0.3174, respectively.
This shows that the lack-of-ﬁt is small compared to a residual error. A small lack-of-ﬁt
is a good sign because it indicates that the terms left out of the model are insigniﬁcant.
p-values for the lack-of-ﬁt for T and E were not available. This implies that the lack-of-ﬁt
is minimal or non-existent for TS, T, and E, but signiﬁcant for TS and Ra of residual error.
The determination coefﬁcient examines the goodness-of-ﬁt of the regression models. It
is preferable to have a larger prediction coefﬁcient (close to 1.0). For all parameters, the
created relationship had a signiﬁcant value of R2, the adjusted R2, and the anticipated R2,
indicating a good correlation between the experimental and calculated values. A number
greater than four is preferred. In this investigation, the appropriate precision for FS and TS
is greater than 4, indicating a sufﬁcient signal.
Table 4. Performance parameters, mean, standard deviation, and ANOVA models were used for
the investigation.
Performance
Parameter
Name
Units
Observations
Min
Max
Mean
Std. Dev.
Ratio
Model
1
FS
MPa
20
39.47
61.81
50.07
6.75
1.57
Quadratic
2
TS
MPa
20
26.14
40.02
32.12
3.85
1.53
Quadratic
3
Ra
µm
20
3.77
10.18
7.62
1.69
2.70
Quadratic
4
T
min
20
36
106
60.80
19.69
2.94
Quadratic
5
E
kwh
20
0.14
0.41
0.2340
0.0754
2.93
Quadratic
Table 5. The standard deviation for each performance parameter at each point.
FS
TS
Ra
T
E
0.197525
1.5
0.017725
2.7
0.0105
2.0625
1.4105
0.252
4.1
0.0155
2.3
1.8995
0.1885
5.3
0.0205
3.0905
2.001
0.3825
3.6
0.014
2.736
1.554
0.3845
2.7
0.0105
2.695
1.552
0.3985
2.7
0.0105
2.68
1.4285
0.3985
2.7
0.0105
2.382
1.5435
0.46
2.35
0.009
2.6985
1.554
0.3935
2.7
0.0105
2.005
1.3995
0.3985
2.2
0.0085
2.5345
1.6995
0.483
2.05
0.008
2.899
1.781
0.3895
2.75
0.0105
2.573
1.565
0.2925
3.6
0.014
1.9735
1.558
0.507
1.8
0.007
2.776
1.8675
0.315
4.1
0.0155
2.8505
1.9055
0.509
2.1
0.008
2.7155
1.584
0.3985
2.7
0.0105
2.0665
1.4095
0.2575
5.2
0.02
2.0655
1.307
0.373
3.05
0.0115
2.265
1.527
0.4355
2.4
0.009
Table 6. Analysis results of the regression models.
Performance Parameter
R2
Adj-R2
Pre-R2
Precision
F-Value
Lack-of-Fit
Model p-Value
FS
97.68
95.60
81.97
23.09
46.09
0.004
<0.0001
TS
95.82
92.05
82.45
19.59
25.45
0.556
<0.0001
Ra
98.78
97.67
90.86
34.22
89.64
0.01
<0.0001
T
99.43
98.93
95.82
71.63
196.35
<0.0001
E
99.27
98.61
94.64
44.33
150.26
<0.0001


---


## Page 8


Materials 2023, 16, 3392
8 of 22
Before reaching any stronger conclusions, performing a residual analysis to test the
assumptions behind the ANOVA results is critical. This is shown in Figure 4a–e as a
comparison between the expected and experimental values for the FS/TS, Ra, T, and E.
According to the experimental results, the predicted values are extremely close to the
actual ones. To put it another way, this shows that existing models can accurately predict
the answers.
(a) 
(b) 
(c) 
(d) 
 
(e) 
Figure 4. Predicted vs. actual performance parameters for (a) FS, (b) TS, (c) Ra, (d) T, and (e) E.


---


## Page 9


Materials 2023, 16, 3392
9 of 22
3.2. Printing Parametric Effects on Mechanical Properties
Thermoplastic polymers such as ABS are used in FFF-based 3D printing. The material
is heated to a moderate condition before extruding through the nozzle to create the desired
three-dimensional shape. The LT utilized in the printing may inﬂuence the interfacial
bonding or the strength of the link between neighboring layers in the 3D-printed item.
Due to the bigger LT’s ability to reduce non-uniform temperature gradients, deformations,
and thermal stresses, it may be possible to reduce the required heat cycles [61]. Figure 5
shows this weak interlayer link might cause delamination or part failure for 3D-printed
components exposed to severe loads or pressures—thinner inter-layer bonding results in
a lesser void volume fraction, eventually giving higher strength to the material. The 3D-
printed component’s strength and integrity may be increased, and its resistance to failure
under stress can increase. However, the microlayers are fragile, and the thinner layers
induce movement at the lowest LT. Thus, 0.25 mm of LT is where it is at for FS. Figure 5d
shows that even at the maximum level of LT, the LT was less of a factor in TS because the
LT provided less area to the sample, and there were fewer microstructure concerns.
(a) 
(b) 
(c) 
(d) 
(e) 
(f) 
Figure 5. The effect of printing parameters on ABS: (a) FS vs. LT, (b) ID vs. FS, (c) PS vs. FS, (d) LT vs.
TS, (e) ID vs. TS, and (f) PS vs. TS. Red represents center point. Black is the average data line and
green lines show the min and max of data.
The mechanical qualities of a 3D-printed item may be affected by the ID of the compo-
nent, which is the total quantity of material utilized to ﬁll the part’s interior. This means
that increasing the ID of a 3D-printed item for FS and TS made it stronger and stiffer, as seen
in Figure 5b,e. This is because an increase in ID implies an increased amount of material
present to balance stresses throughout the item.
A 3D-printed object’s mechanical qualities may change depending on how quickly it
was created. After a speciﬁc threshold, raising the printing speed yields a weaker and less
exact ﬁnal item, while reducing the PS yields a stronger and more speciﬁc object, as shown


---


## Page 10


Materials 2023, 16, 3392
10 of 22
in Figure 5c for TS. A 3D printer’s output quality suffers when the extruded polymer is
not given enough time to cool and harden before adding another layer. The ﬁnal product
may have less strength because of the weaker link between the layers. Furthermore, the
extruded polymer may lose accuracy due to the rapid printing pace.
When 3D printing at a low speed, the printer’s nozzle moves slowly, which means that
the material being deposited has more time to absorb heat from the nozzle. As a result, the
material becomes softer and more pliable, making it easier to bond with the layers below
it. This process is known as “bonding strength development at the interface”. However,
the nozzle’s slow movement can increase the material’s residual stresses, reducing the
material’s strength [49,50].
ln(σ) = −1
n ln(PS) + C
(7)
This equation is derived from the polymer healing theory equation, where C is
a constant.
Despite this risk, printing at a low speed can be beneﬁcial in certain situations, for
example, when the printed material is prone to cracking or has already developed small
cracks. In that case, printing at a low PS could help to “heal” these cracks by allowing
the material to bond more strongly at the interface. This healing process may not be
complete, but it could still improve the overall strength of the object, as shown in Figure 5f
for TS. Figure 5f showed the highest TS at the midpoint, and then further increment of PS
decreased the value of TS.
The optimum printing speed for a given 3D-printed ABS polymer object will depend
on its intended use and the desired mechanical properties. Objects that require high
strength and precision, such as mechanical parts or structural components, will beneﬁt
from a lower printing speed. Objects that do not require high strength and precision, such
as prototypes or decorative items, can be printed at a higher speed without sacriﬁcing
performance.
Figure 6 shows the SEM images taken for TS and FS samples. Figure 6a,b show the
SEM samples at the highest and the lowest values of FS, respectively. The highest level
of FS was obtained in experiment 4. Figure 6a shows little distortion in layers, bulges,
and micro crack due to some humidity in material [59,62]. It shows well-packed layers
with 100% ID, which give bigger strength to the sample, and some layers were so packed
that they were coming out of the samples, as shown in the micro-SEM image of Figure 6a.
Figure 6b shows the FS sample at the lowest FS at experiment number 14 with an FS value
of 39.47 (see Figure 6g), at the lowest value of ID as 20% and high level of thickness as
0.3 mm and PS at highest value as 75 mm/s. Figure 6c shows the maximum and minimum
FS values of the stress–strain curve.
Figure 6d shows the TS sample at the highest level of TS in experiment 4. It shows
well-packed layers with 100% ID, giving the sample bigger strength. TS showed the lowest
value at experiment number 19 with a TS value of 26.14 MPa at the lowest value of ID as
20% and of thickness as 0.14 mm and PS at the highest value of 75 mm/s. At the mid of
parametric value at exp number 5 (ID = 52%, PS = 61 mm/s and LT 0.22), as shown in
Figure 6e, TS was found to be around 31.02 (see Figure 6h). Figure 6f shows the maximum
and minimum TS values of the stress–strain curve. However, the PS remains less signiﬁcant.
Thus, the ID got dominated as an inﬂuencing factor on TS. The investigation coincides with
the research performed by [46], where the PS was less signiﬁcant than ID.
Figure 7a shows the FS with contour graphs, showing that the LT and ID combinedly
contributed to increasing the highest ID value and about 0.25 mm of the LT. However, the
TS value did not signiﬁcantly increase by changing the value of LT, as shown in Figure 7b.


---


## Page 11


Materials 2023, 16, 3392
11 of 22
 
 
(a) 
(b) 
(c) 
 
 
(d) 
(e) 
(f) 
 
 
(g) 
(h) 
Figure 6. SEM images of TS and FS samples: (a) FS-Exp 4 (ID = 100%, PS = 75 mm/s, LT = 0.22 mm),
(b) FS-Exp number 14 (ID = 20%, LT = 0.3 mm, PS = 75 mm/s), (c) Stress strain curve for Exp 4 and
14, (d) TS-Exp 4 (ID = 100%, PS = 61 mm/s, LT = 0.22 mm), (e) TS-Exp 5 (ID = 52% PS = 61 mm/s,
LT = 0.22), (f) Stress strain curve for Exp 4 and 5, and (g) FS results for ABS (h) TS results for ABS.
 
(a) 
(b) 
Figure 7. 2D contour plots show the effect of the printing parameters and interaction on FS and TS;
(a) effect of LT Vs. ID on FS, (b) effect of LT Vs. ID on TS.


---


## Page 12


Materials 2023, 16, 3392
12 of 22
3.3. Effect of Printing Parameters on Ra
When the LT and PS are both high, the surface of the printed item has a sharper
appearance (see Figure 8a,b), and the layers emerge more, which results in increased
Ra [63].
Figure 8. The effect of printing parameters on the Ra of the ABS polymer; (a) effect of LT on Ra,
(b) effect of ID on Ra; (c) effect of PS on Ra. Red represents center point. Black is the average data line
and green lines show the min and max of data.
As seen in Figure 8a, an increase in LT caused the high staircase effect, resulting in
Ra. In certain cases, the staircase effect may be minimized by adjusting the LT to a value
that works the best value was signiﬁcantly reduced by a decrease in LT. Its ID inﬂuenced
the Ra of a 3D-printed item less. A smoother surface is shown in Figure 8b, as its D rises
in the accompanying graph. This lower ID might result in rougher surface quality, as the
extruded material has more opportunity to spread and produce rough or uneven layers, as
seen in Figure 8b.
Ra increased dramatically along with the increasing PS factor (Figure 8b). A high
PS may create ringing artifacts and even shifting layers. The Ra value increased at lower
values of ID. However, as shown in Figure 9a in contour graphs, it did not considerably
inﬂuence the Ra, and the literature investigation results correspond with the literature
ﬁndings [36]. After experimentation, the author found that the minimum Ra value was
3.77 µm, and the highest value for ABS was 10.18 µm (see Figure 10c). The contour graphs
in Figure 9a,b show the lowest Ra value at the lowest LT, PS, and ID.
 
 
(a) 
(b) 
Figure 9. 2D contour plots show the parameters’ effect and their interaction parameters on Ra;
(a) effect of LT Vs. ID on Ra, (b) effect of LT Vs. PS on Ra.


---


## Page 13


Materials 2023, 16, 3392
13 of 22
 
 
(a) 
(b) 
 
(c) 
Figure 10. SEM analysis of Ra-ABS and experimental results; (a) SEM image of exp 16 (0.34 mm LT),
(b) SEM image of exp 2 (LT = 0.14 mm, PS = 47 mm/s, ID 20%), and (c) graphical representation of
each experimental performance parameter value of Ra.
Figure 10a,b show the SEM images of the high Ra at experiment number 16—Figure 10a
shows the results with a highly rough surface, while Figure 10b shows the lowest Ra of
3.77 µm.
3.4. Eco-Friendly 3D Printing
According to a report by Georgia State University’s School of Public Health and the
Chemical Insights Research Institute, ABS polymer used in FFF 3DP can release fumes that
emit a strong odor. These fumes can be harmful if inhaled. Decreasing print time and print
energy can help minimize these fumes. This is because failed prints waste print time and


---


## Page 14


Materials 2023, 16, 3392
14 of 22
material and limiting them will go a long way towards printing more efﬁciently. Addi-
tionally, heating plastic causes minor decomposition in the ﬁlament, producing particulate
matter that can harm health. Therefore, reducing print time and energy can help minimize
the amount of heated and decomposed plastic, thereby reducing the number of fumes and
particulate matter released during printing.
Adopting an eco-conscious polishing strategy presents a forward-thinking approach
to surface reﬁnement, emphasizing environmentally considerate methods and materials
(see Figure 11). By incorporating these green polishing techniques, manufacturers can
lessen their ecological footprint, curtail waste production, and champion resource preserva-
tion. This mindset embraces using biodegradable, non-hazardous, or aqueous polishing
compounds, in tandem with capitalizing on energy-conserving machinery and procedures.
Furthermore, this green polishing philosophy may encompass integrating practices that cur-
tail emissions, diminish energy demands, and conﬁne the discharge of harmful substances.
By wholeheartedly accepting eco-friendly polishing, industries can actively participate in
fostering a more sustainable future and endorse conscientious manufacturing protocols
while continuing to attain premium surface results on their merchandise.
Figure 11. Eco-friendly ABS printing beneﬁts.
Due to the staircase effect and the fact that the sample is completed in fewer cycles as
LT increases, the printing time is reduced dramatically. Figure 12a,d shows that less E is
consumed when controlling T.


---


## Page 15


Materials 2023, 16, 3392
15 of 22
(a) 
(b) 
(c) 
 
(d) 
(e) 
(f) 
Figure 12. Effect of printing parameters on (a–c) for T and (d–f) for E. Red represents center point.
Black is the average data line and green lines show the min and max of data.
How ID affects T in FFF printing is context-speciﬁc and subject to change based on
several variables, such as the nature and size of the printed item, the kind of material
being used, and the amount of precision and detail needed. If you increase the ID, the
time constant will be longer; if you decrease it, the time constant will be shorter. Since
FFF printing works by depositing layers of material on top of each other to build up the
object, a larger ID requires more layers to be deposited to ﬁll the object’s interior space. This
additional material deposition takes time, resulting in a longer print time [64], as shown in
Figure 12b,e.
In addition, the quality and durability of the ﬁnal product may be modiﬁed by raising
the ID. Stronger and longer-lasting items may be the outcome of higher ID. However, they
might come at the expense of increased material requirements and more weight. This is
especially relevant for mechanical components or working prototypes that will be put
under stress or pressure.
The T decreased as the machine’s speed rose because the printer head could ﬁnish
the cycle rapidly when working at high speed. The fact that the machine is only used
brieﬂy means that the E uses less energy, as shown in Figure 12c,f. The contour’s graphs
in Figure 13 clearly show that for ABS, the lowest value of T and E was obtained using
the highest value of LT, the lowest value of ID, and PS. The research agreed with previous
research [48].
Figure 14a,b shows the T and E for PLA, respectively. According to Figure 14a,
experiment number 3 took the most T, due to the high ID = 84%, lowest LT = 0.14 mm, and
lowest PS = 0.47. Due to the longer T, it also had higher E, which was around 0.41 kwh. The
PLA sample took the least time at exp number 14 of 36 min due to the lowest ID, highest
LT, and the highest level of the PS. Due to this reason, the E of experiment number 14 also
had the least E of 0.14 kwh.


---


## Page 16


Materials 2023, 16, 3392
16 of 22
(a) 
(b) 
 
(c) 
(d) 
Figure 13. 2D contour plots showing the effect of parameters and their interaction parameters on T
and E; (a) effect of LT Vs. ID on T, (b) effect of LT Vs. PS on T, (c) effect of LT Vs. ID on E, (d) effect of
LT Vs. PS on E.
 
(a) 
(b) 
Figure 14. Graphical representation of the mechanical performance parameters values for every
experiment: (a) for T-ABS and (b) for E-ABS.


---


## Page 17


Materials 2023, 16, 3392
17 of 22
4. Multi-Optimization Using Response Surface Methodology
Optimal mechanical properties (TS, FS), smallest Ra, and shortest T for ABS polymer
resulted from a multi-objective numerical optimization of process parameters. Numerical
optimization may address multiple goals, with the resultant minimum and maximum
values directly applicable to the parameter optimization. The red dots in Figure 15 represent
the optimal levels of parameters, and the blue dots show the performance parameters. This
optimization ramp was generated using the Design Expert software. The LT should be
around 0.27 mm to obtain the optimal balance with ABS.
Figure 15. Optimization conditions and ﬁnal performance parameters as the result of optimization:
(a–c) for the parameters and (d–h) for the responses.
Maximum mechanical qualities, including FS of 59.39 MPa and TS of 36.11, lowest
Ra of 7.78 m, lowest T of 57.4 min, and lowest E of 0.22 kwh, need ID and PS values of
84 percent and 51.1 mm/s, respectively. Figure 16 depicts contour graphs of the LT and
ID relationships by highlighting the points when the PS and the permanent variable are
at 51.1 mm/s values. Because the author set the LT to 0.27 (middle ground) and the ID to
its maximum value at the top, the data points fell roughly in the end corner to the upper
regions of the graph. It calculated a desirability of 0.65, which is quite good. We chose this
optimization because it allowed us to get a balanced optimized sample with improved
mechanical characteristics, a smoother surface, and a higher quality, even though we could
have obtained the lowest values for Ra, T, and E at other places. This ﬁnding lends credence
to the argument that the input parameters do have an impact on the outcomes. Finally,
the enhanced mechanical properties (Ra, T, and E) created by the numerical optimization
of the process parameters are tested for accuracy. This led to the development of three
ABS specimens, which were used to double-check the experiment and determine the
optimal parameters.


---


## Page 18


Materials 2023, 16, 3392
18 of 22
Figure 16. Numerical optimization plots show the region of optimal FFF parameters: (a) desir-
ability, (b) FS optimization, (c) TS optimization, (d) Ra optimization, (e) T optimization, and (f) E
optimization.
Conformation Test
Laboratory trials with optimal parameter settings are compared to the projected values
based on mathematical models, as indicated in the estimated proportion of errors given in
Equation (8):
Prediction error percentage =

Actual −predicted
actual
 ∗100
(8)
It can be understood from Table 7 that the variation percentage between the predicted
values and experimental values lies within 2.32%, 0.86%, 2.96%, 1.05%, and 4.55% for FS,
TS, Ra, T, and E, respectively. Thus, the prediction performance of the model is satisfactory.
This conﬁrms an excellent accomplishment of results using the RSM-CCD.
Table 7. Predicted process parameters, performance parameters, experimental performance parame-
ters, and error by RSM optimization.
Predicted Process Parameters
Predicted Performance
Parameters
Experimental Performance
Parameters
Error %
Name
Unit
Value
Name
Unit
Value
Name
Unit
Value
Value
LT
mm
0.27
FS
MPa
59.39
FS
MPa
58.01
2.32
ID
%
84
TS
MPa
36.11
TS
MPa
35.8
0.86
PS
mm/s
51.1
Ra
µm
7.78
Ra
µm
8.01
2.96
T
min
57.4
T
min
58
1.05
E
kwh
0.22
E
kwh
0.21
4.55


---


## Page 19


Materials 2023, 16, 3392
19 of 22
5. Conclusions and Prospects
The following conclusions were drawn from the results of the experimentation:
•
Inclusive multi-objective optimization of important performance parameters that
are vital for industry (tensile strength (TS), ﬂexural strength (FS), average surface
roughness (Ra), print time (T), and energy consumption (E)) have been studied.
•
Comprehensive investigations yielded contradictory optimized performance param-
eters, such as high FS and TS, low Ra value, and lowest T and E. The most crucial
element in obtaining the desired Ra and T was LT (due to the staircase effect), whereas
ID was the most crucial element in attaining the desired mechanical characteristics. PS
also affected mechanical properties due to the polymer healing effects.
•
Optimal printing settings combination for achieving FS, TS, Ra, T, and E for ABS
were found at layer thickness LT = 0.27 mm, ID = 84%, and PS = 51.1 mm/s using
the numerical multi-objective optimization. FS of 58.01 MPa, TS of 35.8 MPa, lowest
Ra of 8.01 µm, lowest T of 58 min, and E of 0.21 kwh were attained using numerical
multi-objective optimization. The variation percentage between the predicted and
experimental values lies within 2.32%, 0.86%, 2.96%, 1.05%, and 4.55% for FS, TS, Ra, T,
and E, respectively. Thus, the prediction implementation of the model is satisfactory.
•
Reducing the T and E demonstrates that the FFF approach is feasible regarding power
consumption, fuel efﬁciency, and controllable carbon emissions.
•
The ABS mathematical models projected performance parameters ﬁndings and experi-
mental results were all very close. When used for product quality testing, these data
can be used as a guide to determine the best printing settings, saving time on trial
and error.
Author Contributions: R.T.M.: Conceptualization, Methodology, Validation, Formal Analysis, Inves-
tigation, Writing—Original Draft Preparation; A.I.: Methodology, Investigation, Funding Acquisition;
Y.W.: Funding Acquisition, Project Administration, Supervision; M.R.: Data Curation, Visualiza-
tion; M.I.P.: Data Curation, Writing—Review and Editing. All authors have read and agreed to the
published version of the manuscript.
Funding: The research grant is funded by (1) the Shaanxi Province Key Research and Development
Projects (2021LLRH08 and 2022GXLH-02-15); (2) the Science and technology planning project of Xian
(20KYPT0002-1); (3) the Emerging Interdisciplinary Project of Northwestern Polytechnical University
(22GH0306); (4) the Fundamental Research Funds for the Central Universities (3102022gxb002) and
(5) University Research Grant (Grant number: UBD/RSCH/URC/RG(b)/2022/027) by Universiti
Brunei Darussalam, Brunei.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Mushtaq, R.T.; Iqbal, A.; Wang, Y.; Cheok, Q.; Abbas, S. Parametric Effects of Fused Filament Fabrication Approach on Surface
Roughness of Acrylonitrile Butadiene Styrene and Nylon-6 Polymer. Materials 2022, 15, 5206. [CrossRef] [PubMed]
2.
Wang, Y.; Mushtaq, R.T.; Ahmed, A.; Ahmed, A.; Rehman, M.; Rehman, M.; Khan, A.M.; Sharma, S.; Ishfaq, D.K.; Ali, H.; et al.
Additive Manufacturing Is Sustainable Technology: Citespace Based Bibliometric Investigations of Fused Deposition Modeling
Approach. Rapid Prototyp. J. 2022, 28, 654–675. [CrossRef]
3.
Shanmugam, R.; Ramoni, M.O.; Chandran, J.; Mohanavel, V.; Pugazhendhi, L. A Review on the Signiﬁcant Classiﬁcation of
Additive Manufacturing. J. Phys. Conf. Ser. 2021, 2027, 12026. [CrossRef]
4.
Rehman, M.; Yanen, W.; Mushtaq, R.T.; Ishfaq, K.; Zahoor, S.; Ahmed, A.; Kumar, M.S.; Gueyee, T.; Rahman, M.M.; Sultana, J.
Additive Manufacturing for Biomedical Applications: A Review on Classiﬁcation, Energy Consumption, and Its Appreciable
Role since COVID-19 Pandemic. Prog. Addit. Manuf. 2022, 1–35. [CrossRef]
5.
Ur Rehman, A.; Pitir, F.; Salamci, M.U. Full-Field Mapping and Flow Quantiﬁcation of Melt Pool Dynamics in Laser Powder Bed
Fusion of SS316L. Materials 2021, 14, 6264. [CrossRef] [PubMed]


---


## Page 20


Materials 2023, 16, 3392
20 of 22
6.
Ur Rehman, A.; Mahmood, M.A.; Pitir, F.; Salamci, M.U.; Popescu, A.C.; Mihailescu, I.N. Keyhole Formation by Laser Drilling
in Laser Powder Bed Fusion of Ti6Al4V Biomedical Alloy: Mesoscopic Computational Fluid Dynamics Simulation versus
Mathematical Modelling Using Empirical Validation. Nanomaterials 2021, 11, 3284. [CrossRef]
7.
Ali, Z.; Yan, Y.; Mei, H.; Cheng, L.; Zhang, L. Effect of inﬁll density, build direction and heat treatment on the tensile mechanical
properties of 3D-printed carbon-ﬁber nylon composites. Compos. Struct. 2023, 304, 116370. [CrossRef]
8.
Ur Rehman, A.; Mahmood, M.A.; Ansari, P.; Pitir, F.; Salamci, M.U.; Popescu, A.C.; Mihailescu, I.N. Spatter Formation and
Splashing Induced Defects in Laser-Based Powder Bed Fusion of AlSi10Mg Alloy: A Novel Hydrodynamics Modelling with
Empirical Testing. Metals 2021, 11, 2023. [CrossRef]
9.
Mohamed, O.A.; Masood, S.H.; Bhowmik, J.L. Optimization of Fused Deposition Modeling Process Parameters: A Review of
Current Research and Future Prospects. Adv. Manuf. 2015, 3, 42–53. [CrossRef]
10.
Li, H.; Wang, T.; Sun, J.; Yu, Z. The Effect of Process Parameters in Fused Deposition Modelling on Bonding Degree and Mechanical
Properties. Rapid Prototyp. J. 2018, 24, 80–92. [CrossRef]
11.
Singh, G.; Sharma, S.; Mittal, M.; Singh, G.; Singh, J.; Changhe, L.; Khan, A.M.; Dwivedi, S.P.; Mushtaq, R.T.; Singh, S. Impact of
Post-Heat-Treatment on the Surface-Roughness, Residual Stresses, and Micromorphology Characteristics of Plasma-Sprayed Pure
Hydroxyapatite and 7%-Aloxite Reinforced Hydroxyapatite Coatings Deposited on Titanium Alloy-Based Biomedical Implants. J.
Mater. Res. Technol. 2022, 18, 1358–1380. [CrossRef]
12.
Kumar, M.S.; Javidrad, H.R.; Shanmugam, R.; Ramoni, M.; Adediran, A.A.; Pruncu, C.I. Impact of Print Orientation on
Morphological and Mechanical Properties of L-PBF Based AlSi7Mg Parts for Aerospace Applications. Silicon 2022, 14, 7083–7097.
[CrossRef]
13.
Crump, S.S. Fused Deposition Modeling (FDM): Putting Rapid Back into Prototyping. In Proceedings of the 2nd International
Conference on Rapid Prototyping, Dayton, OH, USA, 23–26 June 1991; pp. 354–357.
14.
Turner, B.N.; Strong, R.; Gold, S.S. A Review of Melt Extrusion Additive Manufacturing Processes: I. Process Design and Modeling.
Rapid Prototyp. J. 2014, 20, 192–204. [CrossRef]
15.
Spreeman, M.E.; Stretz, H.A.; Dadmun, M.D. Role of Compatibilizer in 3D Printing of Polymer Blends. Addit. Manuf. 2019,
27, 267–277. [CrossRef]
16.
Wang, Y.; Müller, W.-D.; Rumjahn, A.; Schwitalla, A. Parameters Inﬂuencing the Outcome of Additive Manufacturing of Tiny
Medical Devices Based on PEEK. Materials 2020, 13, 466. [CrossRef]
17.
Choong, Y.Y.C.; Tan, H.W.; Patel, D.C.; Choong, W.T.N.; Chen, C.-H.; Low, H.Y.; Tan, M.J.; Patel, C.D.; Chua, C.K. The Global Rise
of 3D Printing during the COVID-19 Pandemic. Nat. Rev. Mater. 2020, 5, 637–639. [CrossRef]
18.
Khan, S.B.; Irfan, S.; Lam, S.S.; Sun, X.; Chen, S. 3D printed nanoﬁltration membrane technology for waste water distillation.
J. Water Process Eng. 2022, 49, 102958. [CrossRef]
19.
Pramanik, D.; Mandal, A.; Kuar, A.S. An Experimental Investigation on Improvement of Surface Roughness of ABS on Fused
Deposition Modelling Process. Mater. Today Proc. 2019, 26, 860–863. [CrossRef]
20.
Jin, S.J.; Jeong, I.D.; Kim, J.H.; Kim, W.C. Accuracy (Trueness and Precision) of Dental Models Fabricated Using Additive
Manufacturing Methods. Int. J. Comput. Dent. 2018, 21, 107–113.
21.
Monzon, M.D.; Diaz, N.; Benitez, A.N.; Marrero, M.D.; Hernandez, P.M. Advantages of Fused Deposition Modeling for Making
Electrically Conductive Plastic Patterns. In Proceedings of the 2010 International Conference on Manufacturing Automation,
Hong Kong, China, 13–15 December 2010.
22.
Soriano-Heras, E.; Blaya-Haro, F.; Molino, C.; de Agustín del Burgo, J.M. Rapid Prototyping Prosthetic Hand Acting by a
Low-Cost Shape-Memory-Alloy Actuator. J. Artif. Organs 2018, 21, 238–246. [CrossRef]
23.
Rahim, T.N.A.T.; Abdullah, A.M.; Md Akil, H. Recent Developments in Fused Deposition Modeling-Based 3D Printing of
Polymers and Their Composites. Polym. Rev. 2019, 59, 589–624. [CrossRef]
24.
Shakor, P.; Nejadi, S.; Paul, G.; Sanjayan, J. A Novel Methodology of Powder-Based Cementitious Materials in 3D Inkjet Printing
for Construction Applications. In Proceedings of the 6th International Conference on Durability of Concrete Structures, ICDCS
2018, Leeds, UK, 18–20 July 2018.
25.
Fischer, A.C.; Mäntysalo, M.; Niklaus, F. Inkjet Printing, Laser-Based Micromachining, and Micro–3D Printing Technologies for
MEMS. In Handbook of Silicon Based MEMS Materials and Technologies; Elsevier: Amsterdam, The Netherlands, 2020; pp. 531–545.
26.
Ntousia, M.; Fudos, I. 3D Printing Technologies & Applications: An Overview. In Proceedings of the CAD 2020 Conference,
Singapore, 24–26 June 2019.
27.
Samykano, M.; Selvamani, S.K.; Kadirgama, K.; Ngui, W.K.; Kanagaraj, G.; Sudhakar, K. Mechanical Property of FDM Printed
ABS: Inﬂuence of Printing Parameters. Int. J. Adv. Manuf. Technol. 2019, 102, 2779–2796. [CrossRef]
28.
Lopez, D.M.B.; Ahmad, R. Tensile Mechanical Behaviour of Multi-Polymer Sandwich Structures via Fused Deposition Modelling.
Polymers 2020, 12, 13. [CrossRef]
29.
Mohamed, O.A.; Masood, S.H.; Bhowmik, J.L. Investigation on the Flexural Creep Stiffness Behavior of PC-ABS Material
Processed by Fused Deposition Modeling Using Response Surface Deﬁnitive Screening Design. JOM 2017, 69, 498–505. [CrossRef]
30.
Gautam, R.; Idapalapati, S.; Feih, S. Printing and Characterisation of Kagome Lattice Structures by Fused Deposition Modelling.
Mater. Des. 2018, 137, 266–275. [CrossRef]
31.
Ravi, A.K.; Deshpande, A.; Hsu, K.H. An In-Process Laser Localized Pre-Deposition Heating Approach to Inter-Layer Bond
Strengthening in Extrusion Based Polymer Additive Manufacturing. J. Manuf. Process. 2016, 24, 179–185. [CrossRef]


---


## Page 21


Materials 2023, 16, 3392
21 of 22
32.
Ancans, A.; Rozentals, A.; Nesenbergs, K.; Greitans, M. Inertial Sensors and Muscle Electrical Signals in Human-Computer
Interaction. In Proceedings of the 2017 6th International Conference on Information and Communication Technology and
Accessibility (ICTA), Muscat, Oman, 19–21 December 2017; pp. 1–6.
33.
Bruncko, M.; Anzel, I. Microstructure and Magnetic Properties of Polymer Bonded Magnets Produced by Additive Manufacturing
Technologies. Prakt. Metallogr.-Pract. Metallogr. 2019, 56, 512–522. [CrossRef]
34.
Guessasma, S.; Belhabib, S.; Nouri, H. Microstructure, Thermal and Mechanical Behavior of 3D Printed Acrylonitrile Styrene
Acrylate. Macromol. Mater. Eng. 2019, 304, 11. [CrossRef]
35.
Mwema, F.M.; Akinlabi, E.T. Basics of Fused Deposition Modelling (FDM). In Fused Deposition Modeling. SpringerBriefs in Applied
Sciences and Technology; Springer: Cham, Switzerland, 2020; pp. 1–15. [CrossRef]
36.
Li, L.; Liu, W.; Wang, Y.; Zhao, Z. Mechanical performance and damage monitoring of CFRP thermoplastic laminates with an
open hole repaired by 3D printed patches. Compos. Struct. 2023, 303, 116308. [CrossRef]
37.
Larrañeta, E.; Dominguez-Robles, J.; Lamprou, D.A. Additive Manufacturing Can Assist in the Fight against COVID-19 and
Other Pandemics and Impact on the Global Supply Chain. 3D Print Addit. Manuf. 2020, 7, 100–103. [CrossRef]
38.
Singh, J. Inﬂuence of Process Parameters on Mechanical Strength, Build Time, and Material Consumption of 3D Printed Polylactic
Acid Parts. Polym. Compos. 2022, 43, 5908–5928. [CrossRef]
39.
Enemuoh, E.U.; Duginski, S.; Feyen, C.; Menta, V.G. Effect of Process Parameters on Energy Consumption, Physical, and
Mechanical Properties of Fused Deposition Modeling. Polymers 2021, 13, 2506. [CrossRef]
40.
Das, S.; Hollister, S.F.; Flanagan, C.; Adewunmi, A.; Bark, K.; Chen, C.; Ramaswamy, K.; Rose, D.; Widjaja, E. Freeform Fabrication
of Nylon-6 Tissue Engineering Scaffolds. Rapid Prototyp. J. 2003, 9, 43–49. [CrossRef]
41.
Jaiganesh, V.; Manivannan, S.; Manivannan, S. Numerical Analysis and Simulation of Nylon Composite Propeller for Aircraft. In
Proceedings of the 12th Global Congress on Manufacturing and Management (GCMM—2014), Vellore, India, 8–10 December
2014; Xavior, M.A., Yarlagadda, P., Eds.; Elsevier Science BV: Amsterdam, The Netherlands, 2014; Volume 97, pp. 1079–1088.
42.
Kumar, R.; Singh, R.; Ahuja, I.P.S. Repair of Automotive Bumpers and Bars with Modiﬁed Friction Stir Welding. J. Cent. South
Univ. 2020, 27, 2239–2248. [CrossRef]
43.
Kechagias, J.D.; Vidakis, N.; Petousis, M.; Mountakis, N. A Multi-Parametric Process Evaluation of the Mechanical Response of
PLA in FFF 3D Printing. Mater. Manuf. Process. 2022, 38, 941–953. [CrossRef]
44.
Vidakis, N.; Petousis, M.; Kechagias, J.D. Parameter Effects and Process Modelling of Polyamide 12 3D-Printed Parts Strength
and Toughness. Mater. Manuf. Process. 2022, 37, 1358–1369. [CrossRef]
45.
Saharudin, M.S.; Hajnys, J.; Kozior, T.; Gogolewski, D.; Zmarzły, P. Quality of Surface Texture and Mechanical Properties of Pla
and Pa-Based Material Reinforced with Carbon Fibers Manufactured by Fdm and Cff 3d Printing Technologies. Polymers 2021,
13, 1671. [CrossRef]
46.
Vyavahare, S.; Kumar, S.; Panghal, D. Experimental Study of Surface Roughness, Dimensional Accuracy and Time of Fabrication
of Parts Produced by Fused Deposition Modelling. Rapid Prototyp. J. 2020, 26, 1535–1554. [CrossRef]
47.
Harris, M.; Potgieter, J.; Archer, R.; Arif, K.M. In-Process Thermal Treatment of Polylactic Acid in Fused Deposition Modelling.
Mater. Manuf. Process. 2019, 34, 701–713. [CrossRef]
48.
Dey, A.; Yodo, N. A Systematic Survey of FDM Process Parameter Optimization and Their Inﬂuence on Part Characteristics.
J. Manuf. Mater. Process. 2019, 3, 64. [CrossRef]
49.
Chadha, C.; Crowe, K.A.; Carmen, C.L.; Patterson, A.E. Exploring an AM-Enabled Combination-of-Functions Approach for
Modular Product Design. Designs 2018, 2, 37. [CrossRef]
50.
Chadha, C.; Patterson, A.E.; Jasiuk, I. SFF 2021 Paper- Non-Review Submission Predict Adhesive Strength of Repair of Thermo-
plastic Component Based on Polymer Healing Theory. Rapid Prototyp. J. 2021, 23, 560–574.
51.
Li, C.; Xiao, Q.; Tang, Y.; Li, L. A Method Integrating Taguchi, RSM and MOPSO to CNC Machining Parameters Optimization for
Energy Saving. J. Clean. Prod. 2016, 135, 263–275. [CrossRef]
52.
Mushtaq, R.T.; Wang, Y.; Rehman, M.; Khan, A.M.; Mia, M. State-Of-The-Art and Trends in CO2 Laser Cutting of Polymeric
Materials—A Review. Materials 2020, 13, 3839. [CrossRef] [PubMed]
53.
Kundra, T.K. Multi-Objective Optimisation of Fused Deposition Modelling PROCESS parameters Using RSM and Fuzzy Logic
for Build Time and Support Material. Int. J. Rapid Manuf. 2018, 7, 25–42. [CrossRef]
54.
Grifﬁths, C.A.; Howarth, J.; De Almeida-Rowbotham, G.; Rees, A. A Design of Experiments Approach to Optimise Tensile and
Notched Bending Properties of Fused Deposition Modelling Parts. Proc. Inst. Mech. Eng. B J. Eng. Manuf. 2016, 230, 1502–1512.
[CrossRef]
55.
Saad, M.S.; Nor, A.M.; Baharudin, M.E.; Zakaria, M.Z.; Aiman, A.F. Optimization of Surface Roughness in FDM 3D Printer Using
Response Surface Methodology, Particle Swarm Optimization, and Symbiotic Organism Search Algorithms. Int. J. Adv. Manuf.
Technol. 2019, 105, 5121–5137. [CrossRef]
56.
Selvamani, S.K.; Rajan, K.; Samykano, M.; Kumar, R.R.; Kadirgama, K.; Mohan, R.V. Investigation of Tensile Properties of
PLA–Brass Composite Using FDM. Prog. Addit. Manuf. 2022, 7, 839–851. [CrossRef]
57.
ISO 527-1; BSI Standards Publication Determination of Tensile Properties—ISO527 Part1. ISO: Geneva, Switzerland, 2012.
58.
ASTM D790-10; Standard Test Methods for Flexural Properties of Unreinforced and Reinforced Plastics and Electrical Insulating
Materials; Annual Book of ASTM Standards. ASTM International: West Conshohocken, PA, USA, 2002; pp. 1–12. [CrossRef]


---


## Page 22


Materials 2023, 16, 3392
22 of 22
59.
Hamid, R.A.; Hamezah, F.H.; Abd Razak, J. Inﬂuence of Humidity on the Tensile Strength of 3D Printed PLA Filament. In
Intelligent Manufacturing and Mechatronics. SympoSIMM 2021; Lecture Notes in Mechanical Engineering; Ali Mokhtar, M.N.,
Jamaludin, Z., Abdul Aziz, M.S., Maslan, M.N., Razak, J.A., Eds.; Springer Nature: Singapore, 2022; pp. 497–502.
60.
Teir, L.; Lindstedt, T.; Widmaier, T.; Hemming, B.; Brand, U.; Fahrbach, M.; Peiner, E.; Lassila, A. In-Line Measurement of the
Surface Texture of Rolls Using Long Slender Piezoresistive Microprobes. Sensors 2021, 21, 5955. [CrossRef]
61.
Luzanin, O.; Guduric, V.; Ristic, I.; Muhic, S. Investigating Impact of Five Build Parameters on the Maximum Flexural Force in
FDM Specimens—A Deﬁnitive Screening Design Approach. Rapid Prototyp. J. 2017, 23, 1088–1098. [CrossRef]
62.
De Kergariou, C.; Saidani-Scott, H.; Perriman, A.; Scarpa, F.; Le Duigou, A. The Inﬂuence of the Humidity on the Mechanical
Properties of 3D Printed Continuous Flax Fibre Reinforced Poly(Lactic Acid) Composites. Compos. Part A Appl. Sci. Manuf. 2022,
155, 106805. [CrossRef]
63.
Shirmohammadi, M.; Goushchi, S.J.; Keshtiban, P.M. Optimization of 3D Printing Process Parameters to Minimize Surface
Roughness with Hybrid Artiﬁcial Neural Network Model and Particle Swarm Algorithm. Prog. Addit. Manuf. 2021, 6, 199–215.
[CrossRef]
64.
Kechagias, J.; Chaidas, D.; Vidakis, N.; Salonitis, K.; Vaxevanidis, N.M. Key Parameters Controlling Surface Quality and
Dimensional Accuracy: A Critical Review of FFF Process. Mater. Manuf. Process. 2022, 37, 963–984. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.


---
