from dash import dcc, html
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from columns import ColumnNames as cols 
from main import data
import pandas as pd
from scipy.stats import chi2_contingency, f_oneway, shapiro, levene
from columns import ColumnNames
import io
import statsmodels.api as sm
import scipy.stats as stats
import base64

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

# Obesidad vs. Tos con Sangre
chi2_obesity_cough, p_obesity_cough, table_obesity_cough = chi_square_test(
    pd.cut(data[ColumnNames.Obesity], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto']),
    data[ColumnNames.Coughing_of_Blood] > 5
)

# Riesgo Genético vs. Consumo de Alcohol
chi2_genetic_alcohol, p_genetic_alcohol, table_genetic_alcohol = chi_square_test(
    pd.cut(data[ColumnNames.Genetic_Risk], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto']),
    pd.cut(data[ColumnNames.Alcohol_Use], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto'])
)

# Riesgos Laborales vs. Enfermedad Pulmonar Crónica
chi2_occupational_lung, p_occupational_lung, table_occupational_lung = chi_square_test(
    pd.cut(data[ColumnNames.Occupational_Hazards], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto']),
    data[ColumnNames.Chronic_Lung_Disease] > 5
)

# Tabaquismo vs. Dolor en el Pecho
chi2_smoking, p_smoking, table_smoking = chi_square_test(data['Smoking_Cat'], data['Chest_Pain_Bin'])

# Tos Seca vs. Frío Constante
chi2_dry_cough_cold, p_dry_cough_cold, table_dry_cough_cold = chi_square_test(
    data[ColumnNames.Dry_Cough] > 5,
    data[ColumnNames.Frequent_Cold] > 5
)

# Dificultad para Respirar vs. Pérdida de Peso
chi2_breath_weight, p_breath_weight, table_breath_weight = chi_square_test(
    data[ColumnNames.Shortness_of_Breath] > 5,
    data[ColumnNames.Weight_Loss] > 5
)

# Contaminación del Aire vs. Enfermedad Pulmonar Crónica
chi2_air_lung, p_air_lung, table_air_lung = chi_square_test(
    pd.cut(data[ColumnNames.Air_Pollution], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto']),
    data[ColumnNames.Chronic_Lung_Disease] > 5
)

# Fumador Pasivo vs. Fumador Activo
chi2_passive_active, p_passive_active, table_passive_active = chi_square_test(
    pd.cut(data[ColumnNames.Passive_Smoker], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto']),
    pd.cut(data[ColumnNames.Smoking], bins=[0, 3, 6, 10], labels=['Bajo', 'Medio', 'Alto'])
)

# Dolor en el Pecho vs. Enfermedad Pulmonar Crónica
chi2_chest_lung, p_chest_lung, table_chest_lung = chi_square_test(
    data[ColumnNames.Chest_Pain] > 5,
    data[ColumnNames.Chronic_Lung_Disease] > 5
)

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

# ANOVA para Consumo de Alcohol
alcohol_low = data[data[ColumnNames.Level] == 'Low'][ColumnNames.Alcohol_Use]
alcohol_medium = data[data[ColumnNames.Level] == 'Medium'][ColumnNames.Alcohol_Use]
alcohol_high = data[data[ColumnNames.Level] == 'High'][ColumnNames.Alcohol_Use]
anova_alcohol = f_oneway(alcohol_low, alcohol_medium, alcohol_high)

# Verificar normalidad para Consumo de Alcohol
shapiro_alcohol_low = shapiro(alcohol_low)
shapiro_alcohol_medium = shapiro(alcohol_medium)
shapiro_alcohol_high = shapiro(alcohol_high)

# Verificar homogeneidad de varianzas para Consumo de Alcohol
levene_alcohol = levene(alcohol_low, alcohol_medium, alcohol_high)

# ANOVA para Riesgo Genético
genetic_low = data[data[ColumnNames.Level] == 'Low'][ColumnNames.Genetic_Risk]
genetic_medium = data[data[ColumnNames.Level] == 'Medium'][ColumnNames.Genetic_Risk]
genetic_high = data[data[ColumnNames.Level] == 'High'][ColumnNames.Genetic_Risk]
anova_genetic = f_oneway(genetic_low, genetic_medium, genetic_high)

# Verificar normalidad para Riesgo Genético
shapiro_genetic_low = shapiro(genetic_low)
shapiro_genetic_medium = shapiro(genetic_medium)
shapiro_genetic_high = shapiro(genetic_high)

# Verificar homogeneidad de varianzas para Riesgo Genético
levene_genetic = levene(genetic_low, genetic_medium, genetic_high)

# ANOVA para Obesidad
obesity_low = data[data[ColumnNames.Level] == 'Low'][ColumnNames.Obesity]
obesity_medium = data[data[ColumnNames.Level] == 'Medium'][ColumnNames.Obesity]
obesity_high = data[data[ColumnNames.Level] == 'High'][ColumnNames.Obesity]
anova_obesity = f_oneway(obesity_low, obesity_medium, obesity_high)

# Verificar normalidad para Obesidad
shapiro_obesity_low = shapiro(obesity_low)
shapiro_obesity_medium = shapiro(obesity_medium)
shapiro_obesity_high = shapiro(obesity_high)

# Verificar homogeneidad de varianzas para Obesidad
levene_obesity = levene(obesity_low, obesity_medium, obesity_high)

# Gráficos de pastel
# Paletas de colores personalizadas para cada gráfico
colors_alcohol = [ "#ccebc5",  "#fed9a6", "#fff2ae" ]  # Azul, naranja, verde
colors_genetic = ["#ccebc5",  "#fed9a6", "#fff2ae"]  # Rojo, morado, marrón
colors_obesity = ["#ccebc5",  "#fed9a6", "#fff2ae"]  # Rosa, gris, oliva

# Gráfico de Consumo de Alcohol
fig_alcohol = px.pie(
    data,
    names=ColumnNames.Level,
    values=ColumnNames.Alcohol_Use,
    title="Consumo de Alcohol por Nivel de Riesgo",
    color_discrete_sequence=colors_alcohol,  # Colores específicos para Alcohol
)

# Gráfico de Riesgo Genético
fig_genetic = px.pie(
    data,
    names=ColumnNames.Level,
    values=ColumnNames.Genetic_Risk,
    title="Riesgo Genético por Nivel de Riesgo",
    color_discrete_sequence=colors_genetic,  # Colores específicos para Riesgo Genético
)

# Gráfico de Obesidad
fig_obesity = px.pie(
    data,
    names=ColumnNames.Level,
    values=ColumnNames.Obesity,
    title="Obesidad por Nivel de Riesgo",
    color_discrete_sequence=colors_obesity,  # Colores específicos para Obesidad
)

#Regresión lineal 

# Codificar el nivel de riesgo
risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
data['Risk_Level_Encoded'] = data[ColumnNames.Level].map(risk_mapping)

# Variable independiente y dependiente
X = data[[ColumnNames.Age]]
y = data['Risk_Level_Encoded']

# Agregar constante para el modelo
X = sm.add_constant(X)

# Ajustar el modelo de regresión lineal
model = sm.OLS(y, X).fit()

# Resultados del modelo
summary = model.summary()

# Crear gráfico de dispersión con línea de regresión
fig_regression = px.scatter(data, x=ColumnNames.Age, y='Risk_Level_Encoded', trendline="ols",
                            labels={'Risk_Level_Encoded': 'Nivel de Riesgo Codificado', ColumnNames.Age: 'Edad'},
                            title="Regresión Lineal: Edad vs. Nivel de Riesgo")

# Gráfico de residuos vs. valores ajustados
residuals = model.resid

fig, ax = plt.subplots()
ax.scatter(model.fittedvalues, residuals)
ax.axhline(0, color='red', linestyle='--')
ax.set_xlabel('Valores Ajustados')
ax.set_ylabel('Residuos')
ax.set_title('Residuos vs. Valores Ajustados')
buf = io.BytesIO()
plt.savefig(buf, format='png')
plt.close(fig)
data_residuals_vs_fitted = base64.b64encode(buf.getbuffer()).decode("utf8")

# Gráfico Q-Q para normalidad de residuos
fig, ax = plt.subplots()
stats.probplot(residuals, dist="norm", plot=ax)
ax.set_title('Gráfico Q-Q de Residuos')
buf = io.BytesIO()
plt.savefig(buf, format='png')
plt.close(fig)
data_qq_plot = base64.b64encode(buf.getbuffer()).decode("utf8")

# Prueba de normalidad de Shapiro-Wilk
shapiro_test = stats.shapiro(residuals)