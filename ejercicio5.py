def manejar_directorios(lista_alumnos:ListaDoblementeEnlazada,dir:str,nuevo_dir:str):
    dir = comprobarDir(dir)
    nuevo_dir = comprobarDir(nuevo_dir)
    archivo = "lista_alumnos.txt"

    # Creando el directoroi para guardar el archivo de lista de aumnos
    if not os.path.exists(dir):
        os.makedirs(dir)

    # Guardando lista de alumnos en un archivo txt
    with open(os.path.join(dir, archivo), 'w') as f:
        for alumno in lista_alumnos:
            f.write(str(alumno) + "\n")

    # Mover el directorio
    if os.path.exists(dir):
        os.rename(dir, nuevo_dir)

    print(os.path.join(nuevo_dir, archivo))
    
    # Borrar archivo y directorio
    if os.path.exists(os.path.join(nuevo_dir, archivo)):
        os.remove(os.path.join(nuevo_dir, archivo))

    if os.path.exists(nuevo_dir):
        os.rmdir(nuevo_dir)

def comprobarDir(dir:str):
    if os.path.exists(dir):
        print("El directorio ya existe, inserte un nuevo directorio a continuacion")
        dir = input()
        return comprobarDir(dir)
    else:
        return dir

listaEJ3 = ordenar_lista(ListaDoblementeEnlazada().lista_ejemplo())
manejar_directorios(listaEJ3,"Dir1","nuevo_alumnos_dir")