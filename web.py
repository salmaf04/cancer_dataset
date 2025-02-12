import dash
from data_layout import data_layout, describe_layout
from dash import html
from result_layout import chi_layout, anova_layout, regression_layout


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
])

if __name__ == '__main__':
   app.run_server(debug=True)