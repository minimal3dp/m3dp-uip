# micromachines-11-00633-v2

> **Source:** `micromachines-11-00633-v2.pdf`
> **Converted:** 2025-11-22 21:18:11
> **Method:** PyMuPDF

---

## Page 1


micromachines
Review
Path Planning Strategies to Optimize Accuracy,
Quality, Build Time and Material Use in Additive
Manufacturing: A Review
Jingchao Jiang 1,2
and Yongsheng Ma 3,*
1
Department of Mechanical Engineering, University of Auckland, Auckland 1142, New Zealand;
jjia547@aucklanduni.ac.nz
2
Digital Manufacturing and Design Center, Singapore University of Technology and Design,
Singapore 486842, Singapore
3
Department of Mechanical Engineering, University of Alberta, Edmonton, AB T6G 2V4, Canada
*
Correspondence: yongsheng.ma@ualberta.ca
Received: 18 June 2020; Accepted: 26 June 2020; Published: 28 June 2020


Abstract: Additive manufacturing (AM) is the process of joining materials layer by layer to fabricate
products based on 3D models. Due to the layer-by-layer nature of AM, parts with complex geometries,
integrated assemblies, customized geometry or multifunctional designs can now be manufactured
more easily than traditional subtractive manufacturing. Path planning in AM is an important step in the
process of manufacturing products. The final fabricated qualities, properties, etc., will be different when
using different path strategies, even using the same AM machine and process parameters. Currently,
increasing research studies have been published on path planning strategies with different aims. Due to
the rapid development of path planning in AM and various newly proposed strategies, there is a lack of
comprehensive reviews on this topic. Therefore, this paper gives a comprehensive understanding of the
current status and challenges of AM path planning. This paper reviews and discusses path planning
strategies in three categories: improving printed qualities, saving materials/time and achieving
objective printed properties. The main findings of this review include: new path planning strategies
can be developed by combining some of the strategies in literature with better performance; a path
planning platform can be developed to help select the most suitable path planning strategy with
required properties; research on path planning considering energy consumption can be carried out
in the future; a benchmark model for testing the performance of path planning strategies can be
designed; the trade-off among different fabricated properties can be considered as a factor in future
path planning design processes; and lastly, machine learning can be a powerful tool to further improve
path planning strategies in the future.
Keywords: additive manufacturing; path planning; review
1. Introduction
Additive manufacturing (AM) technologies (also known as rapid prototyping, 3D printing, solid
freeform fabrication, etc.) have been developed for more than 30 years [1–6]. As AM has matured, it has
been applied in many ﬁelds, including aerospace, medical, construction and aesthetic products [7–9].
The manufacturing process of AM is diﬀerent from conventional subtractive manufacturing, which uses
a subtractive manner (e.g., tooling and cutting), while AM uses an additive process to fabricate parts
from the bottom to the top in a point-by-point and then layer-by-layer strategy [10–14]. Currently, AM
technology is mainly divided into seven categories: material extrusion, material jetting, powder bed
fusion, binder jetting, vat photopolymerization, directed energy deposition and sheet lamination [15–17].
Among these seven AM techniques, material extrusion, material jetting, powder bed fusion, binder
Micromachines 2020, 11, 633; doi:10.3390/mi11070633
www.mdpi.com/journal/micromachines


---


## Page 2


Micromachines 2020, 11, 633
2 of 18
jetting, vat photopolymerization and directed energy deposition need a deposition path moving along
the 3D model to fabricate the ﬁnal product. The strategy of designing the paths for manufacturing is
called path planning in AM. Path planning is very critical in AM, as diﬀerent path strategies can aﬀect
surface roughness, dimensional accuracy and the properties (e.g., strength) of the printed products.
In addition, diﬀerent paths mean diﬀerent moving strategies of the corresponding print head (e.g., the
nozzle in fused deposition modeling (FDM), the laser in direct energy deposition (DED)), resulting in
diﬀerent durations needed for completing the same part. Therefore, a better path planning strategy can
lead to better fabricated properties, qualities or a lower fabrication time. Currently, there are already a
lot of papers that have been published on this topic. As a rapidly evolving manufacturing technology,
new additive manufacturing technologies are being developed and will most likely continue to be
developed in the future. It is, therefore, perhaps timely that a review of the topic with regard to path
planning is performed, so that newly developed additive manufacturing technologies can exploit the
most apposite strategies with better performance. The aim of this article is to provide a contextual
framework for the range of research that has been carried out in the area of path planning for additive
manufacturing. The article then reviews the diﬀering strategies of path planning, based on diﬀerent
objectives. Finally, it gives an outlook onto potential future research directions.
2. Path Planning Strategies
In this section, the current available path planning strategies are divided into three groups for
illustration (i.e., improve printed qualities, save materials/time and achieve objective printed properties).
“Improve printed qualities” means proposing path planning strategies in AM to improve printed surface
quality (e.g., surface roughness), shape accuracy and infill distribution quality. “Save materials/time”
means proposing path planning strategies in AM to save the total fabrication time or the material
consumption. “Achieve objective printed properties” means proposing path planning strategies in
AM to achieve better mechanical, topological or functional properties. Before going into detail, some
commonly used path patterns are introduced first. Figure 1 shows the corresponding basic path patterns
are currently being widely used. Most of the improved path planning strategies are based on these
basic path patterns. These patterns are widely used in AM to fill the layers of sliced 3D models. These
patterns can be selected easily in commonly used slicing software, such as Cura and Slic3r.
Figure 1. (a) Raster path; (b) grid path; (c) zigzag path; (d) contour oﬀset path; (e) spiral path.
2.1. Improve Printed Qualities
In this sub-section, path planning for improving printed qualities is illustrated (including printed
surface quality, shape accuracy and infill distribution quality). Due to the point-by-point, line-by-line
and layer-by-layer nature of AM, the qualities of printed parts generally deteriorate as there are gaps
between the printed lines. This leads to different surface qualities, shape accuracies and infill distribution
qualities in different path strategies. Figure 2 illustrates this phenomenon using two different path


---


## Page 3


Micromachines 2020, 11, 633
3 of 18
planning strategies. A 3D model can be manufactured in many different path strategies, Figure 2 only
shows two examples. As can be seen, the surface qualities on Surface 1 in Figure 2 are probably different
in these two different path planning strategies, as well as shape accuracies and infill distribution qualities.
Figure 2. Illustration of path strategies inﬂuencing surface quality.
Surface quality: Jin et al. [18,19] proposed to use closed non-uniform rational B-spline (NURBS)
curves to represent the contours of layers to maintain the surface accuracy of the 3D part model. Then a
mixed and adaptive path generation algorithm was developed to optimize the surface quality. This
algorithm could generate contour paths for AM fabrication to reduce the surface errors of 3D models.
Figure 3 shows an example of generated contour paths by using their method. A curved layer path
planning method for traditional FDM processes was introduced by Jin et al. [20]. This method moved
the path along a curved layer to improve the printed surface qualities. Similarly, Ezair et al. [21] also
proposed a curved layer path planning strategy that could improve the surface quality, using volumetric
covering print paths for material extrusion AM. Jensen et al. [22] proposed two path planning methods
(path projection and parent–child approach) for five degrees of freedom (5DOF) and 6DOF material
extrusion AM, respectively. Their strategy could remedy the staircase effect (shape deviations), thus
achieving better surface quality.
Figure 3. Example of a generated contour reproduced with permission from [18]. Elsevier, 2011.
Shape accuracy: Routhu et al. [23] improved the zigzag and oﬀset pattern based on the laser
scanning speed to reduce the printed height variation in the laser powder-based metal deposition
process, achieving better shape accuracy. A three-step path planning strategy was developed by
Jin et al. [24] to achieve precision manufacturing in FDM. Communal et al. [25] proposed a path
planning strategy considering the shape accuracy of the corners in each layer in material extrusion AM.
Figure 4 shows their successful fabrication of corners with good quality. Liu et al. [26] developed a
composite path planning method with a sharp corner correction strategy to improve the shape accuracy
of parts fabricated in wire and arc AM. Giberti et al. [27] proposed a path planning algorithm based on
the use of Bézier curves aimed at assuring the regulation of the velocity and a uniform distribution of


