import pandas as pd
import streamlit as st
import numpy as np
import math

st.set_page_config(page_title="脫ptica Cu谩ntica",page_icon="馃巼")

st.caption('Esta aplicac贸n fue hecha con el prop贸sito de introducir hacia los fen贸menos cu谩nticos, especificamente dentro de la rama de la 贸ptica cu谩ntica, que ha sido de dificil comprensi贸n para la cual nuestro objetivo es demostrar tales fen贸menos con ejemplos visuales y pr谩cticos de entender')
st.header("脫ptica Cu谩ntica")
page_names = ['Introducci贸n', 'Efecto Fotoel茅ctrico', 'Ecuaciones de Maxwell', 'Polarizaci贸n','Experimento de la doble rendija','Difracci贸n','Reflexi贸n','Refracci贸n','Datos extras de las ondas','Informaci贸n Integrantes']

Temas = st.sidebar.radio("Escoge el tema",page_names)      


if Temas == 'Introducci贸n':
    st.header('Introducci贸n')
    st.subheader('**驴Qu茅 es la luz?**')
    st.write("Una pregunta que los seres humanos han tratado de responder durante siglos.")
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("newton.png", width=600, caption='Figura No.1 Newton y el estudio de la luz')

    with col3:
        st.write("")

    st.write('Newton, principal aportador de la teoria de la luz estipulaba que las part铆culas de luz provenian de una fuente luminosa que estimulaba la vista.')
    st.write('Esta idea le permiti贸 justificar las bases de la refracci贸n y reflexi贸n')
    st.write('Durante su vida sostuv贸 que la luz podr铆a seguir un movimiento ondulatorio lo cual fue demostrado por Thomas Young, que bajo condiciones de difracci贸n los rayos de luz interfieren unos con otros al igual que con las ondas mec谩nicas')

    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        ("![Alt Text](http://blog.soton.ac.uk/soundwaves/files/2013/12/light1.gif)")

    with col3:
        st.write("")

    #("![Your Awsome GIF](https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif)") 

    st.write('Ahora se sabe que la luz act煤a como una onda y una particula, que es a lo que llamamos la naturaleza dual de la luz; la luz sigue principios de electromagnetismo, por lo que decimos que son ondas electromagn茅ticas.')
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("onda.png", width=450, caption='Onda electromangn茅tica')

    with col3:
        st.write("")

    st.write('Las ondas electromagn茅ticas pueden ser clasificadas por su longitud de onda o su frecuencia; esta clasificaci贸n se llama **Espectro electromagn茅tico**')
    st.image("https://cdn.kastatic.org/ka-perseus-images/01f944ab4471010d09766560f4d1c6da4846d97d.png", caption='Espectro electromagn茅tico')
    st.write('Dentro del espectro electromagn茅tico se encuentra la luz visible, esta es una peque帽a parte de todo el espectro que en seres humanos es la 煤nica visualizable; arrastra el punto para ver que color se obtiene a diferentes longitudes')
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

    st.write('No se entend铆a muy bien el concepto de luz hasta 1900, cuando el f铆sico Max Planck empez贸 a estudiar cuerpos negros (Objetos te贸ricos que absorven la energ铆a radiante totalmente), estos se calentaban y empezaban a brillar.')
    st.image("http://nuclear-power.com/wp-content/uploads/blackbody-radiation-chart-min.png",width=700)
    st.write('Planck descubri贸 que la radiaci贸n electromagn茅tica emitida por estos cuerpos no podia ser explicada por la f铆sica cl谩sica; que postulaba que la energ铆a pod铆a ser emitida y absorbida por la materia en cualquier cantidad')
    st.write('Un cuerpo negro absorbe energ铆a en modo de calor y emite luz, la f铆sica cl谩sica postulaba que el cuerpo tiene la capacidad de absorber la energ铆a hasta emitir ondas electromagn茅ticas por encima de la luz visible, emitiendo ondas de alta energ铆a como las UV,  de rayos x y gamma')
    st.markdown('![Alt Text](https://steemitimages.com/DQmSXqSXPGdcPQiP3EfaZZQhipbZJg2RsAZmVTpUJvcGetZ/output_final_radiation.gif)')
    st.write('A esto se le llam贸 la cat谩strofe ultravioleta')
    st.image("https://slideplayer.es/slide/5497387/17/images/12/LEY+DE+RAYLEIGH-JEANS+Cat%C3%A1strofe+ultravioleta.jpg")
    st.write('Planck observ贸 que la materia absorb铆a o emit铆a la energia en multiplos enteros del valor de la constante de Planck, peque帽os paquetes conocidos como cu谩ntos, por lo que Einstein propuso su teor铆a del efecto fotoel茅ctrico')
    st.latex('h=6.626^{-34}Js')
    st.caption('El efecto fotoel茅ctrico nos dice que si un electr贸n absorbe la energ铆a de un fot贸n y este tiene m谩s energ铆a que la funci贸n del trabajo el electr贸n es arrancado del material, explicando porque los materiales no absorben energia hasta emitir ondas de alta energ铆a')
    st.write('Los fotones pueden ser emitidos o absorbidos por los 谩tomos, se absorben por completo y al momento de que el 谩tomo pierde energ铆a se emiten, cargando con la energ铆a exacta que se perdi贸 la cual es directamente proporcional a su frecuencia.')
    st.write('Eso demostr贸 que la luz se comporta tambi茅n como una part铆cula')
    st.write('Esta relaci贸n es descrita por la famosa **Ecuaci贸n de Planck**:')
    st.latex('E=hf')
    st.caption("*Las frecuencias m谩s altas nos hacen m谩s da帽o, porque significan m谩s energ铆a")

