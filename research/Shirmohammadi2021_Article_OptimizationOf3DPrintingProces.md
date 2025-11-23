# Shirmohammadi2021_Article_OptimizationOf3DPrintingProces

> **Source:** `Shirmohammadi2021_Article_OptimizationOf3DPrintingProces.pdf`
> **Converted:** 2025-11-22 21:18:11
> **Method:** PyMuPDF

---

## Page 1


See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/349072563
Optimization of 3D printing process parameters to minimize surface
roughness with hybrid artiﬁcial neural network model and particle swarm
algorithm
Article  in  Progress in Additive Manufacturing · May 2021
DOI: 10.1007/s40964-021-00166-6
CITATIONS
104
READS
3,139
3 authors, including:
Saeid Jafarzadeh Ghoushchi
Urmia University of Technology
111 PUBLICATIONS   4,761 CITATIONS   
SEE PROFILE
P. M. Keshtiban
Urmia University of Technology
28 PUBLICATIONS   257 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Saeid Jafarzadeh Ghoushchi on 07 July 2021.
The user has requested enhancement of the downloaded file.


---


## Page 2


Vol.:(0123456789)
1 3
Progress in Additive Manufacturing
https://doi.org/10.1007/s40964-021-00166-6
FULL RESEARCH ARTICLE
Optimization of 3D printing process parameters to minimize surface
roughness with hybrid artificial neural network model and particle
swarm algorithm
Mohammad Shirmohammadi1 · Saeid Jafarzadeh Goushchi1 · Peyman Mashhadi Keshtiban2 
Received: 12 July 2020 / Accepted: 19 January 2021
© The Author(s), under exclusive licence to Springer Nature Switzerland AG part of Springer Nature 2021
Abstract
Due to the significant impact on the product quality and performance, the surface roughness of produced parts by 3D printers
is one of the important factors in the 3D printing process. Then, the main objective of this research is to determine the optimal
composition of input parameters to minimize surface roughness, using hybrid artificial neural network and particle swarm
algorithm. For this purpose, after using Central Composite Design (CCD) of experiments with five independent parameters
(nozzle temperature, layers thickness, printing speed, nozzle diameter and material density) with three levels, 43 flat parts
were produced with a three-dimensional printer, and roughness tests were performed on produced parts. After training experi-
mental matrix by multilayer perceptron neural network (7-4-1) with a coefficient of 0.95, the subjected matrix was combined
with the particle swarm algorithm to determine the optimal composition of input parameters. To verify results accuracy,
the optimized process parameters obtained from the combined algorithm, have been tested with experimental results. In
addition, to specify the effect of input parameters on the surface roughness, a quadratic model has been developed using
Response Surface Method (RSM). Based on results of the hybrid algorithm, the optimal combination of input parameters
was extracted. It was inferred that, the nozzle temperature of 192.20 °C, the layers’ thickness of 100 μm, the printing speed
of 97.06 mm/s, the nozzle diameter of 0.3 mm and the internal density of 24.88% lead to the surface roughness of 11.319.
Therefore, the use of this hybrid algorithm improves the surface quality of the printed parts during the 3D printing process.
Keywords  3D printing · Surface roughness · Artificial neural network · Particle swarm optimization algorithm · Response
surface method
1  Introduction
Additive manufacturing is one of the three-dimensional
production technologies by adding layer on the material
previous layer. The 3D printing process is an additive man-
ufacturing that enables the production of parts with com-
puter design data in the shortest possible time. This process
involves printing the continuous surfaces of materials that
are placed on each other, and by repeating the subjected
process, final desired part is completed. 3D printing or
additive production is the opposite of the traditional sub-
tractive production. Incremental production has the ability
to produce components with a complex structure. While in
the production of complex structures, the use of traditional
methods such as casting is not simple and requires tools,
time-consuming methods, post-processing, etc.
Recent advances have reduced the cost of 3D printer’s
fabrication. As a result, 3D printing applications have been
developed in schools, homes, libraries and laboratories,
today. While, 3D printing was widely used by architects and
designers to simulate fine and functional specs due to its fast
and economical production capability, formerly. However,
in recent years, various industries have used the 3D print-
ing process instead of prototype simulation to produce final
products [1]. This technology has high potential for cus-
tomization, such as the construction of personal implants for
hip and knee replacement. Today, 3D printing technology is
 *	 Peyman Mashhadi Keshtiban

pmkmech@gmail.com
1
Faculty of Industrial Engineering, Urmia University
of Technology, Urmia, Iran
2
Faculty of Mechanical Engineering, Urmia University
of Technology, P.O.B. 57155‑419, Urmia, Iran


---


## Page 3


