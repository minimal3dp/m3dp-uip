# polymers-13-02190-v2

> **Source:** `polymers-13-02190-v2.pdf`
> **Converted:** 2025-11-22 21:18:09
> **Method:** PyMuPDF

---

## Page 1


polymers
Article
Relationship between FDM 3D Printing Parameters Study:
Parameter Optimization for Lower Defects
Patrich Ferretti, Christian Leon-Cardenas
, Gian Maria Santi
, Merve Sali, Elisa Ciotti, Leonardo Frizziero *
,
Giampiero Donnici
and Alfredo Liverani


Citation: Ferretti, P.; Leon-Cardenas,
C.; Santi, G.M.; Sali, M.; Ciotti, E.;
Frizziero, L.; Donnici, G.; Liverani, A.
Relationship between FDM 3D
Printing Parameters Study: Parameter
Optimization for Lower Defects.
Polymers 2021, 13, 2190. https://
doi.org/10.3390/polym13132190
Academic Editor: H. Jerry Qi
Received: 20 May 2021
Accepted: 24 June 2021
Published: 30 June 2021
Publisher’s Note: MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional afﬁl-
iations.
Copyright: © 2021 by the authors.
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
Department of Industrial Engineering, Alma Mater Studiorum—University of Bologna, I-40136 Bologna, Italy;
patrich.ferretti2@unibo.it (P.F.); christian.leon2@unibo.it (C.L.-C.); gianmaria.santi2@unibo.it (G.M.S.);
merve.sali2@unibo.it (M.S.); elisa.ciotti@studio.unibo.it (E.C.); giampiero.donnici@unibo.it (G.D.);
alfredo.liverani@unibo.it (A.L.)
* Correspondence: leonardo.frizziero@unibo.it
Abstract: Technology evolution and wide research attention on 3D printing efﬁciency and processes
have given the prompt need to reach an understanding about each technique’s prowess to deliver
superior quality levels whilst showing an economical and process viability to become mainstream.
Studies in the ﬁeld have struggled to predict the singularities that arise during most Fused Deposition
Modeling (FDM) practices; therefore, diverse individual description of the parameters have been
performed, but a relationship study between them has not yet assessed. The proposed study lays
the main defects caused by a selection of printing parameters which might vary layer slicing, then
inﬂuencing the defect rate. Subsequently, the chosen technique for optimization is presented, with
evidence of its application viability that suggests that a quality advance would be gathered with such.
The results would help in making the FDM process become a reliable process that could also be used
for industry manufacturing besides prototyping purposes.
Keywords: optimized FDM; defects; printing parameters; optimization; void occurrence
1. Introduction
The Fused Filament Fabrication (FFF) process was ﬁrst introduced under the name
of FDM® in the 1990s, patented as a moldless, fabrication method for three-dimensional
solid objects (US Patent No. 5,738,817). Nowadays, it is among the most popular additive
manufacturing techniques because it offers a versatile choice of thermoplastic materials [1].
It consists of a continuous process of depositing successive layers, from the bottom to the
top by heating and extruding a ﬁlament [2], therefore, building a three-dimensional solid
object having complex shapes, as reported by the studies of SAVU et al. [3], Mahamood
et al. [4], and Brian et al. [5]. The research by Tofail et al. [6] stated that FDM can build fully
functional parts of a product.
In addition, a potential cost-effective solution for small-scale components can be found
in the metal-fused ﬁlament fabrication (FFF) process, since regular desktop FFF printers
could be used to create metal-sourced objects [7].
1.1. FDM 3D Printing
Additive manufacturing (AM) or 3D printing technology is the deﬁnition of a method-
ology that can produce complex, irregular shaped three-dimensional (3D) which would
be more time- and resource-consuming if used traditional machining methods for its
manufacturing. Producing parts in small lots at a fast speed without a mold.
Achieving a better understanding in FDM processing promises to solve cost problems
of other non-conventional FDM methodologies like SLS (Selective Laser Sintering), Poliget
(Stratasys, Object), SLA (Stereolithography), DLP (Digital Light Processing), and MSLA
(Masked Stereolithography) as reviewed by [8–12] that had shown to reach better quality
Polymers 2021, 13, 2190. https://doi.org/10.3390/polym13132190
https://www.mdpi.com/journal/polymers


