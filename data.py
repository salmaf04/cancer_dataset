from dash import dcc, html
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from columns import ColumnNames as cols 
from main import data
import pandas as pd
from scipy.stats import chi2_contingency, f_oneway, shapiro, levene, ttest_ind
from columns import ColumnNames
import io
import statsmodels.api as sm
import scipy.stats as stats
import base64
import numpy as np

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

genre = data.groupby('Gender')['Gender'].value_counts().reset_index()


fig_gender_count = px.bar(genre, 
             x='Gender',
             y='count',
             color='Gender',
             labels={'Gender': 'Genero', 'count': 'Cantidad'},
             title='Cantidad de Pacientes por Genero')

"""
Intervalo de confianza para la proporción de hombres y mujeres
"""

# Obtener el número de hombres y mujeres en los datos
total_hombres = genre[genre['Gender'] == 1]['count'].values[0]
total_mujeres = genre[genre['Gender'] == 2]['count'].values[0]

# Obtener el total de pacientes
total_pacientes = total_hombres + total_mujeres

# Asignar las proporciones observadas en tu dataset
p_hombres_data = total_hombres / total_pacientes  # Proporción observada de hombres en el dataset
p_mujeres_data = total_mujeres / total_pacientes  # Proporción observada de mujeres en el dataset

# Proporciones esperadas para el intervalo de confianza
p_hombres_esperado = 0.6  # Proporción esperada de hombres
p_mujeres_esperado = 0.4  # Proporción esperada de mujeres

# Tamaños de las muestras (hombres y mujeres)
n_hombres = total_hombres
n_mujeres = total_mujeres

# Nivel de confianza
confianza = 0.90

# Z-score para un intervalo de confianza del 90%
z_score = stats.norm.ppf(1 - (1 - confianza) / 2)

# Calcular el error estándar para la diferencia de proporciones usando las proporciones esperadas
se = np.sqrt(p_hombres_esperado * (1 - p_hombres_esperado) / n_hombres + p_mujeres_esperado * (1 - p_mujeres_esperado) / n_mujeres)

# Calcular la diferencia de proporciones
diferencia_esperada = p_hombres_esperado - p_mujeres_esperado

# Calcular el intervalo de confianza
margen_error = z_score * se
ic_inferior = diferencia_esperada - margen_error
ic_superior = diferencia_esperada + margen_error

# Verificar si la diferencia de proporciones del dataset cae dentro del intervalo de confianza
diferencia_data = p_hombres_data - p_mujeres_data

# Resultado
intervalo_confianza = f"""
    Interpretación del Intervalo de Confianza para la Diferencia de Proporciones entre Hombres y Mujeres que son Pacientes de Cáncer:

    - **Proporción observada de hombres**: {p_hombres_data:.4f}
    - **Proporción observada de mujeres**: {p_mujeres_data:.4f}
    - **Diferencia de proporciones observada**: {diferencia_data:.4f}
    
    - **Proporción esperada de hombres**: {p_hombres_esperado:.4f}
    - **Proporción esperada de mujeres**: {p_mujeres_esperado:.4f}
    - **Diferencia de proporciones esperada**: {diferencia_esperada:.4f}
    - **Intervalo de Confianza para la Diferencia de Proporciones (90%)**: ({ic_inferior:.4f}, {ic_superior:.4f})
    
    - **Conclusión**:
      {"La diferencia observada en las proporciones entre hombres y mujeres está dentro del intervalo de confianza, lo cual significa que las proporciones observadas en la muestra son proporcionales a la población. "
       if ic_inferior <= diferencia_data <= ic_superior
       else
       "Se rechaza la hipótesis nula. La diferencia de proporciones observada es estadísticamente significativa."}
    """
    
# Calcular la proporción de pacientes masculinos y femeninos
total_patients = len(data)
male_count = data[data['Gender'] == 1].shape[0]
female_count = total_patients - male_count

# Crear un DataFrame con las proporciones
gender_proportions = pd.DataFrame({
    'Gender': ['Hombres', 'Mujeres'],
    'Count': [male_count, female_count]
})

