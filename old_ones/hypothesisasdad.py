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
from data import data


"""
Pruebas de Hipotesis !!!
1-Socioeconomic Status and Smoking Prevalence
2-Substance Education and Drug Experimentation
3-Mental Health and  Drug Experimentation
4-Smoking Prevalence and Media Influence
5-Drug Experimentation and Media Influence
"""

#Pruebas de Independencia

#Hipotesis de dependencia entre estado socioeconómico y la prevalencia de fumar
smoke_by_socioeconomic_status = data.groupby('Socioeconomic_Status')['Smoking_Prevalence'].mean()

# Generar un gráfico de barras para la proporción de experimentación de drogas
fig5 = px.bar(smoke_by_socioeconomic_status, x=smoke_by_socioeconomic_status.index, y=smoke_by_socioeconomic_status.values,
              labels={'x': 'Estado Socioeconómico', 'y': 'Prevalencia de Fumar'},
              title='Prevalencia de Fumar por Estado Socio')

contingency_table = pd.crosstab(index=data['Socioeconomic_Status'], columns=data['Smoking_Prevalence'])
# Realizar el test de chi-cuadrado
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Interpretación del test de chi-cuadrado
chi2_interpretation = f"""
Interpretación del Test de Chi-Cuadrado:

- **Chi-cuadrado**: {chi2:.2f}
- **P-valor**: {p:.4f}
- **Grados de libertad**: {dof}
- **Valores esperados**:
{expected}

- **Conclusión**:
  - El p-valor es {p:.4f}, lo que es mayor que el umbral de significancia de 0.05.
  - No hay suficiente evidencia para rechazar la hipótesis nula.
  - **Interpretación**: No hay evidencia estadística suficiente para concluir que existe una relación significativa entre el `Socioeconomic_Status` y la `Smoking_Prevalence`.
"""

# Crear un gráfico de cajas y bigotes 
fig6 = px.box(data, x = 'Socioeconomic_Status', y='Smoking_Prevalence',
              labels={'x': 'Estado Socioeconómico', 'y': 'Prevalencia a Fumar'},
              title='Distribución de Experimentación de Drogas por Estado Socioeconómico')

# Crear el histograma para la exploración en drogas
fig4 = px.histogram(data, x='Drug_Experimentation', nbins=20, title='Histograma de Exploración en Drogas')
fig4.update_layout(bargap=0.1)


#Hipotesis de dependencia entre la experimentación con drogas y la educación de la sustancia
drugs_by_substance_education = data.groupby('Substance_Education')['Drug_Experimentation'].mean()

# Generar un gráfico de barras para la proporción de experimentación de drogas
fig7 = px.bar(drugs_by_substance_education, x=drugs_by_substance_education.index, y=drugs_by_substance_education.values,
              labels={'x': 'Educación en Sustancia', 'y': 'Proporción de Experimentación de Drogas (%)'},
              title='Proporción de Experimentación de Drogas por Educación en Sustancia')


contingency_table = pd.crosstab(index=data['Drug_Experimentation'], columns=data['Substance_Education'])
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Interpretación del test de chi-cuadrado
chi2_interpretation2 = f"""
Interpretación del Test de Chi-Cuadrado:

- **Chi-cuadrado**: {chi2:.2f}
- **P-valor**: {p:.4f}
- **Grados de libertad**: {dof}
- **Valores esperados**:
{expected}

- **Conclusión**:
  - El p-valor es {p:.4f}, lo que es mayor que el umbral de significancia de 0.05.
  - No hay suficiente evidencia para rechazar la hipótesis nula.
  - **Interpretación**: No hay evidencia estadística suficiente para concluir que existe una relación significativa entre el `Socioeconomic_Status` y la `Smoking_Prevalence`.
"""
# Crear un gráfico de cajas y bigotes para la distribución de experimentación de drogas
fig8 = px.box(data, x = 'Substance_Education', y='Drug_Experimentation',
              labels={'x': 'Educación en Sustancia', 'y': 'Experimentación de Drogas'},
              title='Distribución de Experimentación de Drogas por Educación en Sustancia')

drugs_by_mental_health = data.groupby('Mental_Health')['Drug_Experimentation'].mean() 

