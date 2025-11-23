# J of Applied Polymer Sci - 2025 - %C3%96zk%C3%BCl - Predicting Mechanical Properties of FDM%E2%80%90Produced Parts Using Machine Learning

> **Source:** `J of Applied Polymer Sci - 2025 - %C3%96zk%C3%BCl - Predicting Mechanical Properties of FDM%E2%80%90Produced Parts Using Machine Learning.pdf`
> **Converted:** 2025-11-22 21:18:11
> **Method:** PyMuPDF

---

## Page 1


1 of 17
Journal of Applied Polymer Science, 2025; 142:e56899
https://doi.org/10.1002/app.56899
Journal of Applied Polymer Science
RESEARCH ARTICLE
OPEN ACCESS
Predicting Mechanical Properties of FDM-­Produced Parts
Using Machine Learning Approaches
Mahmut Özkül1  |  Fatma Kuncan1  |  Osman Ulkir2
1Department of Computer Engineering, Siirt University, Siirt, Turkey  |  2Department of Electric and Energy, Mus Alparslan University, Mus, Turkey
Correspondence: Osman Ulkir (o.ulkir@alparslan.edu.tr)
Received: 7 January 2025  |  Revised: 3 February 2025  |  Accepted: 4 February 2025
Funding: The authors received no specific funding for this work.
Keywords: Mechanical Properties | Surfaces and Interfaces | Thermoplastics
ABSTRACT
Additive manufacturing (AM), especially fused deposition modeling (FDM), has been widely used in industrial production pro-
cesses in recent years. The mechanical properties of parts produced by FDM can be predicted through the correct selection of
printing parameters. In this study, 25 machine learning (ML) algorithms were used to predict the mechanical properties (hard-
ness, tensile strength, flexural strength, and surface roughness) of acrylonitrile butadiene styrene (ABS) samples fabricated by
FDM. Experiments were conducted using three different layer thicknesses (100, 150, 200 μm), infill densities (50%, 75%, 100%),
and nozzle temperatures (220°C, 230°C, 240°C). The effects of printing parameters on mechanical properties were investigated
through analysis of variance (ANOVA). This analysis results indicated that infill density had the most significant effect on hard-
ness (55.56%), tensile strength (80.02%), and flexural strength (77.13%). In addition, the layer thickness was identified as the most
influential parameter on the surface roughness, with an effect of 70.89%. The prediction performance of the ML algorithms was
evaluated based on the mean absolute error (MAE), root mean squared error, mean squared error, and R-­squared (R2) values.
The KSTAR algorithm best predicted both hardness and surface roughness, with MAE values of 0.006 and 0.009, respectively,
and an R2 value of up to 0.99. For the prediction of tensile and flexural strength, the MLP algorithm was determined to be the
most successful method, achieving high accuracy (R2 > 0.99) for both properties. In addition, comparison graphs between the
predicted and actual results showed high overall accuracy, with a particularly strong agreement for hardness, tensile strength,
and surface roughness. The study identified the algorithms with the best prediction performance and provided recommendations
for predicting the 3D printing process based on these findings.
1   |   Introduction
Additive manufacturing (AM) is a rapidly advancing production
technology that has gained traction across various industrial
fields in recent years [1, 2]. This technology enables the fabri-
cation of parts by adding layers, allowing for the cost-­effective
production of complex geometries compared with traditional
manufacturing methods. The flexibility and design freedom
offered by AM have led to its widespread application, partic-
ularly in the fields of prototyping, automotive, aerospace, and
medicine [3–6]. However, realizing the full potential of AM re-
quires a precise determination of the production parameters and
an understanding of how they affect the mechanical properties
of the parts [7]. In this regard, optimizing production parame-
ters based on their effects can lead to improved product quality
and cost efficiency [8].
Fused deposition modeling (FDM), an AM technique, is espe-
cially favored for its compatibility with thermoplastic materials
[9–11]. FDM has gained significant traction in the industrial
This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is
properly cited.
© 2025 The Author(s). Journal of Applied Polymer Science published by Wiley Periodicals LLC.


---


## Page 2


2 of 17
Journal of Applied Polymer Science, 2025
and academic sectors because of its relatively low cost, wide
material range, and broad applicability—from prototype pro-
duction to functional part fabrication [12, 13]. The materials
commonly used in FDM are thermoplastic polymers, with
high-­performance engineering materials such as acrylonitrile
butadiene styrene (ABS), polylactic acid (PLA), and polyeth-
ylene terephthalate glycol (PETG) being among the most widely
utilized [14, 15]. FDM is a technology in which the production
parameters play a critical role in the print quality and mechani-
cal properties [16, 17]. Factors like layer thickness, infill density
(ID), and nozzle temperature (NT) directly affect the print qual-
ity and mechanical characteristics of the final product [18, 19].
Mechanical properties such as hardness, tensile strength, flex-
ural strength, and surface roughness can be optimized through
proper adjustment of these parameters [20–22]. In contrast, in-
correct parameter selection can lead to print errors, low strength
values, and a decrease in overall product quality. Optimizing
printing parameters in FDM technology is crucial for mini-
mizing print time and cost while ensuring that the mechanical
properties meet expectations [23]. Therefore, each printing pa-
rameter directly influences the performance of the final prod-
uct, and optimizing these parameters enables FDM to be used
more effectively across a wide range of applications.
In recent years, machine learning (ML) methods have become
valuable tools for predicting and optimizing AM processes
[24–26]. ML enables more accurate modeling of the manufac-
turing process by working with large datasets and can predict
the effects of specific parameters (such as print speed [PS], layer
height [LH], and NT) on the final properties of products. This ap-
proach makes it possible to enhance process efficiency by reduc-
ing production time, minimizing material waste, and lowering
energy consumption. ML techniques can understand complex
data relationships, learn the dynamics of processes, and forecast
future outcomes without human intervention [27]. This ability is
particularly valuable in AM processes, where parameters have
a direct impact on mechanical properties and numerous factors
interact simultaneously. Consequently, ML helps improve prod-
uct quality, reduces production costs, and optimizes processes,
thereby facilitating the adoption of economically and environ-
mentally sustainable manufacturing methods.
Studies on the application of ML algorithms in AM demonstrate
the effectiveness of these technologies in optimizing production
processes [28–32]. Cerro et al. applied ML algorithms to predict
the surface roughness of parts produced by FDM using polyvi-
nyl butyral material [33]. Five input variables were determined,
and 16 parts were 3D printed with three different surfaces; the
surface roughness was then measured. A total of 40 models were
trained and validated, with the best results obtained using bag-
ging and a backpropagation multi-­layer perceptron. Raster angle
and LH were identified as the most influential parameters on sur-
face quality. Hooda et al. employed a random forest ML model to
predict the ideal placement angle in FDM based on product ge-
ometry [34]. Training data were created using different shapes
and geometries, and significant features were selected using a
correlation-­based feature selection technique. The model's ef-
fectiveness was tested using K-­fold cross-­validation, achieving
94.57% accuracy. Winson et al. investigated the 3D printing of
PLA composites reinforced with 4.6 mm chopped carbon fiber
(CF) using FDM [35]. As the CF content increased, properties
such as tensile and flexural strength, hardness, and thermal con-
ductivity improved significantly compared with pure PLA. The
performance exhibited a rise-­fall-­rise trend with CF addition,
and Gaussian process modeling predicted the optimal CF con-
tent of 6.7 wt%, which was closely aligned with the experimental
results. Charalampous et al. aimed to develop a new parameter
selection method to improve the dimensional accuracy of FDM-­
produced parts [36]. Using ML algorithms, the method predicts
the dimensional deviations between the CAD models and the
fabricated parts. Experiments conducted under various print-
ing conditions demonstrated the effectiveness of the regression
models in suggesting print settings and correcting errors. This
study presents the first ML-­based regression models and correc-
tion strategies for assessing and improving FDM process qual-
ity. Ulkir used carbon black-­filled ABS material for 3D printing
using the FDM process [37]. Tensile tests were conducted to de-
termine the mechanical strength, whereas resistance tests were
carried out to assess electrical conductivity. Factors affecting
strength included ID and LH; infill pattern (IP); for electrical re-
sistance, significant factors were length, NT, and measurement
temperature. The data were analyzed, and predictive models for
tensile strength and electrical resistance were developed using
Gaussian process regression and support vector machine algo-
rithms. Results revealed a linear relationship between electrical
resistance and length, as well as the impact of manufacturing
settings on mechanical strength. However, while these studies
provide valuable insights, many focus on limited ML algorithms
or specific mechanical properties, such as surface roughness or
dimensional accuracy, without comprehensively exploring other
key properties like tensile or flexural strength. Moreover, the in-
teraction effects of critical printing parameters, such as LH, ID,
and NT, remain underexplored in the context of multi-­property
optimization. The potential research gap lies in the need for a
broader analysis of ML algorithms across multiple mechanical
properties and their ability to predict the combined effects of di-
verse printing parameters. While existing studies demonstrate
the feasibility of ML in AM, the lack of a comprehensive evalua-
tion of multiple algorithms for simultaneous prediction of prop-
erties such as hardness, tensile strength, flexural strength, and
surface roughness represents a critical gap. This study seeks to
address this gap by employing 25 different ML algorithms to pre-
dict these properties and by analyzing the impact of key printing
parameters using analysis of variance (ANOVA). The rationale
behind this work is to provide a more holistic understanding of
the predictive capabilities of ML in AM, establish recommenda-
tions for algorithm selection, and optimize printing processes to
improve the quality and reliability of FDM-­produced ABS parts.
This approach builds upon existing literature while filling the
identified research gap through a systematic and comprehensive
evaluation.
This study aimed to predict the mechanical properties, such as
hardness, flexural strength, tensile strength, and surface rough-
ness, of ABS samples produced using the FDM. Experiments
were conducted by selecting the printing parameters of layer
thickness, ID, and NT to achieve this goal. The effects of these
parameters on the mechanical properties and roughness were
statistically evaluated using ANOVA. Data obtained from the ex-
periments were modeled using 25 different ML algorithms, and
the prediction performances of these algorithms were assessed
based on the mean absolute error (MAE), root mean squared
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 3


