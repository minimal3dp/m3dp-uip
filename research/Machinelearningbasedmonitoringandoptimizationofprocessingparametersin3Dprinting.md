# Machinelearningbasedmonitoringandoptimizationofprocessingparametersin3Dprinting

> **Source:** `Machinelearningbasedmonitoringandoptimizationofprocessingparametersin3Dprinting.pdf`
> **Converted:** 2025-11-22 21:18:08
> **Method:** PyMuPDF

---

## Page 1


See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/364328728
Machine-Learning-based Monitoring and Optimization of Processing
Parameters in 3D Printing
Article  in  International Journal of Computer Integrated Manufacturing · December 2022
DOI: 10.1080/0951192X.2022.2145019
CITATIONS
84
READS
1,816
7 authors, including:
Tariku Sinshaw Tamir
King Fahd University of Petroleum and Minerals
46 PUBLICATIONS   643 CITATIONS   
SEE PROFILE
Gang Xiong
Institute of Automation, Chinese Academy of Sciences
593 PUBLICATIONS   7,888 CITATIONS   
SEE PROFILE
Qihang Fang
Institute of Automation, Chinese Academy of Sciences
31 PUBLICATIONS   479 CITATIONS   
SEE PROFILE
Yong Yang
Chinese Academy of Sciences
202 PUBLICATIONS   7,301 CITATIONS   
SEE PROFILE
All content following this page was uploaded by Tariku Sinshaw Tamir on 30 August 2023.
The user has requested enhancement of the downloaded file.


---


## Page 2


Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tcim20
International Journal of Computer Integrated
Manufacturing
ISSN: (Print) (Online) Journal homepage: https://www.tandfonline.com/loi/tcim20
Machine-learning-based monitoring and
optimization of processing parameters in 3D
printing
Tariku Sinshaw Tamir, Gang Xiong, Qihang Fang, Yong Yang, Zhen Shen,
MengChu Zhou & Jingchao Jiang
To cite this article: Tariku Sinshaw Tamir, Gang Xiong, Qihang Fang, Yong Yang, Zhen Shen,
MengChu Zhou & Jingchao Jiang (2023) Machine-learning-based monitoring and optimization
of processing parameters in 3D printing, International Journal of Computer Integrated
Manufacturing, 36:9, 1362-1378, DOI: 10.1080/0951192X.2022.2145019
To link to this article:  https://doi.org/10.1080/0951192X.2022.2145019
Published online: 17 Nov 2022.
Submit your article to this journal
Article views: 560
View related articles
View Crossmark data
Citing articles: 3 View citing articles


---


## Page 3


Machine-learning-based monitoring and optimization of processing parameters
in 3D printing
Tariku Sinshaw Tamir
a,b, Gang Xiong
a,c, Qihang Fanga,b, Yong Yangd, Zhen Shen
a,c, MengChu Zhou
e,f
and Jingchao Jiang
g
aThe State Key Laboratory for Management and Control of Complex Systems, Beijing Engineering Research Center of Intelligent Systems and
Technology, Institute of Automation, Chinese Academy of Sciences, Beijing, China; bThe School of Artificial Intelligence, University of Chinese
Academy of Sciences, Beijing, China; cThe Guangdong Engineering Research Center of 3D Printing and Intelligent Manufacturing, Cloud
Computing Center, Chinese Academy of Sciences, Dongguan, China; dThe State Key Laboratory of High Performance Ceramics and Superfine
Microstructure, Shanghai Institute of Ceramics, Chinese Academy of Sciences, Shanghai, China; eHelen and John C. Hartmann Department of
Electrical and Computer Engineering, New Jersey Institute of Technology, Newark, NJ, USA; fMacao Institute of Systems Engineering and
Collaborative Laboratory for Intelligent Science and Systems, Macau University of Science and Technology, Macao 999078, China;
gDepartment of Mechanical and Automation Engineering, The Chinese University of Hong Kong, Shatin, Hong Kong
ABSTRACT
Additive manufacturing (AM), commonly known as 3D printing, is a rapidly growing technology.
Guaranteeing the quality and mechanical strength of printed parts is an active research area. Most
of the existing methods adopt open-loop-like Machine Learning (ML) algorithms that can be used
only for predicting properties of printed parts without any quality assuring mechanism. Some
closed-loop approaches, on the other hand, consider a single adjustable processing parameter to
monitor the properties of a printed part. This work proposes both open-loop and closed-loop ML
models and integrates them to monitor the effects of processing parameters on the quality of
printed parts. By using experimental 3D printing data, an open-loop classification model formu­
lates the relationship between processing parameters and printed part properties. Then, a closed-
loop control algorithm that combines open-loop ML models and a fuzzy inference system is
constructed to generate optimized processing parameters for better printed part properties. The
proposed system realizes the application of a closed-loop control system to AM.
ARTICLE HISTORY
Received 7 November 2021
Accepted 14 October 2022
KEYWORDS
Additive manufacturing;
closed-loop; 3D printing;
digital manufacturing;
machine learning;
processing parameters
1. Introduction
Generally, manufacturing is defined as an industrial
production system through which raw material is chan­
ged into completed items to be sold in a market. The
strategies for manufacturing can follow forming, cast­
ing, subtracting and additive processes (Esmaeilian,
Behdad, and Wang 2016). Forming applies force to
bring deformations on raw material such that the
required shapes and sizes can be acquired while cast­
ing involves pouring liquid material into a mold (shap­
ing device) and solidify it to make an object.
Subtracting, on the other hand, makes an object by
cutting or removing material away from a solid block of
materials. Different from all of them, additive manufac­
turing (AM) makes an object by joining materials using
a layer-upon-layer deposition approach.
AM (3D printing), as a supporting technology in
social manufacturing and cloud manufacturing (Xiong
et al. 2022), at its infancy was developed in the name of
rapid prototyping. Initially, it is used to define architec­
tural or anatomical production models (Camacho et al.
2018; Ngo et al. 2018). Next, the technology moves to
rapid tooling allowing the fabrication of tools directly
or indirectly such as injection molding, blow molding,
and thermoforming applications and also for fabrica­
tion of electrical discharge machining electrodes
(Uhlmann et al. 2018). Finally, the concept of AM
moves to rapid manufacturing that can produce and
realize fully functional products (Bikas, Stavropoulos,
and Chryssolouris 2016).
In the era of AM, various types of AM technologies
have been discovered and discussed, including fused
deposition modeling, laser engineered net shaping,
stereolithography, direct metal deposition, electron
beam melting, selective laser melting, selective laser
sintering, and wire and arc additive manufacturing
(WAAM) (Zhao et al. 2018; Zhang et al. 2020). Those
AM technologies require basic tasks including
CONTACT Zhen Shen
zhen.shen@ia.ac.cn
Institute of Automation, Chinese Academy of Sciences, No. 95 Zhongguancun E. Road, Beijing 100190, China
INTERNATIONAL JOURNAL OF COMPUTER INTEGRATED MANUFACTURING
2023, VOL. 36, NO. 9, 1362–1378
https://doi.org/10.1080/0951192X.2022.2145019
© 2022 Informa UK Limited, trading as Taylor & Francis Group


---


## Page 4


