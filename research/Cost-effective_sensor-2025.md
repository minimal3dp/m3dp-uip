# Cost-effective_sensor-2025

> **Source:** `Cost-effective_sensor-2025.pdf`
> **Converted:** 2025-11-22 21:18:08
> **Method:** PyMuPDF

---

## Page 1


Cost-effective Sensor-based Digital Twin for Fused Deposition
Modelling 3D Printers
Kemel Shomenova, Md. Hazrat Alia, Nursultan Jyeniskhana, Ahmed Al-Ashaabb, Essam
Shehaba*
a Mechanical and Aerospace Engineering Department, School of Engineering and Digital
Sciences, Nazarbayev University, Astana, Kazakhstan
b Manufacturing and Materials Department, Faculty of Engineering and Applied Sciences,
Cranfield University, Cranfield, UK
1*Email: essam.shehab@nu.edu.kz
Abstract
There is an increasing importance of employing Digital Twin technology in enhancing
manufacturing processes, especially additive manufacturing due to its vital role in generating
customized products and components in many industry sectors such as health care, aerospace,
automotive, and energy. Among various additive manufacturing techniques, Material Extrusion
(MEX), which encompasses Fused Deposition Modeling (FDM), is distinguished as one of the
most widely used. The development of a Digital Twin for 3D printing is playing a crucial role in
achieving high-quality printed objects. It allows for improving the current limitations of Fused
Deposition Modeling (FDM) 3D printing such as long printing time, need for monitoring, and
defects of printed parts. Several studies have been conducted on Digital Twin development for
FDM 3D printing, including IoT-based monitoring, machine learning, and image processing.
However, sensor-based approaches with proper sensor selection, data transfer, and visualization
have not been fully explored yet.
This work aims to develop a Digital Twin (DT) for FDM 3D printing with improved accuracy,
resulting in better control and optimization of the printing process. The main approach in creating
the proposed DT system encompasses several steps: data collection, data transfer, data storage,
data analysis, and graphical user interface (GUI). The system receives two types of data: one from
a 3D printer and the other from embedded sensors. The data from the 3D printer is retrieved by
using Python, while sensor data are collected by using Arduino modules. Those data are collected
and stored in a real-time database to monitor and control the 3D printer during printing processes.
The controller sends GCode commands to a 3D printer line by line which allows editing of the
GCode in real time and automatically detects printing defects. The novelty of this research is that
it proposes the application of affordable and accurate sensors.  This system employs bespoke
Python scripts for real-time autonomous defect detection and interventions, in contrast to
traditional approaches that depend on restricted monitoring or external hosts. The decision-making
framework enables real-time defect detection and pausing of the print upon identifying anomalies
such as layer shifting, under-extrusion, or excessive vibrations. The proposed system enhances 3D
printing reliability and quality by integrating real-time data acquisition, autonomous control, and
Published by T&F. This is the Author Accepted Manuscript issued with: Creative Commons Attribution License (CC:BY 4.0).
The final published version (version of record) is available online at DOI:10.1080/0951192x.2025.2504085.  Please refer to any applicable publisher terms of use.
International Journal of Computer Integrated Manufacturing, Available online 13 May 2025
DOI: 10.1080/0951192x.2025.2504085


---


## Page 2


a user-friendly graphical interface, offering an efficient and cost-effective solution for improving
FDM printing processes.
Keywords: 3D Printing, Fused Deposition Modeling, Material Extrusion, Digital Twin, Sensors
1 Introduction
There is a global trend towards Industry 4.0, which involves incorporating advanced enabling
technologies such as the Internet of Things (IoT), Artificial Intelligence (AI), Digital Twin, Cloud
computing, cyber security, big data analytics, advanced simulation, blockchain, augmented reality,
and robotics(Ortiz and Intechopen 2020). This is to establish an intelligent and effective system.
Digital Twin is a core element of the enabling technologies of Industry 4.0. It is a virtual copy of
a physical product, process, or system that allows real-time monitoring, analysis, and optimization
of performance under various conditions (Grieves 2011). Digital Twinning is a trending topic in
the research community as the number of publications about it has increased exponentially over
the past few years (Lim, Zheng, and Chen 2020).  A sensor-based approach to developing smart
machines has already been proposed for traditional manufacturing (Cheng et al. 2017). The
importance of data from sensors has a large impact on additive manufacturing for improving its
effectiveness, output, and cost efficiency within the context of the fourth industrial revolution
(Khosravani, Nasiri, and Reinicke 2022). Among additive manufacturing techniques, MEX has
gained prominence due to its simplicity, affordability, and accessibility.
With the increasing age of additive manufacturing in different sectors, there is a growing need for
accurate and dependable quality control methods. Conventional manufacturing techniques usually
involve post-production checks, which can be both expensive and time-consuming. This study
seeks to enhance quality control processes and reduce errors by incorporating real-time monitoring
and defect detection features using Digital Twin technology in the 3D printing process. The
importance of this research is to improve additive manufacturing technologies by increasing
operational efficiency, maximizing resource usage, and ensuring the creation of defect-free
products.
This study focuses on the development of Digital Twin for 3D printing, which is one of the popular
non-traditional types of manufacturing. Fused Deposition Modeling (FDM) was chosen for this
study as it is the most widely used technique of 3D printing where objects are created layer by
layer by extruding heated thermoplastic material through a nozzle. The FDM 3D printers have
several limitations such as long printing time, the need for monitoring, and different defects of
printed parts. Utilizing sensor data from the FDM printer, the monitoring of the printing process
and parameters facilitates real-time defect detection in situ, concurrently feeding a virtual model
with sensor data for comprehensive analysis.

2 Literature Review
Several research studies have been conducted on developing a digital twin for MEX 3D printing.
The general process workflow of digital twin for 3D printing was described by Kantaros et al.


---


## Page 3