3 of 17
error (RMSE), mean squared error (MSE), and R-­squared (R2)
values. The algorithms with the best prediction performance
were identified, and optimization recommendations for the 3D
printing process were provided considering these results.
2   |   Materials and Methods
2.1   |   AM Process
In this study, the fabrication of tensile and flexural test specimens
was performed using the FDM method. This method is a widely
used AM technique that enables the physical production of 3D
models by heating and extruding thermoplastic materials through
a nozzle layer by layer [38]. The printer used in the production
process was a Creality K1C model (Figure 1c). This 3D printer is
known for its high printing speed and precision. With a maximum
printing speed of 600 mm/s and a melt extrusion rate of 32 mm3/s,
this printer allows for the rapid and accurate production of com-
plex geometries. The NT of the printer can reach up to 300°C, and
the build platform can be heated up to 100°C, providing a compat-
ible environment for a wide range of materials. In this study, the
material used was ABS, selected for its high durability, hardness,
and heat-­resistance properties [39, 40].
The tensile test specimens were designed in accordance with
the ASTM D638 standard (Figure 1a). This standard specifies
the dimensions and geometric characteristics of specimens
used in tensile tests. The specimens were modeled in 3D using
SolidWorks software, and the models were exported in standard
triangle language (STL) format. This format records the surface
geometry by triangulating the model and aids in generating the
layered structure necessary for 3D printing. The STL file was
then transferred to the slicing software, and parameters such as
LT, PS, and NT were defined. Following the slicing process, a G-­
code file was generated, which controls the printer's movement
paths and material flow. Using this G-­code file, the 3D printer
melted the ABS material at the specified temperature and pro-
duced the tensile test specimens' layer by layer in accordance
with the ASTM D638 standard. The flexural test specimens
were designed in accordance with the ASTM D790 standard
(Figure 1b). This study also examines other mechanical prop-
erties, including hardness and surface roughness, using tensile
test specimens. Twenty-­seven test specimens were produced for
each mechanical property according to experimental design. All
samples were printed on the XY plane and loaded in the Z di-
rection. Based on the design of experiments approach, variable
3D printing parameters and levels were determined. In addition,
other parameters were kept constant during the production
process. The constant 3D printing parameters are detailed in
Table 1.
2.2   |   Measurement of Mechanical Properties
In the ML process, four mechanical properties were examined
as output parameters: tensile strength, flexural strength, hard-
ness, and surface roughness. Mechanical measurements were
conducted on the ABS material produced using FDM. The tensile
strength refers to the maximum amount of stress a material can
withstand without breaking under tension. Tensile tests were per-
formed on a 50-­kN capacity AG-­X Shimadzu device according to
ASTM D638 standards at a pull speed of 1 mm/s. This device com-
plies with ISO 7500/1, ASTM E4, and DIN51221 standards and
provides results with ± 0.1% accuracy. Flexural strength refers to
the maximum stress a material can withstand when bending with-
out breaking. Flexural tests were conducted on a 50-­kN capacity
AGS-­X Shimadzu device, following ASTM D790 standards. The
three-­point bending method was applied using a fixed diameter
mandrel and supports. ABS samples were bent at a speed of 1 mm/s
using the mandrel. Hardness refers to a material's resistance to an
applied force on its surface, typically related to its resistance to
scratching or permanent deformation. Hardness measurements
FIGURE 1    |    The sample dimensions (mm) and FDM-­based 3D printer. [Color figure can be viewed at wileyonlinelibrary.com]
TABLE 1    |    The constant 3D printing parameters during AM.
Parameter
Unit
Value
Nozzle diameter
mm
0.4
Table temperature
°C
90
Number of contours
integer
7
Raster width
mm
0.40
Infill pattern
—
Grid
Printing speed
mm/s
90
Wall thickness
mm
3
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 4


4 of 17
Journal of Applied Polymer Science, 2025
were taken with a TRONIC PD-­801 Analog Shoremeter, which
is capable of measuring on the Shore D scale. According to the
ASTM standards, measurements were taken from five points on
both the top and bottom surfaces of the samples. The average of
these values with a 1 kg/cm2 (9.8 N) applied pressure on the surface
was used to calculate the general hardness value. Surface rough-
ness defines microscopic irregularities or small-­scale protrusions
and depressions on the surface. Surface roughness measurements
were completed using the Mitutoyo Surftest SJ-­210 device with a
sampling length of 2.5 mm and measurement speed of 0.75 mm/s.
Five measurements were performed for each sample. These
tests provided reliable results by ensuring repeatability through
multiple-­point measurements, which helped analyze the mechan-
ical and surface properties of the ABS material.
2.3   |   Design of the Experiment
In AM processes, the printing parameters significantly affect the
mechanical properties of the final product components. In this
study, the three most important parameters affecting the mechan-
ical properties were selected. These are LT, ID, and NT. LT refers
to the height of each printed layer in the 3D printing and AM pro-
cesses [41]. ID is a ratio that determines how solid or empty the
interior of an object will be in 3D printing [42]. NT indicates the
temperature at which the molten material is heated before being
applied to the print surface in 3D printers [43]. These parameters
were used as input variables in the ML implementation. Three lev-
els were defined for each parameter. The other 3D printer param-
eters required for the manufacturing process were kept constant
throughout the experimental stages. The input parameters and
their level values for the ML algorithm are listed in Table 2.
Experimental combinations were created based on the identi-
fied input and output parameters. The present study includes
three factors, each with three levels, resulting in 27 experimen-
tal runs. The data set prepared for the ML algorithm is presented
in Table 3. Each output parameter in the proposed dataset rep-
resents an average of five repeated measurements for improved
accuracy and reliability.
3   |   ML Methodology
3.1   |   Methods of Prediction
ML is the capability of a program to learn from new data and
adapt without human intervention [44, 45]. An ML model an-
alyzes the relationship between process factors and outputs. In
this study, regression strategies were employed to perform com-
putations aimed at predicting the output responses obtained
through 3D printing, namely hardness, tensile strength, surface
roughness, and flexural strength. ML methods are classified
into five main groups: functional algorithms, lazy learning al-
gorithms, meta-­learning algorithms, rule-­based algorithms, and
tree-­based algorithms. Table 4 lists the full names of the 25 ML
algorithms considered in this study.
The dataset created for the ML algorithms comprises three inputs
and four outputs (Table 3). The datasets for the output parameters
are stored in separate files. In this study, the Waikato environment
for knowledge analysis (WEKA) software was used for the ML im-
plementation. WEKA is a Java-­language ML tool for implement-
ing algorithms, data analysis, and data mining tasks [46]. Once
the dataset was loaded into WEKA, fundamental statistics, such
as minimum and maximum values, mean, and standard devia-
tion, were computed. Subsequently, subsets of the data were tested
using all applicable regression algorithms available in WEKA. The
methodology for ML is illustrated in Figure 2. This diagram sum-
marizes the process of output prediction and accuracy evaluation
using an ML-­based regression method for 3D-­printed materials.
Initially, the input data and properties of the 3D-­printed material
are used as inputs for the model. These data are processed through
the ML regression method to produce the predicted output. The
results predicted by the model are then compared with actual ex-
perimental data to evaluate accuracy. This process enhances the
predictive power and performance of the model.
3.2   |   Proposed ML Algorithm
In this study, an ML model was proposed to predict various me-
chanical properties (hardness, tensile strength, surface roughness,
and flexural strength) using critical printing parameters (LT, ID,
and NT) in the 3D printing process. The methodology adopted for
the ML process is illustrated in Figure 3. Initially, the data were
normalized between 0 and 1 to enhance classification efficiency.
Normalization involves scaling all data values to a specific range,
typically to minimize differences in scale among variables and im-
prove algorithm performance. Following normalization, the data
selection phase was conducted, during which training and testing
datasets were prepared. A 10-­fold cross-­validation technique was
applied at this stage to ensure balanced separation between the
training and test datasets, thereby enhancing the reliability and
accuracy of the results. In this study, 75% of the data was allocated
for training, while the remaining 25% was reserved for testing.
Subsequently, ML algorithms were employed with 25 regression
algorithms. A performance analysis was conducted to evaluate the
effectiveness of the proposed algorithms, ensuring a comprehen-
sive comparison of their predictive capabilities.
3.3   |   Performance Evaluation Metrics
Performance analysis is the process used to evaluate the per-
formance of a model and its ability to generalize. This involves
various metrics and methods to assess, compare, and optimize
the outcomes obtained during the training and testing phases
of the models. In this study, the evaluation metrics applied to
the regression models include the MSE, RMSE, MAE, and R2.
The MSE was calculated by taking the average of the squared
TABLE 2    |    Input parameters and level values of the ML algorithm.
Parameter
Symbol
Units
Level 1
Level 2
Level 3
Layer
thickness
LT
(μm)
100
150
200
Infill density
ID
%
50
75
100
Nozzle
temperature
NT
(°C)
220
230
240
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 5


