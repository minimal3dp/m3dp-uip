# Modeling_and_parametric_optimization_of

> **Source:** `Modeling_and_parametric_optimization_of.pdf`
> **Converted:** 2025-11-22 21:18:07
> **Method:** PyMuPDF

---

## Page 1


Vol.:(0123456789)
1 3
International Journal on Interactive Design and Manufacturing (IJIDeM)
https://doi.org/10.1007/s12008-019-00536-z
TECHNICAL PAPER
Modeling and parametric optimization of FDM 3D printing process
using hybrid techniques for enhancing dimensional preciseness
Sandeep Deswal1 · Rajan Narang1 · Deepak Chhabra1
Received: 1 November 2018 / Accepted: 8 January 2019
© Springer-Verlag France SAS, part of Springer Nature 2019
Abstract
In this study, significant process parameters (layer thickness, build orientation, infill density and number of contours) are
optimized for enhancing the magnitude/dimensional preciseness of fused deposition modeling (FDM) devise units. Hybrid
statistical tools such as response surface methodology–genetic algorithm (RSM–GA), artificial neural network (ANN) and
artificial neural network-genetic algorithm (ANN-GA) in MAT LAB 16.0 are utilized for training and optimization. An
attempt has been made to build up a mathematical model in order to set up an indirect correlation between various FDM
process parameters and magnitude preciseness. Sequentially to verify the different developed models and the optimum pro-
cess parameters setting validation tests were also performed. The results showed that various hybrid statistical tools such as
RSM-GA, ANN and ANN-GA are very adequate tools for FDM process parameter optimization. The minimum percentage
variation in length = 0.06409%, width = 0.03961% and thickness = 0.85689% can be obtained by using ANN-GA.
Keywords Response surface methodology (RSM) · Artificial neural network (ANN) · Genetic algorithm (GA) · Fused
deposition modeling (FDM) · Process parameters
1 Introduction
Use of FDM is extensively increasing within in a number
of manufacturing sectors such as automotive, biomedical
implants, aerospace, electronic, telecommunication due to
ability to make prototypes or product with high quality and
different grades of engineering materials. The FDM complex
nature of fabricating end use part in various engineering
applications often create difficulty in selecting various con-
flicting process parameters and controlling high magnitude
preciseness.
Additive manufacturing or 3D printing, also known
as rapid manufacturing technique is used for fabricat-
ing products by depositing layers one over another in an
additive manner as go up against to subtractive manner. In
the current scenario to manage the increased antagonism
in the global economy has necessitated for manufacturers
to deliver new tailored products faster with higher magni-
tude preciseness, quality and good mechanical and physical
properties than before. Thus keeping in mind the end goal to
meet client requests and fulfillment has expanded producer
fixation towards 3D printing techniques. Different 3D print-
ing emerged in the last few years such as fused deposition
modeling (FDM), selective laser sintering (SLS), selective
laser melting (SLM), 3D ink jet printing (Binder Jetting),
Laminated object manufacturing (LOM). These 3D print-
ing techniques are capable of directly making any part of
the CAD database under consideration of different process
parameters, printing materials, manufacturing style, magni-
tude preciseness those could be used for different end use
engineering applications. FDM is one such 3D printing tech-
nique developed by Stratasys Inc. [1] is extensively used to
fabricate product or prototype from thermoplastic material
such as acrylonitrile butadiene styrene (ABS) [2] by deposit-
ing semi-molten plastic filament in a layer by layer additive
manner directly from a CAD model [3, 4] using the princi-
ple of extrusion. The demand of FDM is increasing within
in a number of manufacturing sectors such as automotive,
biomedical implants, aerospace, electronic, telecommunica-
tion [5] due to ability to fabricate prototype or product with
high quality and different grades of engineering materials.
So in such applications to maintain high magnitude stability
and repeatability of the fabricated parts, magnitude variation
 * Deepak Chhabra

deepaknit10@gmail.com
1
Department of Mechanical Engineering, UIET, Maharshi
Dayanand University, Rohtak, Haryana 124001, India


---


## Page 2


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
with stiff tolerance should be maintained. Magnitude pre-
ciseness, quality, mechanical and physical properties of
a part material in FDM process are dependent on various
selected conflicting process parameters [5–7]. Hence, the
study of these parameters is of paramount importance in
order to minimize the dimensional inaccuracy in comparison
to other 3D printing techniques. The complex process nature
and conflicting parameters of FDM creates much difficulty
in determining the process parameters which mainly affect
the magnitude preciseness [8]. Rayegani et al. [5] developed
a relationship between process parameters (Raster angle
and Part orientation) and tensile strength of the fabricated
parts by using Group method for data handling and found
that tensile strength is greatly affected by these two process
parameters. Sood et al. [9] analyzed the effect of different
process factors on the magnitude preciseness using artifi-
cial neural networks (ANN) and Taguchi method. Lieneke
et al. [10] studied about the geometrical deviation in FDM
fabricated parts which is very common due to various con-
flicting process parameters. Application of FDM fabricated
parts for end use part production is limited because relevant
challenges regarding process parameters have not been suf-
ficiently researched yet. Sahu et al. [11] used Fuzzy logic
combined with the Taguchi method to enhance the magni-
tude preciseness by optimizing the effect of various process
parameters. They pointed out that a large number of contra-
dictory factors independently or in interaction with others
may affect the magnitude preciseness. As a result, the fuzzy
logic method is used to improve the magnitude preciseness.
But the use of Fuzzy technique requires prior knowledge
and experience to apply precisely. Equbal et al. [12] used
Taguchi orthogonal array approach for experimental design
matrix combined with ANN and Fuzzy logic to develop
models for improving the magnitude preciseness in terms of
variation in length, width, thickness and diameter under con-
siderations of five factors viz., layer thickness, part build ori-
entation, raster angle, raster to raster gap (air gap) and raster
width each at three levels. Chou et al. [13] has studied that
deformation in FDM made up part is mainly due to growth
of inner stress which was analyzed by using finite element
analysis. Mohamed et al. [14] presented a review on various
optimization techniques such as RSM, Taguchi method, full
factorial, gray relational, fractional factorial, ANN, fuzzy
logic and GA in the determination and optimization of the
various process parameters for FDM. They found that there
were fruitful modern uses of these robust optimization tech-
niques to optimize the FDM process parameters to improve
the dimensional accuracy. The above discussed reading
shows that the magnitude preciseness of FDM made-up parts
depend upon various process parameters such as build ori-
entation, number of contours, layer thickness, raster width,
air gap and raster angle. Although to enhance the magnitude
preciseness of FDM made-up parts various optimization
techniques have been studied with top of writing. They have
few regular confinements and focal points outlined as takes
after: First a large portion of analysts has used Taguchi and
GRG to improve the magnitude precision. However, all such
conventional methods are unable to develop those models
which could predict and established relationship between
magnitude preciseness and various process parameters. For
example Taguchi method leads to non-optimal solution due
to higher interaction and confused interaction between two
factors with the other two factors [11, 15] and unable to
develop higher order empirical polynomial fitting models as
per multiple process optimization requirements in relation to
FDM 3D printing technique magnitude preciseness. Finally,
due to the presence of various conflicting process parameters
in FDM, manufacturers are not able to deliver good quality
parts in terms of magnitude preciseness [16]. Therefore an
interactive approach can be an efficient way to study interac-
tion between various process parameters and magnitude pre-
ciseness of FDM fabricated parts. An interactive approach
is one that encourages mutual communication between the
wellspring of the cooperation and the objective. Interactive
design a part of interactive approach rises as a methodology
that coordinates customer desires in the item advancement
process, enabling the planner to associate with the virtual
item and its condition [17]. Interactive design is a notewor-
thy monetary and vital issue in imaginative items age by
considering three factors: the specialists’ information, the
end-client fulfillment and the acknowledgment of capacities
[18]. In order to gain advancement in the produced parts, the
interactive design helps architects to actualize virtual mod-
els empowering the association among genuine and virtual
components [17]. So as to achieve this point, the proposed
strategy can be utilized as a helpful and profitable piece of
equipment by considering CAD design as a virtual item and
FDM fabricated parts dimensional preciseness as targeted
output at optimum process parameters value to success in
the competitive environment of mechanized units. So there
is a need for further study by keeping in mind indirect cor-
relation, multi parameters connections and limitations on
varying levels of parameters. In a manufacturing industry,
process of interactive design is carried out in following man-
ner: Identification of need, Designing of product, Evaluating,
Building of interactive version of product and Redesigning.
In this proposed study, to enhance the dimensional accuracy
of a product, a number of model has been built and based on
their outcomes an interactive design is proposed.
In contrast with past research, this work helped to
enhance the magnitude preciseness of FDM fabricate parts
by optimizing the various conflicting process parameters
using combine hybrid statistical tool such as RSM-GA,
ANN-GA. A four process parameters, five level central
composite designs were employed to grasp the interac-
tions between various process parameters and magnitude


