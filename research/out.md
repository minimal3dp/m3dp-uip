# out

> **Source:** `out.pdf`
> **Converted:** 2025-11-22 21:18:07
> **Method:** PyMuPDF

---

## Page 1


UNIVERSITY OF OKLAHOMA GRADUATE COLLEGE



MATERIAL CHARACTERIZATION OF 3D-PRINTED SPECIMENS BASED ON
PRINTING ORIENTATION

A THESIS
SUBMITTED TO THE GRADUATE FACULTY
in partial fulfillment of the requirements for the
Degree of
MASTER OF SCIENCE





By Wyatt J Main
Norman, Oklahoma
2025


---


## Page 2


MATERIAL CHARACTERIZATION OF 3D-PRINTED SPECIMENS BASED ON
PRINTING ORIENTATION

A THESIS APPROVED FOR THE SCHOOL OF AEROSPACE AND MECHANICAL
ENGINEERING



BY THE COMMITTEE CONSISTING OF





Dr. J. David Baldwin, Chair



Dr. Ramkumar Parthasarathy



Dr. Mrinal Saha


---


## Page 3


©Copyright by Wyatt J Main 2025
All Rights Reserved.


---


## Page 4


iv

Acknowledgements
I would like to thank Dr. J. David Baldwin for serving as my advisor and the head of my
committee, as well as his constant and unending support throughout this process. He has
made himself and his time available to me so often throughout this process. He was
forthcoming with advice on many different topics and was ready to reach out to others
whenever we got to anything he was unsure of. I also appreciate his efforts to promote me
and suggest methods of advancing my academic and professional development.
I would like to express my appreciation to Dr. Ramkumar Parthasarathy for being willing
to serve on my thesis committee. I would also like to thank him for his continuous
support of me through my academic life here at the university.
I would also like to thank Dr. Mrinal Saha for serving on my committee so willingly. I
also want to thank him for lending me access to his lab and instruments, without which
many parts of this research would not have happened. I also want to thank him for putting
me in touch with Anirban Mondal.
I would like to thank Anirban Mondal who made himself available to me and mentored
me on the molding, polishing, and microscopy processes used in this research. Without
him those steps might not have been possible in the timeframe I had available, as he put
in the effort to make sure I understood the processes in a condensed timeframe.
I would like to thank Dr. Liu for his assistance throughout my time at OU, providing
access to his labs and 3D-printers, as well as introducing me to Peter Vu.
I would like to thank Peter Vu as he helped me get familiar with the Bambu 3D-printer
and the software needed to run it.
I would also like to thank Christian Dix as he helped with the development of the Stress-
Strain curves.
I would like to thank my friends and family who have supported me throughout this
program and in my general life despite the rough patches.
I would like to thank my parents especially as they have continuously supported me in so
many of the things I have done in life and have always had my back.
Finally, I would like to thank the University of Oklahoma for providing me with this
opportunity.


---


## Page 5


v


Table of Contents
Page #
Acknowledgements ............................................................................................................ iv
List of Figures ................................................................................................................... vii
List of Tables .................................................................................................................... viii
Abstract .............................................................................................................................. ix
Chapter 1: Introduction and Background information ........................................................ 1
1.1 Introduction ............................................................................................................... 1
1.2 Background ............................................................................................................... 3
1.3 Research Plan ............................................................................................................ 4
1.3.1 Specimen Fabrication ......................................................................................... 5
1.3.2 Tensile Testing ................................................................................................... 5
1.3.3 Specimen Preparation for Microscopy ............................................................... 5
1.3.4 Microscopy ......................................................................................................... 6
Chapter 2: Specimen Fabrication ........................................................................................ 7
2.1 Specimen Prep ........................................................................................................... 7
2.2 Results ..................................................................................................................... 10
Chapter 3: Tensile Testing ................................................................................................. 13
3.1 Experimental Process and Equipment ..................................................................... 13
3.2 Data Analysis........................................................................................................... 18
3.3 Discussion of Results .............................................................................................. 23
Chapter 4: Specimen Prep for Microscopy ....................................................................... 32
4.1 Molding ................................................................................................................... 32
4.2 Results ..................................................................................................................... 39
Chapter 5: Microscopy ...................................................................................................... 41
5.1 Imaging Procedure .................................................................................................. 41
5.2 Discussion of Results .............................................................................................. 41
Chapter 6. Concluding remarks ........................................................................................ 45
6.1 Interpretations.......................................................................................................... 45
6.2 Plans for the future .................................................................................................. 47
Appendix ........................................................................................................................... 50


---


## Page 6


vi

Appendix 1: Creating an Instron Test Method .............................................................. 50
Appendix 2: Force-Displacement and Strain-Displacement Results ............................ 53
Appendix 3: Stress-Strain Curves ................................................................................. 63
Appendix 4: Estimates of Young’s Modulus ................................................................. 72


---


## Page 7


vii

List of Figures
Figure 1: Dogbone Specimen Dimensions (mm and degrees)............................................ 7
Figure 2: Gage-length Specimen Dimensions (mm and degrees) ...................................... 8
Figure 3: 3D-Printer in use ................................................................................................. 9
Figure 4: Freshly Printed Series of Specimens ................................................................. 12
Figure 5: A mounted specimen ......................................................................................... 16
Figure 6: Extensometer attached to a mounted specimen ................................................. 17
Figure 7:Force and Strain vs. Displacement plot for the A-0 Specimen .......................... 19
Figure 8: Stress - Strain Response of the A-0 Specimen .................................................. 20
Figure 9: Initial portion of the stress vs. strain plot for A-0 ............................................. 21
Figure 10: Visual representation of tensile strength and strain at fracture........................ 23
Figure 11: Tensile Series A Stress-Strain Comparison ..................................................... 24
Figure 12: Tensile Series B Stress-Strain Comparison ..................................................... 24
Figure 13: Tensile Series C Stress-Strain Comparison ..................................................... 25
Figure 14: Tensile Series D Stress-Strain Comparison ..................................................... 25
Figure 15: Tensile Series E Stress-Strain Comparison ..................................................... 26
Figure 16: Tensile Series F Stress-Strain Comparison...................................................... 26
Figure 17: 0-Degree Specimens of Each Tensile Series ................................................... 28
Figure 18: 45- Degree Specimens of Each Tensile Series ................................................ 29
Figure 19: 90- Degree Specimens of Each Tensile Series ................................................ 29
Figure 20: A collection of the tensile data for every specimen ......................................... 30
Figure 21: Orientation of specimens in mold ................................................................... 34
Figure 22: Struers Polisher................................................................................................ 35
Figure 23: The Six Molds in the Order A, B, C, D, E, and F ............................................ 40
Figure 24: Specimen C-0 at 200x magnification .............................................................. 42
Figure 25: Specimen B-45 at 200x magnification ............................................................ 43
Figure 26: Specimen D-90 at 200x magnification ............................................................ 43
Figure 27: Force & Strain vs. Displacement for A-45 ...................................................... 53
Figure 28: Force & Strain vs. Displacement for A-90 ...................................................... 53
Figure 29: Force & Strain vs. Displacement for B-0 ........................................................ 54
Figure 30: Force & Strain vs. Displacement for B-45 ...................................................... 54
Figure 31: Force & Strain vs. Displacement for B-90 ...................................................... 55
Figure 32: Force & Strain vs. Displacement for C-0 ........................................................ 55
Figure 33: Force & Strain vs. Displacement for C-45 ...................................................... 56
Figure 34: Force & Strain vs. Displacement for C-90 ...................................................... 57
Figure 35: Force & Strain vs. Displacement for D-0 ........................................................ 58
Figure 36: Force & Strain vs. Displacement for D-45 ...................................................... 58
Figure 37: Force & Strain vs. Displacement for D-90 ...................................................... 59
Figure 38: Force & Strain vs. Displacement for E-0 ........................................................ 59
Figure 39: Force & Strain vs. Displacement for E-45 ...................................................... 60
Figure 40: Force & Strain vs. Displacement for E-90 ...................................................... 60
Figure 41: Force & Strain vs. Displacement for F-0 ........................................................ 61


---


## Page 8


viii

