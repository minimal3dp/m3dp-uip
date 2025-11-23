# electronics-13-03550-v2

> **Source:** `electronics-13-03550-v2.pdf`
> **Converted:** 2025-11-22 21:18:10
> **Method:** PyMuPDF

---

## Page 1


Citation: Rojek, I.; Marciniak, T.;
Mikołajewski, D. Digital Twins in 3D
Printing Processes Using Artificial
Intelligence. Electronics 2024, 13, 3550.
https://doi.org/10.3390/
electronics13173550
Academic Editors: Cristiana Delprete,
Cheng He and Luigi Gianpio
Di Maggio
Received: 30 June 2024
Revised: 29 August 2024
Accepted: 2 September 2024
Published: 6 September 2024
Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
electronics
Article
Digital Twins in 3D Printing Processes Using Artificial Intelligence
Izabela Rojek 1,*
, Tomasz Marciniak 2
and Dariusz Mikołajewski 1
1
Faculty of Computer Science, Kazimierz Wielki University, Chodkiewicza 30, 85-064 Bydgoszcz, Poland;
dariusz.mikolajewski@ukw.edu.pl
2
Faculty of Telecommunications, Computer Science and Electrical Engineering, Bydgoszcz University of
Science and Technology, Kaliskiego 7, 85-796 Bydgoszcz, Poland; tomasz.marciniak@pbs.edu.pl
*
Correspondence: izabela.rojek@ukw.edu.pl
Abstract: Digital twins (DTs) provide accurate, data-driven, real-time modeling to create a digital
representation of the physical world. The integration of new technologies, such as virtual/mixed
reality, artificial intelligence, and DTs, enables modeling and research into ways to achieve better
sustainability, greater efficiency, and improved safety in Industry 4.0/5.0 technologies. This paper
discusses concepts, limitations, future trends, and potential research directions to provide the in-
frastructure and underlying intelligence for large-scale semi-automated DT building environments.
Grouping these technologies along these lines allows for a better consideration of their individual
risk factors and use of available data, resulting in an approach to generate holistic virtual representa-
tions (DTs) to facilitate predictive analyses in industrial practices. Artificial intelligence-based DTs
are becoming a new tool for monitoring, simulating, and optimizing systems, and the widespread
implementation and mastery of this technology will lead to significant improvements in performance,
reliability, and profitability. Despite advances, the aforementioned technology still requires research,
improvement, and investment. This article’s contribution is a concept that, if adopted instead of
the traditional approach, can become standard practice rather than an advanced operation and can
accelerate this development.
Keywords: artificial intelligence; machine learning; Industry 4.0; Industry 5.0; digital twin; surrogate
modeling; optimization; prediction; intelligent manufacturing; smart factory; 3D printing
1. Introduction to Digital Twins and Support of DT by AI/ML
Properly implemented data management, analysis, and visualization, especially AI-
based classification and prediction, helps all types of organizations and people achieve
greater success in the implementation of most tasks. This is due to the fact that, although
processes are becoming more and more complicated, we are able to measure them more
effectively and precisely and describe them as objectively as possible. Of course, large
amounts of data to be processed (including in real time) and the optimization of inferences
and predictions from data, so that their use is tailored to the needs of users, have become
a barrier. There are two solutions here: artificial intelligence (AI), including data-based
approaches (machine learning—ML), and digital twins (DTs)—models reflecting real objects
accurately enough to predict their correct and incorrect operation. DTs provide accurate,
data-driven modeling in real time to create a digital representation of the physical world.
They are part of an ecosystem of integrated new technologies, such as virtual reality (VR),
mixed reality (AR), and AI/ML, which enable modeling and research into ways to achieve
better sustainability, greater efficiency, and improved safety in Industry 4.0 and Industry 5.0
technologies. The aforementioned group of technologies allows for a better consideration
of individual risk factors and the use of available data towards putting humans and the
environment at the center of events and efforts. This results in an approach to generating
holistic virtual representations such as DTs to facilitate predictive analyses in industrial
practice [1–3].
Electronics 2024, 13, 3550. https://doi.org/10.3390/electronics13173550
https://www.mdpi.com/journal/electronics


---


## Page 2


Electronics 2024, 13, 3550
2 of 24
The evolution of digital twins from basic computer simulations to sophisticated, real-
time virtual representations powered by AI has been driven by advances in computing,
data analysis, and connectivity. Although the term “digital twin” has been popularized
relatively recently, its basic concepts have a history spanning several decades.
•
Early foundations (1960s and 1980s) encompassing the concept of using computers
to simulate physical systems, along with the development of CAD (computer-aided
design) systems to create digital models of physical objects and the creation of physical
and digital replicas of spacecraft on Earth for the Apollo missions, which allowed for
monitoring and troubleshooting problems during spaceflight;
•
The emergence of the digital twin concept (1990s and 2000s) for product lifecycle
management (PLM), which required the integration of data and processes for design,
manufacturing, and maintenance (in 2002, the term “digital twin” was first used by
Dr. Michael Grieves at the University of Michigan to denote a virtual representation
that serves as a real-time digital equivalent of a physical object or process);
•
Technological growth and advancement (2010s) due to the proliferation of the Internet
of Things (IoT), embedding sensors in physical objects, real-time data collection and
communication with their digital counterparts, and the integration of artificial intelli-
gence (AI) with DTs, which has enabled the practical implementation of digital twins
in many areas, from manufacturing to healthcare and smart cities;
•
Modern DT applications (since the 2020s) including complex dynamic DTs based on
AI, edge computing, and augmented reality (AR), developed under the auspices of
organizations such as the Digital Twin Consortium.
AI-based digital twin architectures include a virtual model that mirrors a physical
entity, enabling real-time monitoring, analysis, and optimization. This architecture typically
includes several layers, including data acquisition, processing, and AI-based analysis, that
work together to create a dynamic representation of the physical counterpart. Data from
sensors on the physical object are continuously streamed to the digital twin, where they
are processed and analyzed using machine learning algorithms. These algorithms predict
future states, identify potential problems, and suggest optimizations based on the twin’s
understanding of the physical system. The digital twin is semantically linked to the physical
counterpart via a common data ontology that provides a consistent interpretation of the data
and processes. This semantic layer ensures that changes to the physical entity are accurately
reflected in the digital twin and that the twin’s insights can be efficiently applied back to
the physical system. The architecture supports bidirectional communication, allowing the
digital twin to send feedback or control signals to the physical entity for autonomous or
semi-autonomous adjustments. The AI component continuously refines the twin model
by learning from new data, thus increasing its accuracy and predictive capabilities over
time. Functionally, the digital twin can be used for simulation, diagnostics, and predictive
maintenance, providing a comprehensive understanding of the behavior of the physical
system under different conditions. The relationship between the digital and physical
counterparts is symbiotic; the digital twin improves the operation and performance of the
physical entity, while the physical entity provides live data that improve the twin model.
This architecture is essential in environments where real-time decision making and system
optimization are essential, such as in manufacturing, smart cities, and healthcare systems.
State-of-the-art DT component solutions include advanced sensor networks for precise
data acquisition, high-performance real-time data processing, and AI-based analytics for
predictive insights. Sensor technologies such as IoT devices have improved data accu-
racy and granularity, but they still face challenges in harsh environments and in ensuring
consistent data quality. Edge computing and cloud infrastructure enable real-time pro-
cessing, but data latency and synchronization remain an issue, especially in distributed
systems. AI models, especially deep learning and reinforcement learning, have revolution-
ized predictive maintenance and anomaly detection, outperforming traditional differential
equations by handling complex, nonlinear relationships without explicit modeling. AI
greatly enhances the predictive capabilities of digital twins by learning from large, diverse


---


## Page 3


Electronics 2024, 13, 3550
3 of 24
datasets, enabling the twin to predict failures or optimize performance under different
conditions. However, AI models require significant amounts of data to train and can suffer
from interpretability issues, making it difficult to understand the reasoning behind their
predictions. Technologies such as federated learning are helping to address data privacy
and security concerns by allowing AI models to be trained on distributed datasets without
centralizing sensitive information. The application of digital twins to complex systems,
such as smart cities or advanced manufacturing, benefits greatly from AI, where traditional
differential equations would be impractical due to the immense complexity and variability
of the systems. Despite these advances, challenges remain in creating fully autonomous
digital twins, as integrating AI models with physical systems still requires human oversight
to manage edge cases and unforeseen scenarios. AI-powered digital twins are gradually
moving from reactive to proactive and even prescriptive systems, offering recommenda-
tions based on future predictions that traditional methods would struggle to provide due
to their limited scope in handling dynamic, real-world conditions.
The applications of DTs are wide-ranging and continue to cover new areas, from
investigating the deformation of objects such as bridges [4] to emulating cyber attacks [5]
and emulating museum objects [6]. DTs are also often designed to monitor production
processes or their components [7,8] and the lifecycle of products/services [9]. For the
time being, the unattainable dream is to generate a DT of a patient or at least their organs
(physiological—healthy and pathological—with dysfunction) [10]. The aforementioned
solutions, based on their specific requirements and data collection technologies, are often
prototypical and require dedicated solutions, but nevertheless, it is already possible to
identify key mechanisms and developments that can be clothed in a technological ba-
sis/framework for the creation and use of DTs. These processes are being reinforced by
the use of AI, including ML (a data-driven approach in which the links between input
and output data are extracted automatically in the learning process so that there is no
need to know the rules of operation). AI/ML facilitates data collection and selection and
allows for better preparation of data for computational analyses and a higher level of
accuracy of inference, classification, and prediction, which is crucial for the development of
DTs [11–13].
This paper aims to discuss the concepts, limitations, challenges, future trends, and
potential research directions to provide infrastructure and underlying intelligence for
large-scale semi-autonomous built environments such as DTs.
Introducing our AI into DTs can increase production quality. This applies to both
production planning and configuration, as well as quality control and traceability. As
process simulation is quite well known and understood as a technology, it has already
become a key step in the preparation, design, and monitoring of production processes. The
introduction of AI/ML into the simulation of the above-mentioned processes will reduce
their costs and will become less time-consuming, including the possibility of carrying out
these processes within the production cycle and becoming useful in controlling processes
in real time [14]. As a result, AI/ML-based DTs have the potential to transform existing
simulation processes into real-time, closed-loop production systems. The costs of such
a transformation are acceptable enough that they can be realistically implemented in
industrial conditions.
Desheng et al. [8] showed, using DT technology, that the properties and rolling stability
in hot rolling are strongly dependent on the final rolling temperature, where diagnosing
anomalies in industrial conditions has, so far, been difficult. The proposed method includes
a number of elements subjected to computational processing, listed as follows:
•
The elimination of samples with large deviations using the Hausdorff distance algorithm;
•
Assessment of the tape head setting value based on a random forest model;
•
Assessment of other rolling parameters based on the isolation forest algorithm;
•
Curve risk assessment performed using the LCSS algorithm;