computer aided design (CAD) modeling, slicing, tool­
path generation, part building, and post-processing.
The quality of a 3D printed part is affected by each
stage. Firstly, at the so-called slicing stage, the CAD
model of an object is converted into a series of layers
depending on the type of slicing strategies used. The
most common and widely used slicing technique is
planar slicing which slices the model into parallel
layers. Subsequently, a toolpath is generated, which
guides the motion of the print head in a printing pro­
cess. Finally, the printed object is further enhanced by
processes involving removal of support structures.
Optimizing and monitoring processing parameters is
a tough and one key task in a 3D printing process since
they determine the quality and mechanical strength of
printed parts (Fang et al. 2023). Scientists and engineers
are interested in constructing the direct linkage between
process-structure and property-performance (P-S-P-P)
(Popova et al. 2017; Wang et al. 2018a). However, due
to the high nonlinearity of this linkage it is difficult to
formulate an underlying mathematical expression for it.
Therefore, taking the advantage of its intrinsic nonlinear
behaviors, machine learning (ML) (Ghahramani et al.
2020; Ieracitano et al. 2020; Meng et al. 2020; Goh, Sing,
and Yeong 2020) becomes an ideal solution to formulate
these mathematical relationships in an entire AM
process.
Most of the existing approaches dedicated to guar­
antee the quality and mechanical strength of printed
parts generally depend on the prediction results that
are normally obtained via open-loop-like ML algo­
rithms. In such cases, only part properties are pre­
dicted without any correction mechanism in the
presence of any printed part abnormalities. As
a result, a part building process is not always going
as planned and there may be inaccuracies such as
geometric deviation, surface roughness, porosity,
and poor interconnection between layers. Very few
closed-loop-based ML models (Wang et al. 2018b), on
the other hand, consider no more than one adjustable
processing parameter to maintain the desired printed
part properties. Therefore, a more reliable control
design strategy that considers many adjustable pro­
cessing parameters needs to be proposed. To create
a complete full-scale AM system, it is necessary to
design feedback control algorithms such that the
system can compensate for the corresponding inac­
curacies in a part building process. Maintaining the
shape and size of a designed 3D object needs an
intelligent feedback control loop; while online system
parameter measurements are needed to ensure the
current state of a printing process. Consequently, the
control system can adjust processing parameters. In
this study, both open-loop and closed-loop ML mod­
els are developed. The former is used to generate the
relationship between processing parameters and
printed part properties, which is useful to construct
a closed-loop fuzzy inference system. Then a fuzzy-
based feedback control system is used to optimize
processing parameters.
Fuzzy logic was first coined by Lotfi A. Zadeh in 1965
(Zadeh 1965). Since then it has been used to model
uncertain, linguistic and imprecise data (Liu et al. 2020;
Wang et al. 2021). With its great interpretation capabil­
ity, a fuzzy inference engine is being used as typical
control techniques for non-linear systems (Di et al.
2001). Unlike the conventional ones (Tamir et al.
2020b,c), whose performance depends on the model­
ing accuracy of a physical system, a fuzzy control sys­
tem is used when an analytical model is difficult to
obtain while expert experience is available. Thus, it is
wise to extend the controlling capability of a fuzzy
system in manufacturing industry where experts’
knowledge about a process is present while an analy­
tical model is missing. Heidarzadeh et al. (2020) use
fuzzy logic control to optimize the friction stir welding
of pure copper. Li et al. (2021) prove the effectiveness
of a fuzzy inference system for adjusting deposition
parameters of beads in WAAM.
The remainder of the paper elucidates the state of
the art for the applications of ML in AM industry, and
design and implementation of control methods.
Section 2 presents the researchers’ perspectives on
methods and approaches that are used to monitor
the quality and mechanical strength of printed parts.
As the core of this research work, Section 3 introduces
the methods for machine learning and collection of
datasets in the domain of AM. Section 4 presents
feedback control algorithm implementation along
with the mathematical expression of a 3D printer.
Section 5 gives the results and discussions, followed
by conclusions and perspectives in Section 6.
2. Related work
To assure the surface quality and mechanical strength
of printed parts, various methods are reported in the
literature. In the following paragraphs, we give their
INTERNATIONAL JOURNAL OF COMPUTER INTEGRATED MANUFACTURING
1363


---


## Page 5


detailed review and elaborate how ML methods are
involved to make improvement. The methods mainly
focus on three ways to ensure the quality and
mechanical strength of printed parts.
The first way is incorporating different pre-printing
design techniques, such as an open-loop-based path
design and support structure generation. Typical
research in improving the mechanical strength of AM
parts is reviewed as follows. Sugiyama et al. (2018)
propose a method for manufacturing sandwich struc­
tures by a single piece composed of core shapes
including honeycomb, rhombus, circle, and rectangle.
The three-point bending test shows that increasing
effective density yields maximum load and flexural
modulus for all core shapes, but rhombus core shape
is found to be the strongest. Bin Ishak, Fleming, and
Larochelle (2019) suggest a robotic 3D printer to realize
multi-plane layered path generation. The proposed
printing approach improves the elastic modulus, ulti­
mate tensile strength and yield the strength of the
tensile specimen. Tamir et al. (2022a) propose a novel
robot-assisted AM along with a control system frame­
work, which possesses multi-directional printing with­
out support structures. Huang and Singamneni (2015)
propose an adaptive curved surface slicing algorithm
combining flat and curved layers together. Their three-
point bending test shows that the thicker curved layer
leads to better mechanical strength. Lim et al. (2016)
use planar and surface layer printing in a concrete 3D
printing process; and conclude that surface layer print­
ing yields higher strength. Xia, Lin, and Ma (2020)
improve the mechanical performance of a printed
object by constructing the toolpath in the direction of
maximum principal stress.
Typical research in improving the surface quality of
AM parts is summarized next. Jin et al. (2017) present
a curved layer slicing algorithm to determine
a printing path for a 3-axis 3D printer. In their
approach, the stair-step effect that results in undesir­
able surface finish is reduced. Moreover, curved sur­
faces are accurately approximated by using B-spline.
Isa and Lazoglu (2019) give a 5-axis path planning
algorithm that minimizes staircase effects on solid
and hollow printing part components. Their study
subsequently checks path and tool orientation condi­
tions. Ding et al. (2015) present a path planning algo­
rithm that improves the quality and material
efficiency in WAAM. Feng et al. (2018) propose
a precise, reliable, and practically applicable slicing
approach of T-spline surfaces. Similarly, Xie et al.
(2020) propose a practically applicable, feasible, and
effective spline-based smoothing algorithm to
remove sharp corners around a printing path.
The second and third ways to guarantee quality
and mechanical strength of printed parts are ML-
based pre-process parameter optimization and ML-
based in-situ monitoring, respectively. The former is
an open-loop approach; while the latter is a closed-
loop one. They are discussed next.
Li et al. (2019) propose a data-driven prediction
model for the prediction of surface roughness in AM
industry. To collect temperature and vibration data,
various types of sensors, including accelerometers,
thermocouples, and infrared temperature sensors,
are used. Time and frequency domain data are
extracted from the sensor to train an ensemble learn­
ing algorithm. Khanzadeh et al. (2018) present super­
vised machine learning algorithms to predict porosity
within the printed parts from the morphological char­
acteristics of melt pool boundary. A thermal monitor­
ing system captures the melt pool signals, which may
be labeled as either normal or pores by x-ray tomo­
graphy.
Francis
and
Bian
(2019)
develop
a convolutional neural network-based geometric
compensation mechanism that uses melt pool ther­
mal history as input and distortion as output in
a laser-based AM. Feeding back the distorted model
to the original CAD model compensates geometric
error. Similarly, a convolutional neural network-
based 3D printing model error compensation frame­
work is presented (Shen et al. 2019b; a; Zhao et al.
2019). It has two kinds of networks, i.e. a prediction
network and a compensation network to yield
a compensated model for a 3D printer. Wang et al.
(2021) develop a regression model and layer time
control method to improve product quality and effi­
ciency of a large-scale AM. Their work uses real time
print surface temperature data from an infrared cam­
era. Tamir et al. (2022b) propose a feedback-based
error compensation strategy, which integrates
a fuzzy inference system and a grey wolf optimization
algorithm. Wang et al. (2018b) propose a closed-loop
control framework that integrates a vision-based
technique and neural network (NN). It is able to
inspect in-situ droplet behaviors and accordingly sta­
bilize the printing process in liquid metal jet printing.
Their study combines NN with a proportion-
integration-differentiation (PID) control system to
1364
T. S. TAMIR ET AL.