Figure 42: Force & Strain vs. Displacement for F-45 ...................................................... 61
Figure 43: Force & Strain vs. Displacement for F-90 ...................................................... 62
Figure 44: Stress vs. Strain for A-45 ................................................................................. 63
Figure 45: Stress vs. Strain for A-90 ................................................................................. 63
Figure 46: Stress vs. Strain for B-0 ................................................................................... 64
Figure 47: Stress vs. Strain for B-45 ................................................................................. 64
Figure 48: Stress vs. Strain for B-90 ................................................................................. 65
Figure 49: Stress vs. Strain for C-0 ................................................................................... 65
Figure 50: Stress vs. Strain for C-45 ................................................................................. 66
Figure 51: Stress vs. Strain for C-90 ................................................................................. 66
Figure 52: Stress vs. Strain for D-0 .................................................................................. 67
Figure 53: Stress vs. Strain for D-45 ................................................................................ 67
Figure 54: Stress vs. Strain for D-90 ................................................................................ 68
Figure 55: Stress vs. Strain for E-0 ................................................................................... 68
Figure 56: Stress vs. Strain for E-45 ................................................................................. 69
Figure 57: Stress vs. Strain for E-90 ................................................................................. 69
Figure 58: Stress vs. Strain for F-0 ................................................................................... 70
Figure 59: Stress vs. Strain for F-45 ................................................................................. 70
Figure 60: Stress vs. Strain for F-90 ................................................................................. 71
Figure 61: Initial portion of the stress vs. strain plot for A-45 ......................................... 72
Figure 62: Initial portion of the stress vs. strain plot for A-90 ......................................... 72
Figure 63: Initial portion of the stress vs. strain plot for B-0 ........................................... 73
Figure 64: Initial portion of the stress vs. strain plot for B-45 ......................................... 73
Figure 65: Initial portion of the stress vs. strain plot for B-90 ......................................... 74
Figure 66: Initial portion of the stress vs. strain plot for C-0 ........................................... 74
Figure 67: Initial portion of the stress vs. strain plot for C-45 ......................................... 75
Figure 68: Initial portion of the stress vs. strain plot for C-90 ......................................... 75
Figure 69: Initial portion of the stress vs. strain plot for D-0 ........................................... 76
Figure 70: Initial portion of the stress vs. strain plot for D-45 ......................................... 76
Figure 71: Initial portion of the stress vs. strain plot for D-90 ......................................... 77
Figure 72: Initial portion of the stress vs. strain plot for E-0 ............................................ 77
Figure 73: Initial portion of the stress vs. strain plot for E-45 .......................................... 78
Figure 74: Initial portion of the stress vs. strain plot for E-90 .......................................... 78
Figure 75: Initial portion of the stress vs. strain plot for F-0 ............................................ 79
Figure 76: Initial portion of the stress vs. strain plot for F-45 .......................................... 79
Figure 77: Initial portion of the stress vs. strain plot for F-90 .......................................... 80

List of Tables
Table 1: Specimen Dimensions ..........................................................................................11
Table 2: Material Characteristics derived from the tensile data of the specimens ............ 22


---


## Page 9


ix

Abstract

A PA12 nylon material blended and reinforced with chopped carbon fibers was
prepared as tensile test specimens. Experimentation was performed to investigate what
effects the angle (0o, 45o, or 90o) that the material is laid down in when printing has on the
mechanical properties of the printed specimens. It was determined that of the three angles
investigated, a 0-degree lay down angle to the longitudinal axis results in the stiffest
mechanical properties, but can withstand the least strain at fracture. The 90-degree pattern
results in the least stiff results, and can withstand more strain than the 0-degree specimen.
The 45-degree specimen showed intermediate stiffness and the largest strain at fracture.
Microscopy performed on the specimens revealed that the chopped fibers appeared to be
randomly organized throughout the specimens.


---


## Page 10


1


Chapter 1: Introduction and Background information
1.1 Introduction
Manufacturing is a cornerstone of our modern society. For the vast majority of
nonbiological products there is a manufacturing process, and this is especially true in
regards to metal products. A lump of raw metal is not what most people want, they want
the worked, shaped, and finished products. From a sheet of metal to the bearings of a
vehicle’s wheels, manufactured products are everywhere. For all of these products there is
a process that must be followed to take them from the base materials to a finished product,
and for most products of current times this process is subtractive. Subtractive
manufacturing means that when someone wants to manufacture a part, they start with a
large portion of the material a part is to be made out of, and then shape, cut, and work the
material into the final form, removing portions of the material throughout the process.
However, while subtractive manufacturing has been the dominant manufacturing process
until now, due to being essentially the only method, a new process is arising as additive
manufacturing is estimated to show considerable market growth with a compound annual
growth rate of 23.3% between 2023 and 2030 [1]. Additive manufacturing works as the
reverse of subtractive manufacturing in that it works by taking smaller portions of materials
and shaping them into the desired final form while merging them to each other throughout
the process. Advantages of additive manufacturing include, but are not limited to, ease of
production as products can often be fabricated by a single hands-off machine, lack of
required training as complete, simple products can be fabricated using this process with
little to no training, and ease of access as additive manufacturing has been growing and is


---


## Page 11


2

becoming progressively accessible to the general public. However, additive manufacturing
is not solely advantageous, there are also a number of challenges including, but not limited
to, a lack of resolution as the process is not yet well suited to detail work, and a high starting
cost as while the market for the process is growing, the cost for a personal machine can
still be considered more expensive than many can use on a luxury. Probably the most well-
known example of additive manufacturing is 3D-printing which has been around since as
early as the 1980’s [2]. Specifically, polymer 3D-printing is what most people think of
when they think of 3D-printing.
Polymer 3D-printing is the process of melting and extruding a melted polymer
material onto a bed in a predetermined pattern layer by layer to build a desired product. It
is this predetermined pattern part that this research will be focusing on. In this research,
the primary question being investigated is whether the angle that the material is laid down
in, or raster angle, has any considerable effect on the material characteristics of the final
product. The specific angles investigated in this research were 0o, 45o, and 90o. The reason
for investigating this is a matter of efficiency and safety. From the standpoint of efficiency,
this information should allow a producer to fabricate parts that meet safety requirements
while reducing the amount of material used. While from the standpoint of safety, this
information should allow a producer to fabricate parts that can better withstand stresses
and strains while using the same amount of material. In either case, the information that
one can improve their final product in one way or the other by a small change can lead to
useful effects.
As this research is focusing on whether or not there are any noticeable effects on
the material characteristics based on raster angle two null hypotheses were produced, one


---


## Page 12


3

connected to the tensile data and its results and the other connected to the microscopy
results. The first null hypothesis of this research is that there is no noticeable effect on the
tensile characteristics of the final products based on raster angle. This would be supported
by the Tensile results being indistinguishable between different raster angle specimens. The
second null hypothesis states that the raster angle has no noticeable effect on the orientation
of fibers in the internal structure of the final products. This would be supported if the
orientation of the internal fibers was quasi-random and indistinguishable between different
raster angles. However, as these are the null hypotheses, testing was required to determine
if the results support rejecting these hypotheses, or failing to reject the hypotheses.
1.2 Background

As was previously mentioned, the field of 3D-printing has been growing, and with
this growth there has been research into various aspects of the process. These range from
investigating the effects of infill patterns [3,4], the effects of fiber reinforcement [5-8], the
effects of the distance between the nozzle and bed of the printer [9], to the consistency of
material characteristics for printed specimens [10]. Each of these are just a drop in the
bucket of the research in this field that continues to grow, but they are evidence of the field
continuing to build upon itself.
As is required for the field to grow upon itself, there has been plenty of research
into the field, and as such it is not odd for similar research to exist. A particular article of
research was done that also looked into the effects of raster angle by Ning et al. [11].
However, in this paper the angles that the authors used were alternating by 90 degrees
between each layer. An example of this set up would be that if the bottom layer’s raster
angle was 0o the next layer would be at 90o. From this alternating raster angle, the authors


---


## Page 13


4

had two specimens based on raster angle. These specimens were a [0,90] specimen type
and a [-45,45] specimen. The [0,90] specimens had an initial layer with a raster angle of 0o
with the following layer having a 90o raster angle. The subsequent layers alternated
respectively between these two angles. The [-45,45] specimens followed the same format,
but had -45o replacing 0o and 45o replacing 90o.  Using this alternating raster angle setup,
the authors found that their results showed the [0,90] specimens had greater tensile strength
and Young’s modulus as well as other data points. On the other hand, they found the [-
45,45] specimens had greater toughness and ductility. In comparison, this research will not
be alternating the raster angle between layers. For each specimen investigated in this
research, the raster angle was the same throughout the whole specimen. Similarly, while
Ning, et al. used a 5 wt% chopped carbon fiber reinforced ABS thermoplastic material, this
research uses a 20 wt% chopped carbon fiber reinforced nylon material.
1.3 Research Plan
For this research, there were multiple sections to reach the final conclusions. These
sections include specimen fabrication, tensile testing, specimen prep for microscopy, and
microscopy. Each of these sections contain multiple steps within themselves, and each is
interdependent with at least one of the other sections. An example would be that specimen
fabrication is connected to tensile testing and specimen prep for microscopy as it is in this
section that the specimens that are acted on in those sections are fabricated. However, the
internal steps in the sections are primarily disconnected from the other sections. As such,
the steps will be described individually in the following sections 1.3.1-1.3.4.


