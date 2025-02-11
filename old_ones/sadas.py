import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import dash
from dash import dcc, html
from scipy.stats import norm
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from old_ones.hypothesisasdad import fig4, fig5, fig6, fig7, fig8, fig9, fig10 , chi2_interpretation, chi2_interpretation2, chi2_interpretation3, chi2_interpretation4, fig11, chi2_interpretation5, fig12
from data import data

# Filtrar los datos para excluir el valor 'Both'
filtered_data = data[data['Gender'] != 'Both']

# Contar la frecuencia de cada género
gender_counts = filtered_data['Gender'].value_counts()

# Calcular las proporciones ajustadas
total_count = gender_counts.sum()
proportion_female = gender_counts['Female'] / total_count
proportion_male = gender_counts['Male'] / total_count

# Ajustar las proporciones al 66% restante
adjusted_proportion_female = proportion_female * (total_count / (total_count + data['Gender'].value_counts()['Both']))
adjusted_proportion_male = proportion_male * (total_count / (total_count + data['Gender'].value_counts()['Both']))

# Calcular los intervalos de confianza del 90%
confidence_level = 0.90
z_score = norm.ppf((1 + confidence_level) / 2)

# Tamaño de la muestra ajustada
sample_size = total_count

# Error estándar
se_female = np.sqrt(adjusted_proportion_female * (1 - adjusted_proportion_female) / sample_size)
se_male = np.sqrt(adjusted_proportion_male * (1 - adjusted_proportion_male) / sample_size)

# Intervalos de confianza
ci_female = (adjusted_proportion_female - z_score * se_female, adjusted_proportion_female + z_score * se_female)
ci_male = (adjusted_proportion_male - z_score * se_male, adjusted_proportion_male + z_score * se_male)

# Crear un DataFrame para las proporciones y los intervalos de confianza
proportions = pd.DataFrame({
    'Gender': ['Female', 'Male'],
    'Proportion': [adjusted_proportion_female, adjusted_proportion_male],
    'Lower CI': [ci_female[0], ci_male[0]],
    'Upper CI': [ci_female[1], ci_male[1]]
})

# Crear el gráfico de barras para las proporciones
fig1 = px.bar(proportions, x='Gender', y='Proportion', color='Gender', title='Estimación Puntual de la Proporción de Género')

# Añadir los valores en las barras
for index, row in proportions.iterrows():
    fig1.add_annotation(
        x=row['Gender'],
        y=row['Proportion'],
        text=f"{row['Proportion']:.2f}",
        showarrow=False,
        font=dict(size=14),
        yshift=10
    )

# Crear el gráfico de puntos con barras de error para los intervalos de confianza
fig2 = go.Figure()

# Añadir los puntos
fig2.add_trace(go.Scatter(
    x=proportions['Gender'],
    y=proportions['Proportion'],
    mode='markers',
    marker=dict(color=['blue', 'red'], size=10),
    name='Estimación Puntual'
))

# Añadir las barras de error
fig2.add_trace(go.Scatter(
    x=proportions['Gender'],
    y=proportions['Proportion'],
    error_y=dict(
        type='data',
        symmetric=False,
        array=proportions['Upper CI'] - proportions['Proportion'],
        arrayminus=proportions['Proportion'] - proportions['Lower CI']
    ),
    mode='markers',
    marker=dict(color='black', size=10),
    name='Intervalo de Confianza'
))

# Añadir títulos y etiquetas al gráfico de intervalos de confianza
fig2.update_layout(
    title='Intervalo de Confianza del 90% para la Proporción de Género',
    xaxis_title='Género',
    yaxis_title='Proporción',
    showlegend=True
)

# Interpretación de los intervalos de confianza
interpretation = f"""
Interpretación de los Intervalos de Confianza del 90%:

- **Mujeres**:
  - Estimación Puntual: {adjusted_proportion_female:.2f}
  - Intervalo de Confianza: [{ci_female[0]:.2f}, {ci_female[1]:.2f}]
  - Interpretación: La proporción estimada de mujeres en el conjunto de datos es {adjusted_proportion_female:.2f} con un intervalo de confianza del 90% de [{ci_female[0]:.2f}, {ci_female[1]:.2f}].

- **Hombres**:
  - Estimación Puntual: {adjusted_proportion_male:.2f}
  - Intervalo de Confianza: [{ci_male[0]:.2f}, {ci_male[1]:.2f}]
  - Interpretación: La proporción estimada de hombres en el conjunto de datos es {adjusted_proportion_male:.2f} con un intervalo de confianza del 90% de [{ci_male[0]:.2f}, {ci_male[1]:.2f}].
"""