---


## Page 6


determine a drive voltage by taking droplet-image
features and properties as the training dataset. A
comprehensive review of AM process monitoring,
diagnosis and control can be found in (Fang et al.
2023).
We intend to investigate two key issues from the
aforementioned literature: 1) how to model an open-
loop ML for prediction (Li et al. 2019; Khanzadeh et al.
2018), and 2) how to design an ML-based closed-loop
control system (Wang et al. 2018b, 2021). We aim to
propose a novel system that integrates open-loop ML
models and a fuzzy inference system for processing
parameter optimization, which is never seen before to
our best knowledge. Matlab simulation is done for the
purpose of verification.
3. Design of ML algorithms and dataset
generation
3.1. Data collection
ML algorithms are data-driven approaches whose per­
formance are highly dependent on the amount of data.
In some areas, researchers tend to construct their own
training datasets, such as SQuAD for natural language
processing, ImageNet for image recognition, YouTube-
8 M for video classification, and MNIST for optical
character recognition (Qi et al. 2019). As a result, the
potential of ML is highlighted in those areas. On the
contrary, AM lacks organized experimental datasets
due to high cost of collecting data. This discourages
interested parties to build an open access dataset. Data
collection remains an unsolved problem and becomes
a challenge for those AM practitioners and researchers
who are interested in applying ML.
To ensure an advanced AM technology, sensors are
supposed to be placed in a printing process loop to
capture data, such as geometric deviation, surface
roughness, and porosity. A data collection sensory sys­
tem can be implemented by either offline, online, or
sometimes both. In an offline case, a necessary printed
part geometrical information is measured after the
completion of an entire printing process. Microscope
is ideal equipment to highlight the desired information.
While online sensory system actions are in-situ mea­
surements through which data are collected during
a printing process. A 3D camera can be used to capture
a real time printing information in this case. Both offline
and online sensory systems can be applied. The former
is used to model an ML algorithm for quality prediction
and the latter is used in an online processing parameter
optimization.
This study uses the collected dataset from other
work. The work (Jiang et al. 2020) uses the data to
Figure 1. Fused deposition modeling system.
INTERNATIONAL JOURNAL OF COMPUTER INTEGRATED MANUFACTURING
1365


---


## Page 7


build up an ML model for AM prediction. Its data is
uploaded to GitHub (Jiang 2019) for others to use.
Different from (Jiang et al. 2020), we use the data to
design an ML-based open-loop and closed-loop pre­
diction system for monitoring and optimization of
AM. As a part of a data collection method, they use
an offline sensory system to record the processing
parameters versus printed part properties. Fused
deposition modeling type 3D printer is used to con­
duct a printing experiment as shown in Figure 1. The
experimental real images are shown in Figure 2. Four
adjustable processing parameters, i.e. layer height,
print speed, line distance, and filament extrusion
speed, are used. They are utilized to determine
a connection status among printed lines. The connec­
tion status comprises of five classes – class 0 for large
space, 1 for little space, 2 for good connection, 3 for
little material overflow, and 4 for large material over­
flow – as shown in Figure 3. The class label is given
based on space between two consecutive printed
Figure 2. The experimental images showing connection status between printed lines (Jiang et al. 2020).
Figure 3. Class assignment for printed line connection.
1366
T. S. TAMIR ET AL.


---


## Page 8


lines. Either high spacing or overlapping between two
lines tells us about a poor connection, whereas accep­
table spacing is called a good connection. 400 labeled
data are generated from the experiment, some of
which are shown in Table 1. Note that mm and mm/
s stand for millimeter and millimeter-per-second,
respectively.
3.2. Open-loop control system
In control theory, open-loop and closed-loop control
systems are the two popular algorithms implemented
in a control engineering application area (Mei et al.
2021). The former uses no feedback to generate con­
trol actions. On the other hand, the latter uses feed­
back as a vital component for controlling a system.
The proposed ML classification algorithms in this sec­
tion take processing parameters as input and predict
printed part properties without any correction
mechanism to handle printed part abnormalities.
Rather, they give knowledge to determine optimal
parameters for better part quality. Generally, this pro­
cess is categorized under an open-loop system since it
cannot regenerate new parameters dynamically. This
open-loop-like ML system is a human-in-the-loop sys­
tem since training and testing data are generated by
a human operator. The overall structure of the system
is shown schematically in Figure 4.
3.3. Design of ML algorithms
ML is a rapidly growing technology applicable to
analyze complex systems where mathematical repre­
sentation is a challenge. It has also an ability to learn
tasks with no explicit programming (Geron 2018;
Moe, Rustad, and Hanssen 2018; Khargonekar and
Dahleh 2018). The most known types of ML are super­
vised learning, unsupervised learning, transfer learn­
ing, and reinforcement learning (Cao, Lin and Zhou
2021; Wang et al. 2018a; Goodfellow et al. 2016; Tamir
et al. 2020a; Yao et al. 2022). In a supervised learning,
datasets are presented in a vector form of ðx; yÞ and
the aim is to predict output data y given input data x.
An ML model is trained by using training data and
then used to predict the values of new input data.
In this study, five supervised ML algorithms – deep
neural network (DNN), support vector machine (SVM),
decision tree (DT), random forest (RF), and logistic
regression (LR) – are used for classification. The result­
ing models are used to decide the status of printed line
connection given layer height, print speed, line dis­
tance and filament extrusion speed.
DNN is a special type of NN with many layers hav­
ing basic processing elements called neurons. The
connection of neurons in a layer forms a network.
Each neuron performs its activation function given
a weighted sum of its inputs and a bias. The following
Table 1. Experimental samples.
No.
Filament extrusion speed (mm/s)
Layer height (mm)
Line distance (mm)
Print speed (mm/s)
Classes
1
0.5
0.1
0.3
10
4
2
0.5
0.2
0.3
10
3
3
1
0.1
0.9
10
2
4
1
0.2
0.9
20
0
5
1.5
0.4
0.5
40
0
6
1.5
0.1
0.3
40
1
7
2
0.1
0.3
10
4
8
2
0.3
0.7
10
2
9
2.5
0.2
0.3
30
3
10
2.5
0.2
0.5
50
1
Figure 4. Open-loop-based (offline) optimal parameter settings.
INTERNATIONAL JOURNAL OF COMPUTER INTEGRATED MANUFACTURING
1367


---


## Page 9


