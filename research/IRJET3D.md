# IRJET3D

> **Source:** `IRJET3D.pdf`
> **Converted:** 2025-11-22 21:18:07
> **Method:** PyMuPDF

---

## Page 1


See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/332345142
Process Parameter Optimization for FDM 3D Printer
Article · April 2019
CITATIONS
17
READS
4,173
6 authors, including:
Mahesh Kadam
Burckhardt Compression
17 PUBLICATIONS   57 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Mahesh Kadam on 11 April 2019.
The user has requested enhancement of the downloaded file.


---


## Page 2


International Research Journal of Engineering and Technology (IRJET)       e-ISSN: 2395-0056
                Volume: 06 Issue: 04 | Apr 2019                   www.irjet.net                                                                    p-ISSN: 2395-0072

© 2019, IRJET       |       Impact Factor value: 7.211       |       ISO 9001:2008 Certified Journal       |     Page 1

Process Parameter Optimization for FDM 3D Printer
Yash Magdum1, Divyansh Pandey2, Akash Bankar3, Shantanu Harshe4, Vasudev Parab5,
Mr. Mahesh Shivaji Kadam6
1,2,3,4,5Student, Department of Mechanical Engineering, SGI, Atigre, Kolhapur, India
6Assistant Professor, Department of Mechanical Engineering, SGI, Atigre, Kolhapur, India

---------------------------------------------------------------------***---------------------------------------------------------------------
Abstract - Fused 3D printing technology is an additive
manufacturing method used for manufacturing of solid
Three Dimensional parts. It requires less human efforts
and manufacturing time for parts is less. Different
parameters such as Layer Thickness, Shell Thickness and
Fill Density affect the mechanical properties such as
Surface Roughness, Hardness and Tensile Strength of 3D
Printed Parts. On this basis, this paper focuses on
“Optimization of Process Parameters for 3D Printing
Operation on FDM 3D Printer”. On the basis of
optimized parameters the manufacturing time and
mechanical properties will be enhanced. It provides
proper methodology for optimized 3D Printing.
Experimental results are comparable to those for different
variations in parameters.

Key Words:  3D printing, design of experimens, material
selection, taguchi DOE.

I. INTRODUCTION

The 3D printing or additive manufacturing is
a process of making three dimensional solid objects
from a digital file. 3D printing is used in both rapid
prototyping and additive manufacturing. Objects can be
of almost any shape or geometry and typically are
produced using electronic data source such as
an Additive Manufacturing File (AMF) file. Fused
deposition modelling was developed by S. Scott Crump,
co-founder of Stratasys, in 1988. It is an additive
manufacturing process and is one of the most common
techniques used for 3D printing. It is also known as
solid-based Additive Manufacturing (AM) technology.
In fused deposition modelling, a plastic material
filament is fed through a heated moving head that melts
and extrudes it depositing it, layer after layer, in the
desired shape. A moving platform lowers after each
layer is deposited. Unlike material removed from a
stock in the conventional machining process, 3D
printing or Additive Manufacturing builds a three-
dimensional object from a computer-aided design
(CAD) model or AMF file, usually by successively adding
material layer by layer. The term "3D printing"
originally referred to a process that deposits a binder
material onto a powder bed with inkjet printer heads
layer by layer. For this kind of 3D printing technology
additional vertical support structures are needed to
sustain overhanging parts.
II. METHODOLOGY
 A. Materials and Methods