---


## Page 14


5

1.3.1 Specimen Fabrication

In this section of the research, the specimens that were used throughout the rest of
the research were fabricated. To do this, the specimens were designed as parts in the
SOLIDWORKS software, sliced in the OrcaSlicer software, and Printed using a Bambu
3D-printer. Dogbone specimens were designed according to ASTM D638-22 standard
along with gage lengths that were meant to represent a non-fractured version of the central
bars of the dogbones for the microscopy section. Both were printed at the same time to
keep the gage lengths as similar to their respective dogbones as possible.
1.3.2 Tensile Testing

In this section of the research, the fabricated specimens were subjected to tensile
testing using an Instron instrument according to a Method that was produced specifically
for this research. Tensile testing was performed on each specimen until fracture was
achieved. The results of this tensile testing were analyzed using Window’s Excel software
to determine important material characteristics, e.g. Young’s modulus and tensile strength,
and plot the tensile testing data for comparison between specimens. It was from these
comparison plots that the bulk of conclusions were drawn in this research.
1.3.3 Specimen Preparation for Microscopy

In this section, the gage lengths that were fabricated with their corresponding
dogbones were bisected, molded, and polished. The bisected gage lengths were molded
using Allied Quickcure before being polished with a Struers polishing instrument to a state
that could have microscopy performed on it for clear observation of the internals of the
gage lengths. The polishing consisted of using a variety of sandpaper sheets and polishing
suspensions ranging from 800 grit sandpaper to 1 micrometer polishing suspension.


---


## Page 15


6

1.3.4 Microscopy

In this section of the research, the goal was to observe the state of the carbon fibers
in the specimens to determine if the orientation of the carbon fibers was mostly random or
if the fibers followed a noticeable pattern dependent on the raster angle of the specimen.
This was done in cooperation with the Samuel Roberts Noble Microscopy Lab located on
the University of Oklahoma campus. The Keyence microscope available to students at the
lab was used to obtain several images at varying magnifications of the gage lengths.


---


## Page 16


7

Chapter 2: Specimen Fabrication

This chapter is focused on describing how the specimens were designed,
fabricated, and how close the printed specimens were to the desired dimensions. The first
section of the chapter describes how the specimens were designed, what they were made
of, and how they were fabricated. The second section describes the dimensions of the
printed specimens.
2.1 Specimen Prep

For this research, the specimens were initially designed in SOLIDWORKS, and
took the form of dogbone testing specimens, as can be seen in the SOLIDWORKS drawing
in Figure 1 below. The dogbone specimens had their dimensions dictated by the
specifications of the type-1 specimen from ASTM D638-22.

Figure 1: Dogbone Specimen Dimensions (mm and degrees)
Along with the dogbone specimens, gage length specimens were also prepared.
These gage length specimens take the form of the central bar of the dogbone specimens
and measure as 13x5x50 mm rectangular blocks as can be seen in Figure 2 below.


---


## Page 17


8


Figure 2: Gage-length Specimen Dimensions (mm and degrees)
 These gage lengths were produced to be able to perform microscopy on the interior
of the specimens. This was required because performing the interior of the dogbones post
tensile testing would be irrevocably affected by any changes that occurred during the
tensile testing and subsequent fracture, likely skewing microscopy results. As such, an
additional specimen was printed at the same time for each of the dogbone specimens.
However, due to the size required for the molding process, and to save material, the ends
of the dogbones were removed, leading to the design in Figure 2.
The specimens of this research were made with a chopped carbon fiber reinforced
nylon material, specifically the NylonX Carbon Fiber PA12 Filament – 1.75mm (0.5kg)
material from matterhackers.com. This material is reported to have a nominal diameter of
1.75mm ± 0.02mm, density of 1.00g/cm3, melting point of 180oC, Young’s (tensile)
modulus of 6,000 MPa, and Ultimate (tensile) strength of 100 MPa.
The specimens were printed with a Bambu X-1 Carbon 3D-printer pictured in
Figure 3 below.


---


## Page 18


9


Figure 3: 3D-Printer in use
 Initial prints with this Bambu printer showed that consistency to the desired
dimensions was acceptable by being within 1 millimeter in regards to width and thickness
and 5 millimeters in regards to overall length of the ASTM standard’s dimensions. The
width and thickness were measured with a caliper. However, due to the overall length of
the specimens no available calipers were able to be used to measure the length. Due to this,
a ruler was used instead, despite the level of inaccuracy inherent to it. With the printed
specimens being produced within an acceptable level of error, the printing of specimens
proceeded.

The dogbones were built to the specifications of the standard in SOLIDWORKS
software that can be seen in Figures 1 and 2 above. Once the specimens were built in a
SOLIDWORKS file it was uploaded to the printer using the Orcaslicer v2.1.1 software.


---


## Page 19


10

Using Orcaslicer, specifications of how each print was to be performed were designated.
This functionality was what allowed the raster angle, or the angle that the material was laid
down at in reference to the specimen’s x-axis, to be specified. The angles that were
investigated in this research include 0o, 45o, and 90o from the specimen’s x-axis. These
angles were applied throughout the infill of the specimens. As an example, for a 0o
specimen every layer’s material was laid down line by line at 0o to the x-axis. Other than
the angles, there were a number of other specifications designated in Orcaslicer for the
prints such as having a 5mm wide trimmable brim for more consistent print success, 0.2
mm layer height which produced 25 layers, 0.42mm line width, one top shell layer, 100%
infill density, no infill rotation, and only two wall layers. Based off of these specifications,
six series of specimens were printed. These specimen series were designated as series A-F.
2.2 Results
This section is dedicated to going over the results of the printing of the six series of
specimens, A-F. Located below is Table 1 which lists the width and thickness of the central
bar in millimeters of each dogbone that was measured with a caliper, as well as the overall
length of the dogbone specimens in centimeters including the wider end sections as well
as the central bar. After that is a freshly printed series in Figure 4 to illustrate the state the
specimens were in directly out of the printer.


---


## Page 20


11

Table 1: Tensile Test Specimen Dimensions
Specimen
Series
Angle
(degrees)
Width (mm)
Thickness
(mm)
Overall Length (cm)

A
0
13.74
5.36
16.5
45
13.61
5.48
16.5
90
13.61
5.53
16.5

B
0
13.63
5.51
16.5
45
13.61
5.55
16.3
90
13.66
5.54
16.3

C
0
13.65
5.25
16.3
45
13.54
5.46
16.4
90
13.61
5.25
16.4

D
0
13.79
5.22
16.5
45
13.60
5.42
16.4
90
13.62
5.44
16.4

E
0
13.27
5.02
16.5
45
13.21
5.33
16.4
90
13.33
5.29
16.3

F

0
13.50
5.15
16.5
45
13.21
5.31
16.4
90
13.36
5.28
16.3


---


## Page 21


12



Figure 4: Freshly Printed Series of Specimens
Looking through Table 1 it can be seen that each specimen is within one
millimeter for width and thickness and five millimeters for overall length in comparison
to the designated standard dimensions. This was deemed acceptable for this research as
the material characterization can be done as long as there are accurately measured
dimensions for the width and thickness.


---


## Page 22


13

Chapter 3: Tensile Testing

