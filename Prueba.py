import pandas as pd
import streamlit as st
import numpy as np
import math

st.set_page_config(page_title="Óptica Cuántica",page_icon="🎇")

st.caption('Esta aplicacón fue hecha con el propósito de introducir hacia los fenómenos cuánticos, especificamente dentro de la rama de la óptica cuántica, que ha sido de dificil comprensión para la cual nuestro objetivo es demostrar tales fenómenos con ejemplos visuales y prácticos de entender')

page_names = ['Introducción', 'Efecto Fotoeléctrico', 'Ecuaciones de Maxwell', 'Polarización','Experimento de la doble rendija','Difracción','Reflexión','Refracción','Datos extras de las ondas']

Temas = st.sidebar.radio("Escoge el tema",page_names)      


if Temas == 'Introducción':
    st.header('Introducción')
    st.subheader('**¿Qué es la luz?**')
    st.write("Una pregunta que los seres humanos han tratado de responder durante siglos.")
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("newton.png", width=600, caption='Figura No.1 Newton y el estudio de la luz')

    with col3:
        st.write("")

    st.write('Newton, principal aportador de la teoria de la luz estipulaba que las partículas de luz provenian de una fuente luminosa que estimulaba la vista.')
    st.write('Esta idea le permitió justificar las bases de la refracción y reflexión')
    st.write('Durante su vida sostuvó que la luz podría seguir un movimiento ondulatorio lo cual fue demostrado por Thomas Young, que bajo condiciones de difracción los rayos de luz interfieren unos con otros al igual que con las ondas mecánicas')

    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        ("![Alt Text](http://blog.soton.ac.uk/soundwaves/files/2013/12/light1.gif)")

    with col3:
        st.write("")

    #("![Your Awsome GIF](https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif)") 

    st.write('Ahora se sabe que la luz actúa como una onda y una particula, que es a lo que llamamos la naturaleza dual de la luz; la luz sigue principios de electromagnetismo, por lo que decimos que son ondas electromagnéticas.')
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("onda.png", width=450, caption='Onda electromangnética')

    with col3:
        st.write("")

    st.write('Las ondas electromagnéticas pueden ser clasificadas por su longitud de onda o su frecuencia; esta clasificación se llama **Espectro electromagnético**')
    st.image("https://cdn.kastatic.org/ka-perseus-images/01f944ab4471010d09766560f4d1c6da4846d97d.png", caption='Espectro electromagnético')
    st.write('Dentro del espectro electromagnético se encuentra la luz visible, esta es una pequeña parte de todo el espectro que en seres humanos es la única visualizable; arrastra el punto para ver que color se obtiene a diferentes longitudes')
    longitud = st.slider('Longitud de onda visible en nm',380,750,380)
    if longitud < 450:
        st.write('Color Morado')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Morado.png/250px-Morado.png",width=200)
    if 450 < longitud < 495:
        st.write('Color Azul')
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/52/Tipos_de_azules.png",width=200)
    if 495 < longitud < 570:
        st.write('Color Verde')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Tipos_de_verde.png/250px-Tipos_de_verde.png",width=200)
    if 570 < longitud < 590:
        st.write('Color Amarillo')
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/5b/Amarillos.png",width=200)
    if 590 < longitud < 620:
        st.write('Color Naranja')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Shades_of_orange.png/250px-Shades_of_orange.png",width=200)
    if 620 < longitud < 750:
        st.write('Color Rojo')
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Rojos.png/250px-Rojos.png",width=200)

    st.write('No se entendía muy bien el concepto de luz hasta 1900, cuando el físico Max Planck empezó a estudiar cuerpos negros (Objetos teóricos que absorven la energía radiante totalmente), estos se calentaban y empezaban a brillar.')
    st.image("http://nuclear-power.com/wp-content/uploads/blackbody-radiation-chart-min.png",width=700)
    st.write('Planck descubrió que la radiación electromagnética emitida por estos cuerpos no podia ser explicada por la física clásica; que postulaba que la energía podía ser emitida y absorbida por la materia en cualquier cantidad')
    st.write('Un cuerpo negro absorbe energía en modo de calor y emite luz, la física clásica postulaba que el cuerpo tiene la capacidad de absorber la energía hasta emitir ondas electromagnéticas por encima de la luz visible, emitiendo ondas de alta energía como las UV,  de rayos x y gamma')
    st.markdown('![Alt Text](https://steemitimages.com/DQmSXqSXPGdcPQiP3EfaZZQhipbZJg2RsAZmVTpUJvcGetZ/output_final_radiation.gif)')
    st.write('A esto se le llamó la catástrofe ultravioleta')
    st.image("https://slideplayer.es/slide/5497387/17/images/12/LEY+DE+RAYLEIGH-JEANS+Cat%C3%A1strofe+ultravioleta.jpg")
    st.write('Planck observó que la materia absorbía o emitía la energia en multiplos enteros del valor de la constante de Planck, pequeños paquetes conocidos como cuántos, por lo que Einstein propuso su teoría del efecto fotoeléctrico')
    st.latex('h=6.626^{-34}Js')
    st.caption('El efecto fotoeléctrico nos dice que si un electrón absorbe la energía de un fotón y este tiene más energía que la función del trabajo el electrón es arrancado del material, explicando porque los materiales no absorben energia hasta emitir ondas de alta energía')
    st.write('Los fotones pueden ser emitidos o absorbidos por los átomos, se absorben por completo y al momento de que el átomo pierde energía se emiten, cargando con la energía exacta que se perdió la cual es directamente proporcional a su frecuencia.')
    st.write('Eso demostró que la luz se comporta también como una partícula')
    st.write('Esta relación es descrita por la famosa **Ecuación de Planck**:')
    st.latex('E=hf')
    st.caption("*Las frecuencias más altas nos hacen más daño, porque significan más energía")

