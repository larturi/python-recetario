import os
import shutil
from os import system
from pathlib import Path


def inicio(mi_ruta, finalizar_programa):
    
    while not finalizar_programa:
        limpiar()
        print('*' * 74)
        print('*' * 21 + ' BIENVENIDO AL RECETARIO PYTHON ' + '*' * 21)
        print('*' * 74)
        print('')
        print(f'Las recetas se encuentran en: {mi_ruta}')
        print(f'Total Recetas: {contar_recetas(mi_ruta)}')
        print('')
        menu = get_menu()
        
        if menu == 1:
            categorias = mostrar_categorias(mi_ruta)
            categoria = elegir_categoria(categorias)
            if categoria:
                recetas = mostrar_recetas(Path(mi_ruta, categoria))
                receta = elegir_receta(recetas)
                if receta:
                    leer_receta(Path(mi_ruta, categoria, receta))
                volver_inicio()

        elif menu == 2:
            categorias = mostrar_categorias(mi_ruta)
            categoria = elegir_categoria(categorias)
            
            if categoria:
                crear_receta(Path(mi_ruta, categoria))
                volver_inicio()

        elif menu == 3:
            crear_categoria(mi_ruta)
            volver_inicio()

        elif menu == 4:
            categorias = mostrar_categorias(mi_ruta)
            categoria = elegir_categoria(categorias)
            
            if categoria:
                recetas = mostrar_recetas(Path(mi_ruta, categoria))
                receta = elegir_receta(recetas)
                if receta:
                    eliminar_receta(Path(mi_ruta, categoria, receta))
                    volver_inicio()

        elif menu == 5:
            categorias = mostrar_categorias(mi_ruta)
            categoria = elegir_categoria(categorias)
            
            if categoria:
                eliminar_categoria(Path(mi_ruta, categoria))
                volver_inicio()

        elif menu == 6:
            finalizar_programa = True


def limpiar():
    if os.name == 'nt':
        system('cls')
    else:
        system('clear')


def get_menu():
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        # limpiar()
        print("Elige una opción:")
        print('---------------------------')
        print('[1] - Leer Receta')
        print('[2] - Crear Nueva Receta')
        print('[3] - Crear Nueva Categoría')
        print('[4] - Eliminar Receta')
        print('[5] - Eliminar Categoría')
        print('[6] - Salir')
        print('')
        eleccion_menu = input()
    return int(eleccion_menu)


def contar_recetas(path):
    contador = 0
    for archivo in Path(path).glob('**/*.txt'):
        contador += 1
    return contador


def mostrar_categorias(path):
    limpiar()
    print('Categorías:')
    print('--------------------')
    ruta_categorias = Path(path)
    lista_categorias = []
    contador = 0
    
    for carpeta in ruta_categorias.iterdir():
        if carpeta.is_dir():
            print(f'[{contador + 1}] - {carpeta.name}')
            lista_categorias.append(carpeta.name)
            contador += 1
            
    return lista_categorias


def elegir_categoria(lista_categorias):
    eleccion_correcta = 'x'
    print('')
    
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(0, len(lista_categorias) + 1):
        eleccion_correcta = input("Elige una categoría [0 - Cancelar]: ")
        
    if eleccion_correcta == '0':
        return False
    else:
        return lista_categorias[int(eleccion_correcta) - 1]


def mostrar_recetas(path):
    limpiar()
    print('Recetas:')
    print('-------------------------')
    ruta_recetas = Path(path)
    lista_recetas = []
    contador = 0
    
    for archivo in ruta_recetas.glob('*.txt'):
        print(f'[{contador + 1}] - {archivo.name}')
        lista_recetas.append(archivo.name)
        contador += 1
        
    return lista_recetas


def elegir_receta(lista_recetas):
    
    cantidad_recetas = len(lista_recetas)
    
    if cantidad_recetas == 0:
        print("No hay recetas para mostrar.")
    else:
        eleccion_correcta = 'x'
        print('')
        while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(0, len(lista_recetas) + 1):
            eleccion_correcta = input("Elige una receta [0 - Cancelar]: ")
            
        if eleccion_correcta == '0':
            return False
        else:
            return lista_recetas[int(eleccion_correcta) - 1]


def leer_receta(path_receta):
    limpiar()
    print(Path.read_text(path_receta))
    
    
def crear_receta(path):
    existe = False
    
    while not existe:
        limpiar()
        print('Crear Receta:')
        print('-------------------------')
        nombre_receta = input("Nombre de la receta: ")
        path_receta = Path(path, nombre_receta + '.txt')
        detalle_receta = input("Escribe tu receta: ")
        ruta_receta = Path(path, nombre_receta + '.txt')
        
        if not os.path.exists(ruta_receta):
            Path.write_text(ruta_receta, detalle_receta)
            existe = True
            print(f'Receta "{nombre_receta}" creada.')
        else:
            print("Ya existe una receta con ese nombre.")
            
            
def eliminar_receta(path_receta):
    Path(path_receta).unlink()
    limpiar()
    print(f'La receta "{path_receta.name}" ha sido eliminada.')
    

def eliminar_categoria(path_categoria):
    shutil.rmtree(path_categoria)
    limpiar()
    print(f'La categoría "{path_categoria.name}" ha sido eliminada.')
    
    
def crear_categoria(path):
    existe = False
    
    limpiar()
    
    print('Crear Categoría:')
    print('-------------------------')
    
    while not existe:
        nombre_categoria = input("Nombre de la categoría: ")
        ruta_nueva = Path(path, nombre_categoria)
        
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            existe = True
            print(f'Categoría "{nombre_categoria}" creada.')
            
        else:
            print("Ya existe una categoría con ese nombre.")
        

def volver_inicio():
    eleccion_regresar = 'x'
    
    while eleccion_regresar.lower() != 'v':
        print('')
        eleccion_regresar = input('Presione "V" para volver al inicio: ')
    