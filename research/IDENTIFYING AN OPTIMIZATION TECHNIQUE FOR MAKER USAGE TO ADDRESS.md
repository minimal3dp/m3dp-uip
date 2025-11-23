# IDENTIFYING AN OPTIMIZATION TECHNIQUE FOR MAKER USAGE TO ADDRESS

> **Source:** `IDENTIFYING AN OPTIMIZATION TECHNIQUE FOR MAKER USAGE TO ADDRESS.pdf`
> **Converted:** 2025-11-22 21:18:12
> **Method:** PyMuPDF

---

## Page 1


University of Tennessee, Knoxville
University of Tennessee, Knoxville
TRACE: Tennessee Research and Creative
TRACE: Tennessee Research and Creative
Exchange
Exchange
Doctoral Dissertations
Graduate School
12-2021
IDENTIFYING AN OPTIMIZATION TECHNIQUE FOR MAKER
IDENTIFYING AN OPTIMIZATION TECHNIQUE FOR MAKER
USAGE TO ADDRESS COVID-19 SUPPLY SHORTFALLS
USAGE TO ADDRESS COVID-19 SUPPLY SHORTFALLS
Michael J. Wilson
University of Tennessee, Knoxville, mwils107@vols.utk.edu
Follow this and additional works at: https://trace.tennessee.edu/utk_graddiss
 Part of the Industrial Engineering Commons
Recommended Citation
Recommended Citation
Wilson, Michael J., "IDENTIFYING AN OPTIMIZATION TECHNIQUE FOR MAKER USAGE TO ADDRESS
COVID-19 SUPPLY SHORTFALLS. " PhD diss., University of Tennessee, 2021.
https://trace.tennessee.edu/utk_graddiss/7015
This Dissertation is brought to you for free and open access by the Graduate School at TRACE: Tennessee
Research and Creative Exchange. It has been accepted for inclusion in Doctoral Dissertations by an authorized
administrator of TRACE: Tennessee Research and Creative Exchange. For more information, please contact
trace@utk.edu.


---


## Page 2


To the Graduate Council:
I am submitting herewith a dissertation written by Michael J. Wilson entitled "IDENTIFYING AN
OPTIMIZATION TECHNIQUE FOR MAKER USAGE TO ADDRESS COVID-19 SUPPLY
SHORTFALLS." I have examined the final electronic copy of this dissertation for form and
content and recommend that it be accepted in partial fulfillment of the requirements for the
degree of Doctor of Philosophy, with a major in Industrial Engineering.
Andrew Yu, Major Professor
We have read this dissertation and recommend its acceptance:
Zhongshun Shi, James Simonton, Feng Yuan Zhang
Accepted for the Council:
Dixie L. Thompson
Vice Provost and Dean of the Graduate School
(Original signatures are on file with official student records.)


---


## Page 3


Identifying an Optimization Technique for Maker Usage to Address Covid-19 Supply
Shortfalls




A Dissertation Presented for the
Doctor of Philosophy
Degree
The University of Tennessee, Knoxville






Michael J. Wilson
December 2021


---


## Page 4


ii
Copyright © 2021 Michael J. Wilson All rights reserved.


ISBN:



ISBN-13:


---


## Page 5


iii
ACKNOWLEDGEMENTS
Throughout my PhD classes, my research, and the writing of this dissertation I have
received significant support and assistance.
I would like to thank my dissertation advisor, Dr. Andrew Yu, whose guidance, and
feedback was instrumental in the composition of this research. It was through Dr. Yu’s
willingness to constantly answer my questions that I was able to focus on my research.
I would like to thank all my colleagues at Austin Peay State University that assisted and
advised me during my PhD classes and my research. I would especially like to thank
Dr. Raman Sahi who always made time to tutor me in mathematical and statistical
classes and answer questions. Without her assistance and tutelage, I would not have
been able to complete many of my classes successfully.
Most importantly, I would like to thank my family. My children Braxton and Alex, you
have always been and will always be an inspiration to me. I could not be prouder of you
both. I would like to thank my parents who raised me to love science and to always ask
why. Some of my fondest memories as a child were fishing with my dad and going to
museums with my mom. Lastly, I would like to thank my wife, Tara, whose love, and
support have saved my life both figuratively and literally. You kept me going when I
wanted to quit. I love you.


---


## Page 6


iv
ABSTRACT
Fused Deposition Modeling (FDM) can be purchased for under five hundred dollars.
The availability of these inexpensive systems has created a large hobbyist (or maker)
community. For makers, FDM printing is used numerous uses.
With the onset of the COVID-19 pandemic, the needs for Personal Protective
Equipment (PPE) skyrocketed. COVID-19 mitigation strategies such as social
distancing, businesses closures, and shipping delays created significant supply
shortfalls. The maker community stepped in to fill gaps in PPE supplies.
In the case of 3DP, optimization remains the domain of commercial entities.
Optimization is, at best, ad-hoc for makers. With the need to PPE supplies and COVID-
19 related supply delays, optimization techniques would be of great value to makers.
The objective functions in this research is throughput and cost with quality factored into
both. There are several parameters common to both throughput and surface roughness,
including layer thickness, print speed, infill density, raster width, and wall thickness. This
research will utilize a 2-level fractional factorial design.
Least Squares Regression (OLS) will be completed on throughput and cost
independently. Quality will be considered a component of both. For example, an OLS
will be completed for the throughput to determine the effects of the process parameters
on throughput. Using a 95% confidence interval, a process parameter with a P-value
smaller that .05 will show that the process parameter has a significant effect on the
throughput. Upon completion of each OLS model 𝜖-Contraint methodology will be used


---


## Page 7


v
to jointly optimize the process parameters. Validation trials will be completed to test the
optimized process parameters. The results will be documented and discussed.


---


## Page 8


vi
PREFACE
The basis of this research stems from my work early in the COVID-19 pandemic. I was
part of a team to use 3D printers to create face shields for first responders and medical
personnel. One of the ongoing problems throughout the project was securing resources.
With production and shipping from China heavily impacted, we needed to do more with
less. At the height of the project, tools and methods to easily optimize print parameters
would have been invaluable. Unfortunately, many optimization techniques remain the
domain of engineers and industry.
The focus of this research is to identify optimization methods that can be accessed by
the maker community. In a review of the literature, 𝜖-constraints methodology has not
previously been utilized. This method and the use of open-source tools to execute the
analysis offer an option for makers.


---


## Page 9


vii
TABLE OF CONTENTS
1 — CHAPTER ONE - INTRODUCTION AND GENERAL INFORMATION .................... 1
1.1 — Introduction to AM .............................................................................................. 1
1.2 — The Maker Community and COVID-19 .............................................................. 2
1.3 — COVID-19 and Supply Issues ............................................................................ 6
1.3.1 — Supplies of PPE .......................................................................................... 7
1.4 — Optimization ....................................................................................................... 8
1.4.1 — Makers and Optimization ........................................................................... 10
1.4.2 — Overview of a Face Shield ........................................................................ 10
1.4.3 — Discussion of Variables ............................................................................. 10
1.5 — Chapter 1 Summary ......................................................................................... 13
2 — CHAPTER TWO - LITERATURE REVIEW ............................................................ 15
2.1 — 3DP Introduction .............................................................................................. 15
2.1.1 — History of 3DP ........................................................................................... 16
2.1.2 — Introduction to AM ..................................................................................... 18
2.1.3 — Trends in AM ............................................................................................. 21
Biomaterials ............................................................................................................ 21
Buildings ................................................................................................................. 22
Protective Structures ............................................................................................... 23
Aerospace ............................................................................................................... 24
Low-Cost 3D Printing .............................................................................................. 24
2.1.4 — 3D Printing Tools and Terminology ........................................................... 26
Slicing Software ...................................................................................................... 27
2.1.5 — AM Summary ............................................................................................. 28
2.2 — PPE and COVID-19 ......................................................................................... 28
2.2.1 — COVID-19 Prevention ................................................................................ 30
2.2.2 — American Medical Association Ideas ......................................................... 31
2.3 — The Maker Community and Makerspaces ....................................................... 32
2.3.1 — The Maker Community and COVID-19 ..................................................... 38
2.4 — Introduction to Optimization ............................................................................. 38


---


## Page 10


viii
2.4.1 — Optimization for Makers ............................................................................ 39
Optimization for Makers .......................................................................................... 41
Overview of a Face Shield ...................................................................................... 41
2.4.2 — Discussion of Parameters ......................................................................... 44
2.4.3 — Optimization Summary .............................................................................. 54
3 — CHAPTER THREE - PROBLEM DEFINITION ....................................................... 55
3.1 — Research Scope .............................................................................................. 55
3.2 — Problem Definition ............................................................................................ 58
3.2.1 — Primary Problems ...................................................................................... 59
3.2.2 — Secondary Problems ................................................................................. 63
3.3 — Research Scope and Definition Summary ....................................................... 67
4 — CHAPTER FOUR - EXPERIMENTAL DESIGN AND SOLUTION APPROACH .... 70
4.1 — Design of Experiment (DOE) ........................................................................... 70
4.1.1 — An Example of DOE .................................................................................. 71
4.1.2 — Fractional Factorial Design ........................................................................ 73
4.1.3 — Analysis of Variance (ANOVA) .................................................................. 74
4.1.4 — Ordinary Least Squares Regression ......................................................... 74
4.1.5 — Response Optimization and Epsilon-Constraint ........................................ 76
4.2 — Inspection for Quality Control ........................................................................... 78
4.2.1 — Vigilance, Environment, Posture, Speed, Training, and Documentation ... 82
4.2.2 — Functional vs Nonfunctional Quality .......................................................... 83
4.3 — The Inspection Score ....................................................................................... 85
4.4 — Inspection Measurements ................................................................................ 87
4.5 — Experimental Tools .......................................................................................... 89
FDM Printers ........................................................................................................... 89
Smart Plugs ............................................................................................................. 93
3DP Slicer ............................................................................................................... 93
Octoprint .................................................................................................................. 94
Face Shield Model .................................................................................................. 95
Programming and DOE Modeling ........................................................................... 95
4.6 — Experimental Process ...................................................................................... 96


---


## Page 11


ix
5 — CHAPTER FIVE - CASE STUDY ......................................................................... 103
5.1 — Case Study Introduction ................................................................................. 103
5.2 — COVID-19 3DP in Tennessee ........................................................................ 104
5.3 — TN Project Statistics ....................................................................................... 104
5.4 — Case Study Experiment ................................................................................. 107
6 — CHAPTER SIX - RESULTS AND DISCUSSION .................................................. 119
6.1 — Data Compilation ........................................................................................... 119
Quality Scores .......................................................................................................... 123
6.2 — Data Analysis ................................................................................................. 123
Considering Quality ............................................................................................... 126
6.2.1 — Experimental Analysis A .......................................................................... 130
6.2.2 — Experimental Analysis B .......................................................................... 146
6.2.3 — Experimental Analysis C ......................................................................... 162
6.3 — Addressing the Research Questions ............................................................. 177
6.3.1 — Primary Problems Addressed .................................................................. 177
6.3.2 — Secondary Problems Addressed ............................................................. 185
7 — CHAPTER SEVEN - CONCLUSIONS AND RECOMMENDATIONS ................... 188
7.1 — Conclusions ................................................................................................... 188
7.2 — Recommendations ......................................................................................... 190
LIST OF REFERENCES .............................................................................................. 191
APPENDIX ................................................................................................................... 203
Appendix A - Experimental Data .............................................................................. 203
Raw Results .............................................................................................................. 203
Appendix B - Repeatability ....................................................................................... 243
Vita - Biographical Sketch ............................................................................................ 245


---


## Page 12


x
LIST OF TABLES
Table 1: Advantages of AM (Durakovic, 2018) .............................................................. 19
Table 2: Large Economies and Number of COVID-19 Cases (WHO, 2020) ................. 29
Table 3: JAMA Summary of Recommendations for PPE Conservation and Management
(Livingston, Desai, & Berkwits, 2020) ............................................................................ 33
Table 4: List of Various Parameters from Previous Studies (Dey & Yodo, 2019) .......... 46
Table 5: Low and High Print Parameters ..................................................................... 101
Table 6: Experimental Schedule .................................................................................. 102
Table 7: Use Case Experimental Schedule ................................................................. 110
Table 8: Sample Results from CR-6 SE ....................................................................... 112
Table 9: Sample Results from Sidewinder X1 .............................................................. 113
Table 10: Combined Results for the CR-6 SE ............................................................. 120
Table 11: Average Quality Scores for the CR6 ............................................................ 128
Table 12: Average Quality Scores for the SWX1 ......................................................... 129
Table 13: Raw Results for the CR-6 SE ....................................................................... 203
Table 14: Raw Results for the SWX1 ........................................................................... 208
Table 15: Cost+Power Results for the CR-6 SE .......................................................... 213
Table 16: Cost+Power Results for the SWX1 .............................................................. 218
Table 17: Rework Results for the CR-6 SE .................................................................. 223
Table 18: Rework Results for the SWX1 ...................................................................... 228
Table 19: Quality Score Card for the CR6 ................................................................... 233
Table 20: Quality Score Card for the SWX1 ................................................................ 238


---


## Page 13


xi
LIST OF FIGURES
Figure 1: Example of the Typical 3DP workflow for a maker ........................................... 4
Figure 2: New Workflow to Integrate Optimization ........................................................... 5
Figure 3: Face Shield Components ................................................................................ 11
Figure 4: Diagram of Problem ........................................................................................ 14
Figure 5: Example of the Typical 3DP workflow for a maker ......................................... 42
Figure 6: Face Shield Components ................................................................................ 43
Figure 7: Breakdown of Characteristics vs Parameters (Dey & Yodo, 2019) ................ 50
Figure 8: Examples of Process Parameters (Mohamed, Masood, & Bhowmik, 2018) .. 51
Figure 9: Examples of Width and Angle Parameters (theone8480, 2018) ..................... 52
Figure 10: Diagram of FDM Printer (Zaharin, Rani, & Ginta…, 2018) ........................... 53
Figure 11: Example of the Typical 3DP Workflow for a Maker ....................................... 57
Figure 12: Diagram of the Problems Outline in this Research ....................................... 60
Figure 13: Sample Aesthetic Scoring Form ................................................................... 66
Figure 14: Example OLS Results ................................................................................... 77
Figure 15: 𝜖-Constraint Workflow (Wattanasaeng & Ransikarbum, 2021) ..................... 79
Figure 16: Steps in the Visual Inspection ....................................................................... 86
Figure 17: Visual Inspection (Aesthetics) Score Card .................................................... 88
Figure 18: Index Mold .................................................................................................... 90
Figure 19: Image of Headband Measurements (Measure 1) ......................................... 91
Figure 20: Image of Headband Measurements (Measure 2 and 3) ............................... 92
Figure 21: Breakdown of Characteristics vs Parameters (Dey and Yodo, 2019) ........... 98
Figure 22: New Workflow to Integrate Optimization ....................................................... 99


---


## Page 14


xii
Figure 23: Initial APSU Face Shield based on the Prusa RC 1 Headband .................. 105
Figure 24: Face Shield Components ............................................................................ 106
Figure 25: TEMA Picking Up a Shipment of Face Shields ........................................... 108
Figure 26: Print with Brim ............................................................................................. 111
Figure 27: Sample Inspection Score Card ................................................................... 117
Figure 28: Index Mold .................................................................................................. 118
Figure 29: Highlighted Rows Demonstrate Differences in Raw Cost And Time Vs Those
Including Rework Factors for the CR6 ......................................................................... 124
Figure 30: Highlighted rows demonstrate differences in raw cost and time vs those
including rework factors for the SWX1 ......................................................................... 125
Figure 31: Image of the Unusable Headband .............................................................. 127
Figure 32: Analysis A - CR6 Cost OLS ........................................................................ 131
Figure 33: Analysis A - CR6 Reduced OLS for Cost .................................................... 132
Figure 34: Analysis A - CR6 Time OLS ........................................................................ 134
Figure 35: Analysis A - CR6 Reduced OLS for Time ................................................... 135
Figure 36: Analysis A - SWX1 Cost OLS ..................................................................... 139
Figure 37: Analysis A - SWX1 Reduced OLS for Cost ................................................. 141
Figure 38: Analysis A - SWX1 Time OLS ..................................................................... 142
Figure 39: Analysis A - SWX1 Reduced OLS for Time ................................................ 144
Figure 40: Analysis B - CR6 Cost OLS ........................................................................ 147
Figure 41: Analysis B - CR6 Reduced OLS for Cost .................................................... 148
Figure 42: Analysis B - CR6 Time OLS ........................................................................ 150
Figure 43: Analysis B - CR6 Reduced OLS for Time ................................................... 151


---


## Page 15


xiii
Figure 44: Analysis B - SWX1 Cost OLS ..................................................................... 155
Figure 45: Analysis B - SWX1 Reduced OLS for Cost ................................................. 156
Figure 46: Analysis B - SWX1 Time OLS ..................................................................... 158
Figure 47: Analysis B - SWX1 Reduced OLS for Time ................................................ 159
Figure 48: Analysis C - CR6 Cost OLS ........................................................................ 164
Figure 49: Analysis C - CR6 Reduced OLS for Cost ................................................... 165
Figure 50: Analysis C - CR6 Time OLS ....................................................................... 166
Figure 51: Analysis C - CR6 Reduced OLS for Time ................................................... 167
Figure 52: Analysis C - SWX1 Cost OLS ..................................................................... 171
Figure 53: Analysis C - SWX1 Reduced OLS for Cost ................................................ 172
Figure 54: Analysis C - SWX1 Time OLS .................................................................... 173
Figure 55: Analysis C - SWX1 Reduced OLS for Time ................................................ 175
Figure 56: CR6 Cura Preview at 35 of 71 Layers ........................................................ 179
Figure 57: CR6 Cura Time Estimate ............................................................................ 180
Figure 58: Section Requiring Cut and Paste to add Linear equation to python function
 ..................................................................................................................................... 186


---


## Page 16


xiv
ABBREVIATIONS
List of Key Abbreviations
•
3D - Three-Dimensional
•
3DP - Three-Dimensional Printing
•
aid - Actual Infill Density
•
alh - Actual Layer Height
•
AM - Additive Manufacturing
•
ANOVA - Analysis of Variance
•
aps - Actual Print Speed
•
arw - Actual Raster Width
•
awt - Actual Wall Thickness
•
CAD - Computer Aided Design
•
CR6 - Creality CR6 SE Printer
•
DOE - Design of Experiments
•
FDM - Fused Deposition Modeling
•
id - Infill Density
•
lh - Layer Height
•
OLS - Ordinary Least Squares Regression
•
PLA - Polylactic Acid Filament
•
PPE - Personal Protective Equipment
•
ps - Print Speed
•
RC - Release Candidate


---


## Page 17


xv
•
RSM - Response Surface Methodology
•
rw - Raster Width
•
SWX1 - Artillery Sidewinder X1 Printer
•
TEMA - Tennessee Emergency Management Agency
•
THEC - Tennessee Higher Education Commission
•
wt - Wall Thickness


---


## Page 18


1
1 — CHAPTER ONE - INTRODUCTION AND GENERAL
INFORMATION
1.1 — INTRODUCTION TO AM
Traditional manufacturing utilizes subtractive processes. The part geometry is created
by removing material. Subtractive processes include injection molding, metal casting,
and conventional machining processes (Bhushan & Caspers, 2017). Although there are
numinous types of additive manufacturing (AM), commonly referred to as 3D printing,
most methods deposit a material and build an object layer-by-layer (Yoon et al., 2014).
Typically, a model of the object is created is a computer aided design (CAD) software.
This model is then “printed”.
AM can be utilized for a wide range of manufacturing initiatives; current literature
highlights several applications. According to (Ngo, Kashani, Imbalzano, Nguyen, & Hui,
2018), there are several trending applications for AM. These applications include:
•
Biomaterials
•
Aerospace
•
Buildings
•
Protective Structures
AM offers several benefits over traditional manufacturing. These benefits include:
•
Reduced Materials (Bhushan & Caspers, 2017)


---


## Page 19


2
•
Rapid Prototyping - the results of a print test is an actual part (Kruth, Mercelis,
Van Vaerenbergh, Froyen, & Rombouts, 2005)
•
Multi-material parts and biomedical objects including organs (Bose, Vahabzadeh,
& Bandyopadhyay, 2013)
•
Idea for Small orders (Bhushan & Caspers, 2017)
Although AM is a promising technology, it has several drawbacks. As noted previously,
AM can be efficient and cost effective for small orders. Because of excessive print
times, AM can be less effective that traditional manufacturing. The layer-by-layer
approach to AM can also be problematic in terms of quality control (Bhushan &
Caspers, 2017), cost control, and large volume projects.
AM offers the manufacturing industry many benefits both economically and in
processing. Of particular interest is the usage of 3D printers to create prototypes and for
small-scale production.
With the rise in AM, the number of hobbyist/prosumer 3D printers available. This
availability coincides with the maker movement.
1.2 — THE MAKER COMMUNITY AND COVID-19
The description of the maker movement is broad. The definition is based on an
individual’s ability to be a creator of things. This individual is a maker. This growing
community of hobbyists and professionals with diverse skills, backgrounds, and
interests make their own functional devices. These devices can be technological, or
craft based, such as home decor (Papavlasopoulou, Giannakos, & Jaccheri, 2017).


---


## Page 20


3
By using shared tools, technology, and experience makers have the potential act as
producers in the sharing economy. Makers can also increase entrepreneurship,
advanced manufacturing, and spur economic growth (Browder, Aldrich, & Bradley,
2019).
According to Browder et al. (2019), three features set the maker movement apart from
past eras of craft making:
 “(1) a high level of social exchange and collaboration among diverse actors, (2)
enhanced knowledge creation and sharing in physical or virtual spaces, and (3) the
production of material artifacts using technological resources previously restricted to
corporate research and development (R&D) facilities”
When 3D printers are used by hobbyists, makers, and enthusiast, most use a typical
workflow (Figure 1). The decision on a successful print is a visual inspection. A visual
inspection is subjective and makes true optimization difficult.
The maker community can be limited by the lack of printable material. Traditional
Design of Experiments (DOE) requires numerous runs and samples to identify an
optimal solution. For example, to investigate optimizing for quality, cost, and speed
using 4 print parameters, approximately 160 models would need to be printed. In a
setting outside of industry. This is a prohibitive cost. A new workflow is described in
Figure 2.


---


## Page 21


4

Figure 1: Example of the Typical 3DP workflow for a maker


---


## Page 22


5

Figure 2: New Workflow to Integrate Optimization


---


## Page 23


6
A methodology is required to allow makers to incrementally optimize the print process
while at the same time being cost effective and conducive to the continued use of a
visual inspection. The use of the augmented Epsilon-Constraint method is a possible
solution. This methodology can offer makers the ability to optimize and can be
particularly important considering such issues as this created by COVID-19.
1.3 — COVID-19 AND SUPPLY ISSUES
In 2019 the first cases of the novel coronavirus (2019-nCoV) or the severe acute
respiratory syndrome corona virus 2 (SARS-CoV-2), commonly known as COVID-19,
were reported in Wuhan City of Hubei Province of China (Singhal, 2020). The virus
primarily targets the human respiratory system. The most common COVID-19
symptoms are fever, cough, sore throat, fatigue, muscle/body/headaches, new loss of
taste or smell, congestion or runny nose, nausea or vomiting, and diarrhea (CDC,
2020). The symptoms range from mild to severe. At present, COVID-19 is particularly
deadly for those with compromised immune systems and those over 70 years of age.
Examples of a “compromised immune system” includes individuals with hypertension,
diabetes, cardiovascular disease, and malignancy. The literature currently estimates
that approximately 20% of patients develop severe respiratory illness, with the overall
mortality between 2-4% (Shi et al., 2020), (Sohrabi et al., 2020).
As of 5 March 2020, 7 of the hardest hit countries from COVID-19 were the US, China,
Japan, Germany, Britain, France, and Italy (Baldwin & Mauro, 2020). According to
Baldwin and Mauro (2020), these countries account for the following:
•
60% of world supply and demand (GDP)


---


## Page 24


7
•
65% of world manufacturing
•
41% of world manufacturing exports
As of June 2020, unemployment in the US is approximately 11%. As a comparison, the
rate is over 7% higher than the previous June (BLS, 2020). Initial social distancing
efforts exacerbated already tight supplies of PPE. Baldwin and Mauro (2020) describe
the “triple hit” on world manufacturing:
1.
Direct supply disruptions have hindered production is industrial powerhouses of
China, USA, and Germany.
2.
The supply-chain has faced “supply-chain contagion” as direct supply shocks.
Manufacturers in less hard-hit nations find it harder and more costly to acquire
imported industrial outputs.
3.
Demand disruptions caused by drops in aggregate demand and “wait-and-see”
spending by consumers and industry.
Overall, the effects on global industry and the rapid growth in COVID-19 cases created
shortages in many goods including PPE.
1.3.1 — SUPPLIES OF PPE
China represents much of the world’s personal protective equipment (PPE) production.
In the case of the United States, 48% of all PPE used is sourced from China. In January
and February, production from China dipped 15% (Bown, 2020). PPE shortages have
been documented accrues the globe, including in the US, Italy, South Korea, and the
United Kingdom (Emanuel et al., 2020). Innovative solutions are required to mitigate this
shortfall. Additive manufacturing is one such solution.


---


## Page 25


8
The maker community and makerspaces could provide the resources needed to meet
the PPE supply shortfalls caused by COVID-19.
During the COVID-19 pandemic there have been numinous instances of makers
assisting with the production of medical supplies. These ad hoc efforts to supply PPE
are just a small example of maker efforts happening across the globe. In most cases,
the efforts were spontaneous and lacked centralized coordination an optimization. An
important component of future endeavors would be the optimization of production.
Techniques developed in the field of Industrial Engineering could be integrated into
maker efforts to streamline processes and maximize output.
1.4 — OPTIMIZATION
“Tennessee colleges are teaming up to mass produce face shields for medical workers
battling the coronavirus outbreak. In days, colleges throughout the state have used 3D
printers to produce more than 1,500 pieces of personal protective equipment, with plans
to create thousands more. Hospitals are clamoring for masks, face shields and other
tools as the explosive spread of COVID-19 continues to strain their supply chains.” -
Adam Tamburin, Tennessean, 2020
It is estimated that there are 47,000 3D printers in the United States (US) (Feldman,
2020). Many of these printers became inactive as companies and organizations
transitioned to work-from-home and social distancing in the wake of COVID-19
(Feldman, 2020). This number does not include maker owned 3D printers. It is
estimated that there are at least 300 publicly accessible makerspaces, libraries,


---


## Page 26


9
YMCAs, community colleges, and universities (Holman, 2015). Many organizations
used the idle printers to answer the PPE shortage.
With the growing shortage of PPE, many organizations and individual makers began
producing PPE to meet demand. Novak and Loy (2020) identified many of the early
production projects in February and March 2020. The researchers identified over 91
maker projects of which 60% were producing PPE (Novak & Loy, 2020a). The PPE
beginning produced included:
•
Face Shields (62%)
•
Masks (20%)
•
Goggles (9%)
•
Mask Adjusters (5%)
•
Other (4%)
Universities in Tennessee participated in the production of PPE. In the case mentioned
in the Tennessean (2020), “Tennessee colleges mass producing face shields to guard
against coronavirus using 3D printers”, the Tennessee Universities were producing PPE
face shields. In all, over 18,000 face shields were produced.
The mobilization of the maker community can be considered a bright spot in perilous
times of the COVID-19 pandemic. Many of the 3D models utilized to produce PPE
require hours to print (Tino et al., 2020). Even with multiple printers, the previously
mention TN project was limited by the print time of the face shields. The face shields
typically took between 1.5 to 3.5 hours to print (Wesemann, Pieralli, Fretwurst, Nold, &
Nelson…, 2020). Optimization could be used to increase the throughput of shields while


---


## Page 27


10
at the same time maintaining quality and limiting the materials and labor required to
complete a build.
1.4.1 — MAKERS AND OPTIMIZATION
Makers across the globe have utilized 3D printers to meet the PPE challenges posed by
COVID-19. In the case of face shields, there is a vast array of models and versions
available for maker production. Added to these selections are the numerous options for
FDM printers. Selecting a model, best suited for a given printer can be challenging. The
choices with this selection have an overall effect on the throughput of a project and is
particularly critical during a disaster. Utilizing various industrial engineering
methodologies, it is possible to improve throughput while at the same time retaining
quality and keeping costs down. This study will focus on the optimization of the
production of face shields (Figure 3).
1.4.2 — OVERVIEW OF A FACE SHIELD
A face shield (Figure 3) is composed of a FDM printed frame, a piece of elastic, and a
cut sheet of clear acetate.
The most time consume component of production is the frame.
1.4.3 — DISCUSSION OF VARIABLES
To optimize throughput several variables, need to be investigated (Popescu, Zapciu,
Amza, Baciu, & Marinescu, 2018). Throughput, cost, and quality can all be affected
through the manipulation of various 3D print parameters. Some examples include:


---


## Page 28


11

Figure 3: Face Shield Components


---


## Page 29


12
•
Slicing Parameters - includes a variety of variables including infill, layer height,
nozzle diameter, etc.
•
Build Orientation - Fit of the frame on the build surface
•
Temperature Conditions
The study “Parametric Analysis of the Build Cost for FDM Additive Processed Parts
Using Response Surface Methodology” (Mohamed, Masood, & Bhowmik, 2016b)
identifies a cost model that is applicable for determine the cost for printing FDM parts.
The model developed is:
𝐵!"#$ = 𝐶% + 𝐶& + (𝑀' + 𝑇()*+,)
Where:
•
𝐵!"#$ = Build cost ($)
•
𝐶% = Model material cost ($)
•
𝐶& = Support material cost ($)
•
𝑀' = Machine running cost (Hour)
•
𝑇()*+, = Built time (Hour)
To complete this formulation, the various FDM input factors will need to be identified. In
the case of Mohamed et al (2016), the following inputs selected were:
•
Layer thickness
•
Air gap
•
Raster angle
•
Build orientation


