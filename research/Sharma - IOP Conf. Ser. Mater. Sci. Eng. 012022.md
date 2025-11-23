# Sharma - IOP Conf. Ser. Mater. Sci. Eng. 012022

> **Source:** `Sharma - IOP Conf. Ser. Mater. Sci. Eng. 012022.pdf`
> **Converted:** 2025-11-22 21:18:08
> **Method:** PyMuPDF

---

## Page 1


IOP Conference Series:
Materials Science and
Engineering

PAPER • OPEN ACCESS
Optimization of FDM 3D printing process
parameters using Taguchi technique
To cite this article: Kuldeep Sharma et al 2021 IOP Conf. Ser.: Mater. Sci. Eng. 1168 012022

View the article online for updates and enhancements.
You may also like
Dimensional accuracy of acrylonitrile
butadiene styrene and polylactic acid
samples printed in vacuum-assisted
material extrusion system
Mohd Afiq Shahrum, Thavinesh Kumar
Rajendran, Shajahan Maidin et al.
-
Enhancing the functionality of sugar palm
(Arenga Pinnata) fibre reinforced polylactic
acid composite filament of fused
deposition modelling through Taguchi
method
Hazliza Aida C H, M T Mastura, S I Abdul
Kudus et al.
-
Widely accessible 3D printing technologies
in chemistry, biochemistry and
pharmaceutics: applications, materials and
prospects
Evgeniy G. Gordeev and Valentine P.
Ananikov
-
This content was downloaded from IP address 47.13.127.1 on 03/11/2025 at 16:54


---


## Page 2


Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence. Any further distribution
of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.
Published under licence by IOP Publishing Ltd
CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
1
Optimization of FDM 3D printing process parameters using
Taguchi technique
Kuldeep Sharma, Kapil Kumar, Rishi Kumar Singh and M S Rawat
 Greater Noida Institute of Technology, Greater Noida, UP, India
Abstract. Fused deposition modelling (FDM) is a fast growing and low-cost 3D printing technology in order to
comply most prominent demands of today’s industries in terms of capability to fabricate complex parts along with
high flexibility in design. The dimensional accuracy, is an urgent need of final parts printed by FDM process, that
is primarily influenced by the process parameters. Optimizing the process parameters which significantly influence
the dimensional accuracy is the primary goal of this study in order to achieve the ultimate final part quality. This
experimental study investigates the effect of different process parameters viz. layer height, raster angle, nozzle
temperature and surrounding pressure on thickness of the final part for Poly Lactic Acid (PLA) filament.
Experiments, based on Taguchi’s L9 orthogonal array, were performed and subsequently experimental data have
been analysed by ANOVA. It has been observed that the layer height is the most significant factor in order to
achieve the dimensional accuracy.
Key words- FDM, Taguchi Method, ANOVA
1. Introduction
3D (3 Dimensional) printing or Additive manufacturing (AM) has gained great popularity over the past
few years due to its ability to produce complex objects with ease, available sizes, flexibility of usable
materials, easy handling and wide range of applications such as engineering industry, medical sciences,
food industry, construction, aeronautics, textile industry, automotive industry and so on [1]. There are
various methods of Additive Manufacturing such as stereolithography, syringe extrusion, selective layer
sintering, fused deposition modelling(FDM)/fused filament fabrication(FFF) being used over the field
of its applications as per the requirements of industry but Fused  Deposition Modelling (FDM) has
become the most widely employed rapid prototyping technique among other methods  [2]. FDM uses a
temperature controlled head to extrude semi liquid thermoplastic through a nozzle of fixed orifice in
layer by layer formation, shown in figure 1[3], the movement of printing head is controlled by a
computer aided manufacturing (CAM) software[4].

Figure 1 FDM Process Schematic
Researchers are continuously working towards improving different characteristics of FDM produced
parts by tweaking with different process parameters and stating a range of optimum settings for a FDM
machine and material at which the strength or production time or production cost or any other aspect is


---


## Page 3


CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
2
optimized. Commonly optimized process parameters are layer height, line width, nozzle temperature,
bed temperature, print speed, raster angle etc [5–8]. Most researchers follow conventional technique for
experimentation i.e., varying only one parameter while keeping others constant at one time. This
conventional approach of experimentation is very time consuming and demands enormous number of
resources as number of experiments grows exponentially as more optimizable parameters are to be taken
into consideration. Moreover, interaction terms of various process parameters are not entertained in this
study. Taguchi method is a powerful tool to screen significant process parameters from many while
performing a significantly lesser number of experiments[5]. Taguchi’s L9 OA is adopted here to study
the effect of each processing parameter on dimensional accuracy of parts produced by FDM, and then
to determine optimum process parameters.
2. Literature Review
Parametric optimization of any manufacturing process is a prime necessity of the researchers for
producing quality final product in terms of dimensional accuracy and mechanical properties. This
section provides an extensive review of many researchers regarding optimization of process parameters
of FDM process.  Srivastava et al.[6]  proposed a hybrid approach to optimize model material volume
and build time in fused deposition modelling. RSM based experimentation was conducted on FDM
Maxum modeler for ABS workpiece and a conical primitive of STL size X=20mm, Y=20mm and
Z=69.99mm was taken. Established optimal condition by grey analysis approach are as follows: an air
gap of 0.0254mm, contour width of 0.654mm, orientation of 0.0˚ and raster angle of 0˚. Prashantha and
Roger [2] used fused deposition modelling based three dimensional (3D) printing system for the
fabrication of conductive polymer nanocomposites. Printing was done at 210℃ with a nozzle of
diameter 0.4 mm. Bed temperature at the time of printing was 60℃ and distance between bed surface
and nozzle was fixed at 0.2mm. Specimens printed with two surface layer shells, layer height is fixed at
0.2mm and infill is set to100% linear infill pattern with a stacking alternating between 45˚ and -45˚.
Panda et al.[7] used a recently developed technique such as bacteria foraging was adopted as its superior
performance over other random search techniques as there are only few parameters needed to be
adjusted. The control factors considered in this study are thickness, build orientation, raster angle, raster
width and air gap. Functional relationship between strength and process parameters is developed in this
work using surface methodology for prediction process. Hmeidat et al.[8] used an epoxy resin, Epon
826 in their study, a Bisphenol A diglycidyl ether (DGEBPA) resin with 178-186 weight per epoxide
with a density of 1.162 g/cc. These 3D printed nanocomposites had a strength in range of 80 to 143
MPa, which is significantly higher than any previously reported values for 3D printed thermoset
composites, including short fiber-reinforced materials. These materials have excellent layer-to-layer
bonding because of the crosslinking process which occurs after the component has been printed. Papon
and Haque[9] produced CNF/PLA nanocomposite filaments using a laboratory mixing extruder. The
matrix material used was polylactic acid-biopolymer (PLA) granulates of 3mm size with a glass
transition temperature of 55℃ and melting temperature of 175℃. The reinforcing material they used
was CNF with a maximum length of 400nm and average diameter of 50nm. It was observed that
geometry of nozzle affects the bead spreading architecture. Improved ultimate strength and modulus of
elasticity was seen in CNF/PLA nanocomposites with 0.5% CNF as compared to neat PLA. Bead
orientation direction and orientation of CNF was seen to be affected by extruder orifice and printer
nozzle. Cataldi et al.[10] used a single screw extruder for producing nanocomposites consisting of
polyvinyl alcohol and cellulose nanocrystals. Thermoplastic polyvinyl alcohol was used as Matrix for
the composite in this work. Stiffness of filament and 3D printed specimens was increased after the
introduction of CNC. The toughness of 3D printed material was increased due to good edition between
CNC and PVOH. Lower densification was achieved upon introduction of CNC. Alafaghani et al.[7]
examined the effect of infill percentage, building direction, infill pattern, printer speed, extrusion
temperature and layer height independently on mechanical properties and dimensional accuracy.
Extrusion temperature, layer height and building direction affected dimensional accuracy more than
infill pattern, infill percentage and printing speed. B. Coppola et al.[8] studied the effects of printing


---


## Page 4


CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
3
temperature on PLA/clay nanocomposites in 3D printing. Semi-crystalline polylactic acid (PLA) was
used as matrix in this study. They used FDM technique Tu 3D print dog bone specimens at three different
temperatures: 185, 200 and 215°C to mechanically test in tensile mode. A higher elastic modulus was
exhibited by nanocomposite 3D printed samples as compared with PLA specimens and it increases with
increase in printing temperature. They concluded that printing temperature strongly affects properties
of final object. Ceretti et al.[9] produced multi-layered PCL scaffolds and analysed the influence of
process parameters and extrusion technology on the deposited material. The three configurations used
were: 0.6mm x 0.6mm, 0.8mm x 0.8mm and 1mm x 1mm and path heights were 0.3mm, 0.4mm and
0.5mm for each configuration respectively, while the area of the whole grid was 10mm x 10mm. Human
foreskin fibroblasts cells were seeded at a cellular density of 40000 cells/cm to verify the effectiveness
of produced scaffolds. They concluded that extrusion head don't have significant effects on resulting
geometry of the samples and for the extrusion of poly-caprolactone, grain extrusion head is
preferable. Bartolomeo Coppola et al.[10] used a layered silicate-reinforced polylactic acid (PLA) for
manufacturing samples with additive manufacturing. During the melt-compounding process, the
temperature profile used was: 160°C-180°C-180°C-180°C-180°C-180°C-180°C-170°C (from hopper to
die). The single screw extruder had a die of 3mm, operating temperature profile: 180°C-180°C-160°C
(from hopper to die) and had a screw speed of 10rpm. At the time of printing of specimens, bed
temperature was fixed at 50°C, layer height was fixed at 0.2mm, faster angle was fixed at +/- 45° and
nozzle diameter were fixed at 0.35mm. Printing temperature had a direct effect on specimen
transparency, the transparency increases with increase in printing temperature. They concluded that,
printing temperature should be chosen considering polymer architecture and nanocomposite
morphology. Balchan and Drickamer [11] studied the effects of pressure from 60 to over 400 kbar on
resistance of iodine and selenium. A rapid drop in resistance of selenium was seen between 60 and 128
kbar then a discontinuous drop. When pressure if further increased, its behaviour is apparently metallic.
Iodine shows rapid drop in resistance between 60 and 255 kbar, further increasing pressure shows slower
drop in resistance. Sobczak and Asthana[12] reviewed the effect of pressure on solidification structure
formation in metal castings. They analysed effects of pressure on nucleation growth, phase diagrams,
interfacial energy and diffusion coefficient. Refinement of structure was seen to be promoted due to
high pressure which may be caused by reduced critical radius and reduced rate of new phase nucleation
and decreased interfacial free energy. Russell J. Hemley[13] studied the effect of high pressure on
molecules such as halogens, nitrogen and group V, oxygen and chalcogens, CO and CO2, Simple
hydrocarbons, H2O, related hydrogen bonded systems, simple molecular mixtures, clusters and complex
molecules. Resit Unal and Dean[14] used Taguchi approach in their study to design and optimize quality
and cost. They presented and overview of Taguchi method with steps involved. They found out Taguchi
method is a powerful tool which can simultaneously improve quality and cost. They concluded, Taguchi
method emphasizes on pushing quality back to design stage, resulting in designing a product or process
which is robust to cause quality problems. Mohan Pandey et. al. [15] presented and classified different
slicing algorithms used in rapid prototyping or layered manufacturing process into two categories, one
which consider build edge as rectangular and other which consider build edge as a slope. Ahn et al.[16]
studied the surface roughness in parts produced by fused deposition modelling. They presented a new
approach to formulate surface roughness. Effects of surface angle, layer thickness, cross-sectional shape
of filament and overlap interval on surface roughness were showed. They concluded surface roughness
expression can predict roughness of FDM parts. Boschetto and Bottini [17] formulated a method to
predict dimensional accuracy and surface roughness of FDM parts as a function of process parameters
such as layer thickness and deposition angle. They investigated 60 different deposition angles between
0-180˚. The used ABS for their research. They performed a case study which evidenced that it is possible
to predict dimensional deviations and geometrical tolerances. They concluded that dimensional
deviations are greatly influenced by deposition angle. Bellini et al.[18] studied new developments in
field of fused deposition modelling of ceramics. They developed a new extrusion system which uses
granules instead of filament. Core finding of this study is overcoming the limitations presented by
material being in filament form by using granular form. Pandey et al.[19] presented a semi empirical


