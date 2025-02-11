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
    html.Ul([
        html.Li("""
            La mediana de `Contaminación del Aire`, `Riesgos Laborales` y `Fumador Pasivo` está alrededor de 5, 
            indicando niveles moderados de exposición. La variabilidad es similar, sugiriendo que la mayoría de los pacientes 
            experimentan niveles de exposición entre 3 y 7.
        """),
        html.Li("""
            Los valores atípicos en `Contaminación del Aire` y `Fumador Pasivo` indican exposiciones significativamente diferentes 
            en algunos pacientes, lo que podría ser relevante para estudios más detallados.
        """)
    ]),
    
    html.H3("Factores de Estilo de Vida"),
    html.Ul([
        html.Li("""
            La mediana de `Consumo de Alcohol`, `Tabaquismo`, `Dieta Equilibrada` y `Obesidad` está alrededor de 5, 
            indicando niveles moderados en estos hábitos de vida. La variabilidad es similar, con rangos intercuartílicos 
            que sugieren hábitos de vida entre 3 y 7.
        """),
        html.Li("""
            Los valores atípicos en `Tabaquismo` y `Obesidad` indican hábitos significativamente diferentes en algunos pacientes, 
            lo que podría ser relevante para estudios más detallados.
        """)
    ]),
    
    html.H3("Factores Clínicos"),
    html.Ul([
        html.Li("""
            La mediana de síntomas como `Dolor en el Pecho`, `Tos con Sangre`, y `Dificultad para Respirar` está alrededor de 5, 
            indicando una presencia moderada de estos síntomas en los pacientes.
        """),
        html.Li("""
            La variabilidad es notable en síntomas como `Fatiga` y `Pérdida de Peso`, sugiriendo que estos síntomas varían 
            significativamente entre los pacientes.
        """),
        html.Li("""
            Los valores atípicos en varios síntomas indican que algunos pacientes experimentan niveles significativamente diferentes, 
            lo que podría ser relevante para estudios más detallados.
        """)
    ]),
    
    html.H3("Factores Genéticos"),
    html.Ul([
        html.Li("""
            La mediana de `Riesgo Genético` y `Enfermedad Pulmonar Crónica` está alrededor de 5, indicando un nivel moderado de riesgo 
            genético y presencia de enfermedad.
        """),
        html.Li("""
            La variabilidad en `Enfermedad Pulmonar Crónica` sugiere que algunos pacientes tienen una mayor predisposición, 
            lo que podría ser relevante para estudios genéticos más detallados.
        """)
    ]),
    
    html.P("""
        Este análisis visual complementa el resumen estadístico y nos ayuda a identificar patrones de exposición, hábitos de vida, 
        síntomas y predisposiciones genéticas que podrían ser relevantes para la investigación y la planificación de intervenciones 
        de salud pública.
    """)
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

