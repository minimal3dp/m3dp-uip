# ai for 3d printing_revised_accepted version

> **Source:** `ai for 3d printing_revised_accepted version.pdf`
> **Converted:** 2025-11-22 21:18:09
> **Method:** PyMuPDF

---

## Page 1


A review on Machine Learning in 3D printing: Applications, Potential, and Challenges
G. D. Goh1 , S. L. Sing1 and W. Y. Yeong1*
1Singapore Centre for 3D Printing, School of Mechanical & Aerospace Engineering, Nanyang Technological University, 50
Nanyang Avenue, Singapore 639798

*Corresponding Author
Designation: Associate Professor, Mechanical and Aerospace Engineering and Aerospace and Defence Program
Director, Singapore Centre for 3D Printing, School of Mechanical & Aerospace Engineering, Nanyang
Technological University, Singapore
Email: WYYeong@ntu.edu.sg
Tel: 67904343
Abstract
Additive manufacturing (AM) or 3D printing is growing rapidly in the manufacturing industry and has
gained a lot of attention from various fields owing to its ability to fabricate parts with complex features.
The reliability of the 3D printed parts has been the focus of the researchers to realize AM as an end-
part production tool. Machine Learning (ML) has been applied in various aspects of AM to improve the
whole design and manufacturing workflow especially in the era of industrial revolution 4.0. In the
review article, various types of ML techniques are first introduced. It is then followed by the discussion
on their use in various aspects of AM such as design for 3D printing, material tuning, process
optimization, in-situ monitoring, cloud service, and cybersecurity. Potential applications in the fields of
biomedical, tissue engineering and building & constructions will be highlighted. The challenges faced
by ML in AM such as computational cost, standards for qualification, and data acquisition techniques
will also be discussed. In the authors’ perspective, in-situ monitoring of AM processes will significantly
benefit from the object detection ability of ML. As a large data set is crucial for ML, data sharing of
AM would enable faster adoption of ML in AM. Standards for the shared data are needed to facilitate
easy sharing of data. The use of ML in AM will become more mature and widely adopted as better data
acquisition techniques and more powerful computer chips for ML are developed.
Keywords: Machine Learning, Artificial Intelligence, 3D printing, In-situ Monitoring, Design for
Additive Manufacturing, Process Optimization.
1. Introduction
Additive manufacturing (AM) techniques, or 3D printing, have matured and brought about a paradigm
shift on how things are designed and manufactured. The layer-by-layer fabrication techniques enable
the fabrication of parts with complex geometries and functionally graded properties. AM is also greener
as they reduce material wastage in general. It has come a long way from being a prototyping tool to
slowly being adopted for end-part production.
Various AM fabrication techniques such as fused filament fabrication (FFF), stereolithography (SLA),
selective laser sintering (SLS), selective laser melting (SLM), laser engineered net shaping (LENS)
have been developed to print real functional parts with various kinds and forms of materials. However,
there exist some unique challenges to overcome, such as the porosity due to poor fusion between
adjacent filament, anisotropic nature of the materials, and warping as a result of the residual stress due
to the fast cooling nature of the AM processes.
Detailed understanding of the AM process, from the processability of the feedstock materials
(rheological properties and powder flowability) to the relationship between the process-structure-


---


## Page 2


properties of the AM parts, is necessary. However, the AM processes involve multiple process
parameters that can influence the quality of the final parts which requires interdisciplinary
understanding such as material properties, solid-liquid interaction, fluid dynamics, grain-growth
development, and thermal-mechanical interaction. The setting up of physics-based models can be
difficult and time-consuming as it necessitates a comprehensive knowledge of the multi-scale and multi-
physics AM processes. As a result, individual research typically covers only a few aspects of the entire
printing process which restricted the representation of the whole. For instance, research such as
microscale grain structure evolution of the powder bed fusion using computational fluid dynamics (CFD)
(Acharya, Sharon et al. 2017, Tan, Sing et al. 2020), analytical modeling of residual stress (Fergani,
Berto et al. 2017), and macro-scale melt pool profile and bead shape using finite element analysis (Chen,
Guillemot et al. 2017) has been attempted. Such analyses are time consuming. It is therefore difficult
to emulate the whole AM process quickly and accurately through the physics-based numerical
simulations. The use of machine learning (ML) data-driven models based on the physical understanding
of AM processes is instrumental as optimization of the AM process can be performed with only
incomplete or partial information about the AM processes.
Additionally, quality control of the AM parts has gained wide attention from the industries to ensure
parts fabricated for functional use satisfy specific requirements, particularly in quality and reliability.
As more advanced AM materials are developed and used in critical parts of structures (Wong and
Hernandez 2012, Madara and Selvan 2017), high part quality must be ensured. Unwanted porosity is a
known issue in AM processes (Aboulkhair, Everitt et al. 2014, Liu, Guessasma et al. 2018). These
porosities significantly affect the mechanical performance of the AM parts.  A study has shown that a
highly dense AM part (>99.8%) can be produced using a well-controlled system (Sing, Wiria et al. 2018,
Yu, Sing et al. 2019). In-situ quality control techniques are therefore required to further improve the
quality of the AM parts through detection of anomaly and corrective printing using closed loop feedback.
To overcome the time-consuming physics-based modeling and to detect anomaly during the in-process
monitoring for quality control, data-driven models have been used in the AM field. A large amount of
data is collected and processed by the ML algorithms to predict certain behaviors and properties, which
are essential for decision making. It is also used in AM to recognize certain patterns or irregularities in
the dynamic manufacturing process. The ML has gained a substantial influence on all aspects of AM—
from the design of the AM part, fabrication process, and qualification to logistics. The impact of ML is
expected to grow in the years to come.
This article presents a review of the research development concerning the use of ML in AM, especially
in the areas of design for 3D printing, process optimization, and in-situ monitoring for quality control.
Other areas such as cloud service platform, service evaluation and security of attack detection will also
be discussed. The organization of the article is as follow: Section 2 details the classification and the
working principles of ML techniques used in AM. Next, Section 3 gives a comprehensive review of the
use of ML in various aspects of AM, and lastly, Section 4 depicts the potential and challenges in this
field.
2. Machine Learning techniques
ML techniques are generally categorized into 4 groups: supervised learning, unsupervised learning,
semi-supervised learning, and reinforced learning (Figure 1). In this section, the theories and ideas of
each category of ML techniques will be discussed in detail.


---


## Page 3


Figure 1 Machine learning techniques used in 3D printing
2.1 Supervised Learning
Supervised learning involves training an algorithm on a group of data, in which each training point
contains a label. This label signifies a particular class that the training point belongs to. Supervised
algorithms then try to identify the decision boundaries that split the clusters of data. Supervised learning
algorithms model the relationship between the input features and the labeled outputs. Thus, it is able to
predict input features for “desired” outputs (Figure 2).

Figure 2 Supervised machine learning
Some examples of supervised learning algorithms used in AM field are Naive Bayes (Wu, Phoha et al.
2016, Bacha, Sabry et al. 2019), Decision Trees (Wu, Phoha et al. 2016), Linear Regression,
convolutional neural network (CNN) (Gu, Chen et al. 2018, Ludwig, Meyer et al. 2018, Pham, Lee et
al. 2018, Scime and Beuth 2018, Shevchik, Kenel et al. 2018, Yuan, Guss et al. 2018, Zhang, Hong et
al. 2018, Francis and Bian 2019, Khadilkar, Wang et al. 2019), genetic programming (Vosniakos,
Maroulis et al. 2007, Rong-Ji, Xin-hua et al. 2008, Jiang, Liu et al. 2014, Vijayaraghavan, Garg et al.
2014, Garg, Lam et al. 2016, Yamanaka, Todoroki et al. 2016), long short term memory (Koeppe,
Hernandez Padilla et al. 2018), artificial neural network (ANN), particle swarm algorithm (Asadi-
Eydivand, Solati-Hashjin et al. 2016), k-nearest neighbor (KNN) (Wu, Song et al. 2017), radial basis
function (Vahabli and Rahmati 2016), Siamese neural network (He, Yang et al. 2019), and support
vector machine (SVM) (Gobert, Reutzel et al. 2018).


---


## Page 4


2.2 Unsupervised Learning
Unlike supervised learning, unsupervised learning algorithms require no human expert to label the data.
Unsupervised methods extract features in the input data that are unlabelled and classify the data through
self-taught rules. Thus, these models are usually applied to identify hidden or unknown relationships
among the data (Figure 3).

Figure 3 Unsupervised machine learning
Some examples of unsupervised learning algorithms used in AM field are K means clustering (Scime
and Beuth 2018, Scime and Beuth 2019, Snell, Tammas-Williams et al. 2019), self-organizing map
(SOM) (Gan, Li et al. 2019, Jafari-Marandi, Khanzadeh et al. 2019, Wu, Yu et al. 2019), and restricted
Boltzmann machine (Ye, Hsi Fuh et al. 2018).
2.3 Semi-supervised Learning
Semi-supervised learning is a combination of supervised and unsupervised learning algorithms. Semi-
supervised learning algorithms are applied when dealing with a large volume of data that makes labeling
very impractical and costly and therefore the data fed to the learning algorithms is a mixture of labeled
and unlabelled data. These models use the two sets of data (labeled and unlabelled) and generally
perform better than unsupervised learning because of the presence of the small amount of labeled data.
They are more cost-efficient and simpler to train than supervised learning. Some examples of semi-
supervised algorithms are Gaussian Mixture (Okaro, Jayasinghe et al. 2019), Model low-density
separation, generative models, and graph-based methods.
2.4 Reinforced learning
Unlike supervised learning that has labelled data, training data for reinforced learning algorithms can
only provide an indication on whether they are correct or not. They iteratively learn “good” behavior
by interacting with their environment. They learn through principles similar to supervised learning, but
instead of having a large volume of labeled data, the model has to “interact” with the environment,
which in turn produces a positive reward or a negative punishment. This feedback reinforces the
behavior of the model, thus giving it the name (Figure 4).


---


## Page 5