---


## Page 5


CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
4
model for evaluation of surface roughness of a FDM part. One of the major problems in FDM part is
surface roughness caused by staircase effect. Hot cutter machining (HCM) is used to address this
problem. To find significance index of process variables ANOVA is used. They concluded that HCM
can achieve a surface finish of the order 0.3 µm with 87% confidence level.
The process parameters taken into consideration for optimization for a FDM process are generally the
parameters which could be controlled by the FDM machine itself. In other words, only the parameters
bound to the FDM machine are to be optimized while external factors like surrounding temperature,
pressure, humidity remains unchanged. These external factors can greatly affect the quality and
characteristics of parts produces by FDM. In this study, surrounding pressure is treated as a process
parameter and its value is varied to analyse the effect of surrounding pressure as well as other process
parameters on strength of FDM manufactured parts. Effect of pressure on properties and structure of
material is extensively studied by Nobel laureate physicist P.W. Bridgman[23]. His work showed
importance of pressure for studying changes in structure and properties of matter. It was suggested by
J.D. Bernal in 1928 that all matter should become metallic at sufficiently high pressure due to electron
dislocation caused by forced overlap of electrons[15,24].
3. Experimental Methodology
3.1 Selection of process parameters
Based on literature, it was analysed that the process parameters such as layer height, raster angle and
nozzle temperature greatly affect the dimensional accuracy and mechanical properties of printed parts.
In this study, a new process parameter, surrounding pressure is used with all other process parameters
for evaluating its effect on dimensional accuracy in terms of thickness, pressure is not taken as a process
parameter in any study before as per the literature review, so surrounding pressure is a novel parameter
in this study. Three levels of parameters are considered for sample preparation because Taguchi l9
method is being used for process parameter selection in this study. The levels of these parameters were
selected with the help of machine manual and performing the preliminary test on a 3D printer. On the
basis of preliminary experimentation, the ranges and subsequently the levels of the printing parameters
were chosen as shown in Table 1. The parameters which are kept fixed throughout experimentation are
shown in Table 2.
Table 1 Setting of levels for control factors
Control Factors
symbols
units
Levels
I
II
III
Layer Height
A
mm
0.1
0.15
0.2
Raster Angle
B
degree
0
45
90
Nozzle Temperature
C
º C
200
210
220
Surrounding Pressure
D
psi
0
50
100
Table-2: List of fixed parameters
S.No.
Parameter
Fixed Value
1
2
3
4
5
6
Bed Temperature
Nozzle Diameter
Infill Percentage
Printing Speed
 Solid Layers
 Extrusion Width
60℃
0.4mm
100%
3600 mm/min
3
0.4mm


---


## Page 6


CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
5
3.2 Materials
The specimens used in this study are printed using white 1.75±0.03 mm diameter Polylactic Acid (PLA)
filament. The filament was purchased from amazon.in and sold by 3D bazaar. PLA is a thermoplastic
polyester with chemical formula (C3H4O2)n. It the most widely used filament material in FDM printers.
3.3 Experimental Setup
 Inferno i3 FDM 3D printer (Figure 2) is used in this research for producing specimens. This printer is
capable of producing specimen up to a maximum size of 220*220*250mm by using polylactic acid
(PLA), Acrylonitrile butadiene styrene (ABS), Polyvinyl Alcohol (PVA), High-density polyethylene
(HDPE) and similar materials as this machine is equipped with heated print bed. This machine is running
on marlin firmware and can print over USB while connected to a computer or via SD card which have
G-code file for the part. To control and vary pressure around FDM printer, an air compressor and an air-
tight enclosure is used, shown in Figure 2. The compressor employs a pressure switch which could be
set to a desired value of pressure and a pressure difference, when the desired pressure is reached. This
pressure switch automatically detects the pressure difference and turns off the compressor if there is any
pressure drop and turns the compressor on, allowing the setup to maintain constant pressure. The printer
is kept inside the enclosure then the lid of the container is sealed with the help of fasteners.
3.4 Sample Preparation
The samples used in this study are modelled based on ISO 527-2 (Model 5A) which is standard used for
determination of tensile properties of reinforced and non-reinforced plastics [25]. Figure 3 indicates the
dimensions and shape used to create CAD model. All test specimens are printed using Polylactic Acid
(PLA) on Inferno i3 FDM printer. To evaluate the influence of processing parameters over the
dimensional accuracy and repeatability of samples, the samples were measured and compared with CAD
model. Thickness of printed parts of all 9 samples was measured using a vernier calliper (least count of
0.01 mm) at 3 different points along its axis and average of 3 was taken as a result (Figure 4).