This chapter describes the tensile testing that was performed on the specimens,
the data that were obtained from the tensile testing, and discusses what the data means for
this research.
3.1 Experimental Process and Equipment
With the production of acceptable specimens completed, the next step was
obtaining the tensile testing data that forms the backbone of this research. The data were
obtained with an Instron 34TM-50. The Instron was equipped with a 50 KN load cell,
wedge grips, and was run with Bluehill Universal v4.44 software. The tensile data obtained
were specifically force in Newtons, displacement in millimeters, and axial strain in percent.
The strain was obtained using an Instron 2630-102 Strain Gauge Extensometer.
Displacement was designated as the independent variable for obtaining the other data
points.
To obtain the data points for this research a new Method was created for the Instron
to follow and apply to all of the specimens. The Method is the set of instructions that the
Instron follows to acquire the tensile data, and includes the unit system, selected data types
for collection, data acquisition rate, preload, testing load, and number of specimens, among
other options. The manual for creating this Method as a new Method is included in the
Appendix of this research. The primary values of the Method include applying a preload
tensile displacement of 0.125 mm/s (0.005 in/s) until a load of 22.24 N (5 lbf) was applied
to the specimen at which point it began ramping the displacement at 0.25 mm/s (0.01 in/s)
and measured the required force and strain caused by the displacement. This continued


---


## Page 23


14

until the termination criterion of the current force measurement equaling 40% of the prior
measurement, a situation that should only occur at fracture.
After an original Method has been made according to the procedure in the Appendix,
the process for running subsequent tensile tests proceeds according to the following set of
instructions:
1. Be properly dressed per your lab’s requirements and have your Personal Protection
Equipment (PPE)
2. Turn on the Instron and the attached monitor
3. Create a new folder in the computers file system for the data to be collected
4. Start the Bluehill Universal software
5. Click on and enter the Test section of the Bluehill software
6. Select the original/previous test Method in the new sample section
7. Press OK on the Set Travel Limits page
8. Once the test method has initialized, switch to the Method section
9. Make any changes that are appropriate for your new test such as…
o Designating the new file to save results to in the exports section
o Altering the name of the saved results to differentiate the new test in the
exports section
o Designating a new number of samples in the workflow section
o Others as appropriate
10. Click the Save option and alter the save location to the folder made for the new
Method and Change the name of the Method to differentiate the new Method from
prior Methods


---


## Page 24


15

11. Save the new Method
12. Click on the home button in the top left
13. Do not overwrite the original/previous Method
14. Enter the Test section again
15. Select the new test Method
16. Set the travel limits and press OK
17. Check the Method section to make sure all of the settings meet your desired
requirements/parameters
18. Return to the Test section of the sample
19. Select the before test step of the Test process
20. Measure your specimen if you have not as of yet
21. Unlock the loading frame via the unlock button on the console, and raise the
crosshead to a height that allows your specimen and a level to fit comfortably
between the grips vertically
22. Mount the specimen by inserting the specimen into the upper grip and using a level
to ensure that the specimen is aligned vertically before tightening the upper grip.
23. Lower the upper grip and insert the specimen into the lower grip, tighten the lower
grip to ensure that the specimen is locked in place as can be seen in Figure 5 below.


---


## Page 25


16


Figure 5: A mounted specimen
24. Attach the extensometer to the center of the specimen as can be seen in Figure 6
below.


---


## Page 26


17


Figure 6: Extensometer attached to a mounted specimen
25. Zero and balance the force, displacement and strain measurements
26. Double check that the specimen has been measured, the clamps are tightened, the
Extensometer is on and centered properly, and that your data to be measured are
zeroed and balanced
27.  Begin the tensile testing of the mounted specimen by pressing the unlock button
on the console once more and hitting the start button before the lock reengages
28. Wait for the tensile test to finish and the specimen to fracture
29. Remove the fractured specimen parts from the grips
30. Select the next steps of the testing process to see the generated plots and continue
until you are at the page to start the next specimen’s tensile test
31. Repeat from step 20 of this process for each specimen of the tensile series


---


## Page 27


18

32. Click the checkered flag once tensile testing has been performed on each specimen
of the tensile series to finish the tensile testing
33. Save the tensile testing results
34. Check to make sure that the data was added to the destination folder properly
35. Transfer the data to a storage method of your preference
36. Exit out of the Bluehill Universal program
37. Shutdown the monitor and turn off the loading frame
The tensile testing data obtained from the above process was saved as a CSV file
to the designated folder by the Bluehill Universal software, and can be opened using the
Microsoft Excel Program. The data were copied to a new Excel file so as to maintain the
original data file in its unedited form. Using this copied data, stress strain curves for each
specimen were produced that Young’s moduli could be approximated from. These Young’s
moduli as well as the tensile strength and strain at fracture data points were collected for
each specimen and collected in an Excel file for data keeping.
3.2 Data Analysis
A total of 18 specimens, c.f. Table 1, were subjected to tensile testing in accordance
to the Method provided in the prior section. The data obtained from the tensile testing
process consisted of time in seconds, displacement in millimeters, tensile force in Newtons,
and axial strain in percent. For each specimen, a force vs. displacement and strain vs.
displacement plot was created to confirm that the two data sets follow the same trend of
increasing as the independent value displacement increases. An example of this plot for the
Series A 0-degree specimen can be seen below in Figure 7.


---


## Page 28


19


Figure 7:Force and Strain vs. Displacement plot for the A-0 Specimen
This plot shows that as axial displacement increases so too do axial force and axial
strain. This makes sense as the force required to consistently increase the displacement
should increase, and as the material is stretched to allow this displacement the strain will
likewise increase. This plot also shows how while the displacement was increasing at a
consistent rate, the force and strain increased at a non-linear rate to the displacement.
Similar plots were made for each specimen and can be found in the Appendix and all show
the same trend.
With the raw data in hand from the tensile tests, our focus turned to extracting the
Young’s moduli, tensile strength, and strain at fracture from the raw data. Using the
measured values of thickness and width for each specimen from Table 1, tensile stress was
calculated using 𝜎=
𝐹
𝑊×𝑇 where 𝜎 is the tensile stress, F is the recorded force, W is the
width, and T is the thickness. Along with this modification, the strain was transformed from


---


## Page 29


20

the % values that were measured to a simple strain by dividing the percent strain values by
100.
With the calculated stresses and strains in hand, stress-strain curves were made for
each specimen. An example of such a curve can be seen below in Figure 8 where the data
from the Series A 0-degree specimen is shown.

Figure 8: Stress - Strain Response of the A-0 Specimen
Looking at Figure 8, the stress-strain curve looks like what is expected of a stress
strain curve. The curve begins at the origin, follows a mostly linear slope to a region where
the slope decreases and becomes essentially horizontal until it reaches fracture. Similarly
to the Force and Strain vs. Displacement plot previously, the plots of this type for the other
specimens can be found in the Appendix.
For each specimen, the initial portion of the stress vs. strain plot that is somewhat
linear was extracted by using the first 300 data points of the data set. From these data points
a new plot was made, an example of which can be seen below in Figure 9.


---


## Page 30


21


Figure 9: Initial portion of the stress vs. strain plot for A-0
Using Excel’s trendline function on the above plot the Young’s modulus can be
approximated for each specimen along with an 𝑅2 value showing how well the
approximated trendline fits the data set. For the linear trendline function the intercept was
set to 0. The approximated Young’s modulus for a specimen is equal to the slope of the
trendline equation of the stress-strain plot. Looking at this plot specifically, the Young’s
modulus is approximately 2,425 MPa, and the trendline has a strong correlation to the data
set of 99.9%. The Young’s modulus is rounded from 2,424.7 to 2,425 as the tensile data
points collected have decimal points beyond the level of resolution expected of the system.
This is in conjunction with the low resolution of the caliper measured width and thickness.
As such it was determined that rounding many of the values throughout the obtained results
would be appropriate. The plots for the other specimens can be found in the Appendix.
The Young’s moduli and their 𝑅2 values for each specimen have been collected in
Table 2 below. In addition, Table 2 also contains the tensile strength and strain at fracture
for each specimen that were collected from the stress and strain data points by finding the


---


## Page 31


22

greatest collected value for each before fracture using the MAX function of Excel. Visual
representations of the tensile strength and strain at fracture for an example specimen’s plot
are shown in figure 10 below.
Table 2: Material Characteristics derived from the tensile tests
Specimen
Young’s
Modulus (MPa)
Coefficient of
determination (𝑅2)
Tensile Strength
(MPa)
Strain at
fracture
A-0
2,425
0.999
43.6
0.046
A-45
1,899
0.998
39.5
0.130
A-90
1,726
0.998
36.0
0.063
B-0
2,261
0.998
41.8
0.058
B-45
1,910
0.999
38.6
0.113
B-90
1,806
0.998
35.8
0.076
C-0
2,205
0.998
43.2
0.064
C-45
1,892
0.999
40.2
0.104
C-90
1,753
0.999
38.4
0.081
D-0
2,182
0.998
43.1
0.068
D-45
1,876
0.999
39.5
0.143
D-90
1,708
0.999
36.8
0.093
E-0
3,009
0.999
57.1
0.050
E-45
2,238
0.999
48.6
0.240
E-90
2,138
0.999
47.2
0.146
F-0
2,889
0.999
52.8
0.047
F-45
2,189
0.998
47.8
0.162
F-90
2,280
0.998
45.6
0.143
Average
2133
0.999
43.1
0.102
Std. Dev.
358
4.97*10-4
5.7
0.050
Range
1,301
0.001
21.3
0.194


