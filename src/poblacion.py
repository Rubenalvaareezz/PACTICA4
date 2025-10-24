import csv
from collections import namedtuple

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_csv):

    with open (ruta_csv, encoding = 'utf-8') as f:  
        lector = csv.reader(f)
        lista_poblacion = []
        for pais, codigo, año, censo in lector:
            pais = str(pais)
            codigo = str(codigo)
            año = int(año)
            censo = int(censo)
            tupla = RegistroPoblacion(pais, codigo, año, censo)
            lista_poblacion.append(tupla)
    return lista_poblacion

def tipo_paises(tupla):
    lista_paises = []
    for pais in tupla:
        lista_paises.append(pais[0])

    nombres_paises = set(lista_paises)
    return sorted(nombres_paises)
        
def filtra_por_pais(lista_poblacion, nombre_o_codigo):
    lista_nombre_o_codigos = []
    for r in lista_poblacion:  
        if r == lista_poblacion[0] or r == lista_poblacion[1]:
            lista_nombre_o_codigos.append(lista_poblacion[2]  lista_poblacion[3])
    return lista_nombre_o_codigos
        
            
            