---


## Page 3


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
preciseness of FDM made-up parts. Further with the help of
various hybrids statistical tools it has been tried to optimize
the process parameters more precisely by developing mathe-
matical models, so that enhanced magnitude preciseness can
be obtained by establishing inclusive relationship between
them. This study gives inclusive exploration by taking into
account layer thickness, build orientation, infill density and
number of contours as conflicting process parameters.
2  Methodology
2.1  Experimental work
A total of 30 specimens having magnitude 65 mm length,
13 mm width, and 4 mm thickness (Fig. 1) were fabricated
on the R*P2200i FDM machine by Adroitec using ABS
thermoplastic as an extruded material. All specimens were
designed and modeled in CAD software and converted into
Standard Tessellation Language (STL) file. Then the tool
path was generated for each specimen according to process
parameter value in the FDM machine using an STL file
which was generated earlier. Three values of each dimen-
sion length, width and thickness were measured by using
a micrometer having least count of 0.01 mm. Then average
of these three is considered as experimental value. In this
work percentage variation in length, width and thickness
were taken as the output response value.
2.2  Experimental plan
2.2.1  FDM process parameters
From above discussed literature, it is found that the mag-
nitude preciseness of FDM fabricated parts depends upon
various process parameters. Four parameters layer thick-
ness, build orientation, number of contours and infill density
selected with their range and levels are shown in Table 1.
The low and high value range of the selected parameters
is set in terms of alpha according to the FDM machine speci-
fications and other parameters are kept fixed. Central com-
posite design with five levels for each process parameter was
used to enhance the magnitude preciseness of FDM devise
parts. Each process parameter is defined like so:
Layer thickness (Fig. 2a) Layer thickness based on the
size of nozzle tip is the height of each layer deposited one
over another to fabricate the part.
Build orientation (Fig. 2b) It refers to the direction
in which the part is oriented on the machine bed with
respect to different axis.
Inﬁll density (Fig. 2c) It defines the inside amount of
material used in fabricating the part.
Number of contours (Fig. 2d) it refers to the number of
lines on the periphery.
2.3  Experimental design matrix
A set of mathematical and statistical technique which is
used for analysis and modeling of specific problem factors
is called response surface methodology (RSM). In RSM we
consider the effect of output variables on desired response by
employing linear or square polynomial function to achieve
the optimization. Five level central composite design was
used to study the effect of linear, quadratic, cubic and cross
product models of four process parameters and also used to
develop an experimental design matrix. In this work second
order quadratic model was used for each response value to
develop the mathematical model and to show the correlation
between input process parameters and magnitude precise-
ness by using Eq. (1) given below. A total number of 30
experiments with 6 replicate at the centre were conducted for
estimation of a pure error sum of square using DOE 6.0.8.
Predicted and observed response values of all the experi-
ments have been described in Table 2.
[Q = predicted response value, γ0 = regression equation con-
stant, γi = linear coefficient γii = square term of each param-
eter, γij = first order interaction effect].
2.4  RSM‑GA model for process parameter
optimization
The whole GA cycle which is an extremely well known tool
to tackle wide sorts of seeking, complex and optimization
(1)
Q = 훾0 +
∑
훾ipi +
∑
훾iip2
i +
∑
훾ijpipj
Fig. 1  CAD designed specimen
Table 1  A four process parameter for five level central composite
design
S. no. Process param-
eters
Notation Unit
(−alpha) (+alpha)
1
Layer thickness
A
mm
0.12
0.4
2
Build orientation
B
Degree
0
90
3
Infill density
C
Percentage 0
100
4
No. of contours
D
No.
2
10


---