---


## Page 32


23


Figure 10: Visual representation of tensile strength and strain at fracture

3.3 Discussion of Results
Using Excel’s data selection function, plots were made to compare the stress-strain
curves of multiple specimens. Comparison plots were made for each specimen series, each
angle, and finally all of the stress vs. strain curves. The first type of comparison plot
analyzed in this section compares the stress-strain curves of the three specimens from a
specimen series. Figures 11-16 below are this type of comparison plot for series A-F
respectively.


---


## Page 33


24


Figure 11: Tensile Series A Stress-Strain Comparison

Figure 12: Tensile Series B Stress-Strain Comparison


---


## Page 34


25


Figure 13: Tensile Series C Stress-Strain Comparison

Figure 14: Tensile Series D Stress-Strain Comparison


---


## Page 35


26


Figure 15: Tensile Series E Stress-Strain Comparison

Figure 16: Tensile Series F Stress-Strain Comparison
In these plots there are two primary patterns and one secondary pattern that can be
seen to be consistent throughout the different series. The first primary pattern is that the 0-
degree specimen consistently has the greatest tensile strength, the 45-degree specimen has
the next greatest tensile strength, and finally the 90-degree specimen has the least great
tensile strength. An example of this can be seen by looking at the Series A comparison plot


---


## Page 36


27

in which the 0o specimen had a tensile strength 10.4% greater than the 45o specimen, while
the 45o specimen’s tensile strength was 9.7% greater than the 90o specimen’s tensile
strength. This makes sense on an intuitive level as the material in the 0-degree specimens
were in line with the direction the stress was being applied, and as such should be capable
of resisting the stress to a better degree than the other specimens. In comparison, the
material in the 90-degree specimens is perpendicular to the direction of stress and would
be least capable of resisting the stress. The 45-degree specimens therefore fall in the middle
as their material is in a state midway between parallel and perpendicular to the stress. The
second primary pattern that can be seen in these plots is the pattern of strain at fracture. In
this pattern, the 45-degree specimen consistently reaches the greatest strain before fracture,
followed by the 90-degree specimen, and the 0-degree specimen consistently fractures at
the least strain in comparison to the other specimens of the same series. This can be seen
in the Series A comparison plot in which the 45o specimen’s strain at fracture is 106.4%
greater than the 90o specimen’s strain at fracture while the 90o specimen’s strain at fracture
is 37.0% greater than the 0o specimen. These patterns can also be seen by referring back to
Table 2 and comparing the tensile strength and strain at fracture between specimens of a
series. Consequently, these patterns show evidence that suggests that the raster angle has
noticeable and repeatable effects on the material characteristics of the printed specimens
and supports rejecting the first null hypothesis of this research.
The secondary pattern that can be seen in these series comparison plots is that the
0-degree sample tends to be the stiffest specimen. This is based off of the 0-degree
specimens having the greatest Young’s moduli. Following the 0-degree specimens, the 45-
degree specimens have the next greatest Young’s moduli, and the 90-degree specimens


---


## Page 37


28

usually have the least Young’s Moduli. The only point that goes against this pattern, and
what made it designated as a secondary pattern, would be the Young’s Modulus of F-45
and F-90 where F-45 has a lower Young’s modulus than F-90. However, looking at Figure
15 it can be seen that the incline of these two data sets in the linear region is overlapping
and F-45 still follows the primary pattern of reaching a greater stress than F-90 before its
incline declines out as it enters the non-linear region despite this so it could be due to the
range of data selected for estimating the Young’s moduli of these two specimens.
The next set of comparative plots that were made compare the specimens that share
their raster angle. These plots are shown in the order of 0o, 45o, and then 90o in Figures 17,
18, and 19 respectively.

Figure 17: 0-Degree Specimens of Each Tensile Series


---


## Page 38


29


Figure 18: 45- Degree Specimens of Each Tensile Series

Figure 19: 90- Degree Specimens of Each Tensile Series
Moving the analysis to this next set of plots, the angle specific plots also have a
point of interest. In these plots it can be seen that the specimens have split into two groups
of A-D and E-F. These groupings are designated primarily by the incline of the specimens
in their linear region as each specimen tends to become more unique as they enter their


---


## Page 39


30

non-linear regions. This splitting into groups is a point of interest as the material that was
used for producing each specimen was the same, yet E-F are shown to reach greater stresses
before fracture regardless of raster angle. The reason for this occurring is unknown as of
now, as the only primary difference between A-D and E-F is that E-F were produced earlier
on in the process of this research. However, despite the difference in the max stress between
the two group, all of the tensile series still follow the patterns that were previously
mentioned. This shows that despite the seeming difference in mechanical properties, the
raster angle is still affecting the material in the same way, and is supporting evidence that
the angle of print does have an effect on the final mechanical properties of a specimen.
The final plot made for comparing the stress-strain curves of specimens compares
the stress-strain curves of every tensile specimen in one plot and can be seen in Figure 20
below.

Figure 20: A collection of the tensile data for every specimen
Looking at the results in Figure 19 of the total collection of stress vs. strain curves,
a number of comparisons become more obvious than when looking at individual stress-


---


## Page 40


31

strain curves or the comparison curves for individual series or angles. The first of these
points would be to observe just how much greater the tensile stress of E-0 and F-0 is to
every other specimen. Still looking at the results of series E and F, it can be seen in this
plot that E-90 and F-90 which have the lowest tensile strength of the E and F series have
greater tensile strengths than the 0-degree specimens of series A-D. However, moving on
from the differences between E and F with the other series it can be seen in this plot how
distinct the results are when comparing the specimens of different angles for series A-D.
This can be seen in how distinct the grouping for specimens of angles is in the plot,
supported by there being no overlap between the 0o, 45o, or 90o specimens of series A-D.
The final point of discussion for the results of this chapter is the comparison of the
values from Table 2 with the reported values of the material when purchased.  To restate
the pertinent mechanical properties stated by the vendor, this material is reported to have a
Young’s modulus of 6,000 MPa, and Tensile strength of 100 MPa. However, based on the
results from tensile testing the greatest Young’s modulus found in the tested specimens was
3,009 MPA for the E-0 specimen, while the greatest Tensile strength of 57.1 MPa was also
observed in the E-0 specimen. While it does make sense that the specimen with the greatest
Young’s modulus would also have the greatest Tensile strength, the fact is that both values
are only slightly greater than half of the values that the vendor stated. This is especially
relevant as E-0 had a greater tensile strength to the point that it was visually obvious when
comparing it to the other 0-degree specimens that were tested. The 0-degree specimens of
series A-D tended to have tensile strengths closer to the 43 MPa region which do not even
reach half of what the vendor states to be the expected tensile strength of this material. The
cause of this difference is not known as of now.


---


## Page 41


32

Chapter 4: Specimen Prep for Microscopy

This Chapter’s focus is on the process and results of making and polishing molds
of the gage-lengths of specimens in preparation for performing microscopy on the
molded specimens.
4.1 Molding

In addition to collecting data through tensile testing, microscopy data was also
collected for this research. To prepare specimens for microscopy, the specimens were set
in a mold made of Allied Quickcure. To start this process, the gage lengths of specimens
were debrimmed and bisected horizontally so that there was access to the internal cross-
section of the specimens and that they would fit into the mold cups. For this research, the
bisecting step was completed using a Dremel tool attached with a metal cutting head
attachment.
After the gage length halves cooled down from the cutting process, and were
cleaned, a mold cup (Struers Product ID 40300089) was designated for each specimen to
be molded in, and the following process was followed to make molds of the specimens:
1. PPE is worn, including lab coat, gloves, and eye protection.
2. The molding process begins by adding Allied Quickcure reagents (Allied
Product ID 170-10000) at a ratio of 2:1 of solid and liquid reagents
respectively into a designated mixing cup and stirring the solution until it is
thoroughly mixed and in the form of a viscous fluid.
3. The mixed solution is poured slowly into the bottom of a mold cup until the
bottom of the mold cup is covered with a thin layer of the solution of
approximately 2 mm.