if Temas == 'Efecto Fotoeléctrico':
    st.header('Efecto Fotoeléctrico')
    st.write("Cuando la luz brilla en un metal,los electrones pueden ser expulsados de la superficie del metal en un fenómeno conocido como el efecto fotoeléctrico.")
    st.write("Debido al efecto fotoeléctrico fue prueba que la luz tiene una dualidad, es decir, se puede comportar como partícula y como onda.")
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("FOTO.png")


    with col3:
        st.write("")
    st.subheader("Modelo propuesto por Einstein")
    st.write("Con base en el modelo ondulatorio de la luz, los físicos predijeron que el aumento de la amplitud de la luz incrementaría la energía cinética de los fotoelectrones emitidos, mientras que el aumento de la frecuencia incrementaría la corriente medida. Contrario a las predicciones, los experimentos mostraron que el aumento en la frecuencia incrementaba la energía cinética de los fotoelectrones, mientras que el aumento en la amplitud de la luz incrementaba la corriente.")
    st.write("Con base en estos descubrimientos, Einstein propuso que la luz se comportaba como una corriente de partículas llamadas fotones con una energía de:")
    st.latex("E= hv")
    st.write("La energía de un fotón es proporcional a la frecuencia de la luz (f) por lo que la amplitud de la luz (h) es proporcional al número de fotones con una frecuencia dada.")
    
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/6/6e/EFECTOFOTOELECTRICOpeq.gif)")

    with col3:
        st.write("")
    
    st.subheader("Bandgap")
    st.write("El bandgap o tambien conocido como banda prohibida es la energía mínima necesaria para excitar un electrón desde su estado ligado a un estado libre que le permita participar en la conducción, dentro de una celda solar. Lo importante a resaltar aqui es el intervalo de banda es la cantidad mínima de energía necesaria para un electrón de liberarse de su estado de enlace. Cuando se cumple la energía de banda prohibida, el electrón es excitado a un estado libre, y por lo tanto puede participar en la conducción.La brecha de banda determina la cantidad de energía que se necesita del sol para la conducción, así como la cantidad de energía que se genera.Un agujero se crea donde el electrón estaba obligado anteriormente. Este agujero también participa en la conducción.")
    
    if st.button("Ver tabla"):
        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.write("")

        with col2:
            st.write("")
            st.write("Anchos de Banda",pd.DataFrame({
            'Material':["PbSe","PbTe","PbS","InN","Ge","GaSb","Si","InP","GaAs", "CdTe", "AlSb","CdSe","AlAs","ZnTe","GaP","CdS","AlP","ZnSe","SiC","GaN","ZnS","Diamante","AlN"],
            'Banda Prohibida en eV':[0.27,0.29,0.37,0.67,0.67,0.7,1.11,1.35,1.43,1.58,1.6,1.73,2.16,2.25,2.26,2.42,2.45,2.7,2.86,3.4,3.6,5.5,6.2],
            }))
        with col3:
            st.write("")
        
    else:
        st.write("")    
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")

    with col2:
        st.image("Banda.png", width=600)
    with col3:
        st.write("")
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.markdown('![Alt Text](https://upload.wikimedia.org/wikipedia/commons/1/1f/Bulkbandstructure.gif)')

    with col3:
        st.write("")
    st.write("Ese “agujero” que participa en la conducción, su movimiento es análogo al movimiento de una burbuja en un líquido. A pesar de que en realidad es el líquido que se mueve, es más fácil para describir el movimiento de la burbuja que va en la dirección opuesta.")
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.markdown('![Alt Text](https://i.pinimg.com/originals/c1/4f/b5/c14fb5f3ad4a890f9296c2f842068463.gif)')

    with col3:
        st.write("")
        