## Page 4


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
problems [19–21] consist of four basic steps which were
repeated until the ideal desired target halted fluctuating. The
First step is randomly generate initial new population from
the random individual population. The second is to con-
sider these individuals for evaluation on the basis of objec-
tive function. Third is to select the best individual having
maximum fitness value for mutation and crossover because
that would have a greater probability of generating progeny.
Fourth step is the selection of new individual parent after
selection, mutation and crossover from the population. In
general the following steps were followed to create RSM-
GA model:
1. Randomly generation of the initial individual popula-
tion having length of each chromosome is equal to the
number of process parameters we consider.
2. The individual process parameter values have been gen-
erated within the consider range.
3. In GA, RSM generated equation is considered as fitness
function.
4. The GA, develops a series of novel population. At each
step, the GA uses the individuals to develop the next
novel population. The following steps were used to gen-
erate novel population by GA tool:
5
The Calculation is ended after meeting of best fitness
function and the chromosome based on the best value is
selected as the optimal process parameter for minimiz-
ing the magnitude variation.
2.5  Development of ANN model using experimental
data
The ANN technique is collected work of data which is
used for creating the network, configuring the network,
initializing the weights and biases, network training, vali-
dation of network and investigate the data. Artificial neural
network systems, being great calculations for information
investigation, have given wide chances to making utili-
zation of the information contained in mechanical data-
bases [22]. The sigmoid 10 hidden neurons with two level
feed-forward network fitted the multidimensional map-
ping problem as shown in Fig. 3. The ANN mechanism
to generate the best fit model has used inputs, outputs and
neurons three layer model. The input and output data were
investigated from the RSM design matrix. Every input has
four variables and six replications. The various process
parameters such as input, output, net and fitness obtained
from ANN model were used in GA to find out the optimum
process parameters.
Fig. 2  a Layer thickness. b
Build orientation. c Infill den-
sity (25% 50% 75%). d Number
of contours
(a) Layer thickness
(b) Build orientation
(c) Infill density (25% 50% 75%)
(d) Number of contours


---


## Page 5


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
Table 2  CCD matrix for FDM process parameters
Experi-
ment no.
Layer thick-
ness (mm)
Build orien-
tation (°)
Infill den-
sity (%)
Number of
contours
Percentage variation in length
Percentage variation in width
Percentage variation in thickness
Actual
Predicted
by RSM
Predicted by ANN
Actual
Predicted
by RSM
Predicted by ANN
Actual
Predicted
by RSM
Predicted
by ANN
1
0.19
22.5
25
4
0.5
0.48
0.8363
0.47
0.49
0.8791
2.4
2.38
2.4
2
0.4
45
50
6
1.3
1.25
1.3009
1.13
1.20
1.1264
1.5
1.50
1.5
3
0.26
45
50
10
1.6
1.52
1.5983
1.07
1.08
0.774
1.9
1.79
2.086
4
0.26
45
50
6
1
1.22
1.1809
0.80
0.76
0.7961
1.7
1.59
1.633
5
0.26
45
50
6
1.2
1.22
1.1809
0.67
0.76
0.7961
1.6
1.59
1.633
6
0.26
45
50
6
1.3
1.22
1.1809
0.67
0.76
0.7961
1.6
1.59
1.633
7
0.19
67.5
75
8
1.9
1.92
1.4439
0.27
0.34
0.3222
1
1.12
1.189
8
0.19
67.5
25
8
1.7
1.75
1.7903
0.07
0.06
0.0568
0.9
0.90
0.9
9
0.26
45
50
2
1.2
1.24
1.1308
0.80
0.79
0.6973
1.4
1.39
1.4
10
0.33
67.5
75
4
1.8
1.80
1.8002
0.73
0.73
1.2178
2
2.04
2
11
0.33
67.5
25
4
0.7
0.73
0.7003
0.47
0.48
0.0544
1.5
1.57
1.5
1
0.19
22.5
75
8
0.3
0.18
0.6001
1.00
0.95
1.0061
2.4
2.28
2.284
13
0.19
22.5
75
4
0.5
0.40
0.5027
1.07
1.07
1.0722
2
2.01
2
14
0.26
45
100
6
0.7
0.79
0.7012
0.67
0.74
1.1847
1.7
1.79
1.7
15
0.33
22.5
75
8
1.4
1.57
1.3987
1.93
1.88
1.9349
1.5
1.57
1.639
16
0.26
45
0
6
0.3
0.17
0.7222
0.13
0.06
0.1475
1.2
1.39
1.2
17
0.26
45
50
6
1.1
1.22
1.1809
0.67
0.76
0.7961
1.6
1.59
1.633
18
0.33
22.5
75
4
2.2
2.06
2.1993
1.33
1.31
1.4957
1.1
1.05
1.1
19
0.26
45
50
6
1.3
1.22
1.1809
0.87
0.76
0.7961
1.6
1.59
1.633
20
0.19
67.5
25
4
1
0.97
1.0513
0.27
0.35
0.3076
1.1
1.02
1.376
21
0.33
67.5
75
8
2
1.93
1.7577
1.07
1.01
1.0759
2.5
2.47
2.5
22
0.26
90
50
6
3.1
2.95
3.1035
0.87
0.82
0.8668
1.4
1.35
1.4
23
0.19
22.5
25
8
0.5
0.63
0.5004
0.47
0.51
0.4719
2.4
2.36
2.4
24
0.26
0
50
6
2
2.10
1.9998
1.80
1.84
1.8337
1.7
1.82
1.7
25
0.33
22.5
25
8
1.7
1.50
1.6998
1.60
1.61
1.6065
1.1
1.10
1.197
26
0.26
45
50
6
1.4
1.22
1.1809
0.87
0.76
0.7961
1.5
1.59
1.633
27
0.33
22.5
25
4
1.5
1.62
1.5820
0.93
0.89
0.4656
1
0.87
0.857
28
0.12
45
50
6
0.1
0.10
0.1159
0.20
0.13
0.2119
1.6
1.67
1.6
29
0.19
67.5
75
4
1.4
1.51
1.4156
0.80
0.76
0.7626
1
0.95
1.000
30
0.33
67.5
25
8
1
1.23
1.0011
0.87
0.89
0.8218
1.7
1.69
1.7


---