---


## Page 2


Polymers 2021, 13, 2190
2 of 15
than FDM, but could be more expensive to apply due to the need to use a more specialized
equipment, the type of polymers available [13] for each method, and the need to add other
components like resins that will be important to reach desired mechanical characteristics.
1.2. Defects in 3D Printing
Defects play a key role in 3D printing since they are responsible for the reduction in
mechanical properties with respect to injection molded parts. As suggested in [14], the
presence of pores/voids in the 3D printed structure leads to a decrease in the ﬁnal density
of the specimen and depends on the printing parameter. In addition, in the FDM printing
process, it is necessary to optimize and reduce the presence of voids in the structure because,
even if the defects undergo a sintering process, they decrease in size, but still remain present
in the structure. Moreover, some pores appear due to the chosen printing strategy (i.e.,
places where two perimeters joined or where the inﬁll started and jointed). This alignment
of pores was observed in CT (Computed Tomography) scans of specimens produced by FFF
with other highly ﬁlled ﬁlaments [15], and they can lead to weaker mechanical properties.
This phenomenon could be seen in Figure 1.

Figure 1. Defect appearance on a PLA specimen: (a) material voids between adjacent lines.
A deep knowledge of FFF process parameters is required to obtain objects with
improved mechanical properties (i.e., tensile strength, compressive strength, etc.) [16].
Moreover, it was observed that FFF 3D printing introduces anisotropic behavior to the
manufactured part by means of gaps that could reduce its tensile strength, both in modulus
and in its failure [17–22].
1.3. Volumetric Flow Rate and Density
The density of the material that is coming off from the nozzle is the result of a series
of parameters all inextricably linked together. In order to identify the complexity of the
problem, an understanding about the deformation ﬁeld due to the surface tension and
the Laplace pressure difference, as reported by Liu et al. [23], and the possibility that the
liquid/vapor interface is pinned on the microstructures, is needed to have an idea about
the behavior of the molten material at high temperature [24]. In the ideal case of constant
extrusion speed over time, the density of the melt coming out of the nozzle is related to the
set extrusion temperature and the nozzle material and length. In fact, the nozzle (in most
cases) also acts as a melting chamber in which the thermoplastic is brought to a sufﬁcient
density to be extruded. The heat transfer between heated block and material depends on
the thermal resistance value of the nozzle. Furthermore, the geometry of the nozzle and


---


## Page 3


