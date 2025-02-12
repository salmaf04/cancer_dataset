from dash import html

interpretacion_resumen = html.Div([
    html.H2("Interpretación del Resumen Estadístico"),
    html.P("""
        El resumen estadístico nos proporciona información valiosa sobre las variables numéricas en el dataset. 
        Aquí se destacan algunos puntos clave:
    """),
    html.Ul([
        html.Li("""
            La media de la edad es 37.17 años, indicando que la mayoría de los pacientes están en la mediana edad, 
            un grupo demográfico crítico para el estudio del cáncer.
        """),
        html.Li("""
            La desviación estándar alta en la edad (12.01) sugiere una amplia variabilidad, lo que puede ayudar a identificar 
            grupos de riesgo específicos.
        """),
        html.Li("""
            La moda de 7 en variables como `Air Pollution` y `Smoking` indica niveles frecuentes de exposición, 
            sugiriendo que estos son factores de riesgo comunes que merecen atención.
        """),
        html.Li("""
            Los percentiles muestran que un gran porcentaje de pacientes tiene niveles elevados en factores como `Smoking`, 
            lo cual es un conocido factor de riesgo para el cáncer.
        """),
        html.Li("""
            Variables con baja media y desviación estándar, como `Frequent Cold`, podrían ser menos relevantes para el estudio del cáncer, 
            permitiendo enfocar los recursos en factores más significativos.
        """),
        html.Li("""
            La baja variabilidad en `Chronic Lung Disease` junto con una media relativamente alta sugiere que podría ser un indicador significativo 
            a estudiar más a fondo.
        """)
    ]),
    html.P("""
        Este análisis inicial nos ayuda a priorizar qué variables estudiar más a fondo y a identificar patrones que podrían indicar correlaciones 
        significativas con el cáncer. Al entender la distribución y variabilidad de los datos, podemos diseñar estudios más efectivos y enfocar 
        los esfuerzos en la prevención y diagnóstico temprano.
    """)
])

# Interpretación de la distribución de edades
interpretacion_edades = html.Div([
    html.H2("Interpretación de la Distribución de Edades"),
    html.P("""
        La distribución de edades nos proporciona una visión clara de la demografía de los pacientes. 
        Visualmente, podemos observar varios aspectos importantes:
    """),
    html.Ul([
        html.Li("""
            Como se vio en el resumen estadístico, la media de la edad es 37.17 años. 
            El histograma confirma que la mayoría de los pacientes se encuentran en el rango de 30 a 40 años, 
            lo que representa un grupo demográfico significativo para el estudio del cáncer.
        """),
        html.Li("""
            Hay una notable concentración de pacientes en la mediana edad, lo que sugiere que este grupo podría estar 
            más afectado o ser más propenso a realizarse pruebas de detección.
        """),
        html.Li("""
            La variabilidad en las edades, con pacientes desde los 20 hasta los 70 años, indica que el cáncer afecta 
            a una amplia gama de edades, aunque con mayor frecuencia en ciertos grupos.
        """),
        html.Li("""
            Los picos en el histograma alrededor de los 30 y 40 años podrían indicar la necesidad de enfocar 
            campañas de prevención y diagnóstico temprano en estos grupos de edad.
        """)
    ]),
    html.P("""
        Este análisis visual complementa el resumen estadístico y nos ayuda a identificar patrones demográficos 
        que podrían ser relevantes para la investigación y la planificación de intervenciones de salud pública.
    """)
])