5 of 17
differences between the predicted and actual values. This cal-
culation emphasizes the magnitude of errors by squaring the
differences, which penalizes larger errors more heavily. A lower
MSE value indicates that the model's predictions are closer to
the actual values, which indicates better performance. However,
due to the squared units of the MSE, its interpretation can be
challenging; therefore, the square root of the MSE (RMSE) is
often used for easier interpretation and comparison.
The MAE is calculated by averaging the absolute differences be-
tween the predicted and actual values. After summing the abso-
lute differences, the total is divided by the number of data points
to obtain the average error. Unlike MSE, MAE does not penal-
ize larger errors more heavily; each error contributes equally,
regardless of its magnitude. Therefore, the MAE is particularly
suitable in scenarios in which penalizing large errors is not de-
sirable. A lower MAE value indicates that the model's predic-
tions are closer to the actual values.
(1)
MSE = 1
n
n
∑
i=1
(yi −̂yi
)2
(2)
MAE = 1
N
N
∑
i=1
||yi −̂yi||
TABLE 3    |    Measured responses: Dataset for the experiments.
No
Input parameters
Output parameters
Layer
thickness
(μm)
Infill
density (%)
Nozzle
temperature
(°C)
Hardness
Flexural
strength
(MPa)
Tensile
strength
(MPa)
Roughness
(μm)
1
100
50
220
47.63
34.48
25.76
12.87
2
100
50
230
50.68
36.15
26.95
14.08
3
100
50
240
54.08
37.82
28.35
15.46
4
100
75
220
52.13
40.43
31.05
12.18
5
100
75
230
56.10
42.36
32.79
13.38
6
100
75
240
59.81
44.32
34.52
14.65
7
100
100
220
57.39
47.49
38.01
11.59
8
100
100
230
61.23
49.53
40.06
12.65
9
100
100
240
65.21
51.62
42.57
13.85
10
150
50
220
44.29
31.98
23.95
15.46
11
150
50
230
47.06
33.39
24.36
16.89
12
150
50
240
50.03
34.78
25.49
18.43
13
150
75
220
48.86
37.63
28.03
14.68
14
150
75
230
52.15
39.28
29.45
16.12
15
150
75
240
55.47
40.96
30.89
17.65
16
150
100
220
54.26
43.75
34.57
13.97
17
150
100
230
57.68
45.68
36.62
15.32
18
150
100
240
61.43
47.59
38.54
16.83
19
200
50
220
41.95
30.18
21.47
17.79
20
200
50
230
44.58
31.38
22.59
19.52
21
200
50
240
47.49
32.65
23.68
21.35
22
200
75
220
46.37
35.08
26.29
16.89
23
200
75
230
49.35
36.69
27.58
18.59
24
200
75
240
52.57
38.29
28.83
20.35
25
200
100
220
51.29
40.85
32.24
16.12
26
200
100
230
54.68
42.65
33.95
17.68
27
200
100
240
58.09
44.56
35.89
19.45
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 6


6 of 17
Journal of Applied Polymer Science, 2025
The RMSE was computed as the square root of the mean of the
squared differences between the predicted and actual values.
This metric highlights the magnitude of errors by squaring the
differences and subsequently takes the square root to ensure
that the error units are consistent with the original data. A lower
RMSE value indicates that the model's predictions are closer to
the actual values, which reflects better model performance. The
RMSE is intuitive and straightforward to interpret, making it a
widely used measure for understanding the magnitude of pre-
diction errors.
The R2 coefficient, also known as the coefficient of determina-
tion, is a performance metric that indicates how well a model
explains the variability of the dependent variable. R2 measures
how accurately predicted values approximate actual values. It
takes a value between 0 and 1, where values closer to 1 indicate
that the model explains a larger portion of the variability in the
dependent variable. An R2 value of 1 implies that the model per-
fectly explains all variability, whereas an R2 value of 0 indicates
that the model fails to explain any variability.
4   |   Results and Discussion
4.1   |   ANOVA Results
In this study, ANOVA was applied to investigate the relationship
between input printing parameters, such as LT, ID, and NT, and
output parameters, such as hardness, flexural strength, tensile
strength, and roughness. ANOVA is a statistical test used to un-
derstand the effects of independent variables on dependent vari-
ables. This analysis was used to evaluate the influence of each
input parameter on the output parameters (Table 5). The F-­test
and p-­value were examined. The F-­test measures the contribu-
tion of each variable to the variance of the model and determines
whether the effects of the input parameters are significant. A
high F value indicates that the parameter has a significant im-
pact on the dependent variable. The p-­value, on the other hand,
is used to statistically assess this impact. Generally, if the p-­
value is below 0.05, the parameter has a statistically significant
effect on the output parameter. As a result of this analysis, the
significant effects of input parameters on outcome variables
were evaluated, and the relationships between these parameters
were elucidated.
When examining the p-­values, the selected printing param-
eters were highly significant in terms of their impact on the
mechanical properties and surface roughness. However, due
to differences in F-­values, the contribution levels of these pa-
rameters substantially vary. The calculated contribution val-
ues for each parameter are presented in Table 6. For the Shore
D hardness parameter, the most influential factor was ID,
which contributed 55.56%. Similar results were observed for
the flexural strength and tensile strength parameters, where
the ID was again identified as the most impactful factor. In
contrast, for the roughness parameter, the most significant
factor was the LT, which contributed 70.89%, while the ID had
the lowest impact.
Regression coefficients and effect signs derived from the
ANOVA results were used to determine whether a factor
has a positive (enhancing) or negative (diminishing) effect
(Equations (5–8)). The model aims to identify the main and
interactional effects of printing parameters on mechani-
cal properties. In regression models, positive coefficients
indicate that an increase in the associated model terms en-
hances the parameter, whereas negative coefficients suggest
that an increase in these terms reduces the parameter. The
model in Equations  (5–7) show that the positive coefficient
values for ID and NT imply a gradual increase in hardness,
flexural strength, and tensile strength from lower to higher
levels. Conversely, because the LT parameter has a negative
coefficient, its increase reduces the mechanical properties. In
(3)
RMSE =
√
√
√
√1
n
n
∑
i=1
(yi −̂yi
)2
(4)
R2 = 1 −
∑yi −̂yi
2
∑
yi −y
2
TABLE 4    |    Full forms of all algorithms.
Algorithm
Full form
LR
Linear regression model
GP
Gaussian process
MLP
Multi-­layer perceptron
SLR
Simple linear regression
SMOREG
Sequential minimal optimization regression
IBK
Instance-­based K (K-­Nearest neighbors)
KSTAR
K* (instance-­based learner)
LWL
Locally weighted learning
AR
Association rules
BAGGİNG
Bootstrap aggregating
CVP
Cross-­validation predictor
MS
Model selection
RC
Ridge classifier
RFC
Random forest classifier
RSS
Random subspace
RBD
Reduced error pruning decision tree
IMC
Iterative model construction
DT
Decision tree
M5R
M5’ rules
ZeroR
Zero rule
DS
Decision stump
M5P
M5’ model tree
RandomF
Random forest
RandomT
Random tree
RepTree
Reduced error pruning tree
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 7