Progress in Additive Manufacturing
1 3
widely used in medical, aerospace, construction, automotive,
art, fashion and clothing, jewelry and food industries.
Rapid prototyping, the ability to print complex structures,
reduce defects and improve mechanical properties are some
of the key factors that have led to the development of 3D
printing technology. The most common method of 3D print-
ing, which mainly uses polymer, is known as Fused deposi-
tion modeling (FDM). In addition, Direct energy deposition
(DED), Selective laser sintering (SLS), Stereo lithography
(SLA), Laminated object manufacturing (LOM), Selective
Laser Melting (SLM) are the main methods of 3D print-
ing. A comprehensive review of 3D printing methods by
Bhushan and Caspers in 2017 is presented in a review study
[2]. Emerging 3D printing methods such as electro hydrody-
namic printing (EHDP), projection micro stereo lithography
(PμSLA) have been described in a 2017 study by Mao et al.
[3]
There are many benefits to using the FDM process,
including the freedom to design complex shapes without the
need for molds, the computer’s ability to create the internal
features of a product, which is impossible using traditional
manufacturing techniques [4].  FDM is a popular RP tech-
nology that is primarily used in the manufacture of parts
with complex geometry in industry. The performance, qual-
ity and characteristics of the parts produced by the FDM
process largely depend on the various process parameters.
Therefore, to achieve the desired quality specifications in the
parts produced by the FDM process, it is necessary to study
the parameters of the FDM process. Studying the effect of
3D printing process parameter on the response character-
istics of FDM parts helps us to adjust the level of process
parameters that improve the quality of printed parts [5–7].
Material occupying the largest market share in the field
of 3D printing is the photopolymers. To be able to compete
with traditional materials, the composite materials are abso-
lutely necessary for 3D printing to be a feasible technology
that can produce parts as superior as the parts produced by
conventional technologies with high mechanical, electri-
cal and thermal properties [8]. ABS, PLA, PC and PA are
among the various polymers used in 3D printing. Polylactic
Acid, most commonly known as PLA, is a polymer made
from renewable resources. Contrary to other thermoplastics
which are petroleum-based, some of the raw materials used
for PLA’s production include corn starch, tapioca roots, or
sugarcane. Its properties, however, are comparable to other
plastics in the industry. These properties make PLA the most
used in 3D printing [9].
With advances in materials and technology, 3D print-
ing has shifted from prototype production to final product
production. For mass production with additive production
method, the final products must have suitable mechanical,
quality, etc. properties to improve the performance of the
products. Recently, various researches have been done in the
field of 3D printing process optimization. in process optimi-
zation, extruder temperature, raster angle, layer thickness,
raster gap, raster width, contour width, and specimen ori-
entation are the process parameters that have been studied
extensively to obtain the highest possible mechanical prop-
erties [10, 11]. In addition, controllable input parameters
including nozzle temperature, print speed, layer orientation,
nozzle diameter, filament material diameter, layer height,
internal density, ambient temperature affect the quality of
the final products [12, 13].
3D printing is capable of producing small and large scale
components, but some obstacles in 3D production, are to
achieve good surface quality and component strength [14].
The surface roughness of products is of great importance
given the significant impact on the quality and function of
products. In many industrial applications, such as the pro-
duction and processing of metals, semiconductors, ceramics,
paper and plastics, surface roughness measurements are an
important part of quality inspection [15]. Surface rough-
ness is widely considered as one of the important factors of
quality parameters such as surface beauty, corrosion resist-
ance, fatigue life improvement, surface considerations, and
appropriate precision of critical surface. The flat surface,
due to the lack of post-production payment, greatly reduces
production costs. The mechanism of surface roughness for-
mation in products is very dynamic, complex, and dependent
on the production process [16]
Considering the various applications of 3D printing, the
need for effective use of this technology to produce com-
ponents with a good surface quality, sufficient strength
and minimum dimensional error is increasing. Hence, the
research process on the development of the 3D printing pro-
cess has entered a new phase and efforts to optimize the
process and its applications in new areas have increased
significantly.
Hwang et al. [17] investigated the thermal–mechanical
properties of metallic and polymer composites in 3D print-
ing of FDM. In this research, the effect of process param-
eters such as temperature and internal density on tensile
strength was investigated using differential scanning calo-
rimetry. Based on results, according to ABS viscosity at dif-
ferent temperatures, there is a relationship between tensile
strength and printing temperature. Additionally, it was con-
firmed that the ABS viscosity during extrusion, affects the
tensile properties of final products. Internal density, another
printing parameter, affects the tensile properties of samples,
in which the tensile strength decreases with increasing inter-
nal density.
Torres et al. [18] studied the influence of production
parameters on the mechanical properties of PLA samples
using FDM. In this regard, the Taguchi method has been
used to design experiments and to implement the optimiza-
tion part, the analysis of variance was applied. Based on


---


## Page 4


Progress in Additive Manufacturing
1 3
results, internal density and layer thickness affect the ten-
sile strength, directly. In addition, increasing the tempera-
ture due to increased coherence between layers improves
tensile strength. The study also showed that with low
internal density for material storage, the tensile strength
improves through the increase of the surrounding layers.
Ning et al. [19] examined the effect of printing angle,
internal network printing speed, layer thickness and noz-
zle temperature on the tensile properties of 3D carbon
fiber reinforced composites. In this study, after printing
parts by FDM, tensile test was performed to obtain tensile
properties. Scanning electron microscopy is also used for
better analyzing the experimental data. Based on practi-
cal results, the highest tensile properties were obtained
at a nozzle temperature of 200 °C, printing angle of [0,
90], printing speed of 25 mm/s and a layer thickness of
0.15 mm.
Tontowi et al. [20] optimized the FDM 3D printing pro-
cess parameters to achieve the maximum quality of parts.
Therefore, printed ASTM D638 standard parts have been
evaluated in terms of tensile strength and dimensional
accuracy. In this research, optimization of layers thickness,
printing temperature and angle, was performed using the
combined response surface and Taguchi method. Based on
the results, the tensile strength of the printed parts is mainly
influenced by the layer thickness, while the dimensional
error is created by the printing angle.
Xiong et al. [21] examined the effect of input parameters
on the surface roughness of thin-wall parts which were pro-
duced by gas metal arc welding. In this regard, a laser vision
system was developed to investigate surface appearance and
roughness evaluation of the low carbon steel parts during
gas metal arc welding process. In this study, the effect of
some parameters like the interlayer temperature, the wire
velocity, moving velocity and the constant ratio of the wire
velocity to the moving velocity on the surface roughness
of parts thin walls were discussed. According to results, by
constant keeping of other parameters, the decrease of the
interlayer temperature is accompanied by an increase in the
surface quality of parts. In addition, the lower wire velocity
and movement leads to reduce surface roughness.
Khatwani and Srivastava [22] investigated the mechani-
cal properties of printed parts by FDM 3D printing. In this
research, the effect of nozzle diameter, layer thickness and
printing plate temperature on mechanical properties includ-
ing bending and tensile strength of PLA samples were
investigated. In this regard, scanning electron microscopy
analysis has been performed to evaluate samples fracture
mechanism. According to the results, tensile and bending
strength enhance with increasing printing plate tempera-
ture. In addition, by increasing layers thickness, the tensile
strength decreases, while the bending strength increases. In
addition, with increasing nozzle diameter, tensile strength
increases, while the bending strength decreases firstly and
then increases.
Devicharana and Garg [23] examined the printing quality
of the FDM 3D printing parts by controlling input parame-
ters. The goal of this research is to solve the major problems
of 3D printing, including the adhesion of the initial layers
and the upper layer gaps by controlling the input parameters
such as the nozzle position, the printing speed of layers, and
the temperature of the printing plate. In this research, Pareto
analysis is used to examine the results. Based on results, the
proposed solutions to improve the quality problems will also
amend other features such as cost and print time in the 3D
printing process.
Deswal et al. [24] optimized process parameters to max-
imize dimensional accuracy in 3D FDM printing. In this
study, the input parameters including layer thickness, manu-
facturing orientation, number of lines and internal density
were optimized with the aim of maximizing dimensional
accuracy using combined RSM, artificial neural network and
genetic algorithm. Based on results, the combined neural
network and genetic algorithm as well as hybrid response
surface and genetic algorithm are suited to optimize the
accuracy of 3D printing dimensions. Using the combined
algorithm of the neural network and genetic algorithm, the
minimum percentage change in length, width and thickness
is less than 10%.
In ​3D printing process, surface quality has been under-
estimated as a major factor in the quality of manufactur-
ing components. In addition, investigation of the surface
quality by changing the affecting variables like the nozzle
temperature, layers thickness, the printing speed, the nozzle
diameter and materials density did not studied, yet. In addi-
tion, according to previous studies, it is observed that in the
area of ​the 3D printing process, most researches were done
practically using response surface or taguchi techniques, and
the use of meta heuristic-algorithms is limited to one case to
improve mechanical properties. However, there is no specific
mathematical model and meta-heuristic optimization method
to improve the quality of printed parts. Therefore, the main
objective of this study is to determine the optimal combina-
tion of 3D input parameters to minimize surface roughness
using hybrid artificial neural network and particle swarm
algorithm.
2  Research methodology
2.1  Experimental data
The final surface quality is not limited to the functional-
ity and appearance of parts, but it is also important to
save costs and reduce the production time of parts. One of
the major disadvantages of 3D FDM printing is that the


