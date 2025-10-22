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
        
        
        
            
            