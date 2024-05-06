##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: dashboard.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define los elementos visuales de la pantalla
#   del tablero
#
#-------------------------------------------------------------------------
from src.controller.dashboard_controller import DashboardController
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import dcc, html
from datetime import datetime

class Dashboard:

    def __init__(self):
        pass

    def document(self, start_date:datetime, end_date:datetime):
        return dbc.Container(
            fluid = True,
            children = [
                html.Br(),
                self._header_title("Sales Report"),
                html.Div(html.Hr()),
                self._header_subtitle("Sales summary financial report"),
                html.Br(),
                html.P("Indique la fecha para generar el reporte de los indicadores de ventas", style={"font-style": "italic", "margin-bottom": "10px"}),
                dbc.Row(
                    [
                        dbc.Col(
                        [
                            dcc.DatePickerRange(
                                id='date-picker-range',
                                min_date_allowed = datetime(2010, 1, 1),
                                max_date_allowed = datetime.now(),
                            ),
                            dbc.Button("Update", id="Update-button", color="primary", className="mr-1", n_clicks=0),
                        ],
                        width={"size": 7},
                        ),
                    ]
                ),
                html.Br(),
                html.Div(id='output-container-date-picker-range', children=html.Div(id='updated-content')),
                self._highlights_cards(start_date=start_date, end_date=end_date),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_providers_by_location(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_sales_per_location(start_date=start_date, end_date=end_date),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_orders_per_location(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._panel_best_sellers(start_date=start_date, end_date=end_date),
                                    width=6
                                ),
                                dbc.Col(
                                    self._panel_worst_sales(start_date=start_date, end_date=end_date),
                                    width=6
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._panel_most_selled_products(start_date=start_date, end_date=end_date),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
            ]
        )

    def _header_title(self, title):
        return dbc.Row(
            [
                dbc.Col(html.H2(title, className="display-4"))
            ]
        )

    def _header_subtitle(self, subtitle):
        return html.Div(
            [
                html.P(
                    subtitle,
                    className="lead",
                ),
            ],
            id="blurb",
        )

    def _card_value(self, label, value):
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H2(value, className="card-title"),
                    ]
                ),
                dbc.CardFooter(label),
            ]
        )

    def _highlights_cards(self, start_date:datetime, end_date:datetime):
        products = DashboardController.load_products()
        orders = DashboardController.load_orders()
        providers = DashboardController.load_providers()
        locations = DashboardController.load_locations()
        sales = DashboardController.load_sales(start_date=start_date, end_date=end_date)
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            self._card_value("Products", products["products"])
                        ),
                        dbc.Col(
                            self._card_value("Orders", orders["orders"])
                        ),
                        dbc.Col(
                            self._card_value("Providers", providers["providers"])
                        ),
                        dbc.Col(
                            self._card_value("Locations", locations["locations"])
                        ),
                        dbc.Col(
                            self._card_value("Sales", "$ {:,.2f}".format(float(sales['sales'])))
                        ),
                    ]
                ),
            ]
        )

    def _bar_chart_providers_by_location(self):
        data = DashboardController.load_providers_per_location()
        bar_char_fig = px.bar(data, x="location", y="providers")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Providers per location", className="card-title"),
                        dcc.Graph(
                            id='providers-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _bar_chart_sales_per_location(self, start_date: datetime, end_date: datetime):
        data = DashboardController.load_sales_per_location(start_date=start_date, end_date=end_date)
        bar_char_fig = px.bar(data, x="location", y="sales")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Sales per location", className="card-title"),
                        dcc.Graph(
                            id='sales-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _bar_chart_orders_per_location(self):
        data = DashboardController.load_orders_per_location()
        bar_char_fig = px.bar(data, x="location", y="orders")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Orders per location", className="card-title"),
                        dcc.Graph(
                            id='orders-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _panel_best_sellers(self, start_date:datetime, end_date:datetime):
        best_sellers = DashboardController.load_best_sellers(start_date=start_date, end_date=end_date)
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Best sellers", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- [{sale['invoice']}] $ {sale['total']:,.2f}", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for sale in best_sellers
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def _panel_worst_sales(self, start_date:datetime, end_date:datetime):
        worst_sales = DashboardController.load_worst_sales(start_date=start_date, end_date=end_date)
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Worst sales", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- [{sale['invoice']}] $ {sale['total']:,.2f}", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for sale in worst_sales
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def _panel_most_selled_products(self, start_date:datetime, end_date:datetime):
        most_selled = DashboardController.load_most_selled_products()
        
        # Crear una tabla HTML para mostrar los productos más vendidos
        table_content = html.Table(
            # Cabecera de la tabla
            [html.Tr([html.Th("Producto", style={'padding': '10px'}),
                    html.Th("Piezas vendidas", style={'padding': '10px'}),
                    html.Th("Período", style={'padding': '10px'})],
                    style={'background-color': '#f2f2f2', 'color': 'black', 'margin-bottom': '10px'})] +
            # Filas de la tabla
            [html.Tr([
                html.Td(product['product'], style={'padding': '10px'}),
                html.Td(product['times'], style={'padding': '10px'}),
                html.Td(f"{start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}", style={'padding': '10px'})
            ], style={'background-color': 'white', 'color': 'black', 'margin-bottom': '10px'}) for product in most_selled]
        )

        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H1("Productos más vendidos", className="card-title"),
                                html.Br(),
                                html.H4("Reporte de productos más vendidos", className="card-title"),
                                # Mostrar la tabla de productos más vendidos
                                table_content
                            ]
                        )
                    ]
                )
            ],
            style={'padding': '20px'}
        )