if Temas == 'Ecuaciones de Maxwell':
    st.header("Ecuaciones de Maxwell")
    st.subheader("Ley de Gauss")
    st.latex(r'''
        \overrightarrow{\nabla}* \overrightarrow{E} = \frac{\rho}{\epsilon_0}   
    ''')
    st. write (""" Esta describe como las cargas afectan al campo eléctrico. En concreto te dice que las cargas eléctricas son fuentes de campo eléctrico, si son positivas
    o sumideros de campo eléctrico si son negativas, no es otra cosa que decir en términos
    que cargas del mismo signo repelen y de distinto atraen.
    Captura que el campo eléctrico decae con la distancia y lo hace
    de una manera muy precisa: con el cuadrado de la distancia.""")

    st.write('**¿Para que sirve?**')
    st. write ("""La ley de gauss tiene su máxima utilidad para calcular el campo eléctrico en situaciones donde
    la distribución de carga tiene simetría esférica, cilíndrica o está distribuida uniformemente en un plano o en una placa infinita.""")
    st.image(["images.png","SUPERFICIE CILIDRICA.png"]) 

    st. write ("""Se determina la dirección del campo eléctrico a partir de la
    simetría de la distribución de carga (de la forma de la superfie) uniforme en estos cuerpos
    simétricos y también su magnitud.
    De manera alternativa conociendo el campo eléctrico los alrededores de estas distribuciones simétricas se pudiera
    calcular la carga.
    .""")

    st. write ("""Para calcular el campo eléctrico y su magnitud se utiliza la ley de Gauss:""") 
    st.latex(r'''\oint_s\overrightarrow{E} * d\overrightarrow{s} = \frac{Q_{neta}}{\epsilon_0} ''')

    st. write ("""Va de la mano a este tema para comprender qué es el flujo eléctrico;""") 
    col1, col2, col3 = st.columns([3,6,6])
    with col2:
        st.markdown("![Alt Text](http://3.bp.blogspot.com/-5ryI19Mmm78/USH2VKEzgLI/AAAAAAAACrQ/9OnqCH85ZNE/s400/gauss1.gif)")
        
    st. write ("""
    Imaginemos una superficie plana como la de la imagen, esta
    superficie tiene un área superficial S imaginemos que esta superficie es
    atravesada por líneas de campo eléctrico en este ejemplo en particular imaginemos que ese campo eléctrico es uniforme, para lo cual el flujo eléctrico sería el producto de la magnitud de ese campo eléctrico
    que está atravesando esta superficie por el área superficial por el coseno del ángulo que formaría ese vector campo eléctrico y
    el vector normal n 
    (vector n es un vector que es normal a la
    superficie y forma un ángulo de 90
    grados con la superficie). Esto cuando 
    es uniforme y la superficie es plana.""") 
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image (["Imagen4.png","Imagen5.png"])

    st. write ("""El flujo eléctrico en una superficie general irregular la cual tiene partes curvas es atravesado por infinitas líneas de campo eléctrico, para calcular el flujo eléctrico en este caso tendríamos que dividir la superficie en un gran número de pequeños elementos de área superficial del ts y en este caso el flujo eléctrico sería
    una sumatoria la sumatoria de los productos de las áreas de estos pequeños
    elementos del ts por el campo eléctrico que atraviesa cada uno de esos elementos así el vector que va a tener como módulo el área superficial de ese elemento y ese vector va a ser normal a la superficie va a ser perpendicular y va a
    formar un ángulo con el campo eléctrico.""")
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen7.png")

    st.  write( """La ley de Gauss me indica que el flujo
    eléctrico que pasa a través de cada una
    de estas superficies va a ser igual a la
    carga electrica neta que encierran esas
    superficies entre la constante de
    permeabilidad""")

    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen9.png")

    st.subheader("Ley de Gauss para el magnetismo")

    st.latex(r'''
        \overrightarrow{\nabla}* \overrightarrow{B} = 0 
    ''')

    st. write(""" Esta ley se asemeja a la ley de gauss para campo eléctrico, sin embargo hay que comprender la región en el espacio donde hay interacción de fuerzas magnéticas, vectorial y no causa ningún efecto sobre cargas en reposo.
    Una fuerza magnética es el resultado del producto vectorial de la magnitud de la carga por su velocidad y la intensidad del campo magnético (conocido como la ley y de fuerza de Lorenz):""")

    st.latex(r'''
        \overrightarrow{F} = q * \overrightarrow{v}x\overrightarrow{B} 
    ''')

    st.write ("""Flujo magnético. - A diferencia del eléctrico se define como el número de líneas de campo magnético que atraviesan en el espacio (medido en teslas por metro cuadrado).""")
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen11.png")

    st. write ("""Esta se fundamenta en que las fuentes y sumideros del campo magnético no existen. No hay cargas magnéticas.""")

    st. write (""" Eso no quiere decir que no haya objetos que puedan crear campos magnéticos (eso
    lo hacen los imanes).
    La cosa es que al no haber ni fuentes ni sumideros, el campo magnético siempre debe “cerrarse”
    sobre si mismo.
    Por ejemplo, si intentas partir un imán en dos queriendo separarlo en dos monopolos,
    el campo se cierra en la zona que has cortado, devolviendote dos imanes con dos polos cada
    uno. 
    En nuestro mundo los monopolos son imposibles (si existieran las ecuaciones de Maxwell podrian ser expresadas en una sola ecuación.""")
    st.subheader("Ley de Faraday y Lenz")
    st.latex(r'''
        \overrightarrow{\nabla}* \overrightarrow{E} = -\frac{\partial \overrightarrow{B}}{\partial t}   
    ''')

    st. write ("""De esta ley está el principio básico detrás
    de casi todas las centrales eléctricas del planeta, nos dice que si
    un campo magnético cambia en el tiempo esto activa el campo eléctrico de una manera precisa:
    cerrándose.""")

    col1, col2, col3 = st.columns([2,6,2])
    with col2:
        ("![FLUJO MAGNETICO](https://images.hive.blog/DQmQNxXF7hx7oztpu9CRZvqt7bF18G2EBZfKnYJfjQnVEPX/Electromagnetic_induction_-_solenoid_to_loop_-_animation%20(1).gif)")


    st. write ("""Concretamente si el campo magnético aumenta, el eléctrico se orienta en el sentido de
    las agujas del reloj, si decrece se orienta al contrario.
    En definitiva, no solo cargas e imanes pueden influir en los campos,
    también pueden hacerlo entre ellos.""")

    st. write ("""Eso es lo que encapsula la cuarta ecuación:""")
    st.subheader("La ley de Ampére")

    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen13.png")

    st. write ("""Un campo eléctrico
    cambiando en el tiempo o cargas moviéndose, es decir una corriente eléctrica, activan
    el campo magnético (cerrándose, como tiene que ser).
    """)

    st.latex(r'''
        \overrightarrow{\nabla}* \overrightarrow{E} = \mu_0 \overrightarrow{J} +\mu_0 \epsilon_0 \frac{\partial \overrightarrow{E}}{\partial t}   
    ''')
    st.write("""Nos permite calcular los campos
    magnéticos generados en los alrededores
    de distribuciones de corriente que
    pueden ser uniformes o variables.""")
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen14.png")

    st.subheader ("""**Corriente circular**""")

    st.write("""Imaginemos un conductor de sección transversal
    circular que envia corriente con lo que se va a generar
    alrededor de este una línea circular de campo magnético,  
    muchas líneas que se van a generar fuera del conductor e
    internamente también se van a generar líneas de campo magnético en el campo
    magnético que se genera en esta línea
    circular interna va a ser distinto al
    campo magnético que se genera en esta
    línea circular externa (posible calcular con la ecuación anterior).""") 

    st. write("""La sección transversal del conductor es circular pero puede tener cualquier otra forma irregular.""")
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen16.png")

    st. write ("""Basta con hacer pasar una corriente eléctrica por una bobina con la forma apropiada para
    tener un campo magnético, cuanto más intensa sea la corriente más intenso es el campo magnético.
    Esto es un electroimán y la mayoría de los campos magnéticos del mundo se generan con
    ellos, incluido el que nos protege del viento solar.""")

    st.write("""Momentos en que se aplica la Ley de Ampére:""")
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen15.png")

