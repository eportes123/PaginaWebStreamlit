import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import pycountry
from PIL import Image
from streamlit_option_menu import option_menu

# Configurar el tema a claro

# Configuración de la página
#st.set_page_config(page_title="Premier League 2018-2019", page_icon=":rocket:")
st.set_page_config(page_title="Premier League 2018-2019", page_icon="archivos/kisspng-201617-premier-league-english-football-league-l-lion-emoji-5b460f07222401.1477875515313180231399.png")
# Forzar el tema claro
st.markdown(
    """
    <style>
        footer {display: none}
        [data-testid="stHeader"] {display: none}
        body {
            color: #000000;
            background-color: #C1B3B3;
        }
    </style>
    """, unsafe_allow_html=True
)
with open('archivos/style.css') as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

# Configurar el diseño en dos columnas
col1, col2, col3 = st.columns([1, 1, 1])


with col1:
  # Imagen a la izquierda
  st.write("")
  image1 = Image.open("archivos/tecnologico-de-monterrey-blue.png")
  st.image(image1, use_column_width=True)
  #st.image("tecnologico-de-monterrey-blue.png", width=200)

with col3:
  # Imagen a la derecha
  image2 = Image.open("archivos/logo-Premier-League.png")
  st.image(image2, use_column_width=True)
  #st.image("archivos/logo-Premier-League.png", width=200)

# Título o texto en el medio
st.title("**Premier league 2018-2019**")

# 3. CSS style definitions
selected3 = option_menu(None, ["Menu", "Graficas",  "Mapas", 'KPIs'],
    icons=['house', 'bar-chart-line', "map", 'speedometer2'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#ACACAB"},
        "icon": {"color": "#0D0D0D", "font-size": "20px"},
        "nav-link": {"font-size": "19px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#0339A6"},
    }
)
selected3

# Morado premier 3A0E40

@st.cache_data
def get_data():
  jugadores = pd.read_csv('archivos/england-premier-league-players-2018-to-2019-stats.csv')
  equipos = pd.read_csv('archivos/england-premier-league-teams-2018-to-2019-stats.csv')
  partidos = pd.read_csv('archivos/england-premier-league-matches-2018-to-2019-stats.csv')
  return jugadores,equipos,partidos

jugadores, equipos, partidos = get_data()