---


## Page 30


13
•
Road width
•
Number of contours
This study will review various studies and identify the ideal FDM input factors. The
independent variables will be identified and used as a starting point to identify other key
independent variables. The selection of variables will also be influenced by the various
slicer programs typically used by makers, with a focus on the free/open-source tools.
Various levels of the variables can be tested to identify the cost production variables.
Design of experiments and ANOVA will be utilized to test the results. A quadratic
equation can then be used to optimize the build variables to lowest cost.
1.5 — CHAPTER 1 SUMMARY
The various methodologies for optimization are ideal for researchers but are outside of
the experience and knowledge of the typical maker. This study will focus on the use of
easy to understand and accessible optimization techniques. Figure 4 represents the
various problems outlined previously.


---


## Page 31


14

Figure 4: Diagram of Problem


---


## Page 32


15
2 — CHAPTER TWO - LITERATURE REVIEW
2.1 — 3DP INTRODUCTION
Traditional manufacturing utilizes subtractive processes. The part geometry is created
by removing material. Subtractive processes include injection molding, metal casting,
and conventional machining processes (Bhushan & Caspers, 2017). Although there are
numinous types of 3D printing (3DP) processes, most methods deposit a material and
build an object layer-by-layer (Yoon et al., 2014). Typically, a model of the object is
created is a computer aided design (CAD) software. This model is then “printed”.
Some of the first patents for 3D printing technologies were granted in the 1970s
(Bradshaw, Bowyer, & Haufe, 2010b). At present there is a wide range of available 3D
printing technologies. With the growth in the industry 3D printing devices, machines
previously only available to industry have begun to appear is in universities and private
citizen’s garages (Ludwig, Stickel, Boden, & Pipek, 2014). As noted by Ludwig et
al. (2014):
“…entry level 3D printers and machines such as RepRaps or MakerBots have become
more and more common in various professional and non-professional settings such as
universities and small businesses as well as in the hobbyist and semi-professional
Maker scene.”
In this research, 3DP will be reviewed based on two subcategories additive
manufacturing (AM) and the prosumer 3D printing (P3D). The AM will be used to


---


## Page 33


16
describe the professional 3D printing industry and Industrial and manufacturing
processes. P3D will be used to refer to the semi-professional market, hobbyists,
university, and school 3DP.
2.1.1 — HISTORY OF 3DP
The initial 3D printers were valued as rapid prototyping tools. Not only could a part be
modeled, but once printed the result was the actual part. At present, AM is often used
for small batch products that would require extensive machining for traditional
manufacturing techniques.
The first commercial use of additive manufacturing in 1987 by the company 3D
Systems. 3D Systems’ SLA-1 was a stereolithography (SL) system that used a laser to
solidify thin layers of ultraviolet (UV) light-sensitive liquid polymer (Wohlers & Gornet,
2014).
In the 1990s, several new AM technologies were commercialized (Wohlers & Gornet,
2014). These included:
•   Fused Deposition Modeling (FDM) from Stratasys
•   Solid Ground Curing (SGC) from Cubital
•   Laminated Object Manufacturing (LOM) from Helisys
•   Selective Laser Sintering (SLS)
In Fused Deposition Modeling (FDM), a plastic material, in filament form, is extruded
through a nozzle that contains resistive heaters. As the nozzle traces the part’s cross-


---


## Page 34


17
sectional geometry, the melted material is deposited layer-by-layer (Novakova-
Marcincinova & Kuric, 2012).
With Solid Ground Curing (SGC) also known as Resin Printers, each layer is generated
by creating a negative image mask of the cross section of the part on an
electrostatically charged glass plate. a thin layer of UV-sensitive liquid polymer is
spread across the surface of the workspace. The workspace is then flooded with UV
light creating a layer in one pass (Gu, Zhang, Zeng, & Ferguson, 2001).
Laminated Object Manufacturing (LOM) can be considered a hybrid on additive
manufacturing. Layers are sequentially laminated together (additive) via adhesive
activated by a heating plate. Excess material is then cut away utilizing a special tool
(subtractive).
Selective laser sintering (SLS) uses thermal energy supplied by a laser to consolidate
successive layers of a power material. Each successive layer of the power material is
deposited, typically thickness of 20 till 150 µm, across the workspace. The laser traces
the part’s cross-sectional geometry and melts the powder in the path. The excess
powder is removed from the workspace (Kruth et al., 2005).
The methodologies listed previously represent the common 3D systems still in use.
Although LOM and SLS printers can cost in the hundreds of thousands, many FDM can
be purchased for under five hundred dollars.
The availability of these inexpensive systems has created a large hobbyist community
particularly for the FDM printing.


---


## Page 35


18
2.1.2 — INTRODUCTION TO AM
Additive Manufacturing (AM) utilizes processes to produce objects from digital models.
The models are rendered into a series of 2D cross-sections of a finite thickness. The
cross sections are fed into the AM machine, adding each layer-by-layer to produce the
finished object (Gibson, Rosen, & Stucker, 2014). The layering process defines the
geometry and the material properties of the object. The AM machine feedstock is
transformed via the AM process into the finished part (Thompson et al., 2016).
AM can be utilized for a wide range of manufacturing initiatives; current literature
highlights several applications. According to (Ngo et al., 2018), there are several
trending applications for AM. These applications include:
•
Biomaterials
•
Aerospace
•
Buildings
•
Protective Structures
There is rapid development of AM technologies. AM technology is continuously
improving with the ability to print end user designs using diverse metallic and
nonmetallic materials (Thompson et al., 2016). The literature notes many of the
advantages and benefits of AM over traditional manufacturing processes (Table 1).


---


## Page 36


19
Table 1: Advantages of AM (Durakovic, 2018)
Advantages
Explanation
Cost and
geometry
complexity
The cost of printing complex objects is cheaper than the cost of
printing simple designs AM allows designers to create complex
geometric shapes that are not possible using traditional
manufacturing
Functional
complexity
Besides printing single parts, with AM it is possible to create
functional objects. Examples could include gears, hinges, and
bicycle chains.
Material
complexity
AM allows a designer to create parts that are made from multiple
materials. This type of design allows for an object to have
different physical properties in specific areas.
Hierarchical
complexity
AM designs can utilize a variety of internal structure. These
structures allow for a part to have varied physical properties such
as strength, stiffness, and weight
Low
manufacturing
skills
The printing process is not complicated. To print, an individual
simply needs to be able to design a model. The availability of
pre-made models also lowers the need for training.
Reduced material
waste
AM only uses the material needed to print a model. AM
generates very little waste material


---


## Page 37


20
Table 1 Continued
Advantages
Explanation
Part and material
variety
A designer can alter an existing model to create parts that are
similar. The only requirement is CAD software.
Quality control
Quality control methodologies are well documented in the
literature.


---


## Page 38


21
Although AM and 3D printing is a promising technology, it has several drawbacks. As
noted previously, 3DP can be efficient and cost effective for small orders. Because of
excessive print times, AM can be less effective that traditional manufacturing. The layer-
by-layer approach to 3DP can also be problematic in terms of quality control (Bhushan
& Caspers, 2017), cost control, and large volume projects. The use of 3D printers in
homes and schools can also create problems with intellectual property (Nitti, 2019).
2.1.3 — TRENDS IN AM
The literature documents numerous uses for AM technology. The trending applications
(Ngo et al., 2018) in AM include:
•
Biomaterials
•
Buildings
•
Protective Structures
•
Aerospace
•
Low Cost 3DP
BIOMATERIALS
Biomaterials are defined as natural or synthetic materials that can be used in the repair
of damaged limbs and body parts by interacting with living body. In (Bose, Ke,
Sahasrabudhe, & Bandyopadhyay, 2018), the example of a total hip replacement is
described. With traditional manufacturing techniques, a hip replacement requires a
complex combination of materials and structures. To achieve this blend, multiple steps
are required. Once manufacturing is complete, post-processing steps are often


---


## Page 39


22
required. In all steps specific pattern making or tooling is needed which increases the
expense (Bose, Ke, Sahasrabudhe, & Bandyopadhyay, 2018).
AM is ideally suited for small, custom orders (Bhushan & Caspers, 2017). The typical
biomaterial pattern meets these criteria. Unlike traditional manufacturing where each
step creates expense, in AM the costs are associated with the cost of the AM machine
and the raw materials (Bose, Ke, Sahasrabudhe, & Bandyopadhyay, 2018). As noted by
Bose et al. (2018),
“Comparing the process setup, there are no costs involved in specific pattern making or
tooling. After AM based processing, machining may be needed to get the desired
surface finish. Key advantage towards AM of biomedical devices lies in patient-specific
device manufacturing. In some AM approaches, secondary processing such as
depositing a bio-ceramic coating on a metallic hip stem can also be integrated.”
BUILDINGS
The traditional construction industry faces numerous challenges including resources,
environmental, and productivity. The construction industry utilizes a considerable
quantity of resources and stresses the environment (Wu, Wang, & Wang, 2016). In the
United States, buildings use 36 percent of the total energy consumed, 30 percent of the
raw materials consumed and 12 percent of potable water (Klotz, Horman, &
Bodenschatz, 2007). Additionally, construction poses numerous productivity challenges.
In a comparison of the construction industry productivity in 20 countries, the United
States scored the worst (Nasir, Ahmed, Haas, & Goodrum, 2014).


---


## Page 40


23
In the research, several benefits of 3D printing in construction are noted (Wu, Wang, &
Wang, 2016). These benefits include:
•
Reduced Waste
•
Design Flexibility
•
Reduced Manpower
•
Other improvements in economic, environmental and constructability
These benefits directly address the challenges in the traditional construction industry.
PROTECTIVE STRUCTURES
A trending application of AM manufacturing includes the development of protective
structures. Examples of protective structures include vehicle and personal protection
armor. The ability to rapidly prototype complex structures allows researchers to explore
the protective properties of parallel panels filled with the most disparate lattice cores
and other novel snap-through concepts. This research is ideal for the development of
materials with high stiffness-to-weight and strength-to-weight ratios (Ngo et al., 2018).
An interesting trend in protective structure research is the investigation of bio-inspired
design (BID). BID looks at protective structures in nature such as fish scales, fruit peels,
abdominal armor, and bones to create protective structures. AM processes are ideal for
the creation of these complex structures (Mehta, Ocampo, Tovar, & Chaudhari, 2016).


---


## Page 41


24
AEROSPACE
The aerospace industry requires strong, light, and durable components. Additive
manufacturing is ideally suited to meet these requirements. It is estimated that the
aerospace industry currently accounts for over 12% of global additive manufacturing
applications. At present AM in aerospace is a $1.5 billion dollar industry. It is expected
to grow to $100 billion in the next 20 years (Kumar & Nair, 2017). Although rapid
prototyping is a common aerospace use case, metallic AM processes are often used for
end-use parts. With metallics, much of the research focuses on Powder Bed
Technologies and Deposition Technologies (Dordlofva, Lindwall, Torlind, & others,
2016). AM is an ideal fit for aerospace due to the need for complex components in low
volumes (Gibson, Rosen, & Stucker, 2010). This is demonstrated by the fact that the
international space station has a 3D printer for creating parts and components as
needed (Tofail et al., 2018).
A critical challenge in utilizing AM in aerospace is that of variation. Variation is AM
produced products include those observed from part-to-part as well as machine-to-
machine. It is critical to identify and minimize variations including internal defects,
surface roughness and geometry tolerances (Dordlofva, Lindwall, Torlind, & others,
2016).
LOW-COST 3D PRINTING
Adrian Bowyer in 2004 realized that fused filament deposition (FDM) 3D printing
provides the opportunity to manufacture a significant portion of its own parts. From this
realization, the Replicating Rapid- prototype (RepRap) community was born. RepRap is


---


## Page 42


25
currently a collection of open-source design, software, and hardware. Although RepRap
printers have a slightly lower quality that commercial units, RepRap Based devices are
a fraction of the cost (Bradshaw, Bowyer, & Haufe, 2010b).
The cost (and usability) of RepRap based 3D printers has dropped significantly. For
under five hundred dollars, a user can purchase a machine for home use. While costs
for devices have fallen, there has been an exponential growth of databases for printable
objects (Halassi, Semeijn, & Kiratli, 2019). These databases are repositories of pre-built
items (models) that can be printed. In many cases, these models are free and open-
source. With the open-source models, a user can make changes and customize the
items for their direct use case. A consumer that is now also a producer can be called a
“prosumer” (Rayna, Striukova, & Darlington, 2015). According to Rayna et al., (2015),
“One of the most obvious consequences for businesses of the advent of Internet is the
increased participation of users in the production process. This increased participation
has been particularly visible since the birth of Web 2.0 technologies and for some of the
most successful Web 2.0 outlets (e.g. Facebook, Instagram, Flickr, Twitter), the content
provided by users accounts for most of the value of the service. This increased user
participation blurs the line between consumption and production activities since users
both consume and produce content. No longer ‘pure’ consumers, users have become
prosumers.”
With the growth of school and home 3D printers (Bradshaw et al., 2010b), the usages
include the following:
•
Spare Parts


---


## Page 43


26
•
Craft and Hobby Items
•
Educational Instruction
•
Prototyping
•
Fashion Related Items
•
Maker Spaces
RepRap based printers have led the development of various tools and processes to
design and print models.
2.1.4 — 3D PRINTING TOOLS AND TERMINOLOGY
The RepRap based 3DP stack includes the following components:
•
Firmware - is the software that works with the printer microcontroller (Romero et
al., 2014). The firmware computes and controls the movements of the printer,
sensors, and heaters, by interpreting a sliced model. There are several
alternatives firmware alternatives, these include Sprinter, Teacup, and Marlin.
Marlin is the most used firmware for the prosumer 3D printer (Stănciulescu,
Schulze, & Wąsowski, 2015).
•
Printer Controller - The print controller represents the interface for the user to
interact with the printer. It allows the user to issue commands, set temperatures,
set speed, and send files to print (Stănciulescu, Schulze, & Wąsowski, 2015).
•
GCODE Generator - Commonly referred to as a “slicer”, the GCODE generator
transforms a model into GCODE for printing. The GCODE can then be
transferred to the machine, controls the speed of extrusion, optimizes the tool
path for printing and controls the orientation of the object and the formation of


---


## Page 44


27
layers (Šljivic, Pavlovic, & Kraišnik…, 2019). There are numerous slicer
programs available including commercial and open-source products.
SLICING SOFTWARE
As noted by Baumann et al. (2016), the typical 3DP workflow includes the following:
•
Creating (or downloading) and exporting the 3D model to print. The format of the
exported or downloaded model is commonly standard tessellation language
(STL) format.
•
Calculation of the printer tool path and characteristics based on the sliced STL
file. The sliced file is in GCODE format.
•
Printing based on the GCODE file.
The slicing software or slicer is used to convert a model to control commands suited for
the 3D printer. It should be noted that the GCODE commands are 3D printer specific. A
slicer must be configured to produce GCODE for the printer to be used (Baumann,
Schuermann, Odefey, & Pfeil, 2017).
There are numerous commercial and free slicers available. Some of them include:
•
Simplify3D (Commercial)
•
PrusaSlicer (Open-Source, Free)
•
Slic3r (Open-Source, Free)
•
UltiMaker Cura (Open-Source, Free)
Ultimaker Cura, referred to as Cura is one on the most popular slicers available. It offers
a robust set of features and supports numerous 3D printers. The printer support is in the


---


## Page 45


28
form of profiles. Each printer profile is a set of community tested print parameters ideally
suited for a printer’s hardware. The feature set of Cura allows the user to control and
change numerous 3DP parameters. These changes are reflected in the resultant
GCODE.
2.1.5 — AM SUMMARY
AM offers the manufacturing industry many benefits both economically and in
processing. Of particular interest is the usage of 3D printers to create prototypes and for
small-scale production. These uses, particularly in low-cost printing, are important. Low-
cost printing offers the ability of anyone to become a 3DP prosumer. Although this type
of printing is promising, there remains challenges for the prosumer/maker. One of the
significant challenges is that of optimization.
2.2 — PPE AND COVID-19
On 24 August 2020, the number of cases based on the largest economies is detailed in
Table 2.
As of June 2020, unemployment in the US is approximately 11%. As a comparison, the
rate is over 7% higher than the previous June (BLS, 2020). Initial social distancing
efforts exacerbated already tight supplies of PPE.
Baldwin and Mauro (2020) describe the “triple hit” on world manufacturing:
4.
Direct supply disruptions have hindered production is industrial powerhouses of
China, USA, and Germany.


---


## Page 46


29
Table 2: Large Economies and Number of COVID-19 Cases (WHO, 2020)
Country
GDP Manufacturing Exports Manufactured
Exports
COVID-19
Cases
Rank
US
24%
16%
8%
8%
5,612,163
1
China
16%
29%
13%
18%
90,182
33
Japan
6%
8%
4%
5%
62,507
44
Germany 5%
6%
8%
10%
233,575
19
UK
3%
2%
2%
3%
325,646
13
France
3%
2%
3%
4%
228,224
20
India
3%
3%
2%
2%
3,106,348
3
Italy
2%
2%
3%
3%
259,345
17
Brazil
2%
1%
1%
1%
3,582,362
2
Canada
2%
0%
2%
2%
124,629
25


---


## Page 47


30
5.
The supply-chain has faced “supply-chain contagion” as direct supply shocks
cause manufacturers in less hard-hit nations find it harder and more costly to
acquire imported industrial outputs.
6.
Demand disruptions due to drops in overall demand and “wait-and-see” spending
by consumers and industry.
China represents much of the world’s personal protective equipment (PPE) production.
In the case of the United States, 48% of all PPE used is sourced from China. In January
and February, production from China dipped 15% (Bown, 2020). PPE shortages have
been documented accrues the globe, including in the US, Italy, South Korea, and the
United Kingdom (Emanuel et al., 2020). Innovative solutions are required to mitigate this
shortfall. Without these solutions, rationing will become more prominent.
Transmission of COVID-19 to healthcare workers has been widely documented
(Singhal, 2020). PPE is critical to protecting both healthcare workers and patients. The
PPE should include contact and airborne precautions (Cascella, Rajnik, Cuomo, &
Dulebohn…, 2020). Specifically, PPE includes the following:
•
N95 or FFP3 masks
•
Eye Protection
•
Gowns
•
Gloves
2.2.1 — COVID-19 PREVENTION
Transmission of COVID-19 to health care workers (HCW) caring for the sick was
identified on 20th January 2020 (Singhal, 2020). Using history as a guide, 21% of all


---


## Page 48


31
those affected by the 2002 SARS outbreak were HCW workers (Chang, Xu, Rebaza,
Sharma, & Cruz, 2020). With the rapid spread of COVID-19, personal protective
equipment (PPE) for HCW is critical. The PPE should include contact and airborne
precautions (Cascella, Rajnik, Cuomo, & Dulebohn…, 2020). Specifically, PPE should
include the following:
•
N-95 or FFP3 masks
•
Eye Protection
•
Face Shields
•
Gowns
•
Gloves
COVID-19 has created shocks to the global economy. The demand and supply shocks
has impacted such industries as transportation, manufacturing, mining, and services
(Rio-Chanona, Mealy, & Pichler…, 2020). These shocks have put significant constrains
on the global supply of PPE and other medical supplies.
2.2.2 — AMERICAN MEDICAL ASSOCIATION IDEAS
According to the Journal of the American Medical Association (2020), the PPE shortage
is described in these terms:
“PPE, formerly ubiquitous and disposable in the hospital environment, is now a scarce
and precious commodity in many locations when it is needed most to care for highly
infectious patients. An increase in PPE supply in response to this new demand will


---


## Page 49


32
require a large increase in PPE manufacturing, a process that will take time many
health care systems do not have, given the rapid increase in ill COVID-19 patients.”
Which this in mind, JAMA issued a call for ideas to solve the PPE shortages on 20
March 2020 (Livingston, Desai, & Berkwits, 2020). The call received over 280,000 views
and 291 comments. Numerous ideas were shared including creating and repurposing
supplies using 3D printers (Table 3).
Rationing and the downgrade of safety regulations are a recipe for disaster. Two studies
from early in the pandemic show that 1% of HCW have been infected. Not all of these
HCW had previously worked with COVID-19 patients (Kluytmans-van den Bergh et al.,
2020) and (Lai et al., 2020). As of April 2020, an estimated 9,200 US HCW have been
infected with the virus.
Innovative solutions must be found to provide safe and effective PPE. The engagement
and use of makerspaces, university 3D print labs, and the DIY community offers a
possible path forward.
2.3 — THE MAKER COMMUNITY AND MAKERSPACES
The definition for the maker movement is broad. It is based on an person’s ability to be
a creator of things, This person is known as a maker. This growing community of
hobbyists and professionals with diverse skills, backgrounds, and interests make their
own functional products. These devices can be technological, or craft based, such as
home decor (Papavlasopoulou et al., 2017). According to Browder et al. (2019), the
maker movement differentiates itself by three features:


---


## Page 50


33
Table 3: JAMA Summary of Recommendations for PPE Conservation and Management
(Livingston, Desai, & Berkwits, 2020)
Domain Idea
Import


Purchase from international suppliers: China proposed as a primary market
given manufacturing capacity, experience with and decline in COVID-19
incidence
Reclaim

Dentists, farmers, construction, high schools, universities, veterinarians,
salons, manufacturing, aerospace, industrial “clean labs”

Individual HCW procurement in towns and communities

Charitable movements

Public or private buybacks

Public or private bounties
Reuse


Rotate through 72-h cycles given current understanding of surface viability

Reusable elastomeric respirators (have exchangeable filter cartridges)

Disinfectants

Heat (eg, autoclave), UV, ozone, ethylene oxide, hydrogen peroxide,
bleach, isopropyl alcohol, gamma or e-beam radiation, microwave, copper
sulfate, methylene blue with light, sodium chlorine, iodine, zinc oxide
impregnation (gowns), hypochlorous acid, commercial laundering (for cloth)


---


## Page 51


34
Table 3 Continued
Domain
Idea
Repurpose


Prefabricated masks: snorkel and scuba, 3D printed, welder’s,
civilian military grade gas masks, ski buffs

Eye and face shields: sports eye protectors, motorcycle helmets
with visors, balaclavas

Gowns: plastic ponchos or poly bags, bedbug sheet material

Adhesive bandage as nasal PPE
Create supply


Sewn fabric masks and gowns, coffee filter masks, home HVAC
filter masks
Extend supply


Plastic face shields (water bottle cutouts, thermoplastic sheets,
A4 acetate sheets, Ziploc bags) to preserve face masks and
eyewear
Reduce
nonessential
services


Cancel elective and ambulatory procedures; reduce
questionable contact and isolation precautions (eg, MRSA/VRE,
influenza, cellulitis)


---


## Page 52


35
Table 3 Continued
Domain
Idea
Reduce patient
contact


Utilize mobile and out-of-room monitoring and device controls, e-
consults, extended dwell IVs, batching medications or self-
administration, barrier visits
Alter staffing


Reduce student and trainee patient contacts
Use nonhuman
services


Nonhuman services (drones and robots) for delivery of test kits for
self-testing, robots for equipment movement within hospitals,
decontamination protocols
Stratify use by
patient risk


Cohort patients and reduce PPE use for those at low risk (ideally
requires testing to accurately stratify low and high risk)
Employ immune
workers


---


## Page 53


36
Table 3 Continued
Domain
Idea

HCWs recovered from clinical illness or with demonstrated
immunity care preferentially for COVID-19 patients without PPE
Use government
solutions


Regionalize care and supply, import international supply, ration
supply, loosen import regulations, commandeer business to
accelerate supply
Manage supply


Reduce bulk packaging, Pyxis-like controlled distribution,
nongovernment regional coordination of PPE distribution
Miscellaneous


Convert RV trailers to negative pressure spaces; phase change
material to improve comfort and reduce reuse of gowns


---


## Page 54


37

•
A high level of collaboration and social exchange among a diverse community
•
Enhanced knowledge creation and sharing both physically and virtually
•
The production of material items using technology that had previously only been
the domain of corporate research and development (R&D) facilities
The diverse maker community is composed of includes do-it-yourself (DIY) hobbyists,
engineers, artists, hackers, students and educators, the self-employed, prototyping
entrepreneurs, technology and corporate innovators, and a new type of manufacturers
(Browder et al., 2019). A physical space for this community to share ideas is called a
“makerspace”.
A makerspace, sometimes referred to as a hackerspace or fablab, is a community
workshops where members can access tools and workspace. The benefit of the
makerspace is the shared access to expensive tools and human capital. This capital is
the sharing of knowledge and ideas (Holm, 2015). Makerspaces can be commercial
enterprises with membership fees, public spaces in libraries, or workshops in schools
designed for student access. In an informal 2015 survey, it was estimated that there are
at least 300 publicly accessible makerspaces in the United States. Furthermore 120,000
libraries, 2,600 YMCAs, and 1,200 community colleges provide access to other shared
resources (Holman, 2015). Additionally, makerspaces have been gaining popularity at
universities. The research has identified two significant benefits, the benefits of physical
modeling and the growth of communities of practice (Forest, Moore, Jariwala, &
Fasse…, 2014).


---


## Page 55


38
2.3.1 — THE MAKER COMMUNITY AND COVID-19
During the COVID-19 pandemic there have been numinous instances of makers
assisting with the production of medical supplies. Some examples include:
•
“This Is Truly a Last Resort. Makers Are 3D Printing Ventilator Parts and Sewing
Masks Amid a Critical Shortage in Medical Supplies” (Clark, 2020).
•
“Can The U.S. Crowdsource Its Way Out of a Mask Shortage? No, but it Still
Helps” (Westervelt, 2020)
•
“3D Printer Groups Continue Working Round the Clock to Help 2020 PPE
Shortage” (McCue, 2020)
•
“How Library Maker Spaces Can #FlattentheCurve” (Vecchione & Woltjer, 2020)
•
“Tennessee Colleges Mass Producing Face Shields to Guard Against
Coronavirus Using 3D Printers” (Tamburin, 2020)
These ad hoc efforts to supply PPE are just a small example of maker efforts happening
across the globe. In most cases, the efforts were spontaneous and lacked centralized
coordination and optimization. An important component of future endeavors would be
the optimization of production. Techniques developed in the field of Industrial
Engineering could be integrated into maker efforts to streamline processes and
maximize output.
2.4 — INTRODUCTION TO OPTIMIZATION
Optimization can be defined as “an act, process, or methodology of making something
(such as a design, system, or decision) as fully perfect, functional, or effective as
possible; specifically : the mathematical procedures (such as finding the maximum of a


---


## Page 56


39
function) involved in this” (Merriam-Webster, n.d.). In the case of design of experiments,
optimization is the process of determining the region in the important factors that will
lead to the best possible response (Montgomery, 2017). In the case of manufacturing, a
system must be characterized. Characterization is the process of the identification of the
factors that have the most influence on the response of interest (Montgomery, 2017). In
the case of makers responding to COVID-19 PPE shortages, the critical responses are
print speed, cost, and quality. In the following sections, this research will identify the
critical factors that contribute to the responses of speed, cost, and quality.
2.4.1 — OPTIMIZATION FOR MAKERS
It is estimated that there are 47,000 3D printers in the United States (US) (Feldman,
2020). This number does not include printers an estimated that there are at least 300
publicly accessible makerspaces, libraries, YMCAs, community colleges, and
universities (Holman, 2015). Many of these printers became inactive as companies and
organizations transitioned to work-from-home and social distancing in the wake of
COVID-19 (Feldman, 2020). Many organizations used the idle printers to answer the
PPE shortage.
With the growing shortage of PPE, many organizations and individual makers began
producing PPE to meet demand. Novak and Loy (2020) identified many of the early
production projects in February and March 2020. The researchers identified over 91
maker projects of which 60% were producing PPE (Novak & Loy, 2020a). The PPE
beginning produced included:
•
Face Shields (62%)


---


## Page 57


40
•
Masks (20%)
•
Goggles (9%)
•
Mask Adjusters (5%)
•
Other (4%)
“Tennessee colleges are teaming up to mass produce face shields for medical workers
battling the coronavirus outbreak. In days, colleges throughout the state have used 3D
printers to produce more than 1,500 pieces of personal protective equipment, with plans
to create thousands more. Hospitals are clamoring for masks, face shields and other
tools as the explosive spread of COVID-19-19 continues to strain their supply chains.” -
Adam Tamburin, Tennessean, 2020 (Tamburin, 2020)
Universities in Tennessee participated in the production of PPE. In the case mentioned
in the Tennessean (2020), “Tennessee colleges mass producing face shields to guard
against coronavirus using 3D printers”, the Tennessee Universities were producing PPE
face shields. In all, over 18,000 face shields were produced.
The mobilization of the maker community can be considered a bright spot in perilous
times of the COVID-19 pandemic. Several barriers remain for 3D printing to become a
permanent fixture in the PPE supply chain. These barriers include:
•
PPE Fit/Comfort
•
Regulations
•
Throughput
•
Geometry of Design


---


## Page 58


41
The most significant barrier is that of throughput and, to a lesser degree, geometry of
design (Novak & Loy, 2020b).
Many of the 3D models utilized to produce PPE require hours to print (Tino et al., 2020).
Even with multiple printers, the previously mention TN project was limited by the print
time of the face shields. The face shields typically took between 1.5 to 3.5 hours to print
(Wesemann et al., 2020). Optimization could be used to increase the throughput of
shields.
OPTIMIZATION FOR MAKERS
Makers across the globe have utilized 3D printers to meet the PPE challenges posed by
COVID-19. In the case of face shields, there is a vast array of models and versions
available for maker production. Added to these selections are the numerous options for
FDM printers. Selecting a model, best suited for a given printer can be challenging. The
choices with this selection have an overall effect on the throughput of a project and is
particularly critical during a disaster. Utilizing various industrial engineering
methodologies, it is possible to improve throughput while at the same time retaining
quality and reducing costs. The determination of quality is made via a visual inspection
Figure 5.
This study will focus on the production of face shields (Figure 3).
OVERVIEW OF A FACE SHIELD
A face shield (Figure 6) is composed of a FDM printed frame, a piece of elastic, and a
cut sheet of clear acetate.