---


## Page 4


Micromachines 2020, 11, 633
4 of 18
the extruded material in binder jetting AM, thus improving fabricated shape accuracy. Ding et al. [28]
introduced an automatic path planning method for wire and arc AM, which can achieve good shape
accuracy of fabricated parts.
Figure 4. Successful fabrication of 90◦and 30◦corners reproduced with permission from [25]. Elsevier, 2019.
Inﬁll distribution quality: A contemporary path planning strategy was proposed by Eiliat and
Urbanic [29–31], to ﬁnd optimal paths for achieving better inﬁll quality without voids. Xiong et al. [32]
developed a variable bead width path planning method to manufacture void-free parts in a wire and
arc AM process. In their strategy, the path planning process considers the possibility of changing
bead width when fabricating. In the traditional constant oﬀset path method, voids are left in the
middle of each layer, while by using their proposed adaptive oﬀset path, the manufactured parts can
achieve better inﬁll distribution without voids. Kumar and Maji [33] also proposed a path planning
method to optimize the path width and overlapping between two beads to achieve void-free parts in
wire and arc AM. However, they did not consider the changeable bead widths in each path planning.
Wang et al. [34] proposed a cylindrical path planning strategy to fabricate cylindrical parts (such as the
blades of a propeller), without voids inside, using wire and arc AM. A sequential path planning strategy
for wire and arc AM was proposed by Wang et al. [35], based on a water-pouring rule. Their proposed
solution can transfer all the intersection areas of the path to the outer contour, ensuring that the inner
area is uniform and compact. Michel et al. [36] introduced a modular path planning (MPP) strategy
that incorporates the modularity of feature-based design into the conventional layer-by-layer method.
Their strategy can ensure a uniform defect-free deposition in wire and arc AM processes. A medial
axis transformation (MAT)-based path planning strategy was developed by Ding et al. [37–39], to
allow the wire and arc AM to deposit material along multiple directions. Their MAT-based paths can
guarantee the void-free deposition of layers. They further developed a new path planning strategy
speciﬁcally for thin-walled parts without voids inside [40]. Ren et al. [41] proposed a path planning
strategy of combining a contour-parallel pattern and adaptive zigzag path pattern to achieve void-free


---


## Page 5


Micromachines 2020, 11, 633
5 of 18
part fabrication in metal deposition AM. Han et al. [42] used a grouping and mapping algorithm
to generate paths for fabricating parts without voids inside in FDM processes. Their path planning
strategy was based on normal zigzag and contour paths with a better calculated distance between each
path line, resulting in void-free inﬁll. Jin et al. [43,44] developed an FDM path generation method that
chooses a better inclination of paths to reduce the number of sharp corners in layers, so this method
can adaptively generate paths for fabrication with better inﬁll quality.
2.2. Save Materials/Time
In this sub-section, path planning for saving materials or fabrication time is presented.
Save materials: Jensen et al. [22] proposed two path planning methods (path projection and
parent–child approach) for five degrees of freedom (5DOF) and 6DOF material extrusion AM, respectively.
Their strategy can achieve successful fabrication without support structures, thus saving support material
consumption. Figure 5 shows the example 5DOF machine and the product fabricated using their path
planning method. Zhao et al. [45] introduced a nonplanar path planning strategy that can reduce
the usage of support material in robot-based material extrusion AM. Tarabanis [46] developed a path
planning strategy, based on shelving and bridging features, that allows parts to be able to be printed “in
the air” in FDM, thus reducing support structure usage. We also previously proposed path planning
strategies with the aim of reducing support material consumption in FDM [47–50]. Nguyen et al. [51]
proposed a heuristic path planning strategy for wire and arc AM that can achieve support-free fabrication,
thus reducing material waste. The path planning method, based on medial axis transformation (MAT)
and developed by Ding et al. [37,38], can also save material usage in wire and arc AM. Thompson
and Yoon [52] developed a path planning algorithm to control the motion of an XY stage in aerosol
printing (material jetting) for an arbitrary printing path and desired velocity while minimizing material
waste. A path planning strategy for an eight-axis direct energy deposition system was proposed by
Ding et al. [53] to fabricate complex revolved parts without support consumption. Zhang and Liou [54]
developed an automated path planning strategy for five-axis laser aided AM that can reduce the usage
of support structures.
Figure 5. 5DOF AM machine (left) and the product fabricated without any support (right) [22].
Save time: Bui et al. [55] proposed a path planning strategy for multi-head material extrusion
AM, where multiple printheads can work together without collision, thus reducing fabrication time.
Their strategy is based on multiple heads printing the same material. Choi and Zhu [56] proposed a
dynamic priority-based path planning strategy for multi-material extrusion AM with multiple nozzles.
Their strategy can generate optimized paths for different nozzles (with different materials) and avoid
collisions between nozzles, thus saving total fabrication time. A combined heuristic path planning
method was proposed by Volpato et al. [57] to reduce the total moving length of the extruder nozzle in
material extrusion AM, thus saving fabrication time. Ganganath et al. [58] introduced a path planning
method using triangular and trapezoidal velocity profiles for material extrusion AM. Their method
can generate optimal paths to minimize the transition time between print segments. Fleming et al. [59]


---


## Page 6


Micromachines 2020, 11, 633
6 of 18
proposed a continuous path planning strategy that can reduce the distance traveled between subsequent
space-filling curves and layers, which reduces unnecessary nozzle movement by around 20%. The closed
non-uniform rational B-spline (NURBS) path planning method from [18,19] can also minimize the build
time through their developed analysis mathematical models. Fok et al. [60] developed a path planning
strategy based on the Christofides algorithm that can significantly reduce the length of motion paths in
FDM, compared to a nearest neighbor-based strategy. Jin et al. [61] developed a non-retraction path
planning strategy that can avoid retraction during the printing process in FDM, and hence the time
spent moving along these retracting paths can be saved. Papacharalampopoulos et al. [62] proposed a
path planning strategy that ensures a single continuous motion of the printhead to finish a printing in
material extrusion AM. They used the Hilbert curves as the path pattern, as shown in Figure 6a. Luo and
Tseng [63] proposed a path planning strategy for multi-part production in FDM. They tried to reduce
the length of paths traveled between parts to reduce the fabrication time. Jiang proposed a multi-layer
by multi-layer path strategy to save the fabrication time [64]. A porous path planning strategy was
introduced by Zhai and Chen [65] for the successful fabrication of porous structures in material extrusion
AM. Figure 6b shows a result of their generated paths also shown in this figure. Their strategy found the
optimal workable paths that could save time for printing porous structures. Dreifus et al. [66] proposed
a path planning strategy, based on the Chinese postman problem, specifically for fabricating lattice
structures that can minimize total manufacturing time in material extrusion AM. Coupek et al. [67]
proposed a path planning method for seven-axis material extrusion AM which can avoid the usage of
supports, thus saving materials and fabrication time as well. Figure 6c shows a successful fabrication
using their strategy in their seven-axis FDM machine. An efficient path planning strategy was developed
by McQueen et al. [68] for material extrusion AM with two robotic arms. The allowed two robotic
arms working together could save fabrication time. Shembekar et al. [69] proposed a collision-free
path planning strategy for a 6DOF material extrusion AM system, which could save both material
usage and build time. A group-based path planning strategy for a multi-robotic material extrusion AM
system was developed by Cai and Choi [70]. Their strategy could ensure collision-free printing between
printheads, thus saving total fabrication time when all the robotic heads work together. For wire and arc
AM, Fügenschuh et al. [71] proposed a path planning method on how to partition a given traverse into
continuous segments that are printed without intersection and deadheading between two segments, so
that deadheading is minimized to complete the fabrication as fast as possible.
Figure 6. (a) Hilbert curves path pattern reproduced with permission from [62]. Elsevier, 2018; (b) an
example of generated paths for porous structures reproduced with permission from [65]. Elsevier, 2019;
(c) a successful fabrication by using the path planning strategy reproduced with permission from [67].
Elsevier, 2018.


