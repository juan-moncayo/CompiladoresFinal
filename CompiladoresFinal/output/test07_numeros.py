# Guión interactivo generado

def nivel1():
    print("Nivel 1")
    opcion = input("Ir -> ")
    if opcion.strip():
        nivel2()

def nivel2():
    print("Nivel 2")
    opcion = input("Ir -> ")
    if opcion.strip():
        nivel3()

def nivel3():
    print("Nivel 3")

if __name__ == '__main__':
    nivel1()