if Temas == 'Polarización':
    st.header("Polarización")
    st.write("La polarización es una propiedad de la luz, que describe la geometría interna de una fuente de radiación")
    st.subheader("La luz:")
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.markdown("![Alt Text](https://www.liceoagb.es/quimigen/imagenes/ondaelectromagnetica1.gif)")
    st.write("La luz son ondas electromagneticas, visible al ojo humano,estas ondas vibran en diferentes direcciones perpendiculares en forma de propagación hasta que estas son sometidas a la polarizacion")
    st.subheader("Luz polarizada:")
    st.write("las ondas de luz vibran en un solo plano, esto se produce gracias a la ayuda de un polarizador")
    
    col1, col2, col3 = st.columns([1,6,1])
    
    with col2:
        st.markdown("![Alt Text](http://www.juliohernandezfotografia.cl/wp-content/uploads/2015/10/luz-polarizador.gif)")
    st.subheader("Polarizador:")
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.image("https://www.lifeder.com/wp-content/uploads/2019/04/680px-Wire-grid-polarizer2.jpg")
    botones_vector = ['Lineal','Circular','Elíptica']
    vectores = st.radio ('Tipo de polarizacion',botones_vector)
    if vectores == 'Lineal':
        st.write("El vector E traza sobre el plano perpendicular a la dirección de propagación una linea recta.")
    if vectores == 'Circular':
        st.write('Componentes de E misma magnitud, pero una diferencia de fase, puede verse girando a la izquierda o hacia la derecha.')
    if vectores == 'Elíptica':
        st.write('Componentes de E son diferentes, abarca cualquier diferencia de magnitud de fase de Ex y Ey, es el estado de polarización más general.') 

