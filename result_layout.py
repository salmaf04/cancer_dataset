from dash import html, dcc
from data import (
    chi2_smoking, p_smoking, table_smoking, 
    create_html_table,
    chi2_genetic_alcohol, p_genetic_alcohol, table_genetic_alcohol,
    chi2_occupational_lung, p_occupational_lung, table_occupational_lung,
    chi2_obesity_cough, p_obesity_cough, table_obesity_cough,
    chi2_breath_weight, p_breath_weight, table_breath_weight,
    chi2_dry_cough_cold, p_dry_cough_cold, table_dry_cough_cold,
    chi2_chest_lung, p_chest_lung, table_chest_lung,
    chi2_air_lung, p_air_lung, table_air_lung,
    chi2_passive_active, p_passive_active, table_passive_active,
    anova_alcohol, shapiro_alcohol_low, shapiro_alcohol_medium, shapiro_alcohol_high, levene_alcohol, fig_alcohol,
    anova_genetic, shapiro_genetic_low, shapiro_genetic_medium, shapiro_genetic_high, levene_genetic, fig_genetic,
    anova_obesity, shapiro_obesity_low, shapiro_obesity_medium, shapiro_obesity_high, levene_obesity, fig_obesity
)
chi_layout = html.Div(children=[
    html.H1("Análisis Inferencial del Dataset de Cáncer"),
    
    html.P("""
        Tras los resultados obtenidos tras obervar la matriz de correlación se quiere comprobar si existe una asociación entre
        algunos síntomas, estilos de vida y factores de riesgo. 
    """),
    
    html.H2("Análisis de la relación entre los síntomas y el estilo de vida"),
    
    html.H3("Obesidad vs. Tos con Sangre"),
    html.P("""
        Evaluar la relación entre la obesidad y la presencia de tos con sangre.
    """),
    create_html_table(table_obesity_cough, ['Bajo', 'Medio', 'Alto'], ['Sin Tos', 'Con Tos']),
    html.P(f"Chi2: {chi2_obesity_cough:.2f}, p-valor: {p_obesity_cough:.4f}"),
    html.P("""
        Esto indica una relación significativa entre la obesidad y la presencia de tos con sangre, en la tabla se observa
        que la obesidad influye negativamente en el desarrollo de este síntoma, lo cual sugiere que la obesidad puede ser un factor de 
        riesgo importante a considerar en el diagnóstico y tratamiento de pacientes.
    """),
    
    html.H3("Tabaquismo vs. Dolor en el Pecho"),
    html.P("""
        La correlación observada entre tabaquismo y dolor en el pecho sugiere una posible relación significativa. 
        Esta prueba confirma si el tabaquismo está asociado con la presencia de dolor en el pecho.
    """),
    create_html_table(table_smoking, ['Bajo', 'Medio', 'Alto'], ['Sin Dolor', 'Con Dolor']),
    html.P(f"Chi2: {chi2_smoking:.2f}, p-valor: {p_smoking:.4f}"),
    html.P("""
        Existe una relación significativa entre el tabaquismo y la presencia de dolor en el pecho. 
        El p-valor extremadamente bajo indica que el tabaquismo podría ser un factor de riesgo importante para el desarrollo de síntomas como el dolor en el pecho
        y con los resultados de la tabla se ve que la influencia del tabaquismo en el desarrolo de este síntoma es negativa.
    """),
    
    html.H3("Cocluiones generales sobre la relación entre el estilo de vida y el desarrollo de los síntomas"),
    html.P("""
        Con estos resultados se puede llegar a la conclusión de que el estilo de vida de cada persona puede influir en los
        síntomas que desarrollen y la gravedad de los mismos. 
    """),
    
     html.H2("Análisis de la relación entre los síntomas y factores de riesgo"),
    
    html.H3("Riesgo Genético vs. Consumo de Alcohol"),
    html.P("""
        Determinar si existe una asociación entre el riesgo genético y el consumo de alcohol.
    """),
    create_html_table(table_genetic_alcohol, ['Bajo', 'Medio', 'Alto'], ['Bajo', 'Medio', 'Alto']),
    html.P(f"Chi2: {chi2_genetic_alcohol:.2f}, p-valor: {p_genetic_alcohol:.4f}"),
    html.P("""
           hay una asociación significativa entre el riesgo genético y el consumo de alcohol.
           Estos resultados sugieren que las personas con diferentes niveles de riesgo genético pueden tener patrones de 
           consumo de alcohol distintos. Enla tabal se observa que el consumo de alcohol es proporcional al riesgo genético,
           pues para bajo nivel de riesgo genético hay más personas que el consumo de alcohol es bajo, mientras que para 
           alto nivel de riesgo genético hay más personas que el consumo de alcohol es alto.
    """),
    
    html.H3("Riesgos Laborales vs. Enfermedad Pulmonar Crónica"),
    html.P("""
        Explorar la relación entre la exposición a riesgos laborales y la presencia de enfermedad pulmonar crónica.
    """),
    create_html_table(table_occupational_lung, ['Bajo', 'Medio', 'Alto'], ['Sin Enfermedad', 'Con Enfermedad']),
    html.P(f"Chi2: {chi2_occupational_lung:.2f}, p-valor: {p_occupational_lung:.4f}"),
        html.P("""
        Hay una asociación significativa entre el riesgos laborales y la presencia de enfermedad pulmunar crónica. En
        la tabla de contingencia se observa que el riesgo laboral influye negativamente en la presencia de enfermedad, pues 
        para el riesgo laboral alto no hay ninguna persona que no presente enfermedad pulmonar crónica.
    """),
        
    html.H3("Contaminación del Aire vs. Enfermedad Pulmonar Crónica"),
    html.P("Evaluar la relación entre la contaminación del aire y la presencia de enfermedad pulmonar crónica."),
    create_html_table(table_air_lung, ['Bajo', 'Medio', 'Alto'], ['Sin Enfermedad', 'Con Enfermedad']),
    html.P(f"Chi2: {chi2_air_lung:.2f}, p-valor: {p_air_lung:.4f}"),
    html.P("""
         Se observa una asociación significativa entre la contaminación del aire y la enfermedad pulmonar crónica.
         La mayoría de los casos de enfermedad pulmonar crónica se encuentran en niveles medios y altos de contaminación
         del aire, lo que sugiere que la exposición a la contaminación es un factor de riesgo importante.
    """),
    
    html.H3("Fumador Pasivo vs. Fumador Activo"),
    html.P("Evaluar la relación entre ser fumador pasivo y activo."),
    create_html_table(table_passive_active, ['Bajo', 'Medio', 'Alto'], ['Bajo', 'Medio', 'Alto']),
    html.P(f"Chi2: {chi2_passive_active:.2f}, p-valor: {p_passive_active:.4f}"),
    html.P("""
        Existe una relación significativa entre ser fumador pasivo y activo. Los niveles altos de fumadores pasivos 
        coinciden con niveles altos de fumadores activos, sugiriendo que el entorno influye en ambos comportamientos.
    """),
        
    html.H3("Cocluiones generales sobre la relación entre los factores de riesgo y el desarrollo de los síntomas"),
    html.P("""
        Con estos resultados se puede llegar a la conclusión de que los factores de riesgo pueden influir en los
        síntomas que desarrollen, e incluso en el estilo de vida de la persona que como se vió anteriormente puede influir
        en lo mismo. 
    """),
    
     html.H2("Análisis de la relación entre los síntomas"),

    html.H3("Tos Seca vs. Frío Constante"),
    html.P("Evaluar la relación entre la tos seca y el frío constante."),
    create_html_table(table_dry_cough_cold, ['Sin Tos', 'Con Tos'], ['Sin Frío', 'Con Frío']),
    html.P(f"Chi2: {chi2_dry_cough_cold:.2f}, p-valor: {p_dry_cough_cold:.4f}"),
    html.P("""
        Se observa una asociación significativa entre la tos seca y el frío constante, lo cual indica que estos síntomas 
        tienden a presentarse juntos.
    """),
    
    html.H3("Dificultad para Respirar vs. Pérdida de Peso"),
    html.P("Explorar la relación entre la dificultad para respirar y la pérdida de peso."),
    create_html_table(table_breath_weight, ['Sin Dificultad', 'Con Dificultad'], ['Sin Pérdida', 'Con Pérdida']),
    html.P(f"Chi2: {chi2_breath_weight:.2f}, p-valor: {p_breath_weight:.4f}"),
    html.P("""
        Existe asociación significativa entre la dificultad para respirar y la pérdida de peso. Esto sugiere que estos 
        síntomas tienden a ocurrir juntos más de lo que se esperaría por azar.
    """),
    
    html.H3("Dolor en el Pecho vs. Enfermedad Pulmonar Crónica"),
    html.P("Explorar la relación entre el dolor en el pecho y la presencia de enfermedad pulmonar crónica."),
    create_html_table(table_chest_lung, ['Sin Dolor', 'Con Dolor'], ['Sin Enfermedad', 'Con Enfermedad']),
    html.P(f"Chi2: {chi2_chest_lung:.2f}, p-valor: {p_chest_lung:.4f}"),
        html.P("""
            Hay una asociación significativa entre el dolor en el pecho y la enfermedad pulmonar crónica. El dolor en el 
            pecho es más común en pacientes con enfermedad pulmonar crónica, lo que sugiere que podría ser un síntoma 
            clave.
    """),
           
    html.H3("Cocluiones generales sobre la relación entre síntomas"),
    html.P("""
        Con estos resultados se puede llegar a la conclusión de que hay síntomas que se suelen presentar juntos, lo que
        muestra la existencia de una condición subyacente común o una respuesta del sistema inmunológico similar. Esto 
        puede ser relevante para el diagnóstico y tratamiento de enfermedades.
    """),
    
])