---


## Page 5


Progress in Additive Manufacturing
1 3
surface roughness of the printed parts is higher than that
of other processes. The low level of surface quality in the
final products of the FDM process is mainly due to process
layering. Hence, in this research, FDM technique for the
printing of components was used.
In this study, the effects of input parameters of the 3D
printing process have been comprehensively studied. After
three-dimensional 3D printing experiments, to understand
the performance and the effect of parameters on the sur-
face quality, experiments were carried out using five fac-
tors affecting surface roughness in 3D printing. The sub-
jected factors include nozzle temperature, layer thickness,
printing speed, nozzle diameter and internal density which
were considered at three levels and designed with a CCD
method. Both domain and coded levels for variables of
FDM 3D printing process are reported in Table 1.
According to Table 1, CCD design with five independ-
ent variables was performed at three levels (− 1, 0, and
1), under α = 1 with Design Expert software. Test design
results have been reported in Table 2. Based on the results
of the CCD design, within 43 implementations, 1 test was
located in the center point, 10 tests were located in the axis
points and 32 tests were in the factorial locations.
Designated experiments were manufactured with a
primary red PLA by FDM 3D printers. The samples are
in rectangular 70 mm × 50 mm forms and with the thick-
ness of 5 mm. Figure 1 shows 3D isometric image of the
intended sample for printing samples that were drawn by
AutoCAD software.
All samples were manufactured by Novin Electric Com-
pany with a FDM 3D printer (Fig. 2). Samples were pro-
duced according to the test matrix under equal condition;
with a precision of 50 microns and constant temperature
of 25 ± 1° C. Figure 2 illustrates the 3D printing process
of desired parts.
43 pieces were printed under the same conditions and
then were coded for surface roughness measurements. Fig-
ure 3 shows the typical printed parts.
In this research, the surface roughness of parts was
measured with the Talyprofile gold machine of Starrett
SR300 model in the Razi Metallurgy Research Center. To
avoid the measurement error, roughness test for each piece
was performed twice. Figure 4 demonstrates the Talypro-
file gold surface roughness test device.
After determining the roughness value of each sample,
the input and output data matrix has been completed. In
Table 2, the designed experiments and surface roughness of
each sample has been listed.
2.2  Response surface methodology (RSM)
Due to the use of higher raw materials and a great deal of
time in the production process, researchers are continually
looking for ways to minimize the number of experiments
that result in lower operating and manpower costs [25, 26].
The RSM is a method that generates test design matrix.
Therefore, the number of experiments that need to evaluate
multiple variables and their interaction is reduced [27]. RSM
is developed by Box and Draper [28]. It is also an effective
statistical method for optimizing processes with complex
relationship between variables [29].
For practical reasons, in a 3D printing process, the princi-
pal parameters namely the nozzle temperature, the thickness
of the layers, the printing speed, the nozzle diameter, and
the percentage of materials affect the surface roughness of
products. Usually, researchers use the Box–Behnken method
or CCD method for the RSM framework to obtain design
experiments input matrix. In this study, the CCD has been
used to classify and design the test between the response
variable (surface roughness) and independent variables (noz-
zle temperature, thickness of layers, printing speed, nozzle
diameter and internal density). In addition, the response
variable (Ra) is also expressed as a function of independent
process variables.
2.3  Hybrid neural network algorithm and particle
swarm
Artificial neural network is one of the most popular predic-
tion models that is usually used to estimate outputs in the
range of input parameters. The researchers have success-
fully used the neural network several times to achieve the
machining estimation and rotational parameters [30]. The
neural network is a superior and more accurate modeling
Table 1   Experimental range
and coded levels of the process
variables
Variable (factors)
Units
Design range and coded leve
− α
− 1
0
1
α
Nozzle temperature
C°
190
190
200
210
210
Layer height
µm
100
100
150
200
200
Print speed
mm/s
30
30
75
120
120
Nozzle diameter
mm
0.3
0.3
0.4
0.5
0.5
Infill density
%
10
10
20
30
30


---


## Page 6


Progress in Additive Manufacturing
1 3
method in comparison with the RSM method, because the
nonlinearity of the function can be well illustrated by neu-
ral network [31]. In addition,  to find the optimal global
point in the developed space by the neural network, we can
use the particle swarm optimization (PSO) algorithm [32].
PSO algorithm is one of the optimization techniques that
operates based on a population of early responses. This
technique was first developed by Kennedy and Eberhart
Table 2   CCD matrix for FDM process parameters
Experiment
no.
Nozzle tem-
perature (C°)
Layer height
(µm)
Print speed
(mm/s)
Nozzle diam-
eter (mm)
Infill den-
sity (%)
Test1: surface
roughness (µm)
Test2: surface
roughness (µm)
Standard
deviation
1
210
200
30
0.3
30
42.7
43.1
0.28
2
190
150
75
0.4
20
26.2
26.4
0.14
3
190
200
30
0.5
10
54
54.2
0.14
4
200
200
75
0.4
20
30.5
30.5
0
5
190
100
120
0.5
10
25
25.2
0.14
6
190
100
120
0.3
10
18.3
18.1
0.14
7
190
100
30
0.3
10
26.3
26.3
0.28
8
210
100
30
0.3
30
24.8
25
0.14
9
190
100
120
0.3
30
16
15.6
0.28
10
190
100
30
0.5
10
34.1
33.9
0.14
11
190
200
120
0.3
30
29.6
30.2
0.42
12
200
150
120
0.4
20
27.8
28
0.14
13
210
150
75
0.4
20
30.6
30.2
0.28
14
210
100
120
0.5
10
29.3
28.9
0.28
15
210
100
30
0.3
10
51.8
51.8
0
16
210
200
120
0.3
30
34
33.8
0.14
17
210
100
120
0.5
30
23.7
23.3
0.28
18
210
200
30
0.5
10
58
58.2
0.14
19
200
150
75
0.4
10
33.3
32.9
0.28
20
210
100
30
0.5
10
38
38.2
0.14
21
190
100
30
0.3
30
21
20.8
0.14
22
210
200
120
0.5
30
43.6
43.6
0.14
23
210
200
120
0.3
10
39.6
39.4
0.14
24
210
200
120
0.5
10
49.1
49.1
0
25
210
200
30
0.3
10
48.9
49.3
0.28
26
200
150
75
0.5
20
33.1
32.5
0.42
27
210
200
30
0.5
30
52.3
52.7
0.28
28
210
100
30
0.5
30
32.4
32.6
0.14
29
190
200
30
0.5
30
48.6
48.4
0.14
30
210
100
120
0.3
30
17.6
17.2
0.28
31
210
100
120
0.3
10
20.5
20.5
0
32
200
100
75
0.4
20
19
18.8
0.14
33
190
200
120
0.3
10
35.3
35.7
0.28
34
200
150
75
0.3
20
23.9
24.1
0.14
35
200
150
75
0.4
30
27.7
27.5
0.14
36
200
150
75
0.4
20
28
28.8
0.57
37
200
150
30
0.4
20
36.9
36.9
0
38
190
200
120
0.5
10
45
45.2
0.14
39
190
200
30
0.3
30
38.8
39
0.14
40
190
200
30
0.3
10
44.3
44.7
0.28
41
190
100
120
0.5
30
20.2
19.4
0.57
42
190
100
30
0.5
30
28.7
28.7
0
43
190
200
120
0.5
30
43.1
43.1
0


