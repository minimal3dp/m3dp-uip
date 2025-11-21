

# **The Cyber-Physical Convergence: Deterministic Firmware, Algorithmic Slicing, and the Rise of Multimodal AI in Additive Manufacturing**

## **1\. The Shift from Mechanical Approximalism to Computational Determinism**

The history of desktop additive manufacturing (AM), specifically Fused Deposition Modeling (FDM), has been defined by a gradual migration from mechanical approximation to computational determinism. In the early eras of the RepRap movement, print quality was largely a function of hardware rigidity and basic microcontroller stepping. However, the contemporary landscape, illuminated by the emergence of the Klipper firmware ecosystem and advanced slicers like OrcaSlicer, represents a paradigm shift. We are no longer simply pushing plastic through a hot nozzle; we are orchestrating a complex cyber-physical system where fluid dynamics, resonance physics, and kinematic path planning are managed in real-time.

This transition is characterized by a bifurcation in operational philosophy. On one hand, the "firmware-first" community—exemplified by the "Minimal 3DP" ecosystem—advocates for rigorous, deterministic calibration. This approach posits that mathematical precision in the machine’s configuration files is the prerequisite for quality. On the other hand, the "AI-first" sector is introducing probabilistic layers of intelligence, utilizing Large Language Models (LLMs) and computer vision to monitor, correct, and even generate manufacturing instructions. The convergence of these two philosophies—the deterministic control of the machine and the probabilistic oversight of AI—forms the central thesis of modern additive manufacturing research.

### **1.1 The Klipper Architecture: Offloading Kinematics**

The fundamental innovation of Klipper firmware lies in its architectural departure from legacy systems like Marlin. Traditional firmware processes G-code, calculates motion planning, and executes stepper pulses all on a single, often resource-constrained, microcontroller.1 Klipper decouples these tasks. It utilizes a powerful host computer (typically a single-board computer like a Raspberry Pi) to handle the heavy lifting of trajectory planning and kinematic calculations, while the microcontroller serves as a simple, high-speed pulse generator.

This architecture allows for the implementation of advanced physical models that would overwhelm a standard 8-bit or 32-bit microcontroller. Features such as "Input Shaping" (resonance compensation) and "Pressure Advance" (fluid dynamic compensation) rely on complex mathematical transformations that must be executed in real-time. The "Minimal 3DP" resource hub, curated by Mike Wilson, has become a critical repository for documenting the practical implementation of these features, emphasizing that the power of Klipper is useless without precise calibration.2

### **1.2 The Philosophy of Deterministic Calibration**

The ethos of the "Minimal 3DP" approach is grounded in the belief that software compensation should refine, not fix, mechanical issues. Before applying AI monitoring or advanced shaping algorithms, the machine’s physical movement must be mathematically reconciled with its digital instructions. This is most evident in the shift from "E-steps" to "Rotation Distance."

In legacy firmware, calibration often involved a "steps per mm" value—an abstract number that combined motor resolution, microstepping, and gearing. Klipper replaces this with rotation\_distance, a parameter that represents the physical distance the axis moves during one full rotation of the stepper motor.1 This change forces the operator to engage with the physical reality of the machine—pitch, gear teeth, and thread counts—rather than abstract constants.

## **2\. Kinematic Calibration: The Mathematical Foundation of Motion**

The precision of an FDM printer is bounded by the accuracy of its kinematic configuration. If the firmware believes a motor rotation results in 40mm of travel, but physical reality dictates 40.1mm, this error accumulates over the volume of the print, leading to dimensional inaccuracies that no amount of AI monitoring can correct.

### **2.1 Rotational Distance: Belt-Driven Systems**

For axes driven by belts (typically X and Y in CoreXY or Cartesian kinematics), the rotation\_distance is a deterministic value derived from hardware specifications. It is not a value that should be "tuned" empirically based on print results, as doing so often masks other mechanical issues like belt stretch or skew.

The formula for belt-driven axes is defined as:

$$Rotation\\\_Distance \= Belt\\\_Pitch \\times Pulley\\\_Teeth$$
For the vast majority of modern consumer printers utilizing the GT2 belt standard, the belt pitch is 2mm. A standard stepper motor pulley typically has 20 teeth. Consequently, the calculation becomes:

$$2mm \\times 20 \= 40mm$$
This establishes that for every full revolution of the stepper motor, the carriage moves exactly 40mm.4 Klipper documentation and the Minimal 3DP guides stress that this value is mechanically absolute. Deviations in printed part dimensions on X/Y usually indicate mechanical hysteresis, loose belts, or thermal contraction of the plastic, rather than a need to adjust the rotation distance.5

