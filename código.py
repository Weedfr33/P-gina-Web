# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

import pandas as pd
import base64
# Importamos Path para verificar si las imágenes existen antes de mostrarlas.
# De esta manera, la página no se detendrá si todavía falta subir alguna imagen.
from pathlib import Path

# Abrimos la imagen que utilizaremos como fondo de la portada.
with open("fondoinicio.png", "rb") as archivo_imagen:
    # Convertimos la imagen a texto para que pueda mostrarse dentro del CSS.
    imagen_codificada = base64.b64encode(
        archivo_imagen.read()
    ).decode()


st.markdown(
    """
    <style>
    .titulo{
        text-align:center;
        color:#ED1C2E;
        font-size:110px;
        font-weight:900;
        letter-spacing:12px;
        text-shadow:
            0 0 8px #ff2d4d,
            0 0 25px rgba(237,28,46,.9);
    }

    .subtitulo{
        text-align:center;
        color:#ED1C2E;
        font-size:80px;
        font-weight:900;
        letter-spacing:20px;
        margin-top:-35px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="titulo">M&M</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">THINGS</div>', unsafe_allow_html=True)

# Aplicamos la imagen como fondo general de la página.
st.markdown(
    f"""
    <style>

    .stApp {{
        background-image:
            linear-gradient(
                rgba(5, 1, 8, 0.60),
                rgba(5, 1, 8, 0.88)
            ),
           url("data:image/png;base64,{imagen_codificada}");
        background-size: cover;
        background-position: center top;
        background-attachment: fixed;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# Cargamos la hoja "Tabla" del archivo Excel.
# header=1 indica que los nombres de las columnas se encuentran en la segunda fila.
datos = pd.read_excel(
    "BASE DE DATOS - COMPUTACIONAL.xlsx",
    sheet_name="Tabla",
    header=1
)

# Eliminamos las columnas que estén completamente vacías.
# En este caso, también retiramos la primera columna vacía del archivo Excel.
datos = datos.dropna(axis=1, how="all")

# Eliminamos los espacios adicionales que puedan existir
# al inicio o al final de los nombres de las columnas.
# Esto evita errores al llamar una columna dentro del código.
datos.columns = datos.columns.str.strip()

# Completamos las celdas vacías del título utilizando
# la información registrada en la fila anterior.
datos["Título"] = datos["Título"].ffill()

# Completamos de la misma manera las descripciones vacías.
# Después de limpiar los encabezados, esta columna ya no lleva
# un espacio adicional después del punto.
datos["Descripción sinóptica del episodio"] = datos["Descripción sinóptica del episodio"].ffill()

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
# Relacionamos el nombre que verá el usuario con
# el nombre utilizado dentro del archivo Excel.
temporadas = {
    "Temporada 1": "Primera",
    "Temporada 2": "Segunda",
    "Temporada 3": "Tercera"
}

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Creamos un menú de navegación horizontal para que el usuario pueda
# desplazarse fácilmente entre las diferentes secciones de la página.
selected = option_menu(

    # No mostramos un título dentro del menú porque ya tenemos
    # el nombre principal del proyecto en la parte superior.
    menu_title=None,

    # Definimos las secciones que estarán disponibles dentro de la página web.
    # Cada una representa una funcionalidad distinta del proyecto.
    options=[
        "🧇 Hawkins", "🧪 Hawkins Lab", "📼 The Episodes", "🔦 Upside Down"
    ],

    # No utilizamos los iconos propios de la librería porque
    # cada opción ya incluye un emoji representativo.
    icons=["none", "none", "none", "none"],

    # Tampoco mostramos un icono principal ya que el menú
    # no tiene un título asociado.
    menu_icon=None,

    # Indicamos que la primera sección ("Hawkins") sea la que
    # aparezca seleccionada cuando el usuario abra la página.
    default_index=0,

    # Mostramos el menú de forma horizontal para aprovechar
    # mejor el ancho de la página.
    orientation="horizontal",

    # Personalizamos el diseño del menú para adaptarlo
    # a la estética inspirada en Stranger Things.
    styles={

        # Modificamos el contenedor general donde se encuentra el menú.
        "container": {
            "padding": "7px",
            "background-color": "rgba(8, 7, 15, 0.78)",
            "border": "1px solid rgba(237, 28, 46, 0.22)",
            "border-radius": "8px",
            "backdrop-filter": "blur(8px)"
        },

        # Personalizamos la apariencia de todas las opciones del menú.
        "nav-link": {
            "font-size": "17px",
            "color": "#F5F1F3",
            "padding": "14px 8px",
            "border-radius": "6px",
            "text-align": "center"
        },

        # Definimos el estilo que tendrá únicamente la opción
        # que el usuario tenga seleccionada.
        "nav-link-selected": {
            "background-color": "rgba(210, 20, 43, 0.92)",
            "color": "#FFFFFF",
            "font-weight": "700",
            "box-shadow": "0 0 14px rgba(237, 28, 46, 0.45)"
        }
    }
)
    
# Verificamos si el usuario seleccionó la sección "Hawkins"
# dentro del menú principal de la página.
if selected == "🧇 Hawkins":

    # Mostramos el título principal de la sección de inicio.
    st.markdown(
        """
        <h1 style="
            text-align: center;
            font-size: 55px;
            margin-top: 35px;
            margin-bottom: 10px;
        ">
            Bienvenido a Hawkins
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Agregamos una frase breve para presentar la temática de la página.
    st.markdown(
        """
        <p style="
            text-align: center;
            font-size: 20px;
            color: #D8D5DC;
            margin-bottom: 50px;
        ">
            COLOCAR AQUÍ EL TEXTO.
        </p>
        """,
        unsafe_allow_html=True
    )

    # ---------------------------------------------------------
    # PRIMER BLOQUE: ¿QUÉ ES M&M THINGS?
    # ---------------------------------------------------------

    # Creamos dos columnas de diferente tamaño para colocar
    # el texto del proyecto al lado de una imagen.
    columna_texto, columna_imagen = st.columns([1.2, 1], gap="large")

    # Mostramos la información principal del proyecto
    # dentro de la primera columna.
    with columna_texto:

        st.markdown(
            """
            <h2 style="
                color: #FF203D;
                font-size: 35px;
                margin-bottom: 20px;
            ">
                ¿Qué es M&M Things?
            </h2>
            """,
            unsafe_allow_html=True
        )

        # Creamos un contenedor con borde para separar visualmente
        # la descripción del proyecto del resto de la portada.
        with st.container(border=True):

            # Este texto es provisional y posteriormente puede
            # reemplazarse por la descripción final del proyecto.
            st.markdown(
                """
                COLOCAR AQUÍ EL TEXTO.

                COLOCAR AQUÍ EL TEXTO.
                """
            )

    # Utilizamos la segunda columna para mostrar una imagen
    # representativa de la serie o del proyecto.
    with columna_imagen:

        # Guardamos en una variable la ruta de la imagen
        # que queremos mostrar en esta sección.
        ruta_portada = Path("portada_hawkins.png")

        # Verificamos si la imagen ya fue subida al repositorio.
        if ruta_portada.exists():

            # Mostramos la imagen ocupando todo el ancho disponible
            # dentro de la columna.
            st.image(
                ruta_portada,
                use_container_width=True
            )

        else:

            # Si todavía no existe la imagen, mostramos un mensaje
            # provisional para que la aplicación continúe funcionando.
            with st.container(border=True):
                st.markdown(
                    """
                    ### 🎬 Imagen de portada

                    Aquí se colocará una imagen o póster relacionado
                    con *Stranger Things*.
                    """
                )

    # Agregamos un espacio entre los diferentes bloques
    # para que el contenido no se vea amontonado.
    st.write("")
    st.write("")

    # ---------------------------------------------------------
    # SEGUNDO BLOQUE: OBJETIVO
    # ---------------------------------------------------------

    st.markdown(
        """
        <h2 style="
            text-align: center;
            color: #FF203D;
            font-size: 35px;
            margin-bottom: 20px;
        ">
            Nuestro objetivo
        </h2>
        """,
        unsafe_allow_html=True
    )

    # Creamos una columna central más ancha y dos columnas pequeñas
    # a los lados para que el objetivo aparezca centrado.
    espacio_izquierdo, objetivo, espacio_derecho = st.columns([1, 4, 1])

    with objetivo:

        # Colocamos el objetivo dentro de una tarjeta central.
        with st.container(border=True):

            # Este texto también puede reemplazarse cuando
            # el objetivo final del proyecto esté listo.
            st.markdown(
                """
                COLOCAR AQUÍ EL TEXTO.

                Aquí irá la versión definitiva del objetivo.
                """
            )

    st.write("")
    st.write("")

    # ---------------------------------------------------------
    # TERCER BLOQUE: ¿QUÉ ENCONTRARÁS?
    # ---------------------------------------------------------

    st.markdown(
        """
        <h2 style="
            text-align: center;
            color: #FF203D;
            font-size: 35px;
            margin-bottom: 10px;
        ">
            ¿Qué encontrarás en M&M Things?
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="
            text-align: center;
            color: #D8D5DC;
            font-size: 17px;
            margin-bottom: 35px;
        ">
            Cada sección permite explorar la relación entre la música,
            los episodios y las temporadas de la serie.
        </p>
        """,
        unsafe_allow_html=True
    )

    # Creamos tres columnas para presentar las funciones principales
    # mediante tarjetas independientes.
    tarjeta_episodios, tarjeta_laboratorio, tarjeta_recomendacion = st.columns(
        3,
        gap="large"
    )

    # ---------------------------------------------------------
    # TARJETA: THE EPISODES
    # ---------------------------------------------------------

    with tarjeta_episodios:

        # Creamos una tarjeta con borde para explicar
        # lo que encontrará el usuario en The Episodes.
        with st.container(border=True):

            st.markdown(
                """
                <h3 style="
                    text-align: center;
                    color: #FFFFFF;
                    font-size: 26px;
                ">
                    📼 The Episodes
                </h3>
                """,
                unsafe_allow_html=True
            )

            # Este texto puede cambiarse cuando tengan
            # la descripción definitiva de la sección.
            st.markdown(
                """
                Consulta los episodios de las tres primeras temporadas
                y conoce una breve sinopsis de cada uno.
                """
            )

    # ---------------------------------------------------------
    # TARJETA: HAWKINS LAB
    # ---------------------------------------------------------

    with tarjeta_laboratorio:

        # Esta tarjeta presenta la sección donde estará
        # el repositorio principal de canciones.
        with st.container(border=True):

            st.markdown(
                """
                <h3 style="
                    text-align: center;
                    color: #FFFFFF;
                    font-size: 26px;
                ">
                    🧪 Hawkins Lab
                </h3>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                Explora el repositorio de canciones organizado por
                temporada y episodio, junto con gráficos y mapas.
                """
            )

    # ---------------------------------------------------------
    # TARJETA: UPSIDE DOWN
    # ---------------------------------------------------------

    # Utilizamos la tercera columna para presentar la sección
    # que recomendará una canción aleatoria del repositorio.
    with tarjeta_recomendacion:

        # Creamos una tarjeta con borde para mantener el mismo
        # diseño utilizado en las otras dos secciones.
        with st.container(border=True):

            # Mostramos el nombre de la sección dentro de la tarjeta.
            st.markdown(
                """
                <h3 style="
                    text-align: center;
                    color: #FFFFFF;
                    font-size: 26px;
                ">
                    🔦 Upside Down
                </h3>
                """,
                unsafe_allow_html=True
            )

            # Explicamos brevemente qué encontrará el usuario
            # cuando ingrese a esta sección.
            st.markdown(
                """
                Recibe una canción aleatoria del repositorio y descubre
                en qué temporada y episodio aparece.
                """
            )

    # Agregamos un espacio al final de la portada para que
    # las tarjetas no queden pegadas a la siguiente sección.
    st.write("")
    st.write("")

    # ---------------------------------------------------------
    # MENSAJE FINAL DE LA PORTADA
    # ---------------------------------------------------------
    
    # Dejamos un pequeño espacio antes del mensaje final.
    st.write("")
    st.write("")
    
    # Mostramos un título para invitar al usuario a explorar
    # el contenido de la página.
    st.markdown(
        """
        <h2 style="
            text-align:center;
            color:#FF203D;
            font-size:36px;
            margin-bottom:15px;
        ">
            El soundtrack de Hawkins te espera
        </h2>
        """,
        unsafe_allow_html=True
    )
    
    # Añadimos una breve descripción que indique cómo navegar
    # por las diferentes secciones del proyecto.
    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:19px;
            color:#E8E8E8;
            max-width:850px;
            margin:auto;
            line-height:1.8;
        ">
            Explora las temporadas, descubre la música de cada episodio
            y deja que <strong>Upside Down</strong> te recomiende una canción
            para comenzar tu recorrido.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Agregamos un pequeño espacio para separar el mensaje
    # del final de la portada.
    st.write("")
    st.write("")

# Verificamos si el usuario seleccionó la sección "Hawkins Lab"
# dentro del menú principal.
elif selected == "🧪 Hawkins Lab":

    # Mostramos el título principal de esta sección.
    st.markdown(
        """
        <h1 style="
            text-align: center;
            font-size: 55px;
            margin-top: 35px;
            margin-bottom: 25px;
        ">
            Repositorio musical de Hawkins
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Creamos una lista con las temporadas disponibles.
    opciones_temporada = [
        "Temporada 1",
        "Temporada 2",
        "Temporada 3"
    ]

    # Mostramos una barra desplegable para que el usuario
    # seleccione la temporada que desea explorar.
    temporada_seleccionada = st.selectbox(
        "Selecciona una temporada",
        opciones_temporada
    )
     # Relacionamos el nombre mostrado en la página con
    # el nombre que aparece dentro del archivo Excel.
    temporadas_excel = {
        "Temporada 1": "Primera",
        "Temporada 2": "Segunda",
        "Temporada 3": "Tercera"
    }

    # Obtenemos el nombre de la temporada tal como
    # se encuentra registrado en la base de datos.
    nombre_temporada = temporadas_excel[temporada_seleccionada]

    # Filtramos únicamente las canciones que pertenecen
    # a la temporada elegida por el usuario.
    datos_temporada = datos[
        datos["Temporada"] == nombre_temporada
    ]
        # Obtenemos los episodios disponibles dentro
    # de la temporada seleccionada.
    episodios = sorted(
        datos_temporada["Episodio"]
        .dropna()
        .unique()
        .tolist()
    )

    # Recorremos cada episodio para mostrar su título
    # y la lista de canciones correspondiente.
    for episodio in episodios:

        # Filtramos las canciones pertenecientes
        # al episodio que se está recorriendo.
        datos_episodio = datos_temporada[
            datos_temporada["Episodio"] == episodio
        ]

        # Recuperamos el título del episodio.
        titulo_episodio = datos_episodio["Título"].iloc[0]

        # Mostramos el número y el título del episodio.
        st.markdown(
            f"""
            <h2 style="
                color: #FF203D;
                margin-top: 35px;
                margin-bottom: 20px;
            ">
                Episodio {int(episodio)}: {titulo_episodio}
            </h2>
            """,
            unsafe_allow_html=True
        )

        # Recorremos cada canción del episodio.
        for _, cancion in datos_episodio.iterrows():

            # Creamos dos columnas para colocar la portada
            # al lado de la información de la canción.
            columna_portada, columna_texto = st.columns(
                [1.3,3.7],
                gap="large"
                )

            with columna_portada:

                # Mostramos la portada guardada en el Excel.
                st.image(
                    cancion["Portada (imagen)"],
                    width=300
                )

            with columna_texto:

                # Mostramos el nombre de la canción,
                # el artista y el año de lanzamiento.
                st.markdown(f"### {cancion['Canción']}")
                st.write(f"**Artista:** {cancion['Artista']}")
                st.write(f"**Año:** {int(cancion['Año'])}")

            # Agregamos espacio entre una canción y otra.
            st.write("")

elif selected == '📼 The Episodes':
    st.markdown("<h1 style='text-align: center;'>La música episodio por episodio</h2>", unsafe_allow_html=True)

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
elif selected == '🔦 Upside Down':
    st.markdown("<h1 style='text-align: center;'>Atrévete a descubrir algo nuevo</h2>", unsafe_allow_html=True)

# elif selected == '🧪 Hawkins Lab':
    # st.markdown("<h1 style='text-align: center;'>Analizando el soundtrack</h2>", unsafe_allow_html=True)

