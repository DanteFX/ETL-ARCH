##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: repository.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define el acceso e interacción entre el componente
#   y el API
#
#-------------------------------------------------------------------------
from src.data.provider import Provider
from src.data.queries import Queries
from datetime import datetime

class Repository:

    @staticmethod
    def get_products():
        response = Provider.execute(Queries.get_total_products())
        return response

    @staticmethod
    def get_providers():
        response = Provider.execute(Queries.get_total_providers())
        return response

    @staticmethod
    def get_locations():
        response = Provider.execute(Queries.get_total_locations())
        return response

    @staticmethod
    def get_orders():
        response = Provider.execute(Queries.get_total_orders())
        return response

    @staticmethod
    def get_sales(start_date: datetime, end_date: datetime):
        response = Provider.execute(Queries.get_total_sales_by_date(start_date=start_date, end_date=end_date))
        return response

    @staticmethod
    def get_providers_by_location():
        response = Provider.execute(Queries.get_providers_per_location())
        return response

    @staticmethod
    def get_sales_by_location(start_date: datetime, end_date: datetime):
        response = Provider.execute(Queries.get_sales_per_location_by_date(start_date=start_date, end_date=end_date))
        return response

    @staticmethod
    def get_orders_by_location():
        response = Provider.execute(Queries.get_orders_per_location())
        return response

    @staticmethod
    def get_best_sellers(start_date: datetime, end_date: datetime):
        response = Provider.execute(Queries.get_best_sellers_by_date(start_date=start_date, end_date=end_date))
        return response

    @staticmethod
    def get_worst_sales(start_date: datetime, end_date: datetime):
        response = Provider.execute(Queries.get_worst_sales_by_date(start_date=start_date, end_date=end_date))
        return response
    
    @staticmethod
    def get_most_selled_products():
        response = Provider.execute(Queries.get_most_selled_products())
        return response
    @staticmethod
    def get_sales(start_date: datetime, end_date: datetime):
        response = Provider.execute(Queries.get_total_sales_by_date(start_date=start_date, end_date=end_date))
        return response