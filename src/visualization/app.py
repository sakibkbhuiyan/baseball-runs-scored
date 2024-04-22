import dash
from dash import Dash, dcc, html, callback, Output, Input 
import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output
import pandas as pd 
import numpy as np 
import plotly.graph_objects as go

## ****************************************************************************************************
##
## Import & clean data
##
## ****************************************************************************************************
 
file_path = '../../data/processed/game_log_all.csv'

df = pd.read_csv(file_path, index_col = False)
selected_columns = ['Year', 'Date', 'Era', 'Visiting_Team_Score', 'Home_Team_Score']
df = df[selected_columns]

## Convert column names to lower snake case
df.columns = [col.lower().replace(' ', '_') for col in df.columns]
df['date'] = pd.to_datetime(df['date'])
df['score_difference'] = abs(df['visiting_team_score'] - df['home_team_score'])

era_labels = ['Pre-1900', 'Dead Ball era', 'Live Ball era', 'Integration era', 'Expansion era', 'Free Agent era', 'Steroid era', 'Contemporary era']
df['era'] = pd.Categorical(df['era'], categories = era_labels, ordered = True)

group_columns = ['era', 'visiting_team_score', 'home_team_score']

df_agg = df.groupby(group_columns).agg(
    {
        'year': 'count'
    }
)

df_agg.reset_index(drop = False, inplace = True)
df_agg.rename(columns = {'year': 'game_count'}, inplace = True)

## Replace 0's with NaN
df_agg['game_count'] = df_agg['game_count'].replace(0, np.nan)

unique_eras = df_agg['era'].unique().tolist()
chosen_era_1 = unique_eras[-1]
df_agg_filtered = df_agg[df_agg['era'] == chosen_era_1]
df_filtered = df[df['era'] == chosen_era_1]

## Set axis limits for plots 
axis_upper_bound_heat = max(max(df_agg['home_team_score']), max(df_agg['visiting_team_score']))
axis_upper_bound_hist = max(df['score_difference'])

## Set plot colors 
colors = {"background": "#5E6572", "foreground": "#EEF1EF"}



## ****************************************************************************************************
##
## Create Dash app
##
## ****************************************************************************************************

app = dash.Dash(__name__)

## Define the layout of the app
app.layout = html.Div([
    html.Br(),
    html.H1("Runs Scored in Different Eras"),
    html.Br(), 
    html.Br(), 
    dbc.Row([
        dbc.Col(html.Div([
            html.H3("Please choose an era:"), 
            dcc.Dropdown(id = "era_filter_1", options = unique_eras, value = unique_eras[-1]), 

            ## Heatmap
            dcc.Graph(
                id='heatmap_1',
                figure={}
            ),
            
            ## Histogram
            dcc.Graph(
                id='histogram_1',
                figure={}
        )
        ]), style = {'width': '50%', 'display': 'inline-block'}), 

        dbc.Col(html.Div([
            html.H3("Choose a second era:"), 
            dcc.Dropdown(id = "era_filter_2", options = unique_eras, value = unique_eras[0]), 

            ## Heatmap
            dcc.Graph(
                id='heatmap_2',
                figure={}
            ),
            
            ## Histogram
            dcc.Graph(
                id='histogram_2',
                figure={}
            )
        ]), style = {'width': '50%', 'display': 'inline-block'})
    ]
    )
])


## Add controls to build the interaction 
@app.callback(
    Output(component_id="heatmap_1", component_property="figure"), 
    Input(component_id="era_filter_1", component_property="value")
)
def update_heatmap(chosen_era): 
    df_agg_filtered = df_agg[df_agg['era'] == chosen_era]
    fig = go.Figure(data=go.Heatmap(
        x=df_agg_filtered['home_team_score'].astype(object),
        y=df_agg_filtered['visiting_team_score'].astype(object),
        z=df_agg_filtered['game_count'],
        colorscale='Magma',
        hoverongaps = False))
    fig.update_layout(
        title=f"{chosen_era}",
        xaxis_title='Home Team Score',
        yaxis_title='Visiting Team Score',
        width=1000,
        height=1000,
        yaxis=dict(range = [axis_upper_bound_heat, -0.5], dtick = 1, showgrid = False, zeroline = False),
        xaxis = dict(range = [-0.5, axis_upper_bound_heat], side = 'top', dtick = 1, tickangle=0, showgrid = False, zeroline = False), 
        plot_bgcolor=colors['background'], 
        font=dict(family="Courier New", size=14, color="black"), 
        title_x = 0.5, 
        title_xanchor = 'center', 
        title_y = 0.98
    )
    fig.update_traces(showscale = False)
    return fig 


@app.callback(
    Output(component_id="heatmap_2", component_property="figure"), 
    Input(component_id="era_filter_2", component_property="value")
)
def update_heatmap(chosen_era): 
    df_agg_filtered = df_agg[df_agg['era'] == chosen_era]
    fig = go.Figure(data=go.Heatmap(
        x=df_agg_filtered['home_team_score'].astype(object),
        y=df_agg_filtered['visiting_team_score'].astype(object),
        z=df_agg_filtered['game_count'],
        colorscale='Magma', 
        hoverongaps = False))
    fig.update_layout(
        title=f"{chosen_era}",
        xaxis_title='Home Team Score',
        yaxis_title='Visiting Team Score',
        width=1000,
        height=1000,
        yaxis=dict(range = [axis_upper_bound_heat, -0.5], dtick = 1, showgrid = False, zeroline = False),
        xaxis = dict(range = [-0.5, axis_upper_bound_heat], side = 'top', dtick = 1, tickangle=0, showgrid = False, zeroline = False), 
        plot_bgcolor=colors['background'], 
        font=dict(family="Courier New", size=14, color="black"), 
        title_x = 0.5, 
        title_xanchor = 'center', 
        title_y = 0.98
    )
    fig.update_traces(showscale = False)
    return fig 


@app.callback(
    Output(component_id="histogram_1", component_property="figure"), 
    Input(component_id="era_filter_1", component_property="value")
)
def update_histogram(chosen_era):
    df_filtered = df[df['era'] == chosen_era]
    fig = go.Figure(data=go.Histogram(x=df_filtered['score_difference'], histnorm='density', marker=dict(color=colors['foreground'])))
    fig.update_layout(
        xaxis_title='Score Difference',
        yaxis_title='Density',
        width=1000,
        height=400,
        xaxis = dict(range = [0, axis_upper_bound_hist], dtick = 1),
        plot_bgcolor=colors['background'],
        font=dict(family="Courier New", size=14, color="black")
    )
    return fig 


@app.callback(
    Output(component_id="histogram_2", component_property="figure"), 
    Input(component_id="era_filter_2", component_property="value")
)
def update_histogram(chosen_era):
    df_filtered = df[df['era'] == chosen_era]
    fig = go.Figure(data=go.Histogram(x=df_filtered['score_difference'], histnorm='density', marker=dict(color=colors['foreground'])))
    fig.update_layout(
        xaxis_title='Score Difference',
        yaxis_title='Density',
        width=1000,
        height=400,
        xaxis = dict(range = [0, axis_upper_bound_hist], dtick = 1),
        plot_bgcolor=colors['background'],
        font=dict(family="Courier New", size=14, color="black")
    )
    return fig 


## Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