7 of 17
Equation (8), it is observed that an increase in the LT parame-
ter results in higher surface roughness.
4.2   |   Error Performance Metrics Results
In this section, the prediction performances of various ML algo-
rithms on four different output parameters are compared using
the MAE, MSE, and RMSE values (Table 7). MAE represents
the average of the absolute differences between the predicted
and actual values, while MSE squares the errors, penalizing
larger errors more heavily. The RMSE is calculated by taking
the square root of the MSE, thereby emphasizing the magnitude
of the errors.
The algorithm with the lowest error rate was KSTAR for
Shore D hardness prediction. This algorithm achieved the
best performance, with both an MAE of 0.0066 and an RMSE
of 0.0101, indicating highly accurate predictions for hardness.
MLP (MAE: 0.1662, RMSE: 0.1991) and SMOREG (MAE:
0.1572, RMSE: 0.2245) also produced successful results with
low error rates. However, the cross-­validation predictor (CVP),
MS, and ZeroR algorithms performed the worst, with both the
MAE and RMSE values exceeding 6, indicating poor predic-
tion accuracy.
In the flexural strength prediction, the best performances were
obtained by the MLP and RSS algorithms. MLP (MAE: 0.1874,
RMSE: 0.2202) and SMOREG (MAE: 0.1977, RMSE: 0.3013)
demonstrated successful performance with low error values
for flexural strength prediction. Although KSTAR provided
excellent results for hardness prediction, it was less successful
for flexural strength, with an RMSE value exceeding 1. Again,
CVP, MS, and ZeroR demonstrated the worst performance, with
RMSE values greater than 6.
The best results were again obtained by MLP (MAE: 0.3325,
RMSE: 0.3977) and SLR (MAE: 0.3371, RMSE: 0.4165) algo-
rithms for tensile strength predictions. KSTAR, however, showed
higher error rates in this category, with an RMSE of 1.3541,
falling behind the other algorithms. CVP, MS, and ZeroR once
again had the highest error rates, with CVP reaching an RMSE
of 5.9294, indicating poor performance in tensile strength pre-
diction. The most successful roughness prediction algorithm was
KSTAR (MAE: 0.013, RMSE: 0.0172), which exhibited very low
error rates, indicating outstanding performance in roughness
prediction. MLP (MAE: 0.046, RMSE: 0.059) also showed strong
performance, with very low error values. In contrast, ZeroR,
CVP, and MS demonstrated the worst performance, with RMSE
values as high as 2.6115, indicating poor accuracy in roughness
predictions. In conclusion, the MLP and KSTAR algorithms con-
sistently achieved successful results across multiple parameters
with low MAE, MSE, and RMSE values. In contrast, algorithms
like CVP, MS, and ZeroR generally exhibit high error rates and
the lowest prediction performance. The best-­performing algo-
rithms for each output are indicated in bold in Table 7. These
results emphasize the significant impact of selecting an appro-
priate algorithm on model prediction accuracy.
The MAE and MSE values obtained from ML algorithms have
been graphically presented for better representation. The first
four graphs illustrate the MAE values (Figure  4a–d). In the
hardness and roughness predictions, the MLP and KSTAR algo-
rithms demonstrated low error rates, whereas the CVP, ZeroR,
and IMC algorithms exhibited the highest error rates. For the
flexural and tensile strengths, MLP and SMOREG demonstrated
successful performance with low error rates, whereas CVP and
ZeroR demonstrated the worst performance with high error
rates. The last four graphs depict the MSE values (Figure 4e–h).
MLP and KSTAR algorithms emerged as successful algorithms
with very low error rates across all parameters. CVP, MS, and
ZeroR exhibit the worst performance, consistently showing high
MSE values across all four parameters. The KSTAR algorithm
achieved the best hardness predictions with an MAE of 0.0066
and an MSE of 0.0001. Similarly, the roughness results were
most accurately predicted using the KSTAR algorithm, with an
MAE of 0.013 and an MSE of 0.0003. The best predictions for the
flexural and tensile strengths were made by the MLP algorithm.
(5)
Hardness=
−29.95−0.064 LayerThickness+0.207Infill Density
+0.33NozzleTemperature
(6)
FlexuralStength=
−9.4−0.05LayerThickness+0.24InfillDensity
+0.17NozzleTemperature
(7)
TensileStength=
−14.8−0.05LayerThickness+0.24InfillDensity
+0.15NozzleTemperature
(8)
Roughness=
−23.2+0.052LayerThickness−0.031InfillDensity
+0.147NozzleTemperature
FIGURE 2    |    Method of ML for 3D printed material. [Color figure can be viewed at wileyonlinelibrary.com]
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 8


8 of 17
Journal of Applied Polymer Science, 2025
The MAE and MSE values for the flexural strength were 0.1874
and 0.048, respectively, while those for the tensile strength were
0.3325 and 0.158. These results indicate that MLP and KSTAR
are the most successful algorithms for predicting mechanical
properties and surface roughness, achieving the lowest error
rates across these metrics, whereas simpler algorithms like
ZeroR and CVP demonstrate poor predictive performance.
4.3   |   Coefficient of Determination Results
In this section, the performance of various ML algorithms for
four criteria (hardness, flexural strength, tensile strength, and
roughness) is compared using the coefficient of determination
(R2) values. The results are presented in Table 8. The R2 values
indicate the proportion of variance in the dependent variable
FIGURE 3    |    The proposed machine learning flowchart.
TABLE 5    |    ANOVA results for input–output parameters.
Factors
Hardness
Flexural strength
Tensile strength
Surface roughness
F
p
F
p
F
p
F
p
Layer thickness
627.83
0.000
328.21
0.000
202.92
0.000
1337.73
0.000
Infill density
1626.68
0.000
1494.56
0.000
1079.05
0.000
125.17
0.000
Nozzle temperature
670.32
0.000
114.53
0.000
66.66
0.000
423.69
0.000
Degree of freedom
26
26
26
26
TABLE 6    |    Contribution values of ANOVA results.
Factors
Hardness
Flexural strength
Tensile strength
Surface r+oughness
Layer thickness
21.48%
16.94%
15.05%
70.89%
Infill density
55.56%
77.13%
80.02%
6.63%
Nozzle temperature
22.92%
5.91%
4.94%
22.47%
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 9