---


## Page 4


Electronics 2024, 13, 3550
4 of 24
•
A method for identifying the causes of anomalies, combining the knowledge graph and
the Bayesian network (the occurrence of nodes in the Bayesian network determines
the cause of the anomaly);
•
Model verification “on site”.
The above combination of mechanistic modeling and AI techniques allows for fast,
automatic, and accurate detection and analysis of final rolling temperature anomalies, with
an accuracy of 92% [9].
Abio et al. [15] investigated the use of a substitute model in their analysis of hardening
in the stamping process of a 22MnB5 steel sheet. The key stage of heat treatment is directly
related to the final quality of products—among others, in the automotive industry. Finite
element simulations were proposed for unsteady heat transfer analysis using ABAQUS
software Version 6.9, which generates training data for an ML-based DT, predicting key
process outcomes for the production of entire batches of products (Figure 1). The DT
predicted changes in the most important process temperature variables in many scenarios,
with an average error of about 3 ◦C and a reaction time that was four orders of magnitude
shorter compared to traditional simulations. The described technology can be expanded
to a larger DT for autonomous process control [14]. The data were prepared by ABACUS
for the DT, which included ML; this concerned the production of knowledge, not the
data themselves.
Figure 1. Selected ML methods used in DTs (own version based on [16–37]).


---


## Page 5


Electronics 2024, 13, 3550
5 of 24
Understanding the future evolution of engineering (including its leading areas) is
closely linked to the integration and development of AI, particularly in the development of
DTs. As systems become increasingly complex and interconnected, AI will play a key role
in creating accurate, real-time digital representations of these systems, enabling engineers
to simulate, predict, and optimize performance. The evolution of engineering is likely to
focus on areas such as smart manufacturing, autonomous systems, and sustainable design,
all of which can benefit from AI-powered digital twins. These digital twins will enable
engineers to remotely monitor systems, predict failures before they occur, and optimize
operations for efficiency and sustainability. Additionally, AI can facilitate the analysis of
the vast amounts of data generated by these digital twins, uncovering insights that may not
be immediately apparent through traditional engineering methods. As engineering moves
toward more predictive and adaptive designs, AI will play a key role in developing and
refining digital twins that can evolve alongside their physical counterparts. This symbiotic
relationship will also foster innovation in new materials, energy systems, and robotics,
where AI-based simulations can test and validate concepts before physical prototypes
are built. Additionally, collaboration between AI and engineering via digital twins will
increase the ability to create more personalized and adaptive systems that are tailored
to specific needs and conditions. Ultimately, integrating AI with digital twin technology
will redefine the boundaries of engineering, leading to more efficient, sustainable, and
intelligent systems.
The general concept of using AI/ML in digital twins in engineering involves creating
a virtual replica of a physical system or component that can simulate its behavior under
different conditions. AI and machine learning algorithms analyze real-time data from
the physical system, learning from its performance to predict future behavior, identify
potential failures, and optimize operations. This approach allows engineers to conduct
virtual testing, reducing the need for physical prototypes and accelerating the design pro-
cess. By continuously updating the digital twin with new data, the model becomes more
accurate over time, improving its predictive capabilities. Ultimately, this integration of
AI/ML improves decision making, reduces maintenance costs, and increases the reliability
of systems. In practice, this means that AI/ML in DTs in engineering is used to predict and
prevent equipment failures by analyzing sensor data from machines, enabling predictive
maintenance. In automotive engineering, DTs simulate the behavior of engines or trans-
missions under different driving conditions, optimizing performance and fuel economy.
AI-powered DTs in aerospace engineering help design more efficient aircraft components
by simulating aerodynamic properties and stress factors under different conditions. In
manufacturing, DTs use AI/ML to optimize production lines by predicting bottlenecks
and suggesting improvements in real time. Finally, AI-enhanced digital twins are used in
robotics, where they simulate robot movements and interactions, increasing precision and
reducing the risk of operational errors [28].
2. Our Concept of DTs and the Results of Our Studies
AI and ML in DTs have become popular in recent years, with DTs integrating an AI
component at the interface of these two fields [14].
Our concept of an AI-based DT is based on the creation of a highly detailed and
dynamic virtual model of a physical system that is constantly updated with data from a
physical counterpart in real time. The DT uses AI/ML technologies to simulate, predict, and
optimize the performance of a system throughout its lifecycle. This gives it an advantage
over traditional solutions that are still used [15,16]. The key components of our DT include
the following:
•
The physical entity, i.e., the actual reflected system or component (machine, engine, or
production line) [17];
•
A digital twin model, i.e., a precise digital (virtual) representation of a physical entity,
including all its physical properties and behaviors. This model is built using computer-


---


## Page 6


Electronics 2024, 13, 3550
6 of 24
aided design (CAD) data, finite element analysis (FEA) models, and other engineering
simulations [17];
•
A data acquisition process is carried out in the following way: IIoT sensors and devices
collect real-time data from a physical unit (temperature, pressure, vibration, speed,
and other relevant parameters) [18];
•
Data integration and processing: real-time data are sent to the digital twin either in
the form of full data or (in selected cases) in the form of vectors or matrices of features
extracted within the EC.AI/ML algorithms process these data to dynamically update
the digital model, ensuring an accurate reflection of the current state of the physical
entity, usually in real time [18];
•
AI algorithms analyze data to detect patterns, predict future behavior, and identify
potential problems. ML models can also be trained partially on historical data to
improve prediction accuracy and optimize performance [19];
•
Simulation and analysis: the DT can run simulations to test various scenarios and
predict results without affecting the physical system. This helps one understand how
changes in one part of the system can affect the entire or practice scenarios that are
difficult to implement in a real system (damage, cyber attacks, etc.) [17–19].
Based on the literature review and our own research, we can conclude that the priority
for applications of AI-based DTs, relatively fast in development and industrial application,
is given to the following:
•
Predictive maintenance: AI-based DTs can predict when a particular component is
likely to fail, allowing for timely (preemptive) maintenance before an actual failure
occurs [20].
•
Performance optimization: through continuous data analysis, digital twins can identify
inefficiencies and suggest optimizations, such as recommending adjustments for
operating conditions to improve performance or extend component life; the final
decision here belongs to a person (e.g., a technologist or head of maintenance) [21].
•
Design and testing: DTs can be used to test new designs in a virtual environment before
their physical implementation; this allows for rapid prototyping and the optimization
of designs with reduced costs and time [22].
•
Fault diagnosis and troubleshooting: DTs can help diagnose the problem by comparing
real-time data with expected behavior. This helps to quickly identify and eliminate
faults [23].
•
Lifecycle management: digital twins can monitor and manage the entire lifecycle of
a system, from design and production to operation and decommissioning, ensuring
optimal performance and resource utilization [24].
This approach to DTs allows for the following direct benefits to be achieved:
•
Enhanced decision making: provides actionable insights and data-driven decision
support [25];
•
Cost savings: reduces maintenance costs, prevents downtime, and minimizes the need
to create physical prototypes [26];
•
Improved reliability and performance: provides continuous monitoring and optimiza-
tion increase in system reliability and operational efficiency [27];
•
Greater flexibility: the use of AI/ML enables testing and implementation of changes
in a virtual environment, often in real time, offering greater flexibility in operations
and design adjustments (e.g., planning several variants in switching the production
line to new products) [28].
According to our concept, creating an AI-based DT for any problem involves several
key steps, listed as follows:
•
We start by collecting comprehensive data from the physical system, including sensor
data, operational history, and environmental conditions.
•
We then preprocess and clean these data to ensure accuracy, removing noise and
incomplete or outlier values that could skew the AI model.


---


## Page 7


Electronics 2024, 13, 3550
7 of 24
•
We select the appropriate AI model (traditional artificial neural network, deep learning
algorithm, or a hybrid AI combination, e.g., with fuzzy logic or fractal analysis)
depending on the complexity of the problem and the nature of the data.
•
We train the AI model using the preprocessed data, allowing it to learn the behavior
and patterns of the real system over time.
•
We validate the model’s performance by comparing its predictions with real-world
data, adjusting parameters, and retraining as needed to improve accuracy.
•
We integrate the trained AI model with the simulation environment to create a DT,
ensuring that it can replicate the behavior of the system under different conditions
with the accuracy required for our application.
•
We continuously update the DT with real-time data from the physical system, enabling
it to adapt to changes and improve its predictive capabilities (also as the behavior of
the real system changes, e.g., as it wears out).
•
We use the DT to simulate and predict outcomes for different scenarios, providing
insight into potential issues and optimizing system performance.
•
We implement a feedback loop where the performance of the physical system is
monitored and compared to the DT, improving the model over time to increase
its accuracy.
•
We implement the DT of the digital twin in a user-friendly interface, enabling engineers
and decision makers to interact with it, analyze results, and make informed decisions
about maintenance, design, and operational improvements.
AI uses the employee’s experience, intuition, and invention. It generates knowledge
from data. The lack of clear relationships and rules of thumb prevent/hinder the use of
traditional methods.
DT improvement is an ongoing process that never ends as long as the real system
is in operation. The operation of a DT can be affected by modifications to both the real
system and the DT (including basing the DT on a new simulation engine, environment, or
interface). Synchronization and optimization constitute a continuous process (Figure 2).
Physical processes
3D printing
Database
Knowledge base
• 3D model creation,
• 3D model preparation for
printing,
• product printing,
• product quality
assessment,
• … .
Digital Twin
PP and NN creation
• developing new physical
processes (PP),
• creating NN for new PP,
• testing NN for new PP,
• validating NN for new PP,
• improving NN of existing
PP,
• … .
Synchronization, Optimization
Synchronization, Optimization
3D printing using NN
• NN for 3D model creation,
• NN for 3D model
preparation for printing,
• NN for product printing,
• NN for product quaity
assessment,
• … .