---


## Page 7


Micromachines 2020, 11, 633
7 of 18
2.3. Achieve Objective Printed Properties
In this sub-section, path planning for achieving objective printed properties is presented (including
mechanical, topological, functional, etc.).
Li et al. [72] developed an ingenious path planning strategy that can print continuous carbon
ﬁber-reinforced composites with complex shapes and high mechanical performances in material
extrusion AM. Asif [73] also proposed another strategy with the same aim in material extrusion AM.
Kralji´c and Kamnik [74] developed a path planning strategy that can enhance inter-track bonding
and consequently better strength of printed parts in 6DOF material extrusion AM. Liu et al. [75]
proposed a path planning strategy for achieving topologically optimized lightweight part fabrication
in FDM. They also proposed a path planning strategy along the principle stress direction of parts to
enhance the structural performance of FDM-printed parts [76]. Wavy path planning was developed
by Jin et al. [77] to improve the structural strength of printed parts in FDM. Lin et al. [78] proposed
a maze-like path planning strategy that could fabricate isotropic components in FDM. Jin et al. [79]
developed a path planning strategy for the successful fabrication of thin-walled parts with good
qualities in FDM. Ma et al. [80] also proposed an adaptive path planning method with varying
thickness to successfully fabricate thin-walled parts, but using wire and arc AM. Eliseeva et al. [81]
developed a path planning strategy for the successful fabrication of functionally graded compositions
in multi-material direct energy deposition systems. Deuser et al. [82] also proposed a path planning
method that can successfully print functionally graded compositions, but in material extrusion AM
systems with three printheads. Ozbolat and Khoda [83] proposed a simulation-based path planning
strategy to determine the sequence of material deposition in AM, achieving the successful fabrication
of hollow porous structures with functionally graded materials. Zhu and Yu [84] developed a path
planning strategy, based on a dexel-based spatio-temporal modeling approach that can guarantee the
collision-free movement of printheads, achieving multi-material printing simultaneously in FDM with
multiple printheads. We previously proposed a support interface path planning strategy for easy part
removal after fabrication in direct energy deposition processes [85].
3. Discussion
Table 1 lists the available path planning strategies in literature based on diﬀerent objectives. In the
future, the corresponding path planning strategy can be selected according to the requirements of
the products. For example, when a product with great mechanical strength is required, then the ﬁve
available choices can be the candidates. Further, the 6DOF or normal material extrusion AM machines
can be selected upon the availability of AM machines. Another example is that if the surface quality
is a priority, then the six strategies listed in “improve surface quality” in Table 1 can be considered.
However, it is hard to say which strategy is better than another among these six strategies, as the
diﬀerent strategies used diﬀerent parts, standards or criteria.
Another thing that needs to be known is that other properties or qualities may deteriorate when
adopting an improved path planning strategy for a speciﬁc aim. For instance, when trying to improve
the strength of printed parts by using a diﬀerent path pattern, the dimensional variation and/or building
time of parts may probably also be changed. The trade-oﬀamong these should be considered.


---


## Page 8


Micromachines 2020, 11, 633
8 of 18
Table 1. Path planning strategies in literature.
Objective
Path Planning Strategy
Suitable AM Technique
Improve surface quality
NURBS-based strategy [18,19]
Material extrusion
Curved layer strategy [20]
FDM (material extrusion)
Curved layer strategy [21]
Material extrusion
Path projection strategy [22]
5DOF material extrusion
Parent–child approach strategy [22]
6DOF material extrusion
Improve shape accuracy
Improved zigzag/oﬀset strategy [23]
Laser powder-based metal deposition process (directed energy deposition)
Combination of zigzag and contour pattern strategy [28]
Wire and arc AM (directed energy deposition)
Three-step strategy [24]
FDM (material extrusion)
Improve shape accuracy for corners
Corner strategy [25]
Material extrusion
Composite strategy [26]
Wire and arc AM (directed energy deposition)
Improve shape accuracy under velocity constraints
Bézier curve strategy [27]
Binder jetting
Improve inﬁll distribution quality
Contemporary strategy [29–31]
Material extrusion
Variable width strategy [32], optimized width and overlapping strategy [33],
water-pouring strategy [35], modular strategy [36], MAT strategy [37–39]
Wire and arc AM (directed energy deposition)
Cylindrical strategy speciﬁcally for cylindrical parts [34]
MAT strategy speciﬁcally for thin-walled structures [40]
Grouping and mapping strategy [42], sharp corner strategy [43,44]
FDM (material extrusion)
Adaptive contour/zigzag strategy [41]
Metal-directed energy deposition
Save time
Dynamic priority-based strategy [56]
Multi-material extrusion with multiple nozzles (material extrusion)
Multi-head strategy [55]
Multi-head material extrusion
Two-robot strategy [68]
Material extrusion with two robotic arms
Combined heuristic strategy [57], salesman strategy [58], continuous strategy [59],
NURBS-based strategy [18,19], Christoﬁdes strategy [60], Hilbert curve
strategy [62], non-retraction strategy [61]
Material extrusion
Porous strategy speciﬁcally for porous structures [65]
Material extrusion
Lattice strategy speciﬁcally for lattice structures [66]
Material extrusion
Multi-part strategy speciﬁcally for multi-part production [63]
FDM (material extrusion)
Partition strategy [71]
Wire and arc AM (directed energy deposition)
Collision-free strategy [69]
6DOF material extrusion
Coupek strategy [67]
7DOF material extrusion
Group-based strategy [70]
Multi-robot material extrusion


---


## Page 9