9 of 17
explained by the model. An R2 value closer to 1 indicates a
better-­fitting model.
The hardness values indicate that the highest performance
was achieved by the KSTAR algorithm (0.9997), followed
closely by MLP, SMOREG, and M5P algorithms. These algo-
rithms are highly successful in Shore D hardness prediction.
On the other hand, the performance of algorithms such as
IBK, ZeroR, and MS was considerably low, as their R2 values
were below 0.5. For flexural strength, the most successful al-
gorithm was the MLP with an almost perfect result (0.9999).
Other algorithms like M5R and SMOREG, also exhibit very
high performance. However, the performance of algorithms
such as IMC and ZeroR, on this metric is quite poor. In terms
of tensile strength, MLP again delivers the best result, while
the KSTAR, M5P, and RBD algorithms also demonstrate
similarly high tensile strength. In contrast, LWL, CVP, and
ZeroR yield relatively low results for this metric. Regarding
roughness, the KSTAR (0.9999) and MLP (0.9940) algorithms
were the best. The LR, SMOREG, and M5P algorithms also
performed well on this metric. However, the performance of
algorithms like ZeroR, LWL, and IMC is subpar.
MLP, SMOREG, M5P, and KSTAR perform exceptionally well
across all four metrics, while ZeroR, IMC, and LWL demon-
strate low performance on some metrics. When comparing the
results of MAE, MSE, and RMSE with the R2, the most success-
ful prediction algorithms remain consistent. This consistency
indicates the success of the modeling and prediction processes.
The results suggest that more complex models generally yield
better results in regression problems, although simpler models
may still be adequate in certain cases. The regression graphs of
the algorithms that successfully predicted the output parame-
ters are presented in Figure 5. Although KSTAR was successful
TABLE 7    |    MAE, MSE, and RMSE of all algorithms.
Algorithms
Hardness
Flexural strength
Tensile strength
Roughness
MAE
MSE
RMSE
MAE
MSE
RMSE
MAE
MSE
RMSE
MAE
MSE
RMSE
LR
0.2346
0.088
0.2982
0.2909
0.125
0.3543
0.3744
0.211
0.4594
0.162
0.0368
0.1919
GP
1.8954
5.179
2.2759
1.7489
4.666
2.1602
1.8395
4.822
2.196
0.813
0.9577
0.9786
MLP
0.1662
0.039
0.1991
0.1874
0.048
0.2202
0.3325
0.158
0.3977
0.046
0.0035
0.059
SLR
1.3512
2.509
1.584
0.3454
0.181
0.4264
0.3371
0.173
0.4165
1.167
1.9063
1.3807
SMOREG
0.1572
0.050
0.2245
0.1977
0.090
0.3013
0.3392
0.202
0.4497
0.141
0.0344
0.1854
IBK
3.2633
10.82
3.2899
1.7033
2.967
1.7225
1.4948
2.463
1.5696
1.452
2.1583
1.4691
KSTAR
0.0066
0.0001
0.0101
0.9315
1.345
1.1621
1.041
1.833
1.3541
0.013
0.0003
0.0172
LWL
3.0243
11.939
3.4553
2.5271
8.999
2.9999
2.4408
8.502
2.9159
1.463
3.0026
1.7328
AR
2.3682
0.6381
0.7988
1.6927
4.927
2.2197
1.8009
4.113
2.0282
0.670
7.221
2.6872
BAGGİNG
2.4192
8.0236
2.8326
1.3807
3.664
1.9144
1.3335
3.455
1.859
1.213
2.2819
1.5106
CVP
5.0443
36.709
6.0588
5.1689
36.99
6.0825
5.0788
35.15
5.9294
2.204
6.8199
2.6115
MS
4.7031
36.709
6.0588
5.1689
36.99
6.0828
5.0788
35.15
5.9294
2.204
6.8199
2.6115
RC
1.9232
5.1475
2.2688
1.2042
2.068
1.4381
1.1517
1.808
1.3448
1.391
2.5751
1.6047
RFC
3.3833
11.688
3.4188
2.4733
8.768
2.9611
2.2015
7.503
2.7392
1.498
2.4264
1.5577
RSS
1.1265
2.0076
1.4169
0.4636
0.515
0.7071
0.6299
0.766
0.8755
1.096
1.7022
1.3047
RBD
0.8412
1.1597
1.0769
0.5518
0.444
0.6668
0.7218
0.730
0.8549
0.661
0.7211
0.8492
IMC
5.0443
36.709
6.0588
5.1689
36.99
6.082
5.0788
35.15
5.9294
2.204
6.8199
2.6115
DT
2.2122
7.0671
2.6584
1.5895
3.962
1.9905
1.477
3.320
1.8222
0.809
0.9716
0.9857
M5R
0.3489
0.1982
0.4452
0.2836
0.134
0.3664
0.3656
0.209
0.4582
0.365
0.2657
0.5155
ZeroR
5.0443
36.709
6.0588
5.1689
36.99
6.082
5.0788
35.15
5.9294
2.204
6.8199
2.6115
DS
3.6173
18.630
4.3163
2.6411
10.295
3.2087
2.7295
10.70
3.2724
1.793
4.4192
2.1022
M5P
0.3489
0.1982
0.4452
0.2836
0.1342
0.3664
0.3539
0.195
0.4423
0.372
0.2674
0.5171
RandomF
1.8989
5.0922
2.2566
0.8232
1.281
1.1318
0.8737
1.455
1.2066
1.168
1.9864
1.4094
RandomT
3.0324
11.337
3.3671
1.9256
5.790
2.4064
1.8778
4.766
2.1833
1.364
2.5132
1.5853
RepTree
3.0506
12.022
3.4674
1.9009
5.349
2.3129
2.3121
7.046
2.6546
1.392
2.7569
1.6604
Note: Bold values ​represent the algorithms with the lowest error values ​for each output parameter.
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 10


10 of 17
Journal of Applied Polymer Science, 2025
in predicting hardness and surface roughness, MLP performed
best for the flexural and tensile strength parameters. The re-
gression graph is a critical tool for evaluating the accuracy and
explaining the variability of prediction models. These graphs
help analyze model performance by visualizing how closely pre-
dicted values align with actual values.
FIGURE 4    |    MAE and MSE for predicting mechanical properties and surface roughness. [Color figure can be viewed at wileyonlinelibrary.com]
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 11


11 of 17
In each graph, the red line represents the ideal scenario (where
predicted values perfectly match the actual values), and the blue
dots represent the relationship between actual and predicted val-
ues. The R2 values displayed in the graphs indicate how well the
models perform, with an R2 value close to 1 indicating a highly
successful model. Figure 5a shows hardness predictions made
using the KSTAR algorithm. The R2 value is 0.9997726, indi-
cating an almost perfect fit. The blue dots are distributed very
closely around the red line, indicating that the predicted val-
ues are nearly equal to the actual values. This suggests that the
KSTAR algorithm accurately predicted the Shore D hardness
parameter. The MLP algorithm is used to predict the flexural
strength (Figure 5b). The R2 value is 0.999925, demonstrating
that the algorithm achieved almost flawless performance. The
blue dots are aligned very closely and parallel to the red line. This
confirms that the MLP algorithm is highly effective in predict-
ing flexural strength. Figure 5c shows the performance of the
MLP algorithm in predicting the tensile strength. The R2 value
is 0.999755, again indicating an almost perfect fit. The blue dots
are distributed very close to the red line in a well-­aligned pat-
tern. This demonstrates the MLP algorithm's excellent predictive
ability for this metric. Finally, surface roughness predictions are
presented in Figure 5d using the KSTAR algorithm, with an R2
value of 0.999934. This high value highlights the model's excep-
tional performance. The blue dots are once again very close to
the red line, demonstrating that the model predictions are al-
most identical to the actual roughness values. Thus, the KSTAR
algorithm is also highly effective in predicting roughness. The
regression graphs in Figure 5 demonstrate the impressive predic-
tive power of both the KSTAR and MLP algorithms across differ-
ent metrics. The near-­perfect R2 values in all cases indicate that
these models achieved a high degree of accuracy in predicting.
4.4   |   Predicted Versus Actual Results
The predicted vs. actual graph is a tool used to visualize the re-
lationship between the values predicted by a model or analysis
TABLE 8    |    Coefficient of determination of all algorithms.
Algorithms
Shore D strength
Flexural strength
Tensile strength
Roughness
LR
0.992732
0.988632
0.979902
0.993922
GP
0.684201
0.776114
0.801835
0.716248
MLP
0.994895
0.999925
0.999755
0.994047
SLR
0.686539
0.973774
0.985206
0.716248
SMOREG
0.994895
0.993134
0.985206
0.994047
IBK
0.523452
0.776114
0.801835
0.673046
KSTAR
0.999772
0.907817
0.913194
0.999934
LWL
0.570775
0.776114
0.663841
0.562422
AR
0.601762
0.776114
0.801835
0.832858
BAGGİNG
0.601762
0.814997
0.801835
0.701704
CVP
0.570775
0.639338
0.454410
0.682568
MS
0.447010
0.671224
0.474410
0.698759
RC
0.624915
0.814997
0.801835
0.694707
RFC
0.570775
0.776114
0.688891
0.698762
RSS
0.701071
0.971881
0.957070
0.716248
RBD
0.784287
0.916231
0.926983
0.716248
IMC
0.624915
0.612395
0.494410
0.598714
DT
0.624915
0.776114
0.801835
0.716248
M5R
0.944006
0.993134
0.980013
0.851006
ZeroR
0.523452
0.473206
0.454410
0.468742
DS
0.570775
0.681084
0.653685
0.598761
M5P
0.932961
0.991436
0.984806
0.896323
RandomF
0.648300
0.907817
0.913194
0.716248
RandomT
0.570775
0.776114
0.688891
0.694707
RepTree
0.570775
0.776114
0.678980
0.687303
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 12