if Temas == 'Experimento de la doble rendija':
    st.header('Experimento de la doble rendija')
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        ("![Interferencia](https://i.gifer.com/2V7i.gif)")

    with col3:
        st.write("")
    st.subheader('Interferencia')
    st.write('La luz, como las ondas mecánicas puede presentar interferencia; existen dos tipos: la **Interferencia Constructiva** y la **Interferencia Destructiva**')
    st.write('En la interferencia constructiva la amplitud de la onda resultante es mayor que una u otra onda individual, mientras que en la interferencia destructiva la amplitud resultante es menor que la onda mas grande.')
    st.write('Toda interferencia asociada con ondas de luz aparece cuando se combinan los campos electromagnéticos que constituyen las ondas individuales')
    ("Interferencia Constructiva vs Destructiva","![Interferencia](https://i.gifer.com/Q1JF.gif)")
    st.write('Cuando dos ondas oscilan de manera opuesta se da una interferencia destructiva todal y cuando hay dos con la misma o casi la misma amplitud oscilando de manera simétrica hay interferencia contructiva total')
    st.subheader("Experimento de la doble rendija de Young")
    st.write('La interferencia en ondas de luz provinientes de dos fuentes fue demostrada por Thomas Young')
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        ("![doble rendija](http://mrtremblaycambridge.weebly.com/uploads/9/7/8/8/9788395/656047_orig.gif)")

    with col3:
        st.write("")
    
    st.write('Las líneas más largas al inicio son picos de ondas, que al chocar con las rendijas forman otras otras; cuando las ondas formadas salen de las rendijas crean interferencias las cuales aumentan y disminuyen la luz en ciertos patrones, donde se entrelazan las lineas es donde se forma la interferencia contructiva por la superposicion de las ondas, en cambio cuando los valles chocan con los picos se presenta una interferencia destructiva, disminuyendo la intensidad de la luz en esa zona')
    st.write('En la siguiente imagen se observa un patron de interferencia formado por un láser')
    st.image("data:image/jpeg;base64,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", "Patrón de interferencia", width=700)
    st.write('Un Ejemplo')
    st.write('Una luz de longitud de onda de 700nm brilla a través de una rendija doble donde sus hoyos son 200nm de largo y están separadas por 1,300nm. Si una pantalla esta colocada a "Distancia de separacón" de las rendijas¿Cuál va a ser la distancia del punto más brilloso central al siguiente punto de luz?')
    st.write('Respuesta:')
    st.image("Distancia.jpg")
    xm = st.number_input('Escoge los metros de separación', min_value=1,max_value=100)
    Distancia = xm*0.6387891
    st.text("Nota: a diferentes distancias la imagen cambia, trata con 10, 30, 50 y 80 metros ")
    st.write("La distancia entre el punto de luz central y el siguiente es de", Distancia, "Metros")
    if Distancia < 15:
        st.image("1.jpg")
    else:
        st.write("")
    if 15 < Distancia < 30:
        st.image("2.jpg")
    else:
        st.write("")
    if 30 < Distancia < 45:
        st.image("3.jpg")
    else:
        st.write("")
    if 45 < Distancia <64:
        st.image("4.jpg")
    else:
        st.write("")  
      