Figure 2. Optimization ofphysical processes using a DT with an example of 3D printing processes
(PP—physical process, NN—neural network) (own concept based on previous publications [34]).


---


## Page 8


Electronics 2024, 13, 3550
8 of 24
The architecture of our artificial intelligence-based DT system using 3D printing pro-
cesses as an example is described in Figure 3. It provides a dynamic virtual representation
of a physical object/process at selected stages of its lifecycle. Our DT system covers these
selected physical processes: 3D model creation, 3D model preparation for printing, product
printing, and product quality assessment. In the databases, for product printing, we have
descriptions of these physical processes (e.g., production type, material type, layer height,
coating thickness, bottom thickness, top thickness, fill density, print speed, bed temperature,
print temperature, second nozzle temperature, build orientation, number of contours, and
tensile strength). The systems can both provide observations on the current state of the
system and answer “what if” questions. Multiple neural networks have been defined
for each decision problem at the product printing stage and their specific tasks. In the
knowledge base, we have descriptions in the form of NN models. When an order comes in
from a customer, the control module distributes the tasks to the different departments of
the company. The order is processed. New physical processes are the basis for expanding
the data and knowledge in the system. In this way, the system learns continuously, and
knowledge is accumulated as the system runs [34].
Database
Knowledge base
Digital Twins
3D printing
3D model creation
3D model preparation for printing
product printing
product quality assessment
…
System
control
module
User interface
Work order
Physical processes
Company departments
Design department
Technology department
Manufacturing department
Physical processes data
Corporative Network
Data
management
module
Data
normalization
and coding
Development
of AI models
Customer
Customer order
3D model creation
3D model preparation
for printing
product printing
Quality control department
product quality
assessment
PP and NN creation
developing new physical processes (PP)
creating NN for new PP
testing NN for new PP
validating NN for new PP
improving NN of existing PP
…
Figure 3. DT system architecture based on artificial intelligence using 3D printing processes as an
example (own concept based on previous publications [34]).
Experimentation and testing have been introduced into the DT as a new entity. In
the new entity, experiments and tests concern the creation and testing of new physical
processes and the creation, testing, and validation of new neural network models for new
physical processes. In addition, neural network models for existing physical processes are
being improved.


---


## Page 9


Electronics 2024, 13, 3550
9 of 24
In DT research, the selection of appropriate ML methods and the tuning of their
hyperparameters is crucial for accurate and efficient modeling. The choice of the method
and settings depends on the specific application, the characteristics of the dataset, and,
indirectly, the available computational resources. For this purpose, researchers use a
combination of theoretical knowledge, empirical testing, and automated optimization
techniques to achieve optimal results.
3. The Roles of Our DT
A DT is a virtual representation parameterized based on real process data in order
to model, simulate, monitor, analyze, and optimize the physical systems they represent.
DT theory involves creating virtual models of physical objects, systems, or processes to
simulate, analyze, and optimize their real-world counterparts [29–31]. These digital repli-
cas enable real-time monitoring, control, simulation, and predictive analytics, providing
insights into performance, efficiency, potential problems, and optimization opportuni-
ties [29–32]. By integrating data from sensors and IoT devices, DTs can reflect real-time
changes and predict future behaviors using advanced analytics and AI/ML. This improves
decision making by providing a risk-free environment for scenario testing and process
improvement. Originating from space technology, DTs have expanded into various indus-
tries, including manufacturing, healthcare, and urban planning. They facilitate preventive
maintenance, reducing downtime and costs by identifying problems before they occur. In
smart cities, digital twins help optimize asset management and infrastructure planning.
They also play a key role in personalized healthcare by modeling individual patient con-
ditions to adjust treatment plans. As digital twins evolve, they are expected to become
more autonomous, with self-optimization capabilities that will further enhance operational
efficiency and innovation [33,34]. Insight into how DTs achieve their benefits is provided
by examples of their use in households.
•
Home energy management: DTs of home energy systems can monitor and optimize
energy consumption by simulating different scenarios and suggesting the most effi-
cient solutions, such as switching appliances on and off at the right times to reduce
costs and energy consumption [35].
•
Smart refrigerators: DTs of refrigerators can analyze their interior, monitor the fresh-
ness of products, and suggest purchases and menus based on available ingredients;
they can also simulate a refrigerator’s energy consumption and suggest optimal tem-
perature settings [35].
•
Automation of home appliance maintenance: DTs of household appliances such as
washing machines, dishwashers, or air conditioners can monitor their health and
predict failures, warning household members of the need for service before a major
failure occurs [35].
•
Heating and cooling system management: DTs of the HVAC (heating, ventilation, and
air conditioning) system in the home can simulate different weather conditions and
adjust settings in real time to provide the required comfort to household members
while saving energy [35].
•
Smart garden management: a garden DT (together with devices for watering, mowing,
etc.) can monitor soil conditions, sunlight, and the water needs of plants, optimizing
watering and fertilization, leading to healthier plants and water savings [34,35].
DTs can solve problems by enabling real-time monitoring and analysis of machines and
systems, allowing for the early detection of anomalies and the prevention of unexpected
failures. They provide a virtual testing ground for new designs and modifications, reducing
the need for physical prototypes and speeding up the process of technology and equipment
development. By simulating various operating conditions and risk scenarios, DTs help
optimize performance, increase efficiency, and extend the life of components. They facilitate
predictive maintenance by analyzing data trends to predict when maintenance will be
required, thereby minimizing downtime and associated costs. In addition, DTs enhance
the ability to customize and tune machines to specific requirements, ensuring optimal


---


## Page 10


Electronics 2024, 13, 3550
10 of 24
functionality. With continuous feedback loops and data integration, digital twins support
the continuous improvement and innovation of solutions [36–38].
It seems that the application of DTs in the field of mechanical engineering should be
widespread, which we will explore in the review section later in this article.
3.1. Rules of DT Construction according to Our Concept
Considered in the DT, the subsequent stages of our DT preparation include the following:
•
Sensors, measurements, and data collection;
•
Data cleaning and preparation for use in the model;
•
Process modeling;
•
Component performance and the overall DT;
•
Evaluation, adjustment, and development;
•
Monitoring and control;
•
Use in practical applications and conclusions/improvements from them [6].
Sensorization provides opportunities to measure and describe the characteristics of
the tested system, process monitoring, and control. This allows us to isolate important
parameters, connections between them, and mechanisms implemented in the process,
which are often simultaneous and not stated directly. Sometimes this allows us to describe
the process more precisely in order to improve its final quality, expressed not only in greater
accuracy but also in shorter duration, lower energy consumption, and the amount of waste.
Acquiring and analyzing signals is useful for understanding the correct behavior of a given
system and detecting situations of incorrect operation, or even predicting them, which we
will describe in more detail in the section devoted to the use of AI to create DTs. It should
be noted that research on sensors and measurement equipment is closely related to the
monitoring and development of monitoring strategies described below [9].
Moreover, the quantity and quality of data are crucial. Their quantity, diversity,
certainty, completeness, lack of bias, and balance in classes ensure the correct data input
to the model. For this reason, data preparation is as critical to the model as the modeling
process itself and the selection of its parameters/algorithms.
Modeling is one of the main objectives, as models provide the possibility to understand,
monitor, and control production processes in the laboratory and in industrial applications.
Such modeling is based on both the results of empirical experiments and theoretical motels,
with many hypothetical mechanisms. Reproducible experiments and models reflecting
them are useful as being oriented more towards real-world applications than discussion.
They also allow for consideration of the main controls and their algorithms. This part of
DT development often builds on simplified solutions (e.g., an Ishikawa diagram—Figure 4)
and develops them progressively to more complex, multivariate, and plausible models.
In the following section, we will discuss how AI/ML streamlines this stage, allowing for
movement straight to more advanced models [9].
A significant part of the research when creating a DT is devoted to the modeling and
characterization of individual key components (system components). For this purpose,
the main characterization studies are described and commented on—both theoretical (e.g.,
sets of relevant equations) and experimental (descriptions of the experimental equipment
and experimental procedures used to characterize the performance of the components in
terms of efficiency and performance and experimentally obtaining the relevant coefficients).
This applies to both proper operation and cases of natural wear and damage (e.g., cracks,
operation in improper conditions, etc.). This gives not only better coefficient values and a
reference to optimal operating conditions but also a classification of the operating conditions
of a given element as correct or defective (e.g., leading to premature wear or damage) [9].
Advanced use cases are a good way to better understand the process itself. Practical
applications of DTs not only allow for detailing the process itself and taking into account
their goodness of fit for application but also for isolating of their main features desired
by users and increasing the role of DTs in solving potential problems and ensuring user
satisfaction with DTs (Figure 5) [9].


---


## Page 11