Figure 2 Experimental Setup



Figure 3 Specimen CAD model, dimensions in mm         Figure-4: Measurement of dimensions


---


## Page 7


CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
6
3.5 Experimental design based on Taguchi Method
In order to evaluate the effect of printing parameters of FDM process in terms of dimensional accuracy
of width of parts, a Taguchi method is used here to optimize the process. The Taguchi method has
become a powerful tool for the systematic application of design and analysis of experiments for the
purpose of designing and improving the product quality[26].
According to Taguchi methodology, the characteristic that a target value represents best performance in
terms of dimensional accuracy, is called Nominal is best type of problem. The S/N ratio can be
calculated as shown below:
𝑆𝑁
⁄
= −10 log10
((𝑦1−𝑚)2+(𝑦2−𝑚)2+⋯)
𝑛
                        (1)
Where, m = Target value
              n = Number of repetitions
Table 3 Response values using L9 orthogonal array
Experiment Number
A
B
C
D
Thickness (mm)





Trial
Average
value
S/N ratio
(db)
1
2
3
1
1
1
1
1
1.99
2
1.98
1.99
37.78
2
1
2
2
2
2.01
2.01
2.04
2.02
32.22
3
1
3
3
3
1.97
2.01
2.01
2.00
34.36
4
2
1
2
3
2.02
2.05
2.02
2.03
29.59
5
2
2
3
1
2.01
2.02
2.07
2.03
27.45
6
2
3
1
2
2.03
2.01
1.98
2.01
33.31
7
3
1
3
2
2.1
2.09
2.14
2.11
19.01
8
3
2
1
3
2.09
2.06
2.15
2.10
19.43
9
3
3
2
1
2.07
2.15
2.13
2.12
18.31


Figure 5 Printed parts by FDM process
L9 orthogonal array chosen for the experimentation in which 9 rows corresponding to the number of
experiments, with 4 columns at three levels as shown in Table 3. The experiments were performed for
each combination of rows as per selected L9 orthogonal array and the results are indicated in Table 3.
Figure 5 shows the all 9 printed parts under printing parameters shown in Table 3. Figures 7, 8, 9 show


---


## Page 8


CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
7
the optical micrographs of the surface of the FDM printed parts under different printing conditions.
Dimensional accuracy plays an important role in the assembly of the final product.
4. Result and Discussion
In the present study, the first step in the analysis is to review the test results for each experiment
conducted by the Taguchi’s L9 OA. The S/N ratios are calculated for each experiment by applying
Nominal the Best characteristics, as shown in Table 3. The plot of average values of S/N ratio for each
factor at different levels are shown in Figure 6. In S/N analysis, the greatest value of S/N represents a
more desirable condition for a particular control factor. Figure 6 suggests that the factors at levels A1,
B1, C1, D2, are the best levels that give the target value of the thickness.
Effects of layer height on dimensional accuracy are clearly visible in this study. It is seen that as the
layer height is increased, dimensional accuracy is decreased. When a layer is printed on top of previous
layer, a step is formed and this is called stepping effect. At lower layer height, this stepping effect is
minimized an it results in a smoother and even surface finish. Lower layer height is also known as higher
resolution for 3D printed parts because better surface finish and so have greater dimensional accuracy.
In this study, 0.1mm layer height is optimum layer height because it shows minimum deviation and
highest accuracy. The same results have been observed by [18] in his study. It is observed that as the
nozzle temperature is increased, the dimensional accuracy is decreased within the temperature range
taken in this study, which might be a result of increasing fluidity of extruded PLA with increase in
extrusion temperature. The extruded material, which is in semi liquid form, tends to flow in any direction
it is free to flow, but it gets a very small fraction of time to do so because it begins to cool as soon as it
is out of nozzle. When extrusion temperature is increased, the extruded material takes more time to cool
down and thus have a little longer to flow, which causes dimensional inaccuracy. In this study, 200℃
is optimum nozzle temperature. Higher dimensional accuracy is seen in parts which are printed at 0˚
raster angle in this study which might be because when printing at 0˚ raster angle, all the layers are
printed parallel to x-axis and subsequent layers are also parallel which results in higher accuracy.