Polymers 2021, 13, 2190
3 of 15
heated-block itself inﬂuences the ﬁnal density of the extruded ﬁlament a lot—for example,
the differences between E3D v6 and E3D volcano nozzles as shown in Figure 2.
(a)
(b)
Figure 2. Nozzle length difference according to (a) lower volumetric ﬂow rate, (b) higher volumetric
ﬂow rate.
Constraining the extrusion at constant speed is not a real hypothesis, as the extrusion
speed varies over time, even within the same layer, although the speed set in the slicer is
the same for every sector of the layer (shell, inﬁll, etc.), there are still variations in speed
due to the changes of direction and the fact that, for every line that is not continuous, the
extruder starts from zero speed, accelerates, reaches, if possible, the set speed, decelerates,
and stops. These variations obviously also affect the extrusion speed and consequently the
time the ﬁlament has to be heated inside the fusing chamber, and therefore there are small
variations in the density of the extruded material, previously studied by Pan et al. [25].
It should be noted that, even varying the layer height, keeping the extrusion tempera-
ture constant, results in a variation of the density of the extruded material. Increasing the
layer height will require extrusion of a larger quantity of material (higher volumetric ﬂow
rate), and, consequently, to have the same degree of adhesion, the extrusion temperature
will have to be increased. Therefore, if it is decided to carry out tests on the best layer
height value, the need to take into account the volumetric ﬂow value, and to adjust the
temperature accordingly. Interlayer bonding quality is therefore a result of the temperature
of the extruded material.
Volumetric Flow Rate: depends on a large number of factors, it depends directly on the
actual print speed, width (at width increase, increase the amount of extruded material),
and layer height (greater and higher the amount of extruded material in the unit of time),
as suggested by Percoco et al. [16], the difference of which could be seen in Figure 2.
Delta Temperature: the extrusion temperature, together with the “environment” tem-
perature, determine the actual density of the newly deposited material.
Nozzle Material: Thermal conductivity of steel (23 W/m·K), or copper (330 W/m·K).
By giving a wider desertion about the density explanation performed by Pan et al. [25],
density is consequently a key factor, together with the temperature of the newly extruded
material that allows for achieving excellent adhesion between one layer and the one
afterwards. In order to simplify this model and make it as general as possible, the effect of
density will be incorporated as a correction factor to the main theoretical model.
1.4. A Model for Defect Analysis in FDM Printing
The model arises from the need to understand the inﬂuence of the main printing
parameters on the volume of defects present in the workpiece, in order to make this
analysis as general as possible in a way that it can be used in common polymers for
application in FDM process, but also for MetFDM.
The model focuses on the identiﬁcation of type of defects and the theoretical volume
of those. The model aims to explore the effect of changing nozzle diameter, changing width,
number of shell lines, slicing angle on the single layer, and changing part size, keeping the
above parameters constant.


---


## Page 4


Polymers 2021, 13, 2190
4 of 15
The starting point is the analysis of the shape of a single line and its parameterization.
It was veriﬁed that the model presented by Slic3r [26] and then taken up by PrusaSlicer [27]
and reported in Figure 3 is valid as a simpliﬁcation. In fact, each line is designed with a
geometry that combines two semicircles and a rectangle. This geometry is in fact the same
one that uses the slicer internally to generate the toolpath.

Figure 3. Printing line geometry characterization.
2. Materials and Methods
2.1. Model Construction
2.1.1. Geometry
The geometry chosen to analyze the model is a solid cube (inﬁll set at 100%), the
dimensions of which are set at 30 × 30 × 30 in order to analyze the effect of the various
printing parameters; width and length are changed only if the effect of the component size
on the defect volume is analyzed.
2.1.2. Defect Instances
The ﬁrst hypothesis of this model is that each line touches (in section) the adjacent line
only at one point. This hypothesis allows us to get into a “standard” state, which is in fact
also the way the slicer creates the toolpath, imagining that each line touches the adjacent
line along a line. The inﬁll is set to 100% and the selected inﬁll type is “lines”. The fact that
in reality it is possible for lines to have a non-point contact area will be considered later, as
it is in fact an “improvement” over the point contact condition.
Therefore, four types of defects were identiﬁed. Defects refer to the presence of gaps
in the structure that are not generated randomly, but depend on how the material is placed.
This type of defect is then repeated and, if the conditions during printing do not change
(constant extrusion temperature, constant ambient temperature, no speed changes during
printing, etc.), this type of defect is repeated on each layer.
(A) Defect that considers the volume of missing material compared to a perfectly ﬂat
surface, similar to a surface made with a traditional manufacturing process like injection
molding, for example.
(B) Defects that appear between a shell line and the adjacent shell line; if there are
more than two contour lines, this defect ponders the total volume of the voids.
Details of such defects could be seen in Figure 4.


---


## Page 5