---


## Page 7


Progress in Additive Manufacturing
1 3
[32], based on the collective behavior of birds and fishes
populations [33].
One of the advantages of meta-heuristic algorithms is
the ability to combine them. Although neural networks are
able to track the complex and nonlinear relationship between
independent variables and output variables but, there are
limitations like slow learning. As a result, the use of opti-
mization algorithms such as PSO can significantly improve
ANN performance. Several researchers have succeeded in
using hybrid ANN and PSO models in solving engineering
problems [34].
In this study, an ANN-PSO hybrid algorithm was used to
determine the optimal composition of 3D printing process
parameters. The flowchart of this hybrid algorithm is shown
in Fig. 5. According to this flowchart, after determining the
process parameters to examine the effect on the surface
roughness, the experiments are designed to fit the specified
range of input parameters. After obtaining the input and out-
put data matrix, the Multi-Layer Perceptron (MLP) Neural
Network used to train data. Finally, the trained network that
determine the input parameters by specifying the target func-
tion is combined with particle swarm algorithm and created
the ANN-PSO hybrid algorithm.
3  Results
3.1  Trained neural network
The first step in training with ANN is to select the optimal
structure for the network. Select the optimal structure of
the neural network include selecting the components of the
neural network such as, the appropriate number of hidden
layers and the number of neurons in these layers, the suitable
activation functions and training algorithm with the research
data. To select the appropriate network, three activation
functions namely Tan-sigmoid, Logistic and Purelin and for
the selection of the training algorithm, two Newton-like and
Levenberg–Marquardt algorithms have been tested. Accord-
ing to experiments, the most suitable activation function and
learning algorithm are Tan-sigmoid function for middle lay-
ers and Purelin function for the output layer, respectively.
On the other hand, the proper learning algorithm is Leven-
berg–Marquardt algorithm. In addition, the number of neu-
rons in the input and output layers were obtained through
trial and error. Based on the basic statistical observations
and testing of several neural network algorithms, to find the
optimal network, the multilayer perceptron neural network
has been selected as the optimal network. To achieve the
optimal multilayer perceptron neural network, 18 tested
models have been reported in Table 3.
According to Table 3, the best structure for the neural
network is Model 15, which compared to other structures,
Fig. 1   CAD designed specimen
Fig. 2   FDM 3D printing process
Fig. 3   Samples of printed parts
Fig. 4   Talyprofile gold surface roughness tester


---


## Page 8


Progress in Additive Manufacturing
1 3
has the lowest mean square error (223.79), the highest corre-
lation coefficient (0.974) and the coefficient of determination
(0.949). Thus, the multilayer neural network with 7 and 4 of
neurons in the middle layers and one neuron in the output
layer considered to be the best optimal network structure.
The structure of the developed neural network (7-4-1) is
shown in Fig. 6.
The performance of the developed neural network
requires more information for training, testing and valida-
tion, while empirical experiments are limited due to factors
such as the cost of raw materials and manpower costs. In
this study, to solve this problem, every roughness test was
used as an experimental test for network training. Thus, 86
datasets for training the neural network (7-4-1) have been
used. These 86 data are randomly divided into training data
sets (70%), test data sets (15%) and validation data (15%). In
other words, 60 data for training, 13 data for testing and 13
data for validation purposes have been considered. Figure 7
depicts the implementation of the multilayer perceptron neu-
ral network (7-4-1).
By implementing ANN, the trained network function for
correlation coefficient, determination coefficient and mean
squared error is determined. Figure 8 demonstrates the
regression diagram of the data, which includes the linear
correlation coefficient at training stages, testing and valida-
tion. In addition, Fig. 8 shows the determination coefficient
Fig. 5   Flow chart of hybrid
ANN and PSO for 3D printing
process parameters optimization
Initialize process parameters
Initialize particles
Design variables
Designing experiments
and printing parts
Initial design space
Evaluating the objective function based on the structure of the trained neural network
Record the best position for each particle (Pi best)
& best position among all particles (Pg best)
Convergenc
e check
Optimal 3D printer process parameters
Update the vector of the velocity of all particles
and transfer particles to new situation


---


## Page 9


Progress in Additive Manufacturing
1 3
and mean squares for the total data in the perceptron neural
network (7-4-1).
According to Fig. 8, the correlation coefficient for total
data is equal to 0.97407. Accordingly, the output of the
neural network is in the form of hollow circles against
the targets, and the best linear fit has been shown with
the dash lines. It is observed that the fitted line is close to
this half that indicates the ability of the neural network to
predict surface roughness values based on various input
parameters in the printed parts of the 3D FDM printer.
The distribution of points represents a positive correla-
tion between the output data obtained from the rough-
ness metering tests and predictions by the neural network
(Fig. 9).
To train data for the roughness of printed parts with a
3D printer, specifications of the optimal neural network
criteria are listed in Table 4. Thus, based on neural net-
work criteria, such a learning network can predict a sam-
ples surface roughness with over 94%.
In the training of the present network, 60 data for train-
ing, 13 data for testing and 13 data for validation purposes
were considered. Validation data can be used to check the
performance of the neural network. To measure the per-
formance of the trained neural network based on 13 data
allocated for the validation, actual data and data provided
by the developed neural network are listed in Table 5.
According to Table 5, the maximum relative error is
0.17 and the lowest relative error is 0.01. Figure 10 shows
the comparison between these values in the chart format.
As shown in Fig. 10, the predicted and actual values do
not differ significantly. Figure 11 depicts the regression
diagram of the actual and predicted validation data which
indicates that these validation data have a determination
coefficient of 0.92.
Regarding the results and evaluation of the neural net-
work, it can be stated that the multilayer perceptron neural
network (7-4-1) is able to predict the surface roughness as
a quality objective of 3D printed parts. To minimize the
surface roughness, the developed neural network can be
combined by PSO algorithm.
Table 3   Result obtained from different hidden layer
Hidden layers
R
R2
MSE
1
1–5
0.941
0.887
226.56
2
2–5
0.962
0.926
227.41
3
5–3
0.971
0.943
236.79
4
4–5
0.922
0.850
228.54
5
5–5
0.973
0.947
233.92
6
1–6
0.968
0.937
234.44
7
6–2
0.950
0.902
225.42
8
6–3
0.901
0.820
230.45
9
6–4
0.956
0.913
226.69
10
6–5
0.941
0.885
256.86
11
6–6
0.936
0.876
243.42
12
7–1
0.944
0.891
227.87
13
7–2
0.952
0.907
246.62
14
7–3
0.964
0.930
229.11
15
7–4
0.974
0.949
223.79
16
7–5
0.973
0.947
238.28
17
7–6
0.962
0.926
225.33
18
7–7
0.953
0.901
233.46
Fig. 6   Architecture of neural network (7-4-1)