## Page 6


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
2.6  ANN‑GA model for process parameter
optimization of 3D printing
A MATLAB 16.0 based GA mechanism was used to opti-
mize the input process parameters for minimum percent-
age variation in magnitude by using the previous devel-
oped ANN model. ANN-GA model was developed similar
to RSM-GA as in previous Sect. 2.4. To start with the
GA, mat file developed in the ANN model was used as
a fitness function. Now, with various sets of ANN vari-
ables, generate an initial population randomly and calcu-
late fitness function of each chromosome of ANN. The
Chromosome is one string of the population, which is
further crossover and mutated to generate a new string of
chromosomes for each generation. This process of vari-
ous steps such as reproduction, crossover and mutation is
known as one generation. Each new string of the popula-
tion obtained after mutation is known as child strings,
which become the parent strings for the next generation.
This is continued until the mean fitness squared error of
the strings comes out to be minimum.
3  Results and discussion
In the present work focused is on enhancing magnitude
preciseness by optimizing process parameters using RSM-
GA and ANN-GA hybrid techniques. Table 2 represents
the design matrix which was built using central composite
design under a different set of process parameters includ-
ing experimental response results and predicted value of
different response values by RSM and ANN. Experimental
response values were analyzed by developing mathemati-
cal models using Design of Experiment 6.0.8 and Mat Lab
16.0 software. In present study quadratic and 2FI (two-factor
interaction) models were analyzed and selected according to
three different tests- the sequential model sum of squares,
lack-of-fit and the adequacy model. For percentage variation
in length and width quadratic model has the maximum value
of  R2, adjusted  R2 and predicted  R2 with very fine concord
with each other, but for percentage deviation in the thickness
2FI model has the maximum values for all these correlation
coefficient as represented in Table 3. So smaller p values
and insignificant lack-of-fit for quadratic and 2FI models in
comparison to other models gives an admirable clarification
among FDM process parameters and magnitude preciseness.
3.1  Effect of process parameters on percentage
variation in length
Effect of different FDM process parameters on percentage
variation in length is revealed in Fig. 4a–c. Figure 4a shows
the effect of number of contours and infill density that with
increment in both parameters percentage variation in length
is increasing. After reaching the maximum value again start
to decrease and it is minimum at 4 number of contours and
25% infill density. This is because at low infill density less
amount of material is used, so heat is easily transferred as
Fig. 3  Artificial neural network for FDM process parameter optimiza-
tion
Table 3  Figures summary of the models
Response
Model
Sequential p value Lack of fit-value R2
R2 adj
R2 pred
PRESS
Precision
Remarks
Percentage variation in length
Quadratic
< 0.0001
0.3977
0.968 0.9386
0.8547 1.8120 Sufficient
Suggested
2FI
0.1519
0.0024
0.555 0.3207
0.2393 9.4886 Insufficient
Cubic
0.3969
0.3537
0.987 0.9455
0.3429 8.1960 Insufficient Aliased
Linear
0.0539
0.0018
0.301 0.1895
− 0.087 13.5596 Insufficient
Percentage variation in width
Quadratic
< 0.0001
0.8166
0.983 0.9661
0.9358 0.3797 Sufficient
Suggested
2FI
0.099
0.019
0.817 0.7205
0.6985 1.7845 Insufficient
Cubic
0.6348
0.8095
0.991 0.9616
0.8796 0.7125 Insufficient Aliased
Linear
< 0.0001
0.0123
0.695 0.6456
0.5288 2.7892 Insufficient
Percentage variation in thickness Quadratic
0.3452
0.1434
0.978 0.9573
0.8878 0.6480 Insufficient
2FI
< 0.0001
0.1433
0.971 0.9554
0.9073 0.5352 Sufficient
Suggested
Cubic
0.1524
0.2327
0.994 0.9743
0.6002 2.3088 Insufficient Aliased
Linear
0.3892
0.0001
0.147 0.0104
− 0.331
7.6870 Insufficient


---


## Page 7


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
material cool downs from glass transition temperature to
machine cabin temperature without producing any ther-
mal stress. The minimum percentage variation in length at
a minimum number of contours and infill density is found
0.754167% by keeping other parameter constant as shown
in Fig. 4a. This variation in length can be further reduced to
by lessening the layer thickness. The effect of layer thick-
ness with infill density and number of contours is shown
in Fig. 4b, c which conclude that percentage variation in
length is minimum at lower values of layer thickness. This
Fig. 4  a Effect of infill density
and layer thickness on percent-
age variation in length. b Effect
of number of contours and
layer thickness on percentage
variation in length. c Effect of
number of contours and infill
density on percentage variation
in length
(a) Effect of Infill density & Layer thickness on percentage variation in Length
(b) Effect of Number of contours & Layer thickness on percentage variation in Length
(c) Effect of Number of contours & Infill density on percentage variation in Length


---


## Page 8


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
is due to generation of less amount of inner residual stress as
fabricated part cool down. The main reason of deformation
and distortion is growth of inner stress as layer thickness
increases. The strength of FDM parts also decreases with
increase in layer thickness [23]. So layer thickness should
keep minimum. The least percentage variation in length is
0.695833% at layer thickness of 0.19 mm and 4 number of
contours.
3.2  Effect of process parameters on percentage
variation in width
Figure 5a–d reveals the effect of different process parameters
on percentage variation in width. The effect of build orienta-
tion and layer thickness on percentage variation in width as
can be seen (Fig. 5a). The width is increasing linearly with
increase in layer thickness, but with the increase in build ori-
entation percentage variation in width is decreasing reaches
a minimum value and then again starts increasing. The mini-
mum percentage variation in width is 0.40% at  600 build ori-
entation and 0.19 mm layer thickness. The effect of number
of contours and layer thickness on percentage variation in
width is shown in Fig. 5b. The percentage variation in width
is decreasing linearly with increase in number of contours
but increasing with increase in layer thickness as can be
seen (Fig. 5b). The minimum percentage variation in width
is 0.41% at 8 number of contours and 0.19 mm layer thick-
ness. Figure 5c shows the effect of infill density and build
orientation on percentage variation in width. The minimum
percentage variation in width is 0.42% at 60° build orienta-
tion and 25% infill density. The percentage variation in width
is increasing with raising infill density value. The reason is
thermal expansion due to the large amount of material used
during fabricating part but, with the increase in build orien-
tation, first percentage variation in width is decreasing and
then becomes constant up to 67.50° build orientation value.
Similarly, least percentage variation in width 0.67% at 60°
build orientation and 4 number of contours can be obtained
as shown in Fig. 5d.
3.3  Effect of process parameters on percentage
variation in thickness
Figure 6a–d shows the effect of different process param-
eters on percentage variation in thickness. Figure 6a
reveals the influence of infill density and layer thick-
ness on percentage variation in thickness that thickness
is decreasing linearly with a rise in layer thickness value,
but with the rise in infill density value percentage varia-
tion in thickness is increasing. The minimum percentage
variation in thickness is 1.3075% at 25% infill density and
0.33 mm layer thickness. Similarly the effect of number
of contours and layer thickness on percentage variation in
thickness is shown in Fig. 6b. The minimum percentage
variation in thickness is 1.3825% at 4 number of contours
and 0.33 mm layer thickness. Figure 6c shows the effect
of infill density and build orientation on percentage vari-
ation in thickness. This figure indicates that the minimum
percentage variation in width is 1.29% at 67.500 build
orientation and 25% infill density. The percentage vari-
ation in thickness is increasing with a rise in infill den-
sity value, but with rise in build orientation percentage
variation in thickness is decreasing. Similarly, minimum
percentage variation in thickness 1.39% at 67.500 build
orientation and 4 number of contours can be obtained as
shown in Fig. 6d.
3.4  ANOVA models
In this study different process parameters selected for opti-
mization to enhance the magnitude preciseness were layer
thickness, Build orientation, Density and Number of con-
tours. The process parameters range as given in Table 1 was
selected on the basis of study literature and developed a
design matrix by using RSM based central composite design
(CCD) in the design of expert software 6.0.8. Responses in
terms of percentage variation in length, width and thick-
ness were measured by performing experiments according
to Table 2. For each response value mathematical models
are generated according to the second order equations (ii,
iii and iv) as given below:
(2)
Percentage variation in length
= (−3.05487 + 27.38520 ∗A −0.026865 ∗B
+ 0.014917 ∗C −0.021280 ∗D −27.42347 ∗A2
+ 6.48148E −004 ∗B2 −2.95000E −004 ∗C2
+ 0.010156 ∗D2 −0.21825 ∗A*B + 0.075000 ∗A*C
−0.49107 ∗A*D + 2.77778E −004 ∗B*C
+ 3.47222E −003 ∗B*D −1.87500E −003 ∗C*D)
(3)
Percentage variation in width
= (+0.35930 + 1.76304 ∗A −0.012328 ∗B
+ 0.034635 ∗C −0.31389 ∗D −4.53515 ∗A2
+ 2.85322E −004 ∗B2 −1.42222E −004 ∗C2
+ 0.011111 ∗D2 −0.042328 ∗A*B
−0.023810 ∗A*C + 1.25000 ∗A*D
−7.40741E −005 ∗B*C −1.66667E
−003 ∗B*D −6.66667E −004 ∗C*D)