if selected3 == 'Menu':
  st.markdown('## Temporada 2018-2019 de la Premier League: Un Análisis Visual del Fútbol')
  st.write(''' En esta página, nos sumergiremos en datos y estadísticas clave de la temporada de la Premier League 2018-2019.
  A través de herramientas de visualización interesantes, ofrecemos una experiencia detallada para comprender y apreciar cómo se desarrolló la temporada.

  Examinaremos las historias emocionantes que se desplegaron durante la temporada mediante gráficos interactivos y mapas informativos. Nuestra herramienta
  de visualización te permitirá explorar tendencias, patrones y momentos destacados de manera intuitiva.''')

  st.markdown('### Lo que Encontrarás Aquí')
  col1, col2 = st.columns([1,1])
  with col1:
    st.write('''
    **Gráficas Interactivas:** Observa el desarrollo de datos clave mediante gráficos personalizables. Ajusta las visualizaciones según tus preferencias para obtener perspectivas únicas.

    **Mapas de Jugadores por País:** Explora la diversidad geográfica de los jugadores en la Premier League y comprende la contribución global a este emocionante campeonato.

    **Análisis de Equipos:** Sumérgete en el rendimiento de cada equipo a través de KPIs fundamentales. Desde posesión hasta goles, analizaremos cómo se destacaron los equipos en la temporada.''')
  with col2:
    imagefut = Image.open("archivos/grafico-de-estadisticas-de-futbol.png")
    st.image(imagefut)


  st.write("---")
  st.header('')

  st.markdown('### Base de Datos de Jugadores:')
  st.write('''Esta base de datos contiene información sobre cada jugador, incluido su rendimiento y estadísticas clave. Sirve como el fundamento para los análisis detallados de desempeño individual. ''')
  with st.expander("Datos de jugadores:"):
      st.write(jugadores)
  st.markdown('### Base de Datos de Equipos:')
  st.write(''' Aquí encontrarás datos específicos de cada equipo durante la temporada. Desde resultados hasta estadísticas generales, esta base de datos es esencial para comprender el rendimiento colectivo de cada equipo.''')
  with st.expander("Datos de los equipos:"):
      st.write(equipos)
  st.markdown('### Base de Datos de Partidos:')
  st.write('''La información detallada de cada encuentro de la temporada se encuentra en esta base de datos. Desde resultados hasta eventos clave, esta base proporciona una visión integral de cada partido disputado. ''')
  with st.expander("Datos de los partidos:"):
      st.write(partidos)

  st.write("---")
  st.markdown('## Datos importantes de la Temporada')
  st.markdown('')
  st.markdown('### Mejor Equipo de la Temporada')
  # Configurar el diseño en dos columnas
  title_col, emp_col, k1, k2, k3, k4 = st.columns([1.4,0.2,1,1,1,1])

  with title_col:
    st.markdown('Manchester City FC', unsafe_allow_html = True)
    image1 = Image.open("archivos/Manchester City FC.png")
    st.image(image1, use_column_width=True)

  with k1:
    st.write('')
    st.write('')
    st.write('')
    kpi1= equipos[equipos['team_name'] == 'Manchester City FC']['league_position'].values[0]
    kpi1_formatted = f"{kpi1}°"
    with st.container():
          st.markdown(f'<p class="kpi1_text">Posición en Liga<br></p><p class="price_details">{kpi1_formatted}</p>', unsafe_allow_html=True)


  with k2:
    st.write('')
    st.write('')
    st.write('')
    kpi2=equipos[equipos['team_name'] == 'Manchester City FC']['goals_scored'].values[0]
    with st.container():
          st.markdown(f'<p class="kpi2_text">Goles Anotados<br></p><p class="price_details">{kpi2}</p>', unsafe_allow_html = True)

  with k3:
    st.write('')
    st.write('')
    st.write('')
    kpi3= equipos[equipos['team_name'] == 'Manchester City FC']['goals_conceded'].values[0]
    with st.container():
            st.markdown(f'<p class="kpi5_text">Goles Concedidos<br></p><p class="price_details">{kpi3}</p>', unsafe_allow_html = True)

  with k4:
    st.write('')
    st.write('')
    st.write('')
    kpi4=equipos[equipos['team_name'] == 'Manchester City FC']['goal_difference'].values[0]
    with st.container():
      st.markdown(f'<p class="kpi4_text">Diferencia de Goles<br></p><p class="price_details">{kpi4}</p>', unsafe_allow_html = True)

  st.markdown('')
  st.markdown('### Peor Equipo de la Temporada')
  title_col, emp_col, k1, k2, k3, k4 = st.columns([1.4,0.2,1,1,1,1])

  with title_col:
    st.markdown('Huddersfield Town FC', unsafe_allow_html = True)
    image1 = Image.open("archivos/Huddersfield Town FC.png")
    st.image(image1, use_column_width=True)

  with k1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    kpi1= equipos[equipos['team_name'] == 'Huddersfield Town FC']['league_position'].values[0]
    kpi1_formatted = f"{kpi1}°"
    with st.container():
          st.markdown(f'<p class="kpi1_text">Posición en Liga<br></p><p class="price_details">{kpi1_formatted}</p>', unsafe_allow_html=True)


  with k2:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    kpi2=equipos[equipos['team_name'] == 'Huddersfield Town FC']['goals_scored'].values[0]
    with st.container():
          st.markdown(f'<p class="kpi2_text">Goles Anotados<br></p><p class="price_details">{kpi2}</p>', unsafe_allow_html = True)

  with k3:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    kpi3= equipos[equipos['team_name'] == 'Huddersfield Town FC']['goals_conceded'].values[0]
    with st.container():
            st.markdown(f'<p class="kpi5_text">Goles Concedidos<br></p><p class="price_details">{kpi3}</p>', unsafe_allow_html = True)

  with k4:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    kpi4=equipos[equipos['team_name'] == 'Huddersfield Town FC']['goal_difference'].values[0]
    with st.container():
      st.markdown(f'<p class="kpi4_text">Diferencia de Goles<br></p><p class="price_details">{kpi4}</p>', unsafe_allow_html = True)

  st.write("---")
  st.markdown('')
  st.markdown('### Mejor jugador de la Temporada')
  title_col, emp_col, k1, k2, k3, k4 = st.columns([1.4,0.2,1,1,1,1])

  with title_col:
    st.markdown('Sergio Aguero', unsafe_allow_html = True)
    image1 = Image.open("archivos/SergioAguero.png")
    st.image(image1, use_column_width=True)

  with k1:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    kpi1= jugadores[jugadores['full_name'] == 'Sergio Aguero']['minutes_played_overall'].values[0]
    with st.container():
          st.markdown(f'<p class="kpi1_text">Minutos Jugados<br></p><p class="price_details">{kpi1}</p>', unsafe_allow_html=True)


  with k2:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    kpi2=jugadores[jugadores['full_name'] == 'Sergio Aguero']['appearances_overall'].values[0]
    with st.container():
          st.markdown(f'<p class="kpi2_text">Apariciones Totales<br></p><p class="price_details">{kpi2}</p>', unsafe_allow_html = True)

  with k3:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    kpi3= jugadores[jugadores['full_name'] == 'Sergio Aguero']['goals_overall'].values[0]
    with st.container():
            st.markdown(f'<p class="kpi5_text">Goles Anotados<br></p><p class="price_details">{kpi3}</p>', unsafe_allow_html = True)

  with k4:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    kpi4=jugadores[jugadores['full_name'] == 'Sergio Aguero']['assists_overall'].values[0]
    with st.container():
      st.markdown(f'<p class="kpi4_text">Asistencias Realizadas<br></p><p class="price_details">{kpi4}</p>', unsafe_allow_html = True)

  kpi_values = [
      jugadores[jugadores['full_name'] == 'Sergio Aguero']['penalty_goals'].values[0],
      jugadores[jugadores['full_name'] == 'Sergio Aguero']['penalty_misses'].values[0],
      jugadores[jugadores['full_name'] == 'Sergio Aguero']['yellow_cards_overall'].values[0],
      jugadores[jugadores['full_name'] == 'Sergio Aguero']['appearances_overall'].values[0],
      jugadores[jugadores['full_name'] == 'Sergio Aguero']['goals_overall'].values[0],
      jugadores[jugadores['full_name'] == 'Sergio Aguero']['assists_overall'].values[0]
  ]

  # Nombres de las KPI
  kpi_names = [
      'Penales anotados',
      'Penales fallados',
      'Tarjetas amarillas',
      'Apariciones',
      'Goles anotado',
      'Asistencias',
  ]

  # Crear un DataFrame con los datos
  df = pd.DataFrame({'KPI': kpi_names, 'Valor': kpi_values})

  # Crear el gráfico de radar con Plotly Express
  fig = px.line_polar(df, r='Valor', theta='KPI', line_close=True)

  # Agregar etiquetas de texto a los puntos
  fig.update_traces(
      text=df['Valor'].map(lambda x: f"{x}"),
      hoverinfo='text+name',
      mode='text'
  )

  # Configuraciones adicionales del gráfico
  fig.update_traces(fill='toself')
  fig.update_layout(
      polar=dict(
          radialaxis=dict(
              visible=True,
              range=[0, max(kpi_values)]  # Puedes ajustar el rango según tus datos
          ),
      ),
  )

  # Mostrar el gráfico en Streamlit
  st.plotly_chart(fig)

