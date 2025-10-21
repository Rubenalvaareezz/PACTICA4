import csv
from collections import namedtuple

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_csv):

    with open (ruta_csv, encoding = "utf-8") as f:  
        lector = csv.reader(f)
        lista_poblacion = []
        for pais, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
            tupla = RegistroPoblacion(pais, codigo, año, censo)
            lista_poblacion.append(tupla)
    return lista_poblacion

def tipo_paises(lista_poblacion):
  paises_ordenados = []
  for poblacion in lista_poblacion:
      paises_ordenados.append(lista_poblacion[0])
      nombres
        
        
        
            
            