---


## Page 9


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
Fig. 5  a Effect of build orienta-
tion and layer thickness on
percentage variation in width.
b Effect of number of contours
and layer thickness on percent-
age variation in width. c Effect
of infill density and build orien-
tation on percentage variation
in width. d Effect of number of
contours and build orientation
on percentage variation in width
(a) Effect of Build orientation & Layer thickness on percentage variation in width
 (b) Effect of Number of contours & Layer thickness on percentage variation in width
(c) Effect of Infill density & Build orientation on percentage variation in width
(d) Effect of Number of contours & Build orientation on percentage variation in width


---


## Page 10


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
Fig. 6  a Effect of infill density
and layer thickness on percent-
age variation in thickness. b
Effect of number of contours
and layer thickness on percent-
age variation in thickness. c
Effect of infill density and build
orientation on percentage vari-
ation in thickness. d Effect of
number of contours and build
orientation on percentage varia-
tion in thickness
(a) Effect of Infill density& Layer thicknesson percentage variation in thickness
(b) Effect of Number of contours & Layer thickness on percentage variation in thickness
(c) Effect of Infill density & Build orientation on percentage variation in thickness
(d) Effect of Number of contours &Build orientation on percentage variation in thickness


---


## Page 11


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
Table 4  ANOVA result for
percentage variation in length
Source
Sum of Squares
DF
Mean square
F value
Prob > F (p value) Remarks
Model
12.07783
14
0.862702
32.69188
< 0.0001
Significant
 A
1.98375
1
1.98375
75.17368
< 0.0001
 B
1.08375
1
1.08375
41.06842
< 0.0001
 C
0.570417
1
0.570417
21.61579
0.0003
 D
0.120417
1
0.120417
4.563158
0.0496
 A2
0.495268
1
0.495268
18.76805
0.0006
 B2
2.953125
1
2.953125
111.9079
< 0.0001
 C2
0.932411
1
0.932411
35.33346
< 0.0001
 D2
0.045268
1
0.045268
1.715414
0.21
 AB
1.890625
1
1.890625
71.64474
< 0.0001
 AC
0.275625
1
0.275625
10.44474
0.0056
 AD
0.075625
1
0.075625
2.865789
0.1111
 BC
0.390625
1
0.390625
14.80263
0.0016
 BD
0.390625
1
0.390625
14.80263
0.0016
 CD
0.140625
1
0.140625
5.328947
0.0356
 Residual
0.395833
15
0.026389
 Lack of fit
0.2875
10
0.02875
1.326923
0.3977
Not significant
 Pure error
0.108333
5
0.021667
Cor total
12.47367
29
SD
0.162447
R-Squared
0.968266481
Mean
1.256667
Adj R-Squared
0.938648531
C.V.
12.92678
Pred R-Squared
0.854733973
PRESS
1.812
Adeq Precision
24.81128775
Table 5  ANOVA result for
percentage variation in width
Source
Sum of Squares
DF
Mean square
F value
Prob > F (p value) Remarks
Model
5.815704
14
0.415407
60.08571
< 0.0001
Significant
 A
1.706667
1
1.706667
246.8571
< 0.0001
 B
1.567407
1
1.567407
226.7143
< 0.0001
 C
0.711852
1
0.711852
102.9643
< 0.0001
 D
0.125185
1
0.125185
18.10714
0.0007
 A2
0.013545
1
0.013545
1.959184
0.1819
 B2
0.572275
1
0.572275
82.77551
< 0.0001
 C2
0.21672
1
0.21672
31.34694
< 0.0001
 D2
0.05418
1
0.05418
7.836735
0.0135
 AB
0.071111
1
0.071111
10.28571
0.0059
 AC
0.027778
1
0.027778
4.017857
0.0634
 AD
0.49
1
0.49
70.875
< 0.0001
 BC
0.027778
1
0.027778
4.017857
0.0634
 BD
0.09
1
0.09
13.01786
0.0026
 CD
0.017778
1
0.017778
2.571429
0.1297
 Residual
0.103704
15
0.006914
 Lack of fit
0.053333
10
0.005333
0.529412
0.8166
Not significant
 Pure error
0.05037
5
0.010074
 Cor total
5.919407
29
SD
0.083148
R-Squared
0.982480729
Mean
0.817778
Adj R-Squared
0.966129409
C.V.
10.16755
Pred R-Squared
0.935849434
PRESS
0.379733
Adeq Precision
31.08757791


---