Figure 6 Effect of control factors on thickness
Analysis of Variance (ANOVA) is executed on S/N data and indicated in Table 4. Table 4 describes that
the percent contribution of factor D (surrounding pressure) is very small (0.06 %) in comparison to
factors A, B and C. Hence factor D can be treated as an error. Table 5 indicate pooled ANOVA at 95%
15
20
25
30
35
40
A1 A2 A3
B1
B2
B3
C1
C2
C3
D1 D2 D3
Mean of S/N ratios (db) for Thickness


---


## Page 9


CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
8
confidence interval for S/N data. Table 5, the percent contribution of parameters affecting the target
value of thickness, i.e., layer height (92.15%), raster angle (0.53%) and nozzle temperature (1.14%),
indicates the influence of layer height is more than the other process parameters. In Table 5, the error
percentage contribution is less than 15%. Therefore, it is verified that no significant process parameters
are omitted during the experiment, therefore, no opportunity for the further improvement.
Table 4 ANOVA for S/N ratio
Factor
DOF
Sum of Square (SS)
Variance (V)
Percent Contribution (%P)
A
2
399.11
199.55
92.15
B
2
11.16
5.58
2.58
C
2
22.57
11.28
5.21
D
2
0.26
0.13
0.06
Error
0
0
indeterminate
Total
8
251.45


Table 5 Pooled ANOVA for S/N ratio
Factor DOF Sum of
Square (SS)
Variance
(V)
F-ratio
Pure Sum
(S´)
Percent Contribution
(%P)
A
2
399.11
199.55
1511.36
398.35
92.09
B
2
11.16
5.58
42.26
2.32
0.53
C
2
22.57
11.28
85.48
4.95
1.14
Error
2
0.26
0.13


6.23
Total
8
251.45



100
𝐹0.05(2,2) = 19.0
4.1 Estimation of Optimum Quality Characteristics
After analysis, the selected significant process parameters are A1, B1 and C1. The optimum value of
width can be evaluated as:
𝜇= 𝑇̅ + (𝐴1
̅̅̅ −𝑇̅) + (𝐵1
̅̅̅ −𝑇̅) + (𝐶1
̅̅̅ −𝑇̅)                                         (2)
𝑇̅ = 27.94

𝐴1
̅̅̅ = 34.79
𝐵1
̅̅̅ = 28.79
𝐶1
̅̅̅ = 30.17

𝜇= 37.74 mm
𝐹0.05(2,2) = 19.0         (Tabulated)
Confidence Interval = C.I. = ±√𝐹∝(2,2) 𝑉𝑒
𝑁𝑒
F (2,2) = F-Value from F-Table for minimum DOF (2) and error DOF (2)
𝑉𝑒= Error Variance = 0.13
𝑁𝑒= Effective Number of Replications =
𝑇𝑜𝑡𝑎𝑙 𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑅𝑒𝑠𝑢𝑙𝑡𝑠
𝐷𝑜𝑓 𝑜𝑓 𝑀𝑒𝑎𝑛+𝐷𝑜𝑓 𝑜𝑓 𝑎𝑙𝑙 𝐹𝑎𝑐𝑡𝑜𝑟𝑠
𝑁𝑒=
9
1+6 =1.28


---


## Page 10


CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
9
Confidence Interval = 𝐶. 𝐼. = ±1.92
37.74 −1.92 < 𝜇< 37.74 + 1.92
For 95% C.I., the predicted optimum thickness in decibel is
35.82 < 𝜇< 39.66
For 95% C.I., the predicted optimum thickness in mm is
2.01 < 𝑡ℎ𝑖𝑐𝑘𝑛𝑒𝑠𝑠< 1.97