equation presents the result of an output neuron of
an entire network:
where y is the output of the neuron, x is its input, w ¼
w1; w2; . . . ; wn
ð
ÞT is a weight vector and b is a bias.
Weights and biases are the NN parameters which need
to be updated during an NN training process. The
combination of neurons in a typical NN forms three
layers, including input, hidden, and output layers. If the
number of hidden layers is more than one, a network is
called DNN. This study uses three DNN architectures.
One of them called DNN3 is shown in Figure 5, which is
composed of four hidden layers. Figure 5 shows the
overall network connection and the number of neu­
rons in each layer with the corresponding activation
function. For the first four layers, the rectified linear unit
(ReLU) activation function is used, i.e.
It returns an output equivalent to an input for positive
input values; and otherwise zero for all other input
values. The SoftMax activation function is used in the
last layer. The SoftMax function is a kind of probabil­
istic approach that normalizes all the values into the
range 0; 1
ð
Þ and the sum is equal to one. As a result, it
is suitable for multi-level classification problems. Its
mathematical expression is:
where z is a real number, and again, j indexes the
output units, so j ¼ 1; 2; . . . ; K.
The loss function used in our designed DNN is
categorical cross-entropy, i.e.
where, y, by and n are the predicted output, actual
output, and number of input samples respectively. yi
is the predicted output vector of the ith sample, e.g.
½0:1; 0:1; 0:1; 0:6; 0:1, and yij is the jth element of yi,
e.g. yi4 ¼ 0:6. The Adam optimizer is used in an entire
training process, and also ‘accuracy’ is chosen as
a metric in this model. The batch size and number of
epochs is set as 32 and 500, respectively.
4. Closed-loop ML system design
The application of an ML-based closed-loop control
system in AM industry is becoming one leading inno­
vation that significantly improves a printed part’s
quality. A feedback control algorithm decides the
relationship between processing parameters and
printed part properties in a 3D printing process and
tunes the optimal processing parameters. And the aim
of the feedback control system is to bring the connec­
tion status of class 2 in a possible way. Figure 6 shows
the schematic view of the proposed control system
along with the processing flow path. It consists of
camera, ML models, a Fuzzy Logic Controller (FLC),
and an extruder system. The camera captures an
actual connection among printed lines, which is then
compared with the ML model’s output given the cor­
responding processing parameters. The comparator
Figure 5. The structure of DNN3.
1368
T. S. TAMIR ET AL.


---


## Page 10


outputs, i.e. the error and its derivative, are fed to FLC.
Subsequently, FLC drives the extruder system with the
optimized processing parameters. Priori-knowledge
about the relationship between processing para­
meters and printed part properties formulated by an
open-loop ML is used to construct a fuzzy inference
system.
This work proposes a Multi-Input-Multi-Output
(MIMO) Fuzzy logic-based control algorithm to
generate optimized processing parameters. The
fuzzy system takes ‘error’ and ‘change in error’ as
inputs and outputs four processing parameters –
filament extrusion speed, layer height, layer dis­
tance, and print speed as shown in Figure 7. In
a fuzzification procedure, the triangular member­
ship function is chosen to take the advantage of its
simple calculation. The range of fuzzy membership
functions is determined by a trial-and-error proce­
dure. A Mamdani type fuzzy inference system
(Prieto-Entenza et al. 2019) is applied. The
Figure 6. The proposed negative feedback control system in 3D printing.
Figure 7. The fuzzy system structure.
INTERNATIONAL JOURNAL OF COMPUTER INTEGRATED MANUFACTURING
1369


---


## Page 11


inference system operations are fixed as ‘And-Min’,
‘Implication-Min’, ‘Aggregation-Max, and ‘Centroid’
type of defuzzification. We design twenty-five IF . . .
THEN structured fuzzy rules generated from two
linguistic input variables. Each has five linguistic
values. The five linguistic values are: negative-
large, negative-small, zero, positive-small, and posi­
tive-large. Similarly, each of the four linguistic out­
put variables have five linguistic values, including
level-1, level-2, level-3, level-4, and level-5. The
‘level’ notation indicates that the range of the
values. Figure 7 presents the overall structure of
the designed fuzzy system that shows the inter­
connection of each linguistic values to form a set
of fuzzy rules.
The designed fuzzy system is realized in algo­
rithm 1 and implemented in Matlab Simulink envir­
onment. First, it reads the connection status and
calculates ‘Error’ and ‘Change in Error’ accordingly.
Subsequently, new optimized 3D printer proces­
sing parameters are computed recursively. The
algorithm has two objective functions, ‘Error’ EðxÞ
and ‘Change in Error’ dEðxÞ
dt
as function of proces­
sing parameters. In fact, the error is expressed as
the difference between reference connection status
and actual connection status values. The setting of
processing parameters directly affects the connec­
tion status values. Thus, even though there is no
an equation that depicts the direct relationship
between the error and processing parameters, the
setting of processing parameters affects the error
and it can be said that the relationship is involved
indirectly. By applying the chain rule, the change
in error can be expressed as:
The aim of our optimization problem is to minimize
two objective functions by finding optimized proces­
sing parameters. This can be written mathematically as:
where F x
ð Þ is a column vector of the two objective
functions, and x ¼ x1; x2; x3; x4
ð
ÞT represents four pro­
cessing parameters.
Algorithm 1:
Optimization of processing parameters
Input: Error, EðxÞ, and Change in Error, dEðxÞ
dt , are FLC
inputs, and Processing Parameters, PP, are
MVLR inputs
Output: Processing Parameters, PP, are FLC outputs,
and Connection Status, CS, is MVLR output
Initial Processing Parameters, IPP;
Reference Connection Status, RCS;
while the 3D printer is running do
Read CS;
Compute EðxÞ ¼ RCS   CS;
Compute dEðxÞ
dt ;
if EðxÞ and/or dEðxÞ
dt are/is either large or medium then
New PP = updated PP;
else
New PP = IPP;
end
Return New PP;
end
In addition to closed-loop control system design,
the mathematical expression of a 3D printer is
necessary to ensure the state of a fully controllable
condition. The system performance can be then
verified in Matlab Simulink environment. Basically,
two known modeling techniques, i.e. linear and
nonlinear ones, are used to mathematically model
the process. The former includes a transfer function,
single-variable linear regression, and multi-variate
linear regression. The latter includes state-space
representation, single-variable higher order polyno­
mial regression, and multi-variate higher order poly­
nomial regression (Goodfellow et al. 2016). The
former is applied for systems having inputs which
are independent of each other, and the system out­
put is then affected by individual inputs separately.
The latter, on the other hand, is used when system
inputs have some sort of correlation to each other,
and the way how those inputs affect an output is
then treated in a different manner. In our case, the
variables that are input to the system are uncorre­
lated to each other and their summed-up effect
determines the output variable condition. As one
of the linear modeling techniques, a Multi-Variate
Linear Regression (MVLR) model can be used to
represent the mapping of processing parameters
to 3D-printed part properties. The general mathe­
matical expression of MVLR is:
1370
T. S. TAMIR ET AL.


---


## Page 12


