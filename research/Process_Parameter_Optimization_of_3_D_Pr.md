# Process_Parameter_Optimization_of_3_D_Pr

> **Source:** `Process_Parameter_Optimization_of_3_D_Pr.pdf`
> **Converted:** 2025-11-22 21:18:09
> **Method:** PyMuPDF

---

## Page 1


VOL. 12, NO. 7, APRIL 2017                                                                                                              ISSN 1819-6608
ARPN Journal of Engineering and Applied Sciences
©2006-2017 Asian Research Publishing Network (ARPN). All rights reserved.

www.arpnjournals.com


                                                                                                                                               2291
PROCESS PARAMETER OPTIMIZATION OF 3D PRINTER USING
RESPONSE SURFACE METHOD

M. A. Nazan1, F. R. Ramli1, 2, M. R. Alkahari1, 2, M. N. Sudin1, 2 and M. A. Abdullah1, 2
1Faculty of Mechanical Engineering, Universiti Teknikal Malaysia Melaka, Hang Tuah Jaya, Durian Tunggal, Melaka, Malaysia
2Centre for Advanced Research on Energy, Universiti Teknikal Malaysia Melaka, Hang Tuah Jaya, Durian Tunggal, Melaka, Malaysia
E-Mail: muhd_afdhal@hotmail.com

ABSTRACT
The purpose of this paper is to minimize the warp deformation that usually occurs to plastic part produced by 3D
printers. The process involved 3D solid modelling to design, 3D printing with coated adhesive applied on the printing
platform, warping deformation measurement and statistical analysis. The optimization processes involved Design on
Experiment (DOE) technique where Responses Surface Methodology (RSM) is applied by using Minitab software. The
experiment produced the minimum result of warping deformation value when the layer temperature, infill density, first
layer height and other layer height is 192°C, 13%, 0.20mm and 0.30mm respectively.

Keywords: 3D printer, warping deformation, response surface method.

INTRODUCTION
Open
source
3D
printer
is
an
additive
manufacturing technology that has revolutionized the
manufacturing field and has been slowly replacing the
conventional subtractive process. As a good example, the
additive manufacturing allowed complex geometry to be
produced [1] in simple three dimensional axes of
production. The capability of the new technology has
grown and slowly replacing the conventional. These recent
years, it has drawn significant attention to industry and
academia [2] due to the ability to capitalize on the
consolidated advantages of independent process such as
FDM.
Fused Deposition Modelling is a process that
using similar conventional technique, injection moulding
product formation. The different about moulding using
FDM machine is, it does not use any housing or moulding
to form the product but use a platform that has flat surface
such as glass and steel. The process involved molten
plastic or wax extruded by a hot end nozzle that traces the
parts cross sectional geometry layer by layer [3]. FDM is
also popular with Rapid Prototype technology which
widely used in industries to build complex geometrical
functional and shape parts in short time [4-5]. Generally, it
was used to fabricate prototypes, tool and functional parts
without geometrical complexity limitations [6].
However, one of the drawbacks of open source
FDM 3D printers is the plastic filament that comes out
from its nozzle tends to shrink and warp, and sometimes
peel away from the bed platform. This warped
deformation issues in 3D printers have been highlighted
by several researchers [7-8]. Refer to K. Herman and other
[9], without heating platform there was known as warping
issues that are most severe for elongated, rectangular
shaped objects. Additional surface preparation by applying
synthetic polymer adhesive between the printing bed and
the first layer had been performed to counter this problem
[10-11]. Due to the different 3D printer process
parametersettings, warping deformation may still occur
and because of that, the best 3D printer parameters sett
need to be figure of to obtain the best printing quality. As
mentioned in previous study [12], it is very difficult to
achieve the best characteristics in the fabricated parts of
understanding the impact on the process variables.
The work presented in this paper study on how
the 3D printer parameters affect the warping deformation
and what are the best process parameter values to
minimize the warping deformations. It is essential to
optimize the printing parameter to achieve desired quality
characteristics in the parts of developing open source 3D
printer [13-14]. This involved Design on Experiment
(DOE) and Response Surface Method (RSM) in the
finding. These methods have been used for optimization of
process parameters in various fields in the function of to
investigate the optimum factor levels for fabricating parts
[15-17].

METHODOLOGY
The investigation started with 3D modelling to
prepare a design by using solid modelling software,
CATIA V5 software. This is used as specimens of the
investigation into reducing the warping deformation
height. Hence, a cuboid model was designed with size of
100.0mm of length, 30.0mm of width and total height of
5.0mm as shown in Figure-1. As mentioned by the
previous researcher, the rectangular shape objects have
high tendencies to warp around its corner [9].  This digital
model is then converted into printing instruction in the use
of open source 3D printers by using Slic3r software.