(2021). They investigated interconnection between digital and physical systems where the main
aim of the digital twin is to monitor and optimize process parameters to obtain high quality prints.
Different authors use different methods by integrating particular types of advanced technologies
such as machine learning, image processing, and IoT to achieve this goal, hence they are pillar
technologies of digital twin (Kantaros et al. 2021). Barbosa and Aroca (2017) have proposed IoT
architecture for the control and monitoring of 3D printing processes. The main component of this
architecture is Beacons installed on a 3D printer that allows data transfer via Bluetooth technology.
Those beacons continuously send data to a web address where users can remotely access all data
about the 3D printer’s parameters via mobile devices in real time (Barbosa and Aroca 2017).
However, this architecture uses data only from the 3D printer's serial connection, which, for some
parameters, shows preassigned values rather than real-world data. In comparison, Chhetri et al.
(2019) have presented IoT based methodology by utilizing some sensors to develop digital twin
for MEX systems. Their method is based on using side channels to identify abnormal faults and
improve the quality of printed parts. They used vibration, acoustic, power, and magnetic sensors
to represent the physical status of their 3D printer (Chhetri et al. 2019). Several similar studies
have been conducted such as digital twin application of FDM printers through cloud and edge
systems to real-time monitoring and controlling, and managing printing tasks effectively (Guo et
al. 2021). Another research study employed a novel approach for real-time monitoring of 3D
printers ensuring surface quality through online monitoring strategies using various sensor types
such as accelerometer, thermal camera, current, pressure, and force sensors. It highlights the
effectiveness of non-contact high-performance techniques (Lishchenko, Piteľ, and Larshin 2022).
Similarly, the research by Kazhymurat, Shehab, and Ali (2022) uses a data-receiving approach
from sensors such as thermocouples, accelerometers, thermistors, and a camera for real-time
monitoring of FDM printers remotely.
Only monitoring the 3D printer’s parameters is not enough to build fully functionable
digital twin. The data about 3D printer’s status should be analyzed to optimize necessary
parameters. Sampedro et al. (2022) have presented a machine-learning algorithm to detect nozzle
clogging which is one of the undesired FDM 3D printer’s failures. Their machine-learning
algorithm could predict nozzle clogging with 97% accuracy. Likewise, Butt and Mohaghegh
(2022) also investigated filament extrusion from the nozzle of a 3D printer by using machine
learning. However, they focused on the effect of the extrusion system on the quality of the print.
They collected data by changing different parameters of the extrusion system such as nozzle
temperature and filament feed rate and evaluating the quality of those prints by measuring surface
roughness, tensile, and hardness (Butt and Mohaghegh 2022). Similar research work has been
conducted by Pazhamannil, Govindan, and Sooraj (2021) by using Artificial Neural Network
(ANN) to predict the tensile strength models considering different parameters such as layer
thickness, nozzle temperature, and infill speed. The experiments validate the model within the
range of 5% agreement. In another study, researchers used a Convolutional Neural Network
(CNN), trained on vibration patterns and data, to classify items as good or faulty, reducing
production time and preventing material waste (Scheffel, Fröhlich, and Silvestri 2021). The
research by Tang and Wu (2024) proposes a method for detecting failures independently in 3D-
printed pieces without human involvement. Using three networks proposed in this paper,
specifically trained for brightness or illumination conditions, achieves better average precision


---


## Page 4


(AP) and log-average miss rate (AM) in failure detection compared to training networks with mixed
samples of various illumination conditions (Tang and Wu 2024). The research by Kumar et al.
(2023) presents a technique utilizing artificial intelligence to identify irregularities at each printing
layer. By merging pre-existing models with a Support Vector Machine, the study attains the utmost
precision using Alexnet. This strategy provides an economical resolution for instant defect-
recognition in FDM printing (Kumar et al. 2023).
 Another method of real-time monitoring and defect detection is by using image processing.
Henson, Decker, and Huang (2021) proposed a new method of real-time distortion and failure
detection by using cameras. The authors used three cameras to capture 3D-printed parts from three
different positions. Those cameras are linked to MATLAB software to process images in real time.
The captured images from different perspectives are compared with a 3D model of the object for
the presence of any geometrical distortion (Henson, Decker, and Huang 2021). In comparison,
Moretti, Rossi, and Senin (2021) used a digital video microscope to obtain optical imaging of a
printed layer for its contour identification and stacking. The device was installed near the nozzle
of the 3D printer to capture each printed layer from the top view. The image processing was applied
to compare printed layer contours with preassigned ones in Gcode (Moretti, Rossi, and Senin
2021). Another study suggests a sophisticated learning framework employing Convolutional
Neural Networks (CNNs) to recognize defects in 3D printing, obtaining an accuracy rate of 84%.
By combining image analysis and artificial intelligence, the framework can detect defects and
pause the printing process. Despite its efficacy, challenges include the inability to spot flaws on
vertical surfaces and varying performance caused by a limited dataset (Farhan Khan et al. 2021).
Serial communication-based techniques, discussed in the next article, enable efficient data capture
via cameras for continuous monitoring of nozzle location and timely identification of object tilting.
Compared to 3D scanners, these techniques provide affordable and efficient monitoring solutions,
enhancing additive manufacturing quality control (Jeong et al. 2017).  Another study by Su, Hicks,
and Nassehi (2023) investigates the influence of fidelity on the effectiveness of digital twins (DTs)
in detecting material extrusion failures during 3D printing, such as extrusion errors and layer shifts.
Using image-based comparisons, the study highlights that low-fidelity digital twins can achieve
performance comparable to high-fidelity counterparts while reducing costs related to data storage,
configuration, and simulation time (Su, Hicks, and Nassehi 2023).
The above literature indicated that the authors have not developed a graphical user interface
with a digital copy of a 3D printer. However, several papers proposed a digital replica of an FDM
3D printer. Pantelidakis et al. (2022) built their digital twin in Unity 3D that mimics the real 3D
printer by using data from the printer itself and embedded sensors. Similarly, Rachmawati et al.
(2023) proposed a digital twin platform that can be created in Unity 3D. They also showed that
Lightweight Convolutional Neural Network (LCNN) can be used for fault detection based on
sensor data. In comparison, Corradini and Silvestri (2022) visualized not only the 3D printer’s
motion only, but also material extrusion as well. They used encoders embedded in the stepper
motors to track the nozzle position of the 3D printer. At the same time, thermocouples are used to
provide data about temperature. Then, the authors used those data to visualize the 3D printing
process by using Panda3D and Python libraries. Then, real 3D printed parts and visualized parts
are compared and analyzed (Corradini and Silvestri 2022). Another research was done by
Jyeniskhan et al. (2023) incorporates machine learning, image processing, and 3D visualization of


---


## Page 5


the printing process. They used OctoPrint to collect printer data and Unity to visualize printing.
Their ML EfficientDet-Lite model could detect geometry-related defects with high efficiency
(Jyeniskhan et al. 2023).

Table 1 Summary of literature review on Digital Twin for MEX 3D Printing

Category
Study
Key Contributions
Limitations/Challenges
IoT
Integration
(Barbosa
and
Aroca 2017)
IoT architecture using beacons for
remote monitoring via Bluetooth.
Relies on preassigned values,
lacks real-world data from sensors.

(Chhetri
et
al.
2019)
IoT-based monitoring with vibration,
acoustic, power, and magnetic sensors
for fault identification.
Limited discussion on parameter
optimization.

(Kazhymurat,
Shehab, and Ali
2022)
Real-time
monitoring
using
thermocouples, accelerometers, and
cameras.
Primarily focused on monitoring;
lacks optimization strategies.
Machine
Learning
Models
(Sampedro et al.
2022)
Detects nozzle clogging with 97%
accuracy using machine learning.
Focused only on nozzle clogging.

(Butt
and
Mohaghegh 2022)
Evaluated extrusion system effects on
print quality using ML.
Lacks real-time feedback to the
printer.

(Pazhamannil,
Govindan,
and
Sooraj 2021)
ANN
model
predicting
tensile
strength with ~5% error margin.
Limited scope on tensile strength
alone.

(Tang
and
Wu
2024)
Independent failure detection using
illumination-specific CNNs.
Requires
multiple
networks;
varying performance under mixed
illumination.

