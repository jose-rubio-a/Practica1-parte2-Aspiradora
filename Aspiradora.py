from operator import index
from random import randint
from tabulate import tabulate

def calcular(estados,finales,acciones,inicial):
    caminos = []
    estado = inicial
    accion = 0
    caminos.append(estado)
    accionTotal = 0
    if estado in finales:
        caminos.append("Apagar")
        caminos.append(-1)
    else:
        while accionTotal < 2:
            seguir = True
            estado = inicial
            accion = accionTotal
            nuevoEstado = estados[estado][accion]
            while seguir:
                if nuevoEstado in finales:
                    seguir = False
                    caminos.append(acciones[accion])
                    caminos.append(nuevoEstado)
                    caminos.append(acciones[3])
                else:
                    if nuevoEstado in caminos:
                        accion = accion+1
                    else:
                        caminos.append(acciones[accion])
                        caminos.append(nuevoEstado)
                        accion=0
                if accion >= 3:
                    seguir = False
                    caminos.append(acciones[3])
                else:
                    nuevoEstado = estados[nuevoEstado][accion]
            caminos.append(-1)
            accionTotal=accionTotal+1
    return caminos

def busqueda(camino):
    indice = 0
    resultado = []
    separaciones = []
    i = 0
    k = 0
    while i < len(camino):
        camino.index(-1, i)
        separaciones.append(camino.index(-1, i))
        k=k+1
        i=i+camino.index(-1, i)+1
    i = 0
    k = 0
    while i < separaciones[k]:
        resultado.append(camino[i])
        i = i + 1
    costo = (len(resultado)/2)-1
    return resultado, costo

print("Numero de cuartos: 2")
nCuartos = 2
estados = [[4,0,1], [3,0,1],[6,2,3],[3,2,3],[4,4,5],[7,4,5],[6,6,7],[7,6,7]]
finales = [6,7]
acciones = ["Limpiar", "Izquierda", "Derecha", "Apagar"]

lugarAsp = randint(0, nCuartos-1)
cuartos = []
definirEstados = [[1,1,0], [1,1,1],[1,0,0],[1,0,1],[0,1,0],[0,1,1],[0,0,0],[0,0,1]]
estadoInicial = [1,1,lugarAsp]
inicial = 0
continuar = True

#Generar datos
for i in range(nCuartos):
    cuarto = ["Cuarto "+ str(i+1),"Sucio"]
    print("Cuarto " + str(i+1))
    respuesta = input("¿El cuarto esta limpio? ")
    if(respuesta.lower() == 'si'):
        cuarto[1] = "Limpio"
        estadoInicial[i] = 0
    if lugarAsp == i:
        cuarto.append("_/O")
    else:
        cuarto.append("")
    cuartos.append(cuarto)

print()
print(tabulate(cuartos, headers=["N° Cuarto", "Estado", "Aspiradora"], tablefmt='fancy_grid', stralign='center'))

inicial = definirEstados.index(estadoInicial)
resultado, costo = busqueda(calcular(estados,finales,acciones,inicial))

#Imprimir
print()
print("Acciones a realizar:\n")
print(resultado)
print()
print("Costo del camino: " + str(int(costo)))
print()
input("Presiona enter para finalizar el programa...")