# rvillafuerte,+13268

> **Source:** `rvillafuerte,+13268.pdf`
> **Converted:** 2025-11-22 21:18:09
> **Method:** PyMuPDF

---

## Page 1


Publicación Semestral Pädi Vol. 12 No. Especial 4 (2024) 236-242




           ISSN: 2007-6363

_________
      *Autor para la correspondencia: bysuarezmaker@gmail.com
Correo electrónico: bysuarezmaker@gmail.com (Johovani-Misael Suarez-Luna), jorge.romero@ciateq.mx (Jorge-Adán Romero-Guerrero) david.arenas@ciateq.mx
(David Arenas-Islas).

Historial del manuscrito: recibido el 18/06/2024,   última versión-revisada recibida el 31/07/2024,   aceptado el 16/07/2024,
publicado el 30/11/2024.     DOI: https://doi.org/10.29057/icbi.v12iEspecial4.13268

 J.M. Suarez-Luna
a,*, J.A. Romero-Guerrero
a, D. Arenas-Isalas
a
a Departamento Manufactura Virtual y Lean y Cad Cae, CIATEQ A. C., 42163 San Agustín Tlaxiaca, Hgo, México.


Resumen
En esta investigación se evalúan las variables de productividad que evidencian que la manufactura aditiva es una herramienta
tecnológica que permite a la industria fabricar piezas de refaccionamiento de bajo volumen frente a tecnologías convencionales
como el moldeo por inyección plástica. Se utiliza una metodología donde se analizan los costos de materiales e inventario de
refacciones, se mide la productividad y escalabilidad de la granja mediante los KPI’s (Tasa de utilización de la capacidad, Tiempo
de ciclo de producción, Rendimiento de primera pasada (First-pass yield), Tasa de desecho (Scrap rate), Velocidad de
producción, Costo por pieza producida, Tiempo medio entre fallas (Mean time between failures - MTBF). Las conclusiones
demuestran que las granjas de impresión 3D son una opción viable para enfrentar los retos de suministro de refacciones que no
están en stock, tardan mucho tiempo en ser enviadas por los proveedores o ya no se encuentran en el mercado por su antigüedad.
Se concluye con un comparativo entre la inyección plástica y la manufactura aditiva del caso de estudio.
Palabras Clave: FDM, granja, refacciones, análisis, materiales.

Abstract
This research evaluates the productivity variables that show that additive manufacturing is a technological tool that allows
the industry to manufacture low-volume spare parts compared to conventional technologies such as plastic injection molding. A
methodology is used where the costs of materials and spare parts inventory are analyzed, the productivity and scalability of the
farm is measured through the KPI's (Capacity utilization rate, Production cycle time, First-pass performance yield), Scrap rate,
Production speed, Cost per piece produced, Mean time between failures (MTBF). The conclusions demonstrate that 3D printing
farms are a viable option to address the challenges of supplying spare parts that are not in stock, take a long time to be shipped
by suppliers, or are no longer on the market due to their age. It concludes with a comparison between plastic injection and
additive manufacturing of the case study.
Keywords: FDM, farm, spare parts, analysis, materials.

1. Introducción
La manufactura aditiva o impresión 3D se ha popularizado
gracias a la democratización de la tecnología FDM por el
opensource y en las últimas tres décadas, la tecnología de
fabricación aditiva (AM) ha tenido un avance significativo y
actualmente se utiliza en una gran variedad de sectores
sociales, académicos e industriales. Esta tecnología ha sido
referenciada por una serie de etiquetas, incluyendo la creación
rápida de prototipos (RP), la fabricación en capas (LM) y la
fabricación de sólidos. fabricación de forma libre (SFF)
(Bandyopadhyay, 2019).

De acuerdo con la norma ISO/ASTM 52900-2015 la
manufactura aditiva se clasifica en:

Vat Photopolymerization (VP)

Material Jetting (MJ)

Binder Jetting (BJ)

Powder Bed Fusion (PBF)

Material Extrusion (ME)

Directed Energy Deposition (DED)

Sheet Lamination (SL) (Gibson et al., 2015),
(Saleh Alghamdi et al., 2021).

La Industria 4.0 ha permitido a las empresas aprovechar
soluciones tecnológicas avanzadas junto con estrategias de
gestión innovadoras para satisfacer mejor las necesidades de
sus clientes. Esto es especialmente importante para las
operaciones de servicio, donde la disponibilidad de piezas de
repuesto y componentes para mantenimiento y reparaciones
Productividad de granjas de manufactura aditiva en la cadena de suministro industrial
Productivity of additive manufacturing farms in the industrial supply chain


---


## Page 2


J.M. Suarez-Luna et al. / Publicación Semestral Pädi Vol. 12 No. Especial 4 (2024) 236–242                                                  237

oportunos es crucial para minimizar el tiempo de inactividad y
maximizar la eficacia operativa y la capacidad de respuesta.
Más específicamente, la escasez de piezas de repuesto puede
ser potencialmente catastrófica, ya que un componente fallido
puede provocar prolongadas interrupciones y fallos del sistema
(Huiskonen, 2001), (Rustenburg et al., 2000).

La adopción de la impresión 3D en la fabricación de piezas
de repuesto ha recibido una atención creciente recientemente,
y el número de publicaciones se ha triplicado en los últimos
diez años. Entre estas investigaciones, casi el 50 % se centran
en áreas de ciencia de materiales e ingeniería mecánica, con un
énfasis en el desarrollo de tecnología avanzada para ampliar
los dominios de aplicación (McDermott et al., 2021). Sin
embargo, no se ha estudiado bien cómo la adopción de esta
tecnología impacta en la cadena de suministro de piezas de
repuesto. Algunos pocos estudios y reportes tocan este tema
desde un punto de vista cualitativo. Por ejemplo, Holmström
et al. (2010) destacaron los beneficios de la fabricación aditiva
y sus soluciones para el suministro de piezas de repuesto en la
industria aeronáutica a través de revisiones bibliográficas y
entrevistas a expertos. Luego, en su artículo, se delineó un
procedimiento de evaluación de viabilidad. Holmström y
Partanen (2014) en otro estudio, señalaron que la introducción
de la fabricación aditiva puede aumentar la disponibilidad de
piezas de repuesto y cambiar la configuración de la cadena de
suministro al acercarse más a las ubicaciones de los usuarios.
Más recientemente, Gisario et al. (2019) revisaron la
aplicación de la fabricación aditiva en la industria de la
aviación comercial.

Una revisión de la literatura previa muestra que la adopción
de la fabricación aditiva (AM, por sus siglas en inglés) ha
atraído una atención creciente en el área de investigación
operativa, pero aún se encuentra en una etapa preliminar.
Muchos trabajos cualitativamente discutieron los posibles
beneficios y desafíos que trae consigo la AM desde la
perspectiva de la gestión de operaciones. Al elaborar un plan
para investigaciones futuras, todos estos estudios cualitativos
resaltaron la importancia de contar con una herramienta de
verificación y gestión cuantitativa para la cadena de suministro
de AM. Sin embargo, solo se puede encontrar un puñado de
estudios cuantitativos. Al revisar estos trabajos cuantitativos
limitados, se pueden abordar algunas brechas de investigación.

En primer lugar, los estudios cuantitativos existentes en su
mayoría estudiaron un caso deducido con una estructura muy
simple (Khajavi et al., 2014), (Li et al., 2017), (Li et al., 2018).

Una cadena de suministro de un solo tramo con nodos
independientes no puede reflejar bien la realidad. En segundo
lugar, la mayoría de estos estudios solo compararon costos
entre diferentes escenarios (Khajavi et al., 2014), (Khajavi et
al., 2018), (Tapia-Ubeda et al., 2020).

Deberían estudiarse más indicadores para dar a las partes
interesadas una imagen completa del rendimiento del sistema.

En tercer lugar, casi todos los trabajos existentes centraron
su atención principal en las configuraciones de la cadena de
suministro. Los desafíos en la adopción de AM son más que
los cambios en la configuración.
1.1. Short Running Manufacturing
Se refiere a un enfoque de fabricación que se centra en la
producción de lotes pequeños de productos, generalmente con
ciclos de producción cortos y rápidos cambios entre diferentes
productos o variantes. Este concepto contrasta con la
fabricación de grandes volúmenes de un solo producto durante
períodos prolongados, como en la fabricación en masa
tradicional. En la práctica, el short running manufacturing se
utiliza para satisfacer demandas específicas del mercado,
adaptarse rápidamente a cambios en las preferencias del cliente
o en el diseño del producto, reducir los costos de inventario y
minimizar el tiempo de entrega.

Este enfoque es especialmente relevante en industrias
donde la personalización de productos, la variedad de
productos y la rápida respuesta a la demanda son prioritarias,
como en la fabricación de productos de moda, electrónica de
consumo, dispositivos médicos y automóviles personalizados.

El short running manufacturing se beneficia de tecnologías
avanzadas de fabricación, como la impresión 3D y la
fabricación aditiva, que permiten la producción ágil y flexible
de pequeños lotes de productos con tiempos de configuración
mínimos y costos de producción reducidos. Este enfoque
también puede integrar sistemas de fabricación automatizados
y técnicas de optimización de la cadena de suministro para
mejorar la eficiencia y la calidad del proceso de producción.

2. Metodología de análisis
La metodología para evaluar la productividad de una granja
de impresión 3D se analiza desde diferentes perspectivas, en la
Figura 1 se pueden observar cada una de ellas. El análisis
planteado en este trabajo solo abarcará los indicadores claves
de desempeño (KPI’s por sus siglas en ingles).


Figura 1: Metodología para evaluar la productividad de una granja de
impresión 3D.
Para definir nuestra granja de impresión 3D, es necesario
que seleccionemos el tipo de impresora 3D, número de
máquinas, volumen de impresión y flujo volumétrico de
extrusión.

Actualmente dentro de la tecnología FDM podemos acceder
a máquinas de impresión 3D de FDM, de las cuales tenemos
diferentes configuraciones como: delta, cartesiana y coreXY.


---


## Page 3


J.M. Suarez-Luna et al. / Publicación Semestral Pädi Vol. 12 No. Especial 4 (2024) 236–242                                                  238

Para que nuestra granja de impresión 3D tenga una
velocidad de impresión de alta velocidad es recomendable
utilizar la configuración coreXY. Bajo esta primicia se elige el
modelo KINGROON KPL1 la cual tiene las siguientes
características:

Tabla 1: características de la impresora KLP1.
Característica
Valor
Volumen de impresión
210x210x210 cm
Sistema de movimiento
Guías lineales MG12
Tipo de extrusor
All metal
Velocidad de impresión
200-300 mm/s
Temperatura de extrusión
<300°C
Cerrada o abierta
Cerrada
Materiales para imprimir
PLA, PETG, ABS, ASA

El presupuesto para la implementación de la granja es el
siguiente (solo incluye equipo e insumos), en pesos mexicanos:

Tabla 2: Presupuesto.
Item
Descripción
Cantidad
Costo
Unitario
Costo
total
1
Impresora
Kingroon KPL1
10
$6,850
$68,500
2
Kg de Filamento
PETG
20
$350
$7,000
3
Kit de
Refaccionamiento
10
$1,000
$10,000

El costo total es de $85,500.00 pesos mexicanos.

La pieza con la cual se hará el análisis es un seguro para
sujetar una tapa de un sensor, actualmente la pieza es fabricada
por inyección de plástico y debido a la antigüedad de la
maquinaria, esta pieza ya no es comercial, adicional a este
problema, la pieza sufre de una concentración de esfuerzo que
sobre pasa las propiedades mecánicas y tiende a fallar. Las
características actuales de la pieza son:

Tabla 3: Características del seguro.
Propiedad
Dimensión
Unidad
Largo
45
mm
Ancho
25
mm
Alto
27
mm
Peso
7.9
Gramos
Material
Polietileno de alta
densidad

Número de
piezas
2500
unidades


Figura 2: Seguro de sensor.
Debido a que esta pieza no cuenta un diseño CAD, se tiene
que modelar y se aprovecha para hacer cambios de ingeniería
que mejoren la funcionalidad de la pieza. Para tal actividad se
realiza en el software FUSION 360 de Autodesk. A
continuación, se muestra el modelo 3D.


Figura 3: Modelo 3D del seguro de sensor en Fusion 360.
El proceso de manufactura aditiva de manera general se
describe en las siguientes fases:


Modelado 3D. Durante esta fase se pueden tener 2
escenarios, el primero considera que ya se cuenta un
archivo 3D que permitirá exportar una malla en
formato STL para poder ser importado en el software
de laminado, en el escenario 2, no se cuenta con el
modelo 3D y se tiene que desarrollar tal modelo, en
el caso particular del seguro, se tiene que realizar esta
actividad.


Configuración de la impresión. En esta etapa se
utiliza un software que nos permiten laminar el
modelo 3D y establecer los parámetros de impresión
y obtener el código G que utilizará la impresora 3D.


Enviar el código G a la impresora. Esta acción puede
ser mediante una USB o vía wifi, para la impresora
KLP1 se cuenta con una interfaz que permite
gestionar los archivos desde una IP.


Postprocesado de la pieza. En muchas ocasiones es
necesario realizar una actividad de lijado o
eliminación de soportes para obtener una mejor
calidad de las piezas.

De acuerdo con la metodología propuesta, a continuación,
se describen los KPI’s para su análisis.
2.1. Tasa de utilización de la capacidad
Para calcular la tasa de utilización de la capacidad de una
granja de impresoras 3D, se necesita conocer dos variables: la
cantidad total de tiempo que las impresoras 3D están siendo
utilizadas para imprimir y la cantidad total de tiempo
disponible durante un período determinado. A continuación, se
describe la formula a desarrollar:

  
		 =
 
  ∗100.
(1)


---


## Page 4


J.M. Suarez-Luna et al. / Publicación Semestral Pädi Vol. 12 No. Especial 4 (2024) 236–242                                                  239

Considerando que la impresora KLP1 puede trabajar 24
horas, esto no es recomendable ya que se requiere tiempo de
preparación y descarga de los lotes de piezas fabricadas, por lo
tanto, tendremos un 80% de tiempo disponible.

El tiempo utilizado sería igual a la capacidad máxima de
producción por máquina, es decir, cuantas piezas pueden ser
fabricadas en la cama de impresión. Para obtener el tiempo que
se tarda en fabricar la pieza se tiene que desarrollar la
configuración de laminado y obtener un estimado. A
continuación, se muestra una Tabla con las principales
variables de configuración.

Tabla 4: Parámetros de impresión.
Variable
Dimensión
Unidad
Altura de capa
0.2
mm
Número de
paredes
3
Paredes
Porcentaje de
relleno
20
%
Tipo de relleno
Giroide
Velocidad de
impresión
90
mm/s
Temperatura de
impresión
235
°C
Material de
impresión
PETG

No. De piezas por
lote
1
pieza
Peso de la pieza
7.9
gramos


Figura 4: Configuración de parámetros para impresión por FDM en el
software Orcaslicer.
La capacidad máxima de la cama de impresión de la KLP1
es de 36 piezas y tarda 12.05 horas. La granja de impresión 3D
sería capaz de producir 360 piezas en 12.05 horas.

Con estos datos nuestra tasa de utilización quedaría en un
64%.

  
		ó =
&'.()
&*.' ∗100 = 63%.
(2)
Para maximizar la tasa de utilización podríamos llegar a
fabricar hasta 516 piezas en un periodo de 17.3 horas y nuestra
tasa de utilización quedaría de la siguiente manera:

  
		ó =
&-..
&*.' ∗100 = 90%.
(3)


Figura 5: Distribución de la capacidad total de las piezas en la impresora
KLP1 en el software Orcaslicer.
2.2. Tiempo ciclo
El tiempo ciclo de producción por pieza está definido por
las siguientes actividades que se muestran en la Tabla 5.

Tabla 5: Tiempo ciclo de producción. Escenario A.
Actividad
Duración (hr)
Modelado 3D de la pieza
0.5
Segmentado de la pieza en slicer
0.5
Proceso de impresión
0.37
Retiro y limpieza de bandeja
0.07
Retiro de soportes en la pieza
0
Inspección visual de la pieza
0.08
Eliminación de rebabas de la pieza
0.1
Total
1.65










Figura 6: Diagrama de pastel para el tiempo ciclo del escenario A.

Cuando se trabaja por volumen estos valores se ven
afectados de la siguiente manera:

Tabla 5: Tiempo ciclo de producción por lote de 36 piezas. Escenario B.
Actividad
Duración (hr)
Modelado 3D de la pieza
0.5
Segmentado de la pieza en slicer
0.5
Proceso de impresión
12.05
Retiro y limpieza de bandeja
0.07
Retiro de soportes en la pieza
0
Inspección visual de la pieza
0.90
Eliminación de rebabas de la pieza
0.90
Total
14.91


---


## Page 5


J.M. Suarez-Luna et al. / Publicación Semestral Pädi Vol. 12 No. Especial 4 (2024) 236–242                                                  240











Figura 7: Diagrama de pastel para el tiempo ciclo del escenario B.

Para la granja de impresión 3D quedaría de la siguiente
manera:

Tabla 6: Tiempo ciclo de producción por lote de 36 piezas en una granja de
impresión 3D de 10 impresoras. Escenario c.
Actividad
Duración (hr)
Modelado 3D de la pieza
0.5
Segmentado de la pieza en slicer
0.5
Proceso de impresión
12.05
Retiro y limpieza de bandeja
0.07
Retiro de soportes en la pieza
0
Inspección visual de la pieza
9.00
Eliminación de rebabas de la pieza
9.00
Total
31.11










Figura 8: Diagrama de pastel para el tiempo ciclo del escenario C.

Para alcanzar la producción requerida del cliente se
requieren de 4.84 servicios de impresión, traducido a 83.68
horas de impresión.
2.3. Rendimiento de primera pasada (FPY)
El rendimiento de primera pasada (FPY), se calcula de la
siguiente manera:

012 =
34   564   44 
34    45
∗100%.  (4)
Para nuestro caso de practica el número de unidades
conformes en el primer intento, es de 34 piezas de un total de
36. Por lo tanto, nuestro FPY es igual a:

012 =
.7
.8 ∗100% = 94%.                           (5)

Tabla 7: Comparación entre los tres escenarios.
Variable
Escenario
A
Escenario
B
Escenario
C
Modelado
3D de la
pieza
0.5
0.5
0.5
Segmentado
de la pieza
en slicer
0.5
0.5
0.5
Proceso de
impresión
0.37
12.05
12.05
Retiro y
limpieza de
bandeja
0.07
0.07
0.07
Retiro de
soportes en
la pieza
0
0
0
Inspección
visual de la
pieza
0.08
0.90
9.0
Eliminación
de rebabas
de la pieza
0.1
0.90
9.0


Figura 9: Comparación entre los 3 escenarios.
2.4. Tasa de desecho
La tasa de desecho por lote en la granja de impresión se
calcula con la siguiente formula:

  ℎ =
3ú4   65
3ú4    45 ∗100%.  (6)

  ℎ =
&(
)&8 ∗100% = 1.94%.
      (7)

Para nuestro escenario tenemos una tasa de desecho del
1.94%.
2.5. Velocidad de producción (<)
La velocidad de producción =<> está definida por el
número de unidades producidas por unidad de tiempo, la
formula está definida de la siguiente manera:

< =
3ú4   45
 4544
=
)&8
.&.&& = 16.58.
   (8)