if selected3 == 'Graficas':

  st.markdown('## **Graficas Premier league 2018-2019**')
  st.write("---")
  st.write(" ")
  st.markdown('### Goles Anotados y Minutos por Gol por Equipo')
  st.write('''El análisis de goles anotados y minutos por gol en la Premier League revela la disparidad en la eficiencia ofensiva entre los equipos,
  con Manchester City FC y Liverpool FC liderando la liga en términos de puntuación eficiente. Este tipo de análisis no solo proporciona información
  valiosa para los fanáticos y seguidores del fútbol interesados en evaluar el desempeño de sus equipos favoritos, sino que también es crucial para entrenadores,
  directores técnicos y gerentes de clubes, ya que les permite evaluar la eficacia de sus estrategias ofensivas y tomar decisiones informadas para mejorar el rendimiento
  de sus equipos en futuras temporadas. Además, los analistas de datos deportivos y las casas de apuestas también pueden aprovechar estos datos para desarrollar modelos de
  pronóstico y mejorar la toma de decisiones en el mundo del fútbol.''')

  # Crear un DataFrame con los datos
  data = {
      'team_name': equipos['team_name'],
      'goals_scored': equipos['goals_scored'],
      'minutes_per_goal_scored': equipos['minutes_per_goal_scored']
  }

  df = pd.DataFrame(data)

  # Ordenar el DataFrame por goles anotados de mayor a menor
  df = df.sort_values(by='goals_scored', ascending=False)

  # Crear el gráfico de barras utilizando Plotly
  fig1 = px.bar(df, x='team_name', y='goals_scored', text='minutes_per_goal_scored',
              labels={'team_name': 'Equipo', 'goals_scored': 'Goles Anotados', 'minutes_per_goal_scored': 'Minutos por Gol'},
              title='Goles Anotados y Minutos por Gol por Equipo')

  # Personalizar el diseño del gráfico
  fig1.update_traces(texttemplate='%{text} min', textposition='inside')
  fig1.update_layout(xaxis={'categoryorder': 'total descending'})

  # Mostrar el gráfico
  st.plotly_chart(fig1)

  ###########
  st.write("---")
  st.markdown('### Tiros de esquinas por Partido por Equipo')
  st.write('''
  Calcular y analizar los promedios de tiros de esquina por equipo en la Premier League es de gran importancia en diversas áreas del deporte y las apuestas deportivas.
  Estos datos ofrecen una visión detallada de la estrategia de juego de cada equipo, tanto en casa como fuera. Para entrenadores y estrategas, estos promedios proporcionan
  información clave sobre el enfoque táctico de un equipo, destacando si priorizan la posesión y el ataque a lo largo de la banda o en áreas de pelota parada, lo que puede
  influir en sus decisiones tácticas y de alineación. Además, para los analistas de datos deportivos, esta información puede utilizarse para evaluar el desempeño de los
  equipos a lo largo de la temporada y descubrir tendencias que podrían guiar el análisis y la toma de decisiones en el futuro. En el ámbito de las apuestas deportivas,
  estos datos son especialmente valiosos, ya que muchos mercados de apuestas se centran en cuántos tiros de esquina se producirán en un partido, permitiendo a los apostadores
  tomar decisiones más informadas. Esto agrega un elemento adicional de emoción al seguimiento de los partidos de la Premier League y puede ser una herramienta útil para aquellos
  que buscan usar estadísticas a su favor en las apuestas deportivas.''')
  # Crear un DataFrame con los datos
  data2 = {
      'team_name': equipos['team_name'],
      'corners_per_match': equipos['corners_per_match'],
      'corners_per_match_home': equipos['corners_per_match_home'],
      'corners_per_match_away': equipos['corners_per_match_away']
  }

  df4 = pd.DataFrame(data2)
  # Renombrar las columnas en el DataFrame
  df4.rename(columns={
      'corners_per_match': 'Tiros de esquina/Partido',
      'corners_per_match_home': 'Tiros de esquina/Partido Casa',
      'corners_per_match_away': 'Tiros de esquina/Partido Visita'
  }, inplace=True)

  # Crear el gráfico de barras agrupadas
  fig2 = px.bar(df4, x='team_name', y=['Tiros de esquina/Partido', 'Tiros de esquina/Partido Casa', 'Tiros de esquina/Partido Visita'],
                title='Tiros de esquinas por Partido por Equipo')

  # Personalizar el diseño del gráfico
  fig2.update_layout(xaxis={'categoryorder': 'total ascending'})

  # Mostrar el gráfico
  st.plotly_chart(fig2)

  #########
  st.write("---")
  st.markdown('### Relación entre Minutos Jugados y Goles Marcados (Delanteros)')
  st.write('''
  Un análisis de la relación entre los minutos jugados y los goles marcados es una herramienta valiosa para evaluar el rendimiento de los jugadores en un equipo y
  para el área de scouting en la búsqueda de posibles fichajes. Para los equipos, este análisis permite identificar a los jugadores más efectivos en términos de su
  capacidad para convertir goles en menos tiempo de juego, lo que puede ser crucial al tomar decisiones sobre alineaciones, sustituciones y estrategias. Además, ayuda a
  identificar a aquellos jugadores que son particularmente eficientes en su producción goleadora, lo que es esencial para equipos con presupuestos limitados que buscan
  maximizar su rendimiento con recursos disponibles.

  En el ámbito del scouting, esta métrica se convierte en un criterio fundamental para evaluar a posibles fichajes. Los equipos buscan jugadores que puedan tener un impacto
  inmediato en el marcador, y aquellos con una alta relación entre minutos jugados y goles marcados son considerados activos valiosos. Este análisis no solo puede ayudar a
  identificar talento emergente, sino también a evitar inversiones costosas en jugadores que no rinden de manera eficiente. En resumen, la relación entre minutos jugados y
  goles marcados es una métrica clave para mejorar el rendimiento de los equipos y optimizar las decisiones de fichaje en el mundo del fútbol.''')
  # Filtrar jugadores que sean delanteros
  delanteros = jugadores[jugadores['position'] == 'Forward']

  # Widget para seleccionar la cantidad de jugadores a mostrar
  top_players = st.slider("Seleccionar Top N jugadores:", min_value=1, max_value=len(delanteros), value=10)

  # Filtrar los primeros N jugadores
  top_delanteros = delanteros.nlargest(top_players, 'goals_overall')

  # Crear el Scatter Plot para los mejores jugadores
  fig_top = px.scatter(top_delanteros, x='minutes_played_overall', y='goals_overall', text='full_name',
                      hover_data=['goals_per_90_overall'],
                      labels={'minutes_played_overall': 'Minutos Jugados','full_name':'Nombre', 'goals_overall': 'Goles','goals_per_90_overall':'Goles por 90 minutos'},
                      title=f'Top {top_players} Delanteros con más Goles en relación con minutos jugados')

  # Personalizar el diseño del gráfico
  fig_top.update_traces(textposition='top center', textfont_size=10)
  fig_top.update_layout(showlegend=False, xaxis_title='Minutos Jugados', yaxis_title='Goles')

  # Mostrar el gráfico
  st.plotly_chart(fig_top)

