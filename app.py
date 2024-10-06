import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np

# Inicializa o aplicativo Dash
app = dash.Dash(__name__)

# Função para gerar novos dados
def generate_data():
    frutas = ["Maçã", "Banana", "Laranja", "Uva"]
    quantidade = np.random.randint(1, 10, size=4)
    return frutas, quantidade

# Layout do aplicativo
app.layout = html.Div(children=[
    html.H1(children='Dash '),
    html.Div(children='Clique no botão para gerar novos dados para o gráfico.'),

    dcc.Graph(id='exemplo-grafico'),

    html.Button('Atualizar Gráfico', id='atualizar-botao', n_clicks=0)
])

# Callback para atualizar o gráfico
@app.callback(
    Output('exemplo-grafico', 'figure'),
    Input('atualizar-botao', 'n_clicks')
)
def update_graph(n_clicks):
    frutas, quantidade = generate_data()

    # Define as cores personalizadas
    cores = ['orange', 'orange', 'orange', 'orange']  # Cores para cada fruta

    # Cria o gráfico com cores personalizadas
    fig = px.bar(x=frutas, y=quantidade, color=frutas,
                 title="Quantidade de Frutas",
                 color_discrete_sequence=cores)

    return fig

# Executa o servidor
#if __name__ == '__main__':
    #app.run_server(debug=True)