(Kumar
et
al.
2023)
AI-based
layer-by-layer
defect
detection integrating AlexNet with
SVM.
Dataset
limitations;
cost
considerations
for
layer-wise
monitoring.
Image
Processing
(Henson, Decker,
and Huang 2021)
Real-time distortion detection with
multi-camera setup.
Geometrical
focus
only;
no
optimization insights.

(Moretti,
Rossi,
and Senin 2021)
Top-view layer contour comparison
using optical imaging.
Focused only on single-layer
contours.

(Farhan Khan et
al. 2021)
CNN-based framework integrating
image analysis for defect detection
with 84% accuracy.
Limited dataset; challenges in
detecting vertical surface flaws.
Digital
Twin
Platforms
(Pantelidakis et al.
2022)
Unity
3D-based
digital
twin
mimicking real 3D printer operations.
Visualization without autonomous
decision-making.

(Rachmawati et
al. 2023)
Unity 3D platform with LCNN for
fault detection.
Does not justify sensor selection
comprehensively.

(Corradini
and
Silvestri 2022)
Visualized material extrusion using
encoders,
thermocouples,
and
Panda3D.
Limited integration of autonomous
controls

(Jyeniskhan et al.
2023)
Combines OctoPrint data, Unity
visualization, and EfficientDet-Lite
ML for defect detection.
Geometry-focused
only,
lacks
real-time optimization.


---


## Page 6


The previous studies show that all the important printing parameters while building their digital
twin were not investigated. Additionally, most of the researchers have not justified their choices in
sensor selection. For instance, Infrared distance sensors have an accuracy of 3-5 mm, which is
large for a 3D printer. It is also apparent that real-time autonomous decision-making was not
considered in the previous research efforts.
3 Methodology
3.1 Overview
The primary element of any digital twin is data. In this research, two types of data are employed
to construct the digital twin as shown in Fig. 1. The first type originates from a printer and can be
obtained by sending specific Gcode commands through the serial port. For instance, temperature
readings from thermistors under the bed and inside the hot end can be acquired using the M105
command, and the Gcode line being processed allows us to determine nozzle position and track
the progress of a print. The second type of data is generated from the embedded sensors. Since
most affordable 3D printers only have temperature sensors, additional external sensors are installed
to measure printing parameters. Following data collection, the next step involves analyzing the
gathered information. The system is designed to independently analyze data and identify any
printing issues. It should also have the capability to autonomously pause or stop the print in case
of anomalies. The final component of the digital twin system is the graphical user interface (GUI)
in platforms such as Unity. A user-friendly interface is developed to enable users to remotely
monitor and control the 3D printing process. The printer and sensor data are displayed in an
organized manner to users.


Fig. 1 Stages of Digital Twin development


---


## Page 7


3.2 Identification of Parameters
The data collection stage commenced with the identification of the necessary printing process
parameters that have an impact on component quality. The selected process parameters are nozzle
temperature, nozzle position, bed temperature, vibration, and filament flow rate as shown in Fig.
2. Those five parameters are crucial for every FDM 3D printer and are responsible for common
printing defects (Fig. 3). Nozzle temperature determines the material's melting characteristics,
while nozzle position ensures precise layer deposition for accurate prints. Bed temperature
influences initial layer adhesion, preventing warping issues. Vibration control is essential to avoid
print defects caused by excessive printer movements. Lastly, filament flow rate directly impacts
layer thickness and overall print quality.
The interplay among the five key parameters in 3D printing is critical for optimizing print
quality and minimizing defects. Nozzle temperature affects filament viscosity and flow rate, while
nozzle position determines extrusion paths and influences flow consistency. Vibrations can disrupt
nozzle movements, affecting positioning precision and filament flow. Furthermore, vibrations
caused due to high acceleration can cause layer shifting. Many 3D printing defects arise from the
interaction of multiple incorrectly configured printing parameters. Zits and blobs, for instance, are
caused by improperly configured nozzle temperature and extrusion/retraction settings.
Acceleration and retraction settings also can cause deformed edges at the end of printing paths
(Papazetis and Vosniakos 2019). The extruder pushes on the filament like a spring, maintaining a
roughly constant pressure in the nozzle as printing progresses. Consequently, whenever the print
head decelerates, the excess pressure can lead to over-extrusion. It's observed in the literature
review that many researchers tend to concentrate on just one or two of these printing parameters.
However, for building fully functional digital twin, all five parameters should be covered.

Fig. 2 Working principle of the FDM and key process parameters (Vaes and Van Puyvelde 2021)


---


## Page 8


Fig. 3 Process parameters and printing defects

3.3 Sensor Integration
Selecting appropriate sensors is a key enabler for the development of a sensor-based digital twin
for FDM 3D printers. The choice of sensors directly impacts the accuracy, reliability, and
functionality of the digital twin system. Several key criteria should guide sensor selection. Firstly,
sensors must be capable of capturing relevant data with sufficient accuracy and precision.
Additionally, sensors should offer suitable resolution and dynamic range to capture variations in
the printing process effectively. Moreover, consideration should be given to the sensor's sampling
rate to ensure real-time monitoring and control. Furthermore, factors such as ease of integration
and cost-effectiveness should also be considered. Table 2 shows the basic criteria for sensor
selection for this research.
Table 2 Sensors selection criteria

Sensors
Data samples
per second
Resolution
Accuracy Cost
Size
Vibration
100-1000
16 bits
95-99%
up to 20$ Compact and
lightweight
Filament flow
1-2
1-5 mm
(filament
length)
95-99%
up to 20$ Compact and
lightweight
Nozzle position
5-10
0.01-0.1 mm 95-99%
up to 20$ Compact and
lightweight

To evaluate the suitability of different sensors for 3D printing applications, a comparative analysis
of their technical features, performance, and cost-effectiveness was conducted. Table 3
summarizes key specifications such as data sampling rate, measurement range, accuracy, size, and
cost, assigning scores based on their relevance and efficiency for monitoring parameters like


---


## Page 9


vibration, nozzle position, and filament flow. The scoring system provides a quantitative
assessment to identify the most effective sensor for specific tasks.

Table 3 Comparative Analysis of Sensors for 3D Printing Parameters


Technical
features
Data
samples
per second
Measurement
range
Accuracy
Cost
Size
Score
Vibration
MPU9255
accelerometer
Three-
directional
(10/10)
Up to 4000
Hz (10/10)
±2g to ±16g
(10/10)
±2
%
of
sensitivity
(10/10)
16$
(8/10)
31.2 x 17
mm
(10/10)
58/60
801S
Vibration
sensor