########
  st.write('''
  De igual forma se pueden hacer distintas graficas de dispersion enfocandonos en otros variables como el siguiente:
  ''')

  fig4 = px.scatter(jugadores, x='appearances_overall', y='assists_overall', size='assists_overall',
                  color='position', hover_name='full_name',
                  labels={'assists_overall': 'Asistencias Totales', 'appearances_overall': 'Partidos Jugados'},
                  title='Relación entre asistencias y Partidos Jugados por Jugador')

  fig4.show()
  st.plotly_chart(fig4)

###############################

if selected3 == 'Mapas':

  st.header('Mapa de jugadores por paises')
  st.write('''
  **Diversidad Cultural y Atracción Global:** La Premier League es una de las ligas de fútbol más vistas y seguidas en todo el mundo. Contar con jugadores de diversas nacionalidades contribuye a la diversidad cultural y atrae a aficionados de diferentes partes del mundo. Esto puede aumentar la base de seguidores y expandir la marca de la liga internacionalmente.

  **Marketing y Comercialización:** Con jugadores de diferentes países, la liga puede aprovechar estas diversidades para estrategias de marketing y comercialización. Pueden personalizar campañas y promociones para llegar a audiencias específicas en función de la nacionalidad de los jugadores.

  **Desarrollo de Talentos y Scouting:** Analizar la distribución geográfica de los jugadores en la liga puede ayudar en el desarrollo de talentos y en la identificación de regiones que están produciendo jugadores destacados. Los clubes pueden ajustar sus estrategias de captación y scouting en consecuencia.

  **Atracción de Patrocinadores Internacionales:** La presencia de jugadores internacionales puede hacer que la liga sea más atractiva para patrocinadores globales que buscan llegar a audiencias en todo el mundo.
  ''')


  # Ajustar manualmente para Estados Unidos
  jugadores['nationality'] = jugadores['nationality'].replace({'USA': 'United States'})

  # Agrupar los países del Reino Unido
  reino_unido_aliases = ['England', 'Scotland', 'Wales', 'Northern Ireland']
  jugadores['nationality'] = jugadores['nationality'].replace({alias: 'United Kingdom' for alias in reino_unido_aliases})

  # Diccionario para asignar manualmente códigos de país
  custom_country_codes = {
      'Venezuela': 'VEN',
      'Iran': 'IRN',
      'Republic of Ireland': 'IRL',
      'Congo DR': 'COD',
      'Ivory Coast': 'CIV',
      'South Korea': 'KOR',
      'Czech Republic': 'CZE'
  }

  # Aplicar la lógica de cambio de códigos de país
  jugadores['Country Code'] = jugadores['nationality'].apply(lambda x: pycountry.countries.get(name=x).alpha_3 if pycountry.countries.get(name=x) else custom_country_codes.get(x))

  # Conteo de jugadores por país
  conteo_pais = jugadores[['Country Code','nationality']].value_counts().reset_index()
  conteo_pais.columns = ['Country Code','nationality', 'Player Count']

  # Crear el mapa geográfico
  fig5 = px.choropleth(conteo_pais,
                      locations='Country Code',
                      color="Player Count",
                      hover_name="nationality",
                      color_continuous_scale=px.colors.sequential.Brwnyl,
                      title="Conteo de Jugadores por País")

  # Mostrar el mapa
  st.write(fig5)

