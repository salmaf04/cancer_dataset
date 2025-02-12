import dash
from data_layout import data_layout, describe_layout
from dash import html
from result_layout import chi_layout, anova_layout, regression_layout, gender_layout


# Nueva función para generar el gráfico de barras


app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Estudio sobre pacientes con cáncer"),
    data_layout,
    describe_layout,
    chi_layout,
    anova_layout,
    regression_layout,
    gender_layout,
    html.H2("Conclusiones"),
    html.P("""
        En este proyecto se llevaron a cabo diversas pruebas estadísticas y análisis para evaluar la relación entre 
        factores de riesgo, síntomas y niveles de riesgo de cáncer en los pacientes. A través de pruebas de normalidad 
        (Shapiro-Wilk), análisis de regresión lineal, pruebas ANOVA y pruebas de chi-cuadrado, se exploraron las 
        interacciones entre variables como la edad, el consumo de alcohol, el tabaquismo, la obesidad, el riesgo genético
        y otros factores ambientales y clínicos.
    """),
    html.P("""
        Los resultados indican que, aunque la edad no es un predictor significativo del nivel de riesgo de cáncer, 
        otros factores como el tabaquismo, la obesidad y el riesgo genético están fuertemente asociados con un mayor 
        riesgo de desarrollar la enfermedad. Además, se encontraron relaciones significativas entre síntomas como la 
        tos con sangre, el dolor en el pecho y la dificultad para respirar, lo que sugiere que estos síntomas pueden 
        estar interconectados y ser indicadores de condiciones subyacentes comunes.
    """),
        html.P("""
            En cuanto a las diferencias por género, se observó que los hombres tienen una mayor prevalencia de tabaquismo
            y consumo de alcohol, lo que podría explicar en parte la mayor incidencia de ciertos síntomas como el dolor 
            en el pecho en este grupo. Por otro lado, los análisis de ANOVA revelaron diferencias significativas en el 
            consumo de alcohol, el riesgo genético y la obesidad entre los niveles de riesgo de cáncer, aunque los 
            supuestos de normalidad y homocedasticidad no se cumplieron en todos los casos.
    """),
        html.P("""
            En conjunto, estos hallazgos subrayan la complejidad de las interacciones entre los factores de riesgo, los 
            síntomas y el nivel de riesgo de cáncer. Se evidencia la importancia de considerar múltiples factores al 
            evaluar el riesgo de cáncer y diseñar estrategias de prevención y diagnóstico temprano.
    """),
])

if __name__ == '__main__':
   app.run_server(debug=True)