In a simplified form, equation (7) can be
expressed as:
where Y is an n  1 output feature matrix, X is an n 
k þ 1
ð
Þ input feature matrix, β is an k þ 1
ð
Þ  1 input
feature coefficient matrix, and ε is an n  1 regression
error matrix. k is the number of input features and n is
the number of training examples. This work uses four
input features and one output feature to build an
MVLR model. Filament extrusion speed, print speed,
layer height, and line distance are categorized under
input features, whereas the connection status
between two printed lines is categorized under an
output feature. The total number of training examples
is 400.
The regression error can be compensated by add­
ing a random n  1 compensation matrix ~ε in the left-
hand side of equation (8) , thus resulting in:
Input features’ coefficient matrix β can be
expressed as:
where Xy is the pseudo-inverse of X. To minimize the
effect of regression error on the MVLR model, we
approximate ~ε as ε, and compute β via equation (10).
β is then in the form of β ¼ β1; β2; β3; β4; β5
ð
ÞT.
Therefore, the final MVLR model describing a 3D prin­
ter is derived from equation (7) and mathematically
expressed as:
The regression error histogram of the formulated
MVLR model is shown in Figure 8. The distribution of
Figure 8. Regression error histogram.
Figure 9. Simulink Model of 3D printing control system.
INTERNATIONAL JOURNAL OF COMPUTER INTEGRATED MANUFACTURING
1371


---


## Page 13


residues (Res) for the number of instances is observed
in it. For most of the instances the error falls into the
interval between −0.1 and 0.05. The mean squared
error is found to be 0.0064 and this can be assumed as
a tolerated error value. Therefore, we can use this type
of model to approximate a real system. The Simulink
model of a feedback fuzzy system along with the
mathematical expression of a 3D printer is shown in
Figure 9.
5. Results and discussions
5.1. Open-loop classification analysis
In this section, the open-loop classification results and
discussions are presented. We choose five commonly
used ML models, including DNN, SVM, DT, RF, and LR
and present their performance. For each model, we
first separate the data to two parts. 80% of the data
are used for 5-fold cross-validation and 20% are used
for model testing. Data in 5-fold cross-validation are
further separated to five parts. Each part serves as the
validation data once and the model is trained on the
rest parts. From 400 samples, there are 205, 74, 52, 39,
and 30 samples from label 1 to label 5 respectively.
When the whole dataset is split randomly to training
and testing data, for example, it is highly probable
that the training data includes very few samples of
label 5 (e.g. 2 samples), and the rest 28 samples of
label 5 are included in the testing data. In this case,
the trained model can work poorly. Therefore, each
category of labels needs to be split independently as
shown in Table 2. In cross-validation, we train each
model five times and the validation accuracy for each
model is recorded at each time. After cross-validation,
for each model, we obtain a list of validation accuracy
(V), i.e. V1, V2, V3, V4, and V5.
Three DNN architectures are used – DNN1-DNN3.
The architecture difference comes from the number
of hidden layers used, as illustrated as follows. DNN1
has structure of (4, 10, 10, 5), which means the NN has
4 neurons in the input layer, 10 neurons in the first
layer, 10 neurons in the second layer, and 5 neurons in
the output layer. Similarly, DNN2 and DNN3 have
structure of (4, 10, 10, 10, 5) and (4, 10, 10, 10, 10, 5)
respectively. Table 3 shows validation accuracy of the
individual folds and mean validation accuracy of each
model.
The 5-fold cross-validation classification accuracy
results for each model shown in Table 3 are used to
choose the best model for final classification. Based
on mean validation accuracy recorded in each model,
it is observed that DNN with architecture DNN3 out­
performs all other models with mean validation accu­
racy of 98.42%. On the contrary, LR scores the least
mean validation accuracy of 89.96%. Moreover, from
the DNN architectures, DNN1 scores the least mean
validation accuracy of 98.13%. Therefore, DNN3 is
chosen as the viable classification model for our
task. Then a new DNN3 model is created and trained
by using the whole dataset that was used for 5-fold
cross-validation. As a result, the training accuracy of
the new DNN3 model is achieved at 98.74%. Finally,
the re-trained DNN3 model is used as the final model
to do the testing with 20% of the whole data, and has
reached testing accuracy of 97.53%. Compared to the
training accuracy of 82.5% and testing accuracy of
83.33% that reached in (Jiang et al. 2020), we have
raised these two accuracies by 16.24% and 14.20%,
respectively. Figure 10 shows the classification
Table 2. Splitting data.
Data
Label 1
Label 2
Label 3
Label 4
Label 5
Training data
0.8×205
0.8×74
0.8×52
0.8×39
0.8×30
Testing data
0.2×205
0.2×74
0.2×52
0.2×39
0.2×30
Table 3. Validation accuracy for each model.
ML model
V1
V2
V3
V4
V5
Mean (V)
DNN1
0.9836
1.0
1.0
0.9692
0.9538
0.9813
DNN2
0.9344
1.0
1.0
0.9846
1.0
0.9838
DNN3
0.9672
1.0
1.0
0.9846
0.9692
0.9842
SVM
0.9344
0.9687
0.9687
0.923
0.9384
0.9466
DT
0.9508
0.9531
1.0
0.9846
0.9692
0.9715
RF
1.0
0.9531
1.0
0.9692
0.9538
0.9752
LR
0.8852
0.9062
0.9375
0.8615
0.9076
0.8996
1372
T. S. TAMIR ET AL.


---


## Page 14


Figure 10. Classification performance, (a) on training dataset and (b) on testing dataset.
Figure 11. Probability distributions (a) large space (b) little space (c) good connection (d) little material overflow (e) large material
overflow.
INTERNATIONAL JOURNAL OF COMPUTER INTEGRATED MANUFACTURING
1373


---


## Page 15


performance of DNN3 on the training and testing
data. Blue color squares represent actual connection
statuses, and orange color circles represent the pre­
dicted connection statuses. It is seen that squares and
circles are overlapped in many of instances. The over­
lapping tells us that actual class label is equal to the
predicted one. This assures that DNN3 identifies the
connection status very well.
The proposed open-loop classification model
achieves our first objective, i.e. revealing the relation­
ship between processing parameters and the printed
part properties. From the classification results, the
connection status of printed parts for the correspond­
ing processing parameters is known. Consequently,
we are clear which processing parameters result in
a good connection between the printed lines in an
offline manner.
Moreover, a five-level connection status probability
distribution is generated by making testing data as
input to DNN3. The 10-bin histogram-based graphical
representation of connection statuses, including
‘Large space’, ‘Little space’, ‘Good connection’, ‘Little
material overflow’, and ‘Large material overflow’ are
shown in Figure 11(a–e) respectively. In Figure 11, the
connection status probabilities are presented in
increasing order as Large material overflow, Little
material overflow, Good connection, Little space,
and Large space. We have observed that a ‘Large
space’ occurred in most of instances for our testing
data. This shows that the proposed open-loop classi­
fication approach tells us only the status of the
printed parts without any processing parameters
adjustment. Therefore, incorporating a process mon­
itoring system is required to optimize the effect of
processing parameters on the quality of printed parts.
From the knowledge of open-loop classification
results, we can realize our second objective to design
a closed-loop control system to generate optimal
processing parameters. The proposed closed-loop
system is analyzed next.
5.2. Closed-loop analysis
In this section, the simulation results and discussions
of the proposed closed-loop control system are pre­
sented. A feedback control system that comprises
open-loop ML model, fuzzy inference system,
Figure 12. Connection status setting.
Figure 13. Optimized processing parameters, (a) print speed and (b) the other three parameters.
1374
T. S. TAMIR ET AL.


---


## Page 16