### **2.2 The Z-Axis: Lead Screws and Threaded Rods**

The Z-axis introduces complexity due to the variety of lead screw standards. The calculation requires knowledge of the screw pitch and the number of separate threads (starts). The formula is:

$$Rotation\\\_Distance \= Screw\\\_Pitch \\times Number\\\_of\\\_Threads$$
Common configurations include:

* **T8 Lead Screw:** A pitch of 2mm with 4 starts results in a rotation distance of 8mm ($2 \\times 4$).
* **M8 Threaded Rod:** A pitch of 1.25mm with 1 start results in a rotation distance of 1.25mm.4

Empirical validation is occasionally necessary here, particularly when hardware is replaced or unknown. If a user requests a 300mm move but measures 313mm, the adjustment formula is:
$$ New\_Rotation\_Distance \= Current\_Rotation\_Distance \\times \\frac{Measured\_Distance}{Requested\_Distance}

$$Using the example of a T8 screw (initial distance 8), the correction would be:$$
8 \\times \\frac{313}{300} \= 8.347 $$
This level of granular adjustment allows Klipper to compensate for non-standard hardware configurations often found in DIY or modified machines.6

### **2.3 Extruder Calibration: The Empirical Variable**

Unlike the X, Y, and Z axes, which are rigid systems, the extruder drives a filament that is essentially a fluid-in-waiting. The "hobbed bolt" or drive gear bites into the filament, and the effective diameter of this gear changes based on the hardness of the filament and the tension of the spring. Therefore, extruder calibration is empirical.

The "Measure and Trim" methodology recommended by Minimal 3DP involves:

1. **Preparation:** Heating the nozzle to printing temperature to ensure realistic back-pressure.
2. **Marking:** Placing a mark on the filament at a set distance (e.g., 70mm) from the intake.
3. **Extrusion:** Commanding a slow extrusion of 50mm (e.g., G1 E50 F60). The slow speed (1mm/s) is critical to prevent extruder skipping or pressure buildup from skewing the result.
4. **Measurement:** Measuring the distance from the intake to the mark. If 20mm remains, then 50mm was extruded ($70 \- 20 \= 50$). If 18mm remains, 52mm was extruded.4

The rotation\_distance is then updated inversely proportional to the extrusion error:

$$New\\\_Value \= Old\\\_Value \\times \\frac{Actual\\\_Extruded\\\_Amount}{Requested\\\_Amount}$$
The Minimal 3DP guides emphasize that this process establishes a *mechanical baseline*. Flow rate adjustments in the slicer should be used for fine-tuning per-filament properties, but the rotation distance in Klipper must represent the mechanical reality of the extruder gears.5

### **2.4 Comparison of Calibration Methods**

| Calibration Type | Mechanism | Deterministic vs. Empirical | Update Frequency |
| :---- | :---- | :---- | :---- |
| **X/Y Axis** | Belt Pitch $\\times$ Teeth | Deterministic | Only on hardware change |
| **Z Axis** | Screw Pitch $\\times$ Starts | Deterministic (mostly) | On lead screw replacement |
| **Extruder** | Filament Drive Ratio | Empirical | Initial setup & major maintenance |
| **Flow Rate (Slicer)** | Volume Multiplier | Empirical | Per filament spool/type |

## **3\. Fluid Dynamics and Resonance: Advanced Firmware Compensation**

Once the kinematic motion is calibrated, the focus shifts to the physics of the printing process itself. FDM printing involves moving a heavy print head (mass/inertia) and pushing a viscous fluid (rheology). Klipper addresses these physical limitations through Input Shaping and Pressure Advance.

### **3.1 Input Shaping: Mitigating Mechanical Resonance**

High-speed printing inevitably introduces vibration. As the print head accelerates and decelerates, it induces ringing (ghosting) artifacts on the surface of the print. These are visible echoes of features, caused by the machine oscillating at its resonant frequency.

Input Shaping is a control theory technique that modifies the input signal (the motor commands) to cancel out these resonances. Klipper utilizes an "open-loop" approach where the resonance frequencies are measured beforehand, and the motion planner actively avoids exciting those frequencies.

#### **3.1.1 The ADXL345 Workflow**

While manual "ringing towers" can be used, the gold standard described in Minimal 3DP resources involves using an ADXL345 accelerometer directly attached to the print head.

1. **Data Acquisition:** The firmware vibrates the motors through a frequency sweep (e.g., 10Hz to 100Hz).
2. **CSV Generation:** The resulting vibration data is logged to CSV files (e.g., resonances\_x\_\*.csv) stored in the /tmp directory of the host Pi.7
3. **Analysis:** A Python script (calibrate\_shaper.py) processes these CSVs to generate a power spectral density graph. This graph visualizes the amplitude of vibrations at different frequencies.