---


## Page 42


33

a. While the bottom of the mold cup is being filled, the mold at this
end will be considered the top of the mold itself throughout this
research as this is the side that will be viewed for microscopy after
the molding and polishing processes are complete. Similarly, the end
of the mold at the top of the mold cup will be considered as the
bottom of the mold.
4. After covering the bottom of the mold cup with the solution, one of each
bisected gage length for a specimen series is placed vertically into the mold
cup, cut end at the bottom of the mold cup, according to the pattern shown
in Figure 21 below. This pattern is used consistently through every mold to
keep track of which gage length is what angle as the mold makes it difficult
to see the side of the gage lengths clearly and removes sharpie-based
markings on the gage lengths.


---


## Page 43


34


Figure 21: Orientation of specimens in mold
5. Once the gage lengths are in the mold cup according to the designated
pattern, the remainder of the mold cup is slowly filled with more of the fluid
while taking care to not disturb the gage lengths and repositioning them if
they are disturbed in the process.
6. Once the mold cup is filled and the specimens are fully covered the mold is
allowed to sit and settle for twenty-four hours to guarantee it has set fully.
After allowing the mold to set, it was removed from the mold cup, and
polished using a Struers Laboforce 3 Semi-automatic Polisher shown below in
Figure 22.


---


## Page 44


35


Figure 22: Struers Polisher
To polish the molds, the following process was used:
1. PPE is worn, including a lab coat, gloves, and eye protection.
2. A magnetic plate with a textured top side is first mounted and wetted by
running water over the plate as the polisher runs to spread a thin layer evenly
across the plate.
3. This is followed by removing the water while the polisher continues to run.
a. This is done because the 800-grit sandpaper that is to be mounted
does not have an adhesive side to help it stick to the textured plate.
4. With the textured plate mounted and wetted, a sheet of 800-grit sandpaper
(Struers Product ID 40400010) is mounted on the polisher over the textured
plate.
5. The sandpaper is then wetted in the same way that the textured plate was
wetted.


---


## Page 45


36

6. With the 800-grit sandpaper mounted and wetted, the mold is locked into
place in the instrument, bottom down, and the screw is tightened until the
indicator reads between the second and third marks from the bottom.
7. After locking the mold into place, water is continuously run over the plate
as the instrument is repeatedly turned on for one-minute intervals to remove
the rough edges and irregularities that were often present after the molding
process.
a. Between each one-minute run of the polisher the screw is checked
to make sure that it is still within the accepted range.
8. Once the irregularities are removed from the bottom of the mold, it can be
dismounted from the instrument and washed off to remove any remnant
material from the sandpaper.
9. The 800-grit sandpaper is then removed, and replaced with a 1000-grit
sandpaper (Buehler Product ID 36081000) by pulling the tab on the side of
the 1000-grit sandpaper and removing the cover from the adhesive side of
the sandpaper to securely mount it to the instrument.
10. The 1000-grit is then wetted like with the 800-grit sandpaper.
11. With the 1000-grit sandpaper mounted and wetted, the mold can be mounted
into the polisher once more, with the top down this time.
12. The polisher is then run for 15 one-minute intervals, while checking that the
screw is between the second and third marks from the bottom each time.
a. While the bottom of the mold can take several repetitions of the one-
minute intervals, the process that was determined for the top of the


---


## Page 46


37

mold was to run it through 15 one-minute intervals for each of the
polishing materials.
13. After running the top of the mold over the 1000-grit sandpaper for 15 one-
minute intervals, the mold can be dismounted and rinsed off once more.
14. The 1000-grit sandpaper is then replaced with a 1200-grit sandpaper (Allied
Product ID 50-10077) that is also mounted via its adhesive layer before
wetting it.
15. With the 1200-grit sandpaper mounted and wetted, the mold can be mounted
and secured by tightening the screw once more before starting the next 15
one-minute intervals.
16. Once the 15 1200-grit intervals are run, the mold can be dismounted and
washed off again, making sure to lay the mold bottom down so as not to get
anything on the top of the mold or scratch it, and the 1200-grit sandpaper
sheet can be removed from the instrument.
17. With the 1200-grit polishing completed, the magnetic plate is removed, and
the instrument can be prepped for the 3- and 1-micron treatments.
a. To prepare for this, the 3- and 1-micron polishing suspensions had
already been transferred into empty and sterilized containment
bottles connected to a Struers Labodoser, pictured in Figure 22
above, that allowed for controlled distribution of the suspensions to
be dispensed onto the plate.
18. Before mounting the mold this time, a MD-Dur plate (Struers Product ID
40500074) is mounted and prepped by running the polisher with the 3-


---


## Page 47


38

micron suspension selected on the Labodoser until the 3-micron polishing
suspension (Struers Product ID 40600535) begins to be dispensed onto the
plate.
19. The polisher is then mounted with a washed, blank mold to spread a fresh
layer of the suspension across the plate evenly.
a. If this is the first time polishing, the plate will be blank, otherwise
the plate previously used for 3-micron polishing will be used so as
to keep the polishing suspensions from being mixed.
20. After evenly spreading the 3-micron suspension over the plate, the blank
mold can be removed and washed, and the specimen mold can be mounted
top-down in the instrument and ran for 15 one-minute intervals while
selecting for the 3-micron suspension each time the instrument is started.
21. After these 15 intervals of polishing with the 3-micron polishing
suspension, the mold is dismounted and washed off to remove any remnants
of the polishing suspension from the face being polished.
22. The 3-micron plate is then removed from the instrument and stored for
future use, and the next plate is prepped in the same way as the 3-micron
plate except selecting for the 1-micron suspension.
a. Similarly to the 3-micron plate, if this is the first time prepping for
the 1-micron suspension a blank plate will be used, otherwise the 1-
micron plate from prior polishing sessions will be used.
23. After prepping for the 1-micron suspension (Struers Product ID 40600555)
by evenly spreading it out across the plate with a washed blank mold, the


---


## Page 48


39

specimen mold can once more be mounted into the instrument top down
and ran with the 1-micron suspension for 15 one-minute intervals.
24. After finishing this set of 15 intervals, the mold can be dismounted and
washed off once more before it is stored in preparation to be transported to
the location where microscopy will be performed on it.
a. Along with storing the mold, the 1-micron plate is removed from the
instrument and stored in a similar way to the 3-micron plate for
future use.
25. The polishing station is then cleaned and left in a ready state for the next
person who will use it.
4.2 Results
The results of molding and polishing the gage lengths for each specimen of each
set is best expressed in an image of the finalized, polished molds. Below is Figure 23, an
image of the six molds that were produced and polished. Each mold contains approximately
half of a gage length of each angle for its series.


---


## Page 49


40


Figure 23: The Six Molds in the Order A, B, C, D, E, and F


---


## Page 50


41

Chapter 5: Microscopy

This chapter’s focus is on how microscopy was performed on the polished molds
from Chapter 4 and discusses the conclusions drawn from the images obtained from this
microscopy.
5.1 Imaging Procedure

After polishing the molds, the next step was to begin microscopy. To start this
process, a time was reserved at the Samuel Roberts Noble Microscopy Lab on the
University of Oklahoma campus through the Agilent Cross Lab website ilabsolutions.com
for the Keyence VHX-7000 ultramicroscope. Once there, the microscope and its associated
computer were turned on and initialized. The mold was removed from its storage container
and placed centrally on the microscope’s viewing plate, and the full ring lighting was
chosen from the lighting options. From this point, the microscope was controlled via the
computer to find points of interest on the specimen within the mold. For each point of
interest, the microscope was focused before capturing a set of images at three
magnifications at that point, refocusing the microscope between each capture. During
microscopy, the viewing plate was rotated to ensure that the z-axis of the specimen was in
line with the vertical of the captured images and the x-axis was aligned to be coming out
of the image. The magnifications captured in this research were 100x, 200x, and 500x.
Photos were taken of a point of interest from each specimen at these magnifications in both
.jpg and .tif formats.
5.2 Discussion of Results

In total, the number of microscopy images taken were 54 for each file format.
From these images, three have been chosen to show as examples, one for each angle that


---


## Page 51


42

gives the best view of the state of the carbon fibers in that specimen. These examples
constitute Figures 24-26 below.

Figure 24: Specimen C-0 at 200x magnification


---


## Page 52


43


