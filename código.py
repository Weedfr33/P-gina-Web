# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run PC3.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

import pandas as pd

# Cargamos la hoja "Tabla" del archivo Excel.
# header=1 indica que los nombres de las columnas se encuentran en la segunda fila.
datos = pd.read_excel(
    "BASE DE DATOS - COMPUTACIONAL.xlsx",
    sheet_name="Tabla",
    header=1
)

# Eliminamos la primera columna porque está vacía.
datos = datos.dropna(axis=1, how="all")
# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
#with st.sidebar:
    #selected = option_menu("Selecciona una sección: ",['Inicio', 'Experiencia', 'Gráficos'] , 
       # icons=['0-circle','1-circle', '2-circle'], menu_icon="filetype-py", default_index=0)
    # Crea un menú de selected dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de selected disponibles para navegar -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
selected = option_menu(
    menu_title=None,
    options=['🧇 Hawkins', '🎧 Now Playing', '📼 The Episodes', '🔦 Upside Down', '🧪 Hawkins Lab' ], 
    icons=['film', 'film', 'film'], 
    menu_icon=None, default_index=0, orientation="horizontal")
    # Título que aparece antes de las selected del menú -> menu_title="Selecciona una sección: "
    # Lista de selected que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "selected"
if selected == 'Inicio':
    st.markdown("<h1 style='text-align: center;'>404: Experiencia no encontrada</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena

    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2)

    # Muestra una imagen en la primera columna
    # col1.image("fotoccori.jpg", caption='Ccori', width=300)
    # "ellie.png" es el archivo de imagen que se visualizará -> Aquí debes reemplazar por tu foto de perfil
    # El texto "Ellie" aparecerá como descripción de la imagen
    # width=300 establece el ancho de la imagen en 300 píxeles

    # Define una cadena de texto multilínea que contiene una guía para redactar una presentación personal.
    texto = """
    Hola! Soy Ccori Arias, 
    estudiante de comunicación audiovisual en la PUCP. 
    Lo que más me gusta de mi carrera es que nunca se queda solo en la teoría. Es una carrera muy práctica, donde cada proyecto es una oportunidad para aprender. También disfruto mucho que combine el lado artístico con el pensamiento lógico, porque te reta a crear, analizar y resolver problemas al mismo tiempo.
    En el futuro, me gustaría ser productora ejecutiva y de campo, me encanta crear proyectos audiovisuales y vivir todo el proceso de hacer que una idea cobre vida. 
    Cuando tengo tiempo libre disfruto mucho ver películas, tomar fotos, grabar videos de mis experiencias cotidianas y luego editar el material.
    """

    # Muestra el texto en la segunda columna utilizando HTML
    col2.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    # El estilo CSS justifica el texto y establece un tamaño de fuente de 18 píxeles
    # f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>"
    # unsafe_allow_html=True permite que Streamlit interprete las etiquetas HTML incluidas en la cadena