Figure 4 Reinforcement machine learning
Reinforcement learning algorithms often use the terms exploration and exploitation. Exploitation refers
to taking action that produces the highest possible reward and exploration refers to taking action that
has not been taken before. By using a combination of these two techniques, the model can slowly learn
more about the environment, while understanding inputs that lead to positive rewards, hence, arriving
at optimal solutions. Some examples of reinforcement learning algorithms are Q-Learning (Benoit,
Rana et al. 2018, Wasmer, Le-Quang et al. 2018), Temporal Difference and Deep Adversarial Networks.
3. Applications of ML in 3D printing
The use of ML algorithms in the 3D printing field covers various major aspects that have a direct impact
on the quality of the final 3D printed parts. They include design for 3D printing, part quality/process
optimization, and in-situ monitoring for quality control. There are also some other aspects related to the
efficiency of the design and manufacturing process for 3D printing techniques, namely, printability
checking, slicing acceleration, nozzle path planning, cloud service platform, service evaluation and
security of attack detection. In this section, the use of the ML algorithms in the various aspects of 3D
printing will be discussed.
3.1 Design for 3D printing
Design for 3D printing is an important research topic that requires a comprehensive understanding of
the capabilities and limitations of 3D printing techniques. It is the first and critical step in the process
workflow. A good  computer-aided design (CAD) model design would not only ensure the printability
but would also reduce the amount of support material when it is needed. However, the design process
is normally iterative and time-consuming. Data-driven design for 3D printing would help designers in
the design process.
Maiden et al. showed that the design feature database provided ideas and design features for less-
experienced designers (Bin Maidin, Campbell et al. 2012). The use of the ML technique in 3D printing
enables feature recommendations to existing CAD models, thus helping the designers to speed up the
decision-making process during the design stage. For instance, a hybrid ML algorithm was devised
which uses hierarchical clustering to classify AM design features and support vector machine (SVM)
to enhance the hierarchical clustering result in pursuit of finding the recommended AM design features
(Yao, Moon et al. 2017). It helped inexperience designers who were new to 3D printing to determine
suitable AM design features for the remote-controlled car components without actual physical trials and
errors.


---


## Page 6


Apart from that, ML algorithms have been used for feature recognition of CAD models for
manufacturability analysis of 3D printing. Heat Kernal Signature and multiscale clustering method were
used to detect whether manufacturing constraints existed in a particular CAD model, helping designers
to identify possible design faults early (Shi, Zhang et al. 2018). In a study to determine ideal print
orientation to avoid putting support structures on user-preferred features, a double-layered Extreme
Learning Machine (DL-ELM) was used (Zhang, Le et al. 2015). In this DL-ELM, the first layer was
the ELM classification to evaluate the relative score between the various part orientations, and the
second layer was the ELM regression to construct a global score for all printing directions. It was found
to be able to identify the best printing directions with minimum visual artifacts due to support removal.
In a study to optimize the build orientation, CNN was found to be better in terms of accuracy and
consistency at predicting build time and part mass than the baseline linear regression model (Williams,
Meisel et al. 2019).

Figure 5 Overview of applying ANN for highly efficient numerical modelling. a) experimental test to confirm the FEA results.
b) FEA results used as  input for ANN. c) ANN artitecture containing one fully connected layer followed by two long-short-
term memorcy cell (LSTM) and then followed by another fully connected layer. d) schematics of fully connected layers. e)
schematics of LSTM. f) comparison with FEA showing NN capability in predicting stresses (Koeppe, Hernandez Padilla et al.
2018).
The advancement in numerical simulation has allowed CAD models to be evaluated digitally before
they are fabricated and tested physically, thus reducing the cost and time spent in experiments. However,
numerical simulations can be computationally costly and time-consuming with complex processes,
making online monitoring of the printing processes not feasible. Data-driven models have potential in
predicting the final properties of the printed parts. Khadilkar et al. used a deep learning-based (DL)
framework to estimate stress distribution on the cured layer from SLA in almost real-time (Khadilkar,
Wang et al. 2019). In this attempt, a 3D model database that contains a wide range of geometric features
was first generated. FEA simulations on the 16,700 3D printed models were then used to generate data
labels to train the DL network. They found that a two-stream CNN outperforms single-stream CNN and
ANN. Despite this, ANN is used to learn a parameterized mechanical model of cellular lattice structures
that includes their linear elastoplastic mechanical behavior to predict maximum Von Mises and
equivalent principal stresses in the struts and joints (Koeppe, Hernandez Padilla et al. 2018) (Figure 5).


---


## Page 7


The data-driven stress prediction took about 0.47 seconds, which is significantly shorter in comparison
with the FEM simulation which took 5-10 hours. The trained ANN models can potentially be
incorporated into existing FEM frameworks to simulate the structural performance of larger parts of
various scales. Apart from that, ML algorithms can learn the thermal deformation of the AM processes
and provide appropriate geometric compensation to the models for printing (Chowdhury 2016).
AM or  3D printing has also encouraged the development of new designs, such as biommetic structures
(Meng, Zhao et al. 2020, Yang, Gu et al. 2020). In particular, composite structures can now be tuned
rapidly. ML algorithms have been demonstrated to be suitable for such area, especially in tuning
material properties and is capable of generating new designs that outperform existing composites
available in the dataset (Gu, Chen et al. 2018, Gu, Chen et al. 2018). CNN was used to predict the
stiffness and toughness of the composite. ML simulation, which includes the training (n=80,000) and
predictive (n=20,000) phases, is found to be 250 times quicker compared to FEM simulations. Also, it
is found that a small amount of training data is sufficient to obtain a ML model with high accuracy.
Furthermore, obtaining an optimal design for the composite is still possible with incomplete information.
Table 1 provides a summary of various research works on ML in design for 3D printing.

Table 1 The use of ML in design for 3D printing
Features
ML technique
Remarks
Ref.
Composite design Linear model
and CNN
- predict mechanical properties accurately
even with small amount of training data
- ability to rebuild detailed performances of
designs without using precise information in
the training process.
(Gu, Chen
et al. 2018)
Process planning
Genetic
algorithm (GA)
and classical
gradient-based
schemes
-included design search space restrictions,
which make the objective function not
continuously differentiable in design space
highly nonconvex
(Zohdi
2018)
Design feature
recommendation
Hierarchical
clustering and
SVM
-assist novice designers discover AM-
enabled design freedoms.
-only performance-centric design knowledge
(i.e. “loadings”, “objectives” and
“properties”) has been considered in AM
design feature recommendation.
(Yao, Moon
et al. 2017)
Tuning
microstructure
and
microhardness
SOM
- included physics-based models,
experimental measurements, and a data-
mining method.
- Dendrite arm spacing and microhardness
are approximated using the mechanistic
models.
(Gan, Li et
al. 2019)
Optimize build
orientation with
respect to build
time and part
mass
10 layer CNN
and linear
regression
model
- CNN are most precise at estimating all
three studied factors than the baseline linear
regression model for the training and
evaluation conditions explored.
(Williams,
Meisel et al.
2019)
flatness
perception
classification
tree (C4.5)
- The results indicated some differences in
the perception of flatness quality.
(Petrov,
Pernot et al.
2016)
Geometric
compensation
Feedforward
ANN
- used FE model to simulate the
deformations in the AM part
(Chowdhury
2016)


---


## Page 8


- geometrical compensation is performed on
the STL file of the part using the trained
network.
Part orientation
DL-ELM
- DL-ELM method is used to assessed part
orientation based on viewpoint preference,
visual saliency, smoothness entropy and area
of support.
- scores of a part printed in different
orientations are assessed.
(Zhang, Le
et al. 2015)
manufacturability
Heat Kernel
Signature
(HKS)
-speed up the product development process.
- reduce human error
(Shi, Zhang
et al. 2018)
Part estimation
Knowledge-
Based ANN
- a hybrid learning network that incorporates
topological zones obtained from knowledge
of the process and other zones where
missing knowledge is modelled using
classical ANNs.
-has better generalization capabilities and
uses fewer neurons for training.
(Nagarajan,
Mokhtarian
et al. 2019)
Efficient
numerical
modeling
ANN with a
fully-connected
layer with 1024
rectified linear
units, 2 LSTM-
cells with 1024
units
respectively
and a fully
connected
linear output
layer.
-reduction in computational time from hours
to milliseconds with good agreement in
result.
(Koeppe,
Hernandez
Padilla et al.
2018)
Stress prediction
2-stream CNN
- 16,700 models of data labels are created
using FEA simulation.
-parameters such as peak stress and
dependence on previous layer information
are investigated.
-The deep learning model outperforms the
simple neural network model used for stress
prediction.
(Khadilkar,
Wang et al.
2019)
Composite design CNN
-used ML for coarsegraining – analyzing
and designing materials without the use of
full microstructural data. The coarse-
graining is achieved by condensing a group
of building blocks into a single unit cell,
which greatly lowers the number of
parameters required in the ML algorithm.
(Gu, Chen
et al. 2018)
Designing
surrogate systems
ANN
- 7500 random thickness beams and
corresponding FE solutions are generated to
train the ANN.
- able to replicate the dynamic characteristic
of a target whose physical characteristics are
inaccessible or unknown.
(Sarlo and
Tarazaga
2016)


---


## Page 9


3.2 Part quality/process optimization
Process optimization is often performed when new materials or new processes are developed. Process
optimization of AM processes can be performed to obtain certain characteristics of the 3D printed parts
with variation in the process parameters. Process parameters affect the part properties for AM (Yu, Sing
et al. 2019, Kuo, Chua et al. 2020). A database of process-structure-properties (PSP) relationship for a
certain AM process and materials would enable the proper selection of the parameters based on the
available information in the database .
The PSP relationship is often complicated due to the high dimensionality of the process parameters,
making it difficult to establish the governing mathematical formula of the process. Due to its complex
nature, ML algorithms have been used to determine the PSP relationships for many AM.
Gan et al. attempted using SOM, an unsupervised ML technique, to identify the process-structure-
properties relationship of the directed energy deposition process for Inconel 718 (Figure 6) (Gan, Li et
al. 2019). Multiple objective optimizations of the process parameters can be achieved from the large
and high-dimensional dataset, which is obtained from simulation and validated with experimental
results, with the help of visualized SOM.