anova_layout = html.Div(children=[
    html.H2("Análisis de la relación entre los niveles de avance del cáncer y los síntomas"),
    html.P("""
           Teniendo en cuenta las observaciones hechas en el gráfico de barras sobre la media de los síntomas por cada
           nivel de avance del cáncer, a continuación se realizarán pruebas para verificar si hay diferencia significativa
           de la presencia de algunos síntomas entre los niveles de avance del cáncer.
    """),
    
    html.H3("Consumo de Alcohol"),
    html.Table([
        html.Tr([html.Th("Prueba", style={'text-align': 'left'}), html.Th("F-Stat", style={'text-align': 'left'}), html.Th("p-valor", style={'text-align': 'left'})]),
        html.Tr([html.Td("ANOVA"), html.Td(f"{anova_alcohol.statistic:.2f}"), html.Td(f"{anova_alcohol.pvalue:.4f}")]),
        html.Tr([html.Td("Normalidad (Low)"), html.Td(""), html.Td(f"{shapiro_alcohol_low.pvalue:.4f}")]),
        html.Tr([html.Td("Normalidad (Medium)"), html.Td(""), html.Td(f"{shapiro_alcohol_medium.pvalue:.4f}")]),
        html.Tr([html.Td("Normalidad (High)"), html.Td(""), html.Td(f"{shapiro_alcohol_high.pvalue:.4f}")]),
        html.Tr([html.Td("Homogeneidad de Varianzas"), html.Td(""), html.Td(f"{levene_alcohol.pvalue:.4f}")]),
    ], style={'width': '50%', 'margin': '10px 0', 'border': '1px solid black', 'border-collapse': 'collapse'}),
    html.P("""
        La prueba ANOVA indica diferencias significativas en el consumo de alcohol entre los niveles de riesgo. 
        Sin embargo, los supuestos de normalidad y homogeneidad de varianzas no se cumplen, lo que puede afectar la validez de los resultados.
    """),
    dcc.Graph(figure=fig_alcohol),
    
    html.H3("Riesgo Genético"),
    html.Table([
        html.Tr([html.Th("Prueba", style={'text-align': 'left'}), html.Th("F-Stat", style={'text-align': 'left'}), html.Th("p-valor", style={'text-align': 'left'})]),
        html.Tr([html.Td("ANOVA"), html.Td(f"{anova_genetic.statistic:.2f}"), html.Td(f"{anova_genetic.pvalue:.4f}")]),
        html.Tr([html.Td("Normalidad (Low)"), html.Td(""), html.Td(f"{shapiro_genetic_low.pvalue:.4f}")]),
        html.Tr([html.Td("Normalidad (Medium)"), html.Td(""), html.Td(f"{shapiro_genetic_medium.pvalue:.4f}")]),
        html.Tr([html.Td("Normalidad (High)"), html.Td(""), html.Td(f"{shapiro_genetic_high.pvalue:.4f}")]),
        html.Tr([html.Td("Homogeneidad de Varianzas"), html.Td(""), html.Td(f"{levene_genetic.pvalue:.4f}")]),
    ], style={'width': '50%', 'margin': '10px 0', 'border': '1px solid black', 'border-collapse': 'collapse'}),
    html.P("""
        La prueba ANOVA muestra diferencias significativas en el riesgo genético entre los niveles de riesgo. 
        Sin embargo, los supuestos de normalidad y homogeneidad de varianzas no se cumplen, lo que puede afectar la validez de los resultados.
    """),
    dcc.Graph(figure=fig_genetic),
    
    html.H3("Obesidad"),
    html.Table([
        html.Tr([html.Th("Prueba", style={'text-align': 'left'}), html.Th("F-Stat", style={'text-align': 'left'}), html.Th("p-valor", style={'text-align': 'left'})]),
        html.Tr([html.Td("ANOVA"), html.Td(f"{anova_obesity.statistic:.2f}"), html.Td(f"{anova_obesity.pvalue:.4f}")]),
        html.Tr([html.Td("Normalidad (Low)"), html.Td(""), html.Td(f"{shapiro_obesity_low.pvalue:.4f}")]),
        html.Tr([html.Td("Normalidad (Medium)"), html.Td(""), html.Td(f"{shapiro_obesity_medium.pvalue:.4f}")]),
        html.Tr([html.Td("Normalidad (High)"), html.Td(""), html.Td(f"{shapiro_obesity_high.pvalue:.4f}")]),
        html.Tr([html.Td("Homogeneidad de Varianzas"), html.Td(""), html.Td(f"{levene_obesity.pvalue:.4f}")]),
    ], style={'width': '50%', 'margin': '10px 0', 'border': '1px solid black', 'border-collapse': 'collapse'}),
    html.P("""
        La prueba ANOVA indica diferencias significativas en la obesidad entre los niveles de riesgo. 
        Sin embargo, los supuestos de normalidad y homogeneidad de varianzas no se cumplen, lo que puede afectar la validez de los resultados.
    """),
    dcc.Graph(figure=fig_obesity),
])
