from dash import dcc, html
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from columns import ColumnNames as cols 
from main import data
import pandas as pd
from scipy.stats import chi2_contingency
from columns import ColumnNames

def generar_tabla_resumen():
    # Seleccionar solo las variables numéricas relevantes
    variables_numericas = [
        cols.Age, cols.Air_Pollution, cols.Alcohol_Use, cols.Occupational_Hazards,
        cols.Genetic_Risk, cols.Chronic_Lung_Disease, cols.Balanced_Diet, cols.Obesity,
        cols.Smoking, cols.Passive_Smoker, cols.Chest_Pain, cols.Coughing_of_Blood,
        cols.Fatigue, cols.Weight_Loss, cols.Shortness_of_Breath, cols.Wheezing,
        cols.Swallowing_Difficulty, cols.Frequent_Cold, cols.Dry_Cough
    ]
    data_numericas = data[variables_numericas]
    
    # Resumen estadístico
    summary = data_numericas.describe().drop(['count', 'min', 'max'])
    mode = data_numericas.mode().iloc[0]
    summary.loc['mode'] = mode
    
    # Convertir el resumen a una tabla de Dash
    tabla = html.Table(
        # Encabezado de la tabla
        [html.Tr([html.Th("Estadística")] + [html.Th(col) for col in summary.columns])] +
        # Filas de la tabla
        [html.Tr([html.Th(index)] + [html.Td(f"{value:.2f}") for value in row]) for index, row in summary.iterrows()],
        style={'border': '1px solid black', 'border-collapse': 'collapse', 'width': '100%'}
    )
    return tabla

tabla_resumen = generar_tabla_resumen()

def generar_histograma_age():
    fig = px.histogram(data, x=cols.Age, nbins=20, title='Distribución de Edades')
    fig.update_layout(xaxis_title='Edad', yaxis_title='Frecuencia')
    return fig

histograma_age = dcc.Graph(figure=generar_histograma_age())

nombres_legibles = {
    cols.Age: "Edad",
    cols.Air_Pollution: "Contaminación del Aire",
    cols.Alcohol_Use: "Consumo de Alcohol",
    cols.Occupational_Hazards: "Riesgos Laborales",
    cols.Genetic_Risk: "Riesgo Genético",
    cols.Chronic_Lung_Disease: "Enfermedad Pulmonar Crónica",
    cols.Balanced_Diet: "Dieta Equilibrada",
    cols.Obesity: "Obesidad",
    cols.Smoking: "Tabaquismo",
    cols.Passive_Smoker: "Fumador Pasivo",
    cols.Chest_Pain: "Dolor en el Pecho",
    cols.Coughing_of_Blood: "Tos con Sangre",
    cols.Fatigue: "Fatiga",
    cols.Weight_Loss: "Pérdida de Peso",
    cols.Shortness_of_Breath: "Dificultad para Respirar",
    cols.Wheezing: "Sibilancias",
    cols.Swallowing_Difficulty: "Dificultad para Tragar",
    cols.Frequent_Cold: "Resfriados Frecuentes",
    cols.Dry_Cough: "Tos Seca"
}

def generar_boxplots_factores():
    factores_riesgo = {
        "Factores Ambientales": [cols.Air_Pollution, cols.Occupational_Hazards, cols.Passive_Smoker],
        "Factores de Estilo de Vida": [cols.Alcohol_Use, cols.Smoking, cols.Balanced_Diet, cols.Obesity],
        "Factores Clínicos": [cols.Chest_Pain, cols.Coughing_of_Blood, cols.Fatigue, cols.Weight_Loss,
                              cols.Shortness_of_Breath, cols.Wheezing, cols.Swallowing_Difficulty,
                              cols.Frequent_Cold, cols.Dry_Cough],
        "Factores Genéticos": [cols.Genetic_Risk, cols.Chronic_Lung_Disease]
    }
    graphs = []
    for categoria, factores in factores_riesgo.items():
        # Renombrar columnas para el gráfico
        data_renombrada = data.rename(columns=nombres_legibles)
        factores_legibles = [nombres_legibles[factor] for factor in factores]
        fig = px.box(data_renombrada, y=factores_legibles, title=f'Distribución de {categoria}')
        graphs.append(dcc.Graph(figure=fig))
    return graphs


boxplots_factores = generar_boxplots_factores()

def generar_heatmap_correlacion():
    # Seleccionar solo las variables numéricas relevantes
    variables_numericas = [
        cols.Age, cols.Air_Pollution, cols.Alcohol_Use, cols.Occupational_Hazards,
        cols.Genetic_Risk, cols.Chronic_Lung_Disease, cols.Balanced_Diet, cols.Obesity,
        cols.Smoking, cols.Passive_Smoker, cols.Chest_Pain, cols.Coughing_of_Blood,
        cols.Fatigue, cols.Weight_Loss, cols.Shortness_of_Breath, cols.Wheezing,
        cols.Swallowing_Difficulty, cols.Frequent_Cold, cols.Dry_Cough
    ]
    data_numericas = data[variables_numericas]
    
    # Calcular la matriz de correlación
    corr_matrix = data_numericas.corr()
    
    # Crear el heatmap de correlación
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='fall',  # Usar un colorscale válido
        zmin=-1,  # Límite inferior para la correlación
        zmax=1    # Límite superior para la correlación
    ))
    fig.update_layout(
        title='Matriz de Correlación',
        xaxis_title='Variables',
        yaxis_title='Variables'
    )
    return fig