---


## Page 10


Progress in Additive Manufacturing
1 3
3.2  Implementation of ANN‑PSO algorithm
In this study, hybrid ANN and PSO algorithm has been
developed to optimize the input parameters of 3D print-
ing process with the aim of minimizing surface roughness
via MATLAB software. The flowchart of this combined
algorithm is shown in Fig. 5. Based on Fig. 5, in the first
stage, the experiments are designed in accordance with the
specified parameters, and after the training and performance
check of both R2 and MSE, the MLP neural network is used
for mapping the 3D printing process. In the next steps, opti-
mization of the input parameters is performed based on the
PSO algorithm.
3.3  RSM results
RSM was used to investigate the interaction of each inde-
pendent factor on the surface roughness and also to optimize
the input parameters. This optimization was performed for
comparison with the results of ANN-PSO algorithm. To
select the best model for data analysis, details of the model
types including p value,1 determination coefficient (R2),
adjusted determination coefficient and predicted determi-
nation coefficient are listed in Table 6.
According to Table 6, the P-value for both linear and
quadratic model is less than 0.05, where the P-value of less
than 0.05 indicates that the model is significant. On the
other hand, the coefficients of determination, the adjusted
and predicted coefficients in the quadratic model are 0.9257,
0.09097 and 0.8167, correspondingly which are well suited
with the independent variables than the linear model.
Accordingly, based on the model factors, the model is used
to analyze the data.
Figure 12 shows the effect of each process variables on
the variation of the response variable (surface roughness)
and also the deviation of variables from the center point
(reference). Based on Fig. 11, the reference point for inter-
nal variables are as follows: the nozzle temperature (A) of
200 °C, the height of the layers (B) of 150 μm, the printing
speed (C) of 75 μm / s, the nozzle diameter (D) of 0.4 mm
and the internal density (E) is 20%.
Based on Fig. 12, the independent parameters effect on
the surface roughness differently, so that increasing the
thickness of the layers, nozzle temperature and nozzle diam-
eter leads to an increase in surface roughness with different
slopes. On the other hand, an increase the printing speed
from 30 μm/s and the density from 10% to a reference point
leads to a decrease in surface roughness with a steeper gradi-
ent, while roughness increases after a reference point with
a slight gradient.
The interaction effects of independent variables on the
surface roughness can be well analyzed by three-dimen-
sional graphs. In Fig. 13, the graph of the interaction effects
of both the nozzle temperature and the thickness of layers
on the surface roughness have been shown in two form of (a)
alignment charts and (b) three dimensional graphs.
According to Fig. 13, it is observed that with increas-
ing the nozzle temperature from 190° C to 210° C and the
thickness of the layers from 100 μm to 200 μm, the surface
roughness also increases. The nozzle temperature has a great
influence on the melting of raw materials. Because of the
design simplicity of the printed parts and also the type of
raw material (PLA), it can be inferred that the temperature
of 190 °C is the most suitable temperature for the selected
nozzle, which varies according to the different type of raw
materials and several design of parts. On the other hand, the
direct effect of the layers thickness on the surface roughness
is that by decreasing the thickness of the layers, the lay-
ers become less visible, and the surface of the printed part
becomes smooth. As the thickness of the layers increases,
the surface of the printed part becomes sharper and the lay-
ers appear. In general, the maximum and minimum rough-
ness of the surface, considering two parameters namely the
nozzle temperature and layers thickness, and keeping con-
stant the other parameters, is about 35 and 20 µm.
Fig. 7   Artificial neural network for FDM process parameter optimiza-
tion
1  Probability value.


---


## Page 11


Progress in Additive Manufacturing
1 3
Fig. 8   Correlation coefficient of
data in neural network (7-4-1)
Fig. 9   R2 all & all MSE of data in neural network (7–4-1)


---


## Page 12


Progress in Additive Manufacturing
1 3
Figure 14 shows the interaction graph of both nozzle
diameter and the printing speed on the surface roughness as
(a) the alignment graphs and (b) three dimensional graphs.
Based on Fig. 14, the printing speed in the range of
30 μm/s up to 120 μm/s initially decreases the roughness
of the surface of the printed parts with a steep slope, and
then increases the surface roughness with a moderate slope.
Generally, in 3D printers, speed increases leads to decrease
the surface quality, while in simple design pieces, this is
not the case, and the main reason for these changes is the
design simplicity of printed parts. In addition, according to
Fig. 13, the surface roughness is different for various nozzles
with the diameter of 0.3 mm, 0.4 mm and 0.5 mm, and as
the nozzle diameter increases, the surface roughness of the
printed parts increases too. The reason for the difference in
roughness of different nozzles is that the smaller the nozzle
Table 4   Prediction performance parameters of developed ANN for
training data set (7–4-1)
R
R2
MSE
Training
0.96934
0.93961
216.8723
Test
0.98965
0.9794
285.9348
Validation
0.96653
0.93418
220.2515
Average
0.97407
0.94882
223.793
Table 5   Actual and predicted outputs
Experiment
no.
Actual values
Predicted values
Relative error
8
24.8
28.96
0.17
13
30.6
32.28
0.05
14
29.3
28.36
0.03
24
49.1
49.42
0.01
37
36.9
37.01
0.01
50
26.7
30.94
0.16
51
25
25.59
0.02
59
33.8
33.44
0.01
62
32.9
31.86
0.03
73
17.2
18.89
0.10
76
35.7
33.84
0.05
81
45.2
43.15
0.05
85
28.7
27.05
0.06
Fig. 10   Compare actual and predicted Validation
Fig. 11   Regression diagram of actual and predicted validation data
Table 6   Figures summary of the models
Model
p value
R2
Adjusted R2
Predicted R2
Linear
0.0001
0.8286
0.8054
0.7744
2FI
0.5664
0.8706
0.7987
0.6948
Quadratic
0.0003
0.9257
0.9097
0.8167
Cubic
0.8710
0.9774
0.8643
0.1816
Fig. 12   Deviation from reference point