No direction
(5/10)
Up to 1000
Hz (9/10)
Not
found
(7/10)
Adjustable
(10/10)
8$
(10/10)
35 x 11.5
mm
(10/10)
51/60
Taidacent
DC24V
Piezoelectric
Vibration
Sensor
No direction
(5/10)
Up to 1000
Hz (9/10)
Up
to
20g (10/10)
Not
found
(7/10)
200$
(2/10)
24
x
56
mm
(10/10)
43/60
Nozzle position
VL53LOX
distance
sensor
Laser based
(optical)
(8/10)
Up to 50
Hz (10/10)
Ranging
length:
≤2M
(8/10)
1-3
mm
(affected
by
environmental
conditions and
target
characteristics)
(2/10)
10$
(10/10)
25 x 12.2
mm
(10/10)
48/60
Adoric digital
calipers
Capacitive
displacement
sensor
(10/10)
2 Hz (7/10)
Ranging
length:
depends
on
length of the
caliper (10/10)
±
0.1
mm
(10/10)
10$
(10/10)
62 x 32 x
15
mm
(10/10)
57/60
Signswise
optical
encoder
Optical
encoder
(5/10)
0-20 KHz
(10/10)
360 pulses per
revolution
(10/10)
1
degree
(10/10)
24$
(8/10)
38 x 35.5
mm
(10/10)
53/60
Filament flow
N20
DC
Geared Motor
Encoder

Magnetic
encoder
(10/10)
0 – 50 Hz
(10/10)
7 pulses per
revolution
(9/10)
51.43 degrees
(7/10)
13$
(10/10)
15 x 10.5 x
10.5
mm
(10/10)
56/60
Signswise
optical
encoder
Optical
encoder
(10/10)
0-20 KHz
(10/10)
360 pulses per
revolution
(10/10)
1
degree
(10/10)
24$
(8/10)
38 x 35.5
mm (8/10)
56/60


---


## Page 10


The first printing parameter is vibration which can have a significant impact on FDM 3D
printing. Unnecessary vibrations can cause the extruder to move unintentionally, resulting in the
layer height being inconsistent, or the layers not bonding properly. The vibration can be measured
by using special sensors based on the principle of piezoelectricity. Piezoelectricity is a
phenomenon in which certain materials generate an electric charge in response to applied
mechanical stress. The 10 DOF IMU (MPU9255) sensor is used (Fig. 4) as it has an accelerometer
to sense acceleration in the x,y, and z directions. The MPU9255 has a measurement range of ±2g,
±4g, ±8g and ±16g. The vibration tracking of an FDM 3D printer was successfully conducted by
several papers (Isiani et al. 2023), (Zhang et al. 2019), and (Li et al. 2019) by using MPU-based
accelerometers. The ±2g measurement range was selected for accurate tracking without saturating
the sensor. The sensitivity scale factor for the ±2g range is 16384 LSB/g. According to the
datasheet of the sensor, the output data rate can reach up to 4000 Hz. The bandwidth of 115200
was employed with a sample rate of 830 Hz to accurately capture the vibrations without
overloading the system at the same time. The main advantage of using an accelerometer compared
to other vibration sensors is its ability to sense vibration in three directions independently. The
selected sensor is mounted on the nozzle of the 3D printer.

Fig. 4 Installed vibration sensor
Another important parameter of FDM 3D printers is the amount of filament being extruded.
Most of the portable 3D printers do not have sensors that track the filament usage. In reality, it is
an important parameter that is responsible for the quality of the printed part. Tracking the filament
allows detecting and predicting under extrusion and filament run out or breakage. Some modern
FDM 3D printers have filament sensors, but most of them are designed to detect only filament
breakage or runout. The best option for tracking filament flow rate is by using encoders. There are
various types of encoders in the market designed for different purposes at various prices. The
cheapest option proposed by this paper is using magnetic encoders. A filament sensor is shown in
Fig. 5 is constructed by using a magnetic encoder and extruder components. The extruder gear is
connected to a shaft that rotates freely in a bearing. The magnetic encoder is also connected to this
shaft and rotates when the filament is being extruded or retracted. The sensor is connected to the
Arduino that converts the pulses to the length of filament in millimeters. The extrusion system
(with extruder gear and idler bearing) of the 3D printer and filament sensor (with gear and idler


---


## Page 11


bearing) are located separately. The slippage that might occur in the extrusion system due to
different reasons, e.g. nozzle clogging can be captured by the filament sensor as the encoder stops
rotating in that case. Furthermore, under-extrusion also can be detected by comparing Gcode data
with filament sensor readings in real time.


Fig. 5 Filament sensor
The capacitive displacement sensors would be the best option for nozzle/bed position
measurement. They give stable output and have 0.01-0.1 mm deviation depending on its price
which is suitable for FDM 3D printers. Fig. 6 shows the structure of a capacitive displacement
sensor. These sensors consist of a collection of grid capacitances and signal processing circuits.
The grid capacitances are divided into stator grid capacitance and sliding grid capacitance. On the
slider, another printed circuit board contains 48 separate etched grids known as emitters. Together,
these printed circuit boards form two variable capacitors. As the slider moves, the capacitance
changes in a linear and repeating pattern which allows to measure the linear displacement
precisely. The position of the nozzle can be directly obtained from the pulses provided to the
stepping motors by the controller, however, 3D printers can skip steps for x or y axes because of
mechanical issues such as loose belts. As displacement sensors are installed on the nozzle and bed
directly, they show real-world positions.


---


## Page 12


Fig. 6 Structure of capacitive displacement sensor
The capacitive sensors used in this setup are obtained from Adoric digital calipers. They
have a resolution of 0.1 mm which is sufficient for position tracking of FDM 3D printers. The
length of the scale of those digital calipers is 150 mm. The other advantage of capacitive
displacement sensors is that their scale length can be elongated by adding capacitive grids. The
length of the scale of the assembled position sensors for the x and y axes in this setup is 200 mm.
To integrate them into the 3D printer, the original cases of the digital calipers are replaced with
custom 3D-printed cases. Four wires, namely 3.3V, GND, CLOCK, and DATA, are connected to
corresponding pins on the electronic module. These pins are then linked to the Arduino Mega,
enabling the reading of sensor values. Slider of the position sensor for X axis is fixed with the
nozzle, while the slider of the position sensor for the Y axis is fixed with the bed (Fig. 7). They do
not resist the movement of the 3D printer and slide freely.

Fig. 7 Installed position sensors for X and Y axes


---


## Page 13


3.4 Data Transfer
One of the crucial parts of the system is data transfer between DT system components. The smooth
data flow between a real 3D printer and its digital twin makes the system reliable and provides a
satisfying user experience. Fig. 8 represents the data flow between the digital twin components.
The 3D printer is connected to the computer via a USB cable. The pyserial package of Python
allows to communicate with the 3D printer to receive data and send commands. Furthermore,
Arduino modules are used to collect the sensor data and they are connected to the computer. The
Python file receives data from the 3D printer and Arduino modules via a serial port and sends it to
a database. After comparing the various databases, Firebase was selected for this project. Firebase
is mostly preferred for real-time applications, and it is easier to set up. It is a NoSQL database that
syncs and stores data in real time. Unity is selected as the graphical user interface. The data
collected in Firebase can be easily accessed in Unity. Unity platform allows users to remotely
monitor and control the 3D printing process from a mobile phone or laptop. All necessary data
from the printer and sensors are presented in the GUI.

Fig. 8 Data transfer between DT components