#### **3.1.2 Selecting a Shaper Algorithm**

The analysis script suggests a "shaper" algorithm (e.g., ZV, MZV, EI, 2Hump\_EI) based on the data. There is a critical trade-off here: aggressive shapers (like EI \- Exponential Impulse) are robust against frequency shifts but tend to smooth out fine details (corner rounding). Less aggressive shapers (like ZV \- Zero Vibration) preserve sharp corners but require precise frequency matching.

* *Insight:* The "Minimal 3DP" philosophy suggests seeking mechanical stiffness first (tightening belts) to push the resonance frequency higher, rather than relying solely on aggressive software smoothing, which degrades dimensional fidelity.8

### **3.2 Pressure Advance: Compensating for Filament Elasticity**

In a Bowden tube system, there is a significant lag between the extruder motor pushing filament and the plastic actually leaving the nozzle. This is due to the filament compressing and the tube stretching—a hysteresis effect. Without compensation, this leads to under-extrusion at the start of a line (acceleration) and blobs at the end (deceleration).

Pressure Advance (PA) coordinates the extruder move with the carriage acceleration. It pushes extra filament during acceleration to build pressure and retracts during deceleration to relieve it.

#### **3.2.1 Validation Methodologies**

OrcaSlicer and Klipper provide three methods for tuning PA, each with distinct advantages:

* **The Tower Method:** A hollow tower is printed where the PA value increases with Z-height.
  * *Formula:* $PA \= Start \+ (Height \\times Step)$.
  * *Pros:* Robust, tests a wide range.
  * *Cons:* Slow, requires calipers to measure the height of the "best" corner.9
* **The Line Method:** Prints parallel lines at different PA values on the build plate.
  * *Pros:* Extremely fast.
  * *Cons:* Highly sensitive to First Layer calibration. If the nozzle is too close to the bed, the lines will look squished regardless of the PA value, leading to false positives. Enabling bed mesh leveling is mandatory for accuracy here.11
* **The Pattern Method:** Prints a grid of corner geometries. This is often the most intuitive for visual inspection, allowing the user to select the corner that is sharpest without gaps.9

The optimal PA value is highly dependent on the Bowden length. A direct drive extruder might use a PA of 0.02, while a long Bowden setup might require 0.4 or higher. This underscores why "copying settings" from the internet is futile; the calibration is specific to the physical fluid dynamics of the individual machine.

## **4\. The Algorithm of Slicing: OrcaSlicer's Evolution**

While firmware manages the *execution* of movement, the slicer manages the *strategy*. OrcaSlicer, a fork of Bambu Studio (itself derived from PrusaSlicer), has risen to prominence in the Klipper community. Its rapid development cycle has introduced sophisticated calibration tools that were previously manual calculations.

### **4.1 The Evolution of Flow Rate Calibration**

Calibrating Flow Rate (extrusion multiplier) is the process of matching the slicer's theoretical volume calculation with the physical reality of the extruded plastic's expansion (die swell).

Legacy: The 2-Pass Method
Older versions of OrcaSlicer utilized a "2-Pass" system.

1. **Pass 1:** Printed chips with flow modifiers ranging from \-10% to \+10%. The user selected the best surface.
2. **Pass 2:** A fine-tuning pass with smaller increments (e.g., \-5% to \+5%) based on the result of Pass 1\.
   * *Calculation:* $New\\\_Ratio \= Old\\\_Ratio \\times \\frac{100 \+ Modifier}{100}$.12

Modern: The YOLO (You Only Look Once) Method
OrcaSlicer v2.3.1+ introduced the "YOLO" method, streamlining this into a single print operation. This method prints a specialized pattern (often Archimedean chords) that highlights extrusion artifacts more clearly than simple rectilinear infill.

* *Efficiency:* This reduction in steps aligns with the industry trend toward efficiency. By reducing the time cost of calibration, users are more likely to calibrate for every filament, leading to higher aggregate print reliability.12

### **4.2 Max Volumetric Speed (MVS): The Thermal Ceiling**

A critical, yet often ignored, parameter is the Max Volumetric Speed (MVS), measured in $mm^3/s$. This represents the maximum amount of plastic the hotend can melt per second before the extruder gears skip or grind.

OrcaSlicer includes a procedural test for this:

1. It prints a single-walled object, steadily increasing the print speed (and thus flow rate) as Z height increases.
2. The user observes the print to find the height where the finish changes from glossy to matte (indicating a drop in melt temperature) or where gaps appear (indicating extruder skipping).
3. This height correlates to a specific volumetric flow value.

By setting this limit in the slicer, the user can essentially "uncap" the print speed settings. The slicer will automatically throttle the speed only when the geometry requires a flow rate that exceeds the MVS. This allows for optimizing print times without risking under-extrusion failures.14

### **4.3 Structural Optimization: Infill and Line Width**

The "Minimal 3DP" research highlights that strength is often better achieved through slicer settings than material choice alone.

Line Width Modulation:
Increasing line width (e.g., 0.6mm width on a 0.4mm nozzle) improves layer adhesion significantly. The wider line creates a larger contact area between layers and forces molten plastic into the micro-voids of the layer below. However, this reduces dimensional accuracy on external features.

* *Strategy:* Use wider lines (120-150%) for infill and inner walls to build strength, while maintaining standard width (100%) for outer walls to preserve detail.15

Adaptive Cubic Infill:
This pattern is computationally generated to be dense near the walls and top/bottom surfaces, but sparse in the center of the volume.

* *Performance:* Tests indicate this can reduce print time by over 30% compared to standard Grid or Gyroid infill, while maintaining comparable structural rigidity for functional parts.17

## **5\. The Rise of Visual AI: Defect Detection and Process Control**

As firmware and slicers optimize the deterministic path, Artificial Intelligence is being deployed to handle the probabilistic failures—the random events that math cannot predict. Visual defect detection has evolved from simple "spaghetti detection" to complex quality assurance.

### **5.1 The Spaghetti Problem and Early Solutions**

"Spaghetti" refers to the chaotic nest of filament produced when a print detaches from the bed or a layer fails to adhere. The extruder continues to push plastic into thin air.

Obico (formerly The Spaghetti Detective)
Obico pioneered the use of computer vision for this specific failure mode. It operates by analyzing time-lapse frames from a webcam.

* *Architecture:* It can run in the cloud (SaaS) or be self-hosted on a local server (e.g., a Raspberry Pi).
* *Scale:* Obico's model has been trained on over 7 million hours of print footage, creating a massive dataset of failure modes.18
* *Limitations:* Cloud-based analysis introduces latency. If the internet connection drops, the "watchdog" is blinded. Local hosting requires significant compute (Raspberry Pi 4 or better) to achieve reasonable frame rates.18

### **5.2 Edge Computing and Optimized Models: PrintGuard**

The reliance on cloud compute or heavy local hardware spurred the development of lightweight models. **PrintGuard**, an open-source initiative, utilizes a modified **ShuffleNetv2** architecture.

* *Performance:* Unlike Obico's heavier models, ShuffleNetv2 is optimized for mobile/edge devices. It can achieve \>15 FPS on a Raspberry Pi Zero 2 (a low-power $15 computer), whereas Obico might struggle to hit 1 FPS on the same hardware.19
* *Significance:* High FPS allows for faster reaction times. A print can fail in seconds; waiting 30 seconds for a cloud API response might mean the difference between a salvagable part and a destroyed hotend.

### **5.3 Proprietary Integration: Bambu Lab's Closed Loop**

Bambu Lab represents the vertical integration of this technology. The X1 Carbon printer includes a built-in NPU (Neural Processing Unit) capable of running inference locally.

* *Multimodal Sensors:* It combines visual data (camera) with LiDAR. The LiDAR scans the first layer to verify line width and consistency, creating a "ground truth" that purely visual systems lack.
* *Error Codes:* The system generates specific HMS (Health Management System) codes. For example, code 0C00\_0300\_0003\_0008 indicates a suspected spaghetti failure with low confidence. The system can be configured to pause or simply alert based on sensitivity settings (Low/Medium/High).20
* *Challenges:* Despite the hardware, false positives remain an issue, particularly with dark or shiny filaments (like black TPU or Silk PLA) which confuse the computer vision models due to poor contrast or specular reflections.21 Additionally, edge cases like "spaghetti on the prime tower" (where the waste tower fails but the model is fine) can trigger false stops, frustrating users.22

### **5.4 Comparative Landscape of AI Monitoring Tools**