######

if selected3 == 'KPIs':

  # Crear una lista de nombres de equipos
  equipos_list = equipos['team_name'].tolist()

  logo_col, esp_col = st.columns([0.3,0.7])

  with esp_col:
    # Crear una opción para seleccionar el equipo
    selected_team = st.selectbox("Selecciona un equipo", equipos_list)
    # Fila debajo de col3
    with st.container():
        st.write(" ")
        st.write(" ")
        selected_tipo = st.selectbox("Selecciona tipo de juego", ['General', 'Casa', 'Visitante'])

  with logo_col:
    # Mostrar el logo del equipo seleccionado
    logo_path = f"archivos/{selected_team}.png"
    logo = Image.open(logo_path)
    st.image(logo, caption=f"Logo de {selected_team}", use_column_width=True)


  #title_col, emp_col, btc_col, eth_col, xmr_col, sol_col, xrp_col = st.columns([1.4,0.2,1,1,1,1,1])
  title_col, emp_col, k1, k2, k3 = st.columns([1.4,0.2,1,1,1])
  title_col2, emp_col2, k4, k5, k6 = st.columns([1.4,0.2,1,1,1])
  equipo_seleccionado = equipos[equipos['team_name'] == selected_team]

  # Determinar qué KPIs mostrar según el tipo seleccionado
  if selected_tipo == 'General':
    kpi_prefix = ''
  elif selected_tipo == 'Casa':
      kpi_prefix = '_home'
  elif selected_tipo == 'Visitante':
      kpi_prefix = '_away'

  with title_col:
    st.markdown(f'<p class="dashboard_title">{selected_team}</p>', unsafe_allow_html = True)


  with k1:
    kpi1= equipo_seleccionado[f'average_possession{kpi_prefix}'].values[0]
    with st.container():
      kpi1_formatted = f"{kpi1}%"
      st.markdown(f'<p class="kpi1_text">Posesión / Partido<br></p><p class="price_details">{kpi1_formatted}</p>', unsafe_allow_html=True)


  with k2:
    kpi2=equipo_seleccionado[f'clean_sheet_percentage{kpi_prefix}'].values[0]
    with st.container():
          kpi2_formatted = f"{kpi2}%"
          st.markdown(f'<p class="kpi2_text">Porterias / limpias<br></p><p class="price_details">{kpi2_formatted}</p>', unsafe_allow_html = True)

  with k3:
    kpi3= equipo_seleccionado[f'win_percentage{kpi_prefix}'].values[0]
    with st.container():
            kpi3_formatted = f"{kpi3}%"
            st.markdown(f'<p class="kpi5_text">Porcentaje ganar / Partido<br></p><p class="price_details">{kpi3_formatted}</p>', unsafe_allow_html = True)

  with k4:
      kpi4=equipo_seleccionado[f'average_total_goals_per_match{kpi_prefix}'].values[0]
      with st.container():
          st.markdown(f'<p class="kpi4_text">Goles / Partido<br></p><p class="price_details">{kpi4}</p>', unsafe_allow_html = True)

  with k5:
    kpi5=equipo_seleccionado[f'goals_scored_per_match{kpi_prefix}'].values[0]
    with st.container():
        st.markdown(f'<p class="kpi5_text" style="margin-bottom: 10px;">Goles anotados / Partido<br></p><p class="price_details">{kpi5}</p>', unsafe_allow_html=True)

  with k6:
    kpi6=equipo_seleccionado[f'goals_conceded_per_match{kpi_prefix}'].values[0]
    with st.container():
        st.markdown(f'<p class="kpi2_text" style="margin-bottom: 10px;">Goles condedidos / Partido<br></p><p class="price_details">{kpi6}</p>', unsafe_allow_html=True)


  kpi_values = [
      equipo_seleccionado[f'average_total_goals_per_match{kpi_prefix}'].values[0],
      equipo_seleccionado[f'goals_scored_per_match{kpi_prefix}'].values[0],
      equipo_seleccionado[f'goals_conceded_per_match{kpi_prefix}'].values[0],
      round(equipo_seleccionado[f'shots_on_target{kpi_prefix}'].values[0] / equipo_seleccionado[f'matches_played{kpi_prefix}'].values[0],2)
  ]

  # Nombres de las KPI
  kpi_names = [
      'Goles/partido',
      'Goles anotados/partido',
      'Goles concedidos/partido',
      'Tiros a Puerta/partido'
  ]

  # Crear un DataFrame con los datos
  df = pd.DataFrame({'KPI': kpi_names, 'Valor': kpi_values})

  # Crear el gráfico de radar con Plotly Express
  fig = px.line_polar(df, r='Valor', theta='KPI', line_close=True)

  # Agregar etiquetas de texto a los puntos
  fig.update_traces(
      text=df['Valor'].map(lambda x: f"{x}"),
      hoverinfo='text+name',
      mode='text'
  )

  # Configuraciones adicionales del gráfico
  fig.update_traces(fill='toself')
  fig.update_layout(
      polar=dict(
          radialaxis=dict(
              visible=True,
              range=[0, 9]  # Puedes ajustar el rango según tus datos
          ),
      ),
  )

  # Mostrar el gráfico en Streamlit
  st.plotly_chart(fig)