5. Confirmation Experiments
The confirmation step is the final step to authenticate the results obtained from the analysis phase. The
expected value of thickness at optimum condition is equal to 37.74 db (= 2.00 mm) which is already
calculated in Section 4. Three confirmation experiments are conducted for significant parameters at their
optimal levels obtained in the analysis phase. The average value of thickness at the optimal setting of
process parameters of the FDM process was observed to be 36.68 db. The result of the confirmation
experiment is shown in Table 6. The value of width lies within the range calculated in the analysis phase.
An error of 1.58 % is observed. Therefore, the optimal setting of process parameters, predicted in the
analysis phase, can be recommended. Optical micrograph of confirmation experiment is shown in Figure
9.
Table 6 Result of confirmation experiments
Optimal printing parameters

Prediction
Experimental
Levels
A1B1C1D2
A1B1C1D2
Thickness (db)
37.74
37.14
6. Surface morphology
The samples were observed under an optical microscope (Nikon YTV55) to understand and study their
microscopic structure, voids and irregularities. The samples were observed in such a manner that
different layers could be seen. When samples were observed under microscope, the irregularities in
extruded PLA were clearly visible. The parts printed at 0.1mm layer height have less irregularities and
as the layer height is increased irregularities gradually increased, shown in Figures 7, 8 and 9.




Figure 8 Optical micrograph
of part printed by experiment
9 (A= 0.2 mm, B= 90º, C=
220º C, D= 0 psi)
Figure
9
Optical
micrograph of part printed
by confirmation experiment
(A= 0. mm, B= 0º, C= 200º
C, D= 0 psi)
Figure
7
Optical
micrograph
of
part
printed by experiment 1
(A= 0.1 mm, B= 0º, C=
200º C, D= 0 psi)


---


## Page 11


CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
10
The irregularities obtained in the parts at higher layer height might be caused due to large
compressive force (due to weight of a layer) experienced by extruded material at thick layer height
and it caused the extruded semi liquid material to squeeze. As the layer height is decreased, the value
of compressive force is reduced and material got more space to settle which resulted in less squeezing
of material and hence less irregularities.
7. Conclusions
1. The lower value of layer height (0.1mm), lower value of raster angle (0º) and lower value of nozzle
temperature (200º C) are significant printing parameters to achieve the target value (2 mm) of
thickness.
2. Statistically, influence of layer height is more than any other parameters to maintain dimensional
accuracy.
3. The value of part’s thickness (37.14 db) obtained by confirmation experiment is very close to the
predicted value (37.74 db) at optimal setting of process parameters.
4. The predicted optimal range of thickness at 95% confidence interval is
2.01 𝑚𝑚< 𝑡ℎ𝑖𝑐𝑘𝑛𝑒𝑠𝑠< 1.97 𝑚𝑚
5.  Effects of surrounding pressure on dimensional accuracy are not clearly visible in the range taken in
this study (0-100psi). Therefore, it can be said that the parameter surrounding pressure is ineffective
within this range on dimensional accuracy of FDM parts. Further increasing pressure may have some
effects and there is scope to study this parameter further.

References
[1]
Espalin D, Muse DW, MacDonald E, Wicker RB. 3D Printing multifunctionality: Structures
with electronics. Int J Adv Manuf Technol. 2014;72(5–8):963–78.
[2]
Prashantha K, Roger F. Multifunctional properties of 3D printed poly(lactic acid)/graphene
nanocomposites by fused deposition modeling. J Macromol Sci Part A Pure Appl Chem. 2017
Jan 2;54(1):24–9.
[3]
Alafaghani A, Qattawi A, Alrawi B, Guzman A. Experimental Optimization of Fused
Deposition Modelling Processing Parameters: A Design-for-Manufacturing Approach.
Procedia Manuf. 2017;10:791–803.
[4]
Zein I, Hutmacher DW, Tan KC, Teoh SH. Fused deposition modeling of novel scaffold
architectures for tissue engineering applications. Biomaterials. 2002;23(4):1169–85.
[5]
Dean EB, Unal R. Taguchi Approach to Design Optimization for Quality and Cost: An
Overview. Annu Conf Int Soc Parametr Anal. 1991;1–10.
[6]
Srivastava M, Maheshwari S, Kundra TK, Rathee S. Estimation of the effect of process
parameters on build time and model material volume for fdm process optimization by response
surface methodology and grey relational analysis. In: Advances in 3D Printing and Additive
Manufacturing Technologies. Springer Singapore; 2016. p. 29–38.
[7]
Panda SK, Padhee S, Sood AK, Mahapatra SS. Optimization of Fused Deposition Modelling
(FDM) Process Parameters Using Bacterial Foraging Technique. Intell Inf Manag.
2009;01(02):89–97.