Polymers 2021, 13, 2190
5 of 15
A
B
Figure 4. Defects (A,B).
(C) From a purely geometric point of view, there are no differences in the geometry of
defects B and C, defect C however refers to the lines of the inﬁll (Figure 5).
C
Figure 5. Defect (C).
(D) Defect D, as seen in Figure 6, a defect that takes into account the formation of
empty areas (without extruded material) due to the fact that the number of lines in the
inﬁll is approximated by default.
Figure 6. Defect (D).
After identifying the type of defects and using a spreadsheet, an algorithm was created
to calculate the total volume of defects. To calculate the volume of defects type A and B, it


---


## Page 6


Polymers 2021, 13, 2190
6 of 15
was sufﬁcient to know the width of each line and the initial size of the cube; for defects C
and D, it was necessary to know the length of each line. The veriﬁcation of the algorithm
as seen in Figure 7 was done using gcode generated by Cura software, and then plotting
the various points and lines present in the gcode.


Figure 7. Example of a printing gcode (left); last 8 lines of gcode drawn in geogebra (right); in red: the extrusion moving
path, in gray: the shift movement of a single printer head.
2.1.3. Algorithm Parameters
The parameters taken into account for this study are deﬁned by the total geometry
of the model, geometry of the extruded, molten material and the number of contour lines
that it would take to form the part. Details for parameters of input (Table 1) and output
(Table 2).
Table 1. Algorithm main input parameters.
INPUT
Geometric Dimension of the Test Piece
Slicer Parameters
Parameter
Unit
Parameter
Unit
height
mm
Nozzle dimension
mm
lenght
mm
Line width
mm
width
mm
layer height
mm
Number of outer lines
-
α (raster angle)
◦
Table 2. Algorithm main output parameters.
OUTPUT
Parameter
Unit
Value—About Overall Part Volume
Volume of defects A
mm3
% of defects A
Volume of defects B
mm3
% of defects B
Volume of defects C
mm3
% of defects C
Volume of defects D
mm3
% of defects D
Total volume of defects
mm3
% total of defects


---


## Page 7


Polymers 2021, 13, 2190
7 of 15
3. Results
3.1. Parameter Inﬂuence
3.1.1. Inﬂuence of Shell Number
A number of essays were performed by printing a cube of 30 × 30 × 30 mm, and
keeping constant layer height (0.15 mm) and width (0.4 mm); Figure 8 shows the trial
performed by keeping values for raster angle of the inﬁll at 45◦and increasing the value of
shell lines. This results in the total volume of defects increasing as the number of contour
lines increases. Since the layer height is constant, defects type A and D remained constant.
By varying type B and type C, the variation of the latter leads to a slight increase in the
total volume of defects.
Afterwhile, it can be said that it is good to reduce the number of shell lines as increasing
them does not bring any visible advantage. Furthermore, as theoretically the effect is
minimal, in real terms, it presents some challenges, as the contour lines do not have a raster
angle, and this can result in adhesion issues afterwards.
Figure 8. Inﬂuence of the number of shell (contour) lines on 30 × 30 × 30 mm cube, nozzle 0.4 mm,
line width 0.4 mm, layer height 0.15 mm, raster angle 45◦.
3.1.2. Inﬂuence of Width
The width represents the average distance between a line and the next. Increasing the
width, as shown in the Figure 8, the total volume of defects can be reduced. The lower
limit for the value of the width is usually set equal to the diameter of the nozzle, and
there is the possibility to reduce the value slightly (e.g., when you have to make thin walls,
not multiples of the width, in order to avoid gaps in the printed part), in all other cases,
it is advantageous to increase the width. The maximum attainable value is limited by
two factors:
•
the diameter of the ﬂat area of the nozzle;
•
the density of the extruded material.
For the ﬁrst point, it is essential that all extruded material is contained below the nozzle;
otherwise, defects may occur on the print surface. The density of the extruded material is
crucial, as the material is not simply deposited but is also subjected to a shear stress against


---


## Page 8