| Tool | Architecture | Hardware Req. | Primary Detection | Key Feature |
| :---- | :---- | :---- | :---- | :---- |
| **Obico** | Cloud / Local Container | Pi 3B+ / Pi 4 | Spaghetti | Massive training dataset (7M+ hours) |
| **PrintGuard** | Local (ShuffleNetv2) | Pi Zero 2 | Spaghetti/Defects | High FPS on low-end hardware (\>15 FPS) |
| **Bambu AI** | Local NPU \+ LiDAR | X1C/X1E (Embedded) | First Layer \+ Spag. | LiDAR integration for depth validation |
| **PrintWatch** | Cloud API | OctoPrint Host | Anomaly/Trend | Detection of axis wobble/degradation |
| **OctoEverywhere** | Cloud | OctoPrint Host | General Failure | "Gadget" AI is free/unlimited for community |

## **6\. Generative and Semantic AI: The Future of Manufacturing**

Beyond merely "watching" for errors, the next frontier is AI that "understands" the manufacturing process. This involves Multimodal Large Language Models (MLLMs) that can read G-code, interpret 3D geometry, and assist in troubleshooting.

### **6.1 The Slice-100K Dataset: A Foundation for Manufacturing**

To train an AI to understand 3D printing, it needs data that links design (STL) to instruction (G-code) to outcome (Image). **Slice-100K** is a groundbreaking dataset designed to bridge this gap.23

* *Composition:* It contains over 100,000 pairs of STL files and their corresponding G-code, generated using PrusaSlicer. It also includes rendered images and LVIS (Large Vocabulary Instance Segmentation) categories.
* *Limitations:* The dataset currently focuses on Z-axis slicing, which limits its utility for multi-axis (5-axis) printing research.25
* *Utility:* This dataset allows for the training of "Foundation Models" capable of "G-code flavor translation." An LLM could theoretically take G-code meant for an Ender 3 and rewrite it for a Voron 2.4, understanding the kinematic differences not just syntactically, but geometrically.25

### **6.2 ShapeLLM and Scene-LLM: 3D Native Intelligence**

Current LLMs (like GPT-4) process text. To process 3D shapes, we need a way to "tokenize" geometry.

* **ShapeLLM-Omni:** Utilizes a 3D VQVAE (Vector-Quantized Variational Autoencoder) to map 3D objects into discrete tokens. This allows the model to "speak" in 3D shapes. It was trained on the "3D-Alpaca" dataset, which includes instructions for generation, comprehension, and editing.26
* **Scene-LLM:** Focuses on the spatial relationships in 3D environments. While currently targeted at embodied agents (robots navigating a room), the underlying logic applies to 3D printing: understanding that "Structure A" must support "Structure B" is the fundamental logic of generating support material.27

### **6.3 Semantic Routing and RAG in Technical Support**

For the end-user, the immediate application of these advanced models is in technical support via Retrieval Augmented Generation (RAG).

* **The Problem:** LLMs are slow and expensive. Using GPT-4 to answer a simple question like "How do I load filament?" is inefficient.
* **The Solution (Semantic Router):** A Semantic Router uses vector embeddings to classify a user's query *before* sending it to an LLM.
  * *Mechanism:* The router compares the user's question vector against a list of predefined "routes" (e.g., "Calibration Help," "Defect Analysis," "General Chat").
  * *Efficiency:* If the user asks "Why is my extruder skipping?", the router identifies this as a "Calibration" intent and directs the query to a specific tool or database (like the Minimal 3DP guides) instantly, without the latency of a full LLM reasoning step.28
  * *Implementation:* Libraries like semantic-router in Python allow developers to define these decision layers easily, enabling the creation of responsive, domain-specific AI assistants for 3D printing.30

## **7\. Operational Architectures: Managing the Fleet**

The convergence of these technologies—firmware, slicers, and AI—requires a robust operational architecture. The "Minimal 3DP" ecosystem provides a template for managing this complexity.

### **7.1 Configuration Management and Backups**

Klipper's power lies in its printer.cfg file. This text file contains the entire DNA of the machine—pin mappings, rotation distances, macros, and PID values. Losing this file is catastrophic.

* **Git Integration:** The community standard is to treat printer.cfg as source code. The **Klipper-Backup** script automates the process of committing changes to a GitHub repository. This provides version control, allowing users to "roll back" to a previous configuration if a new tuning tweak causes issues.31
* *Macro Logic:* Advanced users utilize Klipper's macro facility to abstract complex G-code sequences (e.g., START\_PRINT, END\_PRINT) into reliable, reusable functions. This modularity is essential for stability.

### **7.2 The Human Element: Community Resources**

The complexity of this stack (Linux, Python, Kinematics, Fluid Dynamics) creates a high barrier to entry. Resources like the **Minimal 3DP Klipper Calibration Website** serve as a bridge, offering web-based calculators that simplify the math of Pressure Advance and Rotational Distance.2