if Temas == 'Difracción':
    st.header("Difracción")
    st.write("La difracción se presenta cuando una onda se distorsiona al pasar por un obstáculo como una pantalla con una pequeña apertura")
    ("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/2/21/One_wave_slit_diffraction_dirichlet_bw.gif)")
    st.write("Mientras mas hoyos tenga la pared por donde pasa más notorio va a ser la interferencia constructivamente.")
    st.write("Cuando hay muchos puntos y se ve todo más claro lo llamamos **Red de difracción**")
    st.image("https://www.researchgate.net/publication/332921550/figure/fig1/AS:756117697224705@1557283915708/FIGURA-5-a-b-c-Patrones-de-difraccion-de-convolucion-grabados-en-la-region-de.ppm", width=700)
    st.write("Pero **¿Por qué las ondas se difractan cuando pasan por un hoyo?**")
    st.write("Por algo que llamamos el **Principio de Huygens**, el cual nos dice que una onda se puede dividir en muchas difracciones que por interferencia forman la misma onda, por lo tanto si pasa por un hoyo o una rendija, esas divisiones de la onda original van a presentar interferencias, formando un patron de inferferencia")
    st.write("Si la distancia del hoyo des mas grande a la longitud de la onda, los rayos siguen en una trayectoria en línea recta, si la distancia es muy similar a la longitud, esta se extiende al pasar por la apertura y finalmente si la distancia es menor a la longitud, la apertura se comporta como fuente puntual que emite ondas esféricas")
    st.image("Aperturas.png")
    if st.button("Aplicaciones de patrones de Difracción"):
        st.write("Los patrones de difracción han sido utilizados para analizar las formas de las moléculas")
        st.write("Un gran ejemplo es la ganadora del premio novel de química **Dorothy Hodgkin**")
        st.image("https://mujeresconciencia.com/app/uploads/2016/05/Dorothy_Hodgkin.jpg")
        st.write("Ella determinó la estructura de la Penicilina y la Vitamina B12 por medio de cristalografía de rayos x")
        st.write("Esto dió lugar a otros analisis de patrones de difracción como el de las proteínas y otras moléculas, estos se realizan poniendo la muestra cristalina y sometiendola a un rayo de alta intensidad que por lo general suele ser de rayos x")
    if st.button("Patrones de difracción"):
        st.image("https://cnx.org/resources/20b4b8e0168690b7c97c936d8ee8c5c2a2f1ada9/Diffraction", caption="Patrón de difracción de una enzima")
        st.image("https://cnx.org/resources/f7d9cce4d6aa00fbae13d576252dde7545f29c97/Powder", caption="Patrón de difracción del silicio")
    if st.button("Cristales de moléculas"):
        st.image("https://cnx.org/resources/bbab3410b756781b28bfd38b9d293525b9f76368/Insulin%20crystals", caption="Cristales de insulina")
        st.image("https://cnx.org/resources/9491193edbd0ab2e784b580c295c4ce2328002fe/Chrome%20alum", caption="Cristales de Alumbre de cromo")
        st.image("https://cnx.org/resources/5f2097426608b73d32edc90a1a2fb3116a3d1211/Twinned%20crystal", caption="Cristales de Cuarzo")