Electronics 2024, 13, 3550
11 of 24
Figure 4. Idea of the traditional Ishikawa diagram (own version based on [9]).
Figure 5. Stages of DT creation [9].
3.2. Rules of Our DT Operation
The most important goal for research (both in the area and in interdisciplinary research
using AI and engineering solutions) dealing with DTs and considering the industrial
improvement of the processes described by DTs as an important goal is to focus efforts on
DTs as a complete model of a machine and process capable of exchanging data from a real
twin in order to accomplish the following:
•
Improve the ability to design new operating cycles (including their optimization) [9];
•
Improve the final quality of the workpiece/service in an economical and sustain-
able way (energy-saving, with minimal waste, and, in some cases, saving water or
coolant) [9];
•
Anticipate and prevent unexpected phenomena, damage, and downtime [9];
•
Ensure predictive maintenance while maintaining production smoothness [9].
We would like to point out that the above-mentioned principles apply to both tradi-
tional processes, such as milling and turning, and much more demanding ones, such as
waterjet cutting, laser cutting, or additive manufacturing (3D printing). The description
methods are universal, but, for example, when cutting with a water jet, there are some
delays that should be taken into account [6]. In any such case, the entire DT develop-
ment process must be followed and reorganized to define the original DT concept for a
given application.
We would like to point out that, depending on the application, there is already
CAD/CAM/simulation software on the market enabling the simulation of production
processes. It is worth using them, even to identify shortcomings. In addition, to create


---


## Page 12


Electronics 2024, 13, 3550
12 of 24
appropriate communication between the elements of the digital data flow in the process, the
industrial Internet of Things (IIoT) should be used, and process and product/service data
should be protected against unauthorized access, leakage, or cyber attacks. This requires
not only investment and an open approach from machine designers to innovative process
monitoring but also the preparation of engineering staff. When developing DT, CAM
systems can not only pay attention to traditional parameters (tool path, process parameters
such as type and dimensions of the material or cutting depth, and tool movements) but
can also constitute an advisory module in selecting the best tool configuration depending
on the application (cutting trial, target material, high precision, etc.). CAM can also take
into account and compensate for simultaneity, convergence, and delay, and, in some global
applications, time zone differences. Future solutions may include programs for multi-tool
machines (including combinations of machining and 3D printing), for the production of
products from various materials, for feeders (abrasive tools) depending on the position on
the tool path, and for receivers with a disinfection and packaging robot. It is also possible
to introduce new functions for closing the control circuit on the same machine. The DT
simulation must be performed offline before the actual machining operation. This will
create nominal patterns of (virtual) signals that can be compared to real ones (both during
simulation and during operations). However, this increasingly requires the division of roles
into edge computing (EC) as close as possible to the production line and cloud computing
(CC) at the level of the control of the entire line or smart factory. It is in the company’s
interest that all signals from the machine are received and processed—this will not only
allow for the development of a more reliable DT, but in the event of errors, it will allow
them to be found faster [9].
The principles of our DT operation ensure its effective functioning and delivery of
expected benefits. These principles include data integration, model accuracy, real-time
processing, and security measures. This can be presented in detail as follows:
•
Accurate representation: initial model fidelity, i.e., the DT must start with an accurate
and comprehensive model of the physical entity, including all relevant physical proper-
ties and behaviors, and then be subject to continuous calibration; i.e., the model should
be regularly updated based on new data (but also staff observations) to maintain
accuracy over time [22];
•
Real-time data integration: continuous data flow from sensors and IIoT devices in-
stalled in the physical system to capture real-time operational data and reliable data-
processing capabilities to efficiently handle large volumes of real-time data [22];
•
Data management and storage: the scalability of data storage as the amount of data
from a physical unit increases and the integrity, accuracy, and completeness of collected
data [22];
•
The adoption of industry standards for data formats and communication protocols to
facilitate seamless data integration and exchange [22];
•
The integration of the DT system with other digital tools and systems (ERP, PLM,
SCADA, and others) to provide a comprehensive view of the situation and the selection
of appropriate AI/ML algorithm(s) based on specific needs and characteristics of the
system [22];
•
Regularly training AI/ML models, using both historical and real-time data, to improve
their predictive capabilities and accuracy [22];
•
Testing various scenarios without affecting the physical system as predictive analysis
to forecast potential problems and proactively optimize system performance [22];
•
Implementing feedback loops where the digital twin can inform and adapt the perfor-
mance of the physical system based on analysis and simulations [22];
•
Incorporating user feedback into the operation of the digital twin to continually
improve its performance and usefulness [22];
•
Implementing proven cybersecurity measures to protect data and models from unau-
thorized access and cyber threats [22];


---


## Page 13


Electronics 2024, 13, 3550
13 of 24
•
Intuitive and user-friendly interfaces for interaction with the DT, granting authorized
users easy access to information (on a need-to-know basis) and control over the
system [22];
•
Providing users with training and a user support system (Helpdesk) to maximize the
usability of the DT [22];
•
Use of the DT to monitor and manage the entire lifecycle of a system, from design and
production to operation and decommissioning [22];
•
Relying on key performance indicators (KPIs) and metrics to monitor the performance
of both the digital twin and the physical system [22];
•
Developing DT adaptations to changes in the physical system, such as updates or
modifications, without significant rework [22].
We will discuss the challenges in the Discussion section, but we would like to highlight
them here. The main challenges for AI-based DTs include the following:
•
Data management: handling and processing large amounts of data in real time can be
complex and resource-intensive [22].
•
Integration: seamlessly integrating DTs into existing systems and workflows can be a
challenge [22].
•
Accuracy: ensuring that the DT remains an accurate representation of the physical
system requires sophisticated models and constant updates [22].
•
Security: protecting sensitive data and maintaining the cybersecurity of a DT system
is critical [22].
3.3. Interoperability of Our AI-Based DTs in an Innovative Industry Ecosystem
Industry 4.0 and Industry 5.0 have transformed the manufacturing industry towards
full connection between the elements of the production line, with more effective use of
data from production processes and the placing of humans and their environment at the
center of industry attention [39]. The integration of sensors, effectors, communication
technologies, computing platforms, AI/ML, control systems, and predictive tools is used to
effectively manage processes in real time [40]. New technologies, such as DTs, can further
intensify the above-mentioned processes towards the development of smart factories [41].
The combination of real (in the production line) and digital (in one or more DTs) versions of
the system allows for real-time data exchange for the purposes of the control, monitoring,
prediction, and classification of events [42–52]. Thus, classic production control turns into a
forward-looking process, reacting in advance, making optimal use of all opportunities that
will appear, and reacting, in advance, to the needs of repairs and adjustments, anomalies,
and production disturbances [42–52].
In the current comprehensive approach, it has been shown that AI/ML in DTs is
an effective tool for handling production data in the field of second opinion and quality
control systems [45–49], including process quality monitoring [53,54]. It is also possible to
identify service patterns for large amounts of unlabeled data generated in the production
process, e.g., when detecting and classifying anomalies, predicting service, faults, and
quality [46–50]. Generative adversarial networks (GANs) or a hybrid combination of
different ML techniques work well in anomaly detection [51] but also in oversampling
too-small experimental datasets to feed ML algorithms for forecasting [52].
A separate problem is predicting the life of production lines, products, and services.
For practical reasons, a hybrid approach is most often used—a combination of decision trees
and artificial neural networks (ANNs) [53]. Reinforcement learning can ensure that BTs
are goal-oriented and useful for decision making, such as planning, schedule optimization,
maintaining production continuity, and quality control [54,55].
The availability of process data is crucial for the proper operation of AI/ML methods
and techniques for DTs. Unfortunately, conducting all experiments (e.g., regarding damage)
for the purpose of obtaining data from a real production line is often impossible, because it is
expensive and time-consuming, involves stopping and reprogramming the production line,
and wastes raw materials. Therefore, production simulations are mainly a source of data and


---


## Page 14


Electronics 2024, 13, 3550
14 of 24
knowledge about the uninterrupted operation of the real production system [56,57]. Only
DTs can enable research into many scenarios of the anomalous operation of the production
line and its configurations, as well as experimental tests in the scope of modifying the line’s
operating conditions for new experimental conditions, products, services, and, e.g., susceptibility
to cyber attacks.
4. Materials and Methods
4.1. Dataset
When developing bibliometric analysis methods, we focused on understanding the
research picture in the area of AI-based DTs in engineering and the possible progress of
knowledge and practice in this area of research. We formulated a research question (RQ)
that will help us discover the key aspects of the research area regarding finding the concept
of creating an AI-based DT in engineering. This is consistent with both the title and the
Introduction section and the objectives of this paper. The RQ formulated in this way is
significant and can be investigated based on bibliometric data (literature review). The
application of AI in engineering is closely related to the generation of DTs, as AI enhances
the simulation, analysis, and optimization of physical systems, making DTs more accurate
and effective. As industries recognize the value of DTs in improving design, testing, and
maintenance, the emphasis on AI applications in this context is likely to increase, reflecting
a significant trend in both academia and in industries. Overall, the intersection of AI and DT
in engineering represents a key research area with great potential for future development
and innovation. Such analysis and interpretation of bibliometric data can make a key
contribution to the ongoing discussion and build a more solid foundation for further
analyses and research (Figure 6).
Figure 6. Bibliometric analysis procedure.
4.2. Methods
In this review, we used tools built into the Web of Science (WoS) database.
5. Results of the Review
5.1. General Results
Despite expectations, the number of publications in the WoS database with the key-
words (in Topic) “digital twin”, “mechanical engineering”, and “artificial intelligence” was


---


## Page 15


Electronics 2024, 13, 3550
15 of 24
zero, and, with the keywords “digital twin”, “mechanical engineering”, “machine learning”,
there were three [42–44]. There are many more publications in areas other than mechanical
engineering, as Figures 7–10 show. This indicates the need to intensify research on AI-based
DTs used in mechanical engineering and publish them in the best journals indexed in the
WoS database. This may also be due to the limited amount of interdisciplinary research.
Figure 7. Categories of publications (WoS, “digital twin” and “machine learning”: 1130 (2016–2024)).
Figure 8. Annual publications trend (WoS, “digital twin” and “machine learning”: 1130 (2016–2024)).