Raw material which is used in the study is Polylactic
Acid Resins (PLA) of size 1.75mm diameter, which is
one of the common filaments used for 3D Printing. PLA
is one of the thermoplastics used commonly in FDM 3D
Printers which has several characteristics like, it has
low melting point so it requires less temperature from
200O c-300O c to print as well as it is less toxic compare
with other thermoplastics.
The 3D printing machine (I3D Minds, INDIA) is
equipped with number of useful features, such as
automated setup and automated manufacturing, like
giving program in form of codes and getting 3D part
printed. It has maximum built volume of 190x190x180
mm and nozzle diameter is 0.4 mm. The samples were
designed by using ‘Solid works-2017’ and the slicing
program used for preparing samples is ‘CURA ‘.
B. Specimen preparation
The PLA filament was loaded into a 3D Printing
machine. The samples were prepared based on the
various combinations as shown in Table no 1. First of all
the sample with ASTM Standards were prepared in
SolidWorks-2017 CAD software and saved in to STL file
format. Then the file was opened in CURA software for
varying different process parameters like different
layer height (0.1 mm, 02mm & 0.3 mm), fill densities
(50% ,75% and 100%), Shell  thickness (0.6mm ,0.8mm
and 1.0mm),  at constant printing speeds. It provides a
detail combination of 3 different specimens for the


---


## Page 3


International Research Journal of Engineering and Technology (IRJET)       e-ISSN: 2395-0056
                Volume: 06 Issue: 04 | Apr 2019                   www.irjet.net                                                                    p-ISSN: 2395-0072

© 2019, IRJET       |       Impact Factor value: 7.211       |       ISO 9001:2008 Certified Journal       |     Page 2

process parameters. In CURA software the sample file
was converted into standard G code file format which is
compatible with all FDM machines. After preparation of
G Code file, it was provided to FDM machine and G code
file is run. For all experiments, the nozzle diameter 0.4
mm was used for preparation of specimens. The nozzle
was maintained a temperature of 215 ºC for the
extrusion of the PLA material and the build plate was
maintained at 60 ºC. The printer prints the layer
through the nozzle print head onto bed, one layer by
layer, from bottom to top, and the same test setup was
used for all specimens. After the printing is completed,
the printed part is kept for some time to let it cool the
printed part and FDM Machine. After printing, the
printed specimens are usually post hardened or
infiltrated for maximum strength. In this research, it
was observed that depending on variation in printing
parameters changes the time of printing operation. The
post hardening was observed to investigate the
unconditional effect of printing parameters on physical
and mechanical properties of the printed specimens.

Table -1: Specimen printing parameter variations.

Specimen Density Layer
Height
Shell
Thickness
1
50
0.1
0.6
2
50
0.2
0.8
3
50
0.3
1.0
4
75
0.1
1.0
5
75
0.2
0.8
6
75
0.3
0.6
7
100
0.1
0.8
8
100
0.2
1.0
9
100
0.3
0.6

III. Discussion:
A. Different process parameters of specimens:

Layer height (mm):
As this additive manufacturing method uses layer by
layer printing, the Layer Height Parameter plays an
important role in variation in mechanical as well as
physical properties. Layer Height varies from 0.06 to
0.4mm for 0.4mm diameter nozzle.


Shell thickness (mm):
The shell thickness is the thickness of outer shell of the
part. This is used in combination with the fill density
which is selected for printing to increase the
mechanical as well as physical properties.

Infill density (%):
It is the density of the part which is to be printed. For a
solid part use 100% and for an empty part use 0% fill
ensity. A value around 20 is usually enough. This won’t
affect the outside of the print and adjusts how strong
the part becomes.

Printing speed (mm/s):
Printing speed is the speed at which printing happens
by the movement of printing head. A well-adjusted
printer can reach 150mm/s, but for good quality prints
it need to print slower. Printing speed depends on lot
of B. Self-supporting-based strategy
IV. Manufacturing Process
A.
Modeling


Fig. 1 Cad modeling
3D printable models may be created with a computer-
aided design (CAD) package, via a 3D scanner, or by a
plain digital camera and photogrammetry software. 3D
printed models created with CAD result in reduced
errors and can be corrected before printing, allowing
verification in the design of the object before it is
printed. The manual modelling process of preparing
geometric data for 3D computer graphics is similar to
plastic arts such as sculpting. 3D scanning is a process
of collecting digital data on the shape and appearance
of a real object, creating a digital model based on it.


---


## Page 4


International Research Journal of Engineering and Technology (IRJET)       e-ISSN: 2395-0056
                Volume: 06 Issue: 04 | Apr 2019                   www.irjet.net                                                                    p-ISSN: 2395-0072