---


## Page 13


Progress in Additive Manufacturing
1 3
diameter leads to the delicacy increase in printing process.
In general, the maximum and minimum roughness of the
surface, taking into account the two parameters of printing
speed and nozzle diameter, and constant holding of other
parameters is about 50 and 35 microns.
Figure 15 shows the interaction graph of both the nozzle
temperature and internal density parameters on the surface
roughness as (a) the alignment graphs and (b) three dimen-
sional graphs.
Based on Fig. 15, density value in the range of 10–30%
initially reduces the surface roughness and then increases
it. Internal density plays a crucial role in the connection of
parts and outflow patterns in a three-dimensional model.
High internal density reduces outflow and increases the
strength of the piece, thus selecting the most appropriate
choice as the internal density is very important. Finally,
the maximum and minimum roughness of the surface, tak-
ing into account the two parameters of nozzle temperature
and the amount of density, and keeping other parameters
is about 38 and 30 µm.
Fig. 13   RSM plot and contour plot of the surface roughness as the function of nozzle temperature and layer height
Fig. 14   RSM plot and contour plot of the surface roughness as the function of nozzle diameter & print speed


---


## Page 14


Progress in Additive Manufacturing
1 3
The interactions effects of other independent variables
can also be considered on surface roughness in 2D and
3D graphs.
Based on conducted experiments and analysis of tests to
predict the model, the RSM approach provides a quadratic
model, as shown in Eq. (1).
The coefficients were analyzed using ANOVA, and
the sum of squares, degree of freedom, F function and
P value are reported in Table 7. The values ​for F and P
value determine the meaningfulness of the model coeffi-
cients. P values of less than 0.05 represent that quadratic
model is meaningful. On the other hand, the coefficient of
determination for this model is 92.57%, which indicates
that the fitted model describes changes of 92.57% of total
changes in the studied domain. In addition, the adjusted
determination coefficient indicates that the model does not
show less than 10% of the variation of the output variable.
On the other hand, one of the most important statistics in
variance analysis is "Lake of fit", in which the P value
is 0.44 in this model and is not significant at 95% level.
Considering the model’s significance at the level of 95%,
the predicted model in Eq. 1 can be used to determine the
surface roughness of printed flat parts with a 3D printer.
(1)
Ra = 27.35 + 2.41A + 8.62B −4.88C + 3.63D
−3.15E −0.62AB −0.93AC −0.68AD −0.84AE + 0.59BC
+ 1.41BD + 0.56BE + 0.64CD + 0.98CE + 0.64DE
+ 1.13A2 −2.52B2 + 5.18C2 + 1.18D2 + 3.13E2
According to Table 7, P values for each of 3D printing
process parameters are less than 0.05, which indicates the
effectiveness of these parameters on the surface roughness.
On the other hand, P Value is significant for interactions
effects between layer thickness and print speed, in other
words, these two parameters affect each other.
3.4  Optimization
To minimize the surface roughness of the printed parts
which were produced by 3D printing process, both RSM
and ANN-PSO methods have been implemented to find the
optimum values of input parameters (nozzle temperature,
thickness of the layers, printing speed, nozzle diameter and
internal density).
There are two standard PSO and improved PSO algo-
rithms. The standard PSO algorithm has a constant inertia
weight. While the improved PSO algorithm do the search
with limited search space via improvements such as linear
inertial weight loss. In this study, an improved PSO was used
to combine with the MLP neural network. For this algo-
rithm, 30 population density and maximum 30 repetitions
considered, and the corresponding value for both C1 and
C2 is 2.
Fig. 15   RSM plot and contour plot of the surface roughness as the function of nozzle temperature and infill density


---


## Page 15


Progress in Additive Manufacturing
1 3
In this research, to achieve optimal parameters with the
least surface roughness, the hybrid ANN-PSO algorithm
has been implemented. Ten runs have been considered and
median values of these runs were considered as the optimal
parameter. Table 8 shows the results of hybrid ANN-PSO
algorithm.
According to Table 8, the mean value of the optimum
value in 10 runs are as follows: for the nozzle temperature
is 192.198 °C, the thickness of the layers is 100 μm, the
printing speed is 97.06 mm/s, the nozzle diameter is 0.3 and
for the internal density is 975.24%. With the combination
of these parameters, roughness of 11.319 μm is predicted.
To validate the results of the optimization of the hybrid
algorithm, keeping the printing conditions of the previ-
ous pieces, an optimum piece has been produced with the
optimal parameters of the hybrid algorithm. In addition,
the roughness test has been performed according to previ-
ous conditions. After the roughness test, it was found that
the roughness of the optimum hybrid sample is 11.9 μm.
According to the prediction value of 11.319, it was inferred
that the predicted error value is 4.88%.
To validate the proposed method for optimizing the 3D
printing process, the results of this method are compared
with the results of RSM optimization. Hence, 10 RSM sug-
gestions are reported in Table 9.
According to Table 9, considering the average of ten RSM
recommendations, the nozzle temperature is 190.062 °C, the
thickness of the layers is 100.0391 μm, the printing speed
is 96.0525 mm/s, the nozzle diameter is 0.3 mm and the
internal density is 24.8306%. The combination of these
parameters predicts roughness of 10.5852 μm. To confirm
the results of RSM optimization, maintaining optimal print-
ing conditions of the previous pieces, an optimum piece has
been produced with optimal parameters. In addition, the
roughness test has been performed according to the previ-
ous conditions. After the roughness test, it was revealed that
the surface roughness of the optimum sample is 11.6 μm.
Based on the predicted value of 10.5852 μm, the predicted
error value is 8.75%.
Based on validating results of both methods, by produc-
ing optimal samples in accordance with optimal parameters
and their roughness measurements, it was found that the
hybrid algorithm has higher ability to optimize and predict
the surface roughness of the printed parts with 3D FDM
Table 8   ANN-PSO predicted
optimum process and output
parameters for surface
roughness
Run number
Nozzle
temperature
(°C)
Layer
height
(µm)
Print speed (mm/s)
Nozzle
diameter
(mm)
Infill density (%)
Surface
roughness (
µm)
1
200.494
100
91.086
0.3
24.599
12.382
2
190
100
99.562
0.3
24.146
10.874
3
190
100
96.992
0.3
30
12.022
4
190
100
99.045
0.3
24.277
10.872
5
201.484
100
90.305
0.3
24.516
12.389
6
190
100
102
0.3
23.966
10.953
7
190
100
98.918
0.3
24.306
10.873
8
190
100
99.084
0.3
24.367
10.871
9
190
100
98.942
0.3
24.436
10.872
10
190
100
94.636
0.3
25.178
11.082
Average
192.198
100
97.060
0.3
24.975
11.319
Table 7   Quadratic model ANOVA result for surface roughness
*Nozzle temperature (A), Layer height (B), Print speed (C), Nozzle
diameter (D), Infill density (E)
Sum of Squares
Std deviation
DF
F value
P value
Model*
4964.63
1.24
20
22.15
0.0001
A
197.28
0.57
1
17.61
0.0004
B
2524.97
0.57
1
225.35
0.0001
C
810.47
0.57
1
72.33
0.0001
D
447.87
0.57
1
39.97
0.0001
E
337.36
0.57
1
30.11
0.0001
AB
12.25
0.59
1
1.09
0.3071
AC
27.75
0.59
1
2.48
0.1298
AD
14.85
0.59
1
1.33
0.2620
AE
22.44
0.59
1
2.00
0.1710
BC
11.28
0.59
1
1.01
0.3266
BD
63.28
0.59
1
5.65
0.0266
BE
10.13
0.59
1
0.90
0.3521
CD
13.26
0.59
1
1.18
0.2884
CE
30.42
0.59
1
2.71
0.1136
DE
13.01
0.59
1
1.16
0.2930
A2
3.15
2.14
1
0.28
0.6014
B2
15.56
2.14
1
1.39
0.2511
C2
65.94
2.14
1
5.89
0.0239
D2
3.43
2.14
1
0.31
0.5855
E2
24.09
2.14
1
2.15
0.1567