heatmap_correlacion = dcc.Graph(figure=generar_heatmap_correlacion())

frecuencias_level = html.Div([
    html.H3("Frecuencias y Proporciones de Niveles de Riesgo"),
    html.P(f"Low: {data[cols.Level].value_counts()['Low']} ({data[cols.Level].value_counts(normalize=True)['Low'] * 100:.2f}%)"),
    html.P(f"Medium: {data[cols.Level].value_counts()['Medium']} ({data[cols.Level].value_counts(normalize=True)['Medium'] * 100:.2f}%)"),
    html.P(f"High: {data[cols.Level].value_counts()['High']} ({data[cols.Level].value_counts(normalize=True)['High'] * 100:.2f}%)"),
])

# Seleccionar solo las variables numéricas relevantes
variables_numericas = [
cols.Age, cols.Air_Pollution, cols.Alcohol_Use, cols.Occupational_Hazards,
cols.Genetic_Risk, cols.Chronic_Lung_Disease, cols.Balanced_Diet, cols.Obesity,
cols.Smoking, cols.Passive_Smoker, cols.Chest_Pain, cols.Coughing_of_Blood,
cols.Fatigue, cols.Weight_Loss, cols.Shortness_of_Breath, cols.Wheezing,
cols.Swallowing_Difficulty, cols.Frequent_Cold, cols.Dry_Cough
]

# Calcular la media de cada variable por nivel de riesgo
medias_por_nivel = data.groupby(cols.Level)[variables_numericas].mean().reset_index()


def generar_barras_factores_por_nivel():
    # Seleccionar solo las variables numéricas relevantes, excluyendo la edad
    variables_numericas = [
        cols.Air_Pollution, cols.Alcohol_Use, cols.Occupational_Hazards,
        cols.Genetic_Risk, cols.Chronic_Lung_Disease, cols.Balanced_Diet, cols.Obesity,
        cols.Smoking, cols.Passive_Smoker, cols.Chest_Pain, cols.Coughing_of_Blood,
        cols.Fatigue, cols.Weight_Loss, cols.Shortness_of_Breath, cols.Wheezing,
        cols.Swallowing_Difficulty, cols.Frequent_Cold, cols.Dry_Cough
    ]
    
    # Calcular la media de cada variable por nivel de riesgo
    medias_por_nivel = data.groupby(cols.Level)[variables_numericas].mean().reset_index()
    
    # Renombrar columnas para el gráfico
    medias_por_nivel_renombrada = medias_por_nivel.rename(columns=nombres_legibles)
    
    # Verificar que el diccionario nombres_legibles tenga la clave para cols.Level
    if cols.Level in nombres_legibles:
        nivel_riesgo_col = nombres_legibles[cols.Level]
    else:
        nivel_riesgo_col = cols.Level  # Usa el nombre original si no está en el diccionario

    # Crear el gráfico de barras
    fig = px.bar(medias_por_nivel_renombrada, x=nivel_riesgo_col, y=medias_por_nivel_renombrada.columns[1:], barmode='group',
                 title='Comparación de Factores por Nivel de Riesgo')
    fig.update_layout(xaxis_title='Nivel de Riesgo', yaxis_title='Media de Factores')
    return fig

barras_factores_por_nivel = dcc.Graph(figure=generar_barras_factores_por_nivel())


data['Smoking_Cat'] = pd.cut(data[ColumnNames.Smoking], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto'])
data['Alcohol_Use_Cat'] = pd.cut(data[ColumnNames.Alcohol_Use], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto'])
data['Obesity_Cat'] = pd.cut(data[ColumnNames.Obesity], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto'])
data['Chest_Pain_Bin'] = data[ColumnNames.Chest_Pain] > 5
data['Shortness_Breath_Bin'] = data[ColumnNames.Shortness_of_Breath] > 5
data['Genetic_Risk_Cat'] = pd.cut(data[ColumnNames.Genetic_Risk], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto'])

# Pruebas de Chi-Cuadrado
def chi_square_test(var1, var2):
    contingency_table = pd.crosstab(var1, var2)
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return chi2, p, contingency_table

# Resultados de las pruebas
chi2_genetic, p_genetic, table_genetic = chi_square_test(data['Genetic_Risk_Cat'], data[ColumnNames.Level])
chi2_smoking, p_smoking, table_smoking = chi_square_test(data['Smoking_Cat'], data['Chest_Pain_Bin'])
chi2_alcohol, p_alcohol, table_alcohol = chi_square_test(data['Alcohol_Use_Cat'], data[ColumnNames.Level])
chi2_obesity, p_obesity, table_obesity = chi_square_test(data['Obesity_Cat'], data['Shortness_Breath_Bin'])

# Función para crear tablas HTML
def create_html_table(contingency_table, row_labels, col_labels):
    return html.Table([
        html.Thead(html.Tr([html.Th('')] + [html.Th(col, style={'text-align': 'left'}) for col in col_labels])),
        html.Tbody([
            html.Tr([html.Td(row_labels[i])] + [html.Td(contingency_table.iloc[i, j]) for j in range(len(contingency_table.columns))])
            for i in range(len(contingency_table))
        ])
    ], style={'border': '1px solid black', 'border-collapse': 'collapse', 'width': '50%', 'margin': '10px 0'},
       className='contingency-table')