* *Trend:* We are seeing a shift from "tribal knowledge" (forum posts) to "structured tools" (calculators, automated scripts). This formalization is necessary for the industry to mature beyond the hobbyist phase.

## **8\. Synthesis and Strategic Outlook**

The additive manufacturing landscape is undergoing a fundamental transformation. The era of the "dumb" machine is ending.

The Near Future (1-3 Years):
We will see the widespread adoption of "Parameter-Aware" slicers. Instead of manual calibration prints, printers equipped with LiDAR or high-res cameras will run a self-calibration routine before every print, dynamically adjusting Flow Rate and Pressure Advance based on real-time feedback. The integration of tools like PrintGuard directly into firmware will become standard, moving AI from a third-party plugin to a native safety feature.
The Medium Term (3-5 Years):
The Slice-100K dataset and models like ShapeLLM hint at a future where G-code is generated not by geometric algorithms, but by AI inference. A user might speak to a printer: "Make this part stronger near the bolt holes," and the AI will modify the local infill density and wall count (variable settings) and generate the G-code directly, bypassing the traditional CAD-to-STL-to-Slicer workflow entirely.
Conclusion:
For the current practitioner, the path to quality is clear:

1. **Deterministic Foundation:** Use Klipper and the **Minimal 3DP** guides to mathematically perfect the machine's kinematics.
2. **Algorithmic Strategy:** Master **OrcaSlicer's** calibration tools (MVS, YOLO Flow) to optimize the material process.
3. **Probabilistic Safety:** Deploy edge-based AI (like **PrintGuard** or **Obico**) to catch the inevitable random failures.

This layered approach—Hardware Determinism \+ Software Strategy \+ AI Oversight—represents the state-of-the-art in modern additive manufacturing.

---

## **Appendix: Technical Reference & Implementation Guides**

### **A.1 Klipper Calibration Quick-Reference**

*Based on Minimal 3DP Workflows*

1. **Check Mechanics:** Ensure belts are tight (110Hz for Gates 2GT 6mm typical).
2. **Extruder Rotation Distance:**
   * Heat nozzle.
   * Mark 70mm.
   * Extrude 50mm slow (G1 E50 F60).
   * Calculate: $New \= Old \\times (Actual / Requested)$.
3. **PID Tuning:**
   * PID\_CALIBRATE HEATER=extruder TARGET=210
   * PID\_CALIBRATE HEATER=heater\_bed TARGET=60
4. **Resonance Compensation:**
   * Mount ADXL345.
   * Run SHAPER\_CALIBRATE.
   * Apply recommended shaper (prefer ZV or MZV for quality).
5. **Pressure Advance:**
   * Use OrcaSlicer "Pattern Method".
   * Inspect corners for continuity.

### **A.2 Semantic Router Implementation (Python Snippet)**

For integrating RAG into 3D Printer Management Interfaces 29

Python

from semantic\_router import Route, RouteLayer
from semantic\_router.encoders import OpenAIEncoder

\# define the routes (intents)
calibration \= Route(
    name="calibration",
    utterances=\[
        "how do I calibrate e-steps",
        "fix rotation distance",
        "extruder is skipping steps",
        "flow rate is too high"
    \],
)

troubleshooting \= Route(
    name="troubleshooting",
    utterances=\[
        "why is my print spaghetti",
        "layer shift on y axis",
        "nozzle clogged",
        "print detached from bed"
    \],
)

\# initialize the layer
routes \= \[calibration, troubleshooting\]
encoder \= OpenAIEncoder()
rl \= RouteLayer(encoder=encoder, routes=routes)

\# process a user query
query \= "My prints are coming out with gaps in the walls"
decision \= rl(query)

\# logic to direct user
if decision.name \== "calibration":
    print("Directing to Flow Rate Calibration Tool...")
elif decision.name \== "troubleshooting":
    print("Directing to Defect Analysis Module...")

### **A.3 AI Model Comparison for Edge Devices**

| Model Architecture | Target Device | FPS (Est.) | Use Case |
| :---- | :---- | :---- | :---- |
| **MobileNetV2** | Raspberry Pi 4 | \~5-8 FPS | General Object Detection |
| **YOLOv8n (Nano)** | Jetson Nano / Pi 4 | \~10-12 FPS | High accuracy defect detection |
| **ShuffleNetv2** | Raspberry Pi Zero 2 | \>15 FPS | Real-time "Spaghetti" monitoring (PrintGuard) |
| **Proprietary NPU** | Bambu X1C | Real-time | Integrated Lidar/Vision fusion |

This technical appendix serves as a bridge between the theoretical concepts discussed in the report and the practical implementation required by engineers and developers in the field.

