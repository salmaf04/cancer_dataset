from dash import html
from data import (
    histograma_age,
    heatmap_correlacion,
    frecuencias_level,
    boxplots_factores,
    tabla_resumen,
    barras_factores_por_nivel 
)
from interpretation_layaout import (
    interpretacion_resumen,
    interpretacion_edades,
    interpretacion_graficos_caja,
    interpretacion_matriz_correlacion,
    interpretacion_comparacion_factores
)

data_layout = html.Div([
     html.H2("Descripción del Dataset"),
    html.P("""
        Este dataset contiene información sobre pacientes con cáncer, enfocándose en diversos factores que podrían estar relacionados con la enfermedad. 
        Los datos incluyen variables demográficas, factores de riesgo ambientales y genéticos, hábitos de vida, síntomas clínicos y el nivel de riesgo de cáncer.
        El estudio del cáncer es fundamental para comprender hábitos de vida que pueden influir, factores de riesgo y
        principales síntomas. A través del análisis de datos estadísticos, podemos identificar patrones y correlaciones
        en los síntomas, así como identificar factores que afectan el nivel de avance de esta enfermedad.
    """),
    html.H3("Campos del Dataset"),
    html.Ul([
        html.Li("Patient_Id: Identificador único del paciente (P1, P2, ...)."),
        html.Li("Age: Edad del paciente."),
        html.Li("Gender: Género del paciente (1: Masculino, 2: Femenino)."),
        html.Li("Air_Pollution: Nivel de exposición a la contaminación del aire (escala 1-10)."),
        html.Li("Alcohol_Use: Nivel de consumo de alcohol (escala 1-10)."),
        html.Li("Dust_Allergy: Nivel de alergia al polvo (escala 1-10)."),
        html.Li("Occupational_Hazards: Nivel de exposición a riesgos laborales (escala 1-10)."),
        html.Li("Genetic_Risk: Nivel de riesgo genético (escala 1-10)."),
        html.Li("Chronic_Lung_Disease: Presencia de enfermedad pulmonar crónica (escala 1-10)."),
        html.Li("Balanced_Diet: Nivel de dieta equilibrada (escala 1-10)."),
        html.Li("Obesity: Nivel de obesidad (escala 1-10)."),
        html.Li("Smoking: Nivel de tabaquismo (escala 1-10)."),
        html.Li("Passive_Smoker: Nivel de exposición al humo de segunda mano (escala 1-10)."),
        html.Li("Chest_Pain: Nivel de dolor en el pecho (escala 1-10)."),
        html.Li("Coughing_of_Blood: Nivel de tos con sangre (escala 1-10)."),
        html.Li("Fatigue: Nivel de fatiga (escala 1-10)."),
        html.Li("Weight_Loss: Nivel de pérdida de peso (escala 1-10)."),
        html.Li("Shortness_of_Breath: Nivel de dificultad para respirar (escala 1-10)."),
        html.Li("Wheezing: Nivel de sibilancias (escala 1-10)."),
        html.Li("Swallowing_Difficulty: Nivel de dificultad para tragar (escala 1-10)."),
        html.Li("Clubbing_of_Finger_Nails: Nivel de acropaquia (escala 1-10)."),
        html.Li("Frequent_Cold: Nivel de resfriados frecuentes (escala 1-10)."),
        html.Li("Dry_Cough: Nivel de tos seca (escala 1-10)."),
        html.Li("Snoring: Nivel de ronquidos (escala 1-10)."),
        html.Li("Level: Nivel de riesgo de cáncer (Low, Medium, High)."),
    ]),
    html.H3("Objetivo del Análisis"),
    html.P("""
        El objetivo principal es identificar patrones y relaciones entre los factores de riesgo y el nivel de cáncer, con el fin de 
        determinar qué variables tienen un impacto significativo en el nivel de riesgo de cáncer y proporcionar insights para la prevención y el diagnóstico temprano.
    """),
])

describe_layout = html.Div([
    html.H2("Resumen Estadístico"),
    html.P("""
        El resumen estadístico proporciona una visión general de las variables numéricas, incluyendo la media, mediana, desviación estándar y moda.
        Esto nos ayuda a entender la distribución de los datos y detectar posibles valores atípicos.
    """),
    tabla_resumen,
    interpretacion_resumen,
    
    html.H2("Distribución de Edades"),
    html.P("""
        La distribución de edades nos permite entender la demografía de los pacientes y detectar patrones relacionados con la edad.
    """),
    histograma_age,
    interpretacion_edades,
    
    html.H2("Distribución de Factores de Riesgo"),
    html.P("""
        Los gráficos de caja muestran la distribución de los factores de riesgo agrupados en categorías. 
        Esto nos ayuda a identificar patrones, valores atípicos, y relaciones que pueden influir en la salud y 
        el bienestar. Al interpretar estos gráficos, podemos obtener información valiosa sobre la centralidad y 
        variabilidad de cada factor, lo que facilita la identificación de áreas críticas que requieren atención o 
        intervención.
    """),
    *boxplots_factores,
    interpretacion_graficos_caja,
    
    html.H2("Matriz de Correlación"),
    html.P("""
        La matriz de correlación es una herramienta estadística crucial para analizar la relación entre múltiples 
        variables en un conjunto de datos, especialmente en contextos complejos como el estudio de síntomas y estilos de 
        vida en personas con cáncer. En este caso, la matriz de correlación permite identificar cómo factores de estilo
        de vida, como el tabaquismo, el consumo de alcohol, la exposición a la contaminación del aire, y otros factores 
        ambientales y clínicos, se relacionan entre sí y con la presencia de síntomas específicos. Al visualizar estas 
        correlaciones, podemos detectar patrones y asociaciones significativas que podrían indicar interdependencias o 
        influencias mutuas entre los factores de riesgo y los síntomas del cáncer.
    """),
    heatmap_correlacion,
    interpretacion_matriz_correlacion,
    
    html.H2("Frecuencias y Proporciones de Niveles de Riesgo"),
    html.P("""
        Las frecuencias y proporciones de los niveles de riesgo nos permiten entender la distribución de los pacientes en las categorías Low, Medium y High.
    """),
    frecuencias_level,
    
    html.H2("Comparación de Factores por Nivel de Riesgo"),
    html.P("""
        El gráfico de barras muestra la media de cada variable por nivel de riesgo. Esto nos ayuda a identificar diferencias significativas entre los grupos.
    """),
    barras_factores_por_nivel,
    interpretacion_comparacion_factores,
])