---


## Page 2


VOL. 12, NO. 7, APRIL 2017                                                                                                              ISSN 1819-6608
ARPN Journal of Engineering and Applied Sciences
©2006-2017 Asian Research Publishing Network (ARPN). All rights reserved.

www.arpnjournals.com


                                                                                                                                               2292


Figure-1. Size of cuboid model which designed in
millimetre unit.

The conversation of the digital solid model to the
printing instruction is needed by the open source 3D
printer where the Slic3r software changed it from
stereolithography (STL) format to machine instruction or
known as G-Programming Language (G-Code). This is
requiring to setting all parameter of the printer such as
platform size and shape of it to avoid the failure in
printing. In order to convert the STL and creates the G-
Code files, there are several independent variables that
need to be set to control the printing process. In this case,
the several settings are used as the independent variable
where it posits on the variables that affect the printing
result as the objectives stated.

Table-1. The parameter of independent variables.

Symbol
Independent variables
Parameters
𝑇
Layer temperature (°C)
180°C -200°C
𝜌
Fill density (%)
0% - 30%
ℎଵ
First layer height (mm)
0.2mm-0.4mm
ℎଶ
Other layer height (mm)
0.2mm -0.3mm

With the DOE techniques, a screening process of
four parameters which are layer temperature, infill density,
first layer height and the other layer height was varied and
16 samples were prepared as summarized in Table 1 to
form a factorial regression. Based on the table, it shows
that the independent parameters which give credence on
the warping deformation height. Based on observation
which was made before, the recommended sett ranges are
in between as mentioned in the parameter column in the
Table-1.
In the process of fabrication the cuboid model,
the Kossel Mini Delta 3D printer machine and Polylactic
Acid (PLA) material was used. This machine is built
without heating platform and only used a round glass bed
with size 180mm diameters and printable height up to
240mm. Hence, the printing platform required to coat by a
type of adhesive layer where this paper was used synthetic
polymer adhesive, Polyvinylpyrolidone (PVP) to reduce
warping deformation of the first layer. The experiments
were rotated using different parameter that has been
obtained by the DOE process. In order to measure the
warping deformation, vernier height gauge was utilized.
Equation-1 and Figure-2 shows the method to measure the
warping deformation.

𝑤𝑎𝑟݌𝑖݊݃ ݂݀݁݋𝑟݉𝑎𝑡𝑖݋݊, 𝑦= 𝑦ଵ−𝑦ଶ                            (1)



Figure-2. Method of measurement at each sample’s
corner.

By referring to Equation-1, the value of warping
deformation, y is obtained by subtracting the value of   ,
value of total height and, the deflected total height. Four
corners of the cuboid part with five attempts each were
measured and the average value of warping deformation,
are calculated. Statistical software, Minitab 17.0 software,
DOE and RSM are applied to minimize the warping
deformations. The software is used to generate the design
matrix for the DOE with each run corresponding to the
various factor levels combination that will produce the
responses to quality characteristics of dimensional
accuracy and surface finishing [12]. A sample of the
optimization parameter value was then produced by 3D
printers to check for its accuracy of the RSM and the
optimization process

RESULTS AND DISCUSSIONS
Figure-3 shows a cuboid printed sample where
warping deformation occurs at its corners as in circles. All
samples taken in this experiment have more or less
deformation around their corners.



Figure-3. Deflected sample by warping deformation
problem shown in the circles.


---


## Page 3


VOL. 12, NO. 7, APRIL 2017                                                                                                              ISSN 1819-6608
ARPN Journal of Engineering and Applied Sciences
©2006-2017 Asian Research Publishing Network (ARPN). All rights reserved.

www.arpnjournals.com


                                                                                                                                               2293
Table-2. DOE result of warping deformation.

No.
Independent
variables
Dependent variables
Layer
Temperature,  (°C)
Infill Density, (%)
First Layer Height,
(mm)
Other Layer
Height,  (mm)
Corner Y1 (mm)
Corner Y2 (mm)
Corner Y3 (mm)
Corner Y4 (mm)
1
180
10
0.2
0.2
0.10
0.03
0.09
0.09
2
180
10
0.4
0.2
0.17
0.17
0.04
0.12
3
180
30
0.2
0.2
0.23
0.15
0.22
0.20
4
180
30
0.4
0.2
0.19
0.09
0.08
0.19
5
180
10
0.2
0.3
0.02
0.02
0.04
0.05
6
180
10
0.4
0.3
0.03
0.11
0.02
0.02
7
180
30
0.2
0.3
0.03
0.20
0.03
0.10
8
180
30
0.4
0.3
0.05
0.09
0.06
0.06
9
200
10
0.2
0.2
0.21
0.26
0.27
0.19
10
200
10
0.4
0.2
0.18
0.35
0.21
0.29
11
200
30
0.2
0.2
0.27
0.26
0.19
0.18
12
200
30
0.4
0.2
0.19
0.25
0.30
0.34
13
200
10
0.2
0.3
0.10
0.13
0.05
0.03
14
200
10
0.4
0.3
0.04
0.01
0.14
0.13
15
200
30
0.2
0.3
0.18
0.18
0.06
0.04
16
200
30
0.4
0.3
0.17
0.17
0.18
0.16