if Temas == 'Efecto Fotoel茅ctrico':
    st.header('Efecto Fotoel茅ctrico')
    st.write("Cuando la luz brilla en un metal,los electrones pueden ser expulsados de la superficie del metal en un fen贸meno conocido como el efecto fotoel茅ctrico.")
    st.write("Debido al efecto fotoel茅ctrico fue prueba que la luz tiene una dualidad, es decir, se puede comportar como part铆cula y como onda.")
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("FOTO.png")


    with col3:
        st.write("")
    st.subheader("Modelo propuesto por Einstein")
    st.write("Con base en el modelo ondulatorio de la luz, los f铆sicos predijeron que el aumento de la amplitud de la luz incrementar铆a la energ铆a cin茅tica de los fotoelectrones emitidos, mientras que el aumento de la frecuencia incrementar铆a la corriente medida. Contrario a las predicciones, los experimentos mostraron que el aumento en la frecuencia incrementaba la energ铆a cin茅tica de los fotoelectrones, mientras que el aumento en la amplitud de la luz incrementaba la corriente.")
    st.write("Con base en estos descubrimientos, Einstein propuso que la luz se comportaba como una corriente de part铆culas llamadas fotones con una energ铆a de:")
    st.latex("E= hv")
    st.write("La energ铆a de un fot贸n es proporcional a la frecuencia de la luz (f) por lo que la amplitud de la luz (h) es proporcional al n煤mero de fotones con una frecuencia dada.")
    
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/6/6e/EFECTOFOTOELECTRICOpeq.gif)")

    with col3:
        st.write("")
    
    st.subheader("Bandgap")
    st.write("El bandgap o tambien conocido como banda prohibida es la energ铆a m铆nima necesaria para excitar un electr贸n desde su estado ligado a un estado libre que le permita participar en la conducci贸n, dentro de una celda solar. Lo importante a resaltar aqui es el intervalo de banda es la cantidad m铆nima de energ铆a necesaria para un electr贸n de liberarse de su estado de enlace. Cuando se cumple la energ铆a de banda prohibida, el electr贸n es excitado a un estado libre, y por lo tanto puede participar en la conducci贸n.La brecha de banda determina la cantidad de energ铆a que se necesita del sol para la conducci贸n, as铆 como la cantidad de energ铆a que se genera.Un agujero se crea donde el electr贸n estaba obligado anteriormente. Este agujero tambi茅n participa en la conducci贸n.")
    
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
    st.write("Ese 鈥渁gujero鈥? que participa en la conducci贸n, su movimiento es an谩logo al movimiento de una burbuja en un l铆quido. A pesar de que en realidad es el l铆quido que se mueve, es m谩s f谩cil para describir el movimiento de la burbuja que va en la direcci贸n opuesta.")
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
    st. write (""" Esta describe como las cargas afectan al campo el茅ctrico. En concreto te dice que las cargas el茅ctricas son fuentes de campo el茅ctrico, si son positivas
    o sumideros de campo el茅ctrico si son negativas, no es otra cosa que decir en t茅rminos
    que cargas del mismo signo repelen y de distinto atraen.
    Captura que el campo el茅ctrico decae con la distancia y lo hace
    de una manera muy precisa: con el cuadrado de la distancia.""")

    st.write('**驴Para que sirve?**')
    st. write ("""La ley de gauss tiene su m谩xima utilidad para calcular el campo el茅ctrico en situaciones donde
    la distribuci贸n de carga tiene simetr铆a esf茅rica, cil铆ndrica o est谩 distribuida uniformemente en un plano o en una placa infinita.""")
    st.image(["images.png","SUPERFICIE CILIDRICA.png"]) 

    st. write ("""Se determina la direcci贸n del campo el茅ctrico a partir de la
    simetr铆a de la distribuci贸n de carga (de la forma de la superfie) uniforme en estos cuerpos
    sim茅tricos y tambi茅n su magnitud.
    De manera alternativa conociendo el campo el茅ctrico los alrededores de estas distribuciones sim茅tricas se pudiera
    calcular la carga.
    .""")

    st. write ("""Para calcular el campo el茅ctrico y su magnitud se utiliza la ley de Gauss:""") 
    st.latex(r'''\oint_s\overrightarrow{E} * d\overrightarrow{s} = \frac{Q_{neta}}{\epsilon_0} ''')

    st. write ("""Va de la mano a este tema para comprender qu茅 es el flujo el茅ctrico;""") 
    col1, col2, col3 = st.columns([3,6,6])
    with col2:
        st.markdown("![Alt Text](http://3.bp.blogspot.com/-5ryI19Mmm78/USH2VKEzgLI/AAAAAAAACrQ/9OnqCH85ZNE/s400/gauss1.gif)")
        
    st. write ("""
    Imaginemos una superficie plana como la de la imagen, esta
    superficie tiene un 谩rea superficial S imaginemos que esta superficie es
    atravesada por l铆neas de campo el茅ctrico en este ejemplo en particular imaginemos que ese campo el茅ctrico es uniforme, para lo cual el flujo el茅ctrico ser铆a el producto de la magnitud de ese campo el茅ctrico
    que est谩 atravesando esta superficie por el 谩rea superficial por el coseno del 谩ngulo que formar铆a ese vector campo el茅ctrico y
    el vector normal n 
    (vector n es un vector que es normal a la
    superficie y forma un 谩ngulo de 90
    grados con la superficie). Esto cuando 
    es uniforme y la superficie es plana.""") 
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image (["Imagen4.png","Imagen5.png"])

    st. write ("""El flujo el茅ctrico en una superficie general irregular la cual tiene partes curvas es atravesado por infinitas l铆neas de campo el茅ctrico, para calcular el flujo el茅ctrico en este caso tendr铆amos que dividir la superficie en un gran n煤mero de peque帽os elementos de 谩rea superficial del ts y en este caso el flujo el茅ctrico ser铆a
    una sumatoria la sumatoria de los productos de las 谩reas de estos peque帽os
    elementos del ts por el campo el茅ctrico que atraviesa cada uno de esos elementos as铆 el vector que va a tener como m贸dulo el 谩rea superficial de ese elemento y ese vector va a ser normal a la superficie va a ser perpendicular y va a
    formar un 谩ngulo con el campo el茅ctrico.""")
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen7.png")

    st.  write( """La ley de Gauss me indica que el flujo
    el茅ctrico que pasa a trav茅s de cada una
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

    st. write(""" Esta ley se asemeja a la ley de gauss para campo el茅ctrico, sin embargo hay que comprender la regi贸n en el espacio donde hay interacci贸n de fuerzas magn茅ticas, vectorial y no causa ning煤n efecto sobre cargas en reposo.
    Una fuerza magn茅tica es el resultado del producto vectorial de la magnitud de la carga por su velocidad y la intensidad del campo magn茅tico (conocido como la ley y de fuerza de Lorenz):""")

    st.latex(r'''
        \overrightarrow{F} = q * \overrightarrow{v}x\overrightarrow{B} 
    ''')

    st.write ("""Flujo magn茅tico. - A diferencia del el茅ctrico se define como el n煤mero de l铆neas de campo magn茅tico que atraviesan en el espacio (medido en teslas por metro cuadrado).""")
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen11.png")

    st. write ("""Esta se fundamenta en que las fuentes y sumideros del campo magn茅tico no existen. No hay cargas magn茅ticas.""")

    st. write (""" Eso no quiere decir que no haya objetos que puedan crear campos magn茅ticos (eso
    lo hacen los imanes).
    La cosa es que al no haber ni fuentes ni sumideros, el campo magn茅tico siempre debe 鈥渃errarse鈥?
    sobre si mismo.
    Por ejemplo, si intentas partir un im谩n en dos queriendo separarlo en dos monopolos,
    el campo se cierra en la zona que has cortado, devolviendote dos imanes con dos polos cada
    uno. 
    En nuestro mundo los monopolos son imposibles (si existieran las ecuaciones de Maxwell podrian ser expresadas en una sola ecuaci贸n.""")
    st.subheader("Ley de Faraday y Lenz")
    st.latex(r'''
        \overrightarrow{\nabla}* \overrightarrow{E} = -\frac{\partial \overrightarrow{B}}{\partial t}   
    ''')

    st. write ("""De esta ley est谩 el principio b谩sico detr谩s
    de casi todas las centrales el茅ctricas del planeta, nos dice que si
    un campo magn茅tico cambia en el tiempo esto activa el campo el茅ctrico de una manera precisa:
    cerr谩ndose.""")

    col1, col2, col3 = st.columns([2,6,2])
    with col2:
        ("![FLUJO MAGNETICO](https://images.hive.blog/DQmQNxXF7hx7oztpu9CRZvqt7bF18G2EBZfKnYJfjQnVEPX/Electromagnetic_induction_-_solenoid_to_loop_-_animation%20(1).gif)")


    st. write ("""Concretamente si el campo magn茅tico aumenta, el el茅ctrico se orienta en el sentido de
    las agujas del reloj, si decrece se orienta al contrario.
    En definitiva, no solo cargas e imanes pueden influir en los campos,
    tambi茅n pueden hacerlo entre ellos.""")

    st. write ("""Eso es lo que encapsula la cuarta ecuaci贸n:""")
    st.subheader("La ley de Amp茅re")

    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen13.png")

    st. write ("""Un campo el茅ctrico
    cambiando en el tiempo o cargas movi茅ndose, es decir una corriente el茅ctrica, activan
    el campo magn茅tico (cerr谩ndose, como tiene que ser).
    """)

    st.latex(r'''
        \overrightarrow{\nabla}* \overrightarrow{E} = \mu_0 \overrightarrow{J} +\mu_0 \epsilon_0 \frac{\partial \overrightarrow{E}}{\partial t}   
    ''')
    st.write("""Nos permite calcular los campos
    magn茅ticos generados en los alrededores
    de distribuciones de corriente que
    pueden ser uniformes o variables.""")
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen14.png")

    st.subheader ("""**Corriente circular**""")

    st.write("""Imaginemos un conductor de secci贸n transversal
    circular que envia corriente con lo que se va a generar
    alrededor de este una l铆nea circular de campo magn茅tico,  
    muchas l铆neas que se van a generar fuera del conductor e
    internamente tambi茅n se van a generar l铆neas de campo magn茅tico en el campo
    magn茅tico que se genera en esta l铆nea
    circular interna va a ser distinto al
    campo magn茅tico que se genera en esta
    l铆nea circular externa (posible calcular con la ecuaci贸n anterior).""") 

    st. write("""La secci贸n transversal del conductor es circular pero puede tener cualquier otra forma irregular.""")
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen16.png")

    st. write ("""Basta con hacer pasar una corriente el茅ctrica por una bobina con la forma apropiada para
    tener un campo magn茅tico, cuanto m谩s intensa sea la corriente m谩s intenso es el campo magn茅tico.
    Esto es un electroim谩n y la mayor铆a de los campos magn茅ticos del mundo se generan con
    ellos, incluido el que nos protege del viento solar.""")

    st.write("""Momentos en que se aplica la Ley de Amp茅re:""")
    col1, col2, col3 = st.columns([6,6,6])
    with col2:
        st.image ("Imagen15.png")

if Temas == 'Polarizaci贸n':
    st.header("Polarizaci贸n")
    st.write("La polarizaci贸n es una propiedad de la luz, que describe la geometr铆a interna de una fuente de radiaci贸n")
    st.subheader("La luz:")
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.markdown("![Alt Text](https://www.liceoagb.es/quimigen/imagenes/ondaelectromagnetica1.gif)")
    st.write("La luz son ondas electromagneticas, visible al ojo humano,estas ondas vibran en diferentes direcciones perpendiculares en forma de propagaci贸n hasta que estas son sometidas a la polarizacion")
    st.subheader("Luz polarizada:")
    st.write("las ondas de luz vibran en un solo plano, esto se produce gracias a la ayuda de un polarizador")
    
    col1, col2, col3 = st.columns([1,6,1])
    
    with col2:
        st.markdown("![Alt Text](http://www.juliohernandezfotografia.cl/wp-content/uploads/2015/10/luz-polarizador.gif)")
    st.subheader("Polarizador:")
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.image("https://www.lifeder.com/wp-content/uploads/2019/04/680px-Wire-grid-polarizer2.jpg")
    botones_vector = ['Lineal','Circular','El铆ptica']
    vectores = st.radio ('Tipo de polarizacion',botones_vector)
    if vectores == 'Lineal':
        st.write("El vector E traza sobre el plano perpendicular a la direcci贸n de propagaci贸n una linea recta.")
    if vectores == 'Circular':
        st.write('Componentes de E misma magnitud, pero una diferencia de fase, puede verse girando a la izquierda o hacia la derecha.')
    if vectores == 'El铆ptica':
        st.write('Componentes de E son diferentes, abarca cualquier diferencia de magnitud de fase de Ex y Ey, es el estado de polarizaci贸n m谩s general.') 

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
    st.write('La luz, como las ondas mec谩nicas puede presentar interferencia; existen dos tipos: la **Interferencia Constructiva** y la **Interferencia Destructiva**')
    st.write('En la interferencia constructiva la amplitud de la onda resultante es mayor que una u otra onda individual, mientras que en la interferencia destructiva la amplitud resultante es menor que la onda mas grande.')
    st.write('Toda interferencia asociada con ondas de luz aparece cuando se combinan los campos electromagn茅ticos que constituyen las ondas individuales')
    ("Interferencia Constructiva vs Destructiva","![Interferencia](https://i.gifer.com/Q1JF.gif)")
    st.write('Cuando dos ondas oscilan de manera opuesta se da una interferencia destructiva todal y cuando hay dos con la misma o casi la misma amplitud oscilando de manera sim茅trica hay interferencia contructiva total')
    st.subheader("Experimento de la doble rendija de Young")
    st.write('La interferencia en ondas de luz provinientes de dos fuentes fue demostrada por Thomas Young')
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        ("![doble rendija](http://mrtremblaycambridge.weebly.com/uploads/9/7/8/8/9788395/656047_orig.gif)")

    with col3:
        st.write("")
    
    st.write('Las l铆neas m谩s largas al inicio son picos de ondas, que al chocar con las rendijas forman otras otras; cuando las ondas formadas salen de las rendijas crean interferencias las cuales aumentan y disminuyen la luz en ciertos patrones, donde se entrelazan las lineas es donde se forma la interferencia contructiva por la superposicion de las ondas, en cambio cuando los valles chocan con los picos se presenta una interferencia destructiva, disminuyendo la intensidad de la luz en esa zona')
    st.write('En la siguiente imagen se observa un patron de interferencia formado por un l谩ser')
    st.image("data:image/jpeg;base64,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", "Patr贸n de interferencia", width=700)
    st.write('Un Ejemplo')
    st.write('Una luz de longitud de onda de 700nm brilla a trav茅s de una rendija doble donde sus hoyos son 200nm de largo y est谩n separadas por 1,300nm. Si una pantalla esta colocada a "Distancia de separac贸n" de las rendijas驴Cu谩l va a ser la distancia del punto m谩s brilloso central al siguiente punto de luz?')
    st.write('Respuesta:')
    st.image("Distancia.jpg")
    xm = st.number_input('Escoge los metros de separaci贸n', min_value=1,max_value=100)
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
      
if Temas == 'Difracci贸n':
    st.header("Difracci贸n")
    st.write("La difracci贸n se presenta cuando una onda se distorsiona al pasar por un obst谩culo como una pantalla con una peque帽a apertura")
    ("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/2/21/One_wave_slit_diffraction_dirichlet_bw.gif)")
    st.write("Mientras mas hoyos tenga la pared por donde pasa m谩s notorio va a ser la interferencia constructivamente.")
    st.write("Cuando hay muchos puntos y se ve todo m谩s claro lo llamamos **Red de difracci贸n**")
    st.image("https://www.researchgate.net/publication/332921550/figure/fig1/AS:756117697224705@1557283915708/FIGURA-5-a-b-c-Patrones-de-difraccion-de-convolucion-grabados-en-la-region-de.ppm", width=700)
    st.write("Pero **驴Por qu茅 las ondas se difractan cuando pasan por un hoyo?**")
    st.write("Por algo que llamamos el **Principio de Huygens**, el cual nos dice que una onda se puede dividir en muchas difracciones que por interferencia forman la misma onda, por lo tanto si pasa por un hoyo o una rendija, esas divisiones de la onda original van a presentar interferencias, formando un patron de inferferencia")
    st.write("Si la distancia del hoyo des mas grande a la longitud de la onda, los rayos siguen en una trayectoria en l铆nea recta, si la distancia es muy similar a la longitud, esta se extiende al pasar por la apertura y finalmente si la distancia es menor a la longitud, la apertura se comporta como fuente puntual que emite ondas esf茅ricas")
    st.image("Aperturas.png")
    if st.button("Aplicaciones de patrones de Difracci贸n"):
        st.write("Los patrones de difracci贸n han sido utilizados para analizar las formas de las mol茅culas")
        st.write("Un gran ejemplo es la ganadora del premio novel de qu铆mica **Dorothy Hodgkin**")
        st.image("https://mujeresconciencia.com/app/uploads/2016/05/Dorothy_Hodgkin.jpg")
        st.write("Ella determin贸 la estructura de la Penicilina y la Vitamina B12 por medio de cristalograf铆a de rayos x")
        st.write("Esto di贸 lugar a otros analisis de patrones de difracci贸n como el de las prote铆nas y otras mol茅culas, estos se realizan poniendo la muestra cristalina y sometiendola a un rayo de alta intensidad que por lo general suele ser de rayos x")
    if st.button("Patrones de difracci贸n"):
        st.image("https://cnx.org/resources/20b4b8e0168690b7c97c936d8ee8c5c2a2f1ada9/Diffraction", caption="Patr贸n de difracci贸n de una enzima")
        st.image("https://cnx.org/resources/f7d9cce4d6aa00fbae13d576252dde7545f29c97/Powder", caption="Patr贸n de difracci贸n del silicio")
    if st.button("Cristales de mol茅culas"):
        st.image("https://cnx.org/resources/bbab3410b756781b28bfd38b9d293525b9f76368/Insulin%20crystals", caption="Cristales de insulina")
        st.image("https://cnx.org/resources/9491193edbd0ab2e784b580c295c4ce2328002fe/Chrome%20alum", caption="Cristales de Alumbre de cromo")
        st.image("https://cnx.org/resources/5f2097426608b73d32edc90a1a2fb3116a3d1211/Twinned%20crystal", caption="Cristales de Cuarzo")

if Temas == 'Reflexi贸n':
    st.header("Reflexi贸n")
    st.write("**驴Qu茅 es la reflexi贸n?**")
    st.image("https://images.squarespace-cdn.com/content/v1/5ca5fea877b90374d82c2908/1557313538336-0MMOHZP98Z9JSH0C9FU0/pexels-photo-220429.jpeg?format=1000w")
    st.write("La reflexi贸n es el cambio de direcci贸n de una onda electromagn茅tica al entrar en contracto con una superficie de otro medio, por ejemplo el agua o el vidrio")
    st.image("https://www.nexusinnovations.com/wp-content/uploads/2018/09/Reflection.jpg")
    st.write("Existen dos tipos de reflexi贸n; **La reflexi贸n Especular** y **La reflexi贸n Difusa**")
    st.write("En la reflexi贸n especular el angulo de incidencia siempre es el mismo que el reflejado y lo que no refleja la luz por asi decirlo, es reflexi贸n difusa")
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/dd/Reflexi%C3%B3n_especular_y_difusa.gif", caption="Tipos de reflexi贸n")
    st.write("Los colores pueden ser explicados por los electrones, ta que cada 谩tomo tiene su manera de reflejar la luz, cuando absorben la luz entran en un estado exitado y despu茅s de un rato se regresan a su nivel de energ铆a original al emitir un prot贸n")
    st.write("El fot贸n emitido tiene cierta frecuencia, si se mueve a diferentes niveles de energ铆a explicar铆a diferentes colores")
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Lambert2.gif", caption="Reflexi贸n Difusa")

if Temas == 'Refracci贸n':
    st.header("Refraccion")
    st.write("La refracci贸n sucede cuando una onda electromagn茅tica viaja de un medio a otro, su frecuencia no cambia pero su velocidad y longitud de onda si")
    st.image("https://www.amnh.org/var/ezflow_site/storage/images/media/amnh/images/explore/ology-images/physics/see-the-light/broken-straw/5419495-3-eng-US/broken-straw.jpg")
    st.write("Cuando la luz pasa de un medio m谩s r谩pido a uno m谩s lento, el 谩ngulo de incidencia va a ser mayor que el de refracci贸n")
    st.write("El 谩ngulo de incidencia se puede calcular con la **Ley de Snell**")
    st.image("https://personal.math.ubc.ca/~cass/courses/m309-01a/chu/Fundamentals/snell01.gif", width=600)
    st.write("Materiales y sus 铆ndices de refracci贸n",pd.DataFrame({
            'Material':["Vac铆o","Agua","Aire","Vidrio","Aceite","Vidrio Templado", "Safiro","Diamante"],
            'Indice de refracci贸n(n)':[1,1.33,1.00029,1.52,1.53,1.65,1.77,2.42],
            }))
    st.write("**驴Por qu茅 la luz es m谩s lenta en vidrio?**")
    st.write("Cuando las ondas de luz pasan a traves del medio, en el caso del vidrio, la onda que pasa por ahi empieza a hacer que vibren los 谩tomos del material")
    st.image("unknown.png",width=500)
    st.write("Cuando empiezas a mover estas cargas el茅ctricas, cada 谩tomo va a terminar produciendo ondas electromagn茅ticas propias")
    st.write("Luego la superposici贸n de la onda original con las nuevas ondas que se est谩n creando, cuando las sumas todas terminas con la onda que esta viajando a otra velocidad menor a la de la luz originalmente")
    st.image("unknown2.png", width=500)

if Temas == 'Datos extras de las ondas':
    st.header("Datos extras de las ondas")
    st.write("**驴Por qu茅 las ondas de microondas no est谩n enseguida de las ultravioletas si son capaces de causarnos da帽o?**")
    st.write("La microondas emiten ondas que hacen vibrar las p谩rticulas del agua aumentando su temperatura mientras que las ondas de rayos x y UV cargan tanta energ铆a quer son capaces de romper los enlaces de tus mol茅culas, la exposici贸n continua a estas puede causar c谩ncer")
    st.write("Las ondas con freciencias menores nos afectan por como hacen vibrar las mol茅culas del agua ya que resonan de la misma manera de la vibraci贸n del agua")
    st.write("Nuestro cuerpo est谩 formado en un ambiente donde las ondas EM visibles son abundantes, por lo tanto no nos afectan.")
    st.write("**驴De d贸nde salen las ondas electromagn茅ticas?**")
    st.write("Las ondas son la propagaci贸n de una perturbaci贸n en el campo electromagn茅tico causado por la vibraci贸n de cargas.")
    st.write("Considera un par de cargas en el espacio; despu茅s al mover una de ellas la otra no se -percata- instantaneamente del cambio, esa informaci贸n le va a llegar a la velocidad de la luz, cada vez que tienes una carga vibrando en una frecuencia alta, empieza a perturbar el campo electromagn茅tico en forma de ondas")
    st.write("**驴C贸mo es que se comporta como una p谩rticula y como una onda?**")
    st.write("En algunos instantes vemos la luz comportandose como una onda en la refracci贸n, interferencia y a veces como part铆culas como en el efecto fotoel茅ctrico")

if Temas == 'Informaci贸n Integrantes':
    st.header("Integrantes")
    st.subheader("LosPlancks")
    st.write("Dania Veleta De La O ")
    st.caption("a349174@uach.mx")
    st.write("Yazmin Itzel Ontiveros Macias")
    st.caption("a344162@uach.mx")
    st.write("Maximiliano Chavira Hern谩ndez")
    st.caption("a349010@uach.mx")
    st.write("Ruth Estela Chavira L贸pez")
    st.caption("a349170@uach.mx")