4 Experimental Results
The merging of real-time data into digital replicas serves as a foundation, highlighting the essential
role of data in digital twin development. By integrating data collected from attached and in-built
sensors, the digital replicas are enriched with the flexibility needed to mimic real-life
circumstances. These data not only feed digital twin but are also used for defect detection by
utilizing defined analytical analysis. The purpose of the experiments is to evaluate the performance
of the attached sensors and test their efficiency in defect detection in the process-level digital twin.


---


## Page 14


4.1 Vibration Sensor and Anomaly Detection
The vibration sensor was tested at various printing speeds. The typical print speed for most of the
FDM 3D printers is 60 mm/s. Fig. 9 shows acceleration values for the Z axis at 30 mm/s, 60 mm/s,
and 120 mm/s. Higher print speed causes additional vibrations as can be seen in the Fig. 9.
Furthermore, it causes overheating (Fig. 10) as the nozzle fan could not cool the deposited layer
on time. The acceleration values for typical print speed can be used to detect anomalies during 3D
printing. The anomalies can occur due to issues with mechanical parts such as loose screws or
belts. The typical acceleration values for 60 mm/s print speed are between 14000-19000 LSB/g
according to the experiment. Furthermore, it can be used to optimize the print speed according to
the vibration values.

Fig. 9 Vibration tracking at different printing speeds

13000
14000
15000
16000
17000
18000
19000
20000
0
100
200
300
400
500
600
Acceleration (LSB/g)
Time (s)*10e-1
V=30mm/s
V=60mm/s
V=120mm/s


---


## Page 15


Fig. 10 Sample cube printed with different print speed

4.2 Filament Flow Sensor and Material Counting
The filament sensor's performance was assessed by printing a sample withdog bone shape.
According to the Cura slicer, the actual filament length needed for this sample is 568.6 mm. The
sample was printed ten times, and the sensor readings were recorded (Fig. 11). The test revealed
that the filament sensor readings varied within a 16 mm range compared to the actual value (Table
4). This difference in sensor recordings can be attributed to two factors. Firstly, the magnetic
encoder's accuracy is approximately 5.3 mm, as it produces only 7 pulses per rotation. Secondly,
the filament sensor was not installed right next to the extruder, resulting in a slight deviation due
to the distance between the extruder and the filament sensor. Nevertheless, this test indicates that
the filament sensor is capable of detecting under-extrusion defects during the printing process. The
case of an under-extrusion defect was created by using a worn extruder gear. This happens when
users ignore the maintenance of their 3D printer and forget to replace extruder gear. The same
specimen was printed 10 times and recorded values were compared with experimental values with
the normal gear. From Table 4, filament sensor readings showed that less amount of filament was
extruded with the worn gear.


---


## Page 16


Fig. 11 Printed samples for filament sensor test with (a) normal extruder gear and (b) worn
extruder gear
Table 4 Amount of filament to print the sample

Trials Actual value
Normal gear Worn gear
1
568.6 mm
567.1 mm
466.4 mm
2
568.6 mm
561.8 mm
471.7 mm
3
568.6 mm
556.5 mm
455.8 mm
4
568.6 mm
572.4 mm
471.7 mm
5
568.6 mm
561.8 mm
461.1 mm
6
568.6 mm
556.5 mm
455.8 mm
7
568.6 mm
561.8 mm
466.4 mm
8
568.6 mm
567.1 mm
461.1 mm
9
568.6 mm
572.4 mm
471.7 mm
10
568.6 mm
567.1 mm
466.4 mm
Mean
564.45 mm
464.81 mm


---


## Page 17


Average Error
0.73 %
18.3 %
Standard deviation 5.72 mm
6.15 mm

4.3 Nozzle/bed Position Sensor and its Application
Fig. 12 shows real-time nozzle path visualization in Unity based on Gcode and position sensor
readings. The black lines show the nozzle path according to the Gcode, while the red dots show
sensor readings. The Python file receives sensor data from Arduino modules and sends it to the
Firebase. Furthermore, it sends GCode commands to the Firebase after sending them to the 3D
printer. Those data from Firebase are accessed in Unity. Unity interprets and displays this data,
utilizing LineRenderer for the black lines and circular game objects for sensor data. The Python
file ensures a smooth transfer of information between sensors, Firebase, and Unity. Notably,
position sensor data is updated every second, resulting in a lower number of red dots at higher
print speeds. The red dots that show nozzle position according to the sensors are not evenly
distributed mainly for two reasons. The first reason is that the sensor data do not go directly from
the Arduino microcontroller to the Unity GUI. The Python file sends sensor data from the serial
port to the Firebase database, and then they are accessed by Unity GUI. Therefore, it depends on
how fast Python and Unity GUI execute commands related to the position sensor. Secondly, nozzle
speed and acceleration vary over the printing process which leads to uneven distribution of red
dots. Nevertheless, this setup enables real-time tracking of nozzle positions during the printing of
outer layers, a critical factor in identifying layer-shifting defects.

Fig. 12 Nozzle path visualizations in Unity
The final destination of the data transferred in this DT system is Unity GUI. The data from
serial ports go to the Firebase through Python and is accessed in Unity GUI. The data transfer lag


---


## Page 18


between Python and Unity GUI was measured by printing position sensor data on their consoles.
As can be seen from Fig. 13, the data transfer lag varies between 500-700 milliseconds.


Fig. 13 Data lag between Python and Unity GUI

4.4 Autonomous Defect Detection
The proposed Digital Twin system should autonomously detect a printing defect according to the
sensor values. A Python file continuously checks and compares sensor values with GCode data. It
receives sensor data from the Arduino modules via a serial port and reads GCode from the laptop.
If there is an anomaly in sensor data, it should warn the user or pause the print. The three sensors
were embedded in this study; therefore, defects related only to those three sensors are considered.
Fig. 14 illustrates the flowchart detailing the autonomous defect detection working principle
employed in this study. The defect detection methodology relies on a straightforward comparison
technique. Two Python files operate simultaneously for this purpose. The "print.py" file manages
communication with the 3D printer, sending Gcode commands line by line from a file, and
receiving temperature readings. On the other hand, the "sensorData.py" file receives data from
sensors and checks them for anomalies. It compares sensor values against predefined thresholds
set by the user, and if an anomaly is detected, it toggles the "isPaused" variable to 1. When
"isPaused" equals 1, "print.py" stops sending Gcode commands to the 3D printer, pausing the print
job. The acceleration threshold in this study was configured within the range of 14000-19000
LSB/g, while the thresholds for filament sensor and GCode deviation were set at 15 mm (Fig. 15).
The nozzle position data from G-code and position sensors are not compatible for direct
comparison as they are not received at the same time. Additionally, G-code data represents


---


## Page 19


destination points, whereas position sensor data shows the exact position of the nozzle. Therefore,
it checks only whether sensor data are within the outer walls. In this paper, only a square shape is
considered for its easiness to perform comparison.

Fig. 14 Autonomous defect detection flowchart


---


## Page 20


Fig. 15  Algorithmic representation of defect detection

Fig. 16 shows an example of under-extrusion detection; when the difference between
sensor data and Gcode is more than 15 mm it pauses the print by sending the M25 command to
the 3D printer. This approach can detect all filament flow-related defects such as under extrusion,
filament runout/breakage, and nozzle clogging.