Table-2 shows the DOE results of tabulation data
reading at each four corner and is represented by layer
temperature, infill density, first layer height and other
layer height. This is as the first step of optimization where
the data is collected based on the DOE techniques and the
data showed are fluctuations of the reading at each corner
as the symbol Y1, Y2, Y3 and Y4 is referred. Based on the
result, it shows that the minimum value that ever was
measured is 0.01 millimetres which meant that there is no
corner had any effect. Figure-4 below shows example of
Pareto chart that shows the trending of the effects of each
independent variable that are tested for corner Y1. It
shows that the height effects variable is D, other layer
height followed by A, layer temperature and B, infill
density. Based on the data, first layer height variable, C
had less influence on the warping deformation.



Figure-4. Pareto chart of the effects at Y4.

The obtained main effect plotted in Figure-5
shows that the temperature, infill density and other layer
height has high influence on the deformation values
compared to first layer height parameters as well as the
Pareto chart above.  The first layer height does not show
any major effect on the warping deformation by having the
lowest gradient trend.



Figure-5. Main effect plot correspond to warping
deformation for Y2.

In order to create the response surface plot, an
improvement is needed to be complete. This step is to plot
the independent variables that have high impact on the
dependent variables. Other experiments are also needed in
order to analyse the result. The analysis would be more
focusing on the factors that really affect the warping
deformations.

Table-3. Improved data analysis by creating response
surface design.

No.
Independent
variables
Dependent variables
𝑻
𝝆
𝒉૚
𝒉૛
Y1
Y2
Y3
Y4
1
180
10
0.3
0.20
0.17
0.17
0.04
0.12
2
180
30
0.3
0.20
0.19
0.09
0.08
0.19
3
180
10
0.3
0.30
0.03
0.11
0.02
0.02
4
180
30
0.3
0.30
0.05
0.09
0.06
0.06
5
200
10
0.3
0.20
0.18
0.35
0.21
0.29
6
200
30
0.3
0.20
0.19
0.25
0.30
0.34
7
200
10
0.3
0.30
0.04
0.01
0.14
0.13
8
200
30
0.3
0.30
0.17
0.17
0.18
0.16


---


## Page 4


VOL. 12, NO. 7, APRIL 2017                                                                                                              ISSN 1819-6608
ARPN Journal of Engineering and Applied Sciences
©2006-2017 Asian Research Publishing Network (ARPN). All rights reserved.

www.arpnjournals.com


                                                                                                                                               2294
In creating the response surface design, the
maximum and minimum values of the independent
variables is needed. As shown in Table-3, there are only 8
samples left after the first layer height is made constant at
0.3 millimetres. By using these data, the experiment is
continued with creating the response surface design using
central composite analysis with these factors, which are
full design selection and 20 unblocked runs.

Table-4. Central composition analysis.

No.
Independent variables
Dependent variables
𝑻
𝝆
𝒉૚
𝒉૛
Y1
Y2
Y3
Y4
1
180
0.10
0.3
0.20
0.13
0.17
0.04
0.12
2
200
0.10
0.3
0.20
0.15
0.18
0.21
0.29
3
180
0.30
0.3
0.20
0.14
0.09
0.08
0.19
4
200
0.30
0.3
0.20
0.10
0.25
0.26
0.24
5
180
0.10
0.3
0.30
0.13
0.11
0.09
0.03
6
200
0.10
0.3
0.30
0.04
0.01
0.14
0.13
7
180
0.30
0.3
0.30
0.19
0.09
0.11
0.06
8
200
0.30
0.3
0.30
0.18
0.17
0.18
0.16
9
173
0.20
0.3
0.25
0.11
0.18
0.14
0.13
10
206
0.20
0.3
0.25
0.11
0.09
0.19
0.14
11
190
0.03
0.3
0.25
0.12
0.17
0.12
0.24
12
190
0.37
0.3
0.25
0.13
0.25
0.06
0.15
13
190
0.20
0.3
0.17
0.09
0.08
0.10
0.10
14
190
0.20
0.3
0.33
0.11
0.07
0.07
0.07
15
190
0.20
0.3
0.25
0.10
0.05
0.04
0.10
16
190
0.20
0.3
0.25
0.10
0.05
0.04
0.10
17
190
0.20
0.3
0.25
0.10
0.05
0.04
0.10
18
190
0.20
0.3
0.25
0.10
0.05
0.04
0.10
19
190
0.20
0.3
0.25
0.10
0.05
0.04
0.10
20
190
0.20
0.3
0.25
0.10
0.05
0.04
0.10

