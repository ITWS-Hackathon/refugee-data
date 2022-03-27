from dash import Dash, html, dcc

import plotly.express as px

import pandas as pd


data = pd.read_csv("data_continents.csv", on_bad_lines='skip')

# print(data.head())

# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")

# data.sort_values("Value", inplace=True)
# print(data["Inbound Continent"])

app = Dash(__name__)

fig = px.bar(data, x="Year", y="Value", color="Location", barmode="group")
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])



if __name__ == "__main__":

    app.run_server(debug=True)