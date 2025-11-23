# MACS_Volume 12_Issue Special Issue 2_ Mechanics of Advanced Fiber-Reinforced Composite Structures_Pages 261-270

> **Source:** `MACS_Volume 12_Issue Special Issue 2_ Mechanics of Advanced Fiber-Reinforced Composite Structures_Pages 261-270.pdf`
> **Converted:** 2025-11-22 21:18:11
> **Method:** PyMuPDF

---

## Page 1


Mechanics of Advanced Composite Structures 12 (2025), Serial Number 25, 261 – 270


Semnan University
Mechanics of Advanced Composite Structures
Journal homepage: https://macs.semnan.ac.ir/
ISSN: 2423-7043


* Corresponding author.
   E-mail address: prashant.anerao@viit.ac.in
Cite this article as:
Anerao, P., Kulkarni, A., Munde, Y. and Kharate, N., 2025. A Comparative Study of Machine Learning Techniques for Predicting
Mechanical Properties of Fused Deposition Modelling (FDM)-Based 3D-Printed Wood/PLA Biocomposite. Mechanics of Advanced
Composite Structures, 12(2), pp. 261-270.
https://doi.org/10.22075/MACS.2024.33776.1638
Research Article – Part of the Special Issue on Mechanics of Advanced Fiber-Reinforced Composite Structures
A Comparative Study of Machine Learning Techniques for
Predicting Mechanical Properties of Fused Deposition
Modelling (FDM)-Based 3D-Printed Wood/PLA Biocomposite
Prashant Anerao a *
, Atul Kulkarni a
, Yashwant Munde b
, Namrata Kharate c

