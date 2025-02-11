import dash
from data_layout import data_layout, describe_layout
from dash import html
from result_layout import chi_layout, anova_layout


# Nueva función para generar el gráfico de barras


app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    data_layout,
    describe_layout,
    chi_layout,
    anova_layout,
])

if __name__ == '__main__':
   app.run_server(debug=True)