if Temas == 'Reflexión':
    st.header("Reflexión")
    st.write("**¿Qué es la reflexión?**")
    st.image("https://images.squarespace-cdn.com/content/v1/5ca5fea877b90374d82c2908/1557313538336-0MMOHZP98Z9JSH0C9FU0/pexels-photo-220429.jpeg?format=1000w")
    st.write("La reflexión es el cambio de dirección de una onda electromagnética al entrar en contracto con una superficie de otro medio, por ejemplo el agua o el vidrio")
    st.image(width=700,"data:image/jpeg;base64,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")
    st.write("Existen dos tipos de reflexión; **La reflexión Especular** y **La reflexión Difusa**")
    st.write("En la reflexión especular el angulo de incidencia siempre es el mismo que el reflejado y lo que no refleja la luz por asi decirlo, es reflexión difusa")
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/dd/Reflexi%C3%B3n_especular_y_difusa.gif", caption="Tipos de reflexión")
    st.write("Los colores pueden ser explicados por los electrones, ta que cada átomo tiene su manera de reflejar la luz, cuando absorben la luz entran en un estado exitado y después de un rato se regresan a su nivel de energía original al emitir un protón")
    st.write("El fotón emitido tiene cierta frecuencia, si se mueve a diferentes niveles de energía explicaría diferentes colores")
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Lambert2.gif", caption="Reflexión Difusa")

if Temas == 'Refracción':
    st.header("Refraccion")
    st.write("")

if Temas == 'Datos extras de las ondas':
    st.header("Datos extras de las ondas")
    st.write("**¿Por qué las ondas de microondas no están enseguida de las ultravioletas si son capaces de causarnos daño?**")
    st.write("La microondas emiten ondas que hacen vibrar las párticulas del agua aumentando su temperatura mientras que las ondas de rayos x y UV cargan tanta energía quer son capaces de romper los enlaces de tus moléculas, la exposición continua a estas puede causar cáncer")
    st.write("Las ondas con freciencias menores nos afectan por como hacen vibrar las moléculas del agua ya que resonan de la misma manera de la vibración del agua")
    st.write("Nuestro cuerpo está formado en un ambiente donde las ondas EM visibles son abundantes, por lo tanto no nos afectan.")
    st.write("**¿De dónde salen las ondas electromagnéticas?**")
    st.write("Las ondas son la propagación de una perturbación en el campo electromagnético causado por la vibración de cargas.")
    st.write("Considera un par de cargas en el espacio; después al mover una de ellas la otra no se -percata- instantaneamente del cambio, esa información le va a llegar a la velocidad de la luz, cada vez que tienes una carga vibrando en una frecuencia alta, empieza a perturbar el campo electromagnético en forma de ondas")
    st.write("**¿Cómo es que se comporta como una párticula y como una onda?**")
    st.write("En algunos instantes vemos la luz comportandose como una onda en la refracción, interferencia y a veces como partículas como en el efecto fotoeléctrico")