a Department of Mechanical Engineering, Vishwakarma Institute of Information Technology, Pune 411048, India
b Department of Mechanical Engineering, Cummins College of Engineering for Women, Pune 411052, India
c Department of Computer Engineering, Vishwakarma Institute of Information Technology, Pune 411048, India
A R T I C L E  I N F O
A B S T R A C T
Article history:
Received:  2024-04-13
Revised:  2024-07-29
Accepted:  2024-08-12
Wood/PLA biocomposite filament is a 3D printing material that blends Polylactic Acid (PLA),
a biopolymer, with wood powder acting as reinforcement. This combination results in a
sustainable 3D printing filament that has grown in popularity in recent years due to its eco-
friendliness and the natural appearance of 3D-printed parts. To assess the suitability of
wood/PLA biocomposite for various additive manufacturing applications, it is essential to
determine its mechanical properties. This study employs fused deposition modeling (FDM)
as the additive manufacturing process and focuses on assessing the mechanical properties
(tensile, flexural, and impact) of 3D-printed biocomposite. The Taguchi L27 design of the
experiments is utilized, and the key process parameters under consideration are infill pattern,
layer thickness, raster angle, nozzle temperature, and infill density. A layer thickness of 0.3
mm and an infill density of 100% yielded the highest tensile strength of 42.46 MPa, flexural
strength of 83.43 MPa, and impact strength of 44.76 J/m. The dataset has been carefully
prepared to facilitate machine learning for both training and testing, and it contains the
experimental results and associated process parameters. Four distinct machine learning
algorithms have been selected for predictive modeling: Linear Regression, Support Vector
Machine (SVM), eXtreme Gradient Boosting (XGBoost), and Adaptive Boosting (AdaBoost).
Given the intricate nature of the dataset and the presence of nonlinear relationships between
parameters, XGBoost and AdaBoost exhibited exceptional performance. Notably, the XGBoost
model delivered the most accurate predictions. The results were assessed using the
coefficient of determination (R2), and the achieved values for all observed mechanical
properties were found to be greater than 0.99. The results signify the remarkable predictive
capabilities of the machine learning model. This study provides valuable insights into using
machine learning to predict the mechanical properties of 3D-printed wood/PLA composites,
supporting progress in sustainable materials engineering and additive manufacturing.
Keywords:
Additive manufacturing;
3D printing;
Fused deposition modeling;
Biocomposite;
Machine learning;
Mechanical characterization.
© 2025 The Author(s). Mechanics of Advanced Composite Structures published by Semnan University Press.
This is an open access article under the CC-BY 4.0 license. (https://creativecommons.org/licenses/by/4.0/)

1. Introduction
Fused Deposition Modeling (FDM) has
emerged as a commonly adopted additive
manufacturing
(AM)
technique,
gaining
popularity due to its ease of use, low cost,
compact size, and safety [1]. FDM mostly uses
polymeric materials like acrylonitrile butadiene


---


## Page 2


Anerao et al. / Mechanics of Advanced Composite Structures 12 (2025) 261 - 270
262
styrene (ABS) and polylactide (PLA) to construct
3D objects layer by layer. The industry's
commitment to eco-friendly practices and rising
awareness of environmental sustainability led to
a major shift in material choices in the
manufacturing sector [2,3]. In response, an
increase in the use of natural fiber or filler-
reinforced
polymeric
materials
has
been
explored by many researchers for the FDM
process [4]. Numerous studies have been
conducted on the natural fiber reinforcements
such as jute [5], abaca [6], animal feathers [7],
kenaf [8], cotton [5], and lemongrass [9], and
their impact on the mechanical properties of
polymer composites; however, the application of
these green composites for 3D printing is still
limited.
The
functionality
of
3D-printed
components largely depends on mechanical
characteristics, and mechanical performance
depends on the characteristics of reinforcement
as well as matrix material and process variables
of FDM [10].
Zandi et al. [11] demonstrated the effect of
varying printing parameters on timberfill (PLA
reinforced with wood fibers) and found infill
density had the largest influence on tensile
strength. Kechagias et al. [12] achieved maximum
strength in tension of 17.42 MPa for PLA
reinforced with coconut flour. Also, this study
indicated no influence of print speed on
mechanical characteristics. Huang et al. [13]
reported that the rounder shape and low surface
roughness value of the wood particle resulted in
a stiffer and stronger 3D-printed wood-plastic
composite. Chaidas and Kechagias [14] examined
the effect of the thickness of the printing layer on
the surface properties of wood/PLA composite. A
lower value of the parameter resulted in
enhanced
surface
finish
and
dimensional
accuracy. The study by Anerao et al. [15]
demonstrates that the incorporation of biochar
significantly enhances the mechanical properties.
Suggesting the potential suitability of the
additively fabricated biochar/PLA biocomposite
for applications demanding higher stiffness and
impact resistance. According to Morales et al.'s
[16]
investigation,
an
early
initiation
of
degradation was seen in a 3D-printed rice husk-
reinforced recycled plastic composite. Sekar et al.
studied the acoustic performance of 3D-printed
wood/PLA composites, but the mechanical
properties were not explored in detail [17].
Maximum strength in tension of 22 MPa was
achieved by Vigneshwaran and Venkateshwaran
with 0.08 mm layer thickness [18]. Sultana et al.
conducted a study on the effect of various FDM
process parameters on the properties of 3D-
printed wood/PLA composites and found that
layer thickness had the largest contribution,
accounting for 69% of the tensile strength [19].
It
is
difficult
to
model
the
complex
mathematical relationships found in the AM
process because of a variety of elements,
including
working
conditions,
processing
parameters, and material qualities. Machine
learning (ML) can detect latent knowledge and
understand hidden patterns to enhance decision-
making in terms of process optimization and
quality control; it presents a promising path for
improving AM operations [20, 21]. By analyzing
vast amounts of data, ML algorithms can find
optimal settings and predict potential problems
before they occur, significantly improving the
efficiency of the additive manufacturing process.
Mishra and Jatti [22] employed a machine
learning algorithm (graph neural networks) to
forecast
the
strength
of
3D-printed
PLA
components under tension, which resulted in a
prediction with 78% accuracy. Mishra et al. [23]
compared the performance of the nine ML
models for predicting the roughness value of the
surface of 3D-printed PLA items, and the result
demonstrates that XGBoost outperformed the
rest of the ML models.
Limited literature is available on prediction
modeling
using
machine
learning
(ML)
algorithms for the mechanical characteristics of
biocomposites that are additively fabricated.
Therefore, this paper offers a novel perspective
by conducting a comparative analysis of various
ML approaches for predicting the mechanical
properties of FDM-based 3D-printed wood/PLA
biocomposite, addressing a gap in the existing
literature.
2. Materials and Methods
2.1. Material, Fabrication, and Testing of
Wood/PLA Biocomposite
Wood-filled
PLA
composite
filament,
composed of 30% wood and 70% PLA, was
procured from 3D Master, Pune, India. CAD
models for each type of testing were created
using SolidWorks and then translated into STL
format. Key FDM process parameters, i.e., infill
pattern (IP), layer thickness (LT), raster angle
(RA), nozzle temperature (NT), and infill density
(ID), were selected for investigation. Three levels
of variations were decided (refer to Table 1), and
using MINITAB software, experiments were
designed, emphasizing Taguchi L27. Table 2
depicts the details of 27 experiment runs and
corresponding process parameters. As per the
Taguchi L27, the process parameters were set in
Kisslicer Slicer software, and G-codes were
generated for each experiment run. The test
specimens were fabricated using the Accucraft
i250+, which is an FDM-based 3D printer (refer
to Fig. 1).


---


## Page 3


Anerao et al. / Mechanics of Advanced Composite Structures 12 (2025) 261 - 270
263
Table 1. Levels of FDM Process parameters in DoE
Parameters
1
2
3
LT (mm)
0.2
0.3
0.4
RA (°)
0
45
90
NT (°)
200
210
220
ID (%)
33.33
50
100
IP
Line
Octagonal
Rounded

Fig. 1. Fabrication of a test specimen using the Accucraft
i250+ 3D printer
Table 2. Experimental design utilizing a Taguchi L27 orthogonal array for Wood/PLA biocomposite mechanical testing.
Experimental
 Run
IP
LT
(mm)
RA
(°)
NT
(°C)
ID
(%)
1
Line
0.2
0
200
33.33
2
Line
0.2
45
220
100
3
Line
0.2
90
210
50
4
Line
0.3
0
220
50
5
Line
0.3
45
210
33.33
6
Line
0.3
90
200
100
7
Line
0.4
0
210
100
8
Line
0.4
45
200
50
9
Line
0.4
90
220
33.33
10
Octagonal
0.2
0
200
50
11
Octagonal
0.2
45
220
33.33
12
Octagonal
0.2
90
210
100
13
Octagonal
0.3
0
220
100
14
Octagonal
0.3
45
210
50
15
Octagonal
0.3
90
200
33.33
16
Octagonal
0.4
0
210
33.33
17
Octagonal
0.4
45
200
100
18
Octagonal
0.4
90
220
50
19
Rounded
0.2
0
200
100
20
Rounded
0.2
45
220
50
21
Rounded
0.2
90
210
33.33
22
Rounded
0.3
0
220
33.33
23
Rounded
0.3
45
210
100
24
Rounded
0.3
90
200
50
25
Rounded
0.4
0
210
50
26
Rounded
0.4
45
200
33.33
27
Rounded
0.4
90
220
100

Figure 2 illustrates the 3D-printed test
specimens for tensile, flexural, and impact tests,
along with the corresponding ASTM standards.
To determine the tensile strength (TS) and tensile
modulus (TM), tests were done following the
ASTM D638 standard. In accordance with the
ASTM D790 standard, flexural strength (FS) and
flexural modulus (FM) were evaluated. For
impact strength (IS), testing was performed as
per the ASTM D256 standard. The various testing
apparatus used for determining the mechanical
properties of the 3-printed wood/PLA test
sample is shown in Fig. 3.

Fig. 2. 3D-printed Wood/PLA biocomposite specimens.


---


## Page 4


Anerao et al. / Mechanics of Advanced Composite Structures 12 (2025) 261 - 270
264

Fig. 3. Apparatus setup for various mechanical testing on
Wood/PLA biocomposite.
2.2. Implementation of Various ML Models for
Prediction Modeling
The results from the experimentation were
carefully
recorded,
and
the
dataset
was
composed
of
the
process
parameters
as
described in Table 2 along with the resulting
mechanical properties tabulated in Excel. For
each experimental run, three samples were
tested to ensure the precision and reproducibility
of the experimental results. Hence, a total of 81
data points were present in the dataset for
machine learning. Machine learning (ML) was
used to create a prediction model for the essential
mechanical properties of the wood/PLA 3D-
printed biocomposite concerning the process
parameters
of
the
FDM
method
under
investigation. Four ML models, namely linear
regression (LR), support vector machine (SVM),
extreme gradient boosting (XGBoost), and
adaptive boosting (AdaBoost), were selected. All
ML algorithms were implemented and executed
using
Google
Colaboratory,
a
cloud-based
platform for running Python code. Each ML
model was systematically applied to the dataset,
considering IP, LT, RA, NT, and ID as feature
variables and UTS, TM, FS, FM, and IS as target
variables. The dataset was split according to the
IP, as it is a categorical variable. Further, the
dataset was subdivided into datasets for training
and testing of the ML model with a proportion of
80% and 20%, respectively using ‘train_test_split’
from the ‘sklearn’ library. A random state of 100
was set to ensure reproducibility.
At first, LR was selected as the prediction
model for this task due to its simplicity and
effectiveness in handling linear relationships.
The module of LR was implemented for the
'sklearn.linear_model'
library.
The
second
algorithm selected was SVM, due to its ability to
handle
high-dimensional
spaces
and
its
resistance to overfitting. The SVR's essential
hyperparameters comprised a linear kernel and a
regularization parameter C of 1.0, which balances
the trade-off between obtaining low error on
training data and minimizing model complexity.
To allow various mechanical properties to be
predicted
at
the
same
time,
a
'MultiOutputRegressor' was used within the
linear kernel of SVM. Next, XGBoost was used
because of its capacity to handle non-linear
correlations
and
feature
interactions.
'RandomizedSearchCV' was used to tune the
model's
parameters
and
improve
its
performance. Lastly, AdaBoost was used for
training and prediction purposes due to its ability
to enhance the performance of weak learners by
combining them into a strong predictive model.
The
‘AdaBoostRegressor’
from
the
'sklearn.ensemble' module was used in this
implementation.
All ML models were trained on the training
dataset (X train and Y train) using the 'fit' method.
Following training, the model was tested on the
test dataset (X test and Y test) by predicting the
target variables. The predicted values from each
ML model were compared with the mean values
obtained from experiments. The coefficient of
determination (R2) values were calculated to
assess the performance of each ML model.
3. Results and Discussions
3.1. Mechanical Testing
Table 3 presents the mean values obtained for
TS, TM, FS, FM, and IS related to each
experimental run. According to the results, the
highest values for all mechanical properties
correspond to 100% infill density. This is because
more material is available to sustain the loading.
An enhancement in mechanical strengths has
been observed for 0.3 mm layer thickness. Using
ANOVA, the significance of each process
parameter
for
mechanical
properties
was
calculated and presented in Table 4. IP, NT, and
RA had insignificant effects on the mechanical
properties. ID appeared as the most important
process parameter, followed by LT.
Table 3. Mechanical properties for each experimental run.
Experimental
Run
UTS
(MPa)
TM
(MPa)
FS
(MPa)
FM
(MPa)
IS
(J/m)
1
29.72±1.64
1027.12±98.82
61.84±3.86
2470.09±943.15
33.33±3.61
2
42.36±0.34
948.87±298.20
82.93±1.04
3659.68±330.18
35.42±3.61
3
26.03±0.50
801.27±51.24
58.51±0.79
2973.49±328.62
33.33±3.61


---


## Page 5


Anerao et al. / Mechanics of Advanced Composite Structures 12 (2025) 261 - 270
265
4
25.62±0.51
638.54±9.36
62.67±2.50
2534.82±187.76
31.25±0.00
5
27.33±2.27
927.77±113.27
57.09±1.35
3214.78±200.06
35.42±3.61
6
36.86±4.18
848.93±46.77
69.65±2.89
3237.49±254.24
44.79±4.77
7
37.94±0.52
727.74±11.39
75.62±0.11
2933.24±577.46
41.67±3.61
8
24.43±1.37
802.00±95.35
59.95±0.84
2931.69±337.06
39.58±1.80
9
25.53±1.46
715.16±267.78
47.49±2.41
2729.46±398.41
37.5±6.25
10
29.57±0.18
1049.06±71.95
57.22±0.56
3356.93±771.56
29.17±3.61
11
28.02±0.22
895.07±77.02
50.87±0.98
2409.34±406.32
31.25±0.00
12
38.48±0.69
851.03±63.01
74.62±1.51
3389.32±219.84
34.38±5.41
13
39.46±1.39
888.36±313.74
83.44±0.56
3725.24±354.65
40.63±3.13
14
27.14±0.78
893.10±43.44
53.49±2.55
2742.45±119.20
39.58±3.61
15
29.31±0.41
719.70±95.68
59.85±0.32
2865.40±172.26
27.08±3.61
16
22.95±0.83
690.85±39.10
50.50±1.82
2677.57±258.00
36.46±4.77
17
37.40±0.16
789.06±19.31
78.51±0.72
3007.53±824.49
42.71±1.80
18
26.16±0.75
752.08±46.95
46.08±0.22
1778.21±329.85
38.54±1.80
19
37.74±5.82
1135.22±98.75
70.30±16.0
3429.52±663.90
37.50±5.41
20
27.82±0.05
963.76±13.53
49.81±0.94
2322.84±387.24
35.42±3.61
21
24.64±0.36
738.80±21.88
56.15±0.42
3570.00±609.49
33.33±3.61
22
24.79±0.36
670.70±11.70
61.80±1.51
3176.69±581.68
29.17±7.22
23
42.46±0.47
817.13±89.16
83.10±1.99
3694.52±570.61
40.63±3.13
24
26.64±1.13
698.36±22.61
62.62±0.63
2497.70±441.79
36.46±4.77
25
24.29±2.38
727.33±165.48
55.20±0.42
2719.85±460.24
33.33±3.61
26
24.29±0.30
680.26±69.52
56.11±0.76
2937.69±547.48
33.33±7.22
27
35.52±0.47
621.70±9.30
70.64±2.19
2974.44±784.22
41.67±1.80
Table 4. Summary of the significance of the process parameter based on ANOVA results.
Source of
Variation
% Significance
on UTS
% Significance
of TM
% Significance
of FS
% Significance
on FM
% Significance
of IS
IP
1
4
1
2
2
LT
5
45
6
10
18
RA
1
13
2
2
5
NT
0
6
2
8
1
ID
88
4
75
36
42
Residual Error
6
28
14
41
33

3.2. Prediction of Mechanical Properties Using
Various ML Models and their Comparison.
Predicted values of various mechanical
properties, i.e., UTS, TM, FS, FM, and IS, using the
linear regression (LR) model are presented in Fig.
4. LR calculates the coefficients to minimize the
difference between predicted and actual values,
assuming a linear relationship exists between
feature and target parameters. As the dataset
lacks linearity, LR did not fully capture the
relationship. As can be seen from Table 5, LR
resulted in lower R2 values for all mechanical
properties.


---


## Page 6


Anerao et al. / Mechanics of Advanced Composite Structures 12 (2025) 261 - 270
266

Fig. 4. Plot of experimental mean vs. predicted values of various mechanical properties by linear regression.
Table 5. R2 comparison: machine learning models and
predicted mechanical properties.
R2
LR
SVM
XGBoost
AdaBoost
UTS
0.8834
0.0639
0.9970
0.9822
TM
0.5904
0.0214
1.0000
0.5495
FS
0.8263
0.0530
0.9990
0.9907
FM
0.5219
0.0392
1.0000
0.6811
IS
0.8367
0.2683
0.9944
0.8650
Figure
5
provides
the
plots
of
the
experimental mean values vs. predicted values by
Support
Vector
Machine
(SVM)
for
each
experimental run. The graph clearly shows that
the predicted values significantly deviate from
the actual values. Based on Table 5, it can be
concluded that SVM with consistently low values
of R2 might not be suitable for capturing complex
relationships present in the dataset.
The plot of experimental values vs. predicted
values by two ensemble learning models, i.e.,
XGBoost and AdaBoost, is presented in Fig. 6 and
Fig. 7, respectively. With very high R2 values
(refer to Table 5), XGBoost provides accurate
prediction for all properties (e.g., UTS, TM, FS, FM,
and IS), making it the most suitable ML model for
the given dataset. AdaBoost effectively leverages
the ensemble approach to improve predictive
accuracy, as seen by high R2 values (refer to Table
5), particularly for UTS and FS.


---


## Page 7


Anerao et al. / Mechanics of Advanced Composite Structures 12 (2025) 261 - 270
267

Fig. 5. Plot of experimental mean vs. predicted values of various mechanical properties by SVM.

Fig. 6. Plot of experimental mean vs. predicted values of various mechanical properties by XGBoost.


---


## Page 8


Anerao et al. / Mechanics of Advanced Composite Structures 12 (2025) 261 - 270
268

Fig. 7. Plot of experimental mean vs. predicted values of various mechanical properties by AdaBoost.
4. Conclusions
Wood/PLA biocomposite, chosen due to its
sustainability,
underwent
a
comprehensive
investigation for mechanization utilizing the
Taguchi
L27
experimental
design.
ANOVA
suggested ID as the predominant FDM process
parameter, followed by LT. ID accounted for 88%
of the variation in ultimate tensile strength (UTS)
and 75% in flexural strength (FS) in the study. A
0.3 mm LT and 100% ID resulted in maximum
tensile, flexural, and impact strengths of 42.46
MPa, 83.43 MPa, and 44.76 J/m, respectively.
With a consistently low R2 score, the SVM model
failed to generalize the complex relationship
between FDM process parameters and the
resulting
mechanical
properties.
Notably,
XGBoost outperformed all other ML models and
achieved the highest R2 values for every
mechanical
property.
XGBoost
effectively
captured
the
intricate
and
non-linear
relationships
in
the
dataset.
This
study
contributes
by
investigating
the
use
of
sustainable materials in additive manufacturing
for commercial applications such as packaging,
transportation, and the automotive industry, and
shedding insight into the important FDM process
parameters that determine its performance.
Further research is required to optimize FDM
process
parameters
to
achieve
enhanced
mechanical properties by employing advanced AI
and ML techniques.
Funding Statement
This research did not receive any specific
grant from funding agencies in the public,
commercial, or not-for-profit sectors.
Conflicts of Interest
The author declares that there is no conflict of
interest regarding the publication of this article.
References
[1] Mazzanti, V., Malagutti, L., and Mollica, F.,
2019. FDM 3D printing of polymers
containing natural fillers: A review of their
mechanical properties. Polymers. 11 (7).
[2] Palaniappan, S.K., Singh, M.K., Rangappa,
S.M., and Siengchin, S., 2024. Eco-friendly
Biocomposites: A Step Towards Achieving
Sustainable Development Goals. Applied
Science and Engineering Progress.


---


## Page 9


Anerao et al. / Mechanics of Advanced Composite Structures 12 (2025) 261 - 270
269
[3] Suyambulingam, I., Rangappa, S.M., and
Siengchin, S., 2023. Advanced Materials and
Technologies for Engineering Applications.
Applied Science and Engineering Progress.
[4] Prajapati, A.R., Dave, H.K., and Raval, H.K.,
2021. Effect of fiber volume fraction on the
impact strength of fiber reinforced polymer
composites made by FDM process. in: Mater
Today Proc, Elsevier Ltd, pp. 2102–2106.
[5] Kurien, R.A., Santhosh, A., Paul, D., Kurup,
G.B., Reji, G.S., and Selvaraj, D.P., 2021. A
Study on Recent Developments in Jute,
Cotton, Coir, Silk and Abaca Fiber-reinforced
Composites. in: pp. 375–384.
[6] Kurien, R.A., Selvaraj, D.P., Sekar, M., Koshy,
C.P., Paul, C., Palanisamy, S., et al., 2023. A
comprehensive review of the mechanical,
physical, and thermal properties of abaca
fiber for their introduction into structural
polymer composites. Cellulose. 30 (14),
pp.8643–8664.
[7] Kurien, R.A., Biju, A., Raj, A.K., Chacko, A.,
Joseph, B., Koshy, C.P., et al., 2023.
Comparative Mechanical Properties of Duck
Feather–Jute
Fiber
Reinforced
Hybrid
Composites. Transactions of the Indian
Institute of Metals. 76 (9), pp.2575–2580.
[8] Kurien, R.A., Santhosh, A., Paul, D., Kurup,
G.B., and Reji, G.S., 2021. A Review on Recent
Developments in Kenaf, Sisal, Pineapple,
Bamboo
and
Banana
Fiber-Reinforced
Composites. in: pp. 301–310.
[9] Kurien, R.A., Preno Koshy, C., Santhosh, A.,
Kurup, G.B., Paul, D., and Susan Reji, G., 2022.
A study on vetiver fiber and lemongrass fiber
reinforced composites. Materials Today:
Proceedings. 68 pp.2640–2645.
[10] Anerao, P., Kulkarni, A., and Munde, Y., 2023.
A review on exploration of the mechanical
characteristics of 3D-printed biocomposites
fabricated by fused deposition modelling
(FDM). Rapid Prototyping Journal.
[11] Zandi, M.D., Jerez-Mesa, R., Lluma-Fuentes, J.,
Jorba-Peiro, J., and Travieso-Rodriguez, J.A.,
2020. Study of the manufacturing process
effects of fused filament fabrication and
injection molding on tensile properties of
composite PLA-wood parts. International
Journal
of
Advanced
Manufacturing
Technology. 108 (5–6), pp.1725–1735.
[12] Kechagias, J.D., Zaoutsos, S., and Chaidas, D.,
2021. Parameter design of PLA/Wood Fused
Filament
Fabrication
using
Taguchi
optimization methodology.
[13] Huang, Y., Löschke, S., and Proust, G., 2021.
In the mix: The effect of wood composition
on the 3D printability and mechanical
performance of wood-plastic composites.
Composites Part C: Open Access. 5.
[14] Chaidas, D. and Kechagias, J.D., 2022. An
investigation
of
PLA/W
parts
quality
fabricated
by
FFF.
Materials
and
Manufacturing Processes. 37 (5), pp.582–
590.
[15] Anerao, P., Kulkarni, A., Munde, Y., Shinde, A.,
and Das, O., 2023. Biochar reinforced PLA
composite for fused deposition modelling
(FDM): A parametric study on mechanical
performance. Composites Part C: Open
Access. 12.
[16] Morales,
M.A.,
Atencio
Martinez,
C.L.,
Maranon, A., Hernandez, C., Michaud, V., and
Porras,
A.,
2021.
Development
and
characterization of rice husk and recycled
polypropylene composite filaments for 3d
printing. Polymers. 13 (7).
[17] Sekar, V., Eh Noum, S.Y., Sivanesan, S., Putra,
A., Chin Vui Sheng, D.D., and Kassim, D.H.,
2021. Effect of Thickness and Infill Density
on Acoustic Performance of 3D Printed
Panels made of Natural Fiber Reinforced
Composites. Journal of Natural Fibers. 00
(00), pp.1–9.
[18] Vigneshwaran, K. and Venkateshwaran, N.,
2019. Statistical analysis of mechanical
properties
of
wood-PLA
composites
prepared
via
additive
manufacturing.
International Journal of Polymer Analysis
and Characterization. 24 (7), pp.584–596.
[19] Sultana, J., Rahman, M.M., Wang, Y., Ahmed,
A., and Xiaohu, C., 2023. Influences of 3D
printing parameters on the mechanical
properties of wood PLA filament: an
experimental analysis by Taguchi method.
Progress in Additive Manufacturing.
[20] Qin, J., Hu, F., Liu, Y., Witherell, P., Wang,
C.C.L., Rosen, D.W., et al., 2022. Research and
application of machine learning for additive
manufacturing. Additive Manufacturing. 52.


---


## Page 10


Anerao et al. / Mechanics of Advanced Composite Structures 12 (2025) 261 - 270
270
[21] Ladani, L.J., 2021. Applications of artificial
intelligence and machine learning in metal
additive manufacturing. JPhys Materials. 4
(4).
[22] Mishra, A., Di Milano, P., and Jatti, V., 2023.
Graph Neural Networks (GNN) for Tensile
Strength
Prediction
in
Additive
Manufacturing.
[23] Mishra, A., Jatti, V.S., Sefene, E.M., and
Paliwal, S., 2023. Explainable Artificial
Intelligence (XAI) and Supervised Machine
Learning-based Algorithms for Prediction of
Surface
Roughness
of
Additively
Manufactured
Polylactic
Acid
(PLA)
Specimens. Applied Mechanics. 4 (2),
pp.668–698.


---