© 2019, IRJET       |       Impact Factor value: 7.211       |       ISO 9001:2008 Certified Journal       |     Page 3

B. Printing

Fig -2: Specimens Manufacturing
Before printing a 3D model from an STL file, it must
first be examined for errors. Most CAD applications
produce errors in output STL files, of the following
types:
1. Holes;
2. Faces normal;
3. Self-intersections;
4. Noise shells;
5. Manifold errors.
A step in the STL generation known as "repair" fixes
such problems in the original model. Generally STLs
that have been produced from a model obtained
through 3D scanning often have more of these errors.
This is due to how 3D scanning works-as it is often by
point to point acquisition, reconstruction will include
errors in most cases.
C. Finishing

Fig-3: Finishing of specimen
Though the printer-produced resolution is sufficient for
many applications, printing a slightly oversized version
of the desired object in standard resolution and then
removing material with a higher-resolution subtractive
process can achieve greater precision.




V. Design of Experiments.
A. Taguchi DOE:
Taguchi design, or an orthogonal array, is a method of
designing experiments that usually requires only a
fraction of the full factorial combinations. An orthogonal
array means the design is balanced so that factor levels
are weighted equally. Because of this, each factor can be
evaluated independently of all the other factors, so the
effect of one factor does not influence the estimation of
another factor. Dr.Genichi Taguchi is regarded as the
foremost proponent of robust parameter design, which
is an engineering method for product or process design
that focuses on minimizing variation and/or sensitivity
to noise.
B. Taguchi Method

In the optimization of 3D printer there are
THREE Parameters (Factors) THREE Levels.

For Full Factorial method the number of
experiments is 27.

For Taguchi Method for THREE factors THREE
levels.

For maximization of Tensile Strength.

For maximization of Strength (Hardness).

For Larger -the-Better
     S/FL=-10log10 [⅀ (1/y2)/n]

For minimization of Surface Roughness

For Smaller-the-Better
      S/FS=-10log10 [(⅀y2)/n]

Table -2: No. of parameters and levels.
Factors
Levels
1
2
3
Fill Density
50
75
100
Layer Thickness
0.1
0.2
0.3
Shell Thickness
0.6
0.8
1.0


---


## Page 5


International Research Journal of Engineering and Technology (IRJET)       e-ISSN: 2395-0056
                Volume: 06 Issue: 04 | Apr 2019                   www.irjet.net                                                                    p-ISSN: 2395-0072

© 2019, IRJET       |       Impact Factor value: 7.211       |       ISO 9001:2008 Certified Journal       |     Page 4



Table -3: Experiment no. and Control Factors.
Experiment
No.
Control Factors
A
B
C
1
1
1
1
2
1
2
2
3
1
3
3
4
2
1
3
5
2
2
1
6
2
3
2
7
3
1
2
8
3
2
3
9
3
3
1

VI. Testing Techniques
A. Tensile Test

Fig-4: Universal Testing Machine
A universal testing machine (UTM), also known as
a universal
tester, materials
testing
machine or materials test frame, is used to test
the tensile
strength and compressive
strength of materials. An earlier name for a tensile
testing machine is a tensometer. The "universal" part of
the name reflects that it can perform many standard
tensile
and
compression
tests
on
materials,
components, and structures (in other words, that it is
versatile).
Components:
Several variations are in use. Common components
include:

Load frame - Usually consisting of two strong
supports for the machine. Some small machines
have a single support.

Load cell - A force transducer or other means of
measuring
the
load
is
required.
Periodic calibration is usually required by
governing regulations or quality system.