Micromachines 2020, 11, 633
9 of 18
Table 1. Cont.
Objective
Path Planning Strategy
Suitable AM Technique
Save material
Heuristic strategy [51], MAT strategy [37,38]
Wire and arc AM (directed energy deposition)
Aerosol strategy [52]
Material jetting
Nonplanar strategy [45]
5DOF material extrusion
Support optimization strategy [47–49], shelving- and bridging-based strategy [46]
FDM (material extrusion)
Path projection strategy [22]
5DOF material extrusion
Five-axis adaptive slicing strategy [54]
5DOF directed energy deposition
Parent–child approach strategy [22], Collision-free strategy [69]
6DOF material extrusion
Revolved strategy [53]
8DOF directed energy deposition
Improve mechanical properties
Ingenious strategy for ﬁber-reinforced fabrication [72], Asif strategy for
ﬁberreinforced fabrication [73], stress direction strategy [76]
Material extrusion
Kralji´c strategy [74]
6DOF material extrusion
Wavy strategy [77]
FDM (material extrusion)
Fabricate thin-walled parts
Varying thickness strategy [80]
Wire and arc AM (directed energy deposition)
Wavy strategy [79]
FDM (material extrusion)
Fabricate functionally graded compositions
Functional strategy [81]
Directed energy deposition
Simulation-based strategy [83]
AM
Spatio-temporal strategy [84]
FDM with multiple nozzles (material extrusion)
Deuser strategy [82]
Material extrusion with three nozzles
Fabricate lightweight parts
Topology strategy [75]
FDM (material extrusion)
Fabricate isotropic parts
Maze-like strategy [78]
FDM (material extrusion)
Easy part removal after fabrication
Support interface strategy [85]
Directed energy deposition


---


## Page 10


Micromachines 2020, 11, 633
10 of 18
Looking at the number of publications on path planning in the seven AM categories (as shown
in Figure 7), material extrusion AM and directed energy deposition attracted most of the attention
from researchers. Only one publication is seen on optimizing paths for material jetting AM and one for
binder jetting AM. There are no published papers on path planning in the other two categories. When
looking deeper into material extrusion and directed energy deposition, as shown in Figure 8, most
publications (28 papers) focused on FDM in material extrusion while most publications (12 papers)
focused on wire and arc AM in directed energy deposition. One of the reasons for this is that material
extrusion (especially FDM) and directed energy deposition are the two most commonly used and have
been applied in many fields in our daily lives. In addition, FDM is the simplest and most economical
AM technique which mainly uses polymers as raw material with low costs. The principles and findings
of path planning research on FDM, to some extent, can be extended to be used in other AM techniques,
such as directed energy deposition, which always costs a lot. As directed energy deposition has its
specific advantages, especially its ability to manufacture metal lightweight parts, it has been increasingly
applied in aeronautic and astronomic fields. Therefore, increasing attention is also paid to directed
energy deposition. As can be seen from Figure 8, there are also some publications on multi-DOF AM
systems. This is mainly due to the fact that traditional three-DOF AM has some limitations (such
as the staircase effect on surface finishes, anisotropy of parts, limited mechanical strength and the
requirement of support structures). Multi-DOF AM systems are currently being investigated to overcome
these disadvantages.
Figure 7. Number of publications on path planning in the seven AM categories.
Figure 8. Distribution of published papers in material extrusion (a) and directed energy deposition (b).


---


## Page 11


Micromachines 2020, 11, 633
11 of 18
Looking into the objectives of path planning (Figure 9), researchers were concerned mostly about
saving time (18 papers), saving material (14 papers) and improving inﬁll distribution quality (16
papers). This indicates that path planning has a great contribution to the corresponding time spent on
fabrication, material consumption and inﬁll quality. Path planning is important in ensuring AM parts
meet the required qualities. There are also some papers focusing on achieving speciﬁc properties (e.g.,
functionally graded compositions). This means path planning can help to broaden the application of
AM in more ﬁelds in the future. When considering improving the performance of printed parts in
diﬀerent applications using AM, developing novel path planning strategies may be helpful.
Figure 9. Number of publications with diﬀerent objectives.
4. Future Perspectives
(1) As discussed above, path planning strategies on saving materials or fabrication time have been
explored a lot. However, few studies can be seen considering the energy consumption in diﬀerent
path planning strategies. As the world is becoming more sustainable and the focus on sustainable
manufacturing increases signiﬁcantly, AM can become more sustainable and environmentally friendly
in the future through path planning. Research on proposing novel path planning strategies that can
save more energy can be a meaningful research topic in the future.
(2) Develop new AM systems based on the knowledge of the abovementioned path planning
strategies. The current available path planning strategies have been summarized in Table 1, which
can help engineers to choose how to combine their strategies for new AM system development.
For example, if developing an AM system consisting of 10 robots working together to print a house, the
path planning process for this new system can borrow ideas from the path planning strategy for AM
with two robotic arms [68]. Another example is for developing a new AM system with three printheads,
then combining the proposed methods of “multi-head strategy” [55] and “wavy strategy” (improved
mechanical properties of printed parts) [77] can obtain a better AM system with better performance of
fabricated parts.
(3) A comprehensive path planning strategy that can deal with all the aims (quality, function,
time/material minimization, etc.) or some of the aims might be able to be developed in the future,
based on the current available knowledge listed in Table 1. For example, considering both the surface
roughness and mechanical strength as the objective, then it is possible to combine two path planning
strategies (one from improving surface roughness and one from improving mechanical properties)
together and revise them into a new path planning strategy to achieve the corresponding aims. In
addition, while current path planning strategies are generally only suitable for a speciﬁc AM technique,


---


## Page 12


Micromachines 2020, 11, 633
12 of 18
a path planning strategy that can be used in many AM techniques rather than just one (such as only
FDM) might be able to be developed in the future.
(4) A path planning platform can be developed in the future. This platform can automatically
help to choose the best path planning strategy based on the required input properties. This platform
should know all the advantages and disadvantages of each path planning strategy and which path
planning strategy for which AM technique. Then, when inputting the objectives (e.g., saving time),
the corresponding available strategies and recommended best strategy will pop up, with advantages
and disadvantages.
(5) As discussed previously, other properties or qualities may deteriorate when adopting an
improved path planning strategy for a speciﬁc aim. For instance, when trying to improve the strength
of printed parts by using a diﬀerent path pattern, the dimensional variation and/or building time of
parts may also probably be changed. The trade-oﬀamong these can be investigated in the future.
The trade-oﬀdepends on the speciﬁc requirements from the customers. For example, if the customer
would like to have his/her product as soon as possible with a mechanical strength requirement, then
the fabrication time is a priority, while the mechanical strength only needs to be at the qualiﬁed level.
Based on this, a better path planning strategy can be selected or proposed.
(6) Currently, it is not possible to distinguish which path planning strategy is better than another,
as these strategies use diﬀerent parts/models in the research. A benchmark model with all the necessary
features (sharp corner features, thin-walled features, etc.) can be developed in the future for comparing
diﬀerent path planning strategies. Once this benchmark model is available and all the upcoming
research studies can be carried out based on this benchmark model, then it will be possible to know
which path planning strategy is better than another in terms of some objectives (e.g., surface roughness).
This will help to provide useful information for the future choice of adopting which path planning
strategy. For example, when fabricating thin-walled parts, choose the path planning strategy that is
best for thin-walled features.
(7) As the development of AM systems, new AM techniques are emerging rapidly. The hybrid
AM system including additive and subtractive processes with multi-axis machines is one of these
new developed AM techniques. Research on path planning for these new advanced AM systems is
necessary in the future for its further development.
(8) Machine learning, integrated path planning strategies, can be developed in the future. Machine
learning is one of today’s most rapidly growing technical fields. It is a subset of artificial intelligence,
mainly focusing on using algorithms and statistical models to make decisions without specific
programming. Generally, machine learning can be used in medical diagnosis, image processing,
prediction, classification, etc. Recently, research on using machine learning in AM has also been
published for AM process optimization [86–91], dimensional accuracy analysis [92–95], manufacturing
defect detection [96–98] and material property prediction [99–101]. However, machine learning has
not been applied to improving path planning strategies yet. In fact, machine learning is very powerful
in planning strategies. Liu et al. [102] used machine learning to select the best path for driving cars
with the shortest path length. Figure 10a shows the problem map in their study, the black grids are
the places where there are obstacles. The start point is A, while the destination is point B. In their
study, machine learning solved this problem efficiently. Similarly, in the path planning problems of AM,
machine learning can also be used to obtain the best paths and print sequences. All the print paths in
the AM fabrication process can be divided into points (Figure 10b) and the print order of the points can
be decided through machine learning.