# Generar un gráfico de barras para la proporción de experimentación de drogas
fig9 = px.bar(drugs_by_mental_health, x=drugs_by_mental_health.index, y=drugs_by_mental_health.values,
              labels={'x': 'Salud Mental', 'y': 'Proporción de Experimentación de Drogas (%)'},
              title='Proporción de Experimentación de Drogas por Salud Mental')

# Crear un gráfico de cajas y bigotes para la distribución de experimentación de drogas
fig10 = px.box(data, x = 'Mental_Health', y='Drug_Experimentation',
              labels={'x': 'Salud Mental', 'y': 'Experimentación de Drogas'},
              title='Distribución de Experimentación de Drogas por Salud Mental')


#Independency test between mental_health and drug_experimentation
contingency_table = pd.crosstab(data['Mental_Health'], data['Drug_Experimentation'])

chi2_interpretation3 = f"""
Interpretación del Test de Chi-Cuadrado:

- **Chi-cuadrado**: {chi2:.2f}
- **P-valor**: {p:.4f}
- **Grados de libertad**: {dof}
- **Valores esperados**:
{expected}

- **Conclusión**:
  - El p-valor es {p:.4f}, lo que es mayor que el umbral de significancia de 0.05.
  - No hay suficiente evidencia para rechazar la hipótesis nula.
  - **Interpretación**: No hay evidencia estadística suficiente para concluir que existe una relación significativa entre el `Socioeconomic_Status` y la `Smoking_Prevalence`.
"""

# Realizar la Prueba de Chi-Cuadrado
chi2, p, dof, expected = chi2_contingency(contingency_table)


#Independency test between smoking_prevalence and media_influence
contingency_table = pd.crosstab(data["Smoking_Prevalence"], data["Media_Influence"])

chi2, p, dof, expected = chi2_contingency(contingency_table)

chi2_interpretation4 = f"""
Interpretación del Test de Chi-Cuadrado:

- **Chi-cuadrado**: {chi2:.2f}
- **P-valor**: {p:.4f}
- **Grados de libertad**: {dof}
- **Valores esperados**:
{expected}

- **Conclusión**:
  - El p-valor es {p:.4f}, lo que es mayor que el umbral de significancia de 0.05.
  - No hay suficiente evidencia para rechazar la hipótesis nula.
  - **Interpretación**: No hay evidencia estadística suficiente para concluir que existe una relación significativa entre la `Media_Influence` y la `Smoking_Prevalence`.
"""

smoking_prevalence_media_influence = data.groupby('Media_Influence')['Smoking_Prevalence'].mean()

fig11 = px.bar(smoking_prevalence_media_influence, x=smoking_prevalence_media_influence.index, y=smoking_prevalence_media_influence.values,
              labels={'x': 'Prevalencia de Fumar', 'y': 'Influencia de la Medios'},
              title='Influencia de los Medios sobre la Prevalencia de Fumar')


#Independency test between drug_experimentation and media_influence
contingency_table = pd.crosstab(data["Drug_Experimentation"], data["Media_Influence"])

chi2, p, dof, expected = chi2_contingency(contingency_table)

chi2_interpretation5 = f"""
Interpretación del Test de Chi-Cuadrado:

- **Chi-cuadrado**: {chi2:.2f}
- **P-valor**: {p:.4f}
- **Grados de libertad**: {dof}
- **Valores esperados**:
{expected}

- **Conclusión**:
  - El p-valor es {p:.4f}, lo que es mayor que el umbral de significancia de 0.05.
  - No hay suficiente evidencia para rechazar la hipótesis nula.
  - **Interpretación**: No hay evidencia estadística suficiente para concluir que existe una relación significativa entre el `Media Influence` y la `Drug_Experimentation`.
"""

drug_experimentation_media_influence = data.groupby('Drug_Experimentation')['Media_Influence'].mean()

fig12 = px.bar(smoking_prevalence_media_influence, x=smoking_prevalence_media_influence.index, y=smoking_prevalence_media_influence.values,
              labels={'x': 'Experimentacion con Drogas', 'y': 'Influencia de la Media'},
              title='Influencia de los en la Experimentacion con Drogas')


"""
# Interpretación de los resultados
alpha = 0.05
if p < alpha:
    chi_square_result = 'Rechazamos la hipótesis nula. La experimentación de drogas está relacionada con la salud mental.'
else:
    chi_square_result = 'No rechazamos la hipótesis nula. No hay suficiente evidencia para afirmar que la experimentación de drogas está relacionada con la salud mental.'

"""
