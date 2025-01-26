import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np

app = dash.Dash(__name__)

def generate_data():
    frutas = ["Maçã", "Banana", "Laranja", "Uva"]
    quantidade = np.random.randint(1, 10, size=4)
    return frutas, quantidade

app.layout = html.Div(children=[
    html.H1(children='Dash'),
    html.Div(children='Clique no botão para gerar novos dados para o gráfico.'),
    dcc.Graph(id='exemplo-grafico'),
    html.Button('Atualizar Gráfico', id='atualizar-botao', n_clicks=0)
])

@app.callback(
    Output('exemplo-grafico', 'figure'),
    Input('atualizar-botao', 'n_clicks')
)
def update_graph(n_clicks):
    frutas, quantidade = generate_data()

    cores = ['orange', 'blue', 'orange', 'orange'] 

    fig = px.bar(x=frutas, y=quantidade, color=frutas,
                 title="Quantidade de Frutas",
                 color_discrete_sequence=cores)

    return fig

# Executa o servidor
#if __name__ == '__main__':
#app.run_server(debug=True)  # Não deve ser executado quando usar Gunicorn