---


## Page 16


Progress in Additive Manufacturing
1 3
printers. Based on results, the hybrid algorithm with the
error of 4.88% and RSM with the error of 8.75% can predict
and optimize the printed samples.
The optimization results show that both RSM and
hybrid algorithm can estimate optimal parameters with an
error of less than 10%. According to the matrix of experi-
ments, minimum surface roughness is 15.8 µm. As a result,
both optimization methods have improved surface quality,
although the ability of the hybrid algorithm in this area is
greater. Figure 16 shows the improvement of the surface
quality of parts after applying optimization methods.
4  Conclusion
In this paper, the effect of FDM 3D printing process parame-
ters on the surface roughness of printed parts has been inves-
tigated. In this work, after determining the range of input
parameters, 43 experiments were designed with a central
composite design. Designed tests were produced with 3D
FDM printers and roughness tests have been performed on
them. In this research, the effect of input parameters includ-
ing nozzle temperature, layers thickness, printing speed,
nozzle diameter and internal density on the surface rough-
ness of parts have been investigated using the response sur-
face method. According to results, the layer’s thickness is
directly related to the surface roughness, as the thickness of
layers increases, the roughness of the surface increases too,
which demonstrates there is good conformity between this
research and previous studies. The direct effect of layer’s
thickness with the surface roughness is that by decreasing
the thickness, layers become less visible and the surface of
the printed part becomes smooth. By increasing the layer’s
thickness, the surface of the printed part is sharper and lay-
ers appear more. In addition, with increasing the speed, the
roughness firstly decreases and then increases. The similar
occurrence is also happens for internal density and nozzle
temperature. On the other hand, 0.3 mm of nozzle diameter
achieves the best surface quality. The internal density plays
a crucial role in the connection of different parts and outflow
Table 9   RSM predicted optimum process and output parameters for surface roughness
Run number
Nozzle tempera-
ture (°C)
Layer height (µm)
Print speed (mm/s)
Nozzle diameter
(mm)
Infill density (%)
Surface
roughness (
µm)
1
190.001
100.259
95.600
0.3
24.739
10.627
2
190.001
100.000
98.270
0.3
23.835
10.611
3
190.595
100.002
95.635
0.3
24.842
10.598
4
190
100.000
93.819
0.3
25.121
10.594
5
190.020
100.055
98.143
0.3
24.620
10.592
6
190.001
100.000
94.668
0.3
25.625
10.574
7
190.001
100.058
95.401
0.3
24.872
10.572
8
190
100.017
95.924
0.3
24.820
10.564
9
190.001
100.000
96.802
0.3
24.842
10.561
10
190
100.000
96.263
0.3
24.990
10.559
Average
190.062
100.0391
96.0525
0.3
24.8306
10.5852
Fig 16   Samples a before and b after optimization


---


## Page 17


Progress in Additive Manufacturing
1 3
patterns in a three-dimensional model, which high internal
density leads to an outflow reduction and increased compo-
nent strength. In this study, it was found that not only the
density effects on the strength but also effects on the surface
roughness of parts.
The main goal of this research is to determine the optimal
parameters for achieving maximum surface quality. To opti-
mize the parameters of the 3D printing process, two methods
namely response surface and hybrid algorithm of both neu-
ral network and particle swarm have been used. Therefore,
the experiments matrix after training with a multi-layered
perceptron neural network (7-4-1) with a determination
coefficient of 0.95 was combined to determine the optimum
composition of the input parameters with particle swarm
algorithm. The optimal parameters for validating the model
have been empirically extracted and investigated. On the
other hand, the validation has been done for optimal param-
eters of the response surface method.
Based on results of validating methods, by producing
optimal samples in accordance with optimal parameters and
their roughness measurements, it was found that the hybrid
algorithm and the response surface method have high ability
to optimize and predict the roughness of parts printed with
3D FDM printers. Based on results, the hybrid algorithm
with the error of 4.88% and response surface method with
error of 8.75% can predict and optimize printed samples. In
this way, the optimization results show that both response
surface and hybrid algorithm can estimate the optimal
parameters with an error of less than 10%. According to
the matrix of experiments, minimum surface roughness is
15.1 µm, while optimization results in a roughness of less
than 12 µm. As a result, both optimization methods have
improved surface quality, although the ability of the hybrid
algorithm in this area is greater. Therefore, the use of meta
heuristic algorithms improves the performance of printed
parts during 3D printing process.
References
	 1.	 Ngo TD, Kashani A, Imbalzano G, Nguyen KT, Hui D (2018)
Additive manufacturing (3D printing): a review of materi-
als, methods, applications and challenges. Compos B Eng
143:172–196
	 2.	 Bhushan B, Caspers M (2017) An overview of additive manu-
facturing (3D printing) for microfabrication. Microsyst Technol
23(4):1117–1124
	 3.	 Mao M, He J, Li X, Zhang B, Lei Q, Liu Y, Li D (2017) The
emerging frontiers and applications of high-resolution 3D print-
ing. Micromachines 8(4):113
	 4.	 De Laurentis KJ, Mavroidis C (2004) Rapid fabrication of a
non‐assembly robotic hand with embedded components. Assemy
Autom
	 5.	 Basavaraj C, Vishwas M (2016) Studies on effect of fused depo-
sition modelling process parameters on ultimate tensile strength
and dimensional accuracy of nylon. In: IOP conference series:
materials science and engineering, p 012035
	 6.	 Griffiths C, Howarth J, Rowbotham G-A, Rees A (2016) Effect