By referring to the Table-4 above, the central
composition is representing the analysis to second degree
of function. This result is more specific presenting another
six points of the box. As seen at sample number 9 and 10,
the temperatures are shown at 173 °C and 206 °C followed
by other independent variables, where density and other
layer height are calculated by the Minitab software. As a
result, all the samples had been measured and gathered to
fill in the dependent variables which are the warping
deformation values. As shown in the Figure-6 below, the
main effect plot for Y3 that an analysis of the second
degree for response surface design was obtained. These
parabola plots are the vertex point of warping deformation
at Y3 depending on the value of the factors that are set
while slicing the model. The graph shows that the lowest
value of the warping deformation on each factor is around
180°C to 195°C and for the other layer temperature factor,
near 20 percent of infill density and in between 0.24mm to
0.32mm for the layer height.


Figure-6. Main effect plot for Y3 corresponded
to 𝑇, 𝜌 and ℎଶ.

Figure-7 shows the contour plot of the Y3 corner
which responded to the factors. This plot is similar with
the previous plot in the Figure-6. This contour is showing
the best result of minimum warping deformation value is


---


## Page 5


VOL. 12, NO. 7, APRIL 2017                                                                                                              ISSN 1819-6608
ARPN Journal of Engineering and Applied Sciences
©2006-2017 Asian Research Publishing Network (ARPN). All rights reserved.

www.arpnjournals.com


                                                                                                                                               2295
on the middle of the dark blue coloured circle by
comparing the relation between the factors such as layer
temperature and infill density, temperature and layer
height, and also the infill density and the layer height. As
referred to the plot of layer temperature versus infill
density, it shows that the greatest result of warping
deformation is in between the set of 185°C to 190°C of
layer temperature and 20% of infill density.



Figure-7. Contour plot of Y3 corresponded to the
three factors.

Surface plot is a plot that shows the 3D model of
contour plot which is shown in three axes as shown in
Figure-8. The figure shows the surface plot of Y3 corner
of the density and layer height. As mentioned before in the
contour plot graph is shown the best result in reducing the
warping deformation is at the middle of the contour plot
which is dark blue colour, surface plot is also shown as the
vortex at the middle of the 3D graph where it is clearly
seen responded to minimized at the middle of plot.



Figure-8. Surface plot of Y3 corresponded to𝜌 and ℎଶ.

Table-5. Optimized result of the response surface method.

Independent variables
Responses
Theoreti
cal
Experimen
tal
𝑇
(ºC)
𝜌
(%)
ℎଵ
(mm)
ℎଶ
(mm)
𝑦𝑇 𝑎𝑣𝑔
(mm)
𝑦𝐸 𝑎𝑣𝑔
(mm)
192
13
0.20
0.32
0.03
0.04

Table-3 shows the result of optimization obtained
by using the MiniTab software and the comparison
between theoretical and experimental values, the minimum
warping deformation, yTavg is 0.03mm was achieved.
Sample of experimental with optimized parameters were
proved the accuracy of the RSM and the optimization
result where yEavg is 0.04mm.
CONCLUSIONS
It is concluded that the optimum value of the
independent variables are 192°C of layer temperature,
0.13% of fill density, 0.2mm of first layer height and
0.3mm of other layer height with minimum deformation of
0.03mm. The accuracy of RSM and optimization resulted
a small percentages of error is 33%. The objectives are
achieved by obtaining the synthetic polymer adhesive
shows a good result and also reduced the warping
deformation while printing on the glass platform if
compared to plain or direct to the glass. This shows that
the glass needs an adhesive in order to reduce the warping
deformation also resulted the best printing quality. As
future suggestions, in order to get a greatest result, the
experiment should have a good equipment where it is
more precise to measure the deformation, the experiment
should be alert to the surrounding temperature because it is
believed that another factor for warping deformation and
also the adhesive should be apply correctly to all surface
of the printing platform to avoid the warping to be worsen.