Figure 9. Categories of publications (WoS, “digital twin” and “artificial intelligence”: 1016 (2017–2024)).


---


## Page 16


Electronics 2024, 13, 3550
16 of 24
Figure 10. Annual publications trend (WoS, “digital twin” and “artificial intelligence”: 1016 (2017–2024)).
On the basis of such results, it can be concluded that the concept of mechanical
engineering is a very general one, and perhaps that is why the literature cannot be found.
Hence, we checked the following:
•
“digital twin”, “3D printing”, and “artificial intelligence”: 16 (WoS, 2020–2024);
•
“digital twin”, “3D printing”, and “machine learning”: 21 (WoS, 2019–2024).
•
This also indicates a research gap regarding our example in Figures 2 and 3.
Virtual inspections and assessments of infrastructure assets (e.g., bridges) are capable
of creating an accurate digital representation of existing assets (DTs). They are an alternative
to in-person and site-based assessments, while being cheaper, more reliable, and requiring
fewer distributive bridge inspections. For bridge monitoring, the most popular technologies
include unmanned aerial vehicle (UAV) photogrammetry and terrestrial laser scanning
(TLS). These are characterized by their potential to provide qualitative digital models based
on the assessment of generated point clouds in terms of quality and geometric accuracy for
an asset of this size, such as a bridge. The assessment addresses point distribution, outlier
noise level, data completeness, surface deviation, and geometric accuracy [45]. Thus, Bridge
Information Modelling (BrIM), being a specific form of Building Information Modelling
(BIM), provides a digital link between bridge assets related to geometric and non-geometric
control data. A comprehensive asset management system has been developed that uses
BrIM data to enhance and facilitate the BMS. It has shown potential in replacing traditional
paper documentation and managing bridges efficiently and effectively, in addition to being
less prone to subjectivity in assessment [58].
5.2. Examples of Tasks Performed Better than Previous Methods
Despite the concept of AI-based DTs being at the beginning of their development,
several studies have already been published showing their advantages over traditional
solutions. In order to solve the problem of noise and similar gray values between the
foreground and background of pellet images, an AI-based DT based on superpixel fea-
tures was developed. The binary SVM classification model was used to transform the
image segmentation problem into a foreground and background classification problem,
and the four neighbor search algorithm was proposed to reduce the mis-segmentation rate
of edge superpixels. The high accuracy of the proposed method was achieved, at 95.87%,
which enabled visual analysis and decision making [59]. An autonomous mobile robot
platform capable of simulation-based navigation using NVIDIA’s Isaac Simulation 4.1.0
software was developed. AI was used here to analyze environmental data and simula-
tion inputs, enabling the robot to dynamically change course or perform specific tasks.
This resulted in an increase in the robot’s adaptability and performance in different sce-
narios [60]. AI-based fault detection and remote robot control are being explored in the
AI-enabled Cyber–Physical In-Orbit Factory project, which shows how AI is being used to


---


## Page 17


Electronics 2024, 13, 3550
17 of 24
make manufacturing more robust, fault-tolerant, and autonomous, including in a robotic
Assembly, Integration, and Testing (AIT) system where a small satellite could be assembled
by a robotic manipulator from modular subsystems [61].
The aforementioned research has shown that artificial intelligence (AI)-based digital
twins outperform traditional digital twins due to their ability to perform more advanced
data analysis and prediction. AI allows for dynamic learning from large datasets in real
time, enabling more accurate modeling and prediction of the behavior of complex systems.
In traditional digital twins, simulations are typically based on fixed models, which can be
less flexible and slower to respond to change. With AI, digital twins can better identify
patterns and anomalies and optimize processes, leading to higher operational efficiency
rates. This research also highlights AI’s ability to adapt and make autonomous decisions,
which increases the value of digital twins in the context of managing and optimizing
industrial systems.
6. Discussion
So far, we have presented our concept and its applicability to already formulated and
partly investigated problems. However, this does not exhaust the possibilities, as solutions
such as AI-based DTs are only at the threshold of their development, requiring further
research to address the many challenges they face. The complexity of the issues discussed
requires the introduction of a coherent development strategy and the spreading of projects
over time. The existing approaches described in the literature were not as comprehensive
as we would like; hence, the limitations and challenges were much greater. Here, we would
like to narrow them down to the key ones in an interdisciplinary approach.
As an example, we consider the difference between an AI-based DT for autonomous
vehicles and AI-based driving software. Although both are AI-based, they have different
implications for the user and use different data sources, so the ethical and bias implications
of the two are different. The DT for autonomous vehicles is a virtual replica of a physical
vehicle that simulates its behavior, interactions with its environment, and reactions to
various road conditions. It allows for the testing and optimization of systems in a controlled
environment, which minimizes the risk of errors during real-world use. By contrast,
autonomous driving software relies on AI algorithms that continuously process data from
vehicle sensors, making real-time decisions on the road. The DT uses a wide range of
data, including environmental simulations and historical vehicle data, while autonomous
driving software relies primarily on live data. This difference has ethical implications,
as the DT can help identify and correct bias in algorithms in a safe environment before
being utilized on the road. Autonomous driving software must not only be precise but also
transparent in its decision making to minimize the risk of poor decisions. The DT can be
used to analyze long-term environmental impacts, something that autonomous driving
software cannot do in real time. Both solutions, while based on AI, serve different purposes;
one focuses on improvement and testing, while the other focuses on safe driving. AI bias in
the DT can lead to erroneous conclusions during testing, while bias in autonomous driving
software can directly threaten road safety. Therefore, ethical considerations related to the
use of these technologies must take into account the differences in their application and
impact in the real world [62–64].
6.1. Main Limitations and Challenges
Highlighting the main limitations and challenges related to the use of AI to generate
digital twins should be prioritized, as they must be solved, opening up opportunities for
further development of the discussed group of technologies. Chief among these is the
collection of high-quality, comprehensive datasets, which are required for accurate AI
models, but obtaining such data can be challenging due to sensor limitations and data
inconsistency. Moreover, creating and operating DTs requires expensive computational
resources, which may constitute a barrier to their widespread use. Moreover, integrating
AI into existing engineering systems and software can be complex and time-consuming,


---


## Page 18


Electronics 2024, 13, 3550
18 of 24
requiring specialized knowledge. Achieving real-time data processing and simulation in
DTs is difficult due to the previously mentioned high computational requirements. Also,
ensuring that AI models accurately reflect the physical behavior of complex systems is
difficult, especially in dynamic environments. Scaling DT solutions to cover large and
complex systems without sacrificing performance or accuracy is a significant challenge. En-
suring compatibility and seamless communication between the various tools and software
platforms used in engineering can be problematic. There is a lack of specialists with all the
skills necessary to develop and implement artificial intelligence-based DTs. In this case, it is
easier to rely on interdisciplinary teams, but assembling them is also not easy, and training
specialists will take at least several years. The development, deployment, and maintenance
of AI-based DTs can be prohibitively expensive, limiting their availability to smaller or-
ganizations. A system of subsidies or implementation grants may help here. Protecting
sensitive data related to the creation and operation of DTs from cyber threats is crucial
but challenging. AI applications in DTs must meet industry standards, and regulatory
requirements can be complex (e.g., the EU AI Act). Effectively managing uncertainty in
both the data and the models themselves is an ongoing challenge. Continuously monitoring
and updating AI models to reflect changes in the physical system or new data is necessary
but resource-intensive. From the above reasons, it is necessary to rigorously validate and
verify that DTs accurately represent physical systems, which requires extensive testing and
expertise. Ensuring that the use of AI in DTs complies with ethical standards, including
privacy and bias mitigation, adds an additional layer of complexity [65–67].
In the case of virtualized systems, AI-assisted DTs may be limited by the quality and
accuracy of the input data, which affects the precision of simulations and predictions.
AI models may not fully account for all the complex physical interactions, leading to
simplifications or representation errors. The process of training AI models requires a large
amount of data, which can be time-consuming and expensive and not always available for
all systems. DTs may also not be able to handle unpredictable events or failures that were
not accounted for in models trained on historical data. Lastly, computational limitations
can affect the ability to perform complex simulations in real time, especially for highly
complex systems. The current trends in digital twin development is shown in Table 1.
Table 1. Current trends in digital twin development.
Trend
Description
Manufacturing
Efficiency
In manufacturing, DTs are used to optimize production
processes, predict maintenance needs, and reduce
downtime by accurately modeling machines and the flow
of work, intermediates, and materials.
Healthcare
DTs are developed for healthcare, where they simulate
patient-tailored models to improve diagnosis, personalize
treatment plans, and assess patient outcomes.
Smart cities
and territories
Cities are deploying DTs to model urban environments,
improving planning, infrastructure management
(including transport and energy), and emergency
response, providing a detailed, real-time virtual
representation of urban operations.
Aerospace
DTs are increasingly being used for predictive
maintenance, increasing aircraft performance and
optimizing fleet management through data analysis and
real-time simulation.
Sustainability
There is an increasing emphasis on using DTs to achieve
sustainability goals, such as reducing energy consumption,
optimizing resource use, and minimizing
environmental impact.


---


## Page 19