of build parameters on processing efficiency and material perfor-
mance in fused deposition modelling. Procedia CIRP 49:28–32
	 7.	 Leite M, Fernandes J, Deus AM, Reis L, Vaz MF (2018) Study of
the influence of 3D printing parameters on the mechanical proper-
ties of PLA.
	 8.	 Kamaal M, Anas M, Rastogi H, Bhardwaj N, Rahaman A (2020)
Effect of FDM process parameters on mechanical properties of
3D-printed carbon fibre–PLA composite. Prog Add Manuf:1–7
	 9.	 Mirón V, Ferrándiz S, Juárez D, Mengual A (2017) Manufacturing
and characterization of 3D printer filament using tailoring materi-
als. Procedia Manuf 13:888–894
	10.	 Goh GD, Yap YL, Tan H, Sing SL, Goh GL, Yeong WY (2020)
Process–structure–properties in polymer additive manufacturing
via material extrusion: a review. Crit Rev Solid State Mater Sci
45(2):113–133
	11.	 Domingo-Espin M, Travieso-Rodriguez JA, Jerez-Mesa R, Lluma-
Fuentes J (2018) Fatigue performance of ABS specimens obtained
by fused filament fabrication. Materials 11(12):2521
	12.	 Sun Q, Rizvi G, Bellehumeur C, Gu P (2008) Effect of process-
ing conditions on the bonding quality of FDM polymer filaments.
Rapid Prototyp J
	13.	 Sood AK, Ohdar R, Mahapatra SS (2009) Improving dimensional
accuracy of fused deposition modelling processed part using grey
Taguchi method. Mater Des 30(10):4243–4252
	14.	 Wohlers T (2012) Wohlers report 2012. Wohlers Associates, Inc,
	15.	 Choi J-W, Medina F, Kim C, Espalin D, Rodriguez D, Stucker
B, Wicker R (2011) Development of a mobile fused deposition
modeling system with enhanced manufacturing flexibility. J Mater
Process Technol 211(3):424–432
	16.	 Dhanasekar B, Mohan NK, Bhaduri B, Ramamoorthy B (2008)
Evaluation of surface roughness based on monochromatic speckle
correlation using image processing. Precis Eng 32(3):196–206
	17.	 Hwang S, Reyes EI, Moon K-s, Rumpf RC, Kim NS (2015)
Thermo-mechanical characterization of metal/polymer composite
filaments and printing parameter study for fused deposition mod-
eling in the 3D printing process. J Electron Mater 44(3):771–777
	18.	 Torres J, Cole M, Owji A, DeMastry Z, Gordon AP (2016) An
approach for mechanical property optimization of fused depo-
sition modeling with polylactic acid via design of experiments.
Rapid Prototyp J
	19.	 Ning F, Cong W, Qiu J, Wei J, Wang S (2015) Additive manufac-
turing of carbon fiber reinforced thermoplastic composites using
fused deposition modeling. Compos B Eng 80:369–378
	20.	 Tontowi A, Ramdani L, Erdizon R, Baroroh D (2017) Optimiza-
tion of 3D-printer process parameters for improving quality of pol-
ylactic acid printed part. Int J Eng Technol (IJET) 9(2):589–600
	21.	 Xiong J, Li Y, Li R, Yin Z (2018) Influences of process parameters
on surface roughness of multi-layer single-pass thin-walled parts
in GMAW-based additive manufacturing. J Mater Process Technol
252:128–136
	22.	 Khatwani J, Srivastava V (2019) Effect of process parameters on
mechanical properties of solidified PLA parts fabricated by 3D
Printing process. In: 3D Printing and Additive Manufacturing
Technologies. Springer, pp 95–104
	23.	 Devicharan R, Garg R (2019) Optimization of the print quality by
controlling the process parameters on 3D printing machine. In: 3D
Printing and Additive Manufacturing Technologies. Springer, pp
187–194
	24.	 Deswal S, Narang R, Chhabra D (2019) Modeling and parametric
optimization of FDM 3D printing process using hybrid techniques
for enhancing dimensional preciseness. Int J Interact Design
Manuf (IJIDeM) 13(3):1197–1214


---


## Page 18


Progress in Additive Manufacturing
1 3
	25.	 Cronje K, Chetty K, Carsky M, Sahu J, Meikap B (2011) Opti-
mization of chromium (VI) sorption potential using developed
activated carbon from sugarcane bagasse with chemical activation
by zinc chloride. Desalination 275(1–3):276–284
	26.	 Dehghani MH, Mostofi M, Alimohammadi M, McKay G, Yet-
ilmezsoy K, Albadarin AB, Heibati B, AlGhouti M, Mubarak
N, Sahu J (2016) High-performance removal of toxic phenol
by single-walled and multi-walled carbon nanotubes: kinetics,
adsorption, mechanism and optimization studies. J Ind Eng Chem
35:63–74
	27.	 Shojaeimehr T, Rahimpour F, Khadivi MA, Sadeghi M (2014)
A modeling study by response surface methodology (RSM) and
artificial neural network (ANN) on Cu2+ adsorption optimization
using light expended clay aggregate (LECA). J Ind Eng Chem
20(3):870–880
	28.	 Box GE, Draper NR (1987) Empirical model-building and
response surfaces. John Wiley & Sons
	29.	 Hesas RH, Arami-Niya A, Daud WMAW, Sahu J (2013) Prepara-
tion of granular activated carbon from oil palm shell by micro-
wave-induced chemical activation: optimisation using surface
response methodology. Chem Eng Res Des 91(12):2447–2456
	30.	 Ranganathan S, Senthilvelan T, Sriram G (2010) Evalua-
tion of machining parameters of hot turning of stainless steel
(Type 316) by applying ANN and RSM. Mater Manuf Process
25(10):1131–1141
	31.	 Desai KM, Survase SA, Saudagar PS, Lele S, Singhal RS (2008)
Comparison of artificial neural network (ANN) and response sur-
face methodology (RSM) in fermentation media optimization:
case study of fermentative production of scleroglucan. Biochem
Eng J 41(3):266–273
	32.	 Karri RR, Sahu J (2018) Modeling and optimization by particle
swarm embedded neural network for adsorption of zinc (II) by
palm kernel shell based activated carbon from aqueous environ-
ment. J Environ Manage 206:178–191
	33.	 Kennedy J, Eberhart R (1995) Particle swarm optimization. In:
proceedings of IEEE International Conference on Neural Net-
works. Piscataway December
	34.	 Momeni E, Armaghani DJ, Hajihassani M, Amin MFM (2015)
Prediction of uniaxial compressive strength of rock samples
using hybrid particle swarm optimization-based artificial neural
networks. Measurement 60:50–63
Publisher’s Note  Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional affiliations.
View publication stats


---