Fig. 16 Under extrusion detection


---


## Page 21


The position sensors were tested to identify their capability to capture position anomalies
during the layer shifting. The cube with 25x25x25 mm dimension was printed with 25% infill and
with 60 mm/s print speed.

Fig. 17 Printed cube with shifted layers
Table 5 displays nozzle path visualizations in the Unity GUI before and after layer shifting.
The images depicting Layers 27-36 reveal that red dots were captured outside of the outer walls,
indicating a shift in the printing layer along the X-axis. The number of red dots outside the print
boundary varies between 3 and 8.
Table 5 Nozzle path visualizations in Unity GUI

Before layer shifting
Layer 1
Layer 2
Layer 3
Layer 4
Layer 5

Layer 6
Layer 7
Layer 8
Layer 9
Layer 10



After layer shifting


---


## Page 22


Layer 27
Layer 28
Layer 29
Layer 30
Layer 31




Layer 32
Layer 33
Layer 34
Layer 35
Layer 36






4.5 Graphical User Interface (GUI) Integration
The Python file sends GCode to the 3D printer line by line. After sending the GCode line to the
3D printer, it should send it also to the database (Fig. 18). However, a 3D printer can execute
multiple GCode line commands within one second. In contrast, Python cannot transmit several
GCode lines to the database in such a short amount of time, thereby slowing down the 3D printer.
To solve this problem, a buffering method was used to collect GCode commands and send them
to the database every second. Each second, a different amount of data is received by the database
without interrupting the 3D printer. The data in the database is used for visualization in Unity.

Fig. 18 Firebase database screen


---


## Page 23


Fig. 19 shows a Graphical User Interface built in Unity. The interface contains all the
necessary information about the print state. The progress information about a print includes
elapsed and remaining print time. Thermistor readings are also presented in the GUI showing
nozzle and bed temperatures. Furthermore, there are control commands available for a user like
pause or cancel. The GUI also integrates sensor data to offer ground truth information, allowing
users to monitor accelerometer readings and view real-time plots by activating the "Plot" button.
Filament flow data is also presented in the GUI which includes filament sensor recordings and “E”
value from the Gcode. Users can monitor the difference between these two values in real time.
Furthermore, nozzle position data received from position sensors is available in the GUI, enabling
users to track the nozzle path by selecting the "Visualize" button. The nozzle path is visualized for
each layer using black lines (representing G-code) and red dots (indicating sensor data). Nozzle
movement is visualized with a 3D copy of the 3D printer. The 3D model of the 3D printer is
divided into several game objects such as nozzle, bed, x_rod, and frame. Those game objects are
used to simulate the printer movement in real time.

Fig. 19 GUI in Unity


---


## Page 24


5 Discussion
The research paper offers a detailed examination of Digital Twins (DTs) customized specifically
for the field of additive manufacturing. This study aims to tackle the limitations and obstacles
faced in traditional Fused Deposition Modeling (FDM) 3D printing methods. Previous studies have
mainly concentrated on specific functions of DTs for 3D printing, including monitoring process
variables and detecting defects. However, these studies often neglect important printing
parameters, the rationale for sensor selection, and decision-making during printing processes.
Addressing these research gaps, this research studies the DT technology by preferring a
comprehensive approach that covers data collection, sensor integration, real-time monitoring, and
defect detection strategies. The proposed DT system shows the potential in improving the
efficiency, quality, and dependability of FDM 3D printing procedures.
Additionally, the results of the experiments demonstrate the efficiency and practicality of
the suggested DT system in real-life scenarios. By conducting thorough tests and verification
processes, the research illustrates the capabilities of the developed sensors in monitoring important
printing parameters, identifying irregularities, and facilitating automated detection of defects. This
research work integrates various sensors including accelerometer, capacitive displacement sensors,
and magnetic encoder to monitor crucial parameters such as vibrations, nozzle position, and
filament flow. Through meticulous data acquisition and analysis, this research study addresses
common printing defects such as under-extrusion, layer shifting, and excessive vibrations.
Moreover, the incorporation of a Graphical User Interface (GUI) and decision-making process
facilitates real-time monitoring and automatic print pausing upon defect detection, enhancing the
overall efficiency and reliability of the printing process.
A summary of previous research studies and this research work is illustrated in Table 6.
Economically, the choice of low-cost components like the MPU9255 accelerometer and the
exclusion of third-party platforms for control and processing, as opposed to costly piezoelectric
sensors or cloud-based systems, makes this system more accessible for smaller-scale or budget-
constrained applications. Additionally, the simplicity of its threshold-based defect detection
algorithms allows for straightforward customization and maintenance, making it more suitable for
practical deployment. The system’s reliance on Python for real-time data processing and Unity for
visualization ensures a modular and user-friendly architecture, which reduces the learning for
highly specialized systems. Generalizability is another critical strength, as the system’s modular
design and comprehensive parameter coverage enable adaptation to a wide range of FDM 3D
printers and potential integration of additional features, such as augmented reality for enhanced
visualization.
Table 6 Summary of relevant studies

Authors
Data
acquisition
Sensors
Defects
Technique
Graphical
User
Interface
Decision
making


---


## Page 25


Farkhan
Khan et al.
(2020)
-
Camera
Geometrical
anomalies,
CNN - Deep
learning model
-
Real-time
geometrical
anomaly
detection
Jeong et al.
(2017)
Serial port
Camera
Geometrical
deviations
Point matching for
comparison
-
Not automatic,
but provides
notifications
regarding errors
Pantelidak
is et al.
(2022)
Octoprint
 IR sensor (nozzle
position),
thermocouples
(nozzle and bed
temperature)
-
-
Unity 3D
-
Corradini
and
Silvestri
(2022)
Octoprint
Encoders for each
axis, thermistors
(nozzle and bed
temperature)
Layer shifting,
nozzle
clogging
 Point cloud analysis
using
CloudCompare
Panda3D
Print is paused
during
anomalies
Rachmaw
ati et al.
(2023)
Raspberry
Pi
Environmental
sensor (humidity
and temperature)
-
Lightweight
Convolutional
Neural Network
(LCNN)
Unity 3D
-
Su, Hicks,
and
Nassehi
(2023)
Web-API
Camera
Layer shifting,
extrusion
errors
Pearson correlation
coefficient (PCC) to
evaluate the
similarity between
the real-world and
rendered images
Blender,
Human–
machine
inter-face
(HMI)
Print is paused
during printing
failures based
on user
threshold value
This study
Serial port
(python)
Accelerometer
(vibrations),
capacitive
displacement sensor
(nozzle position),
magnetic encoder
(filament flow)
Under-
extrusion,
layer shifting,
excessive
vibrations
Comparison between
Gcode data and
sensor data
according to user
threshold
Unity 3D
Automatic print
pausing during
defect
detection

5.1 Potential benefits

