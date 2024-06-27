## Ejercicio 2:
class Alumno:
    def __init__(self, nombre:str, dni:int, fecha_ingreso:Fecha, carrera):
        self.datos={
            "Nombre": nombre,
            "D.N.I": dni,
            "Fecha de ingreso": fecha_ingreso,
            "Carrera": carrera
        }
    
    def __str__(self):
        return f"Nombre: {self.datos["Nombre"]}, D.N.I:{self.datos["D.N.I"]}, Fecha de ingreso:{self.datos["Carrera"]})

    def __eq__(self, otro_alumno):
        return self.datos ["D.N.I"]== otro_alumno.datos["D.N.I"]

    
    def cambiar_datos (self, **kwargs):
        for key, value in kwargs.items():
            if key in self.datos:
                self.datos[key] = value

    def antiguedad(self):
        hoy= Fecha()
        fecha_ingreso= Fecha(self.datos["Fecha de ingreso"].dia, self.datos["Fecha de ingreso"].mes, self.datos["Fecha de ingreso"].anio)
        return hoy.calcular_dif_fecha(fecha_ingreso)

#ejemplo de uso
alumn= Alumno("Diego", 43245535, Fecha(), "Tecnicatura en Programacion")
alumn.cambiar_datos(nombre= "Diego",dni= 43245535, fecha_ingreso=Fecha(5,2,2024), carrera= "Tecnicatura en Programacion")
print(alumn.datos["D.N.I"])
print(alumn.antiguedad())