12 of 17
Journal of Applied Polymer Science, 2025
method and the actual observed values. In each graph, red and
blue points represent the predicted and actual values, respec-
tively. This type of graph is commonly used to evaluate model
accuracy and performance. In this section, the graphs were
created using 27 data points derived from the outputs of the
best prediction methods. Figure 6 compares the predicted and
actual values for Shore D hardness, flexural strength, tensile
strength, and surface roughness. Figure 6a shows that the pre-
dicted Shore D hardness values are generally very close to the
actual values, with minor deviations in some cases. However,
the overall trend indicates that the model performs well at pre-
dicting hardness. Similarly, in Figure 6b, the flexural strength
predictions align closely with the actual values, showing min-
imal discrepancies between the two. In Figure 6c, the tensile
strength predictions demonstrate a high degree of proximity to
the actual values, although minor deviations are observed in
a few cases. For surface roughness, as depicted in Figure 6d,
the predicted values exhibit strong agreement with the actual
values, even in instances of small differences, maintaining
the overall trend. These findings highlight the model's high
predictive performance and its ability to provide accurate esti-
mates for various mechanical properties. Across all graphs, a
general concordance between the predicted and actual values
is evident. The red and blue points mostly overlap or are po-
sitioned in proximity. This indicates that the ML models per-
formed with high accuracy in predicting both the mechanical
properties and surface roughness. Although minor deviations
were observed in some experiments, the models can be consid-
ered successful in their overall predictions.
The varying performance of ML models in this study can be
attributed to several factors related to the characteristics of
the algorithms and the nature of the dataset. First, certain
algorithms, such as ZeroR and CVP, demonstrated poor per-
formance because they lacked the complexity required to cap-
ture the intricate relationships between the input parameters
(LT, ID, and NT) and the output mechanical properties. ZeroR
only predicts the value of the dependent variable without con-
sidering the input features, making it unsuitable for datasets
with non-­linear relationships. Similarly, simpler models like
LWL and IMC struggled because of their limited ability to
generalize from the provided data, especially in cases where
interactions between parameters were significant. Conversely,
more complex algorithms like MLP and KSTAR performed ex-
ceptionally well due to their ability to model non-­linear rela-
tionships and capture subtle patterns in the data. Algorithms
like MLP, which use neural networks, excel in handling multi-­
dimensional datasets and can adapt to the inherent variabil-
ity in mechanical properties. Algorithms such as IBK and
RandomT, which rely on instance-­based or random tree ap-
proaches, may have underperformed due to their sensitivity to
the small size of the dataset. These models tend to overfit when
FIGURE 5    |    Regression graphs of the most successful machine learning algorithms. [Color figure can be viewed at wileyonlinelibrary.com]
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 13


13 of 17
the dataset is limited, leading to reduced prediction accuracy
on unseen data. In addition, the quality of results is influenced
by the specific design and assumptions of each algorithm.
Tree-­based models like RF and RepTree are effective in han-
dling non-­linear data but may face limitations in extrapolating
beyond the range of the training data. Similarly, methods like
SMOREG, while generally effective, may struggle with data-
sets where the variance in certain output variables is relatively
small, as seen in surface roughness predictions.
An important observation from this study is that different al-
gorithms excel in predicting different mechanical properties.
As an illustration, KSTAR excelled in hardness and surface
roughness predictions, whereas MLP proved to be more effec-
tive in forecasting tensile and flexural strength. This variation
underscores the fact that no single algorithm is universally op-
timal for all types of data or target variables. The differences
can be attributed to the nature of the parameters being ana-
lyzed and the inherent strengths of the algorithms. For exam-
ple, KSTAR, being an instance-­based algorithm, is well suited
for capturing localized patterns in the data, making it effec-
tive for surface roughness and hardness, which are highly
sensitive to specific parameter interactions. In contrast, MLP's
neural network architecture enables it to model complex, non-
linear relationships across the entire dataset, which explains
its superior performance for tensile and flexural strength.
This study highlights the need for a systematic approach to
selecting algorithms that are best suited for specific datasets
and prediction tasks. Although the results offer valuable in-
sights into the performance of different ML models, practical
application in real-­world scenarios requires a method for de-
termining the most appropriate algorithm in advance. Future
study could focus on developing a meta-­learning approach
that examines dataset characteristics, such as feature distribu-
tions, dimensionality, and the degree of nonlinearity, to pre-
dict the most suitable algorithm for a given task. For instance,
analyzing the variance, correlation structure, or complexity
of the input–output relationships could provide a basis for
automated model selection. Such a framework would signifi-
cantly enhance the utility of ML in real-­world applications,
enabling users to select the best algorithm without the need
for extensive trial-­and-­error experimentation. Furthermore,
understanding why certain algorithms perform better for
specific parameters requires a deeper investigation into the
interaction between parameter characteristics and algorithm
architecture. Surface roughness and hardness may be better
predicted by algorithms that focus on localized relationships,
while tensile and flexural strength might benefit from mod-
els capable of capturing global patterns across the dataset.
Exploring such relationships in future studies could provide
FIGURE 6    |    Predicted mechanical properties and surface roughness versus actual values. [Color figure can be viewed at wileyonlinelibrary.com]
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 14


14 of 17
Journal of Applied Polymer Science, 2025
valuable guidelines for both selecting and designing ML mod-
els tailored to specific FDM applications.
In summary, the differences in algorithm performance can
be justified by the balance between model complexity, dataset
size, and the ability to capture non-­linear or interaction effects.
Although some models are inherently better suited for capturing
complex relationships, others are limited by their simplicity or
sensitivity to dataset characteristics. These findings highlight
the importance of selecting appropriate ML models based on
both the nature of the data and the desired prediction accuracy.
In addition, the development of a systematic framework for algo-
rithm selection based on dataset characteristics and parameter-­
specific requirements would be a valuable direction for future
research, further enhancing the practical applicability of ML in
FDM processes.
4.5   |   Discussion
The findings of this study demonstrate the successful applica-
tion of ML algorithms in predicting the mechanical properties
of FDM-­produced ABS parts. The high accuracy achieved by the
KSTAR algorithm in predicting Shore D hardness (R2 = 0.9997)
and surface roughness (R2 = 0.9993), along with the MLP al-
gorithm's superior performance in predicting tensile strength
(R2 = 0.9997) and flexural strength (R2 = 0.9999), validates the
robustness of these approaches within the experimental do-
main established. Regarding the generalizability of these mod-
els, several important considerations emerge. While the models
show exceptional performance within the specified parameter
ranges (LT: 100–200 μm, ID: 50%–100%, NT: 220°C–240°C),
their applicability to broader FDM operations requires careful
examination. The models' predictive capabilities are inherently
influenced by the specific material properties of ABS and the
defined experimental conditions. However, the underlying prin-
ciples and methodologies can be adapted to similar FDM appli-
cations with appropriate modifications.
The transferability of these models to other FDM operations
depends on several factors. First, the physical and chemical
properties of the printing material significantly influence the
mechanical properties. While these models might be directly
applicable to ABS-­based applications within similar parameter
ranges, extending them to other materials (such as PLA, PETG,
or composite materials) would require retraining with material-­
specific data. Second, the printing parameters used in this study,
while comprehensive, represent a subset of the possible FDM
process parameters. Additional factors such as PS, bed tempera-
ture, raster angle, and environmental conditions could affect
the mechanical properties in ways not captured by the current
models. The ANOVA results provide valuable insights into the
relative importance of different parameters, with ID showing
the highest impact on mechanical properties (55.56%–80.02%)
except for surface roughness. This understanding of parameter
significance could be generalized to guide parameter selection in
other FDM applications, even when using different materials or
equipment. However, specific quantitative relationships might
vary depending on the material and process conditions. The ML
approaches demonstrated in this study offer a framework that
could be adapted for other FDM applications. The success of the
KSTAR and MLP algorithms suggests that these methods can
effectively capture the complex relationships between printing
parameters and mechanical properties. The methodology of
using multiple algorithms and selecting the best-­performing
ones based on comprehensive error metrics (MAE, RMSE, MSE,
R2) provides a robust approach that could be replicated for dif-
ferent FDM applications.
In addition to these findings, it is essential to discuss the practi-
cal applications of ML in FDM processes, as highlighted by this
study. The developed ML models can be utilized in real-­world
manufacturing as optimization tools for determining printing
parameter combinations that achieve specific mechanical prop-
erty requirements. For instance, in a production line, where a
particular application demands minimum surface roughness or
maximum tensile strength, these models could quickly identify
the optimal parameter settings. This application would signifi-
cantly reduce the time and costs associated with trial-­and-­error
experiments. One critical aspect not directly addressed in this
study is the comparison between the use of ML techniques and
the expertise of experienced operators. While experienced op-
erators can often determine effective global parameter settings
based on their knowledge and intuition, ML provides an op-
portunity to systematically optimize these parameters, partic-
ularly in situations where new materials are being introduced
or where the relationships between parameters and outcomes
are highly complex. ML models, as demonstrated in this study,
can provide a quantitative and repeatable framework for opti-
mization, reducing the dependency on individual expertise and
minimizing the risk of human error. When working with novel
materials with minimal existing data, refining ML models with
targeted material-­specific information can ensure efficient and
precise parameter optimization. The choice of the algorithm in
such scenarios would depend on the complexity of the material
behavior and the desired mechanical outcomes, as discussed
earlier. Moreover, this study primarily focuses on global pa-
rameter optimization, where the same parameter values are ap-
plied throughout the print. However, as highlighted in previous
studies [47], local optimization—where parameters are varied
dynamically during the printing process—can often result in
superior outcomes, particularly for complex geometries or multi-­
functional parts. Although local optimization was beyond the
scope of this study, it represents a promising avenue for future
research. The integration of ML models into real-­time control
systems could enable dynamic adjustments to parameters such
as NT or ID in response to changing conditions during the print.
Such an approach would leverage the predictive power of ML
to achieve not only global but also localized optimization, fur-
ther enhancing the precision and efficiency of FDM processes.
Another potential application lies in customized manufactur-
ing processes. For example, in the medical field, where person-
alized prosthetics or implants are produced, ML models could
optimize printing parameters to meet specific mechanical and
surface quality requirements, improving the efficiency and pre-
cision of such processes. Despite these promising applications,
certain challenges must be addressed to ensure the successful
industrial integration of these models. First, the models must be
retrained with broader datasets to accommodate wider param-
eter ranges and different materials. Second, the development
of hybrid models that combine physics-­based understanding
with ML could enhance predictive accuracy, especially across
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 15