---


## Page 13


Micromachines 2020, 11, 633
13 of 18
Figure 10. (a) Problem map for selecting the best path reproduced with permission from [102]. IEEE,
2019; (b) example of a 3D model divided into points for path selection using machine learning.
5. Conclusions
Path planning is an important step of AM fabrication that can inﬂuence the ﬁnal printed properties,
qualities, etc. Most of the research done in AM focuses on improving AM processes, the development
of new AM techniques, and new applications of AM, based on the commonly used path strategies.
However, there are still many researchers try to improve AM with diﬀerent objectives through
developing new path planning strategies. In this paper, the focus is given to these publications on
path planning. A comprehensive review on path planning strategies is provided according to the
aims of improving printed qualities, saving materials/time and achieving objective printed properties.
A summarized table is provided for selecting suitable path planning strategies in future AM fabrication
with speciﬁc aims. The main ﬁnding of this review is that there is still plenty of research on path
planning that can be carried out in the future. New path planning strategies can be developed by
combining some of these strategies (Table 1) with better performance. A path planning platform can be
developed to help select the most suitable path planning strategy with required properties. Research
on path planning, considering energy consumption, can be carried out in the future. A benchmark
model for testing the performance of path planning strategies can be designed. The trade-oﬀamong
diﬀerent fabricated properties can be considered as a factor in future path planning design processes.
Lastly, machine learning can be a powerful way to further improve path planning strategies.
Author Contributions: Conceptualization, J.J. and Y.M.; Methodology, J.J. and Y.M.; Validation, J.J. and Y.M.;
Formal Analysis, J.J.; Investigation, J.J.; Resources, Y.M.; Data Curation, J.J.; Writing-Original Draft Preparation,
J.J.; Writing-Review & Editing, Y.M.; Visualization, J.J.; Supervision, Y.M.; Project Administration, Y.M.; Funding
Acquisition, Y.M.. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by NSERC of Canada with grant number RGPIN-2020-03956.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Jiang, J.; Lou, J.; Hu, G. Eﬀect of support on printed properties in fused deposition modelling processes.
Virtual Phys. Prototyp. 2019, 14, 308–315. [CrossRef]
2.
Fu, Y.-F.; Rolfe, B.; Chiu, L.N.S.; Wang, Y.; Huang, X.; Ghabraie, K. Parametric studies and manufacturability
experiments on smooth self-supporting topologies. Virtual Phys. Prototyp. 2019, 15, 22–34. [CrossRef]
3.
Jiang, J.; Yu, C.; Xu, X.; Ma, Y.; Liu, J. Achieving better connections between deposited lines in additive
manufacturing via machine learning. Math. Biosci. Eng. 2020, 17, 3382–3394. [CrossRef]


---


## Page 14


Micromachines 2020, 11, 633
14 of 18
4.
Jiang, J.; Stringer, J.; Xu, X.; Zhong, R.Y. Investigation of printable threshold overhang angle in extrusion-based
additive manufacturing for reducing support waste. Int. J. Comput. Integr. Manuf. 2018, 31, 1–9. [CrossRef]
5.
Fu, Y.-F.; Rolfe, B.; Chiu, L.N.S.; Wang, Y.; Huang, X.; Ghabraie, K. Design and experimental validation of
self-supporting topologies for additive manufacturing. Virtual Phys. Prototyp. 2019, 14, 382–394. [CrossRef]
6.
Bikas, H.; Stavropoulos, P.; Chryssolouris, G. Additive manufacturing methods and modelling approaches:
A critical review. Int. J. Adv. Manuf. Technol. 2015, 83, 389–405. [CrossRef]
7.
Haleem, A.; Javaid, M. 3D printed medical parts with diﬀerent materials using additive manufacturing. Clin.
Epidemiol. Glob. Health 2020, 8, 215–223. [CrossRef]
8.
Yusuf, S.M.; Cutler, S.; Gao, N. Review: The Impact of Metal Additive Manufacturing on the Aerospace
Industry. Metals 2019, 9, 1286. [CrossRef]
9.
Galati, M.; Minetola, P.; Marchiandi, G.; Atzeni, E.; Calignano, F.; Salmi, A.; Iuliano, L. A methodology for
evaluating the aesthetic quality of 3D printed parts. Procedia CIRP 2019, 79, 95–100. [CrossRef]
10.
Jiang, J.; Xu, X.; Stringer, J. Optimisation of multi-part production in additive manufacturing for reducing
support waste. Virtual Phys. Prototyp. 2019, 14, 219–228. [CrossRef]
11.
Liu, J.; Gaynor, A.T.; Chen, S.; Kang, Z.; Suresh, K.; Takezawa, A.; Li, L.; Kato, J.; Tang, J.; Wang, C.C.L.; et al.
Current and future trends in topology optimization for additive manufacturing. Struct. Multidiscip. Optim.
2018, 57, 2457–2483. [CrossRef]
12.
Jiang, J.; Xu, X.; Stringer, J. Eﬀect of Extrusion Temperature on Printable Threshold Overhang in Additive
Manufacturing. Procedia CIRP 2019, 81, 1376–1381. [CrossRef]
13.
Jiang, J.; Hu, G.; Li, X.; Xu, X.; Zheng, P.; Stringer, J. Analysis and prediction of printable bridge length in
fused deposition modelling based on back propagation neural network. Virtual Phys. Prototyp. 2019, 14,
253–266. [CrossRef]
14.
Weng, F.; Gao, S.; Jiang, J.; Wang, J.; Guo, P. A novel strategy to fabricate thin 316L stainless steel rods by
continuous directed energy deposition in Z direction. Addit. Manuf. 2019, 27, 474–481. [CrossRef]
15.
Gao, W.; Zhang, Y.; Ramanujan, D.; Ramani, K.; Chen, Y.; Williams, C.B.; Wang, C.C.L.; Shin, Y.C.; Zhang, S.;
Zavattieri, P.D. The status, challenges, and future of additive manufacturing in engineering. Comput. Des.
2015, 69, 65–89. [CrossRef]
16.
ISO. Additive manufacturing—General principles—Terminology. Iso/Astm 2015, 52900, 1–26. [CrossRef]
17.
Jiang, J.; Xu, X.; Stringer, J. Support Structures for Additive Manufacturing: A Review. J. Manuf. Mater.
Process. 2018, 2, 64. [CrossRef]
18.
Jin, G.; Li, W.; Tsai, C.; Wang, L. Adaptive tool-path generation of rapid prototyping for complex product
models. J. Manuf. Syst. 2011, 30, 154–164. [CrossRef]
19.
Jin, G.; Li, W.; Gao, L. An adaptive process planning approach of rapid prototyping and manufacturing.
Robot. Comput. Manuf. 2013, 29, 23–38. [CrossRef]
20.
Jin, Y.; Du, J.; He, Y.; Fu, G. Modeling and process planning for curved layer fused deposition. Int. J. Adv.
Manuf. Technol. 2016, 91, 273–285. [CrossRef]
21.
Ezair, B.; Fuhrmann, S.; Elber, G. Volumetric covering print-paths for additive manufacturing of 3D models.
Comput. Des. 2018, 100, 1–13. [CrossRef]
22.
Jensen, M.L.; Mahshid, R.; D’Angelo, G.; Walther, J.U.; Kiewning, M.K.; Spangenberg, J.; Hansen, H.N.;
Pedersen, D.B. Toolpath Strategies for 5DOF and 6DOF Extrusion-Based Additive Manufacturing. Appl. Sci.
2019, 9, 4168. [CrossRef]
23.
Routhu, S.; Kanakanala, D.; Ruan, J.; Liu, X.F.; Liou, F. 2-D Path Planning for Direct Laser Deposition Process.
In Proceedings of the Volume 1: 36th Design Automation Conference, Parts A and B; ASME International: New
York, NY, USA, 2010; pp. 415–423.
24.
Jin, Y.; He, Y.; Fu, J.; Gan, W.-F.; Lin, Z.-W. Optimization of tool-path generation for material extrusion-based
additive manufacturing technology. Addit. Manuf. 2014, 1, 32–47. [CrossRef]
25.
Comminal, R.; Serdeczny, M.P.; Pedersen, D.B.; Spangenberg, J. Motion planning and numerical simulation
of material deposition at corners in extrusion additive manufacturing. Addit. Manuf. 2019, 29, 100753.
[CrossRef]
26.
Liu, H.H.; Zhao, T.; Li, L.Y.; Liu, W.J.; Wang, T.Q.; Yue, J.F. A path planning and sharp corner correction
strategy for wire and arc additive manufacturing of solid components with polygonal cross-sections. Int. J.
Adv. Manuf. Technol. 2020, 106, 4879–4889. [CrossRef]