Figure 6 An illustration of the workflow normally used in current numerical studies (top row) and of experimental studies
(bottom row), accompanied by a description of how ML technique can be incorporated to discover useful process-structure-
property relationships of certain materials. (Gan, Li et al. 2019)

ANN (Lee, Park et al. 2001, Shen, Yao et al. 2004, Vosniakos, Maroulis et al. 2007, Rong-Ji, Xin-hua
et al. 2008, Munguía, Ciurana et al. 2009, Sood, Ohdar et al. 2009, Wang, Li et al. 2009, Equbal, Sood
et al. 2011, Sood, Equbal et al. 2012, Sood, Ohdar et al. 2012, Noriega, Blanco et al. 2013, Saqib,
Urbanic et al. 2014, Vijayaraghavan, Garg et al. 2014, Xiong, Zhang et al. 2014, Chen and Zhao 2015,


---


## Page 10


Wang, Jiang et al. 2015, Asadi-Eydivand, Solati-Hashjin et al. 2016, Ding, Pan et al. 2016, Ding, Shen
et al. 2016, Mohamed, Masood et al. 2016, Vahabli and Rahmati 2016, Bayraktar, Uzun et al. 2017,
Zhang, Mehta et al. 2017, Caiazzo and Caggiano 2018, Deng, Feng et al. 2018, Qi, Chen et al. 2019)
is the most commonly used ML technique for process optimization, although other techniques such as
genetic algorithm (GA) (Vosniakos, Maroulis et al. 2007, Rong-Ji, Xin-hua et al. 2008, Jiang, Liu et al.
2014), multigene-genetic programming (MGGP)(Vijayaraghavan, Garg et al. 2014), random forest
network (RFN) (Li, Zhang et al. 2019), support vector regression (SVR)(Li, Zhang et al. 2019),
ensemble algorithms (He, Yang et al. 2019, Li, Zhang et al. 2019), Siamese network (He, Yang et al.
2019), fuzzy C-means (Li, Dong et al. 2009, Equbal, Sood et al. 2011), and k-means(Li, Dong et al.
2009) have also been used. For example, Sario et al. used ANN to design 3D printed surrogate systems
that match the dynamic characteristic of a target whose physical characteristic is not available(Sarlo
and Tarazaga 2016). 7500 random thickness profiles of beams were generated to train the ANN model
to predict the suitable thickness profile of the beam for a certain frequency or mode shape. It is found
that the ANN algorithm can predict surrogates with low modal error (<12%) and moderate frequency
error (<18%).
3-layer ANN structure is sufficient for process optimization, with the first layer being the input layer,
second being the hidden layer, and third being the output layer. The number of neurons in the first layer
depends on the number of input process parameters of the study. The number of neurons in the third
layer is determined by the number of properties to be optimized which is typically one or two. The
number of neurons in the hidden layer is normally more than that of the input layer. The number of
neurons in the hidden layer selected must be appropriate to avoid overfitting or underfitting issues in
ML. Overfitting occurs when noise in the training data is captured and learned as concepts by the model.
In contrast, underfitting refers to the lack of fit of the model to the training data, which means the
reasonable relationship between the data and the model is not obtained.
Normalization of the input parameters is essential before they are used for ML models as it helps the
ANN to learn faster and make sure the inputs are incomparable range. If the inputs are of different
scales, the weights linked to some inputs will be updated much faster than other ones, which is
undesirable. Hence, they are usually linearly normalized to be in the range of either [0,1] or [-1,1] using

ri−rmin
rmax−rmin  (Jiang, Liu et al. 2014, Vahabli and Rahmati 2016, Deng, Feng et al. 2018)

2ri−rmin
rmax−rmin −1 (Xiong, Zhang et al. 2014, Asadi-Eydivand, Solati-Hashjin et al. 2016, Ding, Shen et al.
2016),
where ri is the particular input data, rmin is the smallest input data and rmax is the largest input data,
respectively.
The accuracy of the ANN model also depends on the size of the training data used to train the ANN
model (Qi, Chen et al. 2019). A dataset of 16 to few hundreds samples could generally give error lesser
than 10% (Qi, Chen et al. 2019).
Various studies have compared ML algorithms with conventional optimization methods such as
Taguchi method (Sood, Ohdar et al. 2009, Chen and Zhao 2015, Ding, Shen et al. 2016), polynomial
regression model (Sood, Ohdar et al. 2012, Xiong, Zhang et al. 2014, Mohamed, Masood et al. 2016),
ANOVA (Sood, Equbal et al. 2012, Sood, Ohdar et al. 2012, Saqib, Urbanic et al. 2014, Mohamed,
Masood et al. 2016, Bayraktar, Uzun et al. 2017). In the study of bead geometry prediction during single
track melting using laser welding and gas metal arc welding (Figure 7), 4-12-2 ANN was found to
achieve a lower mean of errors registering 1.922% and 2.104% as compared to a second-order
regression model with a mean of errors of 2.633% and 2.308% for bead width and bead hight predictions
(Xiong, Zhang et al. 2014). In another study to predict the dynamic modulus of elasticity of 3D printed
parts, ANN was found to have the better predictive ability by achieving higher R2 value and lower


---


## Page 11


absolute average deviation as compared to the fractional factorial model despite having limited numbers
of experiments (Mohamed, Masood et al. 2016).

Figure 7 Process optimization for the robotic WAAM system (Ding, Pan et al. 2016).
In the study to predict the wear characteristics, a 5-8-1 ANN model was able to achieve a higher
correlation coefficient (R2 value) of 0.9902 in comparison to the regression model’s 0.9516. The ability
of ANN models to capture the non-linearity between the input and output parameters has allowed
complex AM process mathematical models to be determined with higher accuracy.
Table
2
summarizes the use of ML algorithms in AM process optimization, the input process parameters, and
the target properties.
Table 2 The use of ML for process optimization of AM processes
Process
Purpose
Method
Input parameters
Accuracy
Ref.
FFF
 Optimize
compressive
strength
Resilient
backpropagati
on (RBP)
ANN
Layer thickness,
orientation, raster angle,
raster width, airgap
80.8
(Sood,
Ohdar et al.
2012)
FFF
Predict wear
volume
5-8-1 RBP
ANN
Layer thickness,
orientation, raster angle,
raster width, airgap
-
(Sood,
Equbal et
al. 2012)
FFF
wear
MGGP,
SVR,
ANN
Layer thickness,
Orientation, Raster angle,
Raster width, Air gap
93
(Vijayaragh
avan, Garg
et al. 2014)
FFF
Predicting
Volumetric
error
GA, ANN
Orientation, slice thickness
-
(Vosniakos,
Maroulis et
al. 2007)
FFF
Dimensional
accuracy
Fuzzy logic,
NN, Taguchi
Layer thickness,
orientation, raster angle,
raster width, airgap
-
(Equbal,
Sood et al.
2011)
FFF
Dimensional
accuracy
Grey
Taguchi, BP-
NN
Layer thickness,
orientation, raster angle,
raster width, airgap
-
(Sood,
Ohdar et al.
2009)
FFF
Surface
roughness
Ensemble
algorithm*

Layer thickness, extruder
temperature, feed rate to
flow rate
93
(Li, Zhang
et al. 2019)


---


## Page 12


FFF
Geometric
accuracy
ANN
Part angle, and distance
between parallel faces
-
(Noriega,
Blanco et
al. 2013)
FFF
Scaffold
wire width
ANN and GA
Platform movement speed,
extrusion speed, nozzle
diameter, fiber spacing
-
(Jiang, Liu
et al. 2014)
FFF
Dynamic
modulus of
elasticity
ANN
Layer thickness,
Air gap,
Raster angle,
Build orientation, Road
width,
Number of contours
91.7
(Mohamed,
Masood et
al. 2016)
FFF
Tensile
strength
ANN
Thickness,
Temperature, Raster pattern
96
(Bayraktar,
Uzun et al.
2017)
FFF
Surface
roughness
RBF ANN-
Imperialist
competitive
algorithm
(ICA)
Layer thickness,
Build angle
96
(Vahabli
and
Rahmati
2016)
Ceramic
slurry
extrusion
Extrusion
time, width
deformation
5-11-2 ANN
amount of dispersant SD-
03, glycerol, polyethylene
glycol, HPMC and solid
content
97.4
(Deng,
Feng et al.
2018)
Binder Jet
Predicting
surface
roughness,
shrinkage
rate in y and
z directions
3-layer BP-
ANN
Layer thickness, printing
saturation, heater power
ratio, drying time
-
(Chen and
Zhao 2015)
Binder jet
Compressiv
e strength,
open
porosity
Aggregated
ANN
Orientation, layer
thickness, delay time
96.5
(Asadi-
Eydivand,
Solati-
Hashjin et
al. 2016)
SLS
density
4-9-1 ANN
Laser power, scan speed,
scan spacing, layer
thickness
-
(Shen, Yao
et al. 2004)
SLS
dimension
Radial basic
function
ANN, fuzzy
C-means and
pseudo-
inverse
method, k-
means
Laser power, scan speed,
scan spacing, layer
thickness
-
(Li, Dong
et al. 2009)
SLS
Build time
ANN
Z height, volume, bounding
box
-
(Munguía,
Ciurana et
al. 2009)
SLS
Shrinkage
ratio
ANN, GA
Laser power, scan speed,
hatch spacing, layer
thickness, scan mode,
temperature, interval time
87.3
(Rong-Ji,
Xin-hua et
al. 2008)


---


## Page 13


SLS
Tensile
strength
ANN
Laser power, scan speed,
hatch spacing, layer
thickness, powder
temperature
-
(Wang,
Jiang et al.
2015)
SLS
Density
ANN
Laser power, scan speed,
hatch spacing, layer
thickness, scan mode,
temperature, interval time
-
(Wang, Li
et al. 2009)
SLM
porosity
RFN
Part position and
orientation, recycled
powder content
-