15 of 17
varying operating conditions. Finally, user-­friendly interfaces
and compatibility with real-­time data systems would be crucial
for seamless industrial implementation.
In conclusion, while the models developed in this study show
excellent predictive capability within the specified experimental
domain, their generalization to other FDM operations requires
careful consideration of material properties, process parameters,
and operating conditions. The methodology and insights gained
from this study provide a valuable foundation for developing
similar predictive models for other FDM applications, but the
direct application of the current models should be approached
with appropriate validation and potential adaptation to specific
use cases. In addition, exploring the integration of ML for local
parameter optimization and dynamic control during the print-
ing process represents an important direction for future work.
The high accuracy achieved suggests that ML approaches can
effectively predict mechanical properties in FDM processes, po-
tentially reducing the need for extensive experimental testing
and paving the way for practical industrial applications.
5   |   Conclusions
In this study, 25 different ML algorithms were used to pre-
dict the mechanical properties of ABS parts produced using
the FDM method, and the effects of printing parameters (LT,
ID, and NT) on the mechanical properties were analyzed.
According to the ANOVA results, the ID had the greatest im-
pact on hardness (55.56%), tensile strength (80.02%), and flex-
ural strength (77.13%). In contrast, the LT was identified as
the most influential parameter on the surface roughness, with
a 70.89% effect. The performance of the ML algorithms was
evaluated using various error metrics, including MAE, RMSE,
MSE, and R2. For predicting hardness and surface roughness,
the KSTAR algorithm achieved the best results, with MAE:
0.006 and R2: 0.99 for hardness, and MAE: 0.009 and R2: 0.99
for surface roughness. For the prediction of tensile and flex-
ural strength, the MLP algorithm showed the highest accu-
racy, with R2 > 0.99 for both properties. The regression graphs
demonstrate the performance of the algorithms by comparing
the predicted values with the experimental results. The regres-
sion graphs for hardness and surface roughness demonstrated
that the KSTAR algorithm's predictions were highly consistent
with the experimental values, showing a strong correlation.
The KSTAR algorithm exhibited remarkable precision in hard-
ness prediction, as the predicted values were nearly identical to
the actual data. A similar level of success was observed for the
surface roughness prediction, where the predicted and actual
values were very close. The regression graphs for tensile and
flexural strength prediction highlight the superior performance
of the MLP algorithm. The predicted values for both the tensile
and flexural strengths closely aligned with the experimental
results, showing a strong linear relationship. The R2 > 0.99 val-
ues indicated that the model could explain almost all the varia-
tion in the data, with the predicted results closely matching the
experimental outcomes. In the regression graphs, the predicted
and actual values were mostly aligned along a 45° line (y = x),
further confirming the high accuracy of the model. This study
demonstrated the effectiveness of ML algorithms in predicting
the mechanical properties of ABS parts produced by FDM and
provided recommendations for optimizing printing parame-
ters. The proper selection of parameters such as ID, LT, and
NT plays a crucial role in improving the mechanical properties
of printed parts. Future studies could explore similar analyses
using different materials and production methods, as well as
test the performance of ML algorithms on larger datasets.
Author Contributions
Mahmut Özkül: formal analysis (equal), investigation (equal), meth-
odology (equal), resources (equal), software (equal), validation (equal),
writing – original draft (equal). Fatma Kuncan: conceptualization
(equal), formal analysis (equal), investigation (equal), methodology
(equal), resources (equal), software (equal), supervision (equal), visu-
alization (equal), writing – original draft (equal). Osman Ulkir: con-
ceptualization (equal), formal analysis (equal), investigation (equal),
methodology (equal), software (equal), validation (equal), writing –
original draft (equal).
Ethics Statement
The authors have nothing to report.
Conflicts of Interest
The authors declare no conflicts of interest.
Data Availability Statement
The data that support the findings of this study are available from the
corresponding author upon reasonable request.
References
1. I. Fidan, O. Huseynov, M. A. Ali, et al., “Recent Inventions in Addi-
tive Manufacturing: Holistic Review,” Inventions 8 (2023): 103.
2. P. Badoniya, M. Srivastava, P. K. Jain, and S. Rathee, “A State-­Of-­
The-­Art Review on Metal Additive Manufacturing: Milestones, Trends,
Challenges and Perspectives,” Journal of the Brazilian Society of Me-
chanical Sciences and Engineering 46 (2024): 339.
3. S. Rouf, A. Malik, N. Singh, et al., “Additive Manufacturing Tech-
nologies: Industrial and Medical Applications,” Sustainable Operations
and Computers 3 (2022): 258–274.
4. G. Prashar, H. Vasudev, and D. Bhuddhi, “Additive Manufacturing:
Expanding 3D Printing Horizon in Industry 4.0,” International Journal
on Interactive Design and Manufacturing 17 (2023): 2221–2235.
5. L. Zhou, J. Miller, J. Vezza, et al., “Additive Manufacturing: A Com-
prehensive Review,” Sensors 24 (2024): 2668.
6. T. Vaneker, A. Bernard, G. Moroni, I. Gibson, and Y. Zhang, “Design
for Additive Manufacturing: Framework and Methodology,” CIRP An-
nals 69 (2020): 578–599.
7. S. Gunes, O. Ulkir, and M. Kuncan, “Application of Artificial Neural
Network to Evaluation of Dimensional Accuracy of 3D-­Printed Polylac-
tic Acid Parts,” Journal of Polymer Science 62 (2024): 1864–1889.
8. A. Patel and M. Taufik, “Extrusion-­Based Technology in Additive
Manufacturing: A Comprehensive Review,” Arabian Journal for Science
and Engineering 49 (2024): 1309–1342.
9. Y. Wang, R. T. Mushtaq, A. Ahmed, et al., “Additive Manufacturing
Is Sustainable Technology: Citespace Based Bibliometric Investigations
of Fused Deposition Modeling Approach,” Rapid Prototyping Journal 28
(2022): 654–675.
10. H. Ardeshir, M. Hoseinzadeh, M. B. Limooei, and S. Hosseini, “A
Scientometrics Study and Its Practical Implications for Fused Deposi-
tion Modeling,” Alexandria Engineering Journal 99 (2024): 217–231.
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 16