---


## Page 15


Micromachines 2020, 11, 633
15 of 18
27.
Giberti, H.; Sbaglia, L.; Urgo, M. A path planning algorithm for industrial processes under velocity constraints
with an application to additive manufacturing. J. Manuf. Syst. 2017, 43, 160–167. [CrossRef]
28.
Ding, D.; Pan, Z.; Cuiuri, D.; Li, H. A tool-path generation strategy for wire and arc additive manufacturing.
Int. J. Adv. Manuf. Technol. 2014, 73, 173–183. [CrossRef]
29.
Eiliat, H.; Urbanic, J. Minimizing Voids with Using an Optimal Raster Orientation and Bead Width for a
Material Extrusion Based Process. In ASME International Mechanical Engineering Congress and Exposition;
American Society of Mechanical Engineers: New York, NY, USA, 2016. [CrossRef]
30.
Eiliat, H. Development of Optimal Material Extrusion Additive Manufacturing Tool Path Parameters for Minimizing
Void Regions Using Contemporary Tool Path Solutions; University of Windso: Windsor, ON, Canada, 2016.
31.
Eiliat, H.; Urbanic, J. Visualizing, analyzing, and managing voids in the material extrusion process. Int. J.
Adv. Manuf. Technol. 2018, 96, 4095–4109. [CrossRef]
32.
Xiong, Y.; Park, S.-I.; Padmanathan, S.; Dharmawan, A.G.; Foong, S.; Rosen, D.W.; Soh, G.S. Process planning
for adaptive contour parallel toolpath in additive manufacturing with variable bead width. Int. J. Adv.
Manuf. Technol. 2019, 105, 4159–4170. [CrossRef]
33.
Kumar, A.; Maji, K. Bead Modelling and Deposition Path Planning in Wire Arc Additive Manufacturing of
Three Dimensional Parts. Mater. Sci. Forum 2019, 969, 582–588. [CrossRef]
34.
Wang, R.; Zhang, H.; Gui-Lan, W.; Zhao, X. Cylindrical slicing and path planning of propeller in wire and arc
additive manufacturing. Rapid Prototyp. J. 2020, 26, 49–58. [CrossRef]
35.
Wang, X.; Wang, A.; Li, Y. A sequential path-planning methodology for wire and arc additive manufacturing
based on a water-pouring rule. Int. J. Adv. Manuf. Technol. 2019, 103, 3813–3830. [CrossRef]
36.
Michel, F.; Lockett, H.; Ding, J.; Martina, F.; Marinelli, G.; Williams, S. A modular path planning solution for
Wire + Arc Additive Manufacturing. Robot. Comput. Manuf. 2019, 60, 1–11. [CrossRef]
37.
Ding, D.; Pan, Z.; Cuiuri, D.; Li, H. Process planning for robotic wire and arc additive manufacturing. In
Proceedings of the 2015 IEEE 10th Conference on Industrial Electronics and Applications (ICIEA), Auckland,
New Zealand, 15–17 June 2015; pp. 2000–2003.
38.
Ding, D.; Pan, Z.; Cuiuri, D.; Li, H.; Larkin, N. Adaptive path planning for wire-feed additive manufacturing
using medial axis transformation. J. Clean. Prod. 2016, 133, 942–952. [CrossRef]
39.
Ding, D.; Pan, Z.; Cuiuri, D.; Li, H.; Van Duin, S.; Larkin, N. Bead modelling and implementation of adaptive
MAT path in wire and arc additive manufacturing. Robot. Comput. Manuf. 2016, 39, 32–42. [CrossRef]
40.
Ding, D.; Pan, Z.; Cuiuri, D.; Li, H. A practical path planning methodology for wire and arc additive
manufacturing of thin-walled structures. Robot. Comput. Manuf. 2015, 34, 8–19. [CrossRef]
41.
Ren, L.; Ruan, J.; Eiamsa-ard, K.; Liou, F. Adaptive deposition coverage toolpath planning for metal depositon
process. In Proceedings of the 2007 ASME International Design Engineering Technical Conferences and
Computers and Information in Engineering Conference, DETC2007, Las Vegas, NV, USA, 4–7 September
2007; pp. 413–419.
42.
Han, W.; Jafari, M.A.; Danforth, S.C.; Safari, A. Tool Path-Based Deposition Planning in Fused Deposition
Processes. J. Manuf. Sci. Eng. 2002, 124, 462–472. [CrossRef]
43.
Jin, Y.-A.; He, Y.; Xue, G.-H.; Fu, J.-Z. A parallel-based path generation method for fused deposition modeling.
Int. J. Adv. Manuf. Technol. 2014, 77, 927–937. [CrossRef]
44.
Jin, Y.; Du, J.; Ma, Z.; Liu, A.; He, Y. An optimization approach for path planning of high-quality and uniform
additive manufacturing. Int. J. Adv. Manuf. Technol. 2017, 92, 651–662. [CrossRef]
45.
Zhao, G.; Ma, G.; Feng, J.; Xiao, W. Nonplanar slicing and path generation methods for robotic additive
manufacturing. Int. J. Adv. Manuf. Technol. 2018, 96, 3149–3159. [CrossRef]
46.
Tarabanis, K. Path planning in the Proteus rapid prototyping system. Rapid Prototyp. J. 2001, 7, 241–252.
[CrossRef]
47.
Jiang, J.; Xu, X.; Stringer, J. Optimization of process planning for reducing material waste in extrusion based
additive manufacturing. Robot. Comput. Manuf. 2019, 59, 317–325. [CrossRef]
48.
Jiang, J.; Xu, X.; Stringer, J. A new support strategy for reducing waste in additive manufacturing. In
Proceedings of the 48th International Conference on Computers and Industrial Engineering (CIE 48),
Auckland, New Zealand, 2–5 December 2018; pp. 1–7.
49.
Jiang, J.; Stringer, J.; Xu, X. Support Optimization for Flat Features via Path Planning in Additive
Manufacturing. 3D Print. Addit. Manuf. 2019, 6, 171–179. [CrossRef]