elif selected == 'Experiencia':
    st.markdown("<h1 style='text-align: center;'>Detrás del código 👩🏻‍💻</h1>", unsafe_allow_html=True)

    # Agregar un  texto para la respuesta
    texto_2 = """
    Al principio aprender a programar me daba mucho miedo porque era un curso completamente nuevo para mí. Nunca antes había programado y pensaba que sería muy difícil.
    Sin embargo, poco a poco me di cuenta que la programación no solo es escribir códigos, sino también desarrollar paciencia, resolver problemas y pensar de una manera más organizada.
    Lo que más disfruto de programar es ver cómo unas cuantas líneas de código pueden convertirse en algo funcional. También me gusta personalizar los proyectos y ejercicios, corregir errores porque eso me hace aprender el proceso y con el tiempo, ya sé cual es el error casi intuitivamente. En el futuro me gustaría crear blogs o páginas web relacionadas con el cine y el mundo audiovisual. 
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 1 - Youtube")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    st.video("https://youtu.be/G4dKSeN9d1g")
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se comparan los tipos de datos strings y listas en Python utilizando ejemplos prácticos para facilitar la comprensión de sus diferencias y de las situaciones en las que conviene utilizar cada uno."
    )

    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    st.subheader("🎥 Video 2 - Youtube")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    st.video("https://youtu.be/Hg9DECHpnbY")
    # st.link_button(
            # "Ver video",
            # "https://youtu.be/Hg9DECHpnbY"
        #)
    # Agrega una breve descripción del video.
    st.caption(
        "En este video se explican las principales diferencias entre los bucles for y while en Python mediante ejemplos propios, mostrando su funcionamiento, sus características y las situaciones en las que resulta más adecuado utilizar cada uno."
    )

elif selected == 'Gráficos':
    st.markdown("<h2 style='text-align: center;'>Visualizando variables🧩</h2>", unsafe_allow_html=True)

    graficos = ['📊Gráfico de barras', '📊Gráfico circular', '☁️ Nube de palabras 1', '☁️ Nube de palabras 2', '🗺️Mapa 1']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == '📊Gráfico de barras':
        # Título de la sección
        st.subheader("📊 Gráfico 1: Goles de Barcelona")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 20px;'>
            Este gráfico muestra la distribución de la cantidad de goles anotados y recibidos por el FC Barcelona, diferenciando los partidos disputados como local y como visitante. A partir de la comparación de las frecuencias, es posible observar el rendimiento ofensivo y defensivo del equipo en ambas condiciones, identificando los marcadores que se repiten con mayor frecuencia.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen utilizando tres columnas
        col3, col4, col5 = st.columns([1, 5, 1])

        with col4:
            st.image(
                "Frecuencia_goles_Barcelona.png",
                width=800
            )

    elif grafico_seleccionado == '📊Gráfico circular':
        # Título de la sección
        st.subheader("📊 Gráfico 2: Rendimiento de Barcelona como visitante")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Este gráfico circular muestra la proporción de partidos ganados, empatados y perdidos por el FC Barcelona cuando juega como visitante. Se observa que el equipo obtuvo la victoria en la mayoría de sus encuentros (63,2 %), mientras que las derrotas representan el 31,6 % y los empates solo el 5,3 %. Estos resultados reflejan un rendimiento positivo del equipo fuera de casa.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "Rendimiento_Barcelona_visitante.png",
                width=800
            )
    elif grafico_seleccionado == '☁️ Nube de palabras 1':
        # Título de la sección
        st.subheader("☁️ Nube de palabras 1: Harry Potter")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Esta nube de palabras representa los términos con mayor frecuencia en un extracto de Harry Potter. El tamaño de cada palabra indica la cantidad de veces que aparece en el texto, permitiendo identificar los conceptos, personajes y elementos que tienen mayor presencia. Esta visualización facilita reconocer, de forma rápida, los temas y el vocabulario predominante del fragmento analizado.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "nube_palabras_harry_potter.png",
                width=800
            )
    elif grafico_seleccionado == '☁️ Nube de palabras 2':
        # Título de la sección
        st.subheader("☁️ Nube de palabras 2: Letra de canción")

        # Interpretación del gráfico
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Esta nube de palabras representa los términos más frecuentes de la letra de una canción. Se observa el predominio de palabras como final, que, no y ya, las cuales reflejan la importancia de ciertos conceptos y emociones dentro de la composición. De esta manera, la visualización permite identificar de forma rápida los elementos con mayor presencia en la letra.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Centrar la imagen
        col6, col7, col8 = st.columns([1, 5, 1])

        with col7:
            st.image(
                "nube_palabras_letra.png",
                width=800
            )
    elif grafico_seleccionado == '🗺️Mapa 1':
        # Título de la sección
        st.subheader("🗺️ Mapa: TOP 5 Películas favoritas")

        # Interpretación del mapa
        st.markdown(
            """
            <div style='text-align: justify; font-size: 18px;'>
            Este mapa muestra la ubicación geográfica de los principales lugares de grabación de mis cinco películas favoritas: <strong>Aftersun</strong>, <strong>La peor persona del mundo</strong>, <strong>Titane</strong>, <strong>Trainspotting</strong> y <strong>Enter the Void</strong>. Al seleccionar cada marcador es posible consultar información adicional de la película, como el <strong>director</strong>, el <strong>año</strong> de estreno, el <strong>país</strong> de producción, el <strong>género</strong>, el <strong>tema principal</strong> y el <strong>lugar</strong> específico donde se realizó el rodaje. De esta manera, el mapa permite visualizar tanto la distribución geográfica de las obras como algunos de sus datos más relevantes.
            </div>
            """,
            unsafe_allow_html=True
        )

        # Cargar el mapa HTML generado previamente
        with open("mapa_peliculas.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Mostrar el mapa interactivo
        components.html(
            html_content,
            height=600
        )