#### **Works cited**

1. Rotation distance \- Klipper documentation, accessed November 21, 2025, [https://www.klipper3d.org/Rotation\_Distance.html](https://www.klipper3d.org/Rotation_Distance.html)
2. Klipper Calibration Website \- Minimal 3DP, accessed November 21, 2025, [https://www.minimal3dp.com/blog/2024/04/10/klipper-calibration-website/](https://www.minimal3dp.com/blog/2024/04/10/klipper-calibration-website/)
3. Minimal 3DP, accessed November 21, 2025, [https://minimal3dp.com/](https://minimal3dp.com/)
4. Rotation distance \- Klipper documentation, accessed November 21, 2025, [https://www.klipper3d.org/Rotation\_Distance.html?h=rotat](https://www.klipper3d.org/Rotation_Distance.html?h=rotat)
5. Klipper Rotation Distance \- All You Need to Know \- Obico, accessed November 21, 2025, [https://www.obico.io/blog/klipper-rotation-distance/](https://www.obico.io/blog/klipper-rotation-distance/)
6. X Y Z Rotation Distance (steps/mm ?) calibration in Klipper. How? \- Reddit, accessed November 21, 2025, [https://www.reddit.com/r/klippers/comments/13sj89b/x\_y\_z\_rotation\_distance\_stepsmm\_calibration\_in/](https://www.reddit.com/r/klippers/comments/13sj89b/x_y_z_rotation_distance_stepsmm_calibration_in/)
7. HOW TO CONVERT INPUT SHAPER CALLIBRATION CSV DATA INTO PHG GRAPH FORMAT \- YouTube, accessed November 21, 2025, [https://www.youtube.com/watch?v=PeaDgWv2yAg](https://www.youtube.com/watch?v=PeaDgWv2yAg)
8. Calibration Guide \- SoftFever/OrcaSlicer Wiki \- GitHub, accessed November 21, 2025, [https://github.com/SoftFever/OrcaSlicer/wiki/Calibration](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration)
9. pressure advance calib · SoftFever/OrcaSlicer Wiki \- GitHub, accessed November 21, 2025, [https://github.com/SoftFever/OrcaSlicer/wiki/pressure-advance-calib](https://github.com/SoftFever/OrcaSlicer/wiki/pressure-advance-calib)
10. Calibration · SoftFever/OrcaSlicer Wiki · GitHub, accessed November 21, 2025, [https://github.com/SoftFever/OrcaSlicer/wiki/Calibration/1505371a7f8d494c7e13f0ba7227040766f0f328](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration/1505371a7f8d494c7e13f0ba7227040766f0f328)
11. Calibration · SoftFever/OrcaSlicer Wiki · GitHub, accessed November 21, 2025, [https://github.com/SoftFever/OrcaSlicer/wiki/Calibration/ffa909ad24360290fc6bb80ab26e691a8b87b4b9](https://github.com/SoftFever/OrcaSlicer/wiki/Calibration/ffa909ad24360290fc6bb80ab26e691a8b87b4b9)
12. flow rate calib · SoftFever/OrcaSlicer Wiki \- GitHub, accessed November 21, 2025, [https://github.com/SoftFever/OrcaSlicer/wiki/flow-rate-calib](https://github.com/SoftFever/OrcaSlicer/wiki/flow-rate-calib)
13. OrcaSlicer 2.3.1 Alpha Just Dropped & How to Use the New Flow Rate Calibration, accessed November 21, 2025, [https://www.minimal3dp.com/blog/2025/08/24/orcaslicer-2.3.1-alpha-just-dropped-how-to-use-the-new-flow-rate-calibration/](https://www.minimal3dp.com/blog/2025/08/24/orcaslicer-2.3.1-alpha-just-dropped-how-to-use-the-new-flow-rate-calibration/)
14. OrcaSlicer Calibration and Max Flowrate \- Minimal 3DP, accessed November 21, 2025, [https://minimal3dp.com/projects/tutorials/orca-slicer/orca-slicer-calibration-max-flowrate/](https://minimal3dp.com/projects/tutorials/orca-slicer/orca-slicer-calibration-max-flowrate/)
15. Dimensional Accuracy in 3D Printing: A Deep Dive into Orca Slicer Line Width \- YouTube, accessed November 21, 2025, [https://www.youtube.com/watch?v=vchXVtCReSo](https://www.youtube.com/watch?v=vchXVtCReSo)
16. Orca Slicer Settings EXPLAINED: The SECRET to Stronger Prints via Line Width \- YouTube, accessed November 21, 2025, [https://www.youtube.com/watch?v=n0jb12SLRrU](https://www.youtube.com/watch?v=n0jb12SLRrU)
17. Optimize Your 3D Prints (Orca Slicer and 3D Printer Guide) \- YouTube, accessed November 21, 2025, [https://www.youtube.com/watch?v=JiBZfjWyBxs](https://www.youtube.com/watch?v=JiBZfjWyBxs)
18. 3D Printer Failure Detection \- All You Need to Know \- Obico, accessed November 21, 2025, [https://www.obico.io/blog/3d-printer-failure-detection/](https://www.obico.io/blog/3d-printer-failure-detection/)
19. Introducing PrintGuard \- A new open-source 3D print failure detector running 40x faster than Spaghetti Detective whilst requiring less than 1Gb of RAM for edge deployability : r/3Dprinting \- Reddit, accessed November 21, 2025, [https://www.reddit.com/r/3Dprinting/comments/1lw7it7/introducing\_printguard\_a\_new\_opensource\_3d\_print/](https://www.reddit.com/r/3Dprinting/comments/1lw7it7/introducing_printguard_a_new_opensource_3d_print/)
20. HMS\_0C00-0300-0003-0008: Possible spaghetti defects were detected. Please check the print quality and decide if the job should be stopped. | Bambu Lab Wiki, accessed November 21, 2025, [https://wiki.bambulab.com/en/h2/troubleshooting/hmscode/0C00\_0300\_0003\_0008](https://wiki.bambulab.com/en/h2/troubleshooting/hmscode/0C00_0300_0003_0008)
21. Experiences with AI Spaghetti detection \- Bambu Lab Community Forum, accessed November 21, 2025, [https://forum.bambulab.com/t/experiences-with-ai-spaghetti-detection/172582](https://forum.bambulab.com/t/experiences-with-ai-spaghetti-detection/172582)
22. Spaghetti on prime tower \- Troubleshooting \- Bambu Lab Community Forum, accessed November 21, 2025, [https://forum.bambulab.com/t/spaghetti-on-prime-tower/189590](https://forum.bambulab.com/t/spaghetti-on-prime-tower/189590)
23. 1 The Slice-100K dataset consists of STL files and their G-code counterparts. Each pair here consists of STL (left) and its slices (right) for G-code. \- arXiv, accessed November 21, 2025, [https://arxiv.org/html/2407.04180v1](https://arxiv.org/html/2407.04180v1)
24. \[2407.04180\] Slice-100K: A Multimodal Dataset for Extrusion-based 3D Printing \- arXiv, accessed November 21, 2025, [https://arxiv.org/abs/2407.04180](https://arxiv.org/abs/2407.04180)
25. Slice-100K: A Multimodal Dataset for Extrusion-based 3D Printing \- arXiv, accessed November 21, 2025, [https://arxiv.org/html/2407.04180](https://arxiv.org/html/2407.04180)
26. ShapeLLM-Omni: A Native Multimodal LLM for 3D Generation and Understanding \- arXiv, accessed November 21, 2025, [https://arxiv.org/abs/2506.01853](https://arxiv.org/abs/2506.01853)
27. \[2403.11401\] Scene-LLM: Extending Language Model for 3D Visual Understanding and Reasoning \- arXiv, accessed November 21, 2025, [https://arxiv.org/abs/2403.11401](https://arxiv.org/abs/2403.11401)
28. aurelio-labs/semantic-router: Superfast AI decision making and intelligent processing of multi-modal data. \- GitHub, accessed November 21, 2025, [https://github.com/aurelio-labs/semantic-router](https://github.com/aurelio-labs/semantic-router)
29. Routing in RAG Driven Applications \- Towards Data Science, accessed November 21, 2025, [https://towardsdatascience.com/routing-in-rag-driven-applications-a685460a7220/](https://towardsdatascience.com/routing-in-rag-driven-applications-a685460a7220/)
30. NEW AI Framework \- Steerable Chatbots with Semantic Router \- YouTube, accessed November 21, 2025, [https://www.youtube.com/watch?v=ro312jDqAh0](https://www.youtube.com/watch?v=ro312jDqAh0)
31. Staubgeborener/Klipper-Backup: Klipper-Backup is a script for manual or automated Klipper GitHub backups. It's lightweight, pragmatic and comfortable., accessed November 21, 2025, [https://github.com/Staubgeborener/Klipper-Backup](https://github.com/Staubgeborener/Klipper-Backup)
32. Klipper Calibration | Minimal 3DP, accessed November 21, 2025, [https://minimal3dp.com/klipper-calibration/](https://minimal3dp.com/klipper-calibration/)