Figure 25: Specimen B-45 at 200x magnification

Figure 26: Specimen D-90 at 200x magnification


---


## Page 53


44


Looking at Figures 24-26, the thin white lines were determined to be the carbon
fibers dispersed throughout the specimens. While no statistical analysis was performed,
the distribution of the carbon fibers was deemed to be mostly unaffected by the raster
angle of the specimen. This conclusion was reached, as regardless of which specimen’s
microscopy image was looked at, there did not appear to be any reliable way to
differentiate which raster angle specimen was being examined. This was deemed to mean
that all three angles of specimens appear similarly unorganized. If the carbon fiber
distribution is similarly unorganized regardless of angle, this can be used to assume that it
is unlikely that the carbon fibers are having a considerable effect on the material
characteristics based on the specimen’s raster angle. This seeming randomness of the
carbon fibers also allows for the material to be assumed as somewhat isotropic for the
sake of material characterization. These results, while not statistically supported, appear
to stand as evidence that the raster angle does not have a noticeable effect on the
orientation of the fibers in the specimens. This supports failing to reject the second null
hypothesis of this research.


---


## Page 54


45

Chapter 6. Concluding remarks
6.1 Interpretations
In summary, in Chapter 3 it was determined that based on the results obtained in
this research, the material characteristics follow two primary patterns and one secondary
pattern as a function of the raster angle of the specimen. The first primary pattern is in
regard to the tensile strength that the specimens reached. In this pattern, it was observed
that the 0-degree specimens consistently reached the greatest tensile strength, the 45-degree
specimens reached the next greatest tensile strength, and the 90-degree specimens reached
the least great tensile strength. An example of this was shown when comparing specimens
of Series A in which the 0o specimen had a tensile strength 10.4% greater than the 45o
specimen, while the 45o specimen’s tensile strength was 9.7% greater than the 90o
specimen’s tensile strength. The second primary pattern was in regard to the strain at
fracture that the specimens would reach. In this pattern it was determined that the 45-degree
specimen consistently reached the greatest strain at fracture, the 90-degree specimen
reached the next highest strain at fracture, and the 0-degree specimen reached the least
great strain at fracture. This was shown in the comparison of Series A in which the 45o
specimen’s strain at fracture was 106.4% greater than the 90o specimen’s strain at fracture
while the 90o specimen’s strain at fracture was 37.0% greater than the 0o specimen.
The secondary pattern that was observed in the tensile results was that the 0-degree
specimen was typically the stiffest based on it consistently having the greatest Young’s
modulus of the series, the 45-degree specimen being the next stiffest based on its Young’s
modulus, and the 90-degree specimen being the least stiff. This pattern is considered as
secondary, as while it held for the majority of specimen series, the F series had its 45 and


---


## Page 55


46

90-degree specimens switch according to their Young’s moduli. It was determined that this
could be a problem of chosen data points to create the Young’s moduli estimates as the two
specimens’ Young’s moduli were very close and overlapping in the plot of the F series.
The primary patterns in the tensile results showed that there was evidence that the
raster angle had a noticeable and repeatable effect on the tensile properties of the printed
specimens. This evidence supports rejecting the first null hypothesis of this research.
In Chapter 5, it was deemed that upon observation of the microscopy images the
carbon fibers did not appear to follow any angle-based patterns. Given this finding, it could
be assumed that it was unlikely that the fibers were giving any considerably greater
reinforcement to one angle over another. It was also assumed, based on the lack of pattern,
that the specimens were mostly isotropic for the sake of material characterization.
The findings from Chapter 5’s results show that the fibers appear to be quasi-
randomly oriented regardless of raster angle. These results support failing to reject the
second null hypothesis of this research.
These results agree with the findings of the paper by Ning et al. [11] referenced in
Chapter 1 where they also found a difference based on raster angle. However, in
comparison, the data from this research shows that while they found their (0,90) specimens
to have the greatest tensile strength it was likely that the 0-degree layers of their samples
were contributing the majority of the tensile strength in those results. This shows that if the
stress direction is known for a structural member the greatest tensile strength will be
achieved by aligning the raster angle with that stress direction. Similarly, if the expected
high strain direction is known, and strain is the characteristic that needs to be built for,


---


## Page 56


47

aligning the raster angle 45o with the direction of strain provides the greatest strain before
fracture. Given this information, depending on the requirements for a part, it can also be
proposed that, as 45o specimens had the second greatest tensile strength and the greatest
strain at fracture, aligning the raster angle 45o to the direction of expected stresses will
produce a structure that will have a marginally lesser tensile strength than a 0o raster angle
structure while being able to withstand the most strain.
6.2 Plans for the future

Given the results that were obtained in this research there are primarily three
different directions that could be studied to continue this route of investigation.
1. First, conduct studies to investigate the effects of a wider range of angles such as
15o, 30o, 60o, and 75o and see how the results compare to the results found in this
research.
2. A second possible expansion would require a larger experimental program. This
point would be to essentially repeat this round of research, but instead of using only
one material for the research using a variety of materials to see if the patterns that
were discovered in Chapter 3 hold regardless of material.
3. The third expansion method would focus on the microscopy and image analysis
side of this research by performing a more detailed analysis, such as including
statistical calculations.


---


## Page 57


48

References
[1] Additive Manufacturing Market Size Report, 2030. (n.d.).
https://www.grandviewresearch.com/industry-analysis/additive-manufacturing-
market
[2] González, C. M. (2020, January 30). Timeline of the 3D printing history. ASME.
https://www.asme.org/topics-resources/content/infographic-the-history-of-3d-
printing
[3] Birosz, M. T., Andó, M., & Ledenyák, D. (2021a). Effect of FDM infill patterns
on mechanical properties. SSRN Electronic Journal.
https://doi.org/10.2139/ssrn.3950131
[4] Plocher, J., Wioland, J.-B., & Panesar, A. S. (2022). Additive manufacturing with
fibre-reinforcement – design guidelines and investigation into the influence of
infill patterns. Rapid Prototyping Journal, 28(7), 1241–1259.
https://doi.org/10.1108/rpj-09-2021-0223
[5] Abderrafai, Y., Hadi Mahdavi, M., Sosa-Rey, F., Hérard, C., Otero Navas, I.,
Piccirelli, N., Lévesque, M., & Therriault, D. (2022). Additive manufacturing of
short carbon fiber-reinforced polyamide composites by fused filament fabrication:
Formulation, manufacturing and characterization. Materials &amp; Design, 214,
110358. https://doi.org/10.1016/j.matdes.2021.110358
[6] Russell, T., & Jack, D. A. (2023). Tensile and compression strength prediction
and validation in 3D-printed short-fiber-reinforced polymers. Polymers, 15(17),
3605. https://doi.org/10.3390/polym15173605


---


## Page 58


49

[7] Wang, K., Li, S., Rao, Y., Wu, Y., Peng, Y., Yao, S., Zhang, H., & Ahzi, S.
(2019). Flexure behaviors of ABS-based composites containing carbon and kevlar
fibers by material extrusion 3D printing. Polymers, 11(11), 1878.
https://doi.org/10.3390/polym11111878
[8] Nawafleh, N., Elibol, F. K., Aljaghtham, M., Oflaz, E., Ciciriello, A. J., Dumont,
C. M., Dauer, E., Gorguluarslan, R. M., Demir, T., & Celik, E. (2020). Static and
dynamic mechanical performance of short kevlar fiber reinforced composites
fabricated via direct ink writing. Journal of Materials Science, 55(25), 11284–
11295. https://doi.org/10.1007/s10853-020-04826-w
[9] Banjanin, B., Vladic, G., Pál, M., Balos, S., Dramicanin, M., Rackov, M., &
Knezevic, I. (2018). Consistency analysis of mechanical properties of elements
produced by FDM Additive Manufacturing Technology. Matéria (Rio de Janeiro),
23(4). https://doi.org/10.1590/s1517-707620180004.0584
[10]  Wang, J. Y., Xu, D. D., Sun, W., Du, S. M., Guo, J. J., & Xu, G. J. (2019).
Effects of nozzle-bed distance on the surface quality and mechanical properties of
fused filament fabrication parts. IOP Conference Series: Materials Science and
Engineering, 479, 012094. https://doi.org/10.1088/1757-899x/479/1/012094
[11] Ning, F., Cong, W., Hu, Y., & Wang, H. (2016). Additive manufacturing of
carbon fiber-reinforced plastic composites using fused deposition modeling:
Effects of process parameters on tensile properties. Journal of Composite
Materials, 51(4), 451–462. https://doi.org/10.1177/0021998316646169