Electronics 2024, 13, 3550
19 of 24
6.2. Directions for Further Research
In the area of such complex systems, it is crucial to define research priorities with the
greatest impact on the development of AI-based DTs. The largest research teams will work
on them, and the largest financial resources will be allocated to them. It is important to agree
on them and coordinate them in advance so that the efforts of researchers complement each
other and do not duplicate each other. The starting point is research into advanced sensor
technologies and data collection methods to improve the quality and comprehensiveness of
datasets for digital twins. Real-time data processing requires the optimization of algorithms
and computational resources, as well as the simulation of entire systems. It is necessary to
develop hybrid models that combine artificial intelligence with traditional physics-based
simulations to improve accuracy and reliability. Solutions should be scalable; hence, it is
necessary to explore scalable AI structures and architectures that can effectively support
large-scale and complex systems. This will be helped by establishing standard protocols
and frameworks to ensure seamless integration and interoperability between different
software tools and platforms (including between current and future transition platforms).
Implementation must be cost-effective, so research should explore ways to reduce the costs
of developing, deploying, and maintaining AI-based digital twins to make them more
accessible. Further development requires the development of AI models that can self-adapt
and learn from new data to continually improve their accuracy over time. In current
geopolitical and global market conditions, it is important to develop and explore robust
cybersecurity strategies to protect data and AI models from cyber threats and ensure data
integrity. The shortage of specialists creates a need to create and update educational and
training programs to fill the skills gap and equip specialists with the necessary expertise in
artificial intelligence and digital twins. The standardization and comparability of solutions
increases the need to develop a comprehensive regulatory framework that can keep pace
with rapid advances in artificial intelligence and ensure compliance with industry standards.
In the case of uncertainty analysis, it becomes necessary to improve methods for quantifying
and managing uncertainty in AI models (e.g., via fuzzy logic) in order to increase the
reliability of digital twins. Exploring artificial intelligence-based automatic maintenance
and updates for digital twins aims to reduce the need for manual intervention, reduce
service time, and increase service efficiency. Research into ethical AI practices is needed to
ensure that digital twins are developed and used in a way that respects privacy, fairness, and
transparency. Promoting interdisciplinary collaboration between AI researchers, engineers,
and experts stimulates innovation and the practicality of solutions. For this purpose, it
is necessary to establish benchmarks and performance metrics to assess and compare the
effectiveness of different AI approaches in generating digital twins [68–71].
The use of AI in DTs may raise ethical concerns [72–77], in particular, leading to
significant privacy issues, as the detailed data collected and analyzed may contain sensitive
personal information, requiring robust data protection measures to protect individuals’
privacy. AI algorithms powering DTs may inadvertently perpetuate or exacerbate biases
present in the data, leading to unfair outcomes and discrimination, especially if the data are
not representative or the AI is not carefully monitored and adjusted. Ensuring transparency
in AI models is key to ethical accountability. AI decision-making processes in DTs can be
opaque, making it difficult to hold actors accountable for AI-based actions and decisions.
DTs integrated with AI can become the target of cyber attacks, potentially leading to
unauthorized access and misuse of critical systems and data, raising serious ethical concerns
about digital infrastructure protection. The implementation of AI in DTs raises concerns, as
it may lead to the redundancy of staff currently performing tasks that can be automated.
This requires ethical considerations regarding retraining and social impact on affected
workers [78–82].
7. Conclusions
AI-based DTs are a partly new tool for monitoring, simulating, and optimizing systems.
DTs itself are not a new technology, but AI-based DTs require further and more dedicated


---


## Page 20


Electronics 2024, 13, 3550
20 of 24
research due to their specificity of semi-automatic or automatic creation and the need for
supervision. Widespread adoption and mastery of the technology will lead to significant
improvements in performance, reliability, and profitability [78,79]. However, this requires a
significant upfront investment in transforming traditional approaches to AI-based DTs, training
a sufficient group of specialists from various industries who are ready to fully exploit the
capabilities of this technology, and working with scientists to develop them [83,84].
The emergence of AI-based DT technology has created unique opportunities to use
data transmitted in real time from the physical environment to the digital equivalent of
machines, devices, and production lines. AI plays a key role in AI-based digital twin
(DT) technology, enabling the creation of highly accurate and adaptive virtual models of
physical systems. AI algorithms process vast amounts of data from sensors and other
sources, enabling DTs to more accurately reflect real-world system behavior. AI also
enhances the predictive capabilities of DTs by identifying patterns and trends in historical
and real-time data, enabling more accurate predictions of system behavior. In addition,
AI-based models can simulate more different scenarios, providing insight into potential
outcomes and helping to optimize performance and prevent failures. AI enables DTs to
learn and evolve over time, continually improving their accuracy and relevance as new
data are ingested. In this way, AI enables the digital twin to handle complex, nonlinear
relationships within the system, enabling the modeling of complex problems that traditional
methods struggle to solve. AI also facilitates anomaly detection and diagnostics in DTs,
identifying problems earlier and more precisely before they manifest in the physical system.
AI helps automate decision making by providing recommendations based on simulations
and analyses of the digital twin. AI-based DTs can more easily integrate with other AI
systems, enabling holistic monitoring and control across multiple interconnected systems.
AI plays a key role in the scalability of digital twins, enabling them to be applied almost
automatically to increasingly complex systems with minimal manual intervention and
adaptation by human experts. Finally, AI drives the continuous improvement of digital
twins, ensuring they remain accurate and valuable tools for system management and
optimization in the long term.
Although progress has been made, DTs as a problem-solving paradigm still need to be
improved. Adopting our concept proposed in Section 5 instead of traditional approaches
can become standard practice, rather than an advanced rescue solution for the most difficult
problems observed in engineering, and this will help accelerate this development.
Author Contributions: Conceptualization, I.R., T.M. and D.M.; methodology, I.R., T.M. and D.M.;
software, I.R., T.M. and D.M.; validation, I.R., T.M. and D.M.; formal analysis, I.R., T.M. and D.M.;
investigation, I.R., T.M. and D.M.; resources, I.R., T.M. and D.M.; data curation, I.R., T.M. and D.M.;
writing—original draft preparation, I.R., T.M. and D.M.; writing—review and editing, I.R., T.M.
and D.M.; visualization, I.R., T.M. and D.M.; supervision, I.R.; project administration, I.R.; funding
acquisition, I.R. All authors have read and agreed to the published version of the manuscript.
Funding: The research was conducted as part of Izabela Rojek’s science internship at the Bydgoszcz
University of Science and Technology. This research on artificial intelligence in 3D printing was
carried out as part of the mini-grant “Applications of artificial intelligence methods in the area of
additive manufacturing techniques” in the project funded by the Polish Minister of Science under the
“Regional Initiative of Excellence” program (RID/SP/0048/2024/01) for Kazimierz Wielki University
and by the grant of the Bydgoszcz University of Science and Technology.
Data Availability Statement: Data are contained within the article.
Conflicts of Interest: The authors declare no conflicts of interest.
References
1.
Caldarelli, G.; Arcaute, E.; Barthelemy, M.; Batty, M.; Gershenson, C.; Helbing, D.; Mancuso, S.; Moreno, Y.; Ramasco, J.J.;
Rozenblat, C.; et al. The role of complexity for Digital twins of cities. Nat. Comput. Sci. 2023, 5, 374–381. [CrossRef]
2.
Kamel Boulos, M.N.; Zhang, P. Digital Twins: From Personalised Medicine to Precision Public Health. J. Pers. 2021, 11, 745.
[CrossRef]


---


## Page 21