---


## Page 59


42

Figure 5: Example of the Typical 3DP workflow for a maker


---


## Page 60


43

Figure 6: Face Shield Components


---


## Page 61


44
The most time consume component of production is the 3D printed frame.
2.4.2 — DISCUSSION OF PARAMETERS
To optimize throughput several variables must be investigated (Popescu et al., 2018).
These include:
•
Slicing Parameters - includes a variety of variables including infill, layer height,
nozzle diameter, etc.
•
Build Orientation - Fit of the frame on the build surface
•
Temperature Conditions
Each of the variables impacts the 3D print throughput as well as the frame quality.
There are several studies that have investigated the effect of these variables on FDM
printers. These include and are not limited to:
•
“A Systematic Survey of FDM Process Parameter Optimization and Their
Influence on Part Characteristics” (Dey & Yodo, 2019) - a review of various
process parameter studies.
•
“Build orientation analysis for minimum cost determination in FDM” (Ingole,
Deshmukh, Kuthe, & Ashtankar, 2011) - a study that attempts to develop a
universal cost model for varying geometries.
•
“Mathematical modeling and FDM process parameters optimization using
response surface methodology based on Q-optimal design” (Mohamed, Masood,
& Bhowmik, 2016a) - utilizes Q-optimal response surface methodology to
determine the functional relationship between the processing conditions and the
process quality characteristics.


---


## Page 62


45
•
“FDM process parameters influence over the mechanical properties of polymer
specimens: A review” (Popescu et al., 2018) - is a literature search identifying
various parameters and variable effecting cost.
•
“Design for Scalability and Strength Optimization for Components Created
Through FDM Process” (Qureshi, Mahmood, & Wong…, 2015) - a study that
uses Taguchi’s design of experiment to analyze the effect of these process
parameters on physical characteristics.
The identification of optimal print parameters is a significant problem for makers (Figure
4). Dey and Yodo, (2019) conducted an in-depth survey of various studies looking at
printing parameters and their effects on part characteristics (Table 4). This research will
serve as a basis for determine the process parameters to optimize for makers.
In the studies reviewed by Dey and Yodo, (2019) (Figure 7), the common variables
affecting build time and quality is layer thickness, print speed, infill density and raster
width. Layer thickness (Figure 8) is the thickness of a layer deposited by nozzle and is
affected by extrusion speed and can depend upon the type of the nozzle (Gurrala &
Regalla, 2012). Print Speed is the mm/s that the printer head deposits filament. Infill
density (or percentage) is the percentage of an infill pattern that fills voids in print. The
raster width is the thickness of lines in a print (Figure 9). Build orientation (Figure 8) is
the geometry of the model as it is printed on the build plate (Figure 10).


---


## Page 63


46
Table 4: List of Various Parameters from Previous Studies (Dey & Yodo, 2019)
Part Characteristics
Process Parameters
Strength
Build orientation and raster orientation
Elastic performance
Layer thickness, raster orientation, raster
width, air gap
Throwing distance of a bow
Layer thickness, raster orientation, raster
width, air gap
Residual stress and part distortion
Layer thickness, print speed, raster width
Ultimate tensile, yield, ﬂexural, and
impact strength
Raster orientation
Tensile, ﬂexural, and impact strength
Layer thickness, build orientation, raster
orientation, raster width, air gap
Tensile, ﬂexural, and impact strength
Layer thickness, build orientation, raster
orientation, raster width, air gap
Tensile, ﬂexural, and impact strength,
and deﬂection test
Raster orientation
Viscosity and modulus
Build style, raster orientation, raster width
Dynamic stress–strain response
Build orientation
Tensile strength and elastic modulus
Raster orientation and layer thickness


---


## Page 64


47
Table 4 Continued
Part Characteristics
Process Parameters
Build time, dimensional accuracy, warp
deformation
Width compensation, layer thickness,
extrusion velocity and filling velocity
Ultimate tensile strength, modulus of
elasticity, elongation
Raster orientation and layer thickness
Ultimate shear strength, 0.2% yield
strength, proportional limit, shear
modulus, and fracture strain
Layer thickness, infill density and
postprocessing heat-treatment time
Part cost, tensile, compressive and
ﬂexural properties
Infill Pattern
Tensile strength and fatigue
performance
Raster orientation
Tensile and shear properties
Raster Orientation and Build orientation
Young’s modulus, yield strength, tensile
strength, dimensional accuracy
Build orientation, infill density, print speed,
layer thickness, inﬁll thickness, infill pattern,
extrusion temperature
Tensile strength, failure strain, modulus
Poisson’s ratio, thermal expansion
Build orientation
Tensile, ﬂexural and impact strength
Build orientation, layer thickness, raster
orientation, raster width, air gap


---


## Page 65


48
Table 4 Continued
Part Characteristics
Process Parameters
Hardness, flexural modulus, tensile
tensile strength, and surface
roughness
Layer thickness, build orientation, support
material, model interior
Tensile, dynamic, and thermoelectric
properties
Inﬁll pattern and inﬁll density
Elongation, and tensile, flexural, and
impact strength
Print speed, layer thickness, extrusion
temperature, inﬁll temperature, infill density
Ultimate tensile and yield strength,
modulus of elasticity and elongation
Inﬁll density, extrusion temperature, raster
orientation, and layer thickness
Compressive properties, porosity
Air gap, raster width, build orientation, build
layer, and build profile
Build time, support material volume
Layer thickness, raster and build orientation,
raster width, shell
Impact strength
Build orientation
Storage modulus, Storage modulus,
loss modulus, mechanical dumping
Layer thickness, air gap, raster orientation,
build orientation, road width, and number of
shells
Layer height, raster height, width
Thermal conductivity


---


## Page 66


49
Table 4 Continued
Part Characteristics
Process Parameters
Tensile strength, strength, modulus of
rupture, impact resistance
Raster orientation
Build time and support volume
Layer thickness, air gap, raster and build
orientation, and shell width
Material volume
Layer thickness, air gap, road and shell
width
Lattice structure

Tensile strength, energy consumption
and build time
Extrusion temperature, raster orientation,
infill density


---


## Page 67


50


Figure 7: Breakdown of Characteristics vs Parameters (Dey & Yodo, 2019)


---


## Page 68


51



Figure 8: Examples of Process Parameters (Mohamed, Masood, & Bhowmik, 2018)


---


## Page 69


52


Figure 9: Examples of Width and Angle Parameters (theone8480, 2018)


---


## Page 70


53


Figure 10: Diagram of FDM Printer (Zaharin, Rani, & Ginta…, 2018)


---


## Page 71


54
2.4.3 — OPTIMIZATION SUMMARY
The various methodologies for optimization are ideal for researchers but are outside of
the experience and knowledge of the typical maker. This study will focus on the review
and identification of methods and processes that could be used by makers increase
throughput to meet supply shortfalls in a disaster. The literature demonstrates that
common factors that affect print speed, cost, and quality include:
•
layer thickness
•
print speed
•
infill density
•
raster width
It should be noted that a key component of the maker workflow is a visual inspection
Figure 5. This inspection is used to determine the quality of the printed object. An
overview of visual quality control can be found in the ~.• — Inspection for Quality
Control section.


---


## Page 72


55
3 — CHAPTER THREE - PROBLEM DEFINITION
3.1 — RESEARCH SCOPE
As noted previously, makers from across the globe have utilized 3D printers to meet the
PPE challenges posed by COVID-19. According to Salmi et al., (2020), some of the
items that were produced via 3DP include:
•
Testing Supplies
•
Ventilator parts
•
Face Masks
•
Face Shields
Salmi et al., (2020) estimates that the pandemic demand for face shields is in excess of
1 billion units. According to Novak and Loy (2020), from February to March 2020, 62%
of PPE projects were focused on the production of face shields. Of all the PPE project
surveyed, over 60% utilized FDM printers. In many cases, maker production
represented volunteer efforts to create PPE that was in short supply. The quick
production (throughput) of PPE was critical to alleviate short falls but because of the
strain on unpaid volunteers utilizing their own resources, it was critical to minimize the
need for materials (print stock) and cost on the maker community. Optimization could be
used to increase the throughput of shields while at the same time maintaining quality
and limiting the materials and cost required to complete a build.
This study is to focus on the adaptation of an optimization technique for injection
modeling to optimize FDM print parameters. The primary objective is to define an


---


## Page 73


56
optimization technique to maximize throughput while at the same time maintaining
quality, and cost reduction. A key component for the maker build process is a visual
inspection which is described in Figure 11.
As a secondary objective, this research will develop a methodology for scoring quality
based on functionality and surface quality. Finally, as a tertiary objective, the study will
structure the optimization model in an accessible manner for makers.
As stated previously, the primary objective is to increase throughput, while reducing
costs and maintaining an acceptable quality. Based on the work of Dey and Yodo,
(2019), there are numerous parameters that can affect quality, speed, and cost. Of
particular interest for this study are the following FDM process parameters including:
•
Layer Thickness - refers to the amount of material deposited by the FDM along
the vertical axis. The layer thickness is less that the nozzle diameter. The thicker
the layers, the faster the print speed. The thickness directly contributes to surface
roughness and build strength/flexibility (Solomon, Sevvel, & Gunasekaran, 2020).
•
Print Speed - is the speed of the nozzle as it traverses the build surface
depositing material (Solomon, Sevvel, & Gunasekaran, 2020). Besides
throughput, print speed has been found to have a significant impact on
deformation of the active layer (Kačergis, Mitkus, & Sinapius, 2019).
•
Infill Density - Solomon et al. (2020) states that, “Infill density denotes the
material volume printed on the given component. Infill density directly dominates
the printed component’s properties. Lesser density affects the mechanical
properties considerably whereas the denser component possesses better


---


## Page 74


57

Figure 11: Example of the Typical 3DP Workflow for a Maker


---


## Page 75


58
mechanical properties than the earlier one but needs more time to prepare the
component.”
•
Raster Width (Infill Line Width) - can be described as the tool path width of the
pattern used to fill the interior regions of a model (Gurrala & Regalla, 2012).
Raster width is particularly impactful on a part’s surface roughness (Patil, Singh,
Raykar, & Bhamu, 2021).
•
Wall Thickness - refers to the thickness of the external walls of a printed model.
This parameter can affect surface roughness, stability, and throughput (LIANG &
LI, 2017).
The following sections will describe the research problems addressed in this study and
will also describe the research methodology.
3.2 — PROBLEM DEFINITION
As manufactures have shut down or been disrupted by COVID-19 overall demand for
PPE and other medical equipment has skyrocketed while the availability of raw
materials has decreased and constrained production (Paul & Chowdhury, 2020). The
effects on global industry and the rapid growth in COVID-19 cases has created
shortages in many goods including PPE.
With the growing shortages of PPE, many organizations and individual makers began
producing PPE to meet demand. Most of the 3D models utilized to produce PPE require
hours to print (Tino et al., 2020). Face shields typically took between 1.5 to 3.5 hours to
print (Wesemann et al., 2020). In some cases, COVID-19 created delays in shipping of
3D filament. To meet PPE demand, it was critical to produce as many face shields as


---


## Page 76


59
possible with minimal material. Optimization could be used to increase the throughput of
shields while at the same time maintaining quality and limiting the materials and cost
required to complete a build.
For makers, there are several issues that can be identified when utilizing FDM printers
Figure 12. The issues can be categorized as primary and secondary problems and are
as follows:
•
Primary Problems - Speed, Cost, and Quality
1. What parameters should be optimized to increase speed, reduce costs,
and achieve satisfactory quality?
2. What is the contribution of each parameter to the increase speed,
reduce costs, and achieve satisfactory quality?
•
Secondary Problems
1. Because of the subjective nature of quality inspection, what is an
acceptable methodology to quantify the quality of a 3D printed model?
2. Accessibility of the optimization methodologies remains the domain of
engineers. Can the optimization method utilized in this study be made
accessible to makers?
3. Does the additive nature of FDM allow for the quick elimination of print
parameters?
3.2.1 — PRIMARY PROBLEMS
What parameters should be optimized to increase speed, reduce costs, and achieve
satisfactory quality?


---


## Page 77


60

Figure 12: Diagram of the Problems Outline in this Research


---


## Page 78


61
In the studies reviewed by Dey and Yodo, (2019) (Figure 7), the common variables
affecting build time and quality is layer thickness, print speed, infill density and raster
width. Layer thickness (Figure 8) is the thickness of a layer deposited by nozzle and is
affected by extrusion speed and can depend upon the type of the nozzle (Gurrala &
Regalla, 2012). Print Speed is the mm/s that the printer head deposits filament. Infill
density (or percentage) is the percentage of an infill pattern that fills voids in print. The
raster width is the thickness of lines in a print. Build orientation (Figure 8) is the
geometry of the model as it is printed on the build plate (Figure 10).
It is proposed that this research look at the effects of the following variables on print
speed and quality:
•
Layer Thickness
•
Print Speed
•
Infill Density
•
Raster Width
•
Wall Thickness
What is the contribution of each parameter to the increase speed, reduce costs, and
achieve satisfactory quality?
For this study, I propose that the methodology utilized by Tranter et al. (2017) (Figure 4)
with modifications to address research gaps identified by Dey and Yodo (2019). In the
study, Tranter et al. (2017) optimized for energy consumption and quality in injection
molding be adapted to optimizing for throughput, cost, and quality in FDM printing.


---


## Page 79


62
A study by Tranter et al., (2017) offers a possible solution developing a cost and quality
model that could be utilized by makers. The study is an investigation into the reduction
of energy consumption in injection molding while maintaining a part’s quality. According
to the paper the “work focused on study on the effects of selected process parameters
of the injection molding process on energy consumption and quality of the molded parts.
This is to achieve an optimal process parameter configuration that would reduce the
energy consumption, whilst still maintaining production of parts of good quality.”
The design of the experiment in the Tranter et al., (2017) paper utilized design of
experiments to test the design parameters to determine the relationship with the
process output. The study focused on the following:
•
A Melt Temperature, 𝑇-
•
B Mold Temperature, 𝑇-𝑜
•
C Holding Pressure, 𝑃.
•
D Holding Time, 𝑡ℎ
•
E Cooling Time, 𝑡𝑐
The researchers utilized a 2-level fractional factorial design in which process
parameters had a specified upper (+1) and lower (-1) levels. With 16 trails, the 25-1
design, no main effects were confounded with any other main effect or 2-factor
interaction. This allowed them to be estimated separately from one another without the
requirement for conducting a full factorial (32 trails) (Tranter, Refalo, & Rochman, 2017).
A total of 10 parts were created per trail.


---


## Page 80


63
Once the trials were completed, Analysis of Variance (ANOVA) was utilized to
determine the effects of the process parameters on the energy consumption. 5 of the 10
samples generated per trial were selected at random and then a quality determination
procedure was applied. ANOVA was employed again to determine the effects of the
process parameters on the part quality. Once the energy and quality data were
collected response optimization was used to jointly optimize the process parameters
(Tranter, Refalo, & Rochman, 2017).
The results of the research show that the outlined process can be used to optimize for
energy and quality. The researchers also state that their methodology could be used in
other studies using other materials and energy requirements (Tranter, Refalo, &
Rochman, 2017).
3.2.2 — SECONDARY PROBLEMS
Because of the subjective nature of quality inspection, what is an acceptable
methodology to quantify the quality of a 3D printed model?
For makers using FDM printing, the quantification of quality offers challenges, shown as
A in Figure 4. As noted previously, quality will be rated based on a visual inspection. In
the case of makers and low cost 3DP, the literature does not offer guidance for a
previously used system. As part of this work, a rating system will be developed. The
rating system will provide a unified methodology for scoring quality. This rating system
could be extended to other projects and uses.
Previous studies have used a visual inspection to check the functional and non-function
aspects of a 3D printed model (Ramananantoandro et al., 2014 and Li et al., 2017). The


---


## Page 81


64
functionality of a print can be considered an objective measurement. With the
production of face shields the 3D printed band is functional if it has both flexibility and
precision.
The band must be flexible to fit on a person’s head. A simple stretching of the band by
hand will suffice. Problems with the band could be inflexible or brittle. In either case,
• Flexibility - Band is flexible (ie it can fit on the head)
• Precision of print
The simplistic design of the face shield lends itself to a less rigorous need for exact
headband measurements and dimensions. Basically, a headband does not need to
have exact measurements to work. However, measurements should be considered as
part of the inspection process. To assess the measurements and dimensions of the
headbands, a stencil with flex marks will be created. The assessor can then compare
the headband to the stencil and use the flex marks as a means to determine
functionality. For the functionality of the band, characteristics 1-2 should be considered
binary.
In the case of aesthetics, a subjective assessment is required. This study will utilize a
visuotactile perception classification based on the work of Ramananantoandro et
al. (2014), an assessor classifies an object based upon a scale of 1-5(1 being the worst
value and 5 the best). The three characteristics to be classified are as follows:
•
Hedonic tactile appreciation - this characteristic is the preference of the object
based upon touch (Ramananantoandro, Larricq, & Eterradossi, 2014).


---


## Page 82


65
•
Tactile roughness perception - this characteristic is the determination of
roughness based upon touch (Ramananantoandro, Larricq, & Eterradossi, 2014).
•
Visual impression of roughness - this characteristic is the determination of
surface roughness based upon sight only (Ramananantoandro, Larricq, &
Eterradossi, 2014).
The scores will be captured via a “scoring card” (Figure 13).
Accessibility of the optimization methodologies remains the domain of engineers. Can
the optimization method utilized in this study be made accessible to makers?
As the proposed methodology (•.•.‚ — Primary Problems) is applied, efforts will be
made to allow makers to easily utilize the optimization process in future projects. Jupiter
Notebooks off a possible free and open-source solution to reproduce the methodology
in an accessible manner.
Does the additive nature of FDM allow for the quick elimination of print parameters?
“Everyone then who hears these words of mine and does them will be like a wise man
who built his house on the rock. And the rain fell, and the floods came, and the winds
blew and beat on that house, but it did not fall, because it had been founded on the
rock. And everyone who hears these words of mine and does not do them will be like a
foolish man who built his house on the sand. And the rain fell, and the floods came, and
the winds blew and beat against that house, and it fell, and great was the fall of it.”
Matthew 7: 24-27


---


## Page 83


66

Figure 13: Sample Aesthetic Scoring Form


---


## Page 84


67
FDM printing is additive in nature, the quote above regarding foundations has struck a
chord with me. I will be investigating the possibility that if a single print parameter can
cause a print to be non-functional or to be of poor quality be itself, will future
experimental runs that include that parameter with the same settings cause functionality
and quality issues in a run.
For example, it is proposed that this research look at the effects of the following
variables on print speed and quality:
•
Layer Thickness
•
Print Speed
•
Infill Density
•
Raster Width
•
Wall Thickness
In experiment Run 2, Layer Thickness is set to .28 and all other parameters are set to
the default. The prints from Run 2 are judged to be of poor quality. How is the quality of
any other runs that include the Layer Thickness set to .28? Can a single print
parameter, such as Layer Thickness be a foundation of sand?
3.3 — RESEARCH SCOPE AND DEFINITION SUMMARY
Research Scope
This research has several objectives, primary, secondary, and tertiary. The objectives
are as follows:


---


## Page 85


68
•
Primary - define an optimization technique to maximize throughput while at the
same time maintaining quality, and cost reduction.
•
Secondary - develop a methodology for scoring quality based on functionality
and surface quality.
•
Tertiary
–
Structure the optimization model in an accessible manner for makers.
–
Determine the possibility of eliminating print parameters from the
experimental design due to the additive nature of FDM.
To achieve the project objectives, this study will address the following research
problems.
Primary Problems - Speed, Cost, and Quality
Utilizing the research, several print parameters will be used to optimize FDM printing.
this research looks at the effects of the following variables on print speed and quality:
•
Layer Thickness
•
Print Speed
•
Infill Density
•
Raster Width
•
Wall Thickness
This work will represent the use of existing engineering approaches used in processes
outside of FDM, as identified in Tranter et al., (2017), to optimization while maintaining
quality in FDM printing. Additionally, rather than the use of response surface


---


## Page 86


69
methodology to determine the optimal settings, this study will use the numerical
optimization of 𝜖 -Contraint methodology.
Secondary Problems
Previous studies have used a visual inspection to check the functional and non-function
aspects of a 3D printed model (Ramananantoandro et al., 2014 and Li et al., 2017). This
study will lean on Ramananantoandro et al., (2014) and Li et al., (2017) to develop an
inspection methodology for FDM printing.
Accessibility of the optimization methodologies remains the domain of engineers. Can
the optimization method utilized in this study be made accessible to makers? This study
will utilize Jupiter notebooks as a method to make the various analysis more accessible.
Jupiter notebooks can be described as a document format for publishing code, results
and explanations in a readable form that can be executed (Kluyver et al., 2016). The
notebook is is designed to allow for reproducible computational workflows (Yin et al.,
2017). In the case of these experiments, the notebooks are designed to allow the
results to be calculated in a repeatable manner. Additionally, the notebooks will allow for
the results and code to be utilized in future research with minimal effort.


---


## Page 87


70
4 — CHAPTER FOUR - EXPERIMENTAL DESIGN AND
SOLUTION APPROACH
4.1 — DESIGN OF EXPERIMENT (DOE)
According to the “NIST/SEMATECH e-Handbook of Statistical Methods”, Design of
experiments (DOE) can be defined as:
“Design of experiments (DOE) is a systematic, rigorous approach to engineering
problem-solving that applies principles and techniques at the data collection stage so as
to ensure the generation of valid, defensible, and supportable engineering conclusions.
In addition, all of this is carried out under the constraint of a minimal expenditure of
engineering runs, time, and money.”
DOE can be categorized in 4 general engineering domains (Natrella, 2010). The
domains include:
•
Comparison - the researcher is interested in how changes in a single variable
affect the system.
•
Screening and Characterization - this process allows the researcher to
understand the system. It also allows for the creation of a ranked list of factors
and their influence on the overall results.
•
Modeling - the modeling process allows the researcher to create an equation that
accurately and with high predictive power to emulate the system.


---


## Page 88


71
•
Optimization - a researcher is interested in the determination of the optimal
settings of the system factors. The settings of these factors will then optimize the
process response.
This study will focus on the engineering domain of optimization.
In the case of makers responding to COVID-19 PPE shortages, the critical responses
are print speed, cost, and quality. This research will leverage DOE to identify the critical
factors that contribute to the responses of speed, cost, and quality. Once the factors
have been identified, processes described in the following sections will be utilized to
minimize costs, maximize speed, and maintain quality.
4.1.1 — AN EXAMPLE OF DOE
In Tranter et al. (2017) the research team optimized for energy consumption and quality
in injection molding. This method could be adapted to optimize for throughput, cost, and
quality in FDM printing. The study is an investigation into the reduction of energy
consumption in injection molding while maintaining a part’s quality. According to the
paper the “work focused on study on the effects of selected process parameters of the
injection molding process on energy consumption and quality of the molded parts. This
is to achieve an optimal process parameter configuration that would reduce the energy
consumption, whilst still maintaining production of parts of good quality.”
The design of the experiment in the Tranter et al., (2017) paper utilized design of
experiments to test the design parameters to determine the relationship with the
process output. The study focused on the following:


---


## Page 89


72
•
A Melt Temperature, 𝑇-
•
B Mold Temperature, 𝑇-𝑜
•
C Holding Pressure, 𝑃.
•
D Holding Time, 𝑡ℎ
•
E Cooling Time, 𝑡𝑐
The researchers utilized a •-level fractional factorial design in which process
parameters had a specified upper (+1) and lower (-1) levels. With 16 trails, the 25-1
design, no main effects were confounded with any other main effect or 2-factor
interaction. This allowed them to be estimated separately from one another without the
requirement for conducting a full factorial (32 trails) (Tranter, Refalo, & Rochman, 2017).
A total of 10 parts were created per trail.
Once the trials were completed, ~.‚.• — Analysis of Variance (ANOVA) was utilized to
determine the effects of the process parameters on the energy consumption. 5 of the 10
samples generated per trial were selected at random and then a quality determination
procedure was applied. ANOVA was employed again to determine the effects of the
process parameters on the part quality. Once the energy and quality data were
collected response optimization was used to jointly optimize the process parameters
(Tranter, Refalo, & Rochman, 2017).
The results of the research show that the outlined process can be used to optimize for
energy and quality. The researchers also state that their methodology could be used in
other studies using other materials and energy requirements (Tranter, Refalo, &
Rochman, 2017).


---


## Page 90


73
4.1.2 — FRACTIONAL FACTORIAL DESIGN
In a factorial design, the factors are varied together rather than one at a time. Factorial
design is ideal for dealing with several factors. In the case of Tranter (2017), the factors
of interest were:
• A Melt Temperature, 𝑇-
• B Mold Temperature, 𝑇-𝑜
• C Holding Pressure, 𝑃.
• D Holding Time, 𝑡ℎ
• E Cooling Time, 𝑡𝑐
Tranter (2017) utilized a 2-level fractional factorial design. The level notation can be
described as the following (Christensen, 1996):
“A useful notation for factorial experiments identifies the number of factors and the
number of levels of each factor. For example, the alcohol–sleeping pill experiment has 4
treatments because there are 2 levels of alcohol times 2 levels of sleeping pills. This is
described as a 2 × 2 factorial experiment. If we had 3 levels of alcohol and 4 doses
(levels) of sleeping pills we would have a 3×4 experiment involving 12 treatments.”
Fractional factorial design utilizes confounding. This is a method to design factorial
experiments allowing incomplete blocks. By using fractional replication, fewer
treatments are needed as compared to full factorial. A basic concept in experimental


---


## Page 91


74
design is making sure that there is adequate replication to provide a satisfactory
estimate of error (Christensen, 1996).
4.1.3 — ANALYSIS OF VARIANCE (ANOVA)
The Analysis of Variance (ANOVA) was developed by Sir Ronald Fisher for the analysis
of results in agricultural experiments (Fisher, 1992). According to Larson (2008),
“ANOVA can be defined as a statistical technique used to analyze variation in a
response variable measured under conditions defined by discrete factors. ANOVA is
frequently used to test equality among several means by comparing variance among
groups relative to variance within groups.”
In the case of Tranter (2017), ANOVA was utilized to analyze the effects of the process
parameters on both energy consumption and quality. With energy consumption, ANOVA
allowed the researchers to study their effect of energy use based on the process
parameters. The same ANOVA process was also utilized to determine the effects of the
parameters on the part quality. Upon determining the effects of the process parameters,
response optimization was conducted to jointly optimize the parameters (Tranter,
Refalo, & Rochman, 2017).
4.1.4 — ORDINARY LEAST SQUARES REGRESSION
Ordinary Least Squares Regression (OLS) is a common linear analysis model. OLS
models the relationship between a dependent value and a collection of independent
variables (Pohlman & Leitner, 2003). The value of the dependent variable is defined by
the linear combination of the independent variables as defined by:


---


## Page 92


75
𝑌= 𝛽/ + 𝛽0 ∗𝑋0 + 𝛽1 ∗𝑋1 + 𝛽2 ∗𝑋2 + 𝜖
where:
•
𝑌 is the dependent variable
•
𝛽s are the regression coefficients
•
𝑋 is the column vector of the independent variables
•
𝜖 is the vector of errors of the prediction.
The errors are assumed to be normally distributed and expected to be zero with a
common variance (Pohlman & Leitner, 2003).
In the case of this study, the OLS equation is expected to be like:
𝐶𝑜𝑠𝑡= 𝛽/ + 𝛽0 ∗𝑥0 + 𝛽1 ∗𝑥1 + 𝛽3 ∗𝑥3 + 𝛽4 ∗𝑥4 + 𝛽5 ∗𝑥5
and
𝑇𝑖𝑚𝑒= 𝛽/ + 𝛽0 ∗𝑥0 + 𝛽1 ∗𝑥1 + 𝛽3 ∗𝑥3 + 𝛽4 ∗𝑥4 + 𝛽5 ∗𝑥5
where:
•
𝐶𝑜𝑠𝑡 and 𝑇𝑖𝑚𝑒 are the dependent variable
•
𝛽s are the regression coefficients
•
𝑥0 is the column vector of the layer height (lh)
•
𝑥1 is the column vector of the print speed (ps)
•
𝑥3 is the column vector of the infill density (id)
•
𝑥4 is the column vector of the raster width (rw)
•
𝑥5 is the column vector of the wall thickness (wt)


---


## Page 93


76
In Figure 14, the “coef” column represents the 𝛽 values.
4.1.5 — RESPONSE OPTIMIZATION AND EPSILON-CONSTRAINT
Tranter (2017) utilized response optimization to determine the ideal process parameters
to optimize for multiple responses. When optimizing for a single response, a solution
can be easily obtained. In the Tranter study, the objective was to minimize energy
consumption while at the same time maximizing part quality. In cases where there are
multiple objectives to optimize, multiple response optimization offers a solution.
Multiple response optimization or response surface methodology (RSM) is set of
mathematical and statistical techniques that can be used in cases where modeling and
analysis require multiple responses of interest is to be optimized. A desirability function
allows the researcher to optimize of all responses simultaneously by combining the
various objectives into a single objective function. This function represents the
relationship of all responses that are to be optimized (Akçay & Anagün, 2013).
As noted in Dey and Yodo (2019):
“In most of the existing research, the optimum combination of process parameters was
determined from experimental studies instead of applying numerical optimizations.
Thus, an optimum solution is one of the combinations from the experimental data.
However, the actual optimal solutions might be different.”
This study will utilize 𝜖-constraint methodology. 𝜖-constraint is a class of multiple
objective programming. These types of problems focus on the mathematical
optimization of multiple objective functions where the objectives need to be optimized


