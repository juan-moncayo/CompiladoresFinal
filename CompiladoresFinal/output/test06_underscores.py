# Guión interactivo generado

def nivel_1():
    print("Nivel 1")
    opcion = input("Siguiente -> ")
    if opcion.strip():
        nivel_2()

def nivel_2():
    print("Nivel 2")

if __name__ == '__main__':
    nivel_1()