Cross head - A movable cross head (crosshead)
is controlled to move up or down. Usually this is
at a constant speed: sometimes called
a constant rate of extension (CRE) machine.
Some machines can program the crosshead
speed or conduct cyclical testing, testing at
constant force, testing at constant deformation,
etc. Electromechanical, servo-hydraulic, linear
drive, and resonance drive are used.
Means of measuring extension or deformation - Many
tests require a measure of the response of the
test specimen to
the
movement
of
the
cross
head. Extensometers are sometimes used.
Output device - A means of providing the test result is
needed. Some older machines have dial or digital
displays and chart recorders. Many newer machines
have a computer interface for analysis and printing.
Conditioning
-
Many tests
require
controlled
conditioning (temperature, humidity, pressure, etc.).
The machine can be in a controlled room or a
special environmental chamber can be placed around
the test specimen for the test.
Test fixtures, specimen holding jaws, and related
sample making equipment are called for in many test
methods.
B. Hardness Test

Fig-5: Shore-A Durometer.
The Shore Durometer is a device for measuring
the hardness of
a
material,
typically
of polymers, elastomers, and rubbers
Higher numbers on the scale indicate a greater
resistance to indentation and thus harder materials.
Lower numbers indicate less resistance and softer
materials.


---


## Page 6


International Research Journal of Engineering and Technology (IRJET)       e-ISSN: 2395-0056
                Volume: 06 Issue: 04 | Apr 2019                   www.irjet.net                                                                    p-ISSN: 2395-0072

© 2019, IRJET       |       Impact Factor value: 7.211       |       ISO 9001:2008 Certified Journal       |     Page 5

The term is also used to describe a material's rating on
the scale, as in an object having a “‘Shore Durometer’ of
90.”
The scale was defined by Albert Ferdinand Shore, who
developed a suitable device to measure hardness in the
1920s. It was neither the first hardness tester nor the
first to be called a Durometer (ISV duro- and -meter;
attested since the 19th century), but today that name
usually refers to Shore hardness; other devices use
other measures, which return corresponding results,
such as for Rockwell hardness.
4.2.1 Mititoyo SJ-210


Fig-6: Surface Roughness Test
FEATURES
• The 2.4-inch colour graphic LCD provides excellent
readability and an intuitive display that is easy to use.
The LCD also includes a backlight for improved
visibility in dark environments.
• The Mititoyo SJ-210 can be easily operated using the
buttons on the front of the unit and under the sliding
cover.
• Up to 10 measurement conditions and one measured
profile can be stored in the internal memory.
• An optional memory card can be used as an extended
memory to store large quantities of measured profiles
and conditions. Access to each feature can be password
protected which prevents unintended operations and
allows you to protect your settings.
• The display interface supports 16 languages, which
can be freely switched.
• An alarm warns you when the cumulative
measurement distance exceeds a preset limit.
• The Mititoyo SJ-210 complies with the following
standards: JIS (JIS-B0601-2001,
JIS-B0601-1994, JIS B0601-1982), VDA, ISO-1997 and
ANSI.
• In addition to calculation results, the Mititoyo SJ-210
can display sectional calculation results and assessed
profiles, load curves, and amplitude distribution curves.

VII. CONCLUSIONS
On the basis of varying different parameters in different level
a Design of Experiments are carried out which can be used
for preparation of specimens for optimization of 3D printed
products for different parameters of 3D printing. Testing
machines are selected for testing mechanical properties such
as Tensile strength, Hardness and Surface Roughness of 3D
printed specimens.

REFERENCES