## Page 12


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
The percentage variation in length, width and thick-
ness actual measured were in the range of (0.1–3.1%,
0.07–1.93%, 0.9–2.5%). The model fitness is quadratic for
length and width, but 2FI for thickness, which find that
there is only one arrangement for each dimension where
various process parameters show minimum magnitude vari-
ation from the actual one. Then from the F and p test values
which were checked for each model terms in Eqs. (2), (3)
and (4), it was decided that the model was significant or not
significant as described in Tables 4, 5 and 6. The response is
affected more as compared to other terms in quadratic equa-
tion if the coefficient of the terms in the developed equation
is significant. Different significant model terms obtained for
each response are shown in Tables 4, 5 and 6. The model F
(32.69) and p (< 0.0001) values for percentage variation in
length, F (60.08571) and p (< 0.0001) values for percentage
variation in width and F (63.08638) and p (< 0.0001) values
for percentage variation in thickness showed that the models
were significant.
Point prediction optimization method was used in this
work to find out optimum process parameters at minimum
(4)
Percentage variation in thickness
= (+7.59976 −21.84524 ∗A −0.093122 ∗B
−0.031429 ∗C −0.11607 ∗D + 0.32540 ∗A*B
+ 0.078571 ∗A*C + 0.44643 ∗A*D + 1.33333E
−004 ∗B*C −5.55556E −004 ∗B*D
+ 1.50000E −003 ∗C*D)
percentage variation in part dimension and to confirm the
validity of the model. It was found that at the 0.19 mm layer
thickness, 40.74° build orientation, 25% infill density and
4 number of contours the minimum percentage variation
in length is 0.360421%, minimum percentage variation in
width is 0.30% and the minimum percentage variation in
thickness is 1.83182%. To validate the RSM model a mini-
mum three parts are fabricated at the above obtained opti-
mum process parameters. The minimum percentage varia-
tion in length = 0.3524%, minimum percentage variation in
width = 0.345% and minimum percentage variation in thick-
ness = 1.78312% were found close to the above predicted
values. Thus, from experimental results confirm that the
model is very adequate and reliable for this problem. Fur-
ther optimization of the FDM process parameters to enhance
magnitude preciseness is necessary as the above discussed
models output is not much significant as our objective and
also developed mathematical equations can not find out
the accurate results [7]. So further hybrid techniques were
applied to optimize the FDM process parameters.
3.5  Parameter optimization by RSM‑GA
In GA epochs is a measure which shows the performance
and the number of cycles that processed by the genetic algo-
rithm for various numbers of generations. It was performed
for experiments using 50 generations and 200 population
size to find out the number of souls. Constraint dependent
crossovers were used up as a crossover function and adap-
tive feasible mutation was taken as mutation function. The
Table 6  ANOVA result
for percentage variation in
thickness
Source
Sum of Squares
DF
Mean square
F value
Prob > F (p value)
Remarks
Model
5.605833
10
0.560583
63.08638
< 0.0001
Significant
 A
0.041667
1
0.041667
4.689042
0.0433
 B
0.326667
1
0.326667
36.76209
< 0.0001
 C
0.24
1
0.24
27.00888
< 0.0001
 D
0.24
1
0.24
27.00888
< 0.0001
 AB
4.2025
1
4.2025
472.9368
< 0.0001
 AC
0.3025
1
0.3025
34.04245
< 0.0001
 AD
0.0625
1
0.0625
7.033564
0.0157
 BC
0.09
1
0.09
10.12833
0.0049
 BD
0.01
1
0.01
1.12537
0.3021
 CD
0.09
1
0.09
10.12833
0.0049
 Residual
0.168833
19
0.008886
 Lack of fit
0.148833
14
0.010631
2.657738
0.1433
Not significant
 Pure error
0.02
5
0.004
 Cor total
5.774667
29
SD
0.094265
R-Squared
0.970763
Mean
1.586667
Adj R-Squared
0.955375
C.V.
5.941096
Pred R-Squared
0.907324
PRESS
0.535175
Adeq precision
27.88458


---


## Page 13


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
Fig. 7  RSM-GA plot for per-
centage variation in length
Fig. 8  RSM-GA plot for per-
centage variation in width
Fig. 9  RSM-GA plot for per-
centage variation in thickness


---


## Page 14


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
crossover fraction was chosen as 0.8 and elite count was
taken as 0.05 of population sizes. The hybrid RSM-GA has
been run to get optimum process parameters for least per-
centage variation in different magnitudes in MATLAB by
fixing upper and lower bound parameter limits as found out
from the design matrix of RSM.
The minimum percentage variation in length obtained
with RSM-GA is 0.17919% at process parameters (layer
thickness 0.19 mm, build orientation 22.50°, infill den-
sity 75% and number of contours 8) and its convergence as
shown in Fig. 7; the minimum percentage variation in width
is 0.05342% at process parameters value (layer thickness
0.19 mm, build orientation 62.301°, infill density 25.002%,
and number of contours 8) and its convergence as shown
in Fig. 8; the minimum percentage variation in thickness
is 0.87418% at process parameters value (layer thickness
0.33 mm, build orientation 22.5°, infill density 25%, and
number of contours 4) and its convergence as shown in
Fig. 9.
3.6  Validation of RSM‑GA
The optimum process parameter combination sets obtained
from the RSM-GA developed models were used to validate
the model. A minimum of three parts were fabricated by
selecting the optimum process parameters combination
set for each magnitude from Table 7 to confirm the ade-
quacy of predicted models. An observed average minimum
0.18076% variation in length, 0.05741% variation in width
and 0.88906% variation in thickness process parameters
were near to the predicted value of 0.179192% variation in
length, 0.05342% variation in width and 0.87418% variation
in thickness and hence confirms the adequacy of developed
RSM-GA model.
3.7  Fitness function development and training
using ANN
The ANN generated model has been trained with 30 sets
of input process parameters (A, B, C, D) and an output
response (variation in length, width and thickness). The
input [4 × 30] and output [1 × 30] were sacrificed to the neu-
ral fitting tool as an input and output data set. In this study
30 samples were divided randomly among three varieties
of samples viz. testing (15%), validation (15%) and training
(70%) for training purpose. Ten numbers of hidden neurons
were taken in the fitting network’s hidden layer to define a
fitting neural network. Chronological arranged incremen-
tal training with learning functions (trains) were utilized to
perform training. Testing offers an independent standard
Table 7  Validation of RSM-GA results
Sr. no
A
B
C
D
Percentage varia-
tion in magnitude
For percentage variation in length
 1
0.19
22.5
75
8
0.17983
 2
0.19
22.514
74.999
7.999
0.17994
 3
0.19
22.506
75
7.997
0.182514
For percentage variation in width
 1
0.19
62.301
25.002
8
0.05243
 2
0.191
62.435
25
8
0.06258
 3
0.191
62.39
25.001
7.999
0.05721
For percentage variation in thickness
 1
0.33
22.5
25
4
0.88215
 2
0.191
67.5
25.005
8
0.89781
 3