---


## Page 12


CEME 2020
IOP Conf. Series: Materials Science and Engineering
1168  (2021) 012022
IOP Publishing
doi:10.1088/1757-899X/1168/1/012022
11
[8]
Hmeidat NS, Kemp JW, Compton BG. High-strength epoxy nanocomposites for 3D printing.
Compos Sci Technol. 2018 May 26;160:9–20.
[9]
Papon EA, Haque A. Tensile properties, void contents, dispersion and fracture behaviour of 3D
printed carbon nanofiber reinforced composites. J Reinf Plast Compos. 2018 Mar 1;37(6):381–
95.
[10]  Cataldi A, Rigotti D, Nguyen VDH, Pegoretti A. Polyvinyl alcohol reinforced with crystalline
nanocellulose for 3D printing application. Mater Today Commun. 2018 Jun 1;15:236–44.
[11]  Coppola B, Cappetti N, Di Maio L, Scarfato P, Incarnato L. Influence of 3D printing
parameters on the properties of PLA/clay nanocomposites. In: AIP Conference Proceedings.
American Institute of Physics Inc.; 2018.
[12]  Ceretti E, Ginestra P, Neto PI, Fiorentino A, Da Silva JVL. Multi-layered Scaffolds Production
via Fused Deposition Modeling (FDM) Using an Open Source 3D Printer: Process Parameters
Optimization for Dimensional Accuracy and Design Reproducibility. In: Procedia CIRP.
Elsevier B.V.; 2017. p. 13–8.
[13]  Coppola B, Cappetti N, Maio L Di, Scarfato P, Incarnato L. 3D printing of PLA/clay
nanocomposites: Influence of printing temperature on printed samples properties. Materials
(Basel). 2018 Oct 11;11(10).
[14]  Balchan AS, Drickamer HG. Effect of pressure on the resistance of iodine and selenium. J
Chem Phys. 1961;34(6):1948–9.
[15]  Sobczak JJ, Drenchev L, Asthana R. Effect of pressure on solidification of metallic materials.
Int J Cast Met Res. 2012;25(1):1–14.
[16]  Hemley RJ. Effects of high pressure on molecules. 2000;c:763–800.
[17]  Unal, Resit; Dean EB. Taguchi approach to design optimization... Annu Conf Int Soc Parametr
Anal. 1991;1–10.
[18]  Mohan Pandey P, Venkata Reddy N, Dhande SG. Slicing procedures in layered manufacturing:
A review. Rapid Prototyp J. 2003;9(5):274–88.
[19]  Ahn D, Kweon JH, Kwon S, Song J, Lee S. Representation of surface roughness in fused
deposition modeling. J Mater Process Technol. 2009;209(15–16):5593–600.
[20]  Boschetto A, Bottini L. Accuracy prediction in fused deposition modeling. Int J Adv Manuf
Technol. 2014;73(5–8):913–28.
[21]  Bellini A, Shor L, Guceri SI. New developments in fused deposition modeling of ceramics.
Rapid Prototyp J. 2005;11(4):214–20.
[22]  Pandey PM, Reddy NV, Dhande SG. Improvement of surface finish by staircase machining in
fused deposition modeling. J Mater Process Technol. 2003;132(1–3):323–31.
[23]  Bridgman PW. The physics of high pressures. London: G. Bell & Sons, Ltd.; 1931.
[24]  Bernal JD. The problem of metallic state. 1929;
[25]  ISO 527-2. International Standard. 2019.
[26]  Kumar K, Agarwal S. Multi-objective parametric optimization on machining with wire electric
discharge machining. Int J Adv Manuf Technol. 2012;62(5–8):617–33.


---