[1] Elizabeth Matias, Bharat Rao, 3D Printing: On Its
Historical Evolution and the Implications for Business,
PICMET '15: Management of the Technology Age ,(2015)
(Pg.551-558)
[2] Dina R. Howeidy ,  The Impact of Using 3D Printing on
Model Making Quality and Cost in the Architectural
Design Projects,  International Journal of Applied
Engineering Research ISSN 0973-4562 Volume 12,
(2017) (pg.987-994).
[3] Mamta Junejaa, Niharika Thakura, Dinesh Kumara,
Ankur Guptab, Babandeep Bajwac, Accuracy in dental
surgical guide fabrication using different 3-D printing
techniques, Additive Manufacturing, (2018), (Pg.243-
255).
[4] Barry Berman, 3-D printing: The new industrial
revolution, Kelley School of Business, Indiana University.
All rights reserved, (2011) (Pg.155-162).
[5] Wei Dai Vian, PhD and Nancy L. Denton, Hardness
Comparison of Polymer Specimens Produced with
Different Processes , PE School of Engineering
Technology Purdue University Kokomo and West
Lafayette, Indiana, (2015) (Pg.1312-1314).
[6] Wenyong Liu, Ying Li, Jinyu Liu, Xufeng Niu, Yu Wang
and Deyu Li, Application and Performance of 3D Printing
in Nanobiomaterials, Key Laboratory for Biomechanic
sand Mechanobiology of Ministry of Education, School of
Biological
Science
and
Medical
Engineering,
BeihangUniversity,Beijing100191,China, (2014)(Pg.1-7)
[7] Nathaniel Hudson1, Celena Alcock2, Parmit K. Chilana1,
Understanding Newcomers to 3D Printing:  Motivations,
Workflows,
and
Barriers
of
Casual
Makers
,
1Management
Sciences
University
of
Waterloo
Waterloo, ON Canada {ndphudso, pchilana} 2Drama and
Speech
Communication
University
of
Waterloo
Waterloo, ON Canada(2016)(Pg. 384-396)
[8] Yingying Xuea, Xinfu Wanga, Wen Wanga, Xiaokang
Zhonga, Fusheng Hana,Compressive property of Al-
based auxetic lattice structures fabricated by 3D
printing combined with investment casting, aKey


---


## Page 7


International Research Journal of Engineering and Technology (IRJET)       e-ISSN: 2395-0056
                Volume: 06 Issue: 04 | Apr 2019                   www.irjet.net                                                                    p-ISSN: 2395-0072

© 2019, IRJET       |       Impact Factor value: 7.211       |       ISO 9001:2008 Certified Journal       |     Page 6

Laboratory of Materials Physics, Institute of Solid State
Physics, Chinese Academy of Sciences, Hefei, Anhui
230031, China bUniversity of Science and Technology of
China, Hefei, Anhui 230026, China(2018)(255-262)
[9] Chelsea
Schelly,
GeraldAnzalone,
BasWijnen,
JoshuaM.Pearce , Open-source 3-D printing technologies
for education: Bringing additive manufacturing to the
classroom,(2015)(Pg. 1-12)
[10] Nadim S. Hmeidat, James W. Kemp, Brett G. Compton,
High-strength epoxy nanocomposites for 3D printing,
Mechanical, Aerospace, and Biomedical Engineering
Department
University
of
Tennessee,
Knoxville
Knoxville, TN 37996 USA, (2018)(1-36)
[11] Wei Dai Vian, PhD and Nancy L. Denton, Hardness
Comparison of Polymer Specimens Produced with
Different Processes, School of Engineering Technology
Purdue University Kokomo and West Lafayette, Indiana,
(2018)
[12] Daniel Farbman, Material Testing of 3D Printed ABS and
PLA Samples To Guide Mechanical Design, University of
California, Berkeley Berkeley, California, United States of
America, (2017)(1-12)
BIOGRAPHIES


Y D. Magdum, pursuing B.E degree
in Mechanical Engineering from
Shivaji University, Kolhapur, India,
in 2018.

D L. Pandey, pursuing B.E degree
in Mechanical Engineering from
Shivaji University, Kolhapur, India,
in 2018.

A S. Bankar, pursuing B.E degree in
Mechanical
Engineering
from
Shivaji University, Kolhapur, India,
in 2018.


S S. Harshe, pursuing B.E degree in
Mechanical
Engineering
from
Shivaji University, Kolhapur, India,
in 2018.




V A. Parab, pursuing B.E degree in
Mechanical
Engineering
from
Shivaji University, Kolhapur, India,
in 2018.


M S. Kadam, received M.E Degree
in Mechanical engineering from
KIT
College
of
Engineering,
Kolhapur, India 2014 and He is
currently pursuing the Ph.d Degree
in mechanical engineering at
Shivaji University From 2016, he is
assistant professor at Sanjay
Ghodawat College of engineering.
And his research area is Nano
Composite and other research
interest is Finite Element Analysis.





View publication stats


---