interpretacion_graficos_caja = html.Div([
    html.H2("Interpretación de los Gráficos de Caja"),
    html.P("""
        Los gráficos de caja proporcionan una visión detallada de la distribución de diferentes factores que pueden influir en la salud de los pacientes. 
        A continuación, se presenta una interpretación de cada categoría de factores:
    """),
    
    html.H3("Factores Ambientales"),
    
    html.P("""
        En la distribución de factores ambientales, observamos que la contaminación del aire tiene una caja que se 
        extiende de 2 a 6, con una mediana en 3. Esto indica que la mayoría de los valores se encuentran en este rango,
        con un sesgo hacia valores más bajos, ya que la mediana está más cerca del límite inferior. Los bigotes se 
        extienden desde 1 hasta 8, sugiriendo que hay algunos valores extremos en ambos extremos. Para riesgos 
        laborales, la caja va de 3 a 7 con una mediana de 5, lo que sugiere una distribución más centrada y simétrica 
        en comparación con la contaminación del aire. Los bigotes también van de 1 a 8, indicando la presencia de 
        valores extremos. En el caso de fumador pasivo, la caja se extiende de 2 a 7 con una mediana de 4, mostrando 
        una distribución ligeramente sesgada hacia valores más bajos, con bigotes que van de 1 a 8, lo que indica 
        variabilidad en los datos.
    """),

    
    html.H3("Factores de Estilo de Vida"),
    html.P("""
        Para los factores de estilo de vida, el consumo de alcohol muestra una caja de 2 a 7 con una mediana de 5, 
        lo que sugiere una distribución centrada con valores extremos en ambos lados, ya que los bigotes van de 1 a 8. 
        En tabaquismo, la caja también va de 2 a 7, pero la mediana es 3, indicando una tendencia hacia valores más bajos.
        Los bigotes de 1 a 8 sugieren variabilidad. La dieta equilibrada tiene una caja de 2 a 7, con una mediana de 4, y
        bigotes de 1 a 7, lo que indica una distribución más uniforme sin valores extremos superiores. En obesidad, la 
        caja va de 3 a 7 con una mediana de 4, y bigotes de 1 a 7, sugiriendo una distribución más centrada y simétrica.
    """),
    
    html.H3("Factores Clínicos"),
    html.P("""
        En la distribución de factores clínicos, el dolor de pecho tiene una caja de 2 a 7 con una mediana de 4, y 
        bigotes de 1 a 9, indicando una amplia variabilidad y algunos valores extremos. La tos con sangre muestra una 
        caja de 3 a 7 con una mediana de 4, y bigotes de 1 a 9, sugiriendo una distribución similar. Fatiga tiene una 
        caja más estrecha de 2 a 5, con una mediana de 3, y bigotes de 1 a 9, lo que indica una concentración de valores 
        en el rango inferior. La pérdida de peso tiene una caja de 2 a 6, con una mediana de 3, y bigotes de 1 a 8, 
        sugiriendo una distribución sesgada hacia valores más bajos. Dificultad para respirar y sibilancias tienen 
        cajas de 2 a 6 y 2 a 5 respectivamente, ambas con medianas de 4, y bigotes que indican variabilidad. Dificultad 
        para tragar y resfriados frecuentes muestran cajas de 2 a 5, con medianas de 4 y 3 respectivamente, y bigotes que
        sugieren una distribución más concentrada. Finalmente, tos seca tiene una caja de 2 a 6, con una mediana de 4, y 
        bigotes de 1 a 7, indicando una distribución más uniforme.
    """),
    
    html.H3("Factores Genéticos"),
    html.P("""
        En la distribución de factores genéticos, el riesgo genético tiene una caja de 2 a 7, con una mediana de 5, y un 
        bigote inferior que llega a 1, lo que sugiere una distribución centrada con algunos valores extremos inferiores. 
        La enfermedad pulmonar crónica muestra una caja de 3 a 6, con una mediana de 4, y bigotes de 1 a 7, indicando una
        distribución más centrada y simétrica con menos variabilidad en comparación con el riesgo genético.
    """),
])