SLM
Keyhole
porosity
k-means
clustering
Energy density
40-44
(Snell,
Tammas-
Williams et
al. 2019)
SLA
Dimensional
accuracy
ANN
Layer thickness, border
overcure, hatch overcure,
fill cure depth, fill spacing
and hatch spacing
-
(Lee, Park
et al. 2001)
SLA
printability
Ensemble
method,
Siamese
network
Print speed
Ensemble
: 73
Siamese:
88
(He, Yang
et al. 2019)
LMD
Geometrical
accuracy
ANN
Laser power, scanning
speed, powder feeding rate
94.2-98%
(Caiazzo
and
Caggiano
2018)
EBM
Volume,
roughness
ANN
Spreader translation speed,
rotation speed
97.5%
(Zhang,
Mehta et al.
2017)
WAAM
Offset
distance
3-12-1 ANN
Bead width, height, center
distance of adjacent
deposition paths
-
(Qi, Chen
et al. 2019)
Arc
welding
Bead
geometry
(width and
height)
ANN
Wire-feed rate, travel
speed,
Stick-out
-
(Ding,
Shen et al.
2016)
Arc
welding
Bead
geometry
(width and
height)
4-12-2 ANN
wire feed rate (F), welding
speed (S), arc voltage (V),
and nozzle-to-plate distance
(D)
93
(Xiong,
Zhang et al.
2014)
Wire and
arc
additive
manufact
uring
(WAAM)
Bead
geometry
(width and
height)
2-13-2 ANN
Wire-feed rate, travel speed
98
(Ding, Pan
et al. 2016)
Laser
cladding
Melt pool
width
ANN
Laser power, Powder feed
rate, Laser speed, Focal
length,  Contact tip to
work-piece distance
-
(Saqib,
Urbanic et
al. 2014)
* Contains classification and regression trees (CART), Random vector functional link (RVFL),
network Ridge regression (RR), SVR, Random forests (RF) AdaBoost


---


## Page 14


3.3 In-situ monitoring for quality control
In-situ monitoring of the AM process could potentially improve the reliability and repeatability of the
3D printed parts through the means of closed-loop feedback control with the help of sensors. By
detecting defects during the printing process, in-process corrective printing could be realized, which
could potentially facilitate in-process part qualification.
Active research about quality monitoring of AM techniques have been on (1) obtaining melt pool
temperature history through means of pyrometers and high-speed camera, (2) defect detection at every
individual level by analyzing images obtained by the optical camera, near-infrared thermal CMOS
cameras, photodiodes, and x-ray phase-contrast imaging (XPCI) (Zhao, Fezzaa et al. 2017, Le-Quang,
Shevchik et al. 2018, Wasmer, Le-Quang et al. 2018) and/or x-ray computed tomography (CT) of the
entire workpiece (Thompson, Maskery et al. 2016).  These measurements are then used to infer the
existence of potential defects in the build process (Figure 8). Gobert et al. highlighted that image
resolution, lighting condition, and the number of sensors or cameras are key to improving the
performance of the in-situ monitoring (Gobert, Reutzel et al. 2018).

Figure 8 An example of porosity prediction method utilizing supervised ML(Khanzadeh, Chowdhury et al. 2018)
Detection of flaws through human-created condition-based algorithms requires an in-depth
understanding of the printing process as well as the computer vision knowledge. Such condition-based
algorithms are more restrictive as new algorithms have to be generated when new materials become
available, or when new part geometries are introduced as this method needs to take the interactions
between various parameters into consideration. The reliance on the human operator makes condition-
based algorithms less practical.
ML allows anomaly detection through a large dataset of good printing samples and bad printing samples
and the detection capability can be improved by adding new training data.
As most of the in-situ monitoring uses cameras to acquire information about the printing condition,
defect detection relies heavily on the capability of computer vision (CV). The most used ML technique
in computer vision is CNN (Figure 9), although other techniques have been used as well. For instance,
Scime and Beuth used scale invariant feature transform (SIFT) to extract melt pool features and adopted
various features extraction techniques such as a bag of words (BoW), histogram of oriented gradients


---


## Page 15


(HOG) clustering  to extract useful features from images and form feature vectors. The feature vector
is then fed to SVM image claissification algorithm to learn the defects such as under-melting, keyholing,
and balling (Scime and Beuth 2019). They also attempted using ML techniques with CV to detect
anomalies such as recoater hopping, recoater streaking, debris, superelevation, part failure, and
incomplete powder spreading.

Figure 9 CNN used in computer vision for in-situ monitoring of AM process (Scime and Beuth 2018)
Although the ML algorithm can predict no anomaly with 100% accuracy, the algorithm was not able to
predict recoater streaking with high accuracy (50.6%) (Scime and Beuth 2018). They compared the
BoW technique with multiscale CNN (MsCNN) and found that MsCNN can achieve higher
classification accuracies but it is more computationally expensive (75% slower) (Scime and Beuth
2018). Self-Organizing Error-Driven Neural Networks (SOEDNN), a combination of SOM ann ANN,
is found to be more accurate in classifying porosity defects than K Nearest Neighbor (KNN), and multi-
layer perceptron (MLP) (Jafari-Marandi, Khanzadeh et al. 2019).  KNN is a supervised classification
algorithm that will give new data points accordingly to the k number or the closest data points.  Another
group of researchers used spectral CNN and reinforced learning algorithm to classify the acoustic
emission features obtained from the fiber-Bragg grating (FBG) sensor to predict the quality of the prints.
Spectral convolutional neural networks (SCNN) was found to have higher classification accuracies (83,
85 and 89 % for high, medium and poor workpiece qualities) (Shevchik, Kenel et al. 2018) compared
to the reinforced learning technique (74, 79 and 82% for high, medium and poor workpiece qualities)
(Wasmer, Le-Quang et al. 2018). Ye et al. used a deep belief algorithm that consists of stacking
restricted Boltzmann machines (RBMs), which has undirected connections between its top two layers
and directed connections between all following adjacent layers, to classify the plume and spatter with
minimum preprocessing and no feature extraction. The deep belief algorithm can achieve a 83.4%
accuracy rate(Ye, Hsi Fuh et al. 2018). In another work to extract melt pool, plume, and splatter data,
CNN (92.7%) was found to have higher classification accuracy as compared to SVM (89.6%) and the
combination of SVM and principle component analysis (PCA) (90.1%)(Zhang, Hong et al. 2018). A
summary of the use of ML in in-situ monitoring of AM processes is shown in Table 3.


---


## Page 16


Table 3 The use of ML in in-situ monitoring of AM processes
Technique
s
Type of
sensors
Machine
learning
technique
Kernel
size
Type of
defects
Accurac
y
Ref.
PBF
one
megapixel
Photron
FASTCAM
Mini AX200
high-speed
camera
-BoW
- SIFT
- HOG
-k-means
unsupervise
d clustering
algorithm
2x2
desirable,
balling,
severe
keyholing,
keyholing
porosity, or
under-
melting
-
(Scime and
Beuth 2019)
PBF
Optical
camera
Reinforced
learning
-
Surface
roughness
96
(Benoit, Rana
et al. 2018)
PBF
EOS M290
stock camera
(1280X1024
pixels)
bag-of-
keypoints
- filter
responses
k-means
unsupervise
d clustering
algorithm
20X20,
10X40,
100X100
Recoater
hopping,
Recoater
streaking,
Debris,
Super-
elevation,
Part failure,
Incomplete
spreading
83.4
(Scime and
Beuth 2018)
PBF
DSLR camera
(Nikon
D800E)( 7360
× 4912 pixels)