2.6. Costo de producción por lote
El costo de producción está integrado por los siguientes
conceptos:


---


## Page 6


J.M. Suarez-Luna et al. / Publicación Semestral Pädi Vol. 12 No. Especial 4 (2024) 236–242                                                  241



@  AB	
 =@>

@  kWh =@FGH>

	AI  IB	ó IB
 =>

Depreciación por unidades de
IB	=VF>

En la siguiente tabla se describen los parámetros antes
mencionados.

Tabla 8: Costo de pieza.
@
@FGH

VH
$ 350.00
$ 0.94
12.05
$ 0.01957

Con la siguiente formula podríamos calcular el costo de
producción:

@455 = W ∗ X∗@A
&((( Y 
 ∗@Z[ℎY VAℎ\,
(9)
@455 = 516 ∗^7.9 ∗1000
$350
Y 0.37 ∗0.94 Y 0.01957a,
=  $7,281.57.
@4 =
$-,'c&.)-
)&8
=   $14.11.                        (10)
El costo unitario por pieza es de $14.11, el costo total por
las 2,500 piezas que requiere el usuario es de $35,278.93 pesos
mexicanos.
2.7. Tiempo medio entre fallas
El Tiempo Medio Entre Fallas (MTBF, por sus siglas en
inglés: Mean Time Between Failures) es una métrica de
confiabilidad que indica el tiempo promedio que un sistema o
componente opera sin fallar. Para calcular el MTBF, se utiliza
la siguiente formula:

de0 =
   45ó
3ú4  6
.
            (11)

Tabla 9: Tiempo medio entre fallas.
Tiempo total de operación
Número de fallas
800
3

de0 =
c((
. = 266.6 ℎB.                            (12)
Esto significa que, en promedio, la impresora 3D opera
durante 266.6 horas antes de experimentar una falla.

3. Molde por inyección plástica
Para evaluar el costo del molde por inyección plástica se
realiza una cotización en la plataforma ICOMOLD BY
FHATOM y el resultado que nos da es un costo aproximado
de: $3,462 dólares con un tiempo de entrega mínimo de 15
días. Adicional a diseñar y fabricar el molde, es necesario
considerar las siguientes variables:


Adquisición de materia prima.

Adquisición o renta de una inyectora,

Transporte

Operadores especializados.

Si solo se contemplara el costo del molde y se dividiera
entre las 2500 piezas que solicita el cliente, se tendría un costo
por unidad de: 1.3848 dólares y su equivalente en pesos
mexicanos seria de: $25.6188 pesos mexicanos.


Figura 10: Cotización en la plataforma ICOMOLD BY FHATOM.

4. Conclusiones
La manufactura aditiva o impresión 3D en tecnología FDM
es una herramienta capaz de satisfacer volúmenes de
producción cortos a bajo costo, con una flexibilidad que
permite cambios en el diseño de piezas y materiales. En
nuestro caso de estudio, se demostró que una granja de
impresión 3D de 10 impresoras puede producir 2500 piezas en
83.68 horas, equivalente a 4.3 días, con un costo de $7,281.57
pesos mexicanos. La fabricación de un molde de inyección
para una pieza de este tipo, debido al bajo volumen, no es
viable por la alta inversión requerida.

La producción mediante impresión 3D permite una rápida
adaptación a las necesidades cambiantes del mercado y la
personalización
de
productos
sin
incrementar
significativamente los costos. Esto ofrece una ventaja
competitiva,
especialmente
en
industrias
donde
la
disponibilidad inmediata de repuestos es crítica.

En futuros trabajos, se analizarán las características
geométricas y propiedades mecánicas de las piezas producidas
para integrar estos aspectos en el estudio, fortaleciendo la
investigación y validando aún más la viabilidad y eficiencia de
la
manufactura
aditiva.
Además,
se
explorará
la
implementación de granjas de impresión 3D en sistemas de
manufactura más amplios y su impacto en la cadena de
suministro y logística industrial.

Comparando la tecnología convencional de inyección
plástica nos arroja un costo mínimo de al menos 2 veces el
costo unitario por pieza en referencia con la manufactura
aditiva o impresión 3D.
Referencias
Bandyopadhyay, A., Bose, S. (2019). Additive Manufacturing. CRC Press.
Gisario, A., Kazarian, M., Martina, F., & Mehrpouya, M. (2019). Metal
additive manufacturing in the commercial aviation industry: A review.
Journal of Manufacturing Systems, 53, 124-149.
Holmström, J., Partanen, J., Tuomi, J., & Walter, M. (2010). Rapid
manufacturing in the spare parts supply chain: Alternative approaches to
capacity deployment. Journal of manufacturing technology management,
21(6), 687-697.
Holmström, J., & Partanen, J. (2014). Digital manufacturing-driven
transformations of service supply chains for complex products. Supply
Chain Management: An International Journal, 19(4), 421-430.


---


## Page 7


J.M. Suarez-Luna et al. / Publicación Semestral Pädi Vol. 12 No. Especial 4 (2024) 236–242                                                  242

Huiskonen, J. (2001). Maintenance spare parts logistics: Special
characteristics and strategic choices. International journal of production
economics, 71(1-3), 125-133.
Gibson, I., Rosen, D., & Stucker, B. (2015). Additive manufacturing
technologies: 3D printing, rapid prototyping, and direct digital
manufacturing. Springer.
Khajavi, S. H., Partanen, J., & Holmström, J. (2014). Additive manufacturing
in the spare parts supply chain. Computers in industry, 65(1), 50-63.
Khajavi, S. H., Deng, G., Holmström, J., Puukko, P., & Partanen, J. (2018).
Selective laser melting raw material commoditization: impact on
comparative competitiveness of additive manufacturing. International
Journal of Production Research, 56(14), 4874-4896.
Li, Y., Jia, G., Cheng, Y., & Hu, Y. (2017). Additive manufacturing
technology in spare parts supply chain: a comparative study. International
Journal of Production Research, 55(5), 1498-1515.
Li, Y., Cheng, Y., Hu, Q., Zhou, S., Ma, L., & Lim, M. K. (2019). The
influence of additive manufacturing on the configuration of make-to-order
spare parts supply chain under heterogeneous demand. International
journal of production research, 57(11), 3622-3641.
McDermott, K. C., Winz, R. D., Hodgson, T. J., Kay, M. G., King, R. E., &
McConnell, B. M. (2021). Performance tradeoffs for spare parts supply
chains with additive manufacturing capability servicing intermittent
demand. Journal of Defense Analytics and Logistics, 5(2), 179-213.
Rustenburg, W. D., van Houtum, G. J., & Zijm, W. H. M. (2000). Spare parts
management for technical systems: resupply of spare parts under limited
budgets. IIE transactions, 32(10), 1013-1026.
Saleh Alghamdi, S., John, S., Roy Choudhury, N., & Dutta, N. K. (2021).
Additive manufacturing of polymer materials: Progress, promise and
challenges. Polymers, 13(5), 753.
Tapia-Ubeda, F. J., Miranda, P. A., Roda, I., Macchi, M., & Durán, O. (2020).
Modelling and solving spare parts supply chain network design problems.
International Journal of Production Research, 58(17), 5299-5319.


---