Polymers 2021, 13, 2190
8 of 15
the surface of the nozzle and the layer underneath. This results in a backpressure inside
the nozzle which increases as the extrusion temperature decreases (extruded ﬁlament
density). It should also be noted that increasing the width increases the volumetric ﬂow
rate because it increases the amount of material deposited in the unit of time. The risk of
using temperatures that are too low is that of generating ﬁlament stripping or a loss of E
steps. Increasing the width is therefore a very powerful tool but is needed to check the
print parameters carefully. Results of width inﬂuence could be seen in Figures 9 and 10.
Figure 9. Lower extrusion width (on top) and higher extrusion width (on bottom) compared for a
given dimension L.
Figure 10. Inﬂuence of width (considering 2 shell (contour) lines, raster angle 45◦, nozzle 0.4 mm,
layer height 0.15 mm).
3.1.3. Layer Height
It was chosen to keep the width constant and equal to the nozzle diameter, raster
angle at 45◦, two shell lines.


---


## Page 9


Polymers 2021, 13, 2190
9 of 15
Decreasing the layer height is an effective way to reduce the volume of defects, and it
is very interesting to evaluate what happens by changing not only the layer height, but
also the size of the nozzle.
The same cube of 30 × 30 × 30 is kept, but the diameter of the nozzle is increased
and therefore the value of width is increased. Valid values for the layer height are a range
between 15 and 75% of the value of the considered nozzle. It is interesting to see how the
ability to use a larger nozzle can allow you to print at a higher layer height and also reduce
the number of defects. This is possible because increasing the diameter of the nozzle also
increases the width. Figure 11 outlines the effect of layer height by considering different
nozzle diameters.

Figure 11. Different nozzle diameter compared at different layer heights; the width is equal to nozzle
diameter for each of those.
3.1.4. Workpiece Size
Considering a parallelepiped with a square base and ﬁxed height of 30 mm, the aim
was to evaluate the theoretical trend of the defects volume, by increasing and decreasing
the section. The cube parameters are: nozzle 0.4 mm, width 0.4 mm, two shell lines, and
layer height of 0.15 mm.
Displayed in Figure 12, by increasing the section, the volume of defects increased as
expected. The trend begins to undergo important variations when the section decreases.
Finally, at very small sizes, 2 mm, a peak in the volume of defects can be seen. The
oscillations are due to defect D, seen in Figure 6, which becomes more important as the
cross section decreases. Defect D arises from the approximation, by defect, of the number
of internal lines, hence the behavior is oscillatory.


---


## Page 10


Polymers 2021, 13, 2190
10 of 15
Figure 12. Inﬂuence of geometric dimension on volume of defects, layer height 0.15 mm, width
0.4 mm, 2 shell (contour) lines, raster angle 45◦.
Afterwards, the use of a larger nozzle size, such as 0.6, allows for a reduction of defects
as already noted, seen in Figure 11, but the oscillatory behavior becomes evident at higher
values of the cross section, as shown in Figure 13, with respect to the counterpart with a
smaller nozzle.

Figure 13. Comparison on the inﬂuences of the geometry considering the 0.4 mm and 0.6 mm nozzle;
in the case of a 0.4 mm nozzle, the layer height is 0.15 mm, width 0.4 mm; in the case of a 0.6 mm
nozzle, the layer height is 0.2 mm and width 0.6 mm.


---


## Page 11