-
anomaly
91.5
(Abdelrahma
n, Reutzel et
al. 2017)
PBF
10.55 Mpix
IDS UI-
5490SE-C-
HQ camera
(3840×2749
Pixel
Active
Contours
without
Edges
(ACWE)
bias field
estimation
(LSE BFE)
-
Geometric
deviation



(Caltanissetta
, Grasso et al.
2018)
PBF
Mikrotron
EOsens
MC1362
(256x256
pixels) at
1000FPS
CNN-tensor
flow
64X64
Melt pool
size, Track
continuity
93.1
(Yuan, Guss
et al. 2018)
PBF
Photodiode
(100kHz)
Semi-
supervised
Gaussian
Mixture
Model
(GMM)
Expectation
Maximizatio
n (EM)
algorithm
-
-
70
(Okaro,
Jayasinghe et
al. 2019)
PBF
FASTCAM
Mini
deep belief
network
Down-
sized
plume and
spatter
83.40
(Ye, Hsi Fuh
et al. 2018)


---


## Page 17


UX50/100
high-speed
NIR camera
5000 fps
(DBN)
restricted
Boltzmann
machine
image of
100x125

PBF
high-speed
camera 2000
fps
Principal
component
analysis,
SVM, CNN

11x11
5x5
3x3
melt pool,
plume and
spatters

92.8
(Zhang,
Hong et al.
2018)
PBF
DSLR Nikon
D800E 36.3-
megapixels
linear SVM
CNN
3,5,7,9,11
voxels
Discontinuiti
es such as
incomplete
fusion,
porosity,
cracks, or
inclusions
85
(Gobert,
Reutzel et al.
2018)
PBF
EOS M290
stock camera
(1280X1024
pixels)
Multiscale
CNN
25X25,
100X100,
Downsize
d
200X200
Recoater
hopping,
Recoater
streaking,
Debris,
Super-
elevation,
Part failure,
Incomplete
spreading
85
(Scime and
Beuth 2018)
PBF
Inline
coherent
imaging
(Laser Depth
Dynamics
LD-600-AL)
(200kHz)
-
-
-
-
(Kanko,
Sibley et al.
2016)
PBF
co-axial
pyrometer
camera (480 ×
752)
dual control
charting
system that
consists of
Hoteling’s
T2 and Q
charts
130x130
25x36
6x6
porosity and
mini-cracks
90.97
(Khanzadeh,
Tian et al.
2018)
LENS
dual-
wavelength
pyrometer
(Stratonics,
Inc.) and an
IR camera
(Sierra-
Olympic
Technologies,
Inc.
Viento320)
KNN, SVM,
decision
tree,
discriminant
analysis
-
porosity
recall
value
(98.44%
)
(Khanzadeh,
Chowdhury
et al. 2018)
FFF
Differential
wide-band AE
sensor, a PAC
SOM’s
clustering
-
Scratching &
hitting,
-
(Wu, Yu et
al. 2019)


---


## Page 18


2/4/6
preamplifier,
and a PAC
PCI-2 DAQ
system. (50
kHz- 900
kHz) (10 M
samples per
second)
Fiber
debonding &
material
peeling off,
Material
rubbing &
sliding

3.4 Cloud 3D printing service platform
The cloud platform is integral in popularizing 3D printing and advancing towards industry 4.0.  It is a
server-based computing model that consists of both hardware and software resources. It enables the
sharing of resources to a public repository, including 3D models or printing services, and integrates
them to form a comprehensive pool of resources (Figure 10) (Wang, Wang et al.).
ML algorithms can learn to do service evaluation and demand matching to allow extensive assessment
of terminal printers and manage the resources intelligently based on printing accuracy, quality, cost and
time (Wu, Peng et al. 2016). ML also enables features recommendation for designs to allow intelligent
customization of products (Yao, Moon et al. 2017). This lowers the entry barrier for public users.
Resource allocation algorithms have been used to develop adaptive and collective management of
resources (Wang, Wang et al.). Using an optimization algorithm based on fuzzy number different
quantization by hamming distance, Wu et al. quantified the service quality and improve the accuracy
of service selection (Wu, Peng et al. 2016). In another work, Dong et al. used GA to create a quality of
service (QoS) acquisition method and a trust evaluation model for cloud manufacturing service (Dong
and Guo 2014).

Figure 10 Parameters of customization demand and 3D printing service(Mai, Zhang et al. 2016)
3.5 Security of attack detection
3D printing takes an important role in the Industry 4.0, where file sharing and cloud manufacturing has
gained more attention in recent years. Cyber-security for 3D printing is a growing concern as attacks
on the systems may lead to unwanted flaws to the products through the malicious alteration of process
parameters. ML can be applied to circumvent such situations.


---


## Page 19


To spot malicious attacks spontaneously in the FFF technique, Wu et al. applied three supervised
learning algorithms, namely k Nearest Neighbours (kNN) algorithm, random forest algorithm, and an
unsupervised anomaly detection algorithm to detect anomalies (Wu, Song et al. 2017). Images obtained
from the optical camera are transformed into a greyscale plot. Features such as grayscale mean, standard
deviation, number of pixels higher than the threshold value are extracted from the grayscale value
distribution. The study has shown that the unsupervised anomaly detection learning algorithm was able
to achieve higher accuracy (96.1%) as compared to kNN (87.5%) and random forest (95.5%).
Faruque attempted using supervised and unsupervised K-Means ML algorithms to detect cyberattacks
from information such as the design specification of the printed parts and the thermal history of the 3D
printer (Figure 11) (Faruque 2016). However, the inadequate amount of thermal camera, low sampling
frequency and resolution and the lack of dynamic focus capability of the camera have limited the
performance of the attack detection.

Figure 11 Workflow of cyberattack detection in AM using ML (Faruque 2016).
File sharing has lowered the difficulty of an average user to access and fabricate various parts using 3D
printing. It could pose threats to the community if 3D models of some dangerous weapons are shared
online and fabricated using 3D printers. Pham et al. proposed an anti-weapon model detection algorithm
that can be used to prevent sharing and printing of the restriction items (Pham, Lee et al. 2018). In the
proposed algorithm, facets and vertices are extracted to form pairs of random points from the 3D mesh
(Figure 12). The distances between the pairs of two points are then calculated. The D2 shape distribution,
which is a distribution of Euclidean distances of the pairs, is then calculated to obtain a D2 vector. The
D2 vectors are then used to train the CNN to detect firearm and knife models. CNN is found to have an
accuracy of 98.03% which is higher than other methods that used depth image (Wohlkinger and Vincze
2011).


---


## Page 20


Figure 12 Workflow of 3d weapon model detection for AM(Pham, Lee et al. 2018)
4. Potential and challenges
In this section, the potential of ML in 3D printing for various fields and the challenges faced when
applying the ML algorithm in 3D printing are discussed in detail.
4.1 Potential
4.1.1 Medical
AM anatomical models can result in more precise treatment planning, better communication, and
improved training and education. The fabrication of anatomical models involves image acquisition and
reconstruction of the anatomy using CT, image segmentation, and finally printing of the anatomical
models (van Eijnatten, van Dijk et al. 2018, Radzi, Tan et al. 2020).
The precision of the models relies heavily on the imaging and image segmentation steps. Gassman et
al. attempted using ANN to perform the segmentation to reduce the possibility of rater drift and inter-
rater variability (Gassman, Powell et al. 2008). The ANN also saves time and effort to manually obtain
the data of interest, enabling the possibility of tailor-made models for patients. Material tuning of multi-
material printing using material jetting techniques such as polyjet can be performed by training the ML
algorithm to learn from the large dataset of mechanical properties and doctors’ input on haptic
perception. However, Huff et al. pointed out that having a large dataset for every organ system for


---


## Page 21


training the ML algorithm is challenging but necessary step towards realizing these personalized
anatomical models (Huff, Ludwig et al. 2018).
4.1.2 Tissue engineering
Bioprinting is an emerging field in tissue engineering that utilizes 3D printing processes to print bio-
inks to fabricate tissue-like structures (Khan, Kahin et al. 2019, Mishbak, Cooper et al. 2019). ML can
be useful in predicting material properties of the various mixture composition of the bio-inks as well as
coming up with new scaffold designs that suit specific purpose through learning from a large database
of materials and designs (Yu and Jiang 2020). Multiple objectives optimization of the printing of bio-
ink using ML algorithms can be performed. For instance, Menon et al. applied hierarchical machine
learning to concurrently optimize material, process variables, and formulate additive manufacturing of
silicone elastomer through freeform reversible embedding (Menon, Póczos et al. 2019).
4.1.3 Building & constructions
The use of ML in 3D printing for building and constructions can cover various aspects including
material, design and process (Lim, Tan et al. 2018, Lao, Li et al. 2020). The search for new 3D printing
materials with specific performance such as high compression and tensile properties, strong crack
resistance and toughness, short setting time and high setting strength can be done by training the ML
algorithms to detect features and patterns from a large database of available material properties. ML
can also allow quantity surveying to be done easier using the past relevant cases to predict the amount
of material needed and provide a precise budget for targetted cost control. New and novel data-driven
design of 3D printable structures that are multifunctional and more sophisticated (Sanjayan and
Nematollahi 2019) can be created using the ML technique. The tool path planning of multiple robots
for 3D printing requires a good understanding of the dynamic mechanical behavior of the extruded
material as well as the synchronization of the robots (Al Jassmi, Al Najjar et al. 2018). ML can also be
applied to learn a large number of process plans and to optimize the material consumption and reduce
the build time by comparing the cost of the various plans.
4.2 Challenges
4.2.1 Computational cost
Data-driven numerical simulations using ML techniques are found to be more computationally efficient
as compared to physics-based numerical simulations. The stress prediction of lattice structure from a
trained ML model takes about 0.47 s as compared to a FEM simulation which would take 5-10 h to
complete (Koeppe, Hernandez Padilla et al. 2018). In another work, is found that stress prediction can
be made within milliseconds using data-driven CNN in comparison to FEA which took a few minutes
(Khadilkar, Wang et al. 2019). However, training a large data set can be computationally expensive and
time-consuming. Nagarajan employed knowledge based-ANN model to reduce the training time and
cost (Nagarajan, Mokhtarian et al. 2019). The knowledge-based ANN consists of four modular ANN,
where the output of the sub-ANN output is the input of another sub-ANN. By doing this, the knowledge-
based ANN can have 12 fewer neurons than the classical ANN and allow the hidden layers to work in
a more dimensionally homogeneous space, thus improving its efficiency.
Computational cost also plays an important role in in-situ monitoring and closed-loop control. Real-
time layer-by-layer defect detection and melt pool inspection require defects to be detected
spontaneously so as not to increase the build time which significantly affects the production rate. Scime
and Beuth compared the computational time of BoW and MsCNN for anomaly detection and found that
the computational time for each layer for the BoW technique was 4 s, which is shorter than that of the
MsCNN (7 s) (Scime and Beuth 2018). The detection operation was considered fast considering the
printing of a layer takes several minutes to finish. However, melt pool inspection with the high-speed
camera requires more computational power due to the larger data set. Better ML techniques are required


---


## Page 22


for this kind of application that involves a large data set. Francis and Bian used high- performance
computing to study the thermal-mechanical modeling using Convolutional and Artificial Neural
Network for Additive Manufacturing Prediction using Big Dat (CAMP-BD) deep learning algorithm
(Francis and Bian 2019). A total of 21818 thermal images are captured which amounts to 40 GB of data.
The training of the CAMP-BD took 26 days to finish using the supercomputer cluster at Mississippi
State.
4.2.2 Standards for qualification
The sharing of data is key to develop a large database, which is essential for ML algorithms to work.
With more groups of researchers working on new materials and process development, standards for
data acquisition and pre-processing of the data would ensure sharing of data and encourage
collaboration among the AM community. Besides, there are several ML frameworks such as
Tensorflow, Caffe, and Pytorch available in the markets. However, they are not compatible with each
other. Hence, it is important to have a unified framework to facilitate the sharing of ML models among
the research community.
4.2.3 Data acquisition techniques
ML algorithms learn from the data obtained from sensors and the performance of ML algorithms is only
as good as the quality of the input data. It is therefore important to have a reliable acquisition technique
to ensure that the data obtained can provide informative insights into the printing process. Apart from
that, it requires strong fundamental knowledge on image processing analysis to identify the most
suitable sensors to be used for capturing important features. For examples, Sensors used in 3D printing
processes that involve melting must have a high refresh rate and high resolution to capture the
information of the melt pools. These melt pools have high thermal gradients and heat transfer rates. Wu
et al. pointed out that blurriness due to the motion of the camera has resulted in lower accuracy as
compared to the simulation results (Wu, Song et al. 2017).
In spite of the huge range of sensors used, each in-situ monitoring technique has its limitations that
impede its use in the actual production line (Tapia and Elwany 2014, Everton, Hirsch et al. 2016).
Temperature measurement of the melt pool is restricted to the surface of the melt pool and contains no
information regarding the complicated fluid flow and heat transfer in the build direction. Due to the
high laser scan speed and fast-cooling nature of the process, expensive high-speed cameras are often
required and calibration of the emissivity of the melt pool can be challenging. Layer wise anomaly
detection using an optical camera or thermal camera offers an inexpensive way to detect defects. The
layer-wise anomaly detection can detect defects at the surface of each new layer after it is created but
not the pores or defects within the new layers. Although x-ray technologies such as XPCI and CT can
detect internal flaws for the study of origin and propagation of cracks, they are not suitable for real-time
monitoring applications. Also, the two x-ray methods technologies are expensive and time-consuming
(Thompson, Maskery et al. 2016, Zhao, Fezzaa et al. 2017, Le-Quang, Shevchik et al. 2018).
Furthermore, the sensor would need to be able to function properly in harsh printing conditions, such
as in elevated temperatures.
5. Conclusion
The use of ML in 3D printing covers a wide spectrum of applications, ranging from design for 3D
printing, process optimization, to in-situ monitoring. ML has been demonstrated to be a powerful tool
to perform data-driven numerical simulation, design features recommendation, real-time anomaly
detection, and cybersecurity (Figure 13).
ML has shown to outperform conventional optimization methods such as second-order polynomial
regression especially when dealing with high dimensionality data. ANN is found to be the most common
and efficient ML technique for process optimization. A 3-layer ANN is sufficient to achieve an accuracy


---


## Page 23


as high as 98%.  CNN is found to be more efficient than ANN in dealing with 2D images and 3D models
due to its ability to capture spatial features. Hence, CNN has found applications in feature recognition,
feature recommendation in designing objects for 3D printing, as well as anomaly detection in in-situ
monitoring.
Labelling of data is a tedious work and it requires the users to have a knowledge of the outcome of the
data. On the other hand, unsupervised learning is very useful when user does not know what to extract
from the data. It is often used in in-situ monitoring for anomaly detection without needing to have
labelled data. The learning performance can be greatly improved by using reinforced learning technique
where a small amount of labelled data is provided.
Potential applications and challenges have been identified and discussed. Large datasets are the key to
achieving high predicting and detecting accuracy. Data acquisition and processing in a standardized
format would make the sharing of 3D printing data easier among the AM community to build up a large
dataset. Developing more advanced ML algorithm techniques and higher computational power in the
future would see improved real-time in-situ monitoring and closed-loop feedback control. Classification
accuracy should be further improved to achieve higher detection rate and to reduce false detection rate.
As the quality of the input data greatly affects the performance of the ML algorithms, better sensors
with higher data acquisition rate and higher resolution would definitely improve the performance of the
ML algorithms. Advanced data compression technique that are more efficient would be required to
handle the large dataset from the sensors.
Future research should focus on multi-task learning that would significantly improve the reliability of
the model so that designers would be able to assess the functionality of AM products prior to actual
manufacturing. Such a predictive model will further accelerate the effort of realizing digital twins for
AM. It opens an exciting opportunity for ML to grow and be used in 3D printing applications.


Figure 13 Summary of AI in 3D printing
Acknowledgement
This research is supported by the National Research Foundation, Prime Minister’s Office, Singapore under its
Medium-Sized Centre funding scheme.


---


## Page 24


Declarations
Funding: National Research Foundation, Prime Minister’s Office, Singapore under its Medium-Sized Centre
funding scheme
Conflicts of interest: The authors declare no conflict of interest.
Availability of data and material: Not applicable
Code availability: Not applicable
References

Abdelrahman, M., E. W. Reutzel, A. R. Nassar and T. L. Starr (2017). "Flaw detection in powder bed
fusion using optical imaging." Additive Manufacturing 15: 1-11.
Aboulkhair, N. T., N. M. Everitt, I. Ashcroft and C. Tuck (2014). "Reducing porosity in AlSi10Mg parts
processed by selective laser melting." Additive Manufacturing 1: 77-86.
Acharya, R., J. A. Sharon and A. Staroselsky (2017). "Prediction of microstructure in laser powder bed
fusion process." Acta Materialia 124: 360-371.
Al Jassmi, H., F. Al Najjar and A.-H. I. Mourad (2018). Large-Scale 3D printing: the way forward. IOP
Conference Series: Materials Science and Engineering, IOP Publishing.
Asadi-Eydivand, M., M. Solati-Hashjin, A. Fathi, M. Padashi and N. A. Abu Osman (2016). "Optimal
design of a 3D-printed scaffold using intelligent evolutionary algorithms." Applied Soft Computing
39: 36-47.
Bacha, A., A. H. Sabry and J. Benhra (2019). "Fault Diagnosis in the Field of Additive Manufacturing
(3D Printing) Using Bayesian Networks." International Journal of Online and Biomedical Engineering
(iJOE) 15(03).
Bayraktar, Ö., G. Uzun, R. Çakiroğlu and A. Guldas (2017). "Experimental study on the 3D-printed
plastic parts and predicting the mechanical properties using artificial neural networks." Polymers for
Advanced Technologies 28(8): 1044-1051.
Benoit, N., H. Rana and A. Valamanesh (2018). Applying Machine Learning for Real Time
Optimization of Powder Bed Manufacturing, Worcester Polytechnic Institute.
Bin Maidin, S., I. Campbell and E. Pei (2012). "Development of a design feature database to support
design for additive manufacturing." Assembly Automation 32(3): 235-244.
Caiazzo, F. and A. Caggiano (2018). "Laser Direct Metal Deposition of 2024 Al Alloy: Trace Geometry
Prediction via Machine Learning." Materials (Basel) 11(3).
Caltanissetta, F., M. Grasso, S. Petrò and B. M. Colosimo (2018). "Characterization of in-situ
measurements based on layerwise imaging in laser powder bed fusion." Additive Manufacturing 24:
183-199.
Chen, H. and Y. F. Zhao (2015). Learning Algorithm Based Modeling and Process Parameters
Recommendation System for Binder Jetting Additive Manufacturing Process. ASME 2015
International Design Engineering Technical Conferences and Computers and Information in
Engineering Conference.
Chen, Q., G. Guillemot, C.-A. Gandin and M. Bellet (2017). "Three-dimensional finite element
thermomechanical modeling of additive manufacturing by selective laser melting for ceramic
materials." Additive Manufacturing 16: 124-137.
Chowdhury, S. (2016). Artificial neural network based geometric compensation for thermal
deformation in additive manufacturing processes, University of Cincinnati.
Deng, L., B. Feng and Y. Zhang (2018). "An optimization method for multi-objective and multi-factor
designing of a ceramic slurry: Combining orthogonal experimental design with artificial neural
networks." Ceramics International 44(13): 15918-15923.


---


## Page 25


Ding, D., Z. Pan, D. Cuiuri, H. Li, S. van Duin and N. Larkin (2016). "Bead modelling and
implementation of adaptive MAT path in wire and arc additive manufacturing." Robotics and
Computer-Integrated Manufacturing 39: 32-42.
Ding, D., C. Shen, Z. Pan, D. Cuiuri, H. Li, N. Larkin and S. van Duin (2016). "Towards an automated
robotic arc-welding-based additive manufacturing system from CAD to finished part." Computer-
Aided Design 73: 66-75.
Dong, Y. and G. Guo (2014). "Evaluation and selection approach for cloud manufacturing service
based on template and global trust degree." Computer Integrated Manufacturing Systems 20(1):
207-214.
Equbal, A., A. K. Sood and S. S. Mahapatra (2011). "Prediction of dimensional accuracy in fused
deposition modelling- a fuzzy logic approach." International Journal of Productivity and Quality
Management 7(1): 22-43.
Everton, S. K., M. Hirsch, P. Stravroulakis, R. K. Leach and A. T. Clare (2016). "Review of in-situ
process monitoring and in-situ metrology for metal additive manufacturing." Materials & Design 95:
431-445.
Faruque, M. A. A. (2016). "Forensics of Thermal Side-Channel in Additive Manufacturing systems."
Fergani, O., F. Berto, T. Welo and S. Liang (2017). "Analytical modelling of residual stress in additive
manufacturing." Fatigue & Fracture of Engineering Materials & Structures 40(6): 971-978.
Francis, J. and L. Bian (2019). "Deep Learning for Distortion Prediction in Laser-Based Additive
Manufacturing using Big Data." Manufacturing Letters 20: 10-14.
Gan, Z., H. Li, S. J. Wolff, J. L. Bennett, G. Hyatt, G. J. Wagner, J. Cao and W. K. Liu (2019). "Data-
Driven Microstructure and Microhardness Design in Additive Manufacturing Using a Self-Organizing
Map." Engineering 5(4): 730-735.
Garg, A., J. S. L. Lam and M. M. Savalani (2016). A New Variant of Genetic Programming in
Formulation of Laser Energy Consumption Model of 3D Printing Process. Handbook of Sustainability
in Additive Manufacturing: Volume 1. S. S. Muthu and M. M. Savalani. Singapore, Springer
Singapore: 31-50.
Gassman, E. E., S. M. Powell, N. A. Kallemeyn, N. A. DeVries, K. H. Shivanna, V. A. Magnotta, A. J.
Ramme, B. D. Adams and N. M. Grosland (2008). "Automated bony region identification using
artificial neural networks: reliability and validation measurements." Skeletal radiology 37(4): 313-
319.
Gobert, C., E. W. Reutzel, J. Petrich, A. R. Nassar and S. Phoha (2018). "Application of supervised
machine learning for defect detection during metallic powder bed fusion additive manufacturing
using high resolution imaging." Additive Manufacturing 21: 517-528.
Gu, G. X., C.-T. Chen and M. J. Buehler (2018). "De novo composite design based on machine learning
algorithm." Extreme Mechanics Letters 18: 19-28.
Gu, G. X., C.-T. Chen, D. J. Richmond and M. J. Buehler (2018). "Bioinspired hierarchical composite
design using machine learning: simulation, additive manufacturing, and experiment." Materials
Horizons 5(5): 939-945.
He, H., Y. Yang and Y. Pan (2019). "Machine learning for continuous liquid interface production:
Printing speed modelling." Journal of Manufacturing Systems 50: 236-246.
Huff, T. J., P. E. Ludwig and J. M. Zuniga (2018). "The potential for machine learning algorithms to
improve and reduce the cost of 3-dimensional printing for surgical planning." Expert Rev Med
Devices 15(5): 349-356.
Jafari-Marandi, R., M. Khanzadeh, W. Tian, B. Smith and L. Bian (2019). "From in-situ monitoring
toward high-throughput process control: cost-driven decision-making framework for laser-based
additive manufacturing." Journal of Manufacturing Systems 51: 29-41.
Jiang, Z., Y. Liu, H. Chen and Q. Hu (2014). Optimization of Process Parameters for Biological 3D
Printing Forming Based on BP Neural Network and Genetic Algorithm. 21st ISPE Inc. International
Conference on Concurrent Engineering.


---


## Page 26


Kanko, J. A., A. P. Sibley and J. M. Fraser (2016). "In situ morphology-based defect detection of
selective laser melting through inline coherent imaging." Journal of Materials Processing Technology
231: 488-500.
Khadilkar, A., J. Wang and R. Rai (2019). "Deep learning–based stress prediction for bottom-up SLA
3D printing process." The International Journal of Advanced Manufacturing Technology 102(5-8):
2555-2569.
Khan, Z., K. Kahin, S. Rauf, G. Ramirez-Calderon, N. Papagiannis, M. Abdulmajid and C. Hauser (2019).
"Optimization of a 3D bioprinting process using ultrashort peptide bioinks." International Journal of
Bioprinting 5(1): 173.
Khanzadeh, M., S. Chowdhury, M. Marufuzzaman, M. A. Tschopp and L. Bian (2018). "Porosity
prediction: Supervised-learning of thermal history for direct laser deposition." Journal of
Manufacturing Systems 47: 69-82.
Khanzadeh, M., W. Tian, A. Yadollahi, H. R. Doude, M. A. Tschopp and L. Bian (2018). "Dual process
monitoring of metal-based additive manufacturing using tensor decomposition of thermal image
streams." Additive Manufacturing 23: 443-456.
Koeppe, A., C. A. Hernandez Padilla, M. Voshage, J. H. Schleifenbaum and B. Markert (2018).
"Efficient numerical modeling of 3D-printed lattice-cell structures using neural networks."
Manufacturing Letters 15: 147-150.
Kuo, C. N., C. K. Chua, P. C. Peng, Y. W. Chen, S. L. Sing, S. Huang and Y. L. Su (2020). "Microstructure
evolution and mechanical property response via 3D printing parameter development of Al–Sc alloy."
Virtual and Physical Prototyping 15(1): 120-129.
Lao, W., M. Li, T. N. Wong, M. J. Tan and Tjahjowidodo (2020). "Improving surface finish quality in
extrusion-based 3D concrete printing using machine learning-based extrudate geometry control."
Virtual and Physical Prototyping 15(2): 178-193.
Le-Quang, T., S. Shevchik, B. Meylan, F. Vakili-Farahani, M. Olbinado, A. Rack and K. Wasmer (2018).
"Why is in situ quality control of laser keyhole welding a real challenge?" Procedia CIRP 74: 649-653.
Le-Quang, T., S. A. Shevchik, B. Meylan, F. Vakili-Farahani, M. P. Olbinado, A. Rack and K. Wasmer
(2018). "Why is in situ quality control of laser keyhole welding a real challenge?" Procedia CIRP 74:
649-653.
Lee, S. H., W. S. Park, H. S. Cho, W. Zhang and M. C. Leu (2001). "A neural network approach to the
modelling and analysis of stereolithography processes." Proceedings of the Institution of Mechanical
Engineers, Part B: Journal of Engineering Manufacture 215(12): 1719-1733.
Li, X.-f., J.-h. Dong and Y.-z. Zhang (2009). Modeling and Applying of RBF Neural Network Based on
Fuzzy Clustering and Pseudo-Inverse Method. 2009 International Conference on Information
Engineering and Computer Science, Wuhan, China, IEEE.
Li, Z., Z. Zhang, J. Shi and D. Wu (2019). "Prediction of surface roughness in extrusion-based additive
manufacturing with machine learning." Robotics and Computer-Integrated Manufacturing 57: 488-
495.
Lim, C. W., K. Tan and X. Zhu (2018). "The Framework of Combining Artificial Intelligence and
Construction 3D Printing in Civil Engineering." MATEC Web of Conferences 206.
Liu, T., S. Guessasma, J. Zhu, W. Zhang, H. Nouri and S. Belhabib (2018). "Microstructural defects
induced by stereolithography and related compressive behaviour of polymers." Journal of Materials
Processing Technology 251: 37-46.
Ludwig, M., G. Meyer, I. Tastl, N. Moroney and M. Gottwals (2018). An appearance uniformity metric
for 3D printing. Proceedings of the 15th ACM Symposium on Applied Perception. Vancouver, British
Columbia, Canada, ACM: 1-8.
Madara, S. R. and C. P. Selvan (2017). "Review of Recent Developments in 3-D Printing of Turbine
Blades." European Journal of Advances in Engineering and Technology 4(7): 497-509.
Mai, J., L. Zhang, F. Tao and L. Ren (2016). "Customized production based on distributed 3D printing
services in cloud manufacturing." The International Journal of Advanced Manufacturing Technology
84(1-4): 71-83.


---


## Page 27


Meng, L., J. Zhao, X. Lan, H. Yang and Z. Wang (2020). "Multi-objective optimisation of bio-inspired
lightweight sandwich structures based on selective laser melting." Virtual and Physical Prototyping
15(1): 106-119.
Menon, A., B. Póczos, A. W. Feinberg and N. R. Washburn (2019). "Optimization of Silicone 3D
Printing with Hierarchical Machine Learning." 3D Printing and Additive Manufacturing 6(4): 181-189.
Mishbak, H. H., G. Cooper and P. J. D. S. Bartolo (2019). "Development and Characterisation of a
Photocurable Alginate Bioink for 3D Bioprinting." International Journal of Bioprinting 5(2): 189.
Mohamed, O. A., S. H. Masood and J. L. Bhowmik (2016). "Investigation of dynamic elastic
deformation of parts processed by fused deposition modeling additive manufacturing." Advances in
Production Engineering & Management 11(3): 227-238.
Munguía, J., J. Ciurana and C. Riba (2009). "Neural-network-based model for build-time estimation in
selective laser sintering." Proceedings of the Institution of Mechanical Engineers, Part B: Journal of
Engineering Manufacture 223(8): 995-1003.
Nagarajan, H. P. N., H. Mokhtarian, H. Jafarian, S. Dimassi, S. Bakrani-Balani, A. Hamedi, E. Coatanéa,
G. Gary Wang and K. R. Haapala (2019). "Knowledge-Based Design of Artificial Neural Network
Topology for Additive Manufacturing Process Modeling: A New Approach and Case Study for Fused
Deposition Modeling." Journal of Mechanical Design 141(2).
Noriega, A., D. Blanco, B. J. Alvarez and A. Garcia (2013). "Dimensional accuracy improvement of
FDM square cross-section parts using artificial neural networks and an optimization algorithm." The
International Journal of Advanced Manufacturing Technology 69(9-12): 2301-2313.
Okaro, I. A., S. Jayasinghe, C. Sutcliffe, K. Black, P. Paoletti and P. L. Green (2019). "Automatic fault
detection for laser powder-bed fusion using semi-supervised machine learning." Additive
Manufacturing 27: 42-53.
Petrov, A., J. Pernot, F. Giannini, B. Falcidieno and P. Véron (2016). "Mapping aesthetic properties to
3D free form shapes through the use of a machine learning based framework." IMATI REPORT Series:
16-16.
Pham, G., S.-H. Lee, O.-H. Kwon and K.-R. Kwon (2018). "Anti-3D Weapon Model Detection for Safe
3D Printing Based on Convolutional Neural Networks and D2 Shape Distribution." Symmetry 10(4).
Qi, X., G. Chen, Y. Li, X. Cheng and C. Li (2019). "Applying Neural-Network-Based Machine Learning to
Additive Manufacturing: Current Applications, Challenges, and Future Perspectives." Engineering
5(4): 721-729.
Radzi, S., J. H. K. Tan, G. J. S. Tan, W. Y. Yeong, M. A. Ferenczi, N. Low-Beer and S. R. Mogali (2020).
"Development of a three-dimensional printed heart from computed tomography images of a
plastinated specimen for learning anatomy." Anatomy & Cell Biology 53(1): 48.
Rong-Ji, W., L. Xin-hua, W. Qing-ding and W. Lingling (2008). "Optimizing process parameters for
selective laser sintering based on neural network and genetic algorithm." The International Journal
of Advanced Manufacturing Technology 42(11-12): 1035-1042.
Sanjayan, J. G. and B. Nematollahi (2019). Chapter 1 - 3D Concrete Printing for Construction
Applications. 3D Concrete Printing Technology. J. G. Sanjayan, A. Nazari and B. Nematollahi,
Butterworth-Heinemann: 1-11.
Saqib, S., R. J. Urbanic and K. Aggarwal (2014). "Analysis of Laser Cladding Bead Morphology for
Developing Additive Manufacturing Travel Paths." Procedia CIRP 17: 824-829.
Sarlo, R. and P. A. Tarazaga (2016). A Neural Network Approach to 3D Printed Surrogate Systems,
Cham, Springer International Publishing.
Scime, L. and J. Beuth (2018). "Anomaly detection and classification in a laser powder bed additive
manufacturing process using a trained computer vision algorithm." Additive Manufacturing 19: 114-
126.
Scime, L. and J. Beuth (2018). "A multi-scale convolutional neural network for autonomous anomaly
detection and classification in a laser powder bed fusion additive manufacturing process." Additive
Manufacturing 24: 273-286.


---


## Page 28


Scime, L. and J. Beuth (2019). "Using machine learning to identify in-situ melt pool signatures
indicative of flaw formation in a laser powder bed fusion additive manufacturing process." Additive
Manufacturing 25: 151-165.
Shen, X., J. Yao, Y. Wang and J. Yang (2004). Density Prediction of Selective Laser Sintering Parts
Based on Artificial Neural Network. International Symposium on Neural Networks, Springer.
Shevchik, S. A., C. Kenel, C. Leinenbach and K. Wasmer (2018). "Acoustic emission for in situ quality
monitoring in additive manufacturing using spectral convolutional neural networks." Additive
Manufacturing 21: 598-604.
Shi, Y., Y. Zhang, S. Baek, W. De Backer and R. Harik (2018). "Manufacturability analysis for additive
manufacturing using a novel feature recognition technique." Computer-Aided Design and
Applications 15(6): 941-952.
Sing, S. L., F. E. Wiria and W. Y. Yeong (2018). "Selective laser melting of titanium alloy with 50 wt%
tantalum: effect of laser process parameters on part quality." International Journal of Refractory
Metals and Hard Materials 77: 120-127.
Snell, R., S. Tammas-Williams, L. Chechik, A. Lyle, E. Hernández-Nava, C. Boig, G. Panoutsos and I.
Todd (2019). "Methods for Rapid Pore Classification in Metal Additive Manufacturing." Jom.
Sood, A. K., A. Equbal, V. Toppo, R. K. Ohdar and S. S. Mahapatra (2012). "An investigation on sliding
wear of FDM built parts." CIRP Journal of Manufacturing Science and Technology 5(1): 48-54.
Sood, A. K., R. K. Ohdar and S. S. Mahapatra (2009). "Parametric appraisal of fused deposition
modelling process using the grey Taguchi method." Proceedings of the Institution of Mechanical
Engineers, Part B: Journal of Engineering Manufacture 224(1): 135-145.
Sood, A. K., R. K. Ohdar and S. S. Mahapatra (2012). "Experimental investigation and empirical
modelling of FDM process for compressive strength improvement." Journal of Advanced Research
3(1): 81-90.
Tan, J. H. K., S. L. Sing and W. Y. Yeong (2020). "Microstructure modelling for metallic additive
manufacturing: a review." Virtual and Physical Prototyping 15(1): 87-105.
Tapia, G. and A. Elwany (2014). "A review on process monitoring and control in metal-based additive
manufacturing." Journal of Manufacturing Science and Engineering 136(6).
Thompson, A., I. Maskery and R. K. Leach (2016). "X-ray computed tomography for additive
manufacturing: a review." Measurement Science and Technology 27(7): 072001.
Vahabli, E. and S. Rahmati (2016). "Application of an RBF neural network for FDM parts’ surface
roughness prediction for enhancing surface quality." International Journal of Precision Engineering
and Manufacturing 17(12): 1589-1603.
van Eijnatten, M., R. van Dijk, J. Dobbe, G. Streekstra, J. Koivisto and J. Wolff (2018). "CT image
segmentation methods for bone used in medical additive manufacturing." Med Eng Phys 51: 6-16.
Vijayaraghavan, V., A. Garg, J. S. L. Lam, B. Panda and S. S. Mahapatra (2014). "Process
characterisation of 3D-printed FDM components using improved evolutionary computational
approach." The International Journal of Advanced Manufacturing Technology 78(5-8): 781-793.
Vosniakos, G.-C., T. Maroulis and D. Pantelis (2007). "A method for optimizing process parameters in
layer-based rapid prototyping." Proceedings of the Institution of Mechanical Engineers, Part B:
Journal of Engineering Manufacture 221(8): 1329-1340.
Wang, C., N. Jiang, Z. Chen, Y. Chen and Q. Dong (2015). Prediction of Sintering Strength for Selective
Laser Sintering of Polystyrene Using Artificial Neural Network.
Wang, R.-J., J. Li, F. Wang, X. Li and Q. Wu (2009). "ANN model for the prediction of density in
Selective Laser Sintering." International Journal of Manufacturing Research 4(3): 362 - 373.
Wang, W., Y. Wang, W. Williams and A. Browne "Secure Cloud Manufacturing: Research Challenges
and a Case Study."
Wasmer, K., T. Le-Quang, B. Meylan and S. A. Shevchik (2018). "In Situ Quality Monitoring in AM
Using Acoustic Emission: A Reinforcement Learning Approach." Journal of Materials Engineering and
Performance 28(2): 666-672.


---


## Page 29


Wasmer, K., T. Le-Quang, B. Meylan, F. Vakili-Farahani, M. Olbinado, A. Rack and S. Shevchik (2018).
"Laser processing quality monitoring by combining acoustic emission and machine learning: A high-
speed X-ray imaging approach." Procedia CIRP 74: 654-658.
Williams, G., N. A. Meisel, T. W. Simpson and C. McComb (2019). "Design Repository Effectiveness
for 3D Convolutional Neural Networks: Application to Additive Manufacturing." Journal of
Mechanical Design 141(11).
Wohlkinger, W. and M. Vincze (2011). Shape-based depth image to 3d model matching and
classification with inter-view similarity. 2011 IEEE/RSJ International Conference on Intelligent Robots
and Systems, IEEE.
Wong, K. V. and A. Hernandez (2012). "A review of additive manufacturing." International scholarly
research notices 2012.
Wu, H., Z. Yu and Y. Wang (2019). "Experimental study of the process failure diagnosis in additive
manufacturing based on acoustic emission." Measurement 136: 445-453.
Wu, M., V. V. Phoha, Y. B. Moon and A. K. Belman (2016). Detecting Malicious Defects in 3D Printing
Process Using Machine Learning and Image Classification. ASME 2016 International Mechanical
Engineering Congress and Exposition.
Wu, M., Z. Song and Y. B. Moon (2017). "Detecting cyber-physical attacks in CyberManufacturing
systems with machine learning methods." Journal of Intelligent Manufacturing 30(3): 1111-1123.
Wu, Y., G. Peng, L. Chen and H. Zhang (2016). Service architecture and evaluation model of
distributed 3D printing based on cloud manufacturing. 2016 IEEE International Conference on
Systems, Man, and Cybernetics (SMC), IEEE.
Xiong, J., G. Zhang, J. Hu and L. Wu (2014). "Bead geometry prediction for robotic GMAW-based
rapid manufacturing through a neural network and a second-order regression analysis." Journal of
Intelligent Manufacturing 25(1): 157-163.
Yamanaka, Y., A. Todoroki, M. Ueda, Y. Hirano and R. Matsuzaki (2016). "Fiber Line Optimization in
Single Ply for 3D Printed Composites." Open Journal of Composite Materials 06(04): 121-131.
Yang, J., D. Gu, K. Lin, C. Ma, R. Wang, H. Zhang and M. Guo (2020). "Laser 3D printed bio-inspired
impact resistant structure: failure mechanism under compressive loading." Virtual and Physical
Prototyping 15(1): 75-86.
Yao, X., S. K. Moon and G. Bi (2017). "A hybrid machine learning approach for additive manufacturing
design feature recommendation." Rapid Prototyping Journal 23(6): 983-997.
Ye, D., J. Y. Hsi Fuh, Y. Zhang, G. S. Hong and K. Zhu (2018). "In situ monitoring of selective laser
melting using plume and spatter signatures by deep belief networks." ISA Trans 81: 96-104.
Yu, C. and J. Jiang (2020). "A perspective on Using Machine Learning in 3D Bioprinting." International
Journal of Bioprinting 6(1).
Yu, W. H., S. L. Sing, C. K. Chua, C. N. Kuo and X. L. Tian (2019). "Influence of re-melting on surface
roughness and porosity of AlSi10Mg parts fabricated by selective laser melting." Journal of Alloys
and Compounds 792: 574-581.
Yu, W. H., S. L. Sing, C. K. Chua, C. N. Kuo and X. L. Tian (2019). "Particle-Reinforced Metal Matrix
Nanocomposites Fabricated by Selective Laser Melting: A State of the Art Review." Progress in
Materials Science 104: 330-379.
Yuan, B., G. M. Guss, A. C. Wilson, S. P. Hau‐Riege, P. J. DePond, S. McMains, M. J. Matthews and B.
Giera (2018). "Machine‐Learning‐Based Monitoring of Laser Powder Bed Fusion." Advanced
Materials Technologies 3(12).
Zhang, W., A. Mehta, P. S. Desai and C. Higgs (2017). Machine learning enabled powder spreading
process map for metal additive manufacturing (AM). Int. Solid Free Form Fabr. Symp. Austin, TX.
Zhang, X., X. Le, A. Panotopoulou, E. Whiting and C. C. L. Wang (2015). "Perceptual models of
preference in 3D printing direction." ACM Transactions on Graphics 34(6): 1-12.
Zhang, Y., G. S. Hong, D. Ye, K. Zhu and J. Y. H. Fuh (2018). "Extraction and evaluation of melt pool,
plume and spatter information for powder-bed fusion AM process monitoring." Materials & Design
156: 458-469.


---


## Page 30


Zhao, C., K. Fezzaa, R. W. Cunningham, H. Wen, F. De Carlo, L. Chen, A. D. Rollett and T. Sun (2017).
"Real-time monitoring of laser powder bed fusion process using high-speed X-ray imaging and
diffraction." Scientific Reports 7(1): 3602.
Zhao, C., K. Fezzaa, R. W. Cunningham, H. Wen, F. De Carlo, L. Chen, A. D. Rollett and T. Sun (2017).
"Real-time monitoring of laser powder bed fusion process using high-speed X-ray imaging and
diffraction." Sci Rep 7(1): 3602.
Zohdi, T. I. (2018). "Dynamic thermomechanical modeling and simulation of the design of rapid free-
form 3D printing processes with evolutionary machine learning." Computer Methods in Applied
Mechanics and Engineering 331: 343-362.


---