# Interpretación de la matriz de correlación
interpretacion_matriz_correlacion = html.Div([
    html.H2("Interpretación de la Matriz de Correlación"),
    html.P("""
        La matriz de correlación nos proporciona una visión clara de las relaciones lineales entre las variables numéricas del dataset. 
        A continuación, se destacan algunas correlaciones significativas:
    """),
    html.Ul([
        html.Li("""
            **Obesidad y Tos con Sangre:**Se observan relaciones significativas entre la obesidad y la tos con sangre, 
            pues su correlación es cercana a 1, lo cual indica que la tos con sangre puede ser un síntoma influenciado 
            por la obesidad del paciente.  .
        """),
        html.Li("""
            **Pérdida de Peso y Dificultad para Respirar:** También presentan una correlación positiva, lo que podría 
            indicar que estos síntomas están relacionados y podrían ser indicadores de condiciones subyacentes similares.
        """),
        html.Li("""
            **Tabaquismo y Dolor en el Pecho:** La correlación positiva entre estas variables sugiere que el tabaquismo podría estar 
            relacionado con la aparición de dolor en el pecho, un conocido factor de riesgo para enfermedades respiratorias.
        """),
        html.Li("""
            **Consumo de Alcohol y Riesgo Genético:** Aunque la correlación es más moderada, podría indicar un patrón de comportamiento 
            o predisposición genética que merece un estudio más detallado.
        """),
        html.Li("""
            **Riesgos Laborales y Enfermedad Pulmonar Crónica:** La correlación observada sugiere que los riesgos 
            laborales podrían estar relacionados con la enfermedad pulmonar crónica.
        """),
        html.Li("""
            **Tos Seca y Frío Constante:** También presentan una correlación positiva, lo que podría 
            indicar que estos síntomas están relacionados y podrían ser indicadores de condiciones subyacentes similares.
        """),
        html.Li("""
            **Fumador Pasivo y Fumador Activo:** La correlación observada sugiere que el fumador pasivo podría estar relacionados
            con el fumador activo, indicando como el entorno puedo influir en la decisión de fumar.
            del aire podría estar relacionados con la enfermedad pulmonar crónica.
        """),
        html.Li("""
            **Contaminación del aire y Enfermedad Pulmonar Crónica:** La correlación observada sugiere que la contaminación
            del aire podría estar relacionados con la enfermedad pulmonar crónica.
        """),
        html.Li("""
            **Dolor en el Pecho y Enfermedad Pulmunar Crónica:** También presentan una correlación positiva, lo que podría 
            indicar que estos síntomas están relacionados y podrían ser indicadores de condiciones subyacentes similares.
        """),
    ]),
    html.P("""
        Este análisis visual es fundamental para identificar patrones y relaciones que podrían ser relevantes para la investigación 
        y la planificación de intervenciones de salud pública. Las correlaciones significativas pueden guiar estudios más detallados 
        y ayudar a identificar factores de riesgo conjuntos.
    """)
])

# Interpretación de la comparación de factores por nivel de riesgo
interpretacion_comparacion_factores = html.Div([
    html.H2("Interpretación de la Comparación de Factores por Nivel de Riesgo"),
    html.P("""
        El gráfico de barras nos permite visualizar cómo varían los diferentes factores según el nivel de riesgo de cáncer. 
        A continuación, se destacan algunas observaciones clave:
    """),
    html.Ul([
        html.Li("""
            **Nivel Alto de Riesgo:** Los factores como `Tabaquismo`, `Obesidad` y `Riesgo Genético` muestran medias más altas en el grupo de alto riesgo, 
            lo que sugiere que estos factores están fuertemente asociados con un mayor riesgo de cáncer.
        """),
        html.Li("""
            **Nivel Medio de Riesgo:** En este grupo, los factores como `Consumo de Alcohol` y `Riesgos Laborales` tienen medias moderadas, 
            indicando una posible contribución al riesgo, aunque menos pronunciada que en el grupo de alto riesgo.
        """),
        html.Li("""
            **Comparación General:** La variación en las medias de los factores entre los diferentes niveles de riesgo resalta la importancia de 
            considerar múltiples factores al evaluar el riesgo de cáncer en los pacientes.
        """)
    ]),
    html.P("""
        Este análisis visual es crucial para identificar qué factores tienen un impacto significativo en el riesgo de cáncer y puede guiar 
        intervenciones de salud pública y estrategias de prevención personalizadas.
    """)
])

