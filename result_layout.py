from dash import html
from data import (
    chi2_genetic, 
    p_genetic, 
    chi2_smoking, 
    p_smoking, 
    chi2_alcohol, 
    p_alcohol, 
    chi2_obesity, 
    p_obesity, 
    table_genetic, 
    table_smoking, 
    table_alcohol, 
    table_obesity,
    create_html_table
)
chi_layout = html.Div(children=[
    html.H1("Análisis Inferencial del Dataset de Cáncer"),
    
    html.H2("Riesgo Genético vs. Nivel de Riesgo"),
    html.P("""
        Dado que el riesgo genético mostró variabilidad en los niveles de riesgo, esta prueba evalúa si existe 
        una asociación significativa entre la predisposición genética y el nivel de riesgo de cáncer.
    """),
    create_html_table(table_genetic, ['Bajo', 'Medio', 'Alto'], ['Alto', 'Bajo', 'Medio']),
    html.P(f"Chi2: {chi2_genetic:.2f}, p-valor: {p_genetic:.4f}"),
    html.P("""
        La prueba muestra una asociación significativa entre el riesgo genético y el nivel de riesgo de cáncer. 
        Un p-valor de 0.0000 indica que es altamente improbable que esta asociación sea debida al azar. 
        Esto sugiere que la predisposición genética es un factor importante en la determinación del nivel de riesgo de cáncer.
    """),
    
    html.H2("Tabaquismo vs. Dolor en el Pecho"),
    html.P("""
        La correlación observada entre tabaquismo y dolor en el pecho sugiere una posible relación significativa. 
        Esta prueba confirma si el tabaquismo está asociado con la presencia de dolor en el pecho.
    """),
    create_html_table(table_smoking, ['Bajo', 'Medio', 'Alto'], ['Sin Dolor', 'Con Dolor']),
    html.P(f"Chi2: {chi2_smoking:.2f}, p-valor: {p_smoking:.4f}"),
    html.P("""
        Existe una relación significativa entre el tabaquismo y la presencia de dolor en el pecho. 
        El p-valor extremadamente bajo indica que el tabaquismo podría ser un factor de riesgo importante para el desarrollo de síntomas como el dolor en el pecho.
    """),
    
    html.H2("Consumo de Alcohol vs. Nivel de Riesgo"),
    html.P("""
        Dado que el consumo de alcohol mostró variaciones en los niveles de riesgo, esta prueba determina si 
        el consumo de alcohol está asociado con diferentes niveles de riesgo de cáncer.
    """),
    create_html_table(table_alcohol, ['Bajo', 'Medio', 'Alto'], ['Alto', 'Bajo', 'Medio']),
    html.P(f"Chi2: {chi2_alcohol:.2f}, p-valor: {p_alcohol:.4f}"),
    html.P("""
        La prueba indica una asociación significativa entre el consumo de alcohol y el nivel de riesgo de cáncer. 
        El p-valor sugiere que el consumo de alcohol puede influir en el riesgo de desarrollar cáncer.
    """),
    
    html.H2("Obesidad vs. Dificultad para Respirar"),
    html.P("""
        La relación entre obesidad y dificultad para respirar puede ser significativa. Esta prueba explora si 
        la obesidad está asociada con la presencia de dificultad para respirar.
    """),
    create_html_table(table_obesity, ['Bajo', 'Medio', 'Alto'], ['Sin Dificultad', 'Con Dificultad']),
    html.P(f"Chi2: {chi2_obesity:.2f}, p-valor: {p_obesity:.4f}"),
    html.P("""
        Hay una asociación significativa entre la obesidad y la dificultad para respirar. 
        Este resultado sugiere que la obesidad puede contribuir a problemas respiratorios.
    """),
    
    html.H2("Conclusiones Generales"),
    html.P("""
        Todos los p-valores son extremadamente bajos, indicando asociaciones significativas en todas las pruebas. 
        Estos resultados pueden guiar intervenciones y estrategias de prevención, enfocándose en la reducción de factores de riesgo como el tabaquismo y el consumo de alcohol. 
        La identificación de estas asociaciones puede ayudar en el diagnóstico temprano y en la personalización de tratamientos para pacientes con diferentes niveles de riesgo.
    """)
])