extruder system, and comparator is analyzed. Inputs
to the comparator are reference and actual connec­
tion status information, and the comparator returns
an error as an output. The fuzzy system takes ‘Error’
and ‘Change in error’ as input and generates the
optimized processing parameters that drive the extru­
der system. The fuzzy inference rules are constructed
from a priori-knowledge of the open-loop ML model.
The feedback system simulation is run for 100
seconds. At the very beginning of the printing
process, a 3D printer is assumed to run under
initial processing parameters that correspond to
an initial printed line connection. However, the
initial one may not be the desired one. Therefore,
we assign different types of connection statuses as
a reference, and the objective is to track the best
connection status after some printing time.
Figure 12 shows the five-level connection statuses
that are given to the control algorithm which
could be used as a reference. Following that, the
corresponding processing parameters that may be
different from the initial processing parameters are
generated from the simulation of the feedback
control system. Figure 13 shows the output of
the designed control algorithm, which are named
as the optimized processing parameters, including
layer height, print speed, line distance, and fila­
ment extrusion speed in the function of time. The
new optimized processing parameters thus drive
the printing system to result in a good connection
between the printed lines. We observe that the
quality of connections between printed lines gets
improved by introducing the control loop in the
entire 3D printing process. Figure 14 shows the
actual connection status that basically charac­
terizes the quality of a 3D printing system. It is
observed that after 25 seconds the connection sta­
tus is approaching to class 2, which is good con­
nection status. Despite the fact that the connection
status profile is centered on 1.5, the majority of the
profile touches class 2 and the remainder touches
class 1. This is due to the fact that the 3D printing
process is dynamic and difficult to be steady in
terms of printed part properties. The optimized
processing parameters generate better printed
part properties at a time and the printing process
may not sustain longer due to a variety of reasons
such as environmental disturbances, equipment
problems, and so on. That is why the profile
touches class 2 once and class 1 the other time.
This tells us about the quality assuring capability of
the proposed closed-loop system. Generally speak­
ing, the fuzzy system monitors the overall printing
process by using the fuzzy rules. Moreover, the
proposed feedback system plays a vital role in
generating optimized control actions and at the
same time it ensures the printing quality.
It can be said that performances of the proposed
open-loop and closed-loop approaches mainly rely on
an accurate ML algorithm. The nicely tuned ML algo­
rithm results in a good classification performance.
Furthermore, it is shown that the integration of ML
with feedback control plays a vital role in achieving
good connection between the printed lines in 3D
printing. Although the proposed closed-loop algo­
rithm cannot find an optimal processing parameter
in the early stage of the printing process, it tolerates
some recommended time and tracks the best connec­
tion status.
Last, since AM is a fast growing technology in the
domain of digital manufacturing, proposing a novel
control framework is a vital component for assuring
the quality of products. Far from the existing open-
loop control techniques applied to most of the existing
AM processes, our control framework integrates both
open-loop and closed-loop techniques and improves
the performance of the 3D printing process by gener­
ating the optimized processing parameters. The pro­
posed control system approach gives a promising
result for growing AM technologies further. Therefore,
it is recommended for practitioners to apply this prac­
tical concept for building advanced 3D printing
equipment.
Figure 14. Actual connection status.
INTERNATIONAL JOURNAL OF COMPUTER INTEGRATED MANUFACTURING
1375


---


## Page 17


6. Conclusion
Given the issue of quality and mechanical strength of
printed parts in AM industry, this paper presents
a mechanism to monitor processing parameters,
including layer height, print speed, line distance,
and filament extrusion speed via ML algorithms. Two
types of control frameworks are proposed to monitor
processing parameters. 1) Open-loop approach: five
ML classification algorithms that generate the rela­
tionship between processing parameters and printed
part properties are presented. Among which, DNN3
performs better than others and is thus chosen as the
final classification model in this work. Consequently,
this ML model can identify the best processing para­
meters combinations that result better printed part
quality in an offline manner. Furthermore, this ML
model can be applied to design a closed-loop control
system. 2) Closed-loop approach: a fuzzy logic-based
feedback control system along with the mathematical
model of a 3D printer is designed to generate four
optimized processing parameters. In this regard, the
fuzzy system monitors the overall printing process via
fuzzy rules which characterizes the values of proces­
sing parameters. It can be said that a closed-loop ML
algorithm has good contribution to the monitoring
and optimization of processing parameters in 3D
printing, thus significantly improving the quality of
printed part properties. As a result, a self-adjusting
3D printing system can be formed in the entire print­
ing process and this fact leads to grow AM one step
further. Last, it is observed that this work uses only
adjustable processing parameters to maintain the
quality of printed parts. Therefore, as recommenda­
tion, the quality of a printed part can be further
improved if additional processing parameters are
considered. Moreover, the results can be improved
and complemented by refining the control and opti­
mization frameworks. The next step is to do real-time
closed-loop 3D printing experiments.
Nomenclature
3D
Three Dimensional
AM
Additive Manufacturing
CAD
Computer Aided Design
DNN
Deep Neural Network
DT
Decision Tree
FLC
Fuzzy Logic Controller
LR
Logistic Regression
ML
Machine Learning
MVLR
Multi-Variate Linear Regression
NN
Neural Network
RF
Random Forest
SVM
Support Vector Machine
WAAM
Wire and Arc Additive Manufacturing
Disclosure statement
No potential conflict of interest was reported by the author(s).
Funding
This work was supported in part by the National Key Research
and Development Program of China (No. 2018YFB1700403);
National Natural Science Foundation of China under Grants
U1909204, U1909218, U1811463, 61872365 & 61806198; CAS
Key Technology Talent Program (Zhen Shen); The Guangdong
Basic and Applied Basic Research Foundation under Grant
2021B1515140034; The Foshan Science and Technology
Innovation Team Project under Grant 2018IT100142; The
Scientific Instrument Developing Project of the Chinese
Academy of Sciences under Grant No. YZQT014; CAS STS
Dongguan Joint Project 20201600200072
ORCID
Tariku Sinshaw Tamir
http://orcid.org/0000-0003-3700-
928X
Gang Xiong
http://orcid.org/0000-0002-4303-5559
Zhen Shen
http://orcid.org/0000-0002-9634-4945
MengChu Zhou
http://orcid.org/0000-0002-5408-8752
Jingchao Jiang
http://orcid.org/0000-0002-0446-3454
References
Bikas, H., P. Stavropoulos, and G. Chryssolouris. 2016. “Additive
Manufacturing Methods and Modelling Approaches:
A Critical Review.” International Journal of Advanced
Manufacturing Technology 83 (1–4): 389–405. doi:10.1007/
s00170-015-7576-2.
Bin Ishak, Ismayuzri, David Fleming, and P. Larochelle. 2019.
“Multiplane Fused Deposition Modeling: A Study of Tensile
Strength.” Mechanics Based Design of Structures and Machines
47 (5): 583–598. doi:10.1080/15397734.2019.1596127.
Camacho, D. D., P. Clayton, W. J. O’Brien, C. Seepersad,
M. Juenger, R. Ferron, and S. Salamone. 2018. “Applications
of Additive Manufacturing in the Construction Industry–A
1376
T. S. TAMIR ET AL.


---


## Page 18


