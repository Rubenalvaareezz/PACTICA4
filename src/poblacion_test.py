from poblacion import *

#Apartado 1

    
fichero = lee_poblaciones("data/population.csv")

# paises = tipo_paises(fichero)
# for r in paises:
#     print(f"el nombre de los paises es: {r} ")


informacion = filtra_por_pais(fichero, "ARB")
for r in informacion:
    print(r)