class Nodo:
    def __init__(self, dato: Alumno):
        self.dato: Alumno= dato
        self.siguiente: Nodo= None
        self.anterior: Nodo= None

class ListaDoblementeEnlazada:
    def__init__(self):
        self.cabeza: Nodo= None
        self.cola: Nodo= None

    def limpiar(self):
        self.cabeza: Nodo = None
        self.cola: Nodo= None

    def agregar(self, alumno: Alumno):
        nuevo_nodo= Nodo(alumno)
        if self.cabeza is None:
            self.cabeza= nuevo_nodo
            self.cola= nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior= self.cola
            self.cola= nuevo_nodo
    def __iter__(self):
        actual= self.cabeza
        while actual is not None:
            yield actual.dato
            actual= actual.siguiente
    def lista_ejemplo(self):
        nombres = ["Arturo", "Fran", "Bartolomeo", "Samantha"]
        for i in range(4):
            fecha_ingreso = Fecha(random.randint(1, 28), random.randint(1, 12), random.randint(2010, 2023))
            alumno = Alumno(nombres[i], random.randint(10000000, 99999999), fecha_ingreso, "Carrera" + str(i+1))
            self.agregar(alumno)
        return self

listaEJ = ListaDoblementeEnlazada().lista_ejemplo()
for alm in listaEJ:
    print(alm)

print("--------------------------------------------------------")                        
