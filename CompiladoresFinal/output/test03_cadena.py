# Guión interactivo generado

def cap1():
    print("Capitulo 1")
    opcion = input("Siguiente -> ")
    if opcion.strip():
        cap2()

def cap2():
    print("Capitulo 2")
    opcion = input("Siguiente -> ")
    if opcion.strip():
        cap3()

def cap3():
    print("Fin")

if __name__ == '__main__':
    cap1()