Automated defect detection system: Assists in recognizing defects at the outset of the additive
production process, preventing waste of materials, money, and time.
Enhanced effectiveness: Permits constant monitoring and evaluation of the production procedure,
resulting in faster identification and resolution of problems.
Savings on costs: Spotting flaws early on, decreases the necessity for reworking and discarding,
ultimately cutting down on material and manufacturing expenses.
Savings on time: Detecting flaws early on streamlines the production process, reducing setbacks
and ensuring timely completion of goods.


---


## Page 26


Improved quality control: Provides precise measurements and information for evaluating the
quality of printed components, leading to better overall product excellence.
Enhanced experiments: Facilitates more focused tests and modifications based on real-time
information, minimizing waste and maximizing output.
Remote monitoring & controlling from a global network: It can be monitored and controlled
via a global network, which allows remote access to wireless networks anywhere in the world.
5.2 Technical challenges and limitations

The developed digital twin system for 3D printers lacks attention to important factors like security,
privacy, and scalability. While it's commendable that Python, Arduino, Unity, and Firebase were
integrated, the system could be at risk without strong measures in these areas. Adding encryption,
access controls, and scalable storage is crucial to protect against cyber threats, keep user data
private, and allow the system to grow smoothly. By fixing these issues, the digital twin system
could improve 3D printing with more reliability and resilience.
The accuracy and reliability of sensors can vary under different environmental conditions.
For instance, the vibration sensor's performance may degrade in environments with high
electromagnetic interference, affecting its ability to detect minor vibrations accurately. Similarly,
the filament flow sensor is affected by extruder gear slippage or variations in filament properties,
leading to potential discrepancies in the flow rate measurements.
Even though all the sensor data is handled by Python, they cannot be used in Unity on a
full scale. For instance, accelerometer data is shown in Unity with a simplified plot. Furthermore,
the instant or abrupt nozzle movement cannot be captured precisely with position sensors.
6 Conclusion and Future Work
In this paper, a sensor-based digital twin for (DT) FDM 3D printers is presented for real-time
monitoring, control, and autonomous defect detection. The data transfer method for the DT is
proposed that provides a smooth connection between 3D printer, sensors, database, python, and a
user-friendly interface. The proposed data acquisition system incorporates the use of affordable
but accurate sensors to track printing parameters. Each sensor was tested and evaluated to verify
its use in the proposed DT system.  The application of Python allows manual and autonomous
control of 3D printers according to the sensor values. The Graphical User Interface built in Unity
provides all necessary data about the 3D printer from the printer itself and the external sensors as
well. The sensor-based digital twin system proposed in this paper can be implemented for FDM
3D printers due to its numerous benefits. Autonomous defect detection, capable of pausing prints
during anomalies, can save time and costs. This study demonstrated that simple capacitive
displacement sensors can accurately track the nozzle position and detect layer shifting.
Furthermore, integrating magnetic encoders as filament sensors can detect under-extrusion defects.


---


## Page 27


This research is part of an ongoing research project that aims to incorporate the
optimization of printing parameters according to the sensor values using machine learning
algorithms. In the proposed DT system, python sends GCode commands line by line which allows
editing GCode commands in real time for optimization purposes. Furthermore, research effort is
needed to employ machine learning in analyzing sensor data and predicting possible printing
defects. The sensor data are received via Python, therefore it allows to integrate of machine
learning algorithms in real-time by using python libraries. The Graphical User Interface can be
improved by adding material extrusion visualization based on the filament sensor data. Further
study is required to integrate augmented reality (AR) into the developed digital twin as Unity 3D
supports AR applications. Additionally, investigation of adaptive calibration techniques to enhance
sensor accuracy across different operating conditions and printer setups is needed.

Acknowledgments  The experiments are carried out at the research facilities in the Department of
Mechanical and Aerospace Engineering, School of Engineering and Digital Sciences, Nazarbayev
University, 010000 Astana, Kazakhstan.
Author contribution  KS: Modelling, validation, draft; MHA: Supervision, idea generation, draft
correction, NJ: Validation, draft; AA: Supervision, draft correction; ES: Fund acquisition,
supervision, draft correction.
Funding The research is funded by Nazarbayev University under the Faculty Development
Competitive Research Grant Program (FDCRGP), Grant No. 11022021FD2904.

Declarations
Competing interests  The authors declare no competing interests.

Reference
Butt, Javaid, and Vahaj Mohaghegh. 2022. “Combining Digital Twin and Machine Learning for the Fused
Filament Fabrication Process.” Metals 13 (1): 24. https://doi.org/10.3390/met13010024.
Cheng, Kai, Zhi-Chao Niu, Robin C. Wang, Richard Rakowski, and Richard Bateman. 2017. “Smart
Cutting Tools and Smart Machining: Development Approaches, and Their Implementation and
Application Perspectives.” Chinese Journal of Mechanical Engineering 30 (5): 1162–76.
https://doi.org/10.1007/s10033-017-0183-4.
Chhetri, Sujit Rokka, Sina Faezi, Arquimedes Canedo, and Mohammad Abdullah Al Faruque. 2019.
“QUILT: Quality Inference from Living Digital Twins in IoT-Enabled Manufacturing Systems.”
In Proceedings of the International Conference on Internet of Things Design and Implementation,
237–48. Montreal Quebec Canada: ACM. https://doi.org/10.1145/3302505.3310085.
Corradini, Fabio, and Marco Silvestri. 2022. “Design and Testing of a Digital Twin for Monitoring and
Quality Assessment of Material Extrusion Process.” Additive Manufacturing 51 (March):102633.
https://doi.org/10.1016/j.addma.2022.102633.
Farhan Khan, Mohammad, Aftaab Alam, Mohammad Ateeb Siddiqui, Mohammad Saad Alam, Yasser
Rafat, Nehal Salik, and Ibrahim Al-Saidan. 2021. “Real-Time Defect Detection in 3D Printing


---


## Page 28