---


## Page 94


77

Figure 14: Example OLS Results


---


## Page 95


78
simultaneously or sequentially. In many instances in the literature, the Pareto or efficient
frontier function can be used to illustrate the trade-offs among conflicts between the
multiple objectives (Wattanasaeng & Ransikarbum, 2021). According to Wattanasaeng
and Ransikarbum (2021):
“The advantages of 𝜖-constraint programming includes being able to obtain exact
Pareto solutions, instead of approximated solutions, using a series of single-objective
subproblems in which all but one objective is transformed into constraints.”
Mathematically, 𝜖-constraint programming can be described as the following:
Minimize/Maximize Z: 𝑓*(𝑥)
subject to: 𝑥∈𝑋
𝑓*(𝑥) ≤𝜖6; ∀∈
*
{1, . . . , 𝑘}\{𝑗}
For example, following the 𝜖-constraint workflow (Figure 15), in the case of a problem
with two objectives (𝑓0 and 𝑓1), the researcher would keep 𝑓0 as an objective Minimize
𝑓0(𝑥) and treat 𝑓1 as a constraint - 𝑓1(𝑥) ≤𝜖1 and then keep 𝑓1 as an objective Minimize
𝑓1(𝑥) and treat 𝑓0 as a constraint - 𝑓0(𝑥) ≤𝜖0.
4.2 — INSPECTION FOR QUALITY CONTROL
Numerous definitions for visual inspection are defined in the literature. The FAA (1997)
defines it as the following:


---


## Page 96


79

Figure 15: 𝜖-Constraint Workflow (Wattanasaeng & Ransikarbum, 2021)


---


## Page 97


80
“Visual inspection is defined as the process of using the unaided eye, alone or in
conjunction with various aids, as the sensing mechanism from which judgments may be
made about the condition of a unit to be inspected.”
In the case of this study, visual inspection will be conducted with the unaided eye (FAA,
1997).
Numerous studies outline the generic steps for a visual inspection. These steps remain
the same for manual, automated, and hybrid visual inspection systems. The generic
functions include (Salvendy, 2001):
•
Initiate - Defined as the preparatory work to perform the inspection. Initiation
could include accessing a scoring system, gathering inspection equipment, and
other work (Drury & Watson, 2002).
•
Access - Defines as access to the inspection area or item to be inspected at an
appropriate level (Drury & Watson, 2002).
•
Search - Defines as moving the inspection object to adequately inspect the
object (Drury & Watson, 2002).
•
Decision - Form a indication regarding the object and compare to a standard
(Drury & Watson, 2002).
•
Response - On indication confirmation, document the result and complete the
inspection (Drury & Watson, 2002).
With the development of a visual inspection system, it is important to note the logical
errors that can be made while utilizing the generic steps. Drury and Watson (2002)


---


## Page 98


81
outline some examples of the errors that can occur with each of the generic steps.
These include:
•
Initiate
–
Incorrect equipment
–
Incorrect calibration
•
Access
–
Item damaged in presentation
–
Incorrect Item
•
Search
–
Error Indication Missed
–
Error Indication Misidentified
•
Decision
–
Incorrect Measurement
–
Error Indication Misclassified
•
Response
–
Response Action Incomplete
–
Wrong Response for Indication
By noting these errors, it is hoped that the visual inspection process can be completed
in such a way as to minimize logical errors. The literature outlines some control actions
that can be taken to minimize inspection errors. The actions include vigilance,
environment, posture, speed, training, and documentation (Drury & Watson, 2002).


---


## Page 99


82
4.2.1 — VIGILANCE, ENVIRONMENT, POSTURE, SPEED, TRAINING, AND
DOCUMENTATION
According to the literature, when an individual is performing a task, the individual’s
vigilance for task quality can be affected by the amount of time on task and the
environment. Studies show that an individual has maximum vigilance during the first 15
minutes of a task and vigilance then drops by 10-15% in the first 30 minutes. A gradual
decline in vigilance continues after the first 30 minutes (Warm, Parasuraman, &
Matthews, 2008). Research shows that random noises increase the difficulty of tasks
and decreases an individual’s vigilance (Taylor, Melloy, Dharwada, Gramopadhye, &
Toler, 2004).
The environment that the visual inspection is conducted in a component of success. As
noted, previous the environment can impact an individuals’ vigilance (Taylor, Melloy,
Dharwada, Gramopadhye, & Toler, 2004). An environment for successful visual
inspection should be both distraction free and comfortable (Melchore, 2011).
Additionally, lighting is key to error detection. Inspection area should be well lit and
glare/reflection free (Drury & Watson, 2002).
The comfort of the inspector can affect the quality of the inspection. A growing body of
research demonstrates the importance of ergonomics. Drury and Watson (2002)
enumerate many of these studies.
The velocity of the visual inspection can be affected by the the actual speed the
inspection is performed. The science of human factors engineering is described as
Speed/Accuracy Trade-Off (SATO). The quicker the inspection task is completed, the


---


## Page 100


83
more data limited and constrained is the inspector. This factor in conjunction with
vigilance can be a large negative impact (Drury & Watson, 2002).
Training and documentation are linked factors. In the case of training, a common adage
is “find the right person for the job”. Typically, the right person requires the right training.
Unlike the previous factors, selection and training are ongoing costs. When developing
a training regime, care must be taken to balance initial training with ongoing, update
training (Drury & Watson, 2002).
A study by Webber and Drury (2000) identified that documentation was listed as a
contributing factor in 46% or errors in maintenance and inspection. documentation need
to be designed in accordance with proven guidelines that reduce errors and should be
more usable to inspectors (Drury & Watson, 2002).
In this study, the generic steps for visual inspection will be utilized. Additionally, care will
be taken to mitigate and control the human factor errors of vigilance, environment,
posture, speed, training, and documentation.
4.2.2 — FUNCTIONAL VS NONFUNCTIONAL QUALITY
3DP and FDM technology has been used extensively for rapid prototyping of
components, both simple and intricate. 3DP has also been used to create embossing
tools, conductive polymers, pharmaceuticals, dielectric products, biomedical implants,
medical supplies, spare parts, food, and toys (Mwema, Akinlabi, & Fatoba, 2020). In
cases such as toys, spare parts, and PPE (face shields), quality must be measure
based on functional and non-functional quality.


---


## Page 101


84
In the case of makers, a printed object must be functional and have acceptable
aesthetics (non-functional quality). A visual inspection can be used to determine the if
an object is functional. In the case of aesthetics, a visual inspection will yield a
subjective observation. Previous research has utilized the visuotactile perception to rate
objects (Li et al., 2017).
In a study by Ramananantoandro et al. (2014), visuotactile perception can be classified
as the following:
•
Hedonic tactile appreciation - this characteristic is the preference of the object
based upon touch.
•
Tactile roughness perception - this characteristic is the determination of
roughness based upon touch.
•
Visual impression of roughness - this characteristic is the determination of
surface roughness based upon sight only.
The study had assessors rank objects based upon a scale of 1-5 (1 being the worst
value and 5 the best). Ramananantoandro et al. (2014) utilized samples of wood and
wood materials to determine surface roughness. Li et al., (2017) applied this technique
to 3DP.
In Li et al., (2017), visuotactile perception was compared to measured roughness. Using
the Ramananantoandro et al. (2014) methodology, the measured roughness matched
well with the measured roughness. This methodology could be utilized in this research
project.


---


## Page 102


85
4.3 — THE INSPECTION SCORE
The visual inspection will consist of the following steps outlined in Figure 16.
This study will utilize a visuotactile perception classification based on the work of
Ramananantoandro et al. (2014), An assessor classifies an object based upon a scale
of 1-5 (1 being the worst value and 5 the best) expressed as percentages. The three
characteristics to be classified are as follows:
•
Hedonic tactile appreciation - this characteristic is the preference of the object
based upon touch (Ramananantoandro et al., 2014).
•
Tactile roughness perception - this characteristic is the determination of
roughness based upon touch (Ramananantoandro et al., 2014).
•
Visual impression of roughness - this characteristic is the determination of
surface roughness based upon sight only (Ramananantoandro et al., 2014).
The weighted averages of the aesthetics assessment will be determined as follows:
7.
Tactile Roughness Perception (200) - The face shield headband is meant to be
worn on the head. Potentially, medical personnel could be wearing the face
shield for long streets of time and comfort is key. The “feel” of the headband is
the most important aesthetic factor.
8.
Hedonic Tactile Appreciation (150) - Although not as important as the feel of the
band, the look of the band can help increase perceptions.
9.
Visual Impression of Roughness (100) - the visual inspection of roughness is
given the least weight. This decision was made due to the possibility of varying
colors of bands. In Ramananantoandro et al. (2014), it was noted that the color of


---


## Page 103


86

Figure 16: Steps in the Visual Inspection


---


## Page 104


87
wood samples had an impact on the impression of roughness. In an emergency,
the production of items such as PPE should not be restricted to colors.
Figure 17 represents a template for the visual inspection. The scores will be utilized to
help identify optimized print parameters.
The equations used to determine the weighted inspection score is as follows:
𝑊𝑆= 𝑊∗𝑅
Where:
•
𝑊𝑆 is Weighted Score
•
𝑊 is Weight
•
𝑅 is the rating expressed as a percentage
4.4 — INSPECTION MEASUREMENTS
As noted previously, the simplistic design of the face shield lends itself to a less rigorous
need for exact headband measurements and dimensions. Basically, a headband does
not need to have exact measurements to work. However, measurements should be
considered as part of the inspection process. To assess the measurements and
dimensions of the headbands, the following techniques will be utilized:
• Print an “Index” headband. These headbands will be printed with the highest
quality setting for the print parameters.
• Using the “Index” create a mold of the headband.
• Compare all subsequently printed headbands to the mold.


---


## Page 105


88

Figure 17: Visual Inspection (Aesthetics) Score Card


---


## Page 106


89
• Consider any headband that does not fit the mold as non-functional
To create the mold, modeling clay was purchased. The clay was modeled into 9x9 cake
pans. Once in the pans, the index print was pressed into the mold. The index mold was
used for future comparisons (Figure 18).
In addition to the index mold, various measurements (Figure 19 and Figure 20) were
utilized to determine the functionality of the headband. The measurements include:
1. Top “horns” at approximately 6cm
2. Bottom “horns” at approximately 12cm
3. Right hand elastic clip, at approximately 2.5cm
4.5 — EXPERIMENTAL TOOLS
This study will utilize several tools to meet the project objectives. These tools include:
•
FDM Printer Selection
•
Filament Selection
•
3DP Model Slicer
•
Octoprint
•
Face Shield Model
•
Programming and DOE Modeling
FDM PRINTERS
This study will utilize two low cost FDM printers to test the effects of the listed process
parameters on throughput, cost, and quality. The printers to be used are the


---


## Page 107


90

Figure 18: Index Mold


---


## Page 108


91

Figure 19: Image of Headband Measurements (Measure 1)


---


## Page 109


92

Figure 20: Image of Headband Measurements (Measure 2 and 3)


---


## Page 110


93
Artillery Sidewinder X1 and the Creality CR-6 SE. Both printers retail for under $500 and
are widely available from numerous sites including Amazon.
SMART PLUGS
To collect the cost of electricity to utilize the printers, BN-LINK WIFI Heavy Duty Smart
Plug Outlets were use. These smart plugs allow for the remote monitoring of energy
usage via a mobile application. Energy usage is captured as kilowatts per hour (KWh).
The type of smart plug used offers a cost-effective method to monitor energy
consumption.
Filament
There are numerous FDM filaments are used by makers. The best indicator of popular
brands of filament, is sales data on Amazon.com. The brand of filament selected will be
Hatchbox PLA. This study will review a common, inexpensive Polylactic Acid (PLA)
filament. PLA is a natural polymer derived from plant starch, a large carbohydrate that
plants synthesize during photosynthesis. For these reasons PLA is environmentally
friendly (Valerga, Batista, Salguero, & Girot, 2018). A 1kg roll of PLA costs between
$18-$30.
3DP SLICER
Before experimentation, it was required to determine the lower and upper limits of each
of the process parameters. In order to determine the lower limits, software for •DP
slicing was selected. Cura is an open-source software developed by Ultimaker and a
large community of developers. Although there are several other free and open-source


---


## Page 111


94
slicing software available, Cura has been shown to have good quality (Šljivic, Pavlovic,
Kraišnik, & Ilić, 2019). Additionally, Cura is a popular choice for makers.
Cura allows a user to access numerous process parameters. Cura has built-in
configurations for a large selection of popular 3D printers including the Creality CR-6 SE
and the Artillery Sidewinder X1. These printer profiles have the default values for a all
the process parameters accessible to Cura. The parameter defaults are those submitted
by the Cura community and widely tested. The process parameter defaults will be used
as the lower limits for the process parameters reviewed in this study. The upper limits
will be set based on the defaults. The process parameters for both print filament and the
selected printer can differ.
OCTOPRINT
Octoprint is a free, open-source set of software that allows a user to monitor and control
all aspects of an FDM printer via a Raspberry Pi. In most cases, host software that
sends commands to the printer must remain connected to the printer during the print.
Octoprint allows the users to start print jobs by sending G-code to 3D printer connected
via USB. The user interacts with Octoprint via a web interface. Some of the benefits of
Octoprint are the ability to start and monitor prints remotely (MP, Shinde, Madaki, &
Nadaf, 2019). Additionally, Octoprint has numerous plugins that extend functionality.
In the case of this study, several plugins will be utilized to capture key print metrics.
These plugins include:
•
Filament Manager - a plugin with numerous functions, including the ability to
track material usage


---


## Page 112