Electronics 2024, 13, 3550
21 of 24
3.
Bibri, S.E.; Allam, Z.; Krogstie, J. The Metaverse as a virtual form of data-driven smart urbanism: Platformization and its
underlying processes, institutional dimensions, and disruptive impacts. Comput. Urban Sci. 2022, 2, 24. [CrossRef]
4.
Zhao, Y.; Zhang, G.; Zang, G.; Zhang, G.; Sang, W.; Zhang, S.; Li, W. Monitoring Bridge Dynamic Deformation Law Based on
Digital Photography and Ground-Based RAR Technology. Appl. Sci. 2023, 13, 10838. [CrossRef]
5.
Holik, F.; Yayilgan, S.Y.; Olsborg, G.B. Emulation of Digital Substations Communication for Cyber Security Awareness. Electronics
2024, 13, 2318. [CrossRef]
6.
Zou, C.; Rhee, S.-Y.; He, L.; Chen, D.; Yang, X. Sounds of History: A Digital Twin Approach to Musical Heritage Preservationin
Virtual Museums. Electronics 2024, 13, 2388. [CrossRef]
7.
Annoni, M. A Review of Waterjet Cutting Research towards micro AWJ and the Definition of the Waterjet Digital Twin. Materials
2024, 17, 1328. [CrossRef]
8.
Desheng, C.; Jian, S.; Mingxin, L.; Sensen, X. Digital Twin-Based Fault Diagnosis Platform for Final Rolling Temperature in Hot
Strip Production. Materials 2023, 16, 7021. [CrossRef]
9.
Feng, T.; Guo, W.; Li, W.; Meng, Z.; Zhu, Y.; Zhao, F.; Liang, W. Unveiling Sustainable Potential: A Life Cycle Assessment of
Plant–Fiber Composite Microcellular Foam Molded Automotive Components. Materials 2023, 16, 4952. [CrossRef]
10.
Poletti, G.; Antonini, L.; Mandelli, L.; Tsompou, P.; Karanasiou, G.S.; Papafaklis, M.I.; Michalis, L.K.; Fotiadis, D.I.; Petrini,
L.; Pennati, G. Towards a Digital Twin of Coronary Stenting: A Suitable and Validated Image-Based Approach for Mimicking
Patient-Specific Coronary Arteries. Electronics 2022, 11, 502. [CrossRef]
11.
D’Amico, G.; L’ Abbate, P.; Liao, W.; Yigitcanlar, T.; Ioppolo, G. Understanding Sensor Cities: Insights from Technology Giant
Company Driven Smart Urbanism Practices. Sensors 2020, 20, 4391. [CrossRef]
12.
Lynggaard, P.; Skouby, K.E. Complex IoT Systems as Enablers for Smart Homes in a Smart City Vision. Sensors 2016, 16, 1840.
[CrossRef]
13.
Zeng, F.; Pang, C.; Tang, H. Sensors on Internet of Things Systems for the Sustainable Development of Smart Cities: A Systematic
Literature Review. Sensors 2024, 24, 2074. [CrossRef]
14.
Glaessgen, E.; Stargel, D. The Digital Twin Paradigm for Future NASA and U.S. Air Force Vehicles.
In Proceedings of
the 53rd AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics and Materials Conference, Honolulu, HI, USA,
23–26 April 2012.
15.
Abio, A.; Bonada, F.; Pujante, J.; Grané, M.; Nievas, N.; Lange, D.; Pujol, O. Machine Learning-Based Surrogate Model for Press
Hardening Process of 22MnB5 Sheet Steel Simulation in Industry 4.0. Materials 2022, 15, 3647. [CrossRef]
16.
Li, B.H.; Hou, B.C.; Yu, W.T.; Lu, X.B.; Yang, C.W. Applications of artificial intelligence in intelligent manufacturing: A review.
Front. Inf. Technol. Electron. Eng. 2017, 18, 86–96. [CrossRef]
17.
Wuest, T.; Weimer, D.; Irgens, C.; Thoben, K.D. Machine learning in manufacturing: Advantages, challenges, and applications.
Prod. Manuf. Res. 2016, 4, 23–45. [CrossRef]
18.
Azadeh, A.; Saberi, M.; Kazem, A.; Ebrahimipour, V.; Nourmohammadzadeh, A.; Saberi, Z. A flexible algorithm for fault
diagnosis in a centrifugal pump with corrupted data and noise based on ANN and support vector machine with hyper-parameters
optimization. Appl. Soft Comput. 2013, 13, 1478–1485. [CrossRef]
19.
Penya, Y.K.; Bringas, P.G.; Zabala, A. Advanced fault prediction in high-precision found reproduction. In Proceedings of the 2008
6th IEEE International Conference on Industrial Informatics, Daejeon, Republic of Korea, 13–16 July 2008; pp. 1672–1677.
20.
Khanzadeh, M.; Chowdhury, S.; Marufuzzaman, M.; Tschopp, M.A.; Bian, L. Porosity prediction: Supervised-learning of thermal
history for direct laser deposition. J. Manuf. Syst. 2018, 47, 69–82. [CrossRef]
21.
Zhu, X.; Cai, Z.; Wu, J.; Cheng, Y.; Huang, Q. Convolutional neural network based combustion mode classification for condition
monitoring in the supersonic combustor. Acta Astronaut. 2019, 159, 349–357. [CrossRef]
22.
Domingues, R.; Filippone, M.; Michiardi, P.; Zouaoui, J. A comparative evaluation of outlier detection algorithms: Experiments
and analyses. Pattern Recognit. 2018, 74, 406–421. [CrossRef]
23.
Scime, L.; Beuth, J. Anomaly detection and classification in a laser powder bed additive manufacturing process using a trained
computer vision algorithm. Addit. Manuf. 2018, 19, 114–126. [CrossRef]
24.
Lei, Y.; Jia, F.; Lin, J.; Xing, S.; Ding, S.X. An Intelligent Fault Diagnosis Method Using Unsupervised Feature Learning towards
Mechanical Big Data. IEEE Trans. Ind. Electron. 2016, 63, 3137–3147. [CrossRef]
25.
Alabugin, S.K.; Sokolov, A.N. Applying of Generative Adversarial Networks for Anomaly Detection in Industrial Control Systems.
In Proceedings of the 2020 Global Smart Industry Conference (GloSIC), Chelyabinsk, Russia, 17–20 November 2020; pp. 199–203.
26.
Bhavsar, K.; Vakharia, V.; Chaudhari, R.; Vora, J.; Pimenov, D.Y.; Giasin, K. A Comparative Study to Predict Bearing Degradation
Using Discrete Wavelet Transform (DWT), Tabular Generative Adversarial Networks (TGAN) and Machine Learning Models.
Machines 2022, 10, 176. [CrossRef]
27.
Juez-Gil, M.; Erdakov, I.N.; Bustillo, A.; Pimenov, D.Y. A regression-tree multilayer-perceptron hybrid strategy for the prediction
of precrushing-plate life times. J. Adv. Res. 2019, 18, 173–184. [CrossRef]
28.
Oliff, H.; Liu, Y.; Kumar, M.; Williams, M.; Ryan, M. Reinforcement learning for facilitating human-robot-interaction in manufac-
turing. J. Manuf. Syst. 2020, 56, 326–340. [CrossRef]
29.
Paraschos, P.D.; Koulinas, G.K.; Koulouriotis, D.E. Reinforcement learning for combined production - maintenance and quality
control of a manufacturing system with deterioration failures. J. Manuf. Syst. 2020, 56, 470–483. [CrossRef]


---


## Page 22


Electronics 2024, 13, 3550
22 of 24
30.
Nasruddin, N.A.; Islam, N.; Oyekan, J. Machine Learning Informed Digital Twin for Chemical Flow Processes. In Manufacturing
Technology XXXVI, Proceedings of the 20th International Conference on Manufacturing Research/37th International National Conference on
Manufacturing Research (ICMR) 2023 Advances, Aberystwyth, UK, 6–8 September 2023; IOS Press: Amsterdam, The Netherlands,
2023; Volume 44, pp. 72–78.
31.
Brazina, J.; Stepanek, V.; Bradac, F. Application of Industry 4.0 trends in the teaching process. In Proceedings of the 20th
International Conference on Mechatronics—Mechatronika (ME), Pilsen, Czech Republic, 7–9 December 2022.
32.
Mohammadi, M.; Rashidi, M.; Mousavi, V.; Karami, A.; Yu, Y.; Samali, B. Quality Evaluation of Digital Twins Generated Based on
UAV Photogrammetry and TLS: Bridge Case Study. Remote Sens. 2021, 13, 3499. [CrossRef]
33.
Mohammadi, M.; Rashidi, M.; Yu, Y.; Samali, B. Integration of TLS-derived Bridge Information Modeling (BrIM) with a Decision
Support System (DSS) for digital twinning and asset management of bridge infrastructures. Comput. Ind. 2023, 147, 103881.
[CrossRef]
34.
Rojek, I.; Dostatni, E.; Mikołajewski, D.; Pawłowski, L.; Wegrzyn-Wolska, K. Modern approach to sustainable production in the
context of Industry 4.0. Bull. Pol. Acad. Sci. Tech. Sci. 2022, 70, e143828. [CrossRef]
35.
Hawkinson, E. Automation in Education with Digital Twins: Trends and Issues. Int. J. Open Distance E-Learn. 2022, 8. Available
online: https://ijodel.upou.edu.ph/index.php/ijodel/article/view/229 (accessed on 29 August 2024). [CrossRef]
36.
Ma, W.; Qu, J.; Wang, L.; Zhang, C.; Yang, A.; Zhang, Y. Pellet image segmentation model of super pixel feature-based support
vector machine in digital twin. Appl. Soft Comput. 2024, 151, 111083. [CrossRef]
37.
Marasigan, J.A.L.; Wong, Y.H. Adaptive Robotics: Integrating Robotic Simulation, AI, Image Analysis, and Cloud-Based Digital
Twin Simulation for Dynamic Task Completion. In Artificial Intelligence in HCI; Springer: Cham, Switzerland, 2024; Volume 14736,
pp. 262–271.
38.
Muhammad, K.; David, T.; Nassisid, G.; Farus, T. Integrating Generative AI with Network Digital Twins for Enhanced Network
Operations. arXiv 2024, arXiv:2406.17112.
39.
Kreuzer, T.; Papapetrou, P.; Zdravkovic, J. Artificial intelligence in digital twins—A systematic literature review. Data Knowl. Eng.
2024, 151, 102304. [CrossRef]
40.
Tao, F.; Qi, Q.; Liu, A.; Kusiak, A. Data-driven smart manufacturing. J. Manuf. Syst. 2018, 48, 157–169. [CrossRef]
41.
Mourtzis, D. Simulation in the design and operation of manufacturing systems: State of the art and new trends. Int. J. Prod. Res.
2020, 58, 1927–1949. [CrossRef]
42.
Ye, J.; Fu, G.; Poudel, U.P. Edge-Based Close-Range Digital Photogrammetry for Structural Deformation Measurement. J. Eng.
Mech. 2011, 137, 475–483. [CrossRef]
43.
Maas, H.G.; Hampel, U. Photogrammetric Techniques in Civil Engineering. Material. Test. Struct. Monit. 2006, 72, 39–45.
44.
Detchev, I.; Lichti, D.; Habib, A.; El-Badry, M. Multi-dimensional and Multi-temporal motion estimation of a beam surface during
dynamic testing using low-frame rate digital cameras. Appl. Geomat. 2017, 9, 127–141. [CrossRef]
45.
Khalid, L.A.E. Using smart phones for deformations measurements of structures. Geod. Cartogr. 2017, 43, 66–72.
46.
Rojek, I.; Mikołajewski, D.; Dostatni, E.; Kopowski, J. Specificity of 3D Printing and AI-Based Optimization of Medical Devices
Using the Example of a Group of Exoskeletons. Appl. Sci. 2023, 13, 1060. [CrossRef]
47.
Menaguale, O. Digital twin and cultural heritage—The future of society built on history and art. In The Digital Twin; Springer
International Publishing: Cham, Switzerland, 2023; pp. 1081–1111.
48.
Nikolakopoulos, P.G.; Markopoulos, A.P. Editorial on simulation and modeling using digital twins in mechanical design and in
advanced manufacturing technology. Simul. Model. Pract. Theory 2024, 133, 102904. [CrossRef]
49.
Epiphaniou, G.; Hammoudeh, M.; Yuan, H.; Maple, C.; Ani, U. Digital twins in cyber effects modelling of IoT/CPS points of low
resilience. Simul. Model. Pract. Theory 2023, 125, 102744. [CrossRef]
50.
Stavrinides, G.L.; Karatza, H.D. Cyber-physical systems, digital twins and Industry 4.0: The role of modeling and simulation.
Simul. Model. Pract. Theory 2023, 124, 102727. [CrossRef]
51.
Yang, T.; Razzaq, L.; Fayaz, H.; Qazi, A. Redefining fan manufacturing: Unveiling industry 5.0’s human-centric evolution and
digital twin revolution. Heliyon 2024, 10, e33551. [CrossRef]
52.
Matania, O.; Bechhoefer, E.; Blunt, D.; Wang, W.; Bortman, J. Anomaly Detection and Remaining Useful Life Estimation for the
Health and Usage Monitoring Systems 2023 Data Challenge. Sensors 2024, 24, 4258. [CrossRef]
53.
Xu, X.; Omitaomu, F.; Sabri, S.; Li, X.; Song, Y. Leveraging Generative AI for Smart City Digital Twins: A Survey on the
Autonomous Generation of Data, Scenarios, 3D City Models, and Urban Designs. arXiv 2024, arXiv:2405.19464.
54.
Borges, J.; Bastos, F.; Correa, I.; Batista, P.; Klautau, A. CAVIAR: Co-simulation of 6G Communications, 3D Scenarios and AI for
Digital Twins. arXiv 2024, arXiv:2401.03310. [CrossRef]
55.
Zhang, L.; Zhuang, C.; Tian, Y.; Yao, M. Construction and Application of Energy Footprint Model for Digital Twin Workshop
Oriented to Low-Carbon Operation. Sensors 2024, 24, 3670. [CrossRef]
56.
Xiao, B.; Zhong, J.; Bao, X.; Chen, L.; Bao, J.; Zheng, Y. Digital twin-driven prognostics and health management for industrial
assets. Sci. Rep. 2024, 14, 13443. [CrossRef]
57.
Zheng, P.; Yang, J.; Lou, J.; Wang, B. Design and application of virtual simulation teaching platform for inteligent manufacturing.
Sci. Rep. 2024, 14, 12895. [CrossRef]
58.
Kusiak, A. Smart manufacturing. Int. J. Prod. Res. 2018, 56, 508–517. [CrossRef]