0.191
67.498
25.003
7.999
0.88721
Table 8  Result obtained from
different training functions
R2
Trainlm
Trainoss
Traincgp
Trainscg
Traincgb
Trainrp
Traingdx
Trainb
Training function applied in the fitness function of ANN1
Training
0.99607
0.8841
0.99842
0.98427
0.99557
0.99147
0.97063
80,444
Validation
0.86814
0.60643
0.90706
0.98044
0.88022
0.90007
0.58062
− 0.09356
Test
0.98093
0.8682
0.55654
0.81997
0.73328
0.61286
− 0.59326
0.84991
Overall
0.97006
0.81289
0.93978
0.94986
0.96753
0.94915
0.85722
0.53629
Training function applied in the fitness function of ANN2
Training
1
0.86399
0.98761
0.98543
0.94745
0.96998
0.95929
0.77586
Validation
0.78238
0.97379
0.95627
0.97827
0.94739
0.99351
0.85689
0.17088
Test
0.75499
0.73114
0.98889
0.86137
0.98214
0.95676
0.8701
0.63273
Overall
0.98144
0.83984
0.96918
0.96173
0.9441
0.97326
0.93776
0.70189
Training function applied in the fitness function of ANN3
Training
0.99912
0.72656
0.99752
0.91246
0.9803
0.98826
0.80575
0.1652
Validation
0.9686
0.49512
0.92089
0.986
0.82806
0.71555
0.74699
0.99211
Test
0.97202
0.82114
0.83156
0.91142
0.95202
0.94004
0.78036
0.25293
Overall
0.98145
0.74747
0.94378
0.91528
0.9505
0.90435
0.80298
0.45482


---


## Page 15


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
of network execution and bears no impact on training. The
network was trained multiple times as it generates different
results owing to initial conditions and sampling. In this way
different values of correlation coefficient (R) were obtained
for each run of training algorithm. By varying the number of
hidden layers/neurons value of R can be varied for training,
validation and testing for different types of algorithms. The
value of R decides the relationship, whether it is close or
random, 0 specify random relationship and 1 specify close
relationship. For the best value of correlation coefficient,
Fig. 10  a Neural network parameters for percentage change in length. b Neural network parameters for percentage change in width. c Neural net-
work parameters for percentage change in thickness


---


## Page 16


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
an ANN model has been created in a .mat format by using
MATLAB software as shown in Table 8.
The best correlation coefficients were obtained by trainlm
among different training functions for individual percent-
age variation in magnitude. The different neural network
parameters obtained using ANN as shown in Fig. 10a-c are
as follows.
For percentage variation in length an overall correla-
tion coefficient of 0.97006, training correlation coeffi-
cient 0.99607, validation correlation coefficient 0.86814
and testing correlation coefficient 0.98093., for percent-
age variation in width an overall correlation coefficient
of 0.98144, training correlation coefficient 1.000, valida-
tion correlation coefficient 0.78238 and testing correla-
tion coefficient 0.75499. and for percentage variation in
thickness an overall correlation coefficient of 0.98145,
training correlation coefficient 0.99912, validation corre-
lation coefficient 0.9686 and testing correlation coefficient
0.97202.
3.8  Process parameters optimization by ANN‑GA
An optimization tool of genetic algorithm was used to
predict the optimum combinations of process parameters
to minimize the variation in magnitudes. The ANN model
(.mat file) produced in the previous part utilized with regard
to target work. Bring down furthermore upper limits and
lower limits about process parameters need be fed under
GA. The fused ANN-GA has been run to get optimum pro-
cess parameters for least percentage variation in different
magnitudes in MATLAB by fixing upper and lower bound
parameter limits as found out from the design matrix of
RSM. Parameters population size = 200, generation = 50,
elite count = 0.05 of population size, crossover fraction = 0.8,
constraint dependent crossover function and adaptive feasi-
ble mutation function were used for hybrid ANN-GA.
The minimum percentage variation in length obtained
with ANN-GA is 0.06409% at process parameters (layer
thickness 0.19 mm, build orientation 40.382°, infill density
Fig. 11  ANN-GA plot for per-
centage variation in length
Fig. 12  ANN-GA plot for per-
centage variation in width


---


## Page 17


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
25% and number of contours 6.013) and its convergence
is shown in Fig. 11; the minimum percentage variation in
width is 0.03956% at process parameters value (layer thick-
ness 0.19 mm, build orientation 56.144°, infill density 25%,
and number of contours 8) and its convergence is shown
in Fig. 12; the minimum percentage variation in thickness
is 0.85689% at process parameters value (layer thickness
0.33 mm, build orientation 22.50, infill density 25%, and
number of contours 4) and its convergence is shown in
Fig. 13.
3.9  Validation of ANN‑GA model
The optimum process parameter combination sets obtained
from the ANN-GA developed models were used to validate
the models. A minimum of three parts were fabricated by
selecting the optimum process parameters combination set
for each magnitude from Table 9 to confirm the predicted
models. An observed average minimum 0.06445% variation
in length, 0.03908% variation in width and 0.85337% vari-
ation in thickness process parameters were near to the pre-
dicted value of 0.0640932% variation in length, 0.03961%
variation in width and 0.856886% variation in thickness and
hence confirms the adequacy of developed ANN-GA model.
4  Conclusions
RSM and various hybrid statistical tools such as RSM-GA
and ANN-GA is used for process parameter optimization
to enhance the magnitude preciseness of FDM fabricated
parts. ANN-GA produced better proposed model by using
back-propagation neural network with four inputs, ten hid-
den, multilayer feed-forward and one output layer as showed
by high correlation coefficients R (0.97006, 0.98144,
0.98145) for minimum percentage variation in length,
width and thickness as compared to R (0.96826, 0.98248,
0.970763) obtained from RSM. The minimum percent-
age variation in length = 0.06409% at process parameters
(layer thickness = 0.19 mm, build orientation = 40.382°,
infill density = 25% and number of contours = 6.013), the
minimum percentage variation in width = 0.03961% at pro-
cess parameters value (layer thickness = 0.19 mm, build
orientation = 56.144°, infill density = 25.008%, and number
of contours = 8) and the minimum percentage variation in
thickness = 0.85689% at process parameters value (layer
thickness = 0.33 mm, build orientation = 22.5°, infill den-
sity = 25%, and number of contours = 4) are best predicted
results value by using ANN-GA in comparison to RSM,
RSM-GA predicted results value. The proposed tools as a
computational device used intelligently to help the design-
ing examination through deciding the optimum process
parameters selection for increasing dimensional precise-
ness. Additionally, it very well may be connected to a high
Fig. 13  GA ANN plot for per-
centage variation in thickness
Table 9  Validation of ANN-GA results
Sr. no
A
B
C
D
Percentage varia-
tion in magnitude
For percentage variation in length
 1
