def ordenar_lista(lista: ListaDoblementeEnlazada):
    if lista.cabeza is None:
        return lista

    cambiando = True
    while cambiando:
        cambiando = False
        actual = lista.cabeza
        while actual.siguiente is not None:
            actual_fecha_ingreso = actual.dato.datos["FechaIngreso"]
            siguiente_fecha_ingreso = actual.siguiente.dato.datos["FechaIngreso"]
            if siguiente_fecha_ingreso.calcular_dif_fecha(Fecha()) < actual_fecha_ingreso.calcular_dif_fecha(Fecha()):
                actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                cambiando = True
            actual = actual.siguiente
    return lista

listaEJ2 = ordenar_lista(ListaDoblementeEnlazada().lista_ejemplo())
for alm in listaEJ2:
    print(alm)