---


## Page 16


Micromachines 2020, 11, 633
16 of 18
50.
Jiang, J.; Stringer, J.; Xu, X.; Zheng, P. A benchmarking part for evaluating and comparing support structures
of additive manufacturing. In Proceedings of the 3rd International Conference on Progress in Additive
Manufacturing (Pro-AM 2018), Singapore, 14–17 May 2018. pp. 196–202.
51.
Nguyen, L.; Buhl, J.; Bambach, M. Decomposition algorithm for tool path planning for wire-arc additive
manufacturing. J. Mach. Eng. 2018, 18, 96–107. [CrossRef]
52.
Thompson, B.; Yoon, H.-S. Eﬃcient Path Planning Algorithm for Additive Manufacturing Systems. IEEE
Trans. Components, Packag. Manuf. Technol. 2014, 4, 1555–1563. [CrossRef]
53.
Ding, Y.; Dwivedi, R.; Kovacevic, R. Process planning for 8-axis robotized laser-based direct metal deposition
system: A case on building revolved part. Robot. Comput. Manuf. 2017, 44, 67–76. [CrossRef]
54.
Zhang, J.; Liou, F. Adaptive Slicing for a Multi-Axis Laser Aided Manufacturing Process. J. Mech. Des. 2004,
126, 254–261. [CrossRef]
55.
Bui, H.; Pierson, H.A.; Nurre, S.G.; Sullivan, K.M. Tool Path Planning Optimization for Multi-Tool Additive
Manufacturing. Procedia Manuf. 2019, 39, 457–464. [CrossRef]
56.
Choi, S.; Zhu, W. A dynamic priority-based approach to concurrent toolpath planning for multi-material
layered manufacturing. Comput. Des. 2010, 42, 1095–1107. [CrossRef]
57.
Volpato, N.; Galvão, L.C.; Nunes, L.F.; Souza, R.I.; Oguido, K. Combining heuristics for tool-path optimisation
in material extrusion additive manufacturing. J. Oper. Res. Soc. 2019, 71, 867–877. [CrossRef]
58.
Ganganath, N.; Cheng, C.-T.; Fok, K.-Y.; Tse, C.K. Trajectory planning for 3D printing: A revisit to traveling
salesman problem. In Proceedings of the 2016 2nd International Conference on Control, Automation and
Robotics (ICCAR), Hong Kong, China, 28–30 April 2016; pp. 287–290.
59.
Fleming, C.; Walker, S.; Branyan, C.; Nicolai, A.; Hollinger, G.; Mengüç, Y. Toolpath Planning for Continuous
Extrusion Additive Manufacturing; Oregon State University: Corvallis, OR, USA, 2017.
60.
Fok, K.-Y.; Ganganath, N.; Cheng, C.-T.; Tse, C.K. A 3D printing path optimizer based on Christoﬁdes
algorithm. In Proceedings of the 2016 IEEE International Conference on Consumer Electronics-Taiwan
(ICCE-TW), Nantou County, Taiwan, 27–29 May 2016; pp. 1–2.
61.
Jin, Y.; He, Y.; Fu, G.; Zhang, A.; Du, J. A non-retraction path planning approach for extrusion-based additive
manufacturing. Robot. Comput. Manuf. 2017, 48, 132–144. [CrossRef]
62.
Papacharalampopoulos, A.; Bikas, H.; Stavropoulos, P. Path planning for the inﬁll of 3D printed parts
utilizing Hilbert curves. Procedia Manuf. 2018, 21, 757–764. [CrossRef]
63.
Luo, R.C.; Tseng, P.-K. Trajectory generation and planning for simultaneous 3D printing of multiple objects.
In Proceedings of the 2017 IEEE 26th International Symposium on Industrial Electronics (ISIE), Edinburgh,
UK, 19–21 June 2017; pp. 1147–1152. [CrossRef]
64.
Jiang, J. A novel fabrication strategy for additive manufacturing processes. J. Clean Prod. 2020, in press.
65.
Zhai, X.; Chen, F. Path Planning of a Type of Porous Structures for Additive Manufacturing. Comput. Des.
2019, 115, 218–230. [CrossRef]
66.
Dreifus, G.; Goodrick, K.; Giles, S.; Patel, M.; Foster, R.M.; Williams, C.; Lindahl, J.; Post, B.; Roschli, A.;
Love, L.; et al. Path Optimization Along Lattices in Additive Manufacturing Using the Chinese Postman
Problem. 3D Print. Addit. Manuf. 2017, 4, 98–104. [CrossRef]
67.
Coupek, D.; Friedrich, J.; Battran, D.; Riedel, O. Reduction of Support Structures and Building Time by
Optimized Path Planning Algorithms in Multi-axis Additive Manufacturing. Procedia CIRP 2018, 67, 221–226.
[CrossRef]
68.
McQueen, K.; Darensbourg, S.; Moore, C.; Dickens, T.; Allen, C. Eﬃcient Path Planning of Secondary Additive
Manufacturing Operations. In Proceedings of the MATEC Web of Conferences; EDP Sciences: Les Ulis, France,
2018; Volume 249, p. 03011.
69.
Shembekar, A.V.; Yoon, Y.J.; Kanyuck, A.; Gupta, S.K. Trajectory Planning for Conformal 3D Printing Using
Non-Planar Layers. In Proceedings of the Volume 1A: 38th Computers and Information in Engineering Conference;
ASME International: New York, NY, USA, 2018.
70.
Cai, Y.; Choi, S. Deposition Group-based Toolpath Planning for Additive Manufacturing with Multiple
Robotic Actuators. Procedia Manuf. 2019, 34, 584–593. [CrossRef]
71.
Fügenschuh, A.; Bambach, M.; Buhl, J. Trajectory Optimization for Wire-Arc Additive Manufacturing. Oper.
Res. Proc. 2019, 331–337. [CrossRef]


---


## Page 17