0.19
40.382
25
6.013
0.0620932
 2
0.19
40.381
25.001
6.014
0.0620932
 3
0.191
40.409
25.002
6.015
0.0661766
For percentage variation in width
 1
0.19
56.144
25.008
8
0.03802
 2
0.19
56.134
25
8
0.04082
 3
0.19
56.097
25.012
7.999
0.03839
For percentage variation in thickness
 1
0.33
22.5
25
4
0.85031
 2
0.33
22.506
25.015
4.005
0.84286
 3
0.33
22.503
25.002
4.001
0.86786


---


## Page 18


International Journal on Interactive Design and Manufacturing (IJIDeM)
1 3
scope of relevance, similarity inside the AM frameworks
and simplicity in usage.
References
 1. Yan, X., Gu, P.: A review of rapid prototyping technologies and
systems. Comput. Aided Des. 4, 307–316 (1996)
 2. Lee, B.H., Abdullah, J., Khan, Z.A.: Optimization of rapid proto-
typing parameters for production of flexible ABS object. J. Mater.
Process. Technol. 169, 54–61 (2005)
 3. Mohamed, O.A., Masood, S.H., Bhowmik, J.L.: Experimental
investigation of time dependent mechanical properties of PC-ABS
prototypes processed by FDM additive manufacturing process.
Mater. Lett. 193, 58–62 (2017)
 4. Khodaygan, S., Golmohammadi, A.H.: Multi-criteria optimiza-
tion of the part build orientation (PBO) through a combinedmeta-
modeling/NSGAII/TOPSISmethod for additive manufacturing
processes. Int. J. Interact. Des. Manuf. 12, 1071–1085 (2017)
 5. Rayegani, F., Onwubolu, G.: Fused deposition modelling (FDM)
process parameter prediction and optimization using group
method for data handling (GMDH) and differential evolution
(DE). Int. J. Adv. Manuf. Technol. 73, 509–519 (2014)
 6. Nidagundi, V.B., Keshavamurthy, R., Prakash, C.P.S.: Studies on
parametric optimization for fused deposition modelling. Process.
Materi. Today Proc. 2, 1691–1699 (2015)
 7. Alafaghani, A., Qattawi A., Alrawi B., Guzman, A.: Experimental
optimization of fused deposition modelling processing param-
eters: a design-for-manufacturing approach. In: North American
Manufacturing Research Conference, LA, USA, vol. 10, pp. 791–
803 (2017)
 8. Mohamed, O.A., Masood, S.H., Bhowmik, J.L.: Mathemati-
cal modeling and FDM process parameters optimization using
response surface methodology based on Q-optimal design. Appl.
Math. Model. 40, 10052–10073 (2016)
 9. Sood, A.K., Ohdar, R.K., Mahapatra, S.S.: Improving magnitude
preciseness of fused deposition modelling processed part using
grey Taguchi method. Mater. Des. 30, 4243–4252 (2009)
 10. Lieneke, T., Denzer, V., Adam, G.A.O., Zimmer, D.: Magnitude
tolerances for additive manufacturing: experimental investigation
for fused deposition modeling. Procedia CIRP 43, 286–291 (2016)
 11. Sahu, R.K., Mahapatra, S.S., Sood, A.K.: A study on magnitude
preciseness of fused deposition modeling (FDM) processed parts
using fuzzy logic. J. Manuf. Sci. Prod. 13(3), 183–197 (2013)
 12. Equbal, A., Sood, A.K., Ohdar, R.K., Mahapatra, S.S.: Prediction
of magnitude preciseness in fused deposition modelling: a fuzzy
logic approach. Int. J. Product. Qual. Manag. 7, 22–43 (2011)
 13. Chou, K., Zhang, Y.: A parametric study of part distortion in fused
deposition modeling using three magnitude element analysis. J.
Eng. Manuf. 222(B), 959–967 (2008)
 14. Mohamed, O.A., Masood, S.H., Bhowmik, J.L.: Optimization of
fused deposition modeling process parameters: a review of current
research and future prospects. Adv. Manuf. 3, 42–53 (2015)
 15. Wang, C.C., Lin, T., Hu, S.: Optimizing the rapid prototyping pro-
cess by integrating the Taguchi method with the Gray relational
analysis. Rapid Prototyp. J. 13, 304–315 (2007)
 16. Kim, G.D., Oh, Y.T.: A benchmark study on rapid prototyping
processes and machines: quantitative comparisons of mechanical
properties, accuracy, roughness, speed, and material cost. Proc.
Inst. Mech. Eng. Part B J. Eng. Manuf. 2, 201–215 (2008)
 17. Ordaz-Hernandez, K., Fischer, X., Bennis, F.: Granular modeling
for virtual prototyping in interactive design. Virtual Phys. Proto-
typ. 2(2), 111–126 (2007)
 18. Nadeau, J.P., Fischer, X.: Research in interactive design: virtual,
interactive and integrated product design and manufacturing for
industrial innovation. Springer, Berlin (2011)
 19. Davorin, Kramar, Djordje, Cica, Branislav, Sredanovic, Janez,
Kopa: Design of fuzzy expert system for predicting of surface
roughness in high-pressure jet assisted turning using bioinspired
algorithms. Artif. Intell. Eng. Des. Anal. Manuf. 30, 96–106
(2016)
 20. Singh, P.K., Jain, S.C., Jain, P.K.: Comparative study of genetic
algorithm and simulated annealing for optimal tolerance design
formulated with discrete and continuous variables. Proc. Inst.
Mech. Eng. Part B J. Eng. Manuf. 10, 735–758 (2005)
 21. Singh, P.K., Jain, S.C., Jain, P.K.: A genetic algorithm based solu-
tion to optimum tolerance synthesis of mechanical assemblies
with alternate manufacturing processes—benchmarking with the
exhaustive search method using the Lagrange multiplier. Proc.
Inst. Mech. Eng. Part B J. Eng. Manuf. 7, 765–778 (2004)
 22. Rojek, I.: Technological process planning by the use of neural
networks. Artif. Intell. Eng. Des. Anal. Manuf. 31, 1–15 (2017)
 23. Christiyan, K.G.J., Chandrasekhar, U., Venkateswarlu, K.: A
study on the influence of process parameters on the mechanical
properties of 3D printed ABS composite. IOP Conf. Ser. Mater.
Sci. Eng. 114, 012109 (2016). https ://doi.org/10.1088/1757-
899X/114/1/01210 9
Publisher’s Note Nature remains neutral with regard to jurisdictional
claims in published maps and institutional affiliations.


---