# Crear el histograma para la prevalencia de fumar
fig3 = px.histogram(data, x='Smoking_Prevalence', nbins=20, title='Histograma de Prevalencia de Fumar')
fig3.update_layout(bargap=0.1)

# Study about age in smoking
promedio_experimentacion_por_edad = data.groupby('Age_Group')['Drug_Experimentation'].mean().reset_index()
print(promedio_experimentacion_por_edad)

data_15_19 = data[data["Age_Group"] == '15-19']


print(data_15_19["Drug_Experimentation"].value_counts())

fig13 = px.bar(promedio_experimentacion_por_edad, 
             x='Age_Group',
             y='Drug_Experimentation',
             color='Age_Group',
             labels={'Age_Group': 'Edad', 'Drug_Experimentation': 'Experimentación con Drogas'},
             title='Promedio de Experimentación con Drogas por Rango de Edad')

# Rotar las etiquetas del eje x
fig13.update_layout(xaxis_tickangle=-45)





# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Diseño de la aplicación
app.layout = html.Div([
    html.H1("Análisis de Datos de Fumar y Drogas en Jóvenes"),
    
    html.H3("Estimación Puntual de la Proporción de Género"),
    dcc.Graph(figure=fig1),

    html.H3("Promedio de Experimentación con Drogas por Rango de Edad"),
    dcc.Graph(figure=fig13),
    
    html.H3("Intervalo de Confianza del 90% para la Proporción de Género"),
    dcc.Graph(figure=fig2),
    
    html.H3("Interpretación de los Intervalos de Confianza del 90%"),
    html.Pre(interpretation, style={'whiteSpace': 'pre-wrap', 'wordBreak': 'break-all', 'fontSize': '14px', 'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '5px', 'margin': '20px 0'}),
    
    html.H3("Histograma y Distribución de Prevalencia de Fumar"),
    dcc.Graph(figure=fig3),
    
    html.H3("Hipótesis de Dependencia entre Prevalencia de Fumar y Estado Socioeconómico"),
    dcc.Graph(figure=fig5),
    html.Pre(chi2_interpretation, style={'whiteSpace': 'pre-wrap', 'wordBreak': 'break-all', 'fontSize': '14px', 'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '5px', 'margin': '20px 0'}),
    dcc.Graph(figure=fig6),
    
    html.H3("Histograma y Distribución de Exploración en Drogas"),
    dcc.Graph(figure=fig4),

    html.H3("Hipótesis entre Experimentación en Drogas y Educación de Sustancia"),
    dcc.Graph(figure=fig7),
    html.Pre(chi2_interpretation2, style={'whiteSpace': 'pre-wrap', 'wordBreak': 'break-all', 'fontSize': '14px', 'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '5px', 'margin': '20px 0'}),
    dcc.Graph(figure=fig8),
    
    html.H3("Hipótesis de Dependencia entre Salud Mental y Experimentación en Drogas"),
    dcc.Graph(figure=fig9),
    html.Pre(chi2_interpretation3,
    style={'whiteSpace': 'pre-wrap', 'wordBreak': 'break-all', 'fontSize': '14px', 'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '5px', 'margin': '20px 0'}),
    dcc.Graph(figure=fig10),

    html.H3("Hipotesis de Dependencia entre Prevalencia de Fumar e Influencia de Medios"),
    dcc.Graph(figure=fig11),
    html.Pre(chi2_interpretation4,
    style={'whiteSpace': 'pre-wrap', 'wordBreak': 'break-all', 'fontSize': '14px', 'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '5px', 'margin': '20px 0'}),

    html.H3("Hipotesis de Dependencia entre Experimentacion con Drogas e Influencia de Medios"),
    dcc.Graph(figure=fig12),
    html.Pre(chi2_interpretation5,
    style={'whiteSpace': 'pre-wrap', 'wordBreak': 'break-all', 'fontSize': '14px', 'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '5px', 'margin': '20px 0'}),

])

# Ejecutar la aplicación
if __name__ == '__main__':
   app.run_server(debug=True)