ACKNOWLEDGEMENT
The authors would like to thank to the Ministry of
Higher Education (MOHE), MyBrain15 and Centre for
Advanced Research on Energy (CARe), Faculty of
Mechanical
Engineering
(FKM),
UniversitiTeknikal
Malaysia Melaka (UTeM) for sponsoring this research
study
under
the
research
grants
FRGS/1/2015/TK03/FKM/02/F00270.

REFERENCES

[1] S. Newman, Z. Zhu, V. Dhokia and A. Shokrani.
2015. Process planning for additive and subtractive
manufacturing
technologies.
CIRP
Annals
-
Manufacturing Technology. 64(1): 467-470.
[2] K. Karunakaran, S. Suryakumar, V. Pushpa and S.
Akula. 2010. Low cost integration of additive and
subtractive
processes
for
hybrid
layered
manufacturing. Robotics and Computer-Integrated
Manufacturing. 26(5): 490-499.
[3] L. Novakova-Marcincinova and J. Novak-Marcincin.
2013. Experimental Testing of Materials Used in
Fused Deposition Modeling Rapid Prototyping
Technology. AMR. 740: 597-602.
[4] S. Ahn, M. Montero, D. Odell, S. Roundy and P.
Wright. 2002. Anisotropic material properties of fused
deposition modeling ABS. Rapid Prototyping Journal.
8(4): 248-257.
[5] V. Nidagundi, R. Keshavamurthy and C. Prakash.
2015. Studies on Parametric Optimization for Fused
Deposition Modelling Process. Materials Today:
Proceedings. 2(4-5): 1691-1699.


---


## Page 6


VOL. 12, NO. 7, APRIL 2017                                                                                                              ISSN 1819-6608
ARPN Journal of Engineering and Applied Sciences
©2006-2017 Asian Research Publishing Network (ARPN). All rights reserved.

www.arpnjournals.com


                                                                                                                                               2296
[6] A. Boschetto and L. Bottini. 2016. Design for
manufacturing of surfaces to improve accuracy in
Fused Deposition Modeling. Robotics and Computer-
Integrated Manufacturing. 37: 103-114.
[7] W. Z. Wu, P. Geng, J. Zhao, Y. Zhang, D. W. Rosen
and H. B. Zhang. 2014. Manufacture and thermal
deformation analysis of semicrystalline polymer
polyether ether ketone by 3D printing. Materials
Research Innovations. 18(S5): S5-12-S5-16.
[8] F. Ramli, M. Jailani, H. Unjar, M. Alkahari and M.
Abdullah. 2015. Integrated recycle system concept for
low cost 3D-printer sustainability. Proceeding of
Mechanical Engineering Research Day.pp. 77-78.


[9] K. Herrmann, C. Gärtner, D. Güllmar, M. Krämer and
J. Reichenbach. 2014. 3D printing of MRI compatible
components: Why every MRI research group should
have a low-budget 3D printer. Medical Engineering &
Physics. 36(10): 1373-1380.
[10] A.H.Peng and X.M.Xiao. 2012. Investigation on
reasons Inducing Error and Measures Improving
Accuracy in Fused Deposition Modelling. Advances
in Information Sciences and Service Sciences. 4(5).
[11] M. Nazan, F. Ramli, M. Alkahari, M. Sudin and M.
Abdullah. 2016. Optimization of warping deformation
in open source 3D printer using response surface
method. Proceeding of Mechanical Engineering
Research Day. 2016, pp. 71-72.
[12] S. Masood, K. Mau and W. Song. 2010. Tensile
Properties of Processed FDM Polycarbonate Material.
Materials Science Forum. 654-656: 2556-2559.
[13] S. Kumar and V. Kannan. 2016. Parameter
Optimization of ABS-M30i parts Produced by Fused
Deposition
Modelling
for
Minimum
Surface
Roughness.
International
Journal
of
Current
Engineering and Technology. (3): 93-97.
[14] Stephen
OluwasholaAkande. 2015. Dimensional
Accuracy and Surface Finish Optimization of Fused
Deposition
Modelling
Parts
using
Desirability
Function Analysis. IJERT. 4(04).
[15] B.
Vasudevarao.
2000.
Sensitivity
of
Rapid
Prototyping Surface Finish to Process Parameter
Variation. Solid Freeform Fabrication Proceedings.
[16] H. Liao and J. Shie. 2007. Optimization on selective
laser sintering of metallic powder via design of
experiments method. Rapid Prototyping Journal.
13(3): 156-162.
[17] H. Zhu, N. Li and Z. Liu. 2011. The Method for the
Accuracy Improvement of STL Offset Model Based
on Vertex Offset. AMR. 308-310: 1600-1603.


---
