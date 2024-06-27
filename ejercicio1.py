#EJERCICIO 1
from datetime import date, timedelta
import random
import os
class Fecha:
    def __init__(self, dia: int=None, mes: int=None, anio: int=None):
        if dia is None or mes is None or anio is None:
            hoy = date.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.anio = anio

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

    def __add__(self, dias):
        nueva_fecha = date(self.anio, self.mes, self.dia) + timedelta(days = dias)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def __eq__ (self, otra_fecha):
        return (self.dia == otra_fecha.dia and
                self.mes ==  otra_fecha.mes and
                self.anio == otra_fecha.anio)
    
    def calcular_dif_fecha(self, otra_fecha ):
        fecha1= date(self.anio, self.mes, self.dia)
        fecha2 = date(otra_fecha.anio, otra_fecha.mes, otra_fecha.dia)
        return abs((fecha2 - fecha1).days)