95
•
Cost Estimator - a plug-in that allows a user to estimate print cost for the loaded
model.
•
Print Job History - a plugin stores all print-job information of a print in a database
that can be exported to excel.
FACE SHIELD MODEL
The models to be printed are a basic face shield designed by Prusa Research
(https://www.prusaprinters.org/prints/•†‡†ˆ-prusa-face-shield). Prusa Research is a
Czech company known for their popular FDM Prusa printers. Prusa developed the
Release candidate 1 headband (covid19_headband_rc1.stl) in three days at the onset
of the pandemic. The original model was certified by the Czech Ministry of Health
(Research, 2020). A consortium of Tennessee Universities produced 18,000 face
shields based on the Prusa RC1 headband (Tamburin, 2020). This research will utilize
the Prusa RC1 headband as the model to be optimized.
PROGRAMMING AND DOE MODELING

This study will utilize the Python programming language. An open-source programming
language, python was introduced in 1991 and is considered extremely stable and
mature. Python is used extensively by data scientists and is currently one of the most
popular programming languages in the world. A key aspect of the selection of python is
the availability of DOE and other relevant scientific and data analysis packages.
As part of the analysis of data from the experiments, Jupyter Notebooks
(http://jupyter.org/) using python were utilized. Jupyter notebooks can be described as a


---


## Page 113


96
document format for publishing code, results and explanations in a readable form that
can be executed (Kluyver et al., 2016). The notebook is is designed to allow for
reproducible computational workflows (Yin et al., 2017). In the case of these
experiments, the notebooks are designed to allow the results to be calculated in a
repeatable manner. Additionally, the notebooks will allow for the results and code to be
utilized in future research with minimal effort.
4.6 — EXPERIMENTAL PROCESS
The objective functions in this research are cost, throughput, and quality. In this project,
cost is calculated as the sum of material and energy costs. Throughput is synonymous
with build time. In this project, cost is calculated as the sum of material and energy
costs. Quality, in the case of makers, is expressed as surface roughness.
The study “Parametric Analysis of the Build Cost for FDM Additive Processed Parts
Using Response Surface Methodology” (Mohamed et al., 2016b) identifies a cost model
that is applicable for determine the cost for printing FDM parts. The model developed is:
𝐵!"#$ = 𝐶% + 𝐶& + (𝑀' + 𝑇()*+,)
Where:
•
𝐵!"#$ = Build cost ($)
•
𝐶% = Model material cost ($)
•
𝐶& = Support material cost ($)
•
𝑀' = Machine running cost (Hour)
•
𝑇()*+, = Built time (Hour)


---


## Page 114


97
As noted in Dey and Yodo, (2019) (Figure 21) and Pérez et al., (2018), there are
several parameters common to both throughput and surface roughness. The process
parameters include:
•   Layer Thickness
•   Print Speed
•   Infill Density
•   Raster Width
•   Wall Thickness
As with Tranter et al. (2017), this research will utilize a 2-level fractional factorial design,
in which process parameter had a specified upper (+1) and lower (-1) level. By using the
upper and lower limits, this study will more closely align with the common maker
workflow (Figure 22). The 2570 design will have a total of 16 trials, which was chosen on
the basis that in a resolution −V design, no main effect or 2-factor interactions are
confounded with any other main effect or 2-factor interactions, this will allow the
parameters to be estimated separately from one another without the requirement for
conducting a full factorial (32 trials) (Tranter et al., 2017).
As noted previously, the process parameters to be examined include:
•
Layer Thickness (LH)
•
Print Speed (PS)
•
Infill Density (ID)
•
Raster Width (RW) - Infill Line Width in Cura
•
Wall Thickness (WT)


---


## Page 115


98


Figure 21: Breakdown of Characteristics vs Parameters (Dey and Yodo, 2019)


---


## Page 116


99

Figure 22: New Workflow to Integrate Optimization


---


## Page 117


100
The upper and lower limits of each process parameter is documented in Table 5. For
the Print Speed (PS), the PS on the Creality CR-6 SE the upper limit is 60 and for the
Sidewinder X1 the PS upper limit is 72. The experimental schedule is laid out in Table 6
After each trial, the throughput, quality, and cost values will be recorded. Ordinary Least
Squares Regression (OLS) will be completed on throughput and cost independently.
For example, an OLS will be completed for the throughput to determine the respective
effects of the process parameters. Using a 95% confidence interval, a process
parameter with a P-value smaller that .05 will show that the parameter has a significant
effect on the throughput. Upon completion of each OLS analysis. The linear model
identified will be reduced to represent only significant first and second order
experimental effects. Several OLS runs may be required to reduce the linear equation.
A function will be developed in python to utilize backward regression to complete the
reduction.
𝜖-constraints optimization will be used to identify the combination of process parameters
that will be required to satisfy all the objectives of throughput, cost, and quality. Once
the 𝜖-constraints optimization has been completed, a validation trial will be completed to
test the optimized process parameters. The results will be documented and discussed
in Chapter 6.


---


## Page 118


101
Table 5: Low and High Print Parameters
Factor Process Parameter Unit Lower Value (-1) Upper Level (+1)
A
LH
mm 0.16
0.28
B
PS (+20%)

50
60 (72)
C
ID
%
25
15
D
RW
mm 0.4
0.8
E
WT
mm 1.2
0.8


---


## Page 119


102
Table 6: Experimental Schedule
Trial Number LH PS ID RW WT
1
-1
-1
-1 -1
-1
2
1
-1
-1 -1
-1
3
-1
-1
-1 -1
1
4
-1
1
-1 -1
-1
5
1
1
-1 -1
1
6
-1
-1
1
-1
-1
7
1
-1
1
-1
1
8
-1
1
1
-1
1
9
1
1
1
-1
-1
10
-1
-1
-1 1
-1
11
1
-1
-1 1
1
12
-1
1
-1 1
1
13
1
1
-1 1
-1
14
-1
-1
1
1
1
15
1
-1
1
1
-1
16
-1
1
1
1
-1
17
1
1
1
1
1


---


## Page 120


103
5 — CHAPTER FIVE - CASE STUDY
5.1 — CASE STUDY INTRODUCTION
In the early stages of the COVID-19 pandemic, there were numerous medical supply
shortfalls. Examples include:
•
Testing Supplies
•
Ventilator parts
•
Face Masks
•
Face Shields
In all of the examples listed, 3DP was used to address the shortfalls ((Salmi et al.,
2020), (Cox & Koepsell, 2020), and (Bishop & Leigh, 2020)). Makers from across the
globe have utilized 3D printers to meet the PPE challenges in a survey by Novak and
Loy (2020), from February to March 2020 62% of PPE projects were focused on the
production of face shields. Of all the PPE project surveyed, over 60% utilized FDM
printers. In many cases, maker production represented volunteer efforts to create PPE
that was in short supply. The quick production (throughput) of PPE was critical to
alleviate short falls but because of the strain on unpaid volunteers utilizing their own
resources, it was critical to minimize the need for materials (print stock) and cost on the
maker community. A maker community of public Universities in Tennessee was one of
many maker groups producing face shields.


---


## Page 121


104
5.2 — COVID-19 3DP IN TENNESSEE
In early March 2020, Tennessee Higher Education Commission (THEC) put out a call to
various public Universities across the state of Tennessee to identify the possibility of
harnessing 3DP to produce PPE for the Tennessee Emergency Management Agency
(TEMA). TEMA would collect and distribute any PPE that was produced. Within 24
hours of the initial THEC call, a team at Austin Peay State University produced a
prototype face shield using the Prusa Research RC 1 headband (Figure 23).
TEMA quickly approved the prototype face shield as the model for THEC project to
produce. THEC proceeded to mobilize Universities across the state of Tennessee to
produce face shields. Universities that participated include Technical and Community
Colleges, the University of Tennessee, and Austin Peay State University.
In a project that lasted from March to June 2020, almost 20,000 face shields were
delivered to TEMA. TEMA then distributed the PPE to communities, responders, and
hospitals facing supply shortfalls.
A face shield (Figure 24) is composed of a FDM printed frame, a piece of elastic, and a
cut sheet of clear acetate.
The most time consume component of production is the 3D printed frame.
5.3 — TN PROJECT STATISTICS
As noted previously, a face shield is composed of 3 components a 3D printed
headband, a piece of elastic, and an acetate shield. In the TN project, almost 20,000
face shields were produced. Each headband and elastic were matched with 10


---


## Page 122


105


Figure 23: Initial APSU Face Shield based on the Prusa RC 1 Headband


---


## Page 123


106

Figure 24: Face Shield Components


---


## Page 124


107
replaceable acetate shields. Therefore, a face shield set included 1 headband, 1 piece
of elastic, and 10 pieces of acetate. Each set was boxed for deliver and a box contained
36 sets of face shields (Figure 25).
In the case of the team at Austin Peay State University, the printing process for a
headband averaged 3.5 hours. It can be extrapolated that the 20,000 headbands made
by the consortium of TN Universities represented approximately 70,000 printer hours.
The 70,000 hours represented production with little or no optimization. In the pandemic,
speed is of the essence. By utilizing optimization, the THEC team could have produced
more units in a cheaper manner without sacrificing quality.
5.4 — CASE STUDY EXPERIMENT
In Tranter et al. (2017), an optimization technique was described to optimize for energy
consumption and quality in injection molding. This methodology describes a
straightforward method to optimize the injection molding process and can be adapted to
optimizing for throughput, cost, and quality in FDM printing. Based on previous
research, the process parameters most likely to have a positive impact on speed, cost,
and quality include:
•
Layer Thickness (LH)
•
Print Speed (PS)
•
Infill Density (ID)
•
Raster Width (RW) - Infill Line Width in Cura
•
Wall Thickness (WT)


---


## Page 125


108

Figure 25: TEMA Picking Up a Shipment of Face Shields


---


## Page 126


109
Based on the experimental schedule outlined in Table 6 and the lower and upper limits
in Table 5, the value of the process parameters for each experimental run are as follows
in Table 7
The experiments were conducted on the Creality CR-6 SE and the Artillery Sidewinder
X1 over several weeks in December 2020 - April 2021. The original DOE schedule as
outlined by Tranter et al. (2017) called for 16 runs (Rows 2-17 in Table 7). An additional
run (Row 1 Table 7) was included in this case study to create a baseline headband with
all the lower limit parameter values to be a comparator for the inspection process.
During the initial print, it was noted that models did not adhere to the Sidewinder X1
build plate consistently. To correct for this issue, all models on both printers were sliced
and printed with a brim (Figure 26). A brim is a single-layer feature added by the slicing
software to increase the bed contact area. The brim improves bed adhesion and
reduces warping (Johnson & French, 2018).
Utilizing Octoprint and the Print Job History plugin, a sample of the captured results are
in Table 8 and Table 9.
As noted previously, all print data was collected via the Octoprint plugin, Print Job
History. This plugin collects the time for each print as well as the cost of each print. The
data collected by the plunging was exported to a CSV file.


---


## Page 127


110
Table 7: Use Case Experimental Schedule
Trial Number LH PS
ID RW WT
1
.16 50 (60)* 25 0.4
1.2
2
.28 50 (60)* 25 0.4
1.2
3
.16 50 (60)* 25 0.4
.8
4
.16 60 (72)* 25 0.4
1.2
5
.28 60 (72)* 25 0.4
.8
6
.16 50 (60)* 15 0.4
1.2
7
.28 50 (60)* 15 0.4
.8
8
.16 60 (72)* 15 0.4
.8
9
.28 60 (72)* 15 0.4
1.2
10
.16 50 (60)* 25 .8
1.2
11
.28 50 (60)* 25 .8
.8
12
.16 60 (72)* 25 .8
.8
13
.28 60 (72)* 25 .8
1.2
14
.16 50 (60)* 15 .8
.8
15
.28 50 (60)* 15 .8
1.2
16
.16 60 (72)* 15 .8
1.2
17
.28 60 (72)* 15 .8
.8
* 50 (60) and 60 (72) - The print speed lows for CR6 is 50 and Sidewinder X1 is 60 and
highs for CR6 is 60 and Sidewinder X1 is 72.


---


## Page 128


111


Figure 26: Print with Brim


---


## Page 129


112
Table 8: Sample Results from CR-6 SE
Duration
File Name
File Size
[bytes]
Used
Length
[mm]
Used
Weight
[g]
Used
Filament
Cost
4h11m25s
CCR6SE_Run10.gcode 12960660
9040
27.19
0.54$
4h11m51s
CCR6SE_Run10.gcode 12960660
9040
27.19
0.54$
4h11m48s
CCR6SE_Run10.gcode 12960660
9040
27.19
0.54$
4h11m55s
CCR6SE_Run10.gcode 12960660
9040
27.19
0.54$
4h12m2s
CCR6SE_Run10.gcode 12960660
9040
27.19
0.54$
2h57m4s
CCR6SE_Run11.gcode 6373067
9330
28.05
0.56$
2h57m4s
CCR6SE_Run11.gcode 6373067
9330
28.05
0.56$
2h57m24s
CCR6SE_Run11.gcode 6373067
9330
28.05
0.56$
2h57m26s
CCR6SE_Run11.gcode 6373067
9330
28.05
0.56$
2h56m19s
CCR6SE_Run11.gcode 6373067
9330
28.05
0.56$
4h40m40s
CCR6SE_Run12.gcode 10926032
9330
28.05
0.56$
4h40m37s
CCR6SE_Run12.gcode 10926032
9330
28.05
0.56$
4h41m4s
CCR6SE_Run12.gcode 10926032
9330
28.05
0.56$
13h28m56s CCR6SE_Run12.gcode 10926032
9330
28.05
0.56$
4h40m6s
CCR6SE_Run12.gcode 10926032
9330
28.05
0.56$


---


## Page 130


113
Table 9: Sample Results from Sidewinder X1
Duration
File Name
File Size
[bytes]
Used
Length
[mm]
Used
Weight [g]
Used
Filament
Cost
4h7m16s SWX1-
Default.gcode
13325390
9950
29.91
0.60$
4h18m5s SWX1-
Default.gcode
13325390
9950
29.91
0.60$
4h6m48s SWX1-
Default.gcode
13325390
9950
29.91
0.60$
4h6m38s SWX1-
Default.gcode
13325390
9950
29.91
0.60$
3h58m2s SWX1-
Default.gcode
13016272
9500
28.56
0.57$
4h2m56s SWX1-
Run10.gcode
13270408
10010
30.09
0.60$
4h3m49s SWX1-
Run10.gcode
13270408
10010
30.09
0.60$
4h2m59s SWX1-
Run10.gcode
13270408
10010
30.09
0.60$


---


## Page 131


114
Table 9 Continued
Duration
File Name
File Size
[bytes]
Used
Length
[mm]
Used
Weight [g]
Used
Filament
Cost
4h3m43s
SWX1-
Run10.gcode
13270408
10010
30.09
0.60$
2h38m2s
SWX1-
Run11.gcode
6385350
10300
30.97
0.62$
2h39m8s
SWX1-
Run11.gcode
6385350
10300
30.97
0.62$
2h37m37s SWX1-
Run11.gcode
6385350
10300
30.97
0.62$
2h37m39s SWX1-
Run11.gcode
6385350
10300
30.97
0.62$
2h37m27s SWX1-
Run11.gcode
6385350
10300
30.97
0.62$
3h45m50s SWX1-
Run12.gcode
10657292
10150
30.53
0.61$
3h45m54s SWX1-
Run12.gcode
10657292
10150
30.53
0.61$
3h45m1s
SWX1-
Run12.gcode
10657292
10150
30.53
0.61$


---


## Page 132


115
Table 9 Continued
Duration
File Name
File Size
[bytes]
Used
Length
[mm]
Used
Weight [g]
Used
Filament
Cost
3h45m50s SWX1-
Run12.gcode
10657292
10150
30.53
0.61$
3h46m22s SWX1-
Run12.gcode
10657292
10150
30.53
0.61$


---


## Page 133


116
Upon completion of all the experimental runs, an inspection was conducted based on
the process outlined in Chapter 4. The possible range of scores is 0 - 450. Experimental
Run 1 (baseline headband) was given a top score of 450 and the sets from each printer
was put aside for reference during the inspection process. A sample inspection score
card is shown in Figure 27.
Utilizing modeling clay, a mold was created of the index print from each printer (Figure
28). The molds provided a quick and convenient method to measure the dimensional
accuracy of the various prints. During the quality assessment, the molds will be used to
assess the functionality of a given print. Prints that do not match the index mold will be
considered non-functional. Non-functional prints were noted in the quality score card.


---


## Page 134


117

Figure 27: Sample Inspection Score Card


---


## Page 135


118


Figure 28: Index Mold


---


## Page 136


119
6 — CHAPTER SIX - RESULTS AND DISCUSSION
6.1 — DATA COMPILATION
Upon completion of the experiments, the various results were compiled. The results
data included the following:
•
The print statistics including time and cost were captured during printing and
saved and exported to a CSV file.
•
The quality score was captured via an excel spreadsheet.
Several data transformations were required before the data analysis could be
accomplished. The time data captured by the Octoprint - Print Job History was stored in
hour-minute-second format (Table 8). For example, a replicant for the CR6 SE run 10
had a print time of 4h11m25s. This value had to be converted to a second’s format to
allow for mathematical analysis. The 4h11m25s translates to 15085 seconds. Once all
the time values were converted to seconds format, the data was reviewed for problems.
A time value for a single replica in Run 12 for the CR6 was found to be an anomaly. The
captured print time was recorded to be over 13 hours. All other Run 12 replicants were
approximately 4.5 hours. The problematic results were reprinted. The Run 12 replicant
did not take 13 hours, the recorded data was due to an Octoprint error.
To further simplify analysis, the actual values of the print parameters was added to the
DOE schedule for each printer. An example is listed in Table 10.
•
Actual Layer Height (alh)


---


## Page 137


120
Table 10: Combined Results for the CR-6 SE


---


## Page 138


121
•
Actual Print Speed (aps)
•
Actual Infill Density (aid)
•
Actual Raster Width (arw)
•
Actual Wall Thickness (awt)
It was determined during the data review that the energy cost was not captured by the
Octoprint plugins. A BN-LINK WIFI Heavy Duty Smart Plug Outlets was connected to
each printer, the CR6 and the SWX1. Based on a test print on each printer, the cost of
printing per second was calculated to be:
•
CR6 - $0.00000297240857053766 per second
•
SWX1 - $0.00000197585775290826 per second
These costs were then added to the collected cost on each respective printer. As can
be seen in the calculations, the SWX1 is significantly cheaper to run that the CR6. The
corrected data is in Appendix A.
As noted previously, the quality score component of cost and time needed to be
factored into the cost and time dependent variables. After a review of the rework time, it
was determined that following time values would be utilized based on quality score:
•
450 - Zero (0) rework time
•
450 > and > 399 - Thirty (30) seconds rework time
•
400 > and > 337 - Sixty (60) seconds rework time
•
337 > and > 249 - Ninety (90) second rework time
•
250 > - One Hundred twenty (120) second rework time
•
0 - model unusable


---


## Page 139


122
Therefore:
𝑇𝑖𝑚𝑒$ = 𝑇𝑖𝑚𝑒8 + 𝑇𝑖𝑚𝑒'
where:
•
𝑇𝑖𝑚𝑒$ is Total Time
•
𝑇𝑖𝑚𝑒8 is Time from Experiment
•
𝑇𝑖𝑚𝑒' is the rework time
The time values listed were added to the time values collected during the experimental
process.
To calculate a cost factor, the time values needed to be converted to a cost. To
accomplish this, it was estimated that an unskilled laborers cost would be $15 per hour
salary and $7.50 per hour benefits for a total of $22.50 per hour. This translates to
$0.00625 per second. The cost values to be used based on quality score were as
follows:
•
450 - $0.0
•
450 > and > 399 - $.1875
•
400 > and > 337 - $.375
•
337 > and > 249 - $.5625
•
250 > - $.75
•
0 - model unusable
Therefore:
𝐶𝑜𝑠𝑡$ = 𝐶𝑜𝑠𝑡8 + 𝐶𝑜𝑠𝑡'


---


## Page 140


123
where:
•
𝐶𝑜𝑠𝑡$ is Total Cost
•
𝐶𝑜𝑠𝑡8 is Cost from Experiment (Filament Cost)
•
𝐶𝑜𝑠𝑡' is the rework cost
The data with the quality factors is listed in Appendix A.
Once all transformations were completed, a value was calculated for the response
variables of cost, time, and quality for each experimental run. The experimental
schedule for each of the printers was combined with the experimental results. The raw
results and various stages of transformation are listed in Appendix A.
The CR6 DOE Schedule and SWX1 DOE Schedule results were saved as CSV files to
be utilized via Jupyter notebooks.
QUALITY SCORES
As outlined in previous sections, the quality scores were compiled in the score card.
The score cards for the CR6 in Appendix A. The scores were used to create the rework
tables. Examples are listed in Figure 29 and Figure 30. The complete tables can be
found in Appendix A.
6.2 — DATA ANALYSIS
Based upon the research questions and various transformations conducted on the
experimental data, the following datasets will be analyzed:


---


## Page 141


124

Figure 29: Highlighted Rows Demonstrate Differences in Raw Cost And Time Vs Those
Including Rework Factors for the CR6


---


## Page 142


125

Figure 30: Highlighted rows demonstrate differences in raw cost and time vs those
including rework factors for the SWX1


---


## Page 143


126
•
Analysis A - Optimization of cost (w/o power) and time and review the results for
quality
•
Analysis B - Optimization of cost+power and time and review the results for
quality
•
Analysis C - Optimization of cost+power and time factoring in rework
The various analysis listed will be compared. For all analysis an 𝛼= .05 was utilized.
The analysis was conducted using the methodologies outlined in Chapter ~ -~.• —
Experimental Process. All data and analysis were conducted in python via Jupyter
notebooks. T The steps required to repeat the analysis can be found in Appendix B -
Repeatability.
CONSIDERING QUALITY
During this study, it was found that only one (1) headband was unusable. This unusable
model was due to the model being moved on the print bed (Figure 31). All models were
rated between 100% (excellent quality) and 25% (poor quality). It was found that with
slight rework, all headbands could be made usable. The decision was made to factor
the effects quality into the dependent variables cost and time rather than treat quality as
a separate dependent variable. By factoring quality into cost and time, a more accurate
model could be produced.
When compiling the quality scores, it was found that the CR6 demonstrated better
quality overall (Table 11). The SWX1 prints were of poorer quality (Table 12). It can be
surmised that these differences are due to the overall quality of the printers, The CR6
being of higher quality overall.


---


## Page 144


127

Figure 31: Image of the Unusable Headband


---


## Page 145


128
Table 11: Average Quality Scores for the CR6
1
2
3
4
5
TOTALS
weighted
score
weighted
score
weighted
score
weighted
score
weighted
score
Overall
Score
434.375
440.625
445.3125
443.75
446.875
442.1875


---


## Page 146


129
Table 12: Average Quality Scores for the SWX1
1
2
3
4
5
TOTALS
weighted
score
weighted
score
weighted
score
weighted
score
weighted
score
Overall
Score
300.78125
294.53125
292.1875
295.3125
295.3125
295.625


---


## Page 147


130
In the use of the band molds, it was found not to be valuable. The molds were not a
good indication of functionality. The measurements were more valuable.
6.2.1 — EXPERIMENTAL ANALYSIS A
Optimization of cost (w/o power) and time and review the results for quality
In this set of analysis, I will review the ideal print parameters for cost and time without
directly factoring in quality. Once the ideal parameters are identified, test prints will be
created, and quality will be assessed.
The raw collected results are listed in Appendix A.
6.2.1.1 — Experimental Analysis A - CR6
The initial results (Figure 32) for the CR6 Cost Ordinary Least Squares regression
model (OLS) show that several of the primary effects of the experiments are not
statistically significant. The variables that are not significant factors in the cost of the
model include:
•
Layer height (alh) with p-value 0.927017
•
Infill density (aid) with p-value 0.0905131
The reduced OLS for the CR6 cost is shown in Figure 33. As can be noted in Figure 33,
all the remaining first-order parameters and second-order interactions have a significant
impact of the cost of the model.
There parameters include print speed, raster width, and wall thickness. The interactions
include all of the interactions of the primary parameters.


---


## Page 148


131

Figure 32: Analysis A - CR6 Cost OLS


---


## Page 149


132

Figure 33: Analysis A - CR6 Reduced OLS for Cost


---


## Page 150


133
Based on these results (Figure 33), the following linear equation for CR6 cost was
developed:
𝐶𝑜𝑠𝑡
= 0.30061301677651686 + −0.0014979526099359666 ∗𝑋2 + 0.3541048685686145
∗𝑋4 + 0.24600811428103486 ∗𝑋5 + 0.003193676289093103 ∗𝑋1 ∗𝑋2
+ −0.681545835829839 ∗𝑋1 ∗𝑋3 + 0.15813870197108404 ∗𝑋1 ∗𝑋4
+ −0.15310216338152616 ∗𝑋1 ∗𝑋5 + 0.008101719131677326 ∗𝑋2 ∗𝑋3
+ −0.0026250000000000544 ∗𝑋2 ∗𝑋4 + 0.0011250000000000322 ∗𝑋2 ∗𝑋5
+ 0.3961480849887108 ∗𝑋3 ∗𝑋4 + −0.4897531916854896 ∗𝑋3 ∗𝑋5
+ −0.2593750000000006 ∗𝑋4 ∗𝑋5
This function was utilized in the 𝜖-constraints calculations.
The analysis for CR6 Time OLS, were obtained (Figure 34).
The variables that are not significant factors in the cost of the model include:
Interaction of actual print speed (aps) and actual wall thickness (awt) with p-value
0.712687
•
Actual infill density (aid) with p-value 0.63764
•
Actual raster width (arw) with p-value 0.549529
•
Interaction of aid and arw with p-value 0.12172
•
Interaction of alh and aps with p-value 0.0744513
•
Interaction of arw and awt with p-value 0.0725949
The reduce model for CR6 Time is in Figure 35.


---


## Page 151


134

Figure 34: Analysis A - CR6 Time OLS


---


## Page 152


135

Figure 35: Analysis A - CR6 Reduced OLS for Time


---


## Page 153


136
The variables and interactions that have a significant impact on time include:
•
alh
•
aps
•
awt
•
alh:aid
•
alh:arw
•
alh:awt
•
aps:aid
•
aps:arw
•
aid:awt
Based on these results (Figure 35), the following linear equation for CR6 time was
developed:
𝑇𝑖𝑚𝑒
= 39415.87499999855 + −79138.51046393832 ∗𝑋1 + −128.19137670175314 ∗𝑋2
+ −8860.849838411767 ∗𝑋5 + −46255.95567867106 ∗𝑋1 ∗𝑋3 + 12299.502666120085
∗𝑋1 ∗𝑋4 + 29085.416666666522 ∗𝑋1 ∗𝑋5 + 434.58559556786804 ∗𝑋2 ∗𝑋3
+ −57.717904019688284 ∗𝑋2 ∗𝑋4 + −11377.20914127423 ∗𝑋3 ∗𝑋5
The values utilized for the 𝜖-constraint methodology for Analysis A were:
Minimize:
•
𝑓1 = 0.30061301677651686 + −0.0014979526099359666 ∗𝑋2 +
0.3541048685686145 ∗𝑋4 + 0.24600811428103486 ∗𝑋5 +


---


## Page 154


137
0.003193676289093103 ∗𝑋1 ∗𝑋2 + −0.681545835829839 ∗𝑋1 ∗𝑋3 +
0.15813870197108404 ∗𝑋1 ∗𝑋4 + −0.15310216338152616 ∗𝑋1 ∗𝑋5 +
0.008101719131677326 ∗𝑋2 ∗𝑋3 + −0.0026250000000000544 ∗𝑋2 ∗𝑋4 +
0.0011250000000000322 ∗𝑋2 ∗𝑋5 + 0.3961480849887108 ∗𝑋3 ∗𝑋4 +
−0.4897531916854896 ∗𝑋3 ∗𝑋5 + −0.2593750000000006 ∗𝑋4 ∗𝑋5
•
𝑓2 = 39415.87499999855 + −79138.51046393832 ∗𝑋1 +
−128.19137670175314 ∗𝑋2 + −8860.849838411767 ∗𝑋5 +
−46255.95567867106 ∗𝑋1 ∗𝑋3 + 12299.502666120085 ∗𝑋1 ∗𝑋4 +
29085.416666666522 ∗𝑋1 ∗𝑋5 + 434.58559556786804 ∗𝑋2 ∗𝑋3 +
−57.717904019688284 ∗𝑋2 ∗𝑋4 + −11377.20914127423 ∗𝑋3 ∗𝑋5
st:
•
.16 ≤𝑋1 ≤.28
•
50 ≤𝑋2 ≤60
•
.15 ≤𝑋3 ≤.25
•
. 4 ≤𝑋4 ≤.8
•
.8 ≤𝑋5 ≤1.2
When solved, 𝜖-contraints methodology produces the following values:
•
(𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5) =
S0.28000000999993935,60.000000599972694,0.2500000099939384,
0.8000000096771722,1.2000000119993277
T
•
𝑓1 = 0.53898523398684
•
𝑓2 = 8557.622612553769


---


## Page 155


138
Where:
•
• X1 = layer height = .28 mm
•
• X2 = print speed = 60 mm/s
•
• X3 = infill density = .25
•
• X4 = raster width = .8 mm
•
• X5 = wall thickness = 1.2 mm
•
• f1 = cost = 0.53898523398684
•
• f2 = time = 8557.622612553769 s
In a review of the proposed setting, all the values fit what would be expected for
reduced cost and speed. The exception would be infill density at .25. In part, this
exception is due to the trade-off necessitated by the optimization of cost and time.
Additionally, the model for the headband is composed of very little infill.
As a last step the proposed setting were printed three (3) times. In a review of the of the
quality of the print, it was found to be excellent with a score of 450.
6.2.1.2 — Experimental Analysis A - SWX1
The initial results (Figure 36) for the SWX1 Cost OLS model shows that several of the
primary effects of the experiments are not statistically significant.
The variables that are not significant factors in the cost of the model include:
•
aps:aid with p-value 0.93549
•
alh:aid with p-value 0.99566
•
aps:arw with p-value 0.970373


---


## Page 156


139

Figure 36: Analysis A - SWX1 Cost OLS


---


## Page 157


140
•
aps:awt with p-value 0.994181
•
alh:arw with p-value 0.949303
•
alh:aps with p-value 0.930312
•
aid:arw with p-value 0.679975
•
aps with p-value 0.787536
The reduced OLS for the SWX1 cost is shown in Figure 37. As can be noted in Figure
37, all the remaining first-order parameters and second-order interactions have a
significant impact of the cost of the model.
Based on these results (Figure 37), the following linear equation for SWX1 cost was
developed:
𝐶𝑜𝑠𝑡
= 0.1900000000000014 + 0.24999999999999423 ∗𝑋1 + 0.3999999999999986 ∗𝑋3
+ 0.37499999999999967 ∗𝑋4 + 0.320833333333332 ∗𝑋5 + −0.20833333333332477
∗𝑋1 ∗𝑋5 + −0.25000000000000133 ∗𝑋3 ∗𝑋5 + −0.3124999999999999 ∗𝑋4 ∗𝑋5
This function was utilized in the 𝜖-constraints calculations.
The analysis for SWX1 Time OLS were obtained (Figure 38).
The variables that are not significant factors in the cost of the model include:
•
aps:arw with p-value 0.899404
•
alh:awt with p-value 0.760839
•
aid:awt with p-value 0.641928
•
aid:arw with p-value 0.54847


---


## Page 158


141

Figure 37: Analysis A - SWX1 Reduced OLS for Cost


---


## Page 159


142

Figure 38: Analysis A - SWX1 Time OLS


---


## Page 160


143
•
awt with p-value 0.362301
•
alh:aid with p-value 0.23091
•
alh:arw with p-value 0.223997
•
aps:aid with p-value 0.0884672
The reduce model for SWX1 Time is in Figure 39.
Based on these results (Figure 39), the following linear equation for SWX1 time was
developed:
𝑇𝑖𝑚𝑒
= 41311.84166666333 + −99242.9166666657 ∗𝑋1 + −181.67424724344346 ∗𝑋2
+ 4263.500000000091 ∗𝑋3 + −9967.93702290074 ∗𝑋4 + 815.0694444444525 ∗𝑋1
∗𝑋2 + −116.4993638676806 ∗𝑋2 ∗𝑋5 + 8583.812022900747 ∗𝑋4 ∗𝑋5
The values utilized for the 𝜖-constraint methodology for Analysis A were:
Minimize:
•
𝑓1 = 0.1900000000000014 + 0.24999999999999423 ∗𝑋1 +
0.3999999999999986 ∗𝑋3 + 0.37499999999999967 ∗𝑋4 +
0.320833333333332 ∗𝑋5 + −0.20833333333332477 ∗𝑋1 ∗𝑋5 +
−0.25000000000000133 ∗𝑋3 ∗𝑋5 + −0.3124999999999999 ∗𝑋4 ∗𝑋5
•
𝑓2 = 41311.84166666333 + −99242.9166666657 ∗𝑋1 +
−181.67424724344346 ∗𝑋2 + 4263.500000000091 ∗𝑋3 +


---


## Page 161


144

Figure 39: Analysis A - SWX1 Reduced OLS for Time


---


## Page 162


145
−9967.93702290074 ∗𝑋4 + 815.0694444444525 ∗𝑋1 ∗𝑋2
+ −116.4993638676806 ∗𝑋2 ∗𝑋5 + 8583.812022900747 ∗𝑋4 ∗𝑋5
st:
•
.16 ≤𝑋1 ≤.28
•
50 ≤𝑋2 ≤60
•
.15 ≤𝑋3 ≤.25
•
. 4 ≤𝑋4 ≤.8
•
.8 ≤𝑋5 ≤1.2
When solved, 𝜖-contraints methodology produces the following values:
•
(𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5) =
S0.28000000999993796,72.00000071997286,0.1499999900005892,
0.39999999000704073,1.2000000119995038
T
•
𝑓1 = 0.5900000002000078
•
𝑓2 = 7582.113544009459
Where:
•
• X1 = layer height = .28 mm
•
• X2 = print speed = 72 mm/s
•
• X3 = infill density = .15
•
• X4 = raster width = .4 mm
•
• X5 = wall thickness = 1.2 mm
•
• f1 = cost = 0.5900000002000078
•
• f2 = time = 7582.113544009459 s


---


## Page 163


146
In a review of the proposed setting, all the values fit what would be expected for
reduced cost and speed.
As a last step the proposed setting were printed three (3) times. In a review of the of the
quality of the print, it was found to be excellent with a score of 450.
6.2.2 — EXPERIMENTAL ANALYSIS B
Optimization of cost+power and time and review the results for quality
In this set of analysis, I will review the ideal print parameters for cost and time without
factoring in quality (rework). Once the ideal parameters are identified, test prints will be
created, and quality will be assessed.
The cost+power collected results are listed in Appendix A.
6.2.2.1 — Experimental Analysis B - CR6
Based on the raw collected results (Table 11 and Table 12). The initial results (Figure
40) for the CR6 Cost OLS model shows that several of the effects are not statistically
significant. The variables that are not significant factors in the cost of the model include:
•
aid with p-value 0.138052
•
alh:awt with p-value 0.089003
The reduced OLS for the CR6 cost is shown in Figure 41. As can be noted in Figure 41,
all of the remaining first-order parameters and second-order interactions have a
significant impact of the cost of the model.


---


## Page 164


147

Figure 40: Analysis B - CR6 Cost OLS


---


## Page 165


148

Figure 41: Analysis B - CR6 Reduced OLS for Cost


---


## Page 166


149
Based on these results (Figure 41), the following linear equation for CR6 cost was
developed:
𝐶𝑜𝑠𝑡
= 0.43619166666666676 + −0.3303957650272835 ∗𝑋1 + −0.0018884142076504296
∗𝑋2 + 0.3583517213114778 ∗𝑋4 + 0.2018153688524602 ∗𝑋5
+ 0.00379166666666636 ∗𝑋1 ∗𝑋2 + −0.8282295081967748 ∗𝑋1 ∗𝑋3
+ 0.19062500000000449 ∗𝑋1 ∗𝑋4 + 0.009283737704918856 ∗𝑋2 ∗𝑋3
+ −0.0030125000000000516 ∗𝑋2 ∗𝑋4 + 0.00113750000000004 ∗𝑋2 ∗𝑋5
+ 0.4151163934426205 ∗𝑋3 ∗𝑋4 + −0.5256393442622931 ∗𝑋3 ∗𝑋5
+ −0.25406250000000025 ∗𝑋4 ∗𝑋5
This function was utilized in the 𝜖-constraints calculations.
The analysis for CR6 Time OLS were obtained (Figure 42).
The variables that are not significant factors in the time OLS model include:
•
aps:awt with p-value 0.712687
•
aid with p-value 0.63764
•
arw with p-value 0.549529
•
aid:arw with p-value 0.12172
•
alh:aps with p-value 0.0744513
•
arw:awt with p-value 0.0725949
The reduce model for CR6 Time is in Figure 43.


---


## Page 167


150

Figure 42: Analysis B - CR6 Time OLS


---


## Page 168


151

Figure 43: Analysis B - CR6 Reduced OLS for Time


---


## Page 169


152
Based on these results (Figure 43), the following linear equation for CR6 time was
developed:
𝑇𝑖𝑚𝑒
= 39415.87499999855 + −79138.51046393832 ∗𝑋1 + −128.19137670175314 ∗𝑋2
+ −8860.849838411767 ∗𝑋5 + −46255.95567867106 ∗𝑋1 ∗𝑋3 + 12299.502666120085
∗𝑋1 ∗𝑋4 + 29085.416666666522 ∗𝑋1 ∗𝑋5 + 434.58559556786804 ∗𝑋2 ∗𝑋3
+ −57.717904019688284 ∗𝑋2 ∗𝑋4 + −11377.20914127423 ∗𝑋3 ∗𝑋5
The values utilized for the 𝜖-constraint methodology for Analysis B were:
Minimize:
•
𝑓1 = 0.43619166666666676 + −0.3303957650272835 ∗𝑋1 +
−0.0018884142076504296 ∗𝑋2 + 0.3583517213114778 ∗𝑋4 +
0.2018153688524602 ∗𝑋5 + 0.00379166666666636 ∗𝑋1 ∗𝑋2 +
−0.8282295081967748 ∗𝑋1 ∗𝑋3 + 0.19062500000000449 ∗𝑋1 ∗𝑋4 +
0.009283737704918856 ∗𝑋2 ∗𝑋3 + −0.0030125000000000516 ∗𝑋2 ∗𝑋4 +
0.00113750000000004 ∗𝑋2 ∗𝑋5 + 0.4151163934426205 ∗𝑋3 ∗𝑋4 +
−0.5256393442622931 ∗𝑋3 ∗𝑋5 + −0.25406250000000025 ∗𝑋4 ∗𝑋5
•
𝑓2 = 39415.87499999855 + −79138.51046393832 ∗𝑋1 +
−128.19137670175314 ∗𝑋2 + −8860.849838411767 ∗𝑋5 +
−46255.95567867106 ∗𝑋1 ∗𝑋3 + 12299.502666120085 ∗𝑋1 ∗𝑋4 +
29085.416666666522 ∗𝑋1 ∗𝑋5 + 434.58559556786804 ∗𝑋2 ∗𝑋3 +
−57.717904019688284 ∗𝑋2 ∗𝑋4 + −11377.20914127423 ∗𝑋3 ∗𝑋5


---


## Page 170


153
st:
•
.16 ≤𝑋1 ≤.28
•
50 ≤𝑋2 ≤60
•
.15 ≤𝑋3 ≤.25
•
. 4 ≤𝑋4 ≤.8
•
.8 ≤𝑋5 ≤1.2
When solved, 𝜖-contraints methodology produces the following values:
•
(𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5) =
S0.28000000999993935,60.000000599972694,0.2500000099939384,
0.8000000096771722,1.2000000119993277
T
•
𝑓1 = 0.5656472935545355
•
𝑓2 = 8557.622612553769
Where:
•
• X1 = layer height = .28 mm
•
• X2 = print speed = 60 mm/s
•
• X3 = infill density = .25
•
• X4 = raster width = .8 mm
•
• X5 = wall thickness = 1.2 mm
•
• f1 = cost = 0.5656472935545355
•
• f2 = time = 8557.622612553769 s
The settings in Analysis B match those of Analysis A.


---


## Page 171


154
As a last step the proposed setting were printed three (3) times. In a review of the of the
quality of the print, it was found to be excellent with a score of 450.
6.2.2.2 — Experimental Analysis B - SWX1
Based on the raw collected results (Table 13 and Table 14). The initial results (Figure
44) for the SWX1 Cost OLS model shows that several of the primary effects of the
experiments are not statistically significant.
The variables that are not significant factors in the cost of the model include:
•
alh:aid with p-value 0.818098
•
aps:arw with p-value 0.643285
•
alh:arw with p-value 0.485085
•
aps with p-value 0.251449
•
aid:arw with p-value 0.164261
The reduced OLS for the SWX1 cost is shown in Figure 45. As can be noted in Figure
45, all of the remaining first-order parameters and second-order interactions have a
significant impact of the cost of the model.
Based on these results (Figure 45), the following linear equation for SWX1 cost was
developed:


---


## Page 172


155

Figure 44: Analysis B - SWX1 Cost OLS


---


## Page 173


156

Figure 45: Analysis B - SWX1 Reduced OLS for Cost


---


## Page 174


157
𝐶𝑜𝑠𝑡
= 0.24752499999999666 + 0.08528056112224291 ∗𝑋1 + 0.4780490981963954 ∗𝑋3
+ 0.3561250000000017 ∗𝑋4 + 0.32446325985304236 ∗𝑋5 + 0.001151052104208572
∗𝑋1 ∗𝑋2 + −0.21041666666666942 ∗𝑋1 ∗𝑋5 + −0.0010537742150968782 ∗𝑋2 ∗𝑋3
+ −0.0002772211088844477 ∗𝑋2 ∗𝑋5 + −0.2500000000000011 ∗𝑋3 ∗𝑋5
+ −0.29625000000000157 ∗𝑋4 ∗𝑋5
This function was utilized in the 𝜖-constraints calculations.
The analysis for SWX1 Time OLS were obtained (Figure 46).
The variables that are not significant factors in the throughput of the model include:
•
aps:arw with p-value 0.899404
•
alh:awt with p-value 0.760839
•
aid:awt with p-value 0.641928
•
aid:arw with p-value 0.54847
•
awt with p-value 0.362301
•
alh:aid with p-value 0.23091
•
alh:arw with p-value 0.223997
•
aps:aid with p-value 0.0884672
The reduce model for SWX1 Time is in Figure 47.


---


## Page 175


158

Figure 46: Analysis B - SWX1 Time OLS


---


## Page 176


159

Figure 47: Analysis B - SWX1 Reduced OLS for Time


---


## Page 177


160
Based on these results (Figure 47), the following linear equation for SWX1 time was
developed:
𝑇𝑖𝑚𝑒
= 41311.84166666333 + −99242.9166666657 ∗𝑋1 + −181.67424724344346 ∗𝑋2
+ 4263.500000000091 ∗𝑋3 + −9967.93702290074 ∗𝑋4 + 815.0694444444525 ∗𝑋1
∗𝑋2 + −116.4993638676806 ∗𝑋2 ∗𝑋5 + 8583.812022900747 ∗𝑋4 ∗𝑋5
The values utilized for the 𝜖-constraint methodology for Analysis B were:
Minimize:
•
𝑓1 = 0.24752499999999666 + 0.08528056112224291 ∗𝑋1 +
0.4780490981963954 ∗𝑋3 + 0.3561250000000017 ∗𝑋4 +
0.32446325985304236 ∗𝑋5 + 0.001151052104208572 ∗𝑋1 ∗𝑋2 +
−0.21041666666666942 ∗𝑋1 ∗𝑋5 + −0.0010537742150968782 ∗𝑋2 ∗𝑋3 +
−0.0002772211088844477 ∗𝑋2 ∗𝑋5 + −0.2500000000000011 ∗𝑋3 ∗𝑋5 +
−0.29625000000000157 ∗𝑋4 ∗𝑋5
•
𝑓2 = 41311.84166666333 + −99242.9166666657 ∗𝑋1 +
−181.67424724344346 ∗𝑋2 + 4263.500000000091 ∗𝑋3 +
−9967.93702290074 ∗𝑋4 + 815.0694444444525 ∗𝑋1 ∗𝑋2 +
−116.4993638676806 ∗𝑋2 ∗𝑋5 + 8583.812022900747 ∗𝑋4 ∗𝑋5
st:
•
.16 ≤𝑋1 ≤.28
•
50 ≤𝑋2 ≤60


---


## Page 178


161
•
.15 ≤𝑋3 ≤.25
•
. 4 ≤𝑋4 ≤.8
•
.8 ≤𝑋5 ≤1.2
When solved, 𝜖-contraints methodology produces the following values:
•
(𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5) =
S0.28000000999993796,72.00000071997286,0.1499999900005892,
0.3999999900070408,1.2000000119995038
T
•
𝑓1 = 0.6048893778398489
•
𝑓2 = 7582.113544009455
Where:
•
• X1 = layer height = .28 mm
•
• X2 = print speed = 72 mm/s
•
• X3 = infill density = .15
•
• X4 = raster width = .4 mm
•
• X5 = wall thickness = 1.2 mm
•
• f1 = cost = 0.6048893778398489
•
• f2 = time = 7582.113544009455 s
The settings in Analysis B match those of Analysis A.
As a last step the proposed setting were printed three (3) times. In a review of the of the
quality of the print, it was found to be excellent with a score of 450.


---


## Page 179


162
6.2.3 — EXPERIMENTAL ANALYSIS C
Optimization of cost+power and time and review the results for quality
In this set of analysis, I will review the ideal print parameters for cost and time with the
addition of rework time and costs to address quality issues. Once the ideal parameters
are identified, test prints will be created, and quality will be assessed.
The rework results are listed in Appendix A.
6.2.3.1 — Experimental Analysis C - CR6
The initial results (Figure 48) for the CR6 Cost OLS model shows that several of the
effects are not statistically significant. The variables that are not significant factors in the
cost of the model include:
•
alh:aps with p-value 0.901841
•
aid with p-value 0.77787
•
alh:aid with p-value 0.475609
•
alh:arw with p-value 0.444672
•
aps with p-value 0.294638
•
aps:awt with p-value 0.351045
•
alh with p-value 0.146827
•
alh:awt with p-value 0.362181
•
aid:arw with p-value 0.11887
•
arw:awt with p-value 0.116793


---


## Page 180


163
The reduced OLS for the CR6 cost is shown in Figure 49. As can be noted in Figure 49,
all the remaining first-order parameters and second-order interactions have a significant
impact of the cost of the model.
Based on these results (Figure 49), the following linear equation for CR6 cost was
developed:
𝐶𝑜𝑠𝑡
= 0.022179997348888314 + 0.9805362539766707 ∗𝑋4 + 0.4210264448568395 ∗𝑋5
+ 0.055398409331918294 ∗𝑋2 ∗𝑋3 + −0.016249522799575436 ∗𝑋2 ∗𝑋4
+ −2.5398197242841984 ∗𝑋3 ∗𝑋5
This function was utilized in the 𝜖-constraints calculations.
The analysis for CR6 Time OLS were obtained (Figure 50).
The variables that are not significant factors in the time OLS model include:
•
aps:awt with p-value 0.679939
•
aid with p-value 0.642097
•
arw with p-value 0.529019
•
aid:arw with p-value 0.112705
•
alh:aps with p-value 0.0748668
•
arw:awt with p-value 0.0727373
The reduce model for CR6 Time is in Figure 51.
Based on these results (Figure 51), the following linear equation for CR6 time was
developed:


---


## Page 181


164

Figure 48: Analysis C - CR6 Cost OLS


---


## Page 182


165

Figure 49: Analysis C - CR6 Reduced OLS for Cost


---


## Page 183


166

Figure 50: Analysis C - CR6 Time OLS


---


## Page 184


167

Figure 51: Analysis C - CR6 Reduced OLS for Time


---


## Page 185


168
𝑇𝑖𝑚𝑒
= 39383.12499999856 + −78995.06592013844 ∗𝑋1 + −129.4773731249602 ∗𝑋2
+ −8759.911472760796 ∗𝑋5 + −45752.146814405125 ∗𝑋1 ∗𝑋3
+ 12225.825471698428 ∗𝑋1 ∗𝑋4 + 28897.916666666522 ∗𝑋1 ∗𝑋5
+ 440.7227146814413 ∗𝑋2 ∗𝑋3 + −57.37028301886791 ∗𝑋2 ∗𝑋4
+ −11750.650969529073 ∗𝑋3 ∗𝑋5
The values utilized for the 𝜖-constraint methodology for Analysis B were:
Minimize:
•
𝑓1 = 0.022179997348888314 + 0.9805362539766707 ∗𝑋4 +
0.4210264448568395 ∗𝑋5 + 0.055398409331918294 ∗𝑋2 ∗𝑋3 +
−0.016249522799575436 ∗𝑋2 ∗𝑋4 + −2.5398197242841984 ∗𝑋3 ∗𝑋5
•
𝑓2 = 39383.12499999856 + −78995.06592013844 ∗𝑋1 +
−129.4773731249602 ∗𝑋2 + −8759.911472760796 ∗𝑋5 +
−45752.146814405125 ∗𝑋1 ∗𝑋3 + 12225.825471698428 ∗𝑋1 ∗𝑋4 +
28897.916666666522 ∗𝑋1 ∗𝑋5 + 440.7227146814413 ∗𝑋2 ∗𝑋3 +
−57.37028301886791 ∗𝑋2 ∗𝑋4 + −11750.650969529073 ∗𝑋3 ∗𝑋5
st:
•
.16 ≤𝑋1 ≤.28
•
50 ≤𝑋2 ≤60
•
.15 ≤𝑋3 ≤.25
•
. 4 ≤𝑋4 ≤.8


---


## Page 186


169
•
.8 ≤𝑋5 ≤1.2
When solved, 𝜖-contraints methodology produces the following values:
•
(𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5) =
S0.2800000099999455,60.00000059996157,0.25000000999464544,
0.800000009867982,1.200000011999305
T
•
𝑓1 = 0.6008938634299353
•
𝑓2 = 8557.622612553769
Where:
•
• X1 = layer height = .28 mm
•
• X2 = print speed = 60 mm/s
•
• X3 = infill density = .25
•
• X4 = raster width = .8 mm
•
• X5 = wall thickness = 1.2 mm
•
• f1 = cost = 0.6008938634299353
•
• f2 = time = 8557.622612553769 s
The settings in Analysis C match those of Analysis A.
As a last step the proposed setting were printed three (3) times. In a review of the of the
quality of the print, it was found to be excellent with a score of 450.


---


## Page 187


170
6.2.3.2 — Experimental Analysis C - SWX1
The initial results (Figure 52) for the SWX1 Cost OLS model shows that several of the
primary effects of the experiments are not statistically significant.
The variables that are not significant factors in the cost of the model include:
•
arw with p-value 0.834584
•
alh:awt with p-value 0.723342
•
aid with p-value 0.253413
The reduced OLS for the SWX1 cost is shown in Figure 53. As can be noted in Figure
53, all the remaining first-order parameters and second-order interactions have a
significant impact of the cost of the model.
Based on these results (Figure 53), the following linear equation for SWX1 cost was
developed:
𝐶𝑜𝑠𝑡
= −7.512756311165274 + 15.594282277667375 ∗𝑋1 + 0.1501013849966114 ∗𝑋2
+ 3.3568541135900944 ∗𝑋5 + −0.1873958333333725 ∗𝑋1 ∗𝑋2 + 14.97406461978116
∗𝑋1 ∗𝑋3 + −6.3471031138125085 ∗𝑋1 ∗𝑋4 + −0.17544472807322514 ∗𝑋2 ∗𝑋3
+ 0.02025357325229224 ∗𝑋2 ∗𝑋4 + −0.07640624999999765 ∗𝑋2 ∗𝑋5
+ 3.2956081485919615 ∗𝑋3 ∗𝑋4 + 6.441435526274299 ∗𝑋3 ∗𝑋5
+ −0.6702353647414601 ∗𝑋4 ∗𝑋5
This function was utilized in the 𝜖-constraints calculations.
The analysis for SWX1 Time OLS were obtained (Figure 54).


---


## Page 188


171

Figure 52: Analysis C - SWX1 Cost OLS


---


## Page 189


172

Figure 53: Analysis C - SWX1 Reduced OLS for Cost


---


## Page 190


173

Figure 54: Analysis C - SWX1 Time OLS


---


## Page 191


174
The variables that are not significant factors in the cost of the model include:
•
aps:arw with p-value 0.851224
•
aid:awt with p-value 0.800387
•
alh:awt with p-value 0.742837
•
awt with p-value 0.494038
•
aid:arw with p-value 0.478725
•
alh:arw with p-value 0.316918
•
alh:aid with p-value 0.288586
•
aps:aid with p-value 0.0661897
The reduce model for SWX1 Time is in Figure 55.
Based on these results (Figure 55), the following linear equation for SWX1 time was
developed:
𝑇𝑖𝑚𝑒
= 40760.716666663415 + −96855.41666666564 ∗𝑋1 + −171.22354749789565 ∗𝑋2
+ 4256.00000000009 ∗𝑋3 + −10004.306297709902 ∗𝑋4 + 784.8611111111159 ∗𝑋1
∗𝑋2 + −118.74173027989448 ∗𝑋2 ∗𝑋5 + 8599.556297709905 ∗𝑋4 ∗𝑋5
The values utilized for the 𝜖-constraint methodology for Analysis B were:
Minimize:
•
𝑓1 = −7.512756311165274 + 15.594282277667375 ∗𝑋1 +
0.1501013849966114 ∗𝑋2 + 3.3568541135900944 ∗𝑋5 +
−0.1873958333333725 ∗𝑋1 ∗𝑋2 + 14.97406461978116 ∗𝑋1 ∗𝑋3 +


---


## Page 192


175

Figure 55: Analysis C - SWX1 Reduced OLS for Time


---


## Page 193


176
−6.3471031138125085 ∗𝑋1 ∗𝑋4 + −0.17544472807322514 ∗𝑋2 ∗𝑋3
+ 0.02025357325229224 ∗𝑋2 ∗𝑋4 + −0.07640624999999765 ∗𝑋2 ∗𝑋5
+ 3.2956081485919615 ∗𝑋3 ∗𝑋4 + 6.441435526274299 ∗𝑋3 ∗𝑋5
+ −0.6702353647414601 ∗𝑋4 ∗𝑋5
•
𝑓2 = 40760.716666663415 + −96855.41666666564 ∗𝑋1 +
−171.22354749789565 ∗𝑋2 + 4256.00000000009 ∗𝑋3 +
−10004.306297709902 ∗𝑋4 + 784.8611111111159 ∗𝑋1 ∗𝑋2 +
−118.74173027989448 ∗𝑋2 ∗𝑋5 + 8599.556297709905 ∗𝑋4 ∗𝑋5
st:
•
.16 ≤𝑋1 ≤.28
•
50 ≤𝑋2 ≤60
•
.15 ≤𝑋3 ≤.25
•
. 4 ≤𝑋4 ≤.8
•
.8 ≤𝑋5 ≤1.2
When solved, 𝜖-contraints methodology produces the following values:
•
(𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5) =
S0.2800000099999376,72.00000071997307,0.14999999000059022,
0.39999999000739667,1.2000000119995191
T
•
𝑓1 = 0.9517842950707984
•
𝑓2 = 7641.0830096684
Where:
•
• X1 = layer height = .28 mm


---


## Page 194


177
•
• X2 = print speed = 72 mm/s
•
• X3 = infill density = .15
•
• X4 = raster width = .4 mm
•
• X5 = wall thickness = 1.2 mm
•
• f1 = cost = 0.9517842950707984
•
• f2 = time = 7641.0830096684 s
The settings in Analysis C match those of Analysis A.
As a last step the proposed setting were printed three (3) times. In a review of the of the
quality of the print, it was found to be excellent with a score of 450.
6.3 — ADDRESSING THE RESEARCH QUESTIONS
6.3.1 — PRIMARY PROBLEMS ADDRESSED
What parameters should be optimized to increase speed, reduce costs, and achieve
satisfactory quality?
In the case of the CR6, the optimized parameters were:
•
(𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5) =
S0.28000000999993935,60.000000599972694,0.2500000099939384,
0.8000000096771722,1.2000000119993277
T
Where:
•
• X1 = layer height = .28 mm
•
• X2 = print speed = 60 mm/s
•
• X3 = infill density = .25


---


## Page 195


178
•
• X4 = raster width = .8 mm
•
• X5 = wall thickness = 1.2 mm
Both the infill density and wall thickness did not use the expected values. Both were the
opposite of the expected. In the case of infill density, this result is more surprising. It is
believed that this result is due to the minimal amount of infill in the model. Using Cura, a
preview was generated of the optimized print (Figure 56). This figure shows the model
at layer 35 of 71. The infill density, represented in orange, is extremely minimal.
Additionally, the Cura generated rough estimate of print time shows the infill as 1% of
overall print time (Figure 57).
In the case of models with significantly more infill, it is expected that the result would
meet expectations.
The optimized parameters for the SWX1 were:
•
(𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5) =
S0.28000000999993796,72.00000071997286,0.1499999900005892,
0.39999999000704073,1.2000000119995038
T
Where:
•
• X1 = layer height = .28 mm
•
• X2 = print speed = 72 mm/s
•
• X3 = infill density = .15
•
• X4 = raster width = .4 mm
•
• X5 = wall thickness = 1.2 mm


---


## Page 196


179

Figure 56: CR6 Cura Preview at 35 of 71 Layers


---


## Page 197


180


Figure 57: CR6 Cura Time Estimate


---


## Page 198


181
In the case of the SWX1, both the raster width and wall thickness were not as expected.
It is believed that these unexpected values can be explained as compromises due to the
optimization of cost and time.
What is the contribution of each parameter to the increase speed, reduce costs, and
achieve satisfactory quality?
In the case of both printers, layer height and print speed are shown to have an impact
on cost and time. The linear equation for each printer in each analysis, gives an
indication of the contribution of each variable for cost and time.
CR6 Analysis A
𝐶𝑜𝑠𝑡
= 0.30061301677651686 + −0.0014979526099359666 ∗𝑋2 + 0.3541048685686145
∗𝑋4 + 0.24600811428103486 ∗𝑋5 + 0.003193676289093103 ∗𝑋1 ∗𝑋2
+ −0.681545835829839 ∗𝑋1 ∗𝑋3 + 0.15813870197108404 ∗𝑋1 ∗𝑋4
+ −0.15310216338152616 ∗𝑋1 ∗𝑋5 + 0.008101719131677326 ∗𝑋2 ∗𝑋3
+ −0.0026250000000000544 ∗𝑋2 ∗𝑋4 + 0.0011250000000000322 ∗𝑋2 ∗𝑋5
+ 0.3961480849887108 ∗𝑋3 ∗𝑋4 + −0.4897531916854896 ∗𝑋3 ∗𝑋5
+ −0.2593750000000006 ∗𝑋4 ∗𝑋5
𝑇𝑖𝑚𝑒
= 39415.87499999855 + −79138.51046393832 ∗𝑋1 + −128.19137670175314 ∗𝑋2
+ −8860.849838411767 ∗𝑋5 + −46255.95567867106 ∗𝑋1 ∗𝑋3 + 12299.502666120085
∗𝑋1 ∗𝑋4 + 29085.416666666522 ∗𝑋1 ∗𝑋5 + 434.58559556786804 ∗𝑋2 ∗𝑋3
+ −57.717904019688284 ∗𝑋2 ∗𝑋4 + −11377.20914127423 ∗𝑋3 ∗𝑋5


---


## Page 199


182
SWX1 Analysis A
𝐶𝑜𝑠𝑡
= 0.1900000000000014 + 0.24999999999999423 ∗𝑋1 + 0.3999999999999986 ∗𝑋3
+ 0.37499999999999967 ∗𝑋4 + 0.320833333333332 ∗𝑋5 + −0.20833333333332477
∗𝑋1 ∗𝑋5 + −0.25000000000000133 ∗𝑋3 ∗𝑋5 + −0.3124999999999999 ∗𝑋4 ∗𝑋5
𝑇𝑖𝑚𝑒
= 41311.84166666333 + −99242.9166666657 ∗𝑋1 + −181.67424724344346 ∗𝑋2
+ 4263.500000000091 ∗𝑋3 + −9967.93702290074 ∗𝑋4 + 815.0694444444525 ∗𝑋1
∗𝑋2 + −116.4993638676806 ∗𝑋2 ∗𝑋5 + 8583.812022900747 ∗𝑋4 ∗𝑋5
CR6 Analysis B
𝐶𝑜𝑠𝑡
= 0.43619166666666676 + −0.3303957650272835 ∗𝑋1 + −0.0018884142076504296
∗𝑋2 + 0.3583517213114778 ∗𝑋4 + 0.2018153688524602 ∗𝑋5
+ 0.00379166666666636 ∗𝑋1 ∗𝑋2 + −0.8282295081967748 ∗𝑋1 ∗𝑋3
+ 0.19062500000000449 ∗𝑋1 ∗𝑋4 + 0.009283737704918856 ∗𝑋2 ∗𝑋3
+ −0.0030125000000000516 ∗𝑋2 ∗𝑋4 + 0.00113750000000004 ∗𝑋2 ∗𝑋5
+ 0.4151163934426205 ∗𝑋3 ∗𝑋4 + −0.5256393442622931 ∗𝑋3 ∗𝑋5
+ −0.25406250000000025 ∗𝑋4 ∗𝑋5


---


## Page 200


183
𝑇𝑖𝑚𝑒
= 39415.87499999855 + −79138.51046393832 ∗𝑋1 + −128.19137670175314 ∗𝑋2
+ −8860.849838411767 ∗𝑋5 + −46255.95567867106 ∗𝑋1 ∗𝑋3 + 12299.502666120085
∗𝑋1 ∗𝑋4 + 29085.416666666522 ∗𝑋1 ∗𝑋5 + 434.58559556786804 ∗𝑋2 ∗𝑋3
+ −57.717904019688284 ∗𝑋2 ∗𝑋4 + −11377.20914127423 ∗𝑋3 ∗𝑋5
SWX1 Analysis B
𝐶𝑜𝑠𝑡
= 0.24752499999999666 + 0.08528056112224291 ∗𝑋1 + 0.4780490981963954 ∗𝑋3
+ 0.3561250000000017 ∗𝑋4 + 0.32446325985304236 ∗𝑋5 + 0.001151052104208572
∗𝑋1 ∗𝑋2 + −0.21041666666666942 ∗𝑋1 ∗𝑋5 + −0.0010537742150968782 ∗𝑋2 ∗𝑋3
+ −0.0002772211088844477 ∗𝑋2 ∗𝑋5 + −0.2500000000000011 ∗𝑋3 ∗𝑋5
+ −0.29625000000000157 ∗𝑋4 ∗𝑋5
𝑇𝑖𝑚𝑒
= 41311.84166666333 + −99242.9166666657 ∗𝑋1 + −181.67424724344346 ∗𝑋2
+ 4263.500000000091 ∗𝑋3 + −9967.93702290074 ∗𝑋4 + 815.0694444444525 ∗𝑋1
∗𝑋2 + −116.4993638676806 ∗𝑋2 ∗𝑋5 + 8583.812022900747 ∗𝑋4 ∗𝑋5
CR6 Analysis C
𝐶𝑜𝑠𝑡
= 0.022179997348888314 + 0.9805362539766707 ∗𝑋4 + 0.4210264448568395 ∗𝑋5
+ 0.055398409331918294 ∗𝑋2 ∗𝑋3 + −0.016249522799575436 ∗𝑋2 ∗𝑋4
+ −2.5398197242841984 ∗𝑋3 ∗𝑋5


---


## Page 201


184
𝑇𝑖𝑚𝑒
= 39383.12499999856 + −78995.06592013844 ∗𝑋1 + −129.4773731249602 ∗𝑋2
+ −8759.911472760796 ∗𝑋5 + −45752.146814405125 ∗𝑋1 ∗𝑋3
+ 12225.825471698428 ∗𝑋1 ∗𝑋4 + 28897.916666666522 ∗𝑋1 ∗𝑋5
+ 440.7227146814413 ∗𝑋2 ∗𝑋3 + −57.37028301886791 ∗𝑋2 ∗𝑋4
+ −11750.650969529073 ∗𝑋3 ∗𝑋5
SWX1 Analysis C
𝐶𝑜𝑠𝑡
= −7.512756311165274 + 15.594282277667375 ∗𝑋1 + 0.1501013849966114 ∗𝑋2
+ 3.3568541135900944 ∗𝑋5 + −0.1873958333333725 ∗𝑋1 ∗𝑋2 + 14.97406461978116
∗𝑋1 ∗𝑋3 + −6.3471031138125085 ∗𝑋1 ∗𝑋4 + −0.17544472807322514 ∗𝑋2 ∗𝑋3
+ 0.02025357325229224 ∗𝑋2 ∗𝑋4 + −0.07640624999999765 ∗𝑋2 ∗𝑋5
+ 3.2956081485919615 ∗𝑋3 ∗𝑋4 + 6.441435526274299 ∗𝑋3 ∗𝑋5
+ −0.6702353647414601 ∗𝑋4 ∗𝑋5
𝑇𝑖𝑚𝑒
= 40760.716666663415 + −96855.41666666564 ∗𝑋1 + −171.22354749789565 ∗𝑋2
+ 4256.00000000009 ∗𝑋3 + −10004.306297709902 ∗𝑋4 + 784.8611111111159 ∗𝑋1
∗𝑋2 + −118.74173027989448 ∗𝑋2 ∗𝑋5 + 8599.556297709905 ∗𝑋4 ∗𝑋5
Where, in all cases:
•
• X1 = layer height
•
• X2 = print speed
•
• X3 = infill density


---


## Page 202


185
•
• X4 = raster width
•
• X5 = wall thickness
6.3.2 — SECONDARY PROBLEMS ADDRESSED
Because of the subjective nature of quality inspection, what is an acceptable
methodology to quantify the quality of a 3D printed model?
Using the quality assessment methodology outlined in ~.• — The Inspection Score and
~.~ — Inspection Measurements sections, a quick and easy quality scoring method was
obtained.
Accessibility of the optimization methodologies remains the domain of engineers. Can
the optimization method utilized in this study be made accessible to makers?
Utilizing open-source tools such as python and jupyter notebooks, it is possible to
create a set of tools to allow for makers to run additional experiments. This study
demonstrates two (2) areas that could be improved. These areas are:
•
Automation of the addition of the linear equation to the 𝜖-constraints function
Figure 58.
•
Reduction of the number of experimental runs
In the case of automation, in each case, the linear equation for cost and time developed
must be manually cut and paste into the 𝜖-constraints function in the jupyter notebook
Figure 58. In the initial analysis, I made the mistake of not updating the equations. By
automating this process, it can eliminate future mistakes.


---


## Page 203


186

Figure 58: Section Requiring Cut and Paste to add Linear equation to python function


---


## Page 204


187
The experiments needed to complete this analysis are resource intensive in the case of
both the time and filament needed to complete these experiments and analysis. Work
needs to be done to reduce the resource usage.
Does the additive nature of FDM allow for the quick elimination of print parameters?
Based on the quality results, the quality of the models varied greater than expected.
There does not seem to be a correlation with a particular print parameter and the quality
score.
It was found that there was a difference between the printers. The SWX1 was found to
have a greater difference in the various quality scores.


---


## Page 205


188
7 — CHAPTER SEVEN - CONCLUSIONS AND
RECOMMENDATIONS
7.1 — CONCLUSIONS
This research demonstrates the use of design of experiments (DOE) and 𝜖-constraints
methodology to optimize multiple parameters in 3DP. The methods utilized in this
research use open-source technologies to accomplish the optimization. The methods
are straight forward and offer a blueprint for future optimization experiments and
research for makers.
The quality scoring identified in this study offer a standardized method to assess the
quality of 3DP models. This method is particularly important for use in settings outside
of the laboratory. It follows the methodologies currently employed by the maker
community.
As outlined in the ~.~ — Inspection Measurements section, a mold was used to assist
with the assessment of functionality. It was found during this investigation that the mold
was not particularly informative. A better indicator of quality was the three (3)
measurements utilized.
An interesting observation of this research is the fact that Analysis A, B, and C all
identify the same settings as optimal. When reviewing the various value changes due to
the inclusion of power usage and rework cost/time, the results are particularly
surprising.


---


## Page 206


189
In the case of the CR6, the optimized parameters were:
•
(𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5) =
S0.28000000999993935,60.000000599972694,0.2500000099939384,
0.8000000096771722,1.2000000119993277
T
Where:
•
• X1 = layer height = .28 mm
•
• X2 = print speed = 60 mm/s
•
• X3 = infill density = .25
•
• X4 = raster width = .8 mm
•
• X5 = wall thickness = 1.2 mm
he optimized parameters for the SWX1 were:
•
(𝑋1, 𝑋2, 𝑋3, 𝑋4, 𝑋5) =
S0.28000000999993796,72.00000071997286,0.1499999900005892,
0.39999999000704073,1.2000000119995038
T
Where:
•
• X1 = layer height = .28 mm
•
• X2 = print speed = 72 mm/s
•
• X3 = infill density = .15
•
• X4 = raster width = .4 mm
•
• X5 = wall thickness = 1.2 mm


---


## Page 207


190
In the case of the CR6, infill density did not impact cost and time. This contrasts with the
SWX1 where infill density was optimized. It would be expected that both printers would
optimize the same parameters.
7.2 — RECOMMENDATIONS
Future research should review the following items:
•
Future research should utilize a variety of model geometries. In the case of infill
density, models should be selected with greater infill percentages.
•
The quality scoring methodology should be tested by other researchers. Effort
should be made to use the method in other settings.
•
In future studies, various inexpensive 3DP printers should be tested.
•
With the use of varied printers, the make and model should be included as a
variable.


---


## Page 208


191
LIST OF REFERENCES
Akçay, H., & Anagün, A. S. (2013). Multi response optimization application on a
manufacturing factory. Mathematical and Computational Applications, 18(3), 531-
538.
Baldwin, R., & Mauro, B. W. D. (2020). Economics in the Time of COVID-19.
Baumann, F. W., Schuermann, M., Odefey, U., & Pfeil, M. (2017). From gcode to stl:
Reconstruct models from 3d printing as a service.
Bhushan, B., & Caspers, M. (2017). An overview of additive manufacturing (3D printing)
for microfabrication. Microsystem Technologies, 23(4), 1117-1124.
Bishop, E. G., & Leigh, S. J. (2020). Using large-scale additive manufacturing as a
bridge manufacturing process in response to shortages in personal protective
equipment during the COVID-19 outbreak. International journal of bioprinting, 6(4).
BLS. (2020). State Employment and Unemployment Summary.
Bose, S., Ke, D., Sahasrabudhe, H., & Bandyopadhyay, A. (2018). Additive
manufacturing of biomaterials. Progress in materials science, 93, 45-111.
Bose, S., Vahabzadeh, S., & Bandyopadhyay, A. (2013). Bone tissue engineering using
3D printing. Materials today, 16(12), 496-504.
Bown, C. P. (2020). COVID-19: China’s exports of medical supplies provide a ray of
hope. PIIE Trade and Investment Policy Watch, March, 26.
Bradshaw, S., Bowyer, A., & Haufe, P. (2010b). The intellectual property implications of
low-cost 3D printing. ScriptEd, 7, 5.
Bradshaw, S., Bowyer, A., & Haufe, P. (2010b). The intellectual property implications of
low-cost 3D printing. ScriptEd, 7, 5.


---


## Page 209


192
Browder, R. E., Aldrich, H. E., & Bradley, S. W. (2019). The emergence of the maker
movement: Implications for entrepreneurship research. Journal of Business
Venturing.
Cascella, M., Rajnik, M., Cuomo, A., & Dulebohn…, S. C. (2020). Features, evaluation
and treatment coronavirus (COVID-19). Statpearls ….
CDC. (2020). Symptoms of Coronavirus. https://www.cdc.gov/coronavirus/2019-
nCoV/index.html.
Chang, D., Xu, H., Rebaza, A., Sharma, L., & Cruz, C. S. D. (2020). Protecting health-
care workers from subclinical coronavirus infection. The Lancet Respiratory
Medicine, 8(3), e13.
Christensen, R. (1996). Analysis of variance, design, and regression: applied statistical
methods. CRC Press.
Clark, P. A. (2020). ‘This Is Truly a Last Resort.’ Makers Are 3D Printing Ventilator Parts
and Sewing Masks Amid a Critical Shortage in Medical Supplies.
https://time.com/5811091/makers-3d-printing-coronavirus/.
Cox, J. L., & Koepsell, S. A. (2020). 3D-printing to address COVID-19 testing supply
shortages. Laboratory medicine, 51(4), e45-e46.
Dey, A., & Yodo, N. (2019). A systematic survey of FDM process parameter
optimization and their influence on part characteristics. Journal of Manufacturing
and Materials Processing, 3, 64.
Dordlofva, C., Lindwall, A., T\”orlind, P., & others. (2016). Opportunities and challenges
for additive manufacturing in space applications. DS 85-1: Proceedings of


---


## Page 210


193
NordDesign 2016, Volume 1, Trondheim, Norway, 10th-12th August 2016, 401-
410.
Drury, C. G., & Watson, J. (2002). Good practices in visual inspection. Human factors in
aviation maintenance-phase nine, progress report, FAA/Human Factors in Aviation
Maintenance.@ URL: http://hfskyway. faa. gov.
Durakovic, B. (2018). Design for additive manufacturing: Benefits, trends and
challenges. Periodicals of Engineering and Natural Sciences, 6(2), 179-191.
Emanuel, E. J., Persad, G., Upshur, R., Thome, B., Parker, M., Glickman, A. et al.
(2020). Fair allocation of scarce medical resources in the time of Covid-19.
FAA. (1997). VISUAL INSPECTION FOR AIRCRAFT. FAA AC 43-204.
Feldman, A. (2020). Inside A Silicon Valley Unicorn’s Urgent Dash To 3D-Print Face
Shields And Test Swabs To Battle COVID-19.
https://www.forbes.com/sites/amyfeldman/2020/03/25/inside-a-silicon-valley-
unicorns-urgent-dash-to-3d-print-face-shields-and-test-swabs-to-battle-covid-
19/#5f68b19c4370.
Fisher, R. A. (1992). Statistical methods for research workers Breakthroughs in
statistics. In (pp. 66-70). Springer.
Forest, C. R., Moore, R. A., Jariwala, A. S., & Fasse…, B. B. (2014). The Invention
Studio: A University Maker Space and Culture. Advances in Engineering ….
Gibson, I., Rosen, D., & Stucker, B. (2010). Additive Manufacturing Technologies –
Rapid Prototyping to Direct Digital Manufacturing (5).
Gibson, I., Rosen, D. W., & Stucker, B. (2014). Additive manufacturing technologies
(17). Springer.


---


## Page 211


194
Gu, P., Zhang, X., Zeng, Y., & Ferguson, B. (2001). Quality analysis and optimization of
solid ground curing process. Journal of manufacturing systems, 20(4), 250.
Gurrala, P. K., & Regalla, S. P. (2012). Optimization of support material and build time
in fused deposition modeling (FDM).
Halassi, S., Semeijn, J., & Kiratli, N. (2019). From consumer to prosumer: a supply
chain revolution in 3D printing. International Journal of Physical Distribution &
Logistics Management.
Holm, E. J. V. (2015). Makerspaces and contributions to entrepreneurship. Procedia-
Social and Behavioral Sciences.
Holman, W. (2015). Makerspace: Towards a new civic infrastructure. Places Journal.
Ingole, D. S., Deshmukh, T. R., Kuthe, A. M., & Ashtankar, K. M. (2011). Build
orientation analysis for minimum cost determination in FDM. Proceedings of the
Institution of Mechanical Engineers, Part B: Journal of Engineering Manufacture,
225(10), 1925-1938.
Johnson, G. A., & French, J. J. (2018). Evaluation of infill effect on mechanical
properties of consumer 3D printing materials. Advances in Technology Innovation,
3(4), 179.
Kačergis, L., Mitkus, R., & Sinapius, M. (2019). Influence of fused deposition modeling
process parameters on the transformation of 4D printed morphing structures.
Smart Materials and Structures, 28(10), 105042.
Klotz, L. E., Horman, M., & Bodenschatz, M. (2007). A lean modeling protocol for
evaluating green project delivery. Lean Construction Journal, 3(1).


---


## Page 212


195
Kluytmans-van den Bergh, M. F. Q., Buiting, A. G. M., Pas, S. D., Bentvelsen, R. G.,
van den Bijllaardt, W., van Oudheusden, A. J. G. et al. (2020). Prevalence and
clinical presentation of health care workers with symptoms of coronavirus disease
2019 in 2 Dutch hospitals during an early phase of the pandemic. JAMA network
open, 3(5), e209673-e209673.
Kluyver, T., Ragan-Kelley, B., Pérez, F., Granger, B. E., Bussonnier, M., Frederic, J. et
al. (2016). Jupyter Notebooks-a publishing format for reproducible computational
workflows.
Kruth, J.-P., Mercelis, P., Van Vaerenbergh, J., Froyen, L., & Rombouts, M. (2005).
Binding mechanisms in selective laser sintering and selective laser melting. Rapid
prototyping journal.
Kumar, L. J., & Nair, C. G. K. (2017). Current trends of additive manufacturing in the
aerospace industry Advances in 3d printing \& additive manufacturing
technologies. In (pp. 39-54). Springer.
Lai, X., Wang, M., Qin, C., Tan, L., Ran, L., Chen, D. et al. (2020). Coronavirus disease
2019 (COVID-2019) infection among health care workers and implications for
prevention measures in a tertiary hospital in Wuhan, China. JAMA Network Open,
3(5), e209666-e209666.
Larson, M. G. (2008). Analysis of variance. Circulation, 117(1), 115-121.
Li, Y., Linke, B. S., Voet, H., Falk, B., Schmitt, R., & Lam, M. (2017). Cost, sustainability
and surface roughness quality–A comprehensive analysis of products made with
personal 3D printers. CIRP Journal of Manufacturing Science and Technology, 16,
1-11.


---


## Page 213


196
LIANG, Q. I. N. G.-J. I. E., & LI, X. I. A. O.-D. O. N. G. (2017). Application of FDM
additive manufacturing technology in making medical surgical model. DEStech
Transactions on Engineering and Technology Research, ecame).
Livingston, E., Desai, A., & Berkwits, M. (2020). Sourcing personal protective equipment
during the COVID-19 pandemic. Jama, 323(19), 1912-1914.
Ludwig, T., Stickel, O., Boden, A., & Pipek, V. (2014). Towards sociable technologies:
an empirical study on designing appropriation infrastructures for 3D printing.
McCue, T. J. (2020). 3D Printer Groups Continue Working Round The Clock To Help
2020 PPE Shortage. https://www.forbes.com/sites/tjmccue/2020/03/30/protect-
healthcare-workers-3d-printer-groups-race-to-help-2020-ppe-shortage-
coronavirus-covid19/#76ccdb494ee2.
Mehta, P. S., Ocampo, J. S., Tovar, A., & Chaudhari, P. (2016). Bio-inspired design of
lightweight and protective structures.
Melchore, J. A. (2011). Sound practices for consistent human visual inspection. Aaps
Pharmscitech, 12(1), 215-221.
Merriam-Webster. (n.d.). Optimization. In Merriam-Webster.com dictionary. Retrieved
12/5/2020, https://www.merriam-webster.com/dictionary/optimization.
Mohamed, O. A., Masood, S. H., & Bhowmik, J. L. (2016a). Mathematical modeling and
FDM process parameters optimization using response surface methodology based
on Q-optimal design. Applied Mathematical Modelling.
Mohamed, O. A., Masood, S. H., & Bhowmik, J. L. (2016b). Parametric analysis of the
build cost for FDM additive processed parts using response surface methodology.
Ref. Modul. Mater. Sci. Mater. Eng.


---


## Page 214


197
Mohamed, O. A., Masood, S. H., & Bhowmik, J. L. (2018). Analysis of wear behavior of
additively manufactured PC-ABS parts. Materials Letters.
Montgomery, D. C. (2017). Design and analysis of experiments. John wiley & sons.
MP, G., Shinde, Y., Madaki, R., & Nadaf, S. (2019). IoT based 3D Printer.
Mwema, F. M., Akinlabi, E. T., & Fatoba, O. S. (2020). Visual assessment of 3D printed
elements: A practical quality assessment for home-made FDM products. Materials
Today: Proceedings.
Nasir, H., Ahmed, H., Haas, C., & Goodrum, P. M. (2014). An analysis of construction
productivity differences between Canada and the United States. Construction
Management and Economics, 32(6), 595-607.
Natrella, M. (2010). NIST/SEMATECH e-Handbook of Statistical Methods{Natrella,
2010, #87438}. Nist/Sematech, 49.
Ngo, T. D., Kashani, A., Imbalzano, G., Nguyen, K. T. Q., & Hui, D. (2018). Additive
manufacturing (3D printing): A review of materials, methods, applications and
challenges. Composites Part B: Engineering, 143, 172-196.
Nitti, D. F. (2019). 3D printing, challenges for the future of intellectual property rights.
tesi.luiss.it.
Novak, J. I., & Loy, J. (2020a). A critical review of initial 3D printed products responding
to COVID-19 health and supply chain challenges. Emerald Open Research, 2, 24.
Novak, J. I., & Loy, J. (2020b). A quantitative analysis of 3D printed face shields and
masks during COVID-19. Emerald Open Research, 2, 42.


---


## Page 215


198
Novakova-Marcincinova, L., & Kuric, I. (2012). Basic and advanced materials for fused
deposition modeling rapid prototyping technology. Manuf. and Ind. Eng, 11(1), 24-
27.
Papavlasopoulou, S., Giannakos, M. N., & Jaccheri, L. (2017). Empirical studies on the
Maker Movement, a promising approach to learning: A literature review.
Entertainment Computing, 18, 57-78.
Patil, P., Singh, D., Raykar, S. J., & Bhamu, J. (2021). Multi-objective optimization of
process parameters of Fused Deposition Modeling (FDM) for printing Polylactic
Acid (PLA) polymer components. Materials Today: Proceedings.
Paul, S. K., & Chowdhury, P. (2020). A production recovery plan in manufacturing
supply chains for a high-demand item during COVID-19. International Journal of
Physical Distribution & Logistics Management.
Pohlman, J. T., & Leitner, D. W. (2003). A comparison of ordinary least squares and
logistic regression.
Popescu, D., Zapciu, A., Amza, C., Baciu, F., & Marinescu, R. (2018). FDM process
parameters influence over the mechanical properties of polymer specimens: A
review. Polymer Testing.
Research, P. (2020). Prusa Face Shield. https://www.prusaprinters.org/prints/25857-
prusa-face-shield.
Qureshi, A. J., Mahmood, S., & Wong…, W. L. E. (2015). Design for Scalability and
Strength Optimisation for components created through FDM process. DS 80-6
Proceedings ….


---


## Page 216


199
Ramananantoandro, T., Larricq, P., & Eterradossi, O. (2014). Relationships between 3D
roughness parameters and visuotactile perception of surfaces of maritime
pinewood and MDF. Holzforschung, 68(1), 93-101.
Rayna, T., Striukova, L., & Darlington, J. (2015). Co-creation and user innovation: The
role of online 3D printing platforms. Journal of Engineering and Technology
Management, 37, 90-102.
Rio-Chanona, R. M. D., Mealy, P., & Pichler…, A. (2020). Supply and demand shocks in
the COVID-19 pandemic: An industry and occupation perspective. arXiv preprint
arXiv ….
Romero, L., Guerrero, A., Espinosa, M. M., Jimenez, M., Dominguez, I. A., &
Dominguez, M. (2014). Additive manufacturing with RepRap methodology: current
situation and future prospects.
Salmi, M., Akmal, J. S., Pei, E., Wolff, J., Jaribion, A., & Khajavi, S. H. (2020). 3D
printing in COVID-19: productivity estimation of the most promising open source
solutions in emergency situations. Applied Sciences, 10(11), 4004.
Salvendy, G. (2001). Handbook of Industrial Engineering. John Wiley \& Sons.
Shi, Y., Yu, X., Zhao, H., Wang, H., Zhao, R., & Sheng, J. (2020). Host susceptibility to
severe COVID-19 and establishment of a host risk score: findings of 487 cases
outside Wuhan. Critical Care, 24(1), 1-4.
Singhal, T. (2020). A review of coronavirus disease-2019 (COVID-19). The Indian
Journal of Pediatrics, 1-6.
Šljivic, M., Pavlovic, A., Kraišnik, M., & Ilić, J. (2019). Comparing the accuracy of 3D
slicer software in printed enduse parts.


---


## Page 217


200
Šljivic, M., Pavlovic, A., & Kraišnik…, M. (2019). Comparing the accuracy of 3D slicer
software in printed enduse parts. IOP Conference Series ….
Sohrabi, C., Alsafi, Z., O’Neill, N., Khan, M., Kerwan, A., Al-Jabir, A. et al. (2020). World
Health Organization declares global emergency: A review of the 2019 novel
coronavirus (COVID-19). International Journal of Surgery.
Solomon, I. J., Sevvel, P., & Gunasekaran, J. (2020). A review on the various
processing parameters in FDM. Materials Today: Proceedings.
Stănciulescu, Ş., Schulze, S., & Wąsowski, A. (2015). Forked and integrated variants in
an open-source firmware project.
Tamburin, A. (2020). Tennessee colleges mass producing face shields to guard against
coronavirus using 3D printers. Tennessean.
Taylor, W., Melloy, B., Dharwada, P., Gramopadhye, A., & Toler, J. (2004). The effects
of static multiple sources of noise on the visual search component of human
inspection. International journal of industrial ergonomics, 34(3), 195-207.
theone8480. (2018). required info on professional settings in cura.
https://community.ultimaker.com/topic/21507-required-info-on-professional-
settings-in-cura/.
Thompson, M. K., Moroni, G., Vaneker, T., Fadel, G., Campbell, R. I., Gibson, I. et al.
(2016). Design for Additive Manufacturing: Trends, opportunities, considerations,
and constraints. CIRP annals, 65(2), 737-760.
Tino, R., Moore, R., Antoline, S., Ravi, P., Wake, N., Ionita, C. N. et al. (2020). COVID-
19 and the role of 3D printing in medicine. 3D Printing in Medicine, 6(1).


---


## Page 218


201
Tofail, S. A. M., Koumoulos, E. P., Bandyopadhyay, A., Bose, S., O’Donoghue, L., &
Charitidis, C. (2018). Additive manufacturing: scientific and technological
challenges, market uptake and opportunities. Materials Today, 21(1), 22-37.
Tranter, J. B., Refalo, P., & Rochman, A. (2017). Towards sustainable injection molding
of ABS plastic products. Journal of Manufacturing Processes, 29, 399-406.
Valerga, A. P., Batista, M., Salguero, J., & Girot, F. (2018). Influence of PLA filament
conditions on characteristics of FDM parts. Materials, 11(8), 1322.
Vecchione, A., & Woltjer, G. (2020). How Library Maker Spaces Can #FlattentheCurve.
https://www.libraryjournal.com/?detailStory=how-library-maker-spaces-can-flatten-
the-curve-covid-19-coronavirus.
Warm, J. S., Parasuraman, R., & Matthews, G. (2008). Vigilance requires hard mental
work and is stressful. Human factors, 50(3), 433-441.
Wattanasaeng, N., & Ransikarbum, K. (2021). Model and Analysis of Economic-and
Risk-Based Objective Optimization Problem for Plant Location within Industrial
Estates Using Epsilon-Constraint Algorithms. Computation, 9(4), 46.
Wesemann, C., Pieralli, S., Fretwurst, T., Nold, J., & Nelson…, K. (2020). 3-d printed
protective equipment during covid-19 pandemic. Materials.
Westervelt, E. (2020). Can The U.S. Crowdsource Its Way Out Of A Mask Shortage?
No, But It Still Helps. https://www.npr.org/2020/03/25/820795727/can-the-u-s-
crowdsource-its-way-out-of-a-mask-shortage-no-but-it-still-helps.
WHO. (2020). WHO Coronavirus Disease (COVID-19) Dashboard.
https://covid19.who.int/table.


---


## Page 219


202
Wohlers, T., & Gornet, T. (2014). History of additive manufacturing. Wohlers report,
24(2014), 118.
Wu, P., Wang, J., & Wang, X. (2016). A critical review of the use of 3-D printing in the
construction industry. Automation in Construction, 68, 21-31.
Yin, D., Liu, Y., Padmanabhan, A., Terstriep, J., Rush, J., & Wang, S. (2017). A
CyberGIS-Jupyter Framework for Geospatial Analytics at Scale.
Yoon, H.-S., Lee, J.-Y., Kim, H.-S., Kim, M.-S., Kim, E.-S., Shin, Y.-J. et al. (2014). A
comparison of energy consumption in bulk forming, subtractive, and additive
processes: Review and case study. International Journal of Precision Engineering
and Manufacturing-Green Technology, 1(3), 261-279.
Zaharin, H. A., Rani, A. M. A., & Ginta…, T. L. (2018). Additive manufacturing
technology for biomedical components: A review. IOP Conf. Ser. Mater. Sci ….


---


## Page 220


203
APPENDIX
APPENDIX A - EXPERIMENTAL DATA
RAW RESULTS
Table 13: Raw Results for the CR-6 SE
trial alh
aps aid
arw awt rep cost time
1
0.16 50
0.25 0.4
0.8 1
0.51 18098
2
0.28 50
0.25 0.4
1.2 1
0.51 8741
3
0.16 60
0.25 0.4
1.2 1
0.54 14493
4
0.28 60
0.25 0.4
0.8 1
0.51 10191
5
0.16 50
0.15 0.4
1.2 1
0.54 14914
6
0.28 50
0.15 0.4
0.8 1
0.5
10423
7
0.16 60
0.15 0.4
0.8 1
0.5
16648
8
0.28 60
0.15 0.4
1.2 1
0.54 8534
9
0.16 50
0.25 0.8
1.2 1
0.54 15085
10
0.28 50
0.25 0.8
0.8 1
0.56 10624
11
0.16 60
0.25 0.8
0.8 1
0.56 16840
12
0.28 60
0.25 0.8
1.2 1
0.54 8645
13
0.16 50
0.15 0.8
0.8 1
0.54 17046
14
0.28 50
0.15 0.8
1.2 1
0.54 9012
15
0.16 60
0.15 0.8
1.2 1
0.53 13488


---


## Page 221


204
Table 13 Continued
trial alh
aps aid
arw awt rep cost time
16
0.28 60
0.15 0.8
0.8 1
0.54 9574
17
0.16 50
0.25 0.4
0.8 2
0.51 18042
18
0.28 50
0.25 0.4
1.2 2
0.51 8743
19
0.16 60
0.25 0.4
1.2 2
0.54 14469
20
0.28 60
0.25 0.4
0.8 2
0.51 10185
21
0.16 50
0.15 0.4
1.2 2
0.54 14873
22
0.28 50
0.15 0.4
0.8 2
0.5
10199
23
0.16 60
0.15 0.4
0.8 2
0.5
16652
24
0.28 60
0.15 0.4
1.2 2
0.54 10149
25
0.16 50
0.25 0.8
1.2 2
0.54 15111
26
0.28 50
0.25 0.8
0.8 2
0.56 10624
27
0.16 60
0.25 0.8
0.8 2
0.56 16837
28
0.28 60
0.25 0.8
1.2 2
0.54 8597
29
0.16 50
0.15 0.8
0.8 2
0.54 16923
30
0.28 50
0.15 0.8
1.2 2
0.53 8932
31
0.16 60
0.15 0.8
1.2 2
0.54 13389
32
0.28 60
0.15 0.8
0.8 2
0.54 9521
33
0.16 50
0.25 0.4
0.8 3
0.51 17930
34
0.28 50
0.25 0.4
1.2 3
0.51 8777


---


## Page 222


205
Table 13 Continued
trial alh
aps aid
arw awt rep cost time
35
0.16 60
0.25 0.4
1.2 3
0.54 14478
36
0.28 60
0.25 0.4
0.8 3
0.51 10199
37
0.16 50
0.15 0.4
1.2 3
0.54 15060
38
0.28 50
0.15 0.4
0.8 3
0.5
10345
39
0.16 60
0.15 0.4
0.8 3
0.5
16658
40
0.28 60
0.15 0.4
1.2 3
0.54 8492
41
0.16 50
0.25 0.8
1.2 3
0.54 15108
42
0.28 50
0.25 0.8
0.8 3
0.56 10644
43
0.16 60
0.25 0.8
0.8 3
0.56 16864
44
0.28 60
0.25 0.8
1.2 3
0.54 8587
45
0.16 50
0.15 0.8
0.8 3
0.54 17046
46
0.28 50
0.15 0.8
1.2 3
0.54 12589
47
0.16 60
0.15 0.8
1.2 3
0.53 13465
48
0.28 60
0.15 0.8
0.8 3
0.54 9466
49
0.16 50
0.25 0.4
0.8 4
0.51 18026
50
0.28 50
0.25 0.4
1.2 4
0.51 8733
51
0.16 60
0.25 0.4
1.2 4
0.54 14448
52
0.28 60
0.25 0.4
0.8 4
0.51 10118
53
0.16 50
0.15 0.4
1.2 4
0.54 15063


---


## Page 223


206
Table 13 Continued
trial alh
aps aid
arw awt rep cost time
54
0.28 50
0.15 0.4
0.8 4
0.5
10421
55
0.16 60
0.15 0.4
0.8 4
0.5
16653
56
0.28 60
0.15 0.4
1.2 4
0.54 8480
57
0.16 50
0.25 0.8
1.2 4
0.54 15115
58
0.28 50
0.25 0.8
0.8 4
0.56 10646
59
0.16 60
0.25 0.8
0.8 4
0.56 16477
60
0.28 60
0.25 0.8
1.2 4
0.54 8580
61
0.16 50
0.15 0.8
0.8 4
0.54 17065
62
0.28 50
0.15 0.8
1.2 4
0.54 8944
63
0.16 60
0.15 0.8
1.2 4
0.53 13478
64
0.28 60
0.15 0.8
0.8 4
0.54 9448
65
0.16 50
0.25 0.4
0.8 5
0.48 17634
66
0.28 50
0.25 0.4
1.2 5
0.51 8736
67
0.16 60
0.25 0.4
1.2 5
0.54 14360
68
0.28 60
0.25 0.4
0.8 5
0.51 10200
69
0.16 50
0.15 0.4
1.2 5
0.54 15026
70
0.28 50
0.15 0.4
0.8 5
0.5
10422
71
0.16 60
0.15 0.4
0.8 5
0.5
16565
72
0.28 60
0.15 0.4
1.2 5
0.54 8538


---


## Page 224


207
Table 13 Continued
trial alh
aps aid
arw awt rep cost time
73
0.16 50
0.25 0.8
1.2 5
0.54 15122
74
0.28 50
0.25 0.8
0.8 5
0.56 10579
75
0.16 60
0.25 0.8
0.8 5
0.56 16806
76
0.28 60
0.25 0.8
1.2 5
0.54 8582
77
0.16 50
0.15 0.8
0.8 5
0.54 17058
78
0.28 50
0.15 0.8
1.2 5
0.54 8958
79
0.16 60
0.15 0.8
1.2 5
0.53 13462
80
0.28 60
0.15 0.8
0.8 5
0.54 9459


---


## Page 225


208
Table 14: Raw Results for the SWX1
trial alh
aps aid
arw awt rep cost
time
1
0.16 60
0.25 0.4
0.8 1
$ 0.560 16916
2
0.28 60
0.25 0.4
1.2 1
$ 0.600 9016
3
0.16 72
0.25 0.4
1.2 1
$ 0.600 12906
4
0.28 72
0.25 0.4
0.8 1
$ 0.570 9711
5
0.16 60
0.15 0.4
1.2 1
$ 0.590 14617
6
0.28 60
0.15 0.4
0.8 1
$ 0.550 10142
7
0.16 72
0.15 0.4
0.8 1
$ 0.540 14495
8
0.28 72
0.15 0.4
1.2 1
$ 0.590 7772
9
0.16 60
0.25 0.8
1.2 1
$ 0.600 18254
10
0.28 60
0.25 0.8
0.8 1
$ 0.620 9482
11
0.16 72
0.25 0.8
0.8 1
$ 0.610 13550
12
0.28 72
0.25 0.8
1.2 1
$ 0.600 9646
13
0.16 60
0.15 0.8
0.8 1
$ 0.590 14675
14
0.28 60
0.15 0.8
1.2 1
$ 0.590 8822
15
0.16 72
0.15 0.8
1.2 1
$ 0.590 12575
16
0.28 72
0.15 0.8
0.8 1
$ 0.600 8046
17
0.16 60
0.25 0.4
0.8 2
$ 0.560 16882
18
0.28 60
0.25 0.4
1.2 2
$ 0.600 8981
19
0.16 72
0.25 0.4
1.2 2
$ 0.600 12872


---


## Page 226


209
Table 14 Continued
trial alh
aps aid
arw awt rep cost
time
20
0.28 72
0.25 0.4
0.8 2
$ 0.570 9707
21
0.16 60
0.15 0.4
1.2 2
$ 0.590 14566
22
0.28 60
0.15 0.4
0.8 2
$ 0.550 10064
23
0.16 72
0.15 0.4
0.8 2
$ 0.540 14576
24
0.28 72
0.15 0.4
1.2 2
$ 0.590 7783
25
0.16 60
0.25 0.8
1.2 2
$ 0.600 14654
26
0.28 60
0.25 0.8
0.8 2
$ 0.620 9548
27
0.16 72
0.25 0.8
0.8 2
$ 0.610 13554
28
0.28 72
0.25 0.8
1.2 2
$ 0.600 7774
29
0.16 60
0.15 0.8
0.8 2
$ 0.590 14672
30
0.28 60
0.15 0.8
1.2 2
$ 0.590 8833
31
0.16 72
0.15 0.8
1.2 2
$ 0.590 12602
32
0.28 72
0.15 0.8
0.8 2
$ 0.600 8114
33
0.16 60
0.25 0.4
0.8 3
$ 0.560 16897
34
0.28 60
0.25 0.4
1.2 3
$ 0.600 8997
35
0.16 72
0.25 0.4
1.2 3
$ 0.600 12872
36
0.28 72
0.25 0.4
0.8 3
$ 0.570 9705
37
0.16 60
0.15 0.4
1.2 3
$ 0.590 14660
38
0.28 60
0.15 0.4
0.8 3
$ 0.550 10094


---


## Page 227


210
Table 14 Continued
trial alh
aps aid
arw awt rep cost
time
39
0.16 72
0.15 0.4
0.8 3
$ 0.540 14474
40
0.28 72
0.15 0.4
1.2 3
$ 0.590 7775
41
0.16 60
0.25 0.8
1.2 3
$ 0.600 14576
42
0.28 60
0.25 0.8
0.8 3
$ 0.620 9457
43
0.16 72
0.25 0.8
0.8 3
$ 0.610 13501
44
0.28 72
0.25 0.8
1.2 3
$ 0.600 7747
45
0.16 60
0.15 0.8
0.8 3
$ 0.590 14682
46
0.28 60
0.15 0.8
1.2 3
$ 0.590 8841
47
0.16 72
0.15 0.8
1.2 3
$ 0.590 12605
48
0.28 72
0.15 0.8
0.8 3
$ 0.600 9770
49
0.16 60
0.25 0.4
0.8 4
$ 0.560 16913
50
0.28 60
0.25 0.4
1.2 4
$ 0.600 8975
51
0.16 72
0.25 0.4
1.2 4
$ 0.600 12869
52
0.28 72
0.25 0.4
0.8 4
$ 0.570 9682
53
0.16 60
0.15 0.4
1.2 4
$ 0.590 14664
54
0.28 60
0.15 0.4
0.8 4
$ 0.550 10132
55
0.16 72
0.15 0.4
0.8 4
$ 0.540 14470
56
0.28 72
0.15 0.4
1.2 4
$ 0.590 7778
57
0.16 60
0.25 0.8
1.2 4
$ 0.600 14629


---


## Page 228


211
Table 14 Continued
trial alh
aps aid
arw awt rep cost
time
58
0.28 60
0.25 0.8
0.8 4
$ 0.620 9459
59
0.16 72
0.25 0.8
0.8 4
$ 0.610 13550
60
0.28 72
0.25 0.8
1.2 4
$ 0.600 7737
61
0.16 60
0.15 0.8
0.8 4
$ 0.590 14748
62
0.28 60
0.15 0.8
1.2 4
$ 0.590 8836
63
0.16 72
0.15 0.8
1.2 4
$ 0.590 12545
64
0.28 72
0.15 0.8
0.8 4
$ 0.600 8094
65
0.16 60
0.25 0.4
0.8 5
$ 0.560 16885
66
0.28 60
0.25 0.4
1.2 5
$ 0.600 8981
67
0.16 72
0.25 0.4
1.2 5
$ 0.600 12788
68
0.28 72
0.25 0.4
0.8 5
$ 0.570 9708
69
0.16 60
0.15 0.4
1.2 5
$ 0.590 14655
70
0.28 60
0.15 0.4
0.8 5
$ 0.550 10023
71
0.16 72
0.15 0.4
0.8 5
$ 0.540 14549
72
0.28 72
0.15 0.4
1.2 5
$ 0.590 7760
73
0.16 60
0.25 0.8
1.2 5
$ 0.600 14579
74
0.28 60
0.25 0.8
0.8 5
$ 0.620 9447
75
0.16 72
0.25 0.8
0.8 5
$ 0.610 13582
76
0.28 72
0.25 0.8
1.2 5
$ 0.600 7777


---


## Page 229


212
Table 14 Continued
trial alh
aps aid
arw awt rep cost
time
77
0.16 60
0.15 0.8
0.8 5
$ 0.590 14665
78
0.28 60
0.15 0.8
1.2 5
$ 0.590 8846
79
0.16 72
0.15 0.8
1.2 5
$ 0.590 12591
80
0.28 72
0.15 0.8
0.8 5
$ 0.600 8101


---


## Page 230


213
Table 15: Cost+Power Results for the CR-6 SE
trial alh
aps aid
arw awt rep cost
1
0.16 50
0.25 0.4
0.8 1
0.564
2
0.28 50
0.25 0.4
1.2 1
0.536
3
0.16 60
0.25 0.4
1.2 1
0.583
4
0.28 60
0.25 0.4
0.8 1
0.540
5
0.16 50
0.15 0.4
1.2 1
0.584
6
0.28 50
0.15 0.4
0.8 1
0.531
7
0.16 60
0.15 0.4
0.8 1
0.549
8
0.28 60
0.15 0.4
1.2 1
0.565
9
0.16 50
0.25 0.8
1.2 1
0.585
10
0.28 50
0.25 0.8
0.8 1
0.592
11
0.16 60
0.25 0.8
0.8 1
0.610
12
0.28 60
0.25 0.8
1.2 1
0.566
13
0.16 50
0.15 0.8
0.8 1
0.591
14
0.28 50
0.15 0.8
1.2 1
0.567
15
0.16 60
0.15 0.8
1.2 1
0.570
16
0.28 60
0.15 0.8
0.8 1
0.568
17
0.16 50
0.25 0.4
0.8 2
0.564
18
0.28 50
0.25 0.4
1.2 2
0.536
19
0.16 60
0.25 0.4
1.2 2
0.583


---


## Page 231


214
Table 15 Continued
trial alh
aps aid
arw awt rep cost
20
0.28 60
0.25 0.4
0.8 2
0.540
21
0.16 50
0.15 0.4
1.2 2
0.584
22
0.28 50
0.15 0.4
0.8 2
0.530
23
0.16 60
0.15 0.4
0.8 2
0.549
24
0.28 60
0.15 0.4
1.2 2
0.570
25
0.16 50
0.25 0.8
1.2 2
0.585
26
0.28 50
0.25 0.8
0.8 2
0.592
27
0.16 60
0.25 0.8
0.8 2
0.610
28
0.28 60
0.25 0.8
1.2 2
0.566
29
0.16 50
0.15 0.8
0.8 2
0.590
30
0.28 50
0.15 0.8
1.2 2
0.557
31
0.16 60
0.15 0.8
1.2 2
0.580
32
0.28 60
0.15 0.8
0.8 2
0.568
33
0.16 50
0.25 0.4
0.8 3
0.563
34
0.28 50
0.25 0.4
1.2 3
0.536
35
0.16 60
0.25 0.4
1.2 3
0.583
36
0.28 60
0.25 0.4
0.8 3
0.540
37
0.16 50
0.15 0.4
1.2 3
0.585
38
0.28 50
0.15 0.4
0.8 3
0.531


---


## Page 232


215
Table 15 Continued
trial alh
aps aid
arw awt rep cost
39
0.16 60
0.15 0.4
0.8 3
0.550
40
0.28 60
0.15 0.4
1.2 3
0.565
41
0.16 50
0.25 0.8
1.2 3
0.585
42
0.28 50
0.25 0.8
0.8 3
0.592
43
0.16 60
0.25 0.8
0.8 3
0.610
44
0.28 60
0.25 0.8
1.2 3
0.566
45
0.16 50
0.15 0.8
0.8 3
0.591
46
0.28 50
0.15 0.8
1.2 3
0.577
47
0.16 60
0.15 0.8
1.2 3
0.570
48
0.28 60
0.15 0.8
0.8 3
0.568
49
0.16 50
0.25 0.4
0.8 4
0.564
50
0.28 50
0.25 0.4
1.2 4
0.536
51
0.16 60
0.25 0.4
1.2 4
0.583
52
0.28 60
0.25 0.4
0.8 4
0.540
53
0.16 50
0.15 0.4
1.2 4
0.585
54
0.28 50
0.15 0.4
0.8 4
0.531
55
0.16 60
0.15 0.4
0.8 4
0.549
56
0.28 60
0.15 0.4
1.2 4
0.565
57
0.16 50
0.25 0.8
1.2 4
0.585


---


## Page 233


216
Table 15 Continued
trial alh
aps aid
arw awt rep cost
58
0.28 50
0.25 0.8
0.8 4
0.592
59
0.16 60
0.25 0.8
0.8 4
0.609
60
0.28 60
0.25 0.8
1.2 4
0.566
61
0.16 50
0.15 0.8
0.8 4
0.591
62
0.28 50
0.15 0.8
1.2 4
0.567
63
0.16 60
0.15 0.8
1.2 4
0.570
64
0.28 60
0.15 0.8
0.8 4
0.568
65
0.16 50
0.25 0.4
0.8 5
0.532
66
0.28 50
0.25 0.4
1.2 5
0.536
67
0.16 60
0.25 0.4
1.2 5
0.583
68
0.28 60
0.25 0.4
0.8 5
0.540
69
0.16 50
0.15 0.4
1.2 5
0.585
70
0.28 50
0.15 0.4
0.8 5
0.531
71
0.16 60
0.15 0.4
0.8 5
0.549
72
0.28 60
0.15 0.4
1.2 5
0.565
73
0.16 50
0.25 0.8
1.2 5
0.585
74
0.28 50
0.25 0.8
0.8 5
0.591
75
0.16 60
0.25 0.8
0.8 5
0.610
76
0.28 60
0.25 0.8
1.2 5
0.566


---


## Page 234


217
Table 15 Continued
trial alh
aps aid
arw awt rep cost
77
0.16 50
0.15 0.8
0.8 5
0.591
78
0.28 50
0.15 0.8
1.2 5
0.567
79
0.16 60
0.15 0.8
1.2 5
0.570
80
0.28 60
0.15 0.8
0.8 5
0.568


---


## Page 235


218
Table 16: Cost+Power Results for the SWX1
trial alh
aps aid
arw awt rep cost
1
0.16 60
0.25 0.4
0.8 1
0.593
2
0.28 60
0.25 0.4
1.2 1
0.618
3
0.16 72
0.25 0.4
1.2 1
0.626
4
0.28 72
0.25 0.4
0.8 1
0.589
5
0.16 60
0.15 0.4
1.2 1
0.619
6
0.28 60
0.15 0.4
0.8 1
0.570
7
0.16 72
0.15 0.4
0.8 1
0.569
8
0.28 72
0.15 0.4
1.2 1
0.605
9
0.16 60
0.25 0.8
1.2 1
0.636
10
0.28 60
0.25 0.8
0.8 1
0.639
11
0.16 72
0.25 0.8
0.8 1
0.637
12
0.28 72
0.25 0.8
1.2 1
0.619
13
0.16 60
0.15 0.8
0.8 1
0.619
14
0.28 60
0.15 0.8
1.2 1
0.607
15
0.16 72
0.15 0.8
1.2 1
0.615
16
0.28 72
0.15 0.8
0.8 1
0.616
17
0.16 60
0.25 0.4
0.8 2
0.593
18
0.28 60
0.25 0.4
1.2 2
0.618
19
0.16 72
0.25 0.4
1.2 2
0.625


---


## Page 236


219
Table 16 Continued
trial alh
aps aid
arw awt rep cost
20
0.28 72
0.25 0.4
0.8 2
0.589
21
0.16 60
0.15 0.4
1.2 2
0.619
22
0.28 60
0.15 0.4
0.8 2
0.570
23
0.16 72
0.15 0.4
0.8 2
0.569
24
0.28 72
0.15 0.4
1.2 2
0.605
25
0.16 60
0.25 0.8
1.2 2
0.629
26
0.28 60
0.25 0.8
0.8 2
0.639
27
0.16 72
0.25 0.8
0.8 2
0.637
28
0.28 72
0.25 0.8
1.2 2
0.615
29
0.16 60
0.15 0.8
0.8 2
0.619
30
0.28 60
0.15 0.8
1.2 2
0.607
31
0.16 72
0.15 0.8
1.2 2
0.615
32
0.28 72
0.15 0.8
0.8 2
0.616
33
0.16 60
0.25 0.4
0.8 3
0.593
34
0.28 60
0.25 0.4
1.2 3
0.618
35
0.16 72
0.25 0.4
1.2 3
0.625
36
0.28 72
0.25 0.4
0.8 3
0.589
37
0.16 60
0.15 0.4
1.2 3
0.619
38
0.28 60
0.15 0.4
0.8 3
0.570


---


## Page 237


220
Table 16 Continued
trial alh
aps aid
arw awt rep cost
39
0.16 72
0.15 0.4
0.8 3
0.569
40
0.28 72
0.15 0.4
1.2 3
0.605
41
0.16 60
0.25 0.8
1.2 3
0.629
42
0.28 60
0.25 0.8
0.8 3
0.639
43
0.16 72
0.25 0.8
0.8 3
0.637
44
0.28 72
0.25 0.8
1.2 3
0.615
45
0.16 60
0.15 0.8
0.8 3
0.619
46
0.28 60
0.15 0.8
1.2 3
0.607
47
0.16 72
0.15 0.8
1.2 3
0.615
48
0.28 72
0.15 0.8
0.8 3
0.619
49
0.16 60
0.25 0.4
0.8 4
0.593
50
0.28 60
0.25 0.4
1.2 4
0.618
51
0.16 72
0.25 0.4
1.2 4
0.625
52
0.28 72
0.25 0.4
0.8 4
0.589
53
0.16 60
0.15 0.4
1.2 4
0.619
54
0.28 60
0.15 0.4
0.8 4
0.570
55
0.16 72
0.15 0.4
0.8 4
0.569
56
0.28 72
0.15 0.4
1.2 4
0.605
57
0.16 60
0.25 0.8
1.2 4
0.629


---


## Page 238


221
Table 16 Continued
trial alh
aps aid
arw awt rep cost
58
0.28 60
0.25 0.8
0.8 4
0.639
59
0.16 72
0.25 0.8
0.8 4
0.637
60
0.28 72
0.25 0.8
1.2 4
0.615
61
0.16 60
0.15 0.8
0.8 4
0.619
62
0.28 60
0.15 0.8
1.2 4
0.607
63
0.16 72
0.15 0.8
1.2 4
0.615
64
0.28 72
0.15 0.8
0.8 4
0.616
65
0.16 60
0.25 0.4
0.8 5
0.593
66
0.28 60
0.25 0.4
1.2 5
0.618
67
0.16 72
0.25 0.4
1.2 5
0.625
68
0.28 72
0.25 0.4
0.8 5
0.589
69
0.16 60
0.15 0.4
1.2 5
0.619
70
0.28 60
0.15 0.4
0.8 5
0.570
71
0.16 72
0.15 0.4
0.8 5
0.569
72
0.28 72
0.15 0.4
1.2 5
0.605
73
0.16 60
0.25 0.8
1.2 5
0.629
74
0.28 60
0.25 0.8
0.8 5
0.639
75
0.16 72
0.25 0.8
0.8 5
0.637
76
0.28 72
0.25 0.8
1.2 5
0.615


---


## Page 239


222
Table 16 Continued
trial alh
aps aid
arw awt rep cost
77
0.16 60
0.15 0.8
0.8 5
0.619
78
0.28 60
0.15 0.8
1.2 5
0.607
79
0.16 72
0.15 0.8
1.2 5
0.615
80
0.28 72
0.15 0.8
0.8 5
0.616


---


## Page 240


223
Table 17: Rework Results for the CR-6 SE
trial alh
aps aid
arw awt rep cost
time
1
0.16 50
0.25 0.4
0.8 1
0.564 18098
2
0.28 50
0.25 0.4
1.2 1
0.536 8741
3
0.16 60
0.25 0.4
1.2 1
0.583 14493
4
0.28 60
0.25 0.4
0.8 1
1.103 10281
5
0.16 50
0.15 0.4
1.2 1
0.584 14914
6
0.28 50
0.15 0.4
0.8 1
0.531 10423
7
0.16 60
0.15 0.4
0.8 1
0.549 16648
8
0.28 60
0.15 0.4
1.2 1
0.565 8534
9
0.16 50
0.25 0.8
1.2 1
0.585 15085
10
0.28 50
0.25 0.8
0.8 1
0.592 10624
11
0.16 60
0.25 0.8
0.8 1
0.798 16870
12
0.28 60
0.25 0.8
1.2 1
0.566 8645
13
0.16 50
0.15 0.8
0.8 1
0.591 17046
14
0.28 50
0.15 0.8
1.2 1
0.567 9012
15
0.16 60
0.15 0.8
1.2 1
0.570 13488
16
0.28 60
0.15 0.8
0.8 1
0.568 9574
17
0.16 50
0.25 0.4
0.8 2
0.564 18042
18
0.28 50
0.25 0.4
1.2 2
0.536 8743
19
0.16 60
0.25 0.4
1.2 2
0.583 14469


---


## Page 241


224
Table 17 Continued
trial alh
aps aid
arw awt rep cost
time
20
0.28 60
0.25 0.4
0.8 2
0.728 10215
21
0.16 50
0.15 0.4
1.2 2
0.772 14903
22
0.28 50
0.15 0.4
0.8 2
0.530 10199
23
0.16 60
0.15 0.4
0.8 2
0.549 16652
24
0.28 60
0.15 0.4
1.2 2
0.570 10149
25
0.16 50
0.25 0.8
1.2 2
0.772 15141
26
0.28 50
0.25 0.8
0.8 2
0.592 10624
27
0.16 60
0.25 0.8
0.8 2
0.610 16837
28
0.28 60
0.25 0.8
1.2 2
0.566 8597
29
0.16 50
0.15 0.8
0.8 2
0.590 16923
30
0.28 50
0.15 0.8
1.2 2
0.557 8932
31
0.16 60
0.15 0.8
1.2 2
0.580 13389
32
0.28 60
0.15 0.8
0.8 2
0.568 9521
33
0.16 50
0.25 0.4
0.8 3
0.563 17930
34
0.28 50
0.25 0.4
1.2 3
0.536 8777
35
0.16 60
0.25 0.4
1.2 3
0.583 14478
36
0.28 60
0.25 0.4
0.8 3
0.540 10199
37
0.16 50
0.15 0.4
1.2 3
0.585 15060
38
0.28 50
0.15 0.4
0.8 3
0.531 10345


---


## Page 242


225
Table 17 Continued
trial alh
aps aid
arw awt rep cost
time
39
0.16 60
0.15 0.4
0.8 3
0.550 16658
40
0.28 60
0.15 0.4
1.2 3
0.565 8492
41
0.16 50
0.25 0.8
1.2 3
0.585 15108
42
0.28 50
0.25 0.8
0.8 3
0.967 10704
43
0.16 60
0.25 0.8
0.8 3
0.610 16864
44
0.28 60
0.25 0.8
1.2 3
0.566 8587
45
0.16 50
0.15 0.8
0.8 3
0.591 17046
46
0.28 50
0.15 0.8
1.2 3
0.577 12589
47
0.16 60
0.15 0.8
1.2 3
0.570 13465
48
0.28 60
0.15 0.8
0.8 3
0.568 9466
49
0.16 50
0.25 0.4
0.8 4
0.564 18026
50
0.28 50
0.25 0.4
1.2 4
0.536 8733
51
0.16 60
0.25 0.4
1.2 4
0.583 14448
52
0.28 60
0.25 0.4
0.8 4
0.540 10118
53
0.16 50
0.15 0.4
1.2 4
0.585 15063
54
0.28 50
0.15 0.4
0.8 4
0.531 10421
55
0.16 60
0.15 0.4
0.8 4
0.549 16653
56
0.28 60
0.15 0.4
1.2 4
0.565 8480
57
0.16 50
0.25 0.8
1.2 4
0.585 15115


---


## Page 243


226
Table 17 Continued
trial alh
aps aid
arw awt rep cost
time
58
0.28 50
0.25 0.8
0.8 4
0.779 10676
59
0.16 60
0.25 0.8
0.8 4
0.796 16507
60
0.28 60
0.25 0.8
1.2 4
0.566 8580
61
0.16 50
0.15 0.8
0.8 4
0.591 17065
62
0.28 50
0.15 0.8
1.2 4
0.567 8944
63
0.16 60
0.15 0.8
1.2 4
0.570 13478
64
0.28 60
0.15 0.8
0.8 4
0.568 9448
65
0.16 50
0.25 0.4
0.8 5
0.532 17634
66
0.28 50
0.25 0.4
1.2 5
0.536 8736
67
0.16 60
0.25 0.4
1.2 5
0.583 14360
68
0.28 60
0.25 0.4
0.8 5
0.540 10200
69
0.16 50
0.15 0.4
1.2 5
0.585 15026
70
0.28 50
0.15 0.4
0.8 5
0.531 10422
71
0.16 60
0.15 0.4
0.8 5
0.549 16565
72
0.28 60
0.15 0.4
1.2 5
0.565 8538
73
0.16 50
0.25 0.8
1.2 5
0.585 15122
74
0.28 50
0.25 0.8
0.8 5
0.591 10579
75
0.16 60
0.25 0.8
0.8 5
0.797 16836
76
0.28 60
0.25 0.8
1.2 5
0.566 8582


---


## Page 244


227
Table 17 Continued
trial alh
aps aid
arw awt rep cost
time
77
0.16 50
0.15 0.8
0.8 5
0.591 17058
78
0.28 50
0.15 0.8
1.2 5
0.567 8958
79
0.16 60
0.15 0.8
1.2 5
0.570 13462
80
0.28 60
0.15 0.8
0.8 5
0.568 9459


---


## Page 245


228
Table 18: Rework Results for the SWX1
trial alh
aps aid
arw awt rep cost
time
1
0.16 60
0.25 0.4
0.8 1
0.781 16946
2
0.28 60
0.25 0.4
1.2 1
1.368 9136
3
0.16 72
0.25 0.4
1.2 1
0.626 12906
4
0.28 72
0.25 0.4
0.8 1
1.339 9831
5
0.16 60
0.15 0.4
1.2 1
0.619 14617
6
0.28 60
0.15 0.4
0.8 1
1.320 10262
7
0.16 72
0.15 0.4
0.8 1
1.319 14615
8
0.28 72
0.15 0.4
1.2 1
0.980 7832
9
0.16 60
0.25 0.8
1.2 1
0.636 18254
10
0.28 60
0.25 0.8
0.8 1
1.201 9572
11
0.16 72
0.25 0.8
0.8 1
0.637 13550
12
0.28 72
0.25 0.8
1.2 1
0.994 9706
13
0.16 60
0.15 0.8
0.8 1
1.369 14795
14
0.28 60
0.15 0.8
1.2 1
0.607 8822
15
0.16 72
0.15 0.8
1.2 1
0.802 12605
16
0.28 72
0.15 0.8
0.8 1
1.366 8166
17
0.16 60
0.25 0.4
0.8 2
0.593 16882
18
0.28 60
0.25 0.4
1.2 2
1.368 9101
19
0.16 72
0.25 0.4
1.2 2
0.625 12872


---


## Page 246


229
Table 18 Continued
trial alh
aps aid
arw awt rep cost
time
20
0.28 72
0.25 0.4
0.8 2
1.339 9827
21
0.16 60
0.15 0.4
1.2 2
0.619 14566
22
0.28 60
0.15 0.4
0.8 2
1.320 10184
23
0.16 72
0.15 0.4
0.8 2
1.319 14696
24
0.28 72
0.15 0.4
1.2 2
0.980 7843
25
0.16 60
0.25 0.8
1.2 2
0.816 14684
26
0.28 60
0.25 0.8
0.8 2
1.201 9638
27
0.16 72
0.25 0.8
0.8 2
1.387 13674
28
0.28 72
0.25 0.8
1.2 2
0.990 7834
29
0.16 60
0.15 0.8
0.8 2
0.806 14702
30
0.28 60
0.15 0.8
1.2 2
0.795 8863
31
0.16 72
0.15 0.8
1.2 2
0.802 12632
32
0.28 72
0.15 0.8
0.8 2
1.366 8234
33
0.16 60
0.25 0.4
0.8 3
0.593 16897
34
0.28 60
0.25 0.4
1.2 3
1.368 9117
35
0.16 72
0.25 0.4
1.2 3
0.625 12872
36
0.28 72
0.25 0.4
0.8 3
1.339 9825
37
0.16 60
0.15 0.4
1.2 3
0.619 14660
38
0.28 60
0.15 0.4
0.8 3
1.320 10214


---


## Page 247


230
Table 18 Continued
trial alh
aps aid
arw awt rep cost
time
39
0.16 72
0.15 0.4
0.8 3
1.319 14594
40
0.28 72
0.15 0.4
1.2 3
0.980 7835
41
0.16 60
0.25 0.8
1.2 3
0.816 14606
42
0.28 60
0.25 0.8
0.8 3
1.201 9547
43
0.16 72
0.25 0.8
0.8 3
1.387 13621
44
0.28 72
0.25 0.8
1.2 3
0.990 7807
45
0.16 60
0.15 0.8
0.8 3
0.807 14712
46
0.28 60
0.15 0.8
1.2 3
0.795 8871
47
0.16 72
0.15 0.8
1.2 3
0.802 12635
48
0.28 72
0.15 0.8
0.8 3
1.369 9890
49
0.16 60
0.25 0.4
0.8 4
0.593 16913
50
0.28 60
0.25 0.4
1.2 4
1.368 9095
51
0.16 72
0.25 0.4
1.2 4
0.625 12869
52
0.28 72
0.25 0.4
0.8 4
1.339 9802
53
0.16 60
0.15 0.4
1.2 4
0.619 14664
54
0.28 60
0.15 0.4
0.8 4
1.320 10252
55
0.16 72
0.15 0.4
0.8 4
1.319 14590
56
0.28 72
0.15 0.4
1.2 4
0.980 7838
57
0.16 60
0.25 0.8
1.2 4
0.816 14659


---


## Page 248


231
Table 18 Continued
trial alh
aps aid
arw awt rep cost
time
58
0.28 60
0.25 0.8
0.8 4
1.201 9549
59
0.16 72
0.25 0.8
0.8 4
1.387 13670
60
0.28 72
0.25 0.8
1.2 4
0.803 7767
61
0.16 60
0.15 0.8
0.8 4
0.807 14778
62
0.28 60
0.15 0.8
1.2 4
0.795 8866
63
0.16 72
0.15 0.8
1.2 4
0.802 12575
64
0.28 72
0.15 0.8
0.8 4
1.366 8214
65
0.16 60
0.25 0.4
0.8 5
0.593 16885
66
0.28 60
0.25 0.4
1.2 5
1.368 9101
67
0.16 72
0.25 0.4
1.2 5
0.625 12788
68
0.28 72
0.25 0.4
0.8 5
1.339 9828
69
0.16 60
0.15 0.4
1.2 5
0.619 14655
70
0.28 60
0.15 0.4
0.8 5
1.320 10143
71
0.16 72
0.15 0.4
0.8 5
1.319 14669
72
0.28 72
0.15 0.4
1.2 5
0.793 7790
73
0.16 60
0.25 0.8
1.2 5
0.816 14609
74
0.28 60
0.25 0.8
0.8 5
1.201 9537
75
0.16 72
0.25 0.8
0.8 5
1.387 13702
76
0.28 72
0.25 0.8
1.2 5
0.803 7807


---


## Page 249


232
Table 18 Continued
trial alh
aps aid
arw awt rep cost
time
77
0.16 60
0.15 0.8
0.8 5
0.806 14695
78
0.28 60
0.15 0.8
1.2 5
0.795 8876
79
0.16 72
0.15 0.8
1.2 5
0.615 12591
80
0.28 72
0.15 0.8
0.8 5
1.366 8221


---


## Page 250


233
Table 19: Quality Score Card for the CR6
CR-6 SE Inspection Score Card
#
Criteria
weight
Option
1

Option 2

Option
3

Option
4

Option
5




rating
score
rating
score
rating
score
rating
score
rating
score
1
F/ N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
2
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
3
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
4
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450


---


## Page 251


234

Table 19 Continued
#
Criteria
weight
Option
1

Option
2

Option
3

Option
4

Option
5




rating
score
rating
score
rating
score
rating
score
rating
score
5
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
50%
100
75%
150
100%
200
100%
200
100%
200

Hedonic
150
50%
75
100%
150
100%
150
100%
150
100%
150

Visual
100
75%
75
100%
100
100%
100
100%
100
100%
100

Totals
450

250

400

450

450

450
6
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
75%
150
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

400

450

450

450
7
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
8
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
9
F/N

0
0
0
0
0
0
0
0
0
0


---


## Page 252


235
Table 19 Continued
#
Criteria
weight
Option
1

Option
2

Option
3

Option
4

Option
5




rating
score
rating
score
rating
score
rating
score
rating
score

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
10
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
75%
150
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

400

450

450

450
11
F/N

0
0
0
0
0
0
0
0

0

Tactile
200
100%
200
100%
200
75%
150
75%
150
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
75%
75
100%
100
100%
100

Totals
450

450

450

375

400

450
12
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
75%
150
100%
200
100%
200
75%
150
75%
150

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

400

450

450

400

400
13
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200


---


## Page 253


236
Table 19 Continued
#
Criteria
weight
Option
1

Option
2

Option
3

Option
4

Option
5




rating
score
rating
score
rating
score
rating
score
rating
score

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
14
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
15
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
16
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
17
F/N

0
0
0
0
0
0
0
0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150


---


## Page 254


237
Table 19 Continued
#
Criteria
weight
Option
1

Option 2

Option
3

Option
4

Option
5




rating
score
rating
score
rating
score
rating
score
rating
score

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
Functional (F)
0
Nonfunctional (N)
1


---


## Page 255


238
Table 20: Quality Score Card for the SWX1
SWX1 Inspection Score Card
Run
Criteri
a
weight
Option
1

Option 2

Option
3

Option
4

Option
5




rating
score
rating
score
rating
score
rating
score
rating
score
1


0
0
0
0
0
0

0

0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedon
ic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
2



0

0

0

0

0

Tactile
200
75%
150
100%
200
100%
200
100%
200
100%
200

Hedon
ic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

400

450

450

450

450
3



0

0

0

0

0

Tactile
200
25%
50
25%
50
25%
50
25%
50
25%
50

Hedon
ic
150
25%
37.5
25%
37.5
25%
37.5
25%
37.5
25%
37.5

Visual
100
25%
25
25%
25
25%
25
25%
25
25%
25

Totals
450

112.5

112.5

112.5

112.5

112.5
4



0

0

0

0

0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedon
ic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450


---


## Page 256


239
Table 20 Continued
Run
Criteria
weight
Option
1

Option
2

Option
3

Option
4

Option
5




rating
score
rating
score
rating
score
rating
score
rating
score
5



0

0

0
0
0
0
0

Tactile
200
25%
50
25%
50
25%
50
25%
50
25%
50

Hedonic
150
25%
37.5
25%
37.5
25%
37.5
25%
37.5
25%
37.5

Visual
100
25%
25
25%
25
25%
25
25%
25
25%
25

Totals
450

112.5

112.5

112.5

112.5

112.5
6



0

0

0

0
0
0

Tactile
200
100%
200
100%
200
100%
200
100%
200
100%
200

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

450

450

450

450
7



0

0

0

0
1
0

Tactile
200
25%
50
25%
50
25%
50
25%
50
25%
50

Hedonic
150
25%
37.5
25%
37.5
25%
37.5
25%
37.5
25%
37.5

Visual
100
25%
25
25%
25
25%
25
25%
25
25%
25

Totals
450

112.5

112.5

112.5

112.5

112.5
8



0

0

0

0

0

Tactile
200
25%
50
25%
50
25%
50
25%
50
25%
50

Hedonic
150
25%
37.5
25%
37.5
25%
37.5
25%
37.5
25%
37.5

Visual
100
25%
25
25%
25
25%
25
25%
25
25%
25

Totals
450

112.5

112.5

112.5

112.5

112.5
9



0

0

0

0

0


---


## Page 257


240
Table 20 Continued
Run
Criteria
weight
Option
1

Option
2

Option
3

Option
4

Option
5




rating
score
rating
score
rating
score
rating
score
rating
score

Tactile
200
75%
150
75%
150
75%
150
75%
150
75%
150

Hedonic
150
75%
112.5
75%
112.5
75%
112.5
75%
112.5
100%
150

Visual
100
75%
75
75%
75
75%
75
75%
75
100%
100

Totals
450

337.5

337.5

337.5

337.5

400
10



0

0

0

0

0

Tactile
200
100%
200
75%
150
75%
150
75%
150
75%
150

Hedonic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

400

400

400

400
11



0

0

0

0

0

Tactile
200
50%
100
50%
100
50%
100
50%
100
50%
100

Hedonic
150
75%
112.5
75%
112.5
50%
75
50%
75
50%
75

Visual
100
75%
75
75%
75
75%
75
75%
75
75%
75

Totals
450

287.5

287.5

250

250

250
12



0

0

0

0

0

Tactile
200
100%
200
50%
100
50%
100
50%
100
50%
100

Hedonic
150
100%
150
50%
75
50%
75
50%
75
50%
75

Visual
100
100%
100
50%
50
50%
50
50%
50
50%
50

Totals
450

450

225

225

225

225
13



0

0

0

0

0

Tactile
200
50%
100
50%
100
50%
100
75%
150
75%
150


---


## Page 258


241
Table 20 Continued
Run
Criteri
a
weight
Optio
n 1

Option
2

Optio
n 3

Option
4

Optio
n 5




rating
score
rating
score
rating
score
rating
score
rating
score

Hedon
ic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

350

350

350

400

400
14



0

0

0

0

0

Tactile
200
50%
100
75%
150
75%
150
75%
150
75%
150

Hedon
ic
150
50%
75
100%
150
100%
150
100%
150
100%
150

Visual
100
50%
50
100%
100
100%
100
100%
100
100%
100

Totals
450

225

400

400

400

400
15



0

0

0

0

0

Tactile
200
100%
200
75%
150
75%
150
75%
150
75%
150

Hedon
ic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

450

400

400

400

400
16



0

0

0

0

0

Tactile
200
75%
150
75%
150
75%
150
75%
150
100%
200

Hedon
ic
150
100%
150
100%
150
100%
150
100%
150
100%
150

Visual
100
100%
100
100%
100
100%
100
100%
100
100%
100

Totals
450

400

400

400

400

450
17



0

0

0
0
0

0

Tactile
200
25%
50
25%
50
25%
50
25%
50
25%
50

Hedon
ic
150
25%
37.5
25%
37.5
25%
37.5
25%
37.5
25%
37.5


---


## Page 259


242
Table 20 Continued
Run
Criteri
a
weight
Option
1

Option
2

Option
3

Option
4

Option
5




rating
score
rating
score
rating
score
rating
score
rating
score

Visual
100
25%
25
25%
25
25%
25
25%
25
25%
25

Totals
450

112.5

112.5

112.5

112.5

112.5
Functional (F)
0
Nonfunctional (N)
1


---


## Page 260


243
APPENDIX B - REPEATABILITY
Prerequisites
Install Docker
•
See Install Docker Engine (https://docs.docker.com/engine/install/)
Installation
10. Clone the repo
git clone https://github.com/wilsongis/•DP_Experiments.git

•. Enter workspace folder

cd •DP-Experiments

•. Create ML Workspace

docker run -d \
     -p ‡–‡–:‡–‡– \
    --name "•DP-workspace" \
    -v "$(PWD):/workspace" \
    --env AUTHENTICATE_VIA_JUPYTER="mytoken" \
     --shm-size †‚•m \
    --restart always \


---


## Page 261


244
    mltooling/ml-workspace:–.‚•.‚

~. Install Python Packages
pip install -U pip setuptools wheel pip install -r requirements.txt conda install -c
conda-forge pyomo conda install -c conda-forge ipopt glpk conda install -c r r-
irkernel
Updating
This will override your existing requirements.txt. If you want to append, use >> instead
of >
pip list --format=freeze > requirements.txt


---


## Page 262


245
VITA
Originally from Pennsylvania, Mike Wilson grew up in Philadelphia, Pennsylvania. After
High School, Mike attended Kutztown University and received a Bachelor of Science
degree in Geology. Upon graduation, Mike was accepted to the Master of Science in
Geosciences at Murray State University where he received his degree in 2003. In 2014,
Mike applied and was accepted to the graduate program at the University of
Tennessee, Knoxville to pursue a Doctor of Philosophy degree in Industrial Engineering
with a concentration in Engineering Management. His research interests include GIS,
3D printing, VR. And STEM. Upon graduation, Mike will continue his position at the
Austin Peay State University GIS Center as Director.


---