Using Machine Learning.” Materials Today: Proceedings 42:521–28.
https://doi.org/10.1016/j.matpr.2020.10.482.
Gf, Barbosa, and Aroca Rv. 2017. “An IoT-Based Solution for Control and Monitoring of Additive
Manufacturing Processes.” Journal of Powder Metallurgy & Mining 06 (01).
https://doi.org/10.4172/2168-9806.1000158.
Grieves, Michael. 2011. Virtually Perfect: Driving Innovative and Lean Products through Product
Lifecycle Management. Cocoa Beach, Florida: Space Coast Press.
Guo, Liang, Yunxi Cheng, Yu Zhang, Yingfu Liu, Changcheng Wan, and Jing Liang. 2021.
“Development of Cloud-Edge Collaborative Digital Twin System for FDM Additive
Manufacturing.” In 2021 IEEE 19th International Conference on Industrial Informatics (INDIN),
1–6. Palma de Mallorca, Spain: IEEE. https://doi.org/10.1109/INDIN45523.2021.9557492.
Henson, Christopher M., Nathan I. Decker, and Qiang Huang. 2021. “A Digital Twin Strategy for Major
Failure Detection in Fused Deposition Modeling Processes.” Procedia Manufacturing 53:359–67.
https://doi.org/10.1016/j.promfg.2021.06.039.
Isiani, Alexander, Leland Weiss, Hamzeh Bardaweel, Hieu Nguyen, and Kelly Crittenden. 2023. “Fault
Detection in 3D Printing: A Study on Sensor Positioning and Vibrational Patterns.” Sensors 23
(17): 7524. https://doi.org/10.3390/s23177524.
Jeong, Haedong, Minsub Kim, Bumsoo Park, and Seungchul Lee. 2017. “Vision-Based Real-Time Layer
Error Quantification for Additive Manufacturing.” In Volume 2: Additive Manufacturing;
Materials, V002T01A047. Los Angeles, California, USA: American Society of Mechanical
Engineers. https://doi.org/10.1115/MSEC2017-2991.
Jyeniskhan, Nursultan, Aigerim Keutayeva, Gani Kazbek, Md Hazrat Ali, and Essam Shehab. 2023.
“Integrating Machine Learning Model and Digital Twin System for Additive Manufacturing.”
IEEE Access 11:71113–26. https://doi.org/10.1109/ACCESS.2023.3294486.
Kantaros, Antreas, Dimitrios Piromalis, Georgios Tsaramirsis, Panagiotis Papageorgas, and Hatem
Tamimi. 2021. “3D Printing and Implementation of Digital Twins: Current Trends and
Limitations.” Applied System Innovation 5 (1): 7. https://doi.org/10.3390/asi5010007.
Kazhymurat, Temirlan, Essam Shehab, and Md. Hazrat Ali. 2022. “IoT-Based Real-Time 3D Printing
Monitoring System.” In 2022 International Conference on Smart Information Systems and
Technologies (SIST), 1–5. Nur-Sultan, Kazakhstan: IEEE.
https://doi.org/10.1109/SIST54437.2022.9945778.
Khosravani, Mohammad Reza, Sara Nasiri, and Tamara Reinicke. 2022. “Intelligent Knowledge-Based
System to Improve Injection Molding Process.” Journal of Industrial Information Integration 25
(January):100275. https://doi.org/10.1016/j.jii.2021.100275.
Kiran Kumar, Kommineni, V. Srikanth, G.N.R. Prasad, Bramah Hazela, and Ashish Kumar Tamrakar.
2023. “Fault Detection on the 3-D Printed Objective Surface by Using the SVM Algorithm.”
Materials Today: Proceedings, June, S2214785323033795.
https://doi.org/10.1016/j.matpr.2023.06.016.
Li, Zhiyong, Dawei Zhang, Liangchen Shao, and Shanling Han. 2019. “Experimental Investigation Using
Vibration Testing Method to Optimize Feed Parameters of Color Mixing Nozzle for Fused
Deposition Modeling Color 3D Printer.” Advances in Mechanical Engineering 11 (12):
168781401989619. https://doi.org/10.1177/1687814019896196.
Lim, Kendrik Yan Hong, Pai Zheng, and Chun-Hsien Chen. 2020. “A State-of-the-Art Survey of Digital
Twin: Techniques, Engineering Product Lifecycle Management and Business Innovation
Perspectives.” Journal of Intelligent Manufacturing 31 (6): 1313–37.
https://doi.org/10.1007/s10845-019-01512-w.
Lishchenko, Natalia, Ján Piteľ, and Vasily Larshin. 2022. “Online Monitoring of Surface Quality for
Diagnostic Features in 3D Printing.” Machines 10 (7): 541.
https://doi.org/10.3390/machines10070541.


---


## Page 29


Moretti, M., A. Rossi, and N. Senin. 2021. “In-Process Monitoring of Part Geometry in Fused Filament
Fabrication Using Computer Vision and Digital Twins.” Additive Manufacturing 37
(January):101609. https://doi.org/10.1016/j.addma.2020.101609.
Ortiz, Jesus Hamilton, and Intechopen (Firm), eds. 2020. Industry 4.0: Current Status and Future Trends.
London: IntechOpen.
Pantelidakis, Minas, Konstantinos Mykoniatis, Jia Liu, and Gregory Harris. 2022. “A Digital Twin
Ecosystem for Additive Manufacturing Using a Real-Time Development Platform.” The
International Journal of Advanced Manufacturing Technology 120 (9–10): 6547–63.
https://doi.org/10.1007/s00170-022-09164-6.
Papazetis, George, and George-Christopher Vosniakos. 2019. “Mapping of Deposition-Stable and Defect-
Free Additive Manufacturing via Material Extrusion from Minimal Experiments.” The
International Journal of Advanced Manufacturing Technology 100 (9–12): 2207–19.
https://doi.org/10.1007/s00170-018-2820-1.
Pazhamannil, Ribin Varghese, P. Govindan, and P. Sooraj. 2021. “Prediction of the Tensile Strength of
Polylactic Acid Fused Deposition Models Using Artificial Neural Network Technique.”
Materials Today: Proceedings 46:9187–93. https://doi.org/10.1016/j.matpr.2020.01.199.
Rachmawati, Syifa Maliah, Made Adi Paramartha Putra, Jae Min Lee, and Dong Seong Kim. 2023.
“Digital Twin-Enabled 3D Printer Fault Detection for Smart Additive Manufacturing.”
Engineering Applications of Artificial Intelligence 124 (September):106430.
https://doi.org/10.1016/j.engappai.2023.106430.
Sampedro, Gabriel Avelino R., Danielle Jaye S. Agron, Gabriel Chukwunonso Amaizu, Dong-Seong
Kim, and Jae-Min Lee. 2022. “Design of an In-Process Quality Monitoring Strategy for FDM-
Type 3D Printer Using Deep Learning.” Applied Sciences 12 (17): 8753.
https://doi.org/10.3390/app12178753.
Scheffel, Roberto Milton, Antônio Augusto Fröhlich, and Marco Silvestri. 2021. “Automated Fault
Detection for Additive Manufacturing Using Vibration Sensors.” International Journal of
Computer Integrated Manufacturing 34 (5): 500–514.
https://doi.org/10.1080/0951192X.2021.1901316.
Su, Shuo, Ben Hicks, and Aydin Nassehi. 2023. “Investigating the Influence of Fidelity on the Capability
of a Digital Twin to Detect Material Extrusion Failures.” Journal of Intelligent Manufacturing 35
(5): 2263–76. https://doi.org/10.1007/s10845-023-02144-x.
Tang, Jianning, and Xiaofeng Wu. 2024. “A Fault Tolerant Neural Network for Space-Based 3D Printing
Quality Assessment.” Advances in Space Research 73 (9): 4686–99.
https://doi.org/10.1016/j.asr.2024.01.045.
Vaes, Dries, and Peter Van Puyvelde. 2021. “Semi-Crystalline Feedstock for Filament-Based 3D Printing
of Polymers.” Progress in Polymer Science 118 (July):101411.
https://doi.org/10.1016/j.progpolymsci.2021.101411.
Zhang, Dawei, Zhiyong Li, Shengxue Qin, and Shanling Han. 2019. “Optimization of Vibration
Characteristics of Fused Deposition Modeling Color 3D Printer Based on Modal and Power
Spectrum Method.” Applied Sciences 9 (19): 4154. https://doi.org/10.3390/app9194154.


---