---


## Page 23


Electronics 2024, 13, 3550
23 of 24
59.
Davis, J.; Edgar, T.; Porter, J.; Bernaden, J.; Sarli, M. Smart manufacturing, manufacturing intelligence and demand-dynamic
performance. Comput. Chem. Eng. 2012, 47, 145–156. [CrossRef]
60.
Tuegel, E.J.; Ingraffea, A.R.; Eason, T.G.; Spottswood, S.M. Reengineering aircraft structural life prediction using a digital twin.
Int. J. Aerosp. Eng. 2011, 2011, 154798. [CrossRef]
61.
Leutert, F.; Bohlig, D.; Kempf, F.; Schilling, K.; Mühlbauer, M.; Ayan, B.; Hulin, T.; Stulp, F.; Albu-Schäffer, A.; Kutscher, V.;
et al. AI-enabled Cyber-Physical In-Orbit Factory—AI approaches based on digital twin technology for robotic small satellite
production. Acta Astronaut. 2024, 217, 1–17. [CrossRef]
62.
Kopowski, J.; Mikołajewski, D.; Macko, M.; Rojek, I. Bydgostian hand exoskeleton—Own concept and the biomedical factors.
Bio-Algorithms Med-Syst. 2019, 15, 20190003. [CrossRef]
63.
Argyriou, L.; Economou, D.; Bouki, V. Design methodology for 360 immersive video applications: The case study of a cultural
heritage virtual tour. Pers. Ubiquitous Comput. 2020, 24, 843–859. [CrossRef]
64.
Qiu, C.; Zhou, S.; Liu, Z.; Gao, Q.; Tan, J. Digital assembly technology based on augmented reality and digital twins: A review.
Virtual Real. Intell. Hardw. 2019, 1, 597–610. [CrossRef]
65.
Gürses, A.; Reddy, G.; Masrur, S.; Özdemir, Ö.; Güvenç, I.; Sichitiu, M.L.; Sahin, A.; Alkhateeb, A.; Dutta, R. Digital Twins for
Supporting AI Research with Autonomous Vehicle Networks. arXiv 2024, arXiv:2404.00954.
66.
Zhu, Z.; Liu, C.; Xu, X. Visualisation of the digital twin data in manufacturing by using augmented reality. Procedia CIRP 2019, 81,
898–903. [CrossRef]
67.
Rojek, I.; Kowal, M.; Stoic, A. Predictive compensation of thermal deformations of ball screws in CNC machines using neural
networks. Teh.-Tech. Gaz. 2017, 24, 1697–1703.
68.
Rojek, I. Neural networks as prediction models for water intake in water supply system. In Artificial Intelligence and Soft
Computing—ICAISC 2008; ICAISC 2008; Lecture Notes in Computer Science 5097; Rutkowski, L., Tadeusiewicz, R., Zadeh, L.A.,
Zurada, J.M., Eds.; Springer: Berlin/Heidelberg, Gemany, 2008; pp. 1109–1119.
69.
Hao, W.; Yang, Q.; Li, Z.; Hu, S.; Liu, B.; Ruan, W. Multi-Scale Traffic Aware Cybersecurity Situational Awareness Online Model
for Intelligent Power Substation Communication Network. IEEE Internet Things J. 2023, 10, 1666–1681. [CrossRef]
70.
Manbachi, M.; Nayak, J.; Hammami, M.; Bucio, A.G. Virtualized Experiential Learning Platform for Substation Automation and
Industrial Control Cybersecurity. In Proceedings of the 2022 IEEE Electrical Power and Energy Conference (EPEC), Virtual Event,
5–7 December 2022; pp. 61–66.
71.
Mikołajewska, E.; Mikołajewski, D. Ethical considerations in the use of brain-computer interfaces. Cent. Eur. J. Med. 2013, 8,
20–724. [CrossRef]
72.
Zylka, L.; Burek, J.; Mazur, D. Diagnostic of peripheral longitudinal grinding by using acoustic emission signal. Adv. Prod. Eng.
Manag. 2017, 12, 221–232. [CrossRef]
73.
Mikołajczyk, T.; Mikołajewski, D.; Kłodowski, A.; Łukaszewicz, A.; Mikołajewska, E.; Paczkowski, T.; Macko, M.; Skornia, M.
Energy Sources of Mobile Robot Power Systems: A Systematic Review and Comparison of Efficiency. Appl. Sci. 2023, 13, 7547.
[CrossRef]
74.
Martinek, R.; Ladrova, M.; Sidikova, M.; Jaros, R.; Behbehani, K.; Kahankova, R.; Kawala-Sterniuk, A. Advanced Bioelectrical
Signal Processing Methods: Past, Present, and Future Approach – Part III: Other Biosignals. Sensors 2021, 21, 6064. [CrossRef]
75.
Jorgensen, P.A.; Waltoft-Olsen, A.; Houmb, S.H.; Toppe, A.L.; Soltvedt, T.G.; Muggerud, H.K. Building a Hardware-in-the-Loop
(HiL) Digital Energy Station Infrastructure for Cyber Operation Resiliency Testing. In Proceedings of the 2022 IEEE/ACM 3rd
International Workshop on Engineering and Cybersecurity of Critical Systems (EnCyCriS), Pittsburgh, PA, USA, 16 May 2022;
pp. 9–16.
76.
Liu, R.; Vellaithurai, C.; Biswas, S.S.; Gamage, T.T.; Srivastava, A.K. Analyzing the Cyber-Physical Impact of Cyber Events on the
Power Grid. IEEE Trans. Smart Grid 2015, 6, 2444–2453. [CrossRef]
77.
Boje, C.; Guerriero, A.; Kubicki, S.; Rezgui, Y. Towards a semantic Construction Digital Twin: Directions for future research.
Autom. Constr. 2020, 114, 103179. [CrossRef]
78.
Piras, G.; Agostinelli, S.; Muzi, F. Digital Twin Framework for Built Environment: A Review of Key Enablers. Energies 2024, 17,
436. [CrossRef]
79.
Yousef, L.A.; Yousef, H.; Rocha-Meneses, L. Artificial Intelligence for Management of Variable Renewable Energy Systems: A
Review of Current Status and Future Directions. Energies 2023, 16, 8057. [CrossRef]
80.
Manfren, M.; Gonzalez-Carreon, K.M.; James, P.A.B. Interpretable Data-Driven Methods for Building Energy Modelling—A
Review of Critical Connections and Gaps. Energies 2024, 17, 881. [CrossRef]
81.
Hartmann, S.; Murua, O.; Arrizubieta, J.I.; Lamikiz, A.; Mayr, P. Digital Twin of the laser-DED process based on a multiscale
approach. Simul. Model. Pract. Theory 2024, 132, 102881. [CrossRef]
82.
Jonathan, B.; Barroso, U.; Intes, A. Development of Miniaturized Satellite Technology for Global Environmental Monitoring. J.
Moeslim Res. Tech. 2024, 1, 104–114.


---


## Page 24


Electronics 2024, 13, 3550
24 of 24
83.
Hasidi, O.; Abdelwahed, E.H.; Qazdar, A.; Boulaamail, A.; Krafi, M.; Benzakour, I.; Bourzeix, F.; Baïna, S.; Baïna, K.; Cherkaoui,
M.; et al. Digital Twins-Based Smart Monitoring and Optimisation of Mineral Processing Industry. In Communications in Computer
and Information Science; Springer: Berlin/Heidelberg, Germany, 2022; pp. 411–424.
84.
Örs, E.; Schmidt, R.; Mighani, M.; Shalaby, M. A Conceptual Framework for AI-based Operational Digital Twin in Chemical
Process Engineering. In Proceedings of the 2020 IEEE International Conference on Engineering, Technology and Innovation
(ICE/ITMC), Cardiff, UK, 16 September 2020; pp. 1–8.
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.


---