Forward-Looking Review.” Automation in Construction 89:
110–119. doi:10.1016/j.autcon.2017.12.031.
Cao, Z., C. Lin, and M. Zhou. 2021. “A Knowledge-Based Cuckoo
Search Algorithm to Schedule a Flexible Job Shop with
Sequencing Flexibility.” IEEE Transactions on Automation
Science and Engineering 18 (1): 56–69.
Ding, D., Z. Pan, D. Cuiuri, and H. Li. 2015. “A Practical Path
Planning Methodology for Wire and Arc Additive
Manufacturing of Thin-Walled Structures.” Robotics and
Computer-Integrated Manufacturing 34: 8–19. doi:10.1016/j.
rcim.2015.01.003.
Di, L., T. Srikanthan, R.S. Chandel, and I. Katsunori. 2001.
“Neural-Network-Based Self- Organized Fuzzy Logic
Control for Arc Welding.” Engineering Applications of
Artificial Intelligence 14 (2): 115–124. doi:10.1016/S0952-
1976(00)00057-9.
Esmaeilian, B., S. Behdad, and B. Wang. 2016. “The Evolution and
Future of Manufacturing: A Review.” Journal of Manufacturing
Systems 39: 79–100. doi:10.1016/j.jmsy.2016.03.001.
Fang, Q., G. Xiong, M. Zhou, T. S. Tamir, C.-B. Yan, H. Wu, Z.
Shen, and F. Y. Wang, “Process Monitoring, Diagnosis and
Control of Additive Manufacturing,” IEEE Transactions on
Automation Science and Engineering, to appear in 2023.
Feng, J., J. Fu, Z. Lin, C. Shang, and B. Li. 2018. “Direct Slicing of
T-Spline Surfaces for Additive Manufacturing.” Rapid Prototyping
Journal 24 (4): 709–721. doi:10.1108/RPJ-12-2016-0210.
Francis, J., and L. Bian. 2019. “Deep Learning for Distortion
Prediction in Laser-Based Additive Manufacturing Using
Big Data.” Manufacturing Letters 20: 10–14. doi:10.1016/j.
mfglet.2019.02.001.
Geron, A. 2018. Hands-On Machine Learning with Scikit-Learn
and Tensor Flow. Sebastopol, CA, United States: O’Reily
Media Inc.
Ghahramani, M., Y. Qiao, M. Zhou, A. O. Hagan, and J. Sweeney.
2020. “AI-Based Modeling and Data-Driven Evaluation for Smart
Manufacturing Processes.” IEEE/CAA Journal of Automatica Sinica
7 (4): 1026–1037. doi:10.1109/JAS.2020.1003114.
Goh, G.D., S.L. Sing, and W.Y. Yeong. 2020. “A Review on
Machine Learning in 3D Printing: Applications, Potential,
and Challenges.” Artificial Intelligence Review 54 (1): 1–32.
doi:10.1007/s10462-020-09876-9.
Goodfellow, I., Y. Bengio, A. Courville, and Y. Bengio. 2016. Deep
Learning. Vol. 1. Cambridge, Massachusetts (United States):
MIT press Cambridge.
Heidarzadeh, A., Ö. Müge Testik, G. Güleryüz, and R. Vatankhah
Barenji. 2020. “Development of a Fuzzy Logic Based Model
to Elucidate the Effect of FSW Parameters on the Ultimate
Tensile Strength and Elongation of Pure Copper Joints.”
Journal of Manufacturing Processes 53: 250–259. doi:10.
1016/j.jmapro.2020.02.020.
Huang, B., and S. B. Singamneni. 2015. “Curved Layer Adaptive
Slicing (CLAS) for Fused Deposition Modelling.” Rapid
Prototyping Journal 21 (4): 354–367. doi:10.1108/RPJ-06-
2013-0059.
Ieracitano, C., A. Paviglianiti, M. Campolo, A. Hussain, E. Pasero,
and F. Carlo Morabito. 2020. “A Novel Automatic
Classification System Based on Hybrid Unsupervised and
Supervised Machine Learning for Electrospun Nanofibers.”
IEEE/CAA Journal of Automatica Sinica 8 (1): 64–76. doi:10.
1109/JAS.2020.1003387.
Isa, M. A., and I. Lazoglu. 2019. “Five-Axis Additive
Manufacturing of Freeform Models Through Buildup of
Transition Layers.” Journal of Manufacturing Systems 50:
69–80. doi:10.1016/j.jmsy.2018.12.002.
Jiang, J. 2019. “Machine Learning for Additive Manufacturing”.
Accessed 20 August 2020. http://www.github.com/jjia547/
ML-for-AM
Jiang, J., C. Yu, X. Xu, Y. Ma, and J. Liu. 2020. “Achieving Better
Connections Between Deposited Lines in Additive
Manufacturing via Machine Learning.” Mathematical
Biosciences and Engineering 17 (4): 3382. doi:10.3934/mbe.
2020191.
Jin, Y., J. Du, Y. He, and G. Fu. 2017. “Modeling and Process
Planning for Curved Layer Fused Deposition.” International
Journal of Advanced Manufacturing Technology 91 (1–4):
273–285. doi:10.1007/s00170-016-9743-5.
Khanzadeh,
M.,
S.
Chowdhury,
M.
Marufuzzaman,
M. A. Tschopp, and L. Bian. 2018. “Porosity Prediction:
Supervised-Learning of Thermal History for Direct Laser
Deposition.” Journal of Manufacturing Systems 47: 69–82.
doi:10.1016/j.jmsy.2018.04.001.
Khargonekar, P. P., and M. A. Dahleh. 2018. “Advancing Systems
and Control Research in the Era of ML and AI.” Annual
Reviews in Control 45: 1–4.
Li, Yongzhe, X. Li, G. Zhang, I. Horváth, and Q. Han. 2021.
“Interlayer Closed-Loop Control of Forming Geometries for
Wire and Arc Additive Manufacturing Based on Fuzzy-Logic
Inference.” Journal of Manufacturing Processes 63: 35–47.
Lim, S., R. A. Buswell, P. J. Valentine, D. Piker, S. A. Austin, and
X. De Kestelier. 2016. “Modelling Curved-Layered Printing
Paths
for
Fabricating
Large-
Scale
Construction
Components.” Additive Manufacturing 12: 216–230.
Liu, H.-C., X. Luan, M. Zhou, and Y. Xiong. 2020. “A New
Linguistic
Petri
Net
for
Complex
Knowledge
Representation and Reasoning.” IEEE Transactions on
Knowledge and Data Engineering 34 (3): 1011–1020. doi:10.
1109/TKDE.2020.2997175.
Li, Zhixiong, Z. Zhang, J. Shi, and D. Wu. 2019. “Prediction of
Surface
Roughness
in
Extrusion-Based
Additive
Manufacturing with Machine Learning.” Robotics and
Computer-Integrated Manufacturing 57: 488–495.
Mei, J., Z. Lu, J. Hu, and Y. Fan. 2021. “Energy-Efficient Optimal
Guaranteed Cost Intermittent-Switch Control of a Direct
Expansion Air Conditioning System.” IEEE/CAA Journal of
Automatica Sinica 8 (11): 1852–1866.
Meng, L., B. McWilliams, W. Jarosinski, H. Yeong Park, Y. Gil
Jung, J. Lee, and J. Zhang. 2020. “Machine Learning in
Additive Manufacturing: A Review.” JOM 72: 2363–2377.
doi:10.1007/s11837-020-04155-y.
Moe, S., A. Marthine Rustad, and K. G. Hanssen. 2018. “Machine
Learning in Control Systems: An Overview of the State of the
Art.” In International Conference on Innovative Techniques
and Applications of Artificial Intelligence, 250–265. Springer
International Publishing, Cham: Springer.
INTERNATIONAL JOURNAL OF COMPUTER INTEGRATED MANUFACTURING
1377