16 of 17
Journal of Applied Polymer Science, 2025
11. T. Sathies, P. Senthil, and M. S. Anoop, “A Review on Advancements
in Applications of Fused Deposition Modelling Process,” Rapid Proto-
typing Journal 26 (2020): 669–687.
12. M. Moradi, A. Aminzadeh, D. Rahmatabadi, and A. Hakimi, “Ex-
perimental Investigation on Mechanical Characterization of 3D Printed
PLA Produced by Fused Deposition Modeling (FDM),” Materials Re-
search Express 8 (2021): 035304.
13. A. Rasheed, M. Hussain, S. Ullah, et  al., “Experimental Investi-
gation and Taguchi Optimization of FDM Process Parameters for the
Enhancement of Tensile Properties of bi-­Layered Printed PLA-­ABS,”
Materials Research Express 10 (2023): 095307.
14. M. Algarni and S. Ghazali, “Comparative Study of the Sensitivity of
PLA, ABS, PEEK, and PETG's Mechanical Properties to FDM Printing
Process Parameters,” Crystals 11 (2021): 995.
15. I. Khan, I. Barsoum, M. Abas, A. Al Rashid, M. Koç, and M. Tariq, “A
Review of Extrusion-­Based Additive Manufacturing of Multi-­Materials-­
Based Polymeric Laminated Structures,” Composite Structures 349–350
(2024): 118490.
16. R. B. Kristiawan, F. Imaduddin, D. Ariawan, Ubaidillah, and Z. Ar-
ifin, “A Review on the Fused Deposition Modeling (FDM) 3D Printing:
Filament Processing, Materials, and Printing Parameters,” Open Engi-
neering 11 (2021): 639–649.
17. S. Wickramasinghe, T. Do, and P. Tran, “FDM-­Based 3D Printing of
Polymer and Associated Composite: A Review on Mechanical Proper-
ties, Defects and Treatments,” Polymers (Basel) 12 (2020): 1529.
18. N. A. Fountas, K. Kitsakis, K.-­E. Aslani, J. D. Kechagias, and N. M.
Vaxevanidis, “An Experimental Investigation of Surface Roughness in
3D-­Printed Pla Items Using Design of Experiments,” Proceedings of the
Institution of Mechanical Engineers, Part J: Journal of Engineering Tri-
bology 236 (2022): 1979–1984.
19. K. Tüfekci, B. G. Çakan, and V. M. Küçükakarsu, “Stress Re-
laxation of3DprintedPLAof Various Infill Orientations Under Ten-
sile and Bending Loadings,” Journal of Applied Polymer Science 140
(2023): 140.
20. N. Ben Ali, M. Khlif, D. Hammami, and C. Bradai, “Experimental
Optimization of Process Parameters on Mechanical Properties and the
Layers Adhesion of3Dprinted Parts,” Journal of Applied Polymer Science
139 (2022): 139.
21. N. A. Fountas, J. D. Kechagias, D. E. Manolakos, and N. M. Vaxevan-
idis, “Single and Multi-­Objective Optimization of FDM-­Based Additive
Manufacturing Using Metaheuristic Algorithms,” Procedia Manufac-
turing 51 (2020): 740–747.
22. J. D. Kechagias, S. P. Zaoutsos, N. A. Fountas, and N. M. Vaxevan-
idis, “Experimental Investigation and Neural Network Development
for Modeling Tensile Properties of Polymethyl Methacrylate (PMMA)
Filament Material,” International Journal of Advanced Manufacturing
Technology 134 (2024): 4387–4398.
23. J. Kechagias and S. Zaoutsos, “Effects of 3D-­Printing Processing Pa-
rameters on FFF Parts’ Porosity: Outlook and Trends,” Materials and
Manufacturing Processes 39 (2024): 804–814.
24. S. Kumar, T. Gopi, N. Harikeerthana, et  al., “Machine Learning
Techniques in Additive Manufacturing: A State of the Art Review on
Design, Processes and Production Control,” Journal of Intelligent Man-
ufacturing 34 (2023): 21–55.
25. C. Wang, X. P. Tan, S. B. Tor, and C. S. Lim, “Machine Learning in
Additive Manufacturing: State-­Of-­The-­Art and Perspectives,” Additive
Manufacturing 36 (2020): 101538.
26. G. D. Goh, S. L. Sing, and W. Y. Yeong, “A Review on Machine Learn-
ing in 3D Printing: Applications, Potential, and Challenges,” Artificial
Intelligence Review 54 (2021): 63–94.
27. M. Khalil, A. S. McGough, Z. Pourmirza, M. Pazhoohesh, and S.
Walker, “Machine Learning, Deep Learning and Statistical Analysis for
Forecasting Building Energy Consumption — A Systematic Review,”
Engineering Applications of Artificial Intelligence 115 (2022): 105287.
28. R. Rai, M. K. Tiwari, D. Ivanov, and A. Dolgui, “Machine Learning
in Manufacturing and Industry 4.0 Applications,” International Journal
of Production Research 59 (2021): 4773–4778.
29. A. S. Khusheef, M. Shahbazi, and R. Hashemi, “Deep Learning-­
Based Multi-­Sensor Fusion for Process Monitoring: Application to
Fused Deposition Modeling,” Arabian Journal for Science and Engineer-
ing 49 (2024): 10501–10522.
30. T. Sai, V. K. Pathak, and A. K. Srivastava, “Modeling and Optimi-
zation of Fused Deposition Modeling (FDM) Process Through Printing
PLA Implants Using Adaptive Neuro-­Fuzzy Inference System (ANFIS)
Model and Whale Optimization Algorithm,” Journal of the Brazilian So-
ciety of Mechanical Sciences and Engineering 42 (2020): 617.
31. O. A. Mohamed, S. H. Masood, and J. L. Bhowmik, “Experimental
Study of the Wear Performance of Fused Deposition Modeling Printed
Polycarbonate-­Acrylonitrile Butadiene Styrene Parts Using Definitive
Screening Design and Machine Learning-­Genetic Algorithm,” Journal
of Materials Engineering and Performance 31 (2022): 2967–2977.
32. O. Ulkir, M. S. Bayraklılar, and M. Kuncan, “Raster Angle Predic-
tion of Additive Manufacturing Process Using Machine Learning Algo-
rithm,” Applied Sciences 14 (2024): 2046.
33. A. Cerro, P. E. Romero, O. Yiğit, and A. Bustillo, “Use of Machine
Learning Algorithms for Surface Roughness Prediction of Printed Parts
in Polyvinyl Butyral via Fused Deposition Modeling,” International
Journal of Advanced Manufacturing Technology 115 (2021): 2465–2475.
34. N. Hooda, J. S. Chohan, R. Gupta, and R. Kumar, “Deposition Angle
Prediction of Fused Deposition Modeling Process Using Ensemble Ma-
chine Learning,” ISA Transactions 116 (2021): 121–128.
35. C. Hu, W. N. J. Hau, W. Chen, and Q.-­H. Qin, “The Fabrication of
Long Carbon Fiber Reinforced Polylactic Acid Composites via Fused
Deposition Modelling: Experimental Analysis and Machine Learning,”
Journal of Composite Materials 55 (2021): 1459–1472.
36. P. Charalampous, I. Kostavelis, T. Kontodina, and D. Tzovaras,
“Learning-­Based Error Modeling in FDM 3D Printing Process,” Rapid
Prototyping Journal 27 (2021): 507–517.
37. O. Ulkir, “3D Print,” Additive Manufacturing 10 (2023): 1423.
38. Y. Ni, Q. Gao, Z. Hao, et al., “Enhancing the Strength and Tough-
ness of Polylactic Acid Through Fused Deposition Modeling-­Induced
Orientation and Nucleation Effects of Attapulgite,” Journal of Applied
Polymer Science 141 (2024): 141.
39. B. K. Behera, “Mechanical, Viscoelastic, and Biodegradability Char-
acteristics of Ramie Fibre-­Reinforced Acrylonitrile Butadiene Styrene
Composites,” Journal of Applied Polymer Science 141 (2024): 141.
40. Z. G. Mohammadsalih, A. F. Abdulameer, N. S. Sadeq, L. K. Abbas,
and S. M. Sapuan, “Preparation, Characterization, and Properties of Ac-
rylonitrile Butadiene Styrene / Multi Walled Carbon Nanotubes Nano-
composites,” Journal of Polymer Research 31 (2024): 203.
41. J. Zhu, Z. Su, Q. Wang, et al., “Surface Quality Prediction and Quan-
titative Evaluation of Process Parameter Effects for 3D Printing With
Transfer Learning-­Enhanced Gradient-­Boosting Decision Trees,” Ex-
pert Systems with Applications 237 (2024): 121478.
42. B. El Essawi, S. Abdallah, S. Ali, A. Nassir Abdo Mohammed, R.
A. Susantyoko, and S. Pervaiz, “Optimization of Infill Density, Fiber
Angle, Carbon Fiber Layer Position in 3D Printed Continuous Carbon-­
Fiber Reinforced Nylon Composite,” Results in Engineering 21 (2024):
101926.
43. N. H. Musa, N. N. Mazlan, S. Mohd Yusuf, F. L. Binti Mohd Red-
zuan, N. A. Nordin, and S. A. Mazlan, “Influence of Nozzle Tempera-
tures on the Microstructures and Physical Properties of 316l Stainless
Steel Parts Additively Manufactured by Material Extrusion,” Rapid Pro-
totyping Journal 30 (2024): 2021–2032.
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---


## Page 17


17 of 17
44. M. El Rajab, L. Yang, and A. Shami, “Zero-­Touch Networks: To-
wards Next-­Generation Network Automation,” Computer Networks 243
(2024): 110294.
45. A. H. Salem, S. M. Azzam, O. E. Emam, and A. A. J. Abohany, “Ad-
vancing Cybersecurity: A Comprehensive Review of AI-­Driven Detec-
tion Techniques,” Big Data 11 (2024): 105.
46. A. Gupta and N. K. Chauhan, “A Severity-­Based Classification As-
sessment of Code Smells in Kotlin and Java Application,” Arabian Jour-
nal for Science and Engineering 47 (2022): 1831–1848.
47. J. M. Gardner, K. A. Hunt, A. B. Ebel, et al., “Machines as Craftsmen:
Localized Parameter Setting Optimization for Fused Filament Fabrica-
tion 3D Printing,” Advanced Materials Technologies 4 (2019): 1800653.
 10974628, 2025, 20, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/app.56899, Wiley Online Library on [02/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License


---