Micromachines 2020, 11, 633
17 of 18
72.
Li, N.; Link, G.; Wang, T.; Ramopoulos, V.; Neumaier, D.; Hofele, J.; Walter, M.; Jelonnek, J. Path-designed 3D
printing for topological optimized continuous carbon ﬁbre reinforced composite structures. Compos. Part B
Eng. 2020, 182, 107612. [CrossRef]
73.
Asif, S. Modelling and Path Planning for Additive Manufacturing of Continuous Fiber Composites; Sabanci
University: Istanbul, Turkey, 2018.
74.
Kraljic, D.; Kamnik, R. Trajectory Planning for Additive Manufacturing with a 6-DOF Industrial Robot. In
Proceedings of the Modeling and Control of a Tracked Mobile Robot for Pipeline Inspection; Springer Science and
Business Media LLC: Berlin/Heidelberg, Germany, 2018; pp. 456–465.
75.
Liu, J.; Ma, Y.; Qureshi, A.J.; Ahmad, R. Light-weight shape and topology optimization with hybrid deposition
path planning for FDM parts. Int. J. Adv. Manuf. Technol. 2018, 97, 1123–1135. [CrossRef]
76.
Liu, J.; Yu, H. Concurrent deposition path planning and structural topology optimization for additive
manufacturing. Rapid Prototyp. J. 2017, 23, 930–942. [CrossRef]
77.
Jin, Y.; He, Y.; Shih, A. Process Planning for the Fuse Deposition Modeling of Ankle-Foot-Othoses. Procedia
CIRP 2016, 42, 760–765. [CrossRef]
78.
Lin, S.; Xia, L.; Ma, G.; Zhou, S.; Xie, Y.M. A maze-like path generation scheme for fused deposition modeling.
Int. J. Adv. Manuf. Technol. 2019, 104, 1509–1519. [CrossRef]
79.
Jin, Y.; He, Y.; Du, J. A novel path planning methodology for extrusion-based additive manufacturing of
thin-walled parts. Int. J. Comput. Integr. Manuf. 2017, 30, 1301–1315. [CrossRef]
80.
Ma, G.; Zhao, G.; Li, Z.; Xiao, W. A Path Planning Method for Robotic Wire and Arc Additive Manufacturing
of Thin-Walled Structures with Varying Thickness. In Proceedings of the IOP Conference Series: Materials Science
and Engineering; IOP Publishing: Bristol, UK, 2019; Volume 470, p. 012018.
81.
Eliseeva, O.; Kirk, T.; Samimi, P.; Malak, R.; Arróyave, R.; Elwany, A.; Karaman, I. Functionally Graded
Materials through robotics-inspired path planning. Mater. Des. 2019, 182, 107975. [CrossRef]
82.
Deuser, B.; Tang, L.; Geldmeier, J.; Landers, R.G.; Leu, M.C. Process planning and control for functionally
graded material fabrication using freeze-form extrusion fabrication. In Solid Freeform Fabrication Symposium;
Department of Mechanical and Aerospace Engineering Missouri University of Science and Technology:
Rolla, MO, USA, 2011.
83.
Ozbolat, I.T.; Khoda, A.K.M.B. Design of a New Parametric Path Plan for Additive Manufacturing of Hollow
Porous Structures with Functionally Graded Materials. J. Comput. Inf. Sci. Eng. 2014, 14, 041005. [CrossRef]
84.
Zhu, W.; Yu, K.M. Tool path generation of multi-material assembly for rapid manufacture. Rapid Prototyp. J.
2002, 8, 277–283. [CrossRef]
85.
Jiang, J.; Weng, F.; Gao, S.; Stringer, J.; Xu, X.; Guo, P. A support interface method for easy part removal in
directed energy deposition. Manuf. Lett. 2019, 20, 30–33. [CrossRef]
86.
Aoyagi, K.; Wang, H.; Chiba, A.; Sudo, H. Simple method to construct process maps for additive manufacturing
using a support vector machine. Addit. Manuf. 2019, 27, 353–362. [CrossRef]
87.
Menon, A.; Póczos, B.; Feinberg, A.W.; Washburn, N.R. Optimization of Silicone 3D Printing with Hierarchical
Machine Learning. 3D Print. Addit. Manuf. 2019, 6, 181–189. [CrossRef]
88.
He, H.; Yang, Y.; Pan, Y. Machine learning for continuous liquid interface production: Printing speed
modelling. J. Manuf. Syst. 2019, 50, 236–246. [CrossRef]
89.
Stavroulakis, P.; Chen, S.; Delorme, C.; Bointon, P.; Tzimiropoulos, G.; Leach, R. Rapid tracking of extrinsic
projector parameters in fringe projection using machine learning. Opt. Lasers Eng. 2019, 114, 7–14. [CrossRef]
90.
Baturynska, I.; Semeniuta, O.; Martinsen, K. Optimization of Process Parameters for Powder Bed Fusion
Additive Manufacturing by Combination of Machine Learning and Finite Element Method: A Conceptual
Framework. Procedia CIRP 2018, 67, 227–232. [CrossRef]
91.
Yu, C.; Jiang, J. A perspective on Using Machine Learning in 3D Bioprinting. Int. J. Bioprint. 2020, 6, 4–11.
[CrossRef]
92.
Francis, J.; Bian, L. Deep Learning for Distortion Prediction in Laser-Based Additive Manufacturing using
Big Data. Manuf. Lett. 2019, 20, 10–14. [CrossRef]
93.
Khanzadeh, M.; Rao, P.; Jafari-Marandi, R.; Smith, B.K.; Tschopp, M.A.; Bian, L.; Rao, P.K. Quantifying
Geometric Accuracy with Unsupervised Machine Learning: Using Self-Organizing Map on Fused Filament
Fabrication Additive Manufacturing Parts. J. Manuf. Sci. Eng. 2017, 140, 031011. [CrossRef]
94.
Zhu, Z.; Anwer, N.; Huang, Q.; Mathieu, L. Machine learning in tolerancing for additive manufacturing.
CIRP Ann. 2018, 67, 157–160. [CrossRef]


---


## Page 18


Micromachines 2020, 11, 633
18 of 18
95.
Tootooni, M.S.; Dsouza, A.; Donovan, R.; Rao, P.K.; Kong, Z.J.; Borgesen, P. Classifying the Dimensional
Variation in Additive Manufactured Parts from Laser-Scanned Three-Dimensional Point Cloud Data Using
Machine Learning Approaches. J. Manuf. Sci. Eng. 2017, 139, 091005. [CrossRef]
96.
Scime, L.; Beuth, J. Using machine learning to identify in-situ melt pool signatures indicative of ﬂaw formation
in a laser powder bed fusion additive manufacturing process. Addit. Manuf. 2019, 25, 151–165. [CrossRef]
97.
Caggiano, A.; Zhang, J.; Alﬁeri, V.; Caiazzo, F.; Gao, R.X.; Teti, R. Machine learning-based image processing
for on-line defect recognition in additive manufacturing. CIRP Ann. 2019, 68, 451–454. [CrossRef]
98.
Zhang, B.; Liu, S.; Shin, Y.C. In-Process monitoring of porosity during laser additive manufacturing process.
Addit. Manuf. 2019, 28, 497–505. [CrossRef]
99.
Gu, G.X.; Chen, C.-T.; Richmond, D.J.; Buehler, M.J. Bioinspired hierarchical composite design using machine
learning: Simulation, additive manufacturing, and experiment. Mater. Horizons 2018, 5, 939–945. [CrossRef]
100. Hamel, C.M.; Roach, D.J.; Long, K.N.; Demoly, F.; Dunn, M.L.; Qi, H.J.; Qi, J. Machine-learning based design
of active composite structures for 4D printing. Smart Mater. Struct. 2019, 28, 065005. [CrossRef]
101. Li, Z.; Zhang, Z.; Shi, J.; Wu, D. Prediction of surface roughness in extrusion-based additive manufacturing
with machine learning. Robot. Comput. Manuf. 2019, 57, 488–495. [CrossRef]
102. Liu, X.-H.; Zhang, D.-G.; Yan, H.-R.; Cui, Y.-Y.; Chen, L. A New Algorithm of the Best Path Selection Based
on Machine Learning. IEEE Access 2019, 7, 126913–126928. [CrossRef]
© 2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access
article distributed under the terms and conditions of the Creative Commons Attribution
(CC BY) license (http://creativecommons.org/licenses/by/4.0/).


---
