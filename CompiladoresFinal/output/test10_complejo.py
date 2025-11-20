# Guión interactivo generado

def entrada():
    print("Bifurcacion")
    opcion = input("Izquierda -> ")
    if opcion.strip():
        izq()
    opcion = input("Derecha -> ")
    if opcion.strip():
        der()

def izq():
    print("Tesoro")
    opcion = input("Volver -> ")
    if opcion.strip():
        entrada()

def der():
    print("Dragon")
    opcion = input("Huir -> ")
    if opcion.strip():
        entrada()

if __name__ == '__main__':
    entrada()