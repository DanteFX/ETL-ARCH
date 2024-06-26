##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: application.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define la aplicación que sirve la UI y la lógica 
#   del componente
#
#-------------------------------------------------------------------------
from src.view.dashboard import Dashboard
import dash_bootstrap_components as dbc
import dash
from datetime import datetime
from dash.dependencies import Input, Output, State
from dash import html

app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.title = "ETL"

dashboard = Dashboard()

app.layout = dashboard.document(start_date=datetime(2010, 1, 1), end_date=datetime.now())

@app.callback(
    Output(component_id='output-container-date-picker-range', component_property='children'),
    [Input(component_id='Update-button', component_property='n_clicks')],
    [State(component_id='date-picker-range', component_property='start_date'),
    State(component_id='date-picker-range', component_property='end_date')],
    prevent_initial_call=True
)

def update(n_clicks, start_date:datetime, end_date:datetime):
    if n_clicks > 0:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        
        # Validación para verificar si el período seleccionado excede los 40 días
        delta = end_date - start_date
        if delta.days > 40:
            return html.Div("El período seleccionado excede los 40 días. Por favor, selecciona un rango de fechas más corto.")
        
        # Si el período es válido, actualizamos el contenido del tablero con los nuevos datos
        updated_content = dashboard._highlights_cards(start_date=start_date, end_date=end_date)
        
        # Aquí agregamos los demás componentes que queremos actualizar
        
        return (
                html.Br(),
                html.H1("Indicadores de ventas de todas las sucursales"),
                html.Br(),
                dashboard._highlights_cards(start_date=start_date, end_date=end_date), 
                ## dashboard._bar_chart_providers_by_location(),
                dashboard._bar_chart_sales_per_location(start_date=start_date, end_date=end_date),
                dashboard._panel_best_sellers(start_date=start_date, end_date=end_date),
                dashboard._panel_worst_sales(start_date=start_date, end_date=end_date),
                html.Br(),
                html.Br(),
                ## esto ultimo de ser necesario eliminar si se llega a ver mal con lo que implementen por favor.
                html.H1("Reporte General"),
                html.Br(),
                html.Br(),
                )
    