---


## Page 59


50

Appendix
Appendix 1: Creating an Instron Test Method

The process for creating a new Method from scratch follows these steps:
1. Turn on the Instron and attached monitor
2. Create a new folder that will be where you will save the new method
3. Start the Bluehill Universal program
4. Enter the test section and choose the create a new method option in the new
sample section
5. Choose tension method
6. Press OK on the set the travel limits page
7. Save the method to the folder that you made for it
8. In the General section
a. Set system of units to SI
b. Set specimen parameters to method default
9. In the sample section
a. Make no changes
10. In the Specimen section
a. In the Properties section, modify the geometry based on the specimens
11. In the Measurements section
a. Add Strain from the Measurement types to Measurements available in the
method
12. In the Calculations section
a. Make no changes
13. In the Test Control section


---


## Page 60


51

a. In the strain section, set the primary source to Strain 1
b. In the pre-test section:
i. Turn pre-load on and set the rate to 0.125 mm/s
ii. Set the changeover criteria measurement to Force and set it to
22.24 N
c. In the Test section, set control mode to displacement and set it to 0.25
mm/s
d. In the end of test section:
i. Set criteria 1 to measurement rate
ii. Set measurement 1 to force
iii. Set sensitivity 1 to 40%
iv. Set End of test action to stop
e. In the Data section:
i. Set capture scheme to custom settings
ii. Set measurement 1 to Time
iii. Set interval 1 to 20 ms
14. In the Console section
a. Add Strain 1 and Time to selected live displays
b. Set the order of the live displays to be Time, Displacement, Force, Strain 1
15. In the Workspace section
a. Turn gridlines off for both graph 1 and 2 in their advanced sections
b. On Graph 2 set the Y-Data to be Strain 1
c. In the Raw Data section add Strain 1 to the selected measurements


---


## Page 61


52

16. In the Exports Section
a. In the File settings section
i. Add the file you created for this method as the file location
ii. Modify the sample file name to be recognizable for the test
b. In the exports 1 and 2 sections set the frequency to at finish
c. In the exports 1 section set raw data to on
17. In the workflow section
a. Set the number of specimens to the number in a series
b. Turn run as prompted test on
18. In the reports section
a. In the body section, add graph 2 and results 2 to the selected items
19. Save the method


---


## Page 62


53

Appendix 2: Force-Displacement and Strain-Displacement Results

Figure 27: Force & Strain vs. Displacement for A-45

Figure 28: Force & Strain vs. Displacement for A-90
0
1
2
3
4
5
6
7
8
9
0
500
1000
1500
2000
2500
3000
0
1
2
3
4
5
6
7
8
Axial Strain %
Axial Force, N
Axial Displacement, mm
Force - Displacement
Strain - Displacement


---


## Page 63


54


Figure 29: Force & Strain vs. Displacement for B-0

Figure 30: Force & Strain vs. Displacement for B-45
0
1
2
3
4
5
6
7
0
500
1000
1500
2000
2500
3000
3500
0
1
2
3
4
5
6
Axial Strain %
Axial Force, N
Axial Displacement, mm
Force - Displacement
Strain - Displacement
0
2
4
6
8
10
12
0
500
1000
1500
2000
2500
3000
3500
0
2
4
6
8
10
12
Axial Strain %
Axial Force, N
Axial Displacement, mm
Force Displacement
Strain - Displacement


---


## Page 64


55


Figure 31: Force & Strain vs. Displacement for B-90

Figure 32: Force & Strain vs. Displacement for C-0
0
1
2
3
4
5
6
7
8
9
10
0
500
1000
1500
2000
2500
3000
0
1
2
3
4
5
6
7
8
9
Axial Strain %
Axial Force, N
Axial Displacement, mm
Force Displacement
Strain - Displacement
0
1
2
3
4
5
6
7
8
9
0
500
1000
1500
2000
2500
3000
3500
0
1
2
3
4
5
6
Axial Strain %
Axial Force, N
Axial Displacement, mm
Force - Displacement
Strain - Displacement


---


## Page 65


56


Figure 33: Force & Strain vs. Displacement for C-45

0
2
4
6
8
10
12
14
0
500
1000
1500
2000
2500
3000
3500
0
2
4
6
8
10
12
Axial Strain %
Axial Force, N
Axial Displacement, mm
Force - Displacement
Strain - Displacement


---


## Page 66


57


Figure 34: Force & Strain vs. Displacement for C-90


---


## Page 67


58


Figure 35: Force & Strain vs. Displacement for D-0

Figure 36: Force & Strain vs. Displacement for D-45


---


## Page 68


59


Figure 37: Force & Strain vs. Displacement for D-90

Figure 38: Force & Strain vs. Displacement for E-0


---


## Page 69


60


Figure 39: Force & Strain vs. Displacement for E-45

Figure 40: Force & Strain vs. Displacement for E-90


---


## Page 70


61


Figure 41: Force & Strain vs. Displacement for F-0

Figure 42: Force & Strain vs. Displacement for F-45


---


## Page 71


62


Figure 43: Force & Strain vs. Displacement for F-90


---


## Page 72


63

Appendix 3: Stress-Strain Curves

Figure 44: Stress vs. Strain for A-45

Figure 45: Stress vs. Strain for A-90


---


## Page 73


64


Figure 46: Stress vs. Strain for B-0

Figure 47: Stress vs. Strain for B-45


---


## Page 74


65


Figure 48: Stress vs. Strain for B-90

Figure 49: Stress vs. Strain for C-0


---


## Page 75


66


Figure 50: Stress vs. Strain for C-45

Figure 51: Stress vs. Strain for C-90


---


## Page 76


67


Figure 52: Stress vs. Strain for D-0

Figure 53: Stress vs. Strain for D-45


---


## Page 77


68


Figure 54: Stress vs. Strain for D-90

Figure 55: Stress vs. Strain for E-0


---


## Page 78


69


Figure 56: Stress vs. Strain for E-45

Figure 57: Stress vs. Strain for E-90


---


## Page 79


70


Figure 58: Stress vs. Strain for F-0

Figure 59: Stress vs. Strain for F-45


---


## Page 80


71


Figure 60: Stress vs. Strain for F-90


---


## Page 81


72

Appendix 4: Estimates of Young’s Modulus

Figure 61: Initial portion of the stress vs. strain plot for A-45

Figure 62: Initial portion of the stress vs. strain plot for A-90


---


## Page 82


73


Figure 63: Initial portion of the stress vs. strain plot for B-0

Figure 64: Initial portion of the stress vs. strain plot for B-45


---


## Page 83


74


Figure 65: Initial portion of the stress vs. strain plot for B-90

Figure 66: Initial portion of the stress vs. strain plot for C-0


---


## Page 84


75


Figure 67: Initial portion of the stress vs. strain plot for C-45

Figure 68: Initial portion of the stress vs. strain plot for C-90


---


## Page 85


76


Figure 69: Initial portion of the stress vs. strain plot for D-0

Figure 70: Initial portion of the stress vs. strain plot for D-45


---


## Page 86


77


Figure 71: Initial portion of the stress vs. strain plot for D-90

Figure 72: Initial portion of the stress vs. strain plot for E-0


---


## Page 87


78


Figure 73: Initial portion of the stress vs. strain plot for E-45

Figure 74: Initial portion of the stress vs. strain plot for E-90


---


## Page 88


79


Figure 75: Initial portion of the stress vs. strain plot for F-0

Figure 76: Initial portion of the stress vs. strain plot for F-45


---


## Page 89


80


Figure 77: Initial portion of the stress vs. strain plot for F-90


---


## Page 90


ProQuest Number:


INFORMATION TO ALL USERS
The quality and completeness of this reproduction is dependent on the quality
and completeness of the copy made available to ProQuest.







Distributed by
ProQuest LLC a part of Clarivate (         ).
Copyright of the Dissertation is held by the Author unless otherwise noted.


This work is protected against unauthorized copying under Title 17,
United States Code and other applicable copyright laws.


This work may be used in accordance with the terms of the Creative Commons license
or other rights statement, as indicated in the copyright statement or in the metadata
associated with this work. Unless otherwise specified in the copyright statement
or the metadata, all rights are reserved by the copyright holder.


ProQuest LLC
789 East Eisenhower Parkway
Ann Arbor, MI 48108 USA
31936856
2025


---