# Crear el gráfico de pastel
fig_gender_proportion = px.pie(gender_proportions, 
                               names='Gender', 
                               values='Count', 
                               title='Proporción de Pacientes por Género',
                               color_discrete_sequence=['lightblue', 'pink'])

# Seleccionar solo las variables numéricas relevantes
variables_numericas = [
    cols.Air_Pollution, cols.Alcohol_Use, cols.Occupational_Hazards,
    cols.Genetic_Risk, cols.Chronic_Lung_Disease, cols.Balanced_Diet, cols.Obesity,
    cols.Smoking, cols.Passive_Smoker, cols.Chest_Pain, cols.Coughing_of_Blood,
    cols.Fatigue, cols.Weight_Loss, cols.Shortness_of_Breath, cols.Wheezing,
    cols.Swallowing_Difficulty, cols.Frequent_Cold, cols.Dry_Cough
]

# Calcular la media de cada variable por género
medias_por_genero = data.groupby('Gender')[variables_numericas].mean().reset_index()

# Renombrar columnas para el gráfico
nombres_legibles_genero = {
    cols.Gender : 'Género',
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
medias_por_genero_renombrada = medias_por_genero.rename(columns=nombres_legibles_genero)

# Crear el gráfico de barras
def generar_barras_factores_por_genero():
    fig = px.bar(medias_por_genero_renombrada, x='Género', y=medias_por_genero_renombrada.columns[1:], barmode='group',
                 title='Comparación de Factores por Género')
    fig.update_layout(xaxis_title='Género', yaxis_title='Media de Factores')
    return fig

barras_factores_por_genero = dcc.Graph(figure=generar_barras_factores_por_genero())

data_clean = data.dropna(subset=[cols.Alcohol_Use, cols.Smoking, cols.Chest_Pain])
# Prueba T-Student para el Consumo de Alcohol
alcohol_masculino = data_clean[data_clean['Gender'] == 1][cols.Alcohol_Use]
alcohol_femenino = data_clean[data_clean['Gender'] == 2][cols.Alcohol_Use]
t_stat_alcohol, p_valor_alcohol = ttest_ind(alcohol_masculino, alcohol_femenino, equal_var=False)

# Prueba T-Student para Tabaquismo
tabaquismo_masculino = data_clean[data_clean['Gender'] == 1][cols.Smoking]
tabaquismo_femenino = data_clean[data_clean['Gender'] == 2][cols.Smoking]
t_stat_tabaquismo, p_valor_tabaquismo = ttest_ind(tabaquismo_masculino, tabaquismo_femenino, equal_var=False)

# Prueba T-Student para Dolor en el Pecho
dolor_pecho_masculino = data_clean[data_clean['Gender'] == 1][cols.Chest_Pain]
dolor_pecho_femenino = data_clean[data_clean['Gender'] == 2][cols.Chest_Pain]
t_stat_dolor_pecho, p_valor_dolor_pecho = ttest_ind(dolor_pecho_masculino, dolor_pecho_femenino, equal_var=False)

# Calcular proporciones para cada variable
def calcular_proporciones(variable):
    return data.groupby('Gender')[variable].mean().reset_index()

## Crear gráficos de pastel con colores personalizados
colors = ['#a6cee3', '#fbb4ae']  # Colores personalizados

fig_alcohol_gender = px.pie(calcular_proporciones(cols.Alcohol_Use), names='Gender', values=cols.Alcohol_Use,
                     title='Consumo de Alcohol por Género', labels={'Gender': 'Género'},
                     color_discrete_sequence=colors)

fig_tabaquismo_gender = px.pie(calcular_proporciones(cols.Smoking), names='Gender', values=cols.Smoking,
                        title='Tabaquismo por Género', labels={'Gender': 'Género'},
                        color_discrete_sequence=colors)

fig_dolor_pecho_gender = px.pie(calcular_proporciones(cols.Chest_Pain), names='Gender', values=cols.Chest_Pain,
                         title='Dolor en el Pecho por Género', labels={'Gender': 'Género'},
                         color_discrete_sequence=colors)