Polymers 2021, 13, 2190
11 of 15
4. Discussion
The mathematical model allows for evaluating the theoretical behavior, but, in order
to take into account the effect of density (temperature, ﬂowrate, etc.), and the possibility
to have a defects reduction related to printing parameters’ optimization, the following
formulation is proposed:
V% = KAVA + KBVB + KCVC + KDVD
V% is the total volume in percentage of the occurrence of defects, the parameters KA,
KB, KC, and KD allow for adjusting the theoretical model to the real result.
These values can be obtained experimentally, by observing the layer in sections,
through a common microscope and then performing an image analysis.
KA and VA: the ﬁrst element of the equation is related to defects that are present on
the surface of the workpiece, this term can also be related to several aspects including
surface roughness which is directly related to layer height and the staircase effect. It is
difﬁcult to obtain a reduction of this term by changing only the slicing parameter, but it
is possible to obtain a KA value lower than 1 for some materials (e.g., Polymaker PVB)
related to a chemical smoothing.
KB and KC take into account the same type of defect, one in shell lines and the other
in inﬁll lines.
However, KB and KC are not identical and often have different values.
Shell lines are always stacked on top of each other with a 0◦raster angle. This leads to
a high difﬁculty in reducing the defects between these lines.
Experimental evidence showed a maximum reduction of around 80% and the value of
parameter KB in the range KB: 1–0.8.
For KC instead, related to the possibility to have a raster angle for the inﬁll lines
between different layers and related to a proper selection of printing parameters, a greater
reduction of the gaps between lines is possible. The value of KC parameter is in the range
between 0 and 0.9.
KDVD is related to the presence of voids in the inﬁll, and a reduction of these defects
selecting the option “ﬁll small gaps” in the slicer is possible.
Optimization Scheme and Reduction for KC
The proposed optimization procedure is reported in Figures 14 and 15 that allows for
reducing the values of KB and KC, and, consequently, to the total number of voids/defects
existing on the specimen. The procedure allows for ﬁnding the best performing printing
parameters given a speciﬁc 3D printer device and ﬁlament typology; the correct choice
of printing parameters would guarantee optimal mechanical properties of the printed
elements with zero internal voids.
This optimization process starts by using the recommended printing settings given by
the ﬁlament producer. At a ﬁrst stage, the width must be set equal to the nozzle dimension.
Afterwards, the minimization of the layer height is performed according to the nozzle
diameter and the minimum resolution value of the printer. The ﬁrst optimization loop
cycle, seen in Figure 15, is needed to remove the macro defects on the printed surface of
the part. An additional process is focused on removing defects B and C from the part. In
Figure 16, it is possible to see the result of the proposed optimization loop on a 3D printed
PLA specimen.


---


## Page 12


Polymers 2021, 13, 2190
12 of 15
Figure 14. Flow chart of the optimization process.


---


## Page 13


Polymers 2021, 13, 2190
13 of 15
Figure 15. Optimization process loop cycle.
Figure 16. Printing quality on the microscope (20×): (a) not optimized; (b) increasing performance;
and (c) fully optimized.


---


## Page 14


Polymers 2021, 13, 2190
14 of 15
5. Conclusions
A number of different printing trials demonstrated that a variation in the slicing
parameter has a direct effect on the appearance on the four different defect occurrence
types. Furthermore, a reduction of the defect volume is proven to be feasible by means of a
modiﬁcation of input printing parameters like layer and line dimensions, overall number
of shells, as well as ﬁlament-speciﬁc printing parameters like the extrusion multiplier and
temperature. Additional reduction of defects is possible by means of the application of the
proposed optimization methodology that would allow for gathering a correct value of print-
ing settings. Furthermore, the volume of defects implies that mechanical characteristics of
the material would also be compromised because of a poor choice of printing parameters
for a given 3D printer and ﬁlament type. Internal material consistency is not guaranteed,
making the material susceptible to developing failure due to a poor internal stability.
This approach and the proposed formula made it possible to make a valuable com-
parison between the volume of defects existing inside the specimen and the effect of the
optimization procedure in the reduction of such voids, ending up with an internally quasi-
isotropic structure that would mechanically sustain stresses in a similar way to the material
manufactured from a regular-sourced procedure like injection molding.
This work therefore represents a step forward in order to turn FDM technology
processes into the mainstream production of components with higher mechanical properties
and making this process feasible for creating structural-applicable parts and not just for
aesthetics or prototyping.
Author Contributions: Conceptualization, P.F. and E.C.; methodology, G.M.S., P.F.; validation, G.D.,
P.F., C.L.-C. and L.F.; formal analysis, P.F., C.L.-C.; investigation, P.F., C.L.-C., M.S.; resources, C.L.-C.,
M.S.; data curation, P.F.; writing—original draft preparation, P.F., C.L.-C.; writing—review and
editing, P.F., C.L.-C.; visualization, P.F.; supervision, L.F.; project administration, A.L. All authors
have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data presented in this study are available on request from the
corresponding author.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Guessasma, S.; Belhabib, S.; Nouri, H. Effect of printing temperature on microstructure, thermal behavior and tensile properties
of 3D printed nylon using fused deposition modeling. J. Appl. Polym. Sci. 2021, 138, 50162. [CrossRef]
2.
Shahrubudin, N.; Lee, T.C.; Ramlan, R. An Overview on 3D Printing Technology: Technological, Materials, and Applications.
Procedia Manuf. 2019, 35, 1286–1296. [CrossRef]
3.
Savu, I.D.; Savu, S.V.; Simion, D.; Sîrbu, N.-A.; Ciornei, M.; Ratiu, S.A. PP in 3D Printing–Technical and Economic Aspects. Mater.
Plast. 2019, 56, 931. [CrossRef]
4.
Mahamood, R.; Akinlabi, S.; Shatalov, M.; Murashkin, E.; Akinlabi, E. Additive Manufacturing / 3D Printing Technology: A
Review. Ann. Dunarea Jos Univ. Galati. Fascicle XII Weld. Equip. Technol. 2019, 30. [CrossRef]
5.
Brian, N.T.; Robert, S.; Scott, A.G. A review of melt extrusion additive manufacturing processes: I. Process design and modeling.
Rapid Prototyp. J. 2014, 20, 192–204. [CrossRef]
6.
Tofail, S.A.M.; Koumoulos, E.P.; Bandyopadhyay, A.; Bose, S.; O’Donoghue, L.; Charitidis, C. Additive manufacturing: Scientiﬁc
and technological challenges, market uptake and opportunities. Mater. Today 2018, 21, 22–37. [CrossRef]
7.
Ait-Mansour, I.; Kretzschmar, N.; Chekurov, S.; Salmi, M.; Rech, J. Design-dependent shrinkage compensation modeling and
mechanical property targeting of metal FFF. Prog. Addit. Manuf. 2020, 5, 51–57. [CrossRef]
8.
Linares-Alvelais, J.A.R.; Figueroa-Cavazos, J.O.; Chuck-Hernandez, C.; Siller, H.R.; Rodríguez, C.A.; Martínez-López, J.I.
Hydrostatic high-pressure post-processing of specimens fabricated by DLP, SLA, and FDM: An alternative for the sterilization of
polymer-based biomedical devices. Materials 2018, 11, 2540. [CrossRef]
9.
Frascio, M.; de Marques, E.A.S.; Carbas, R.J.C.; da Silva, L.F.M.; Monti, M.; Avalle, M. Review of Tailoring Methods for Joints with
Additively Manufactured Adherends and Adhesives. Materials 2020, 13, 3949. [CrossRef] [PubMed]


---


## Page 15


Polymers 2021, 13, 2190
15 of 15
10.
Hofstätter, T.; Pedersen, D.B.; Tosello, G.; Hansen, H.N. State-of-the-art of ﬁber-reinforced polymers in additive manufacturing
technologies. J. Reinf. Plast. Compos. 2017, 36, 1061–1073. [CrossRef]
11.
Ali, Z.; Türeyen, E.B.; Karpat, Y.; Çakmakcı, M. Fabrication of polymer micro needles for transdermal drug delivery system using
DLP based projection stereo-lithography. Procedia CIRP 2016, 42, 87–90. [CrossRef]
12.
Zarringhalam, H.; Hopkinson, N.; Kamperman, N.F.; de Vlieger, J.J. Effects of processing on microstructure and properties of SLS
Nylon 12. Mater. Sci. Eng. A 2006, 435–436, 172–180. [CrossRef]
13.
Schmid, M.; Amado, A.; Wegener, K. Polymer powders for selective laser sintering (SLS). In Proceedings of the AIP Conference
proceedings, Cleveland, OH, USA, 6–12 June 2014; AIP Publishing LLC: Melville, NY, USA, 2015; Volume 1664, p. 160009.
14.
Gordeev, E.G.; Galushko, A.S.; Ananikov, V.P. Improvement of quality of 3D printed objects by elimination of microscopic
structural defects in fused deposition modeling. PLoS ONE 2018, 13, e0198370. [CrossRef]
15.
Damon, J.; Dietrich, S.; Gorantla, S.; Popp, U.; Okolo, B.; Schulze, V. Process porosity and mechanical performance of fused
ﬁlament fabricated 316L stainless steel. Rapid Prototyp. J. 2019, 25, 1319–1327. [CrossRef]
16.
Percoco, G.; Arleo, L.; Stano, G.; Bottiglione, F. Analytical model to predict the extrusion force as a function of the layer height, in
extrusion based 3D printing. Addit. Manuf. 2021, 38, 101791. [CrossRef]
17.
Dawoud, M.; Taha, I.; Ebeid, S.J. Mechanical behaviour of ABS: An experimental study using FDM and injection moulding
techniques. J. Manuf. Process. 2016, 21, 39–45. [CrossRef]
18.
Fayazbakhsh, K.; Movahedi, M.; Kalman, J. The impact of defects on tensile properties of 3D printed parts manufactured by
fused ﬁlament fabrication. Mater. Today Commun. 2019, 18, 140–148. [CrossRef]
19.
Sood, A.K.; Ohdar, R.K.; Mahapatra, S.S. Parametric appraisal of mechanical property of fused deposition modelling processed
parts. Mater. Des. 2010, 31, 287–295. [CrossRef]
20.
Pawar, S.; Dolas, D. Experimental Investigation and Empirical Modeling of FDM Process for Tensile Strength Improvement. Lect.
Notes Mech. Eng. 2020, 3, 371–378. [CrossRef]
21.
Vega, V.; Clements, J.; Lam, T.; Abad, A.; Fritz, B.; Ula, N.; Es-Said, O.S. The effect of layer orientation on the mechanical properties
and microstructure of a polymer. J. Mater. Eng. Perform. 2011, 20, 978–988. [CrossRef]
22.
Ahn, S.H.; Montero, M.; Odell, D.; Roundy, S.; Wright, P.K. Anisotropic material properties of fused deposition modeling ABS.
Rapid Prototyp. J. 2002, 8, 248–257. [CrossRef]
23.
Liu, J.L.; Nie, Z.X.; Jiang, W.G. Deformation ﬁeld of the soft substrate induced by capillary force. Phys. B Condens. Matter 2009,
404, 1195–1199. [CrossRef]
24.
Liu, J.-L.; Feng, X.-Q.; Wang, G.; Yu, S.-W. Mechanisms of superhydrophobicity on hydrophilic substrates. J. Phys. Condens. Matter
2007, 19, 356002. [CrossRef]
25.
Pan, A.Q.; Huang, Z.F.; Guo, R.J.; Liu, J. Effect of FDM Process on Adhesive Strength of Polylactic Acid(PLA) Filament. Key Eng.
Mater. 2016, 667, 181–186. [CrossRef]
26.
Hodgson; Ranellucci; Moe Flow Math: Understanding Extrusion Width. Available online: https://manual.slic3r.org/advanced/
ﬂow-math (accessed on 30 June 2021).
27.
Prusa Research, a.s. Layers and Perimeters. Available online: https://help.prusa3d.com/en/article/layers-and-perimeters_1748
(accessed on 30 June 2021).


---