---


## Page 19


Ngo, T. D., A. Kashani, G. Imbalzano, K. T. Nguyen, and D. Hui.
2018. “Additive Manufacturing (3D Printing): A Review of
Materials,
Methods,
Applications
and
Challenges.”
Composites Part B: Engineering 143: 172–196.
Popova, E., T. M. Rodgers, X. Gong, A. Cecen, J. D. Madison, and
S. R. Kalidindi. 2017. “Process-Structure Linkages Using
a Data Science Approach: Application to Simulated
Additive Manufacturing Data.” Integrating Materials and
Manufacturing Innovation 6 (1): 54–68.
Prieto-Entenza, P. J., N. Ramon Cazarez-Castro, L. T. Aguilar,
S. L. Cardenas- Maciel, and J. Antonio Lopez-Renteria. 2019.
“A Lyapunov Analysis for Mamdani Type Fuzzy-Based Sliding
Mode Control.” IEEE Transactions on Fuzzy Systems 28 (8):
1887–1895.
Qi, X., G. Chen, Y. Li, X. Cheng, and C. Li. 2019. “Applying Neural-
Network-Based
Machine
Learning
to
Additive
Manufacturing: Current Applications, Challenges, and
Future Perspectives.” Engineering 5 (4): 721–729.
Shen, Z., X. Shang, Y. Li, Y. Bao, X. Zhang, X. Dong, L. Wan,
G. Xiong, and F.-Y. Wang. 2019a. “PredNet and CompNet:
Prediction and High-Precision Compensation of In-Plane
Shape Deformation for Additive Manufacturing.” In 2019
IEEE 15th International Conference on Automation Science
and Engineering (CASE), Vancouver, BC, Canada, 462–467. IEEE.
Shen, Z., X. Shang, M. Zhao, X. Dong, G. Xiong, and F.-Y. Wang.
2019b.
“A
Learning-Based
Framework
for
Error
Compensation in 3D Printing.” IEEE Transactions on
Cybernetics 49 (11): 4042–4050.
Sugiyama, K., R. Matsuzaki, M. Ueda, A. Todoroki, and
Y. Hirano. 2018. “3D Printing of Composite Sandwich
Structures Using Continuous Carbon Fiber and Fiber
Tension.” Composites Part A, Applied Science and
Manufacturing 113: 114–121.
Tamir, T. S., G. Xiong, X. Dong, Q. Fang, S. Liu, E. Lodhi, Z. Shen,
and F.-Y. Wang. 2022a. “Design and Optimization of a Control
Framework for Robot Assisted Additive Manufacturing Based
on the Stewart Platform.” International Journal of Control,
Automation, and Systems 20 (3): 968–982.
Tamir, T. S., G. Xiong, Q. Fang, X. Dong, Z. Shen, and F.-Y. Wang. 2022b.
“A Feedback-Based Print Quality Improving Strategy for FDM 3D
Printing: An Optimal Design Approach.” International Journal of
Advanced Manufacturing Technology 120 (3): 2777–2791.
Tamir, T. S., G. Xiong, Z. Li, H. Tao, Z. Shen, B. Hu, and
H. Mulugeta Menkir. 2020a. “Traffic Congestion Prediction
Using Decision Tree, Logistic Regression and Neural
Networks.” Ifac-PapersOnline 53 (5): 512–517.
Tamir, T. S., G. Xiong, H. Mulugeta Menkir, X. Shang,
Z. Shen, X. Dong, and X. Gong. 2020b. “Developing
SCADA Systems to Monitor and Control Liquid and
Detergent Factories.” In 2020 IEEE 16th International
Conference on Automation Science and Engineering
(CASE), Hong Kong, China, 691–696. IEEE.
Tamir, T. S., G. Xiong, Z. Shen, X. Gong, S. Liu, E. Lodhi, L. Wan, and
X. Dong. 2020c. “Comparative Study of Four Speed Controllers
of Brushless DC Motors for Industrial Applications.” Ifac-
PapersOnline 53 (5): 59–64.
Uhlmann, E., A. Bergmann, R. Bolz, and W. Gridin. 2018.
“Application of Additive Manufactured Tungsten Carbide
Tool Electrodes in EDM.” Procedia CIRP 68: 86–90.
Wang, F., S. Fathizadan, F. Ju, K. Rowe, and N. Hofmann.
2021. “Print Surface Thermal Modeling and Layer Time
Control for Large-Scale Additive Manufacturing.” IEEE
Transactions on Automation Science and Engineering
18 (1): 244–254.
Wang, T., T.-H. Kwok, C. Zhou, and S. Vader. 2018b. “In-Situ
Droplet Inspection and Closed-Loop Control System Using
Machine Learning for Liquid Metal Jet Printing.” Journal of
Manufacturing Systems 47: 83–92.
Wang, J., Y. Ma, L. Zhang, R. X. Gao, and D. Wu. 2018a. “Deep
Learning
for
Smart
Manufacturing:
Methods
and
Applications.” Journal of Manufacturing Systems 48: 144–156.
Wang, C., W. Pedrycz Z. Li, and M. Zhou. 2021. “Residual-driven
Fuzzy C-Means Clustering for Image Segmentation.” IEEE/
CAA Journal of Automatica Sinica 8 (4): 876–889.
Xia, L., S. Lin, and G. Ma. 2020. “Stress-Based Tool-Path Planning
Methodology for Fused Filament Fabrication.” Additive
Manufacturing 32: 101020.
Xie, F., L. Chen, Z. Li, and K. Tang. 2020. “Path Smoothing and Feed
Rate Planning for Robotic Curved Layer Additive Manufacturing.”
Robotics and Computer-Integrated Manufacturing 65: 101967.
Xiong, G., T. S. Tamir, Z. Shen, X. Shang, H. Wu, and F. Y. Wang.
2022. “A Survey on Social Manufacturing: A Paradigm Shift
for Smart Prosumers,” IEEE Transactions on Computational
Social Systems. doi:10.1109/TCSS.2022.3180201.
Yao, S., Q. Kang, M. Zhou, M. J. Rawa, and A. Abusorrah. 2022.
“A Survey of Transfer Learning for Machinery Diagnostics
and Prognostics.” Artificial Intelligence Review. doi:10.1007/
s10462-022-10230-4.
Zadeh, L. A. 1965. “Fuzzy Sets.” Information and Control 8 (3):
338–353.
Zhang, H., Y. Yang, K. Hu, B. Liu, M. Liu, and Z. Huang. 2020.
“Stereolithography-Based
Additive
Manufacturing
of
Lightweight and High-Strength Cf/SiC Ceramics.” Additive
Manufacturing 34: 101199.
Zhao, G., G. Ma, J. Feng, and W. Xiao. 2018. “Nonplanar Slicing and
Path Generation Methods for Robotic Additive Manufacturing.”
International Journal of Advanced Manufacturing Technology
96 (9–12): 3149–3159.
Zhao, M., G. Xiong, X. Shang, C. Liu, Z. Shen, and H. Wu.
2019.
“Nonlinear
Deformation
Prediction
and
Compensation for 3D Printing Based on CAE Neural
Networks.” In 2019 IEEE 15th International Conference on
Automation Science and Engineering (CASE), Vancouver,
BC, Canada, 667–672. IEEE.
1378
T. S. TAMIR ET AL.
View publication stats


---
