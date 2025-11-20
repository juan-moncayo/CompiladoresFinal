# Guión interactivo generado

def inicio():
    print("Hola! Como estas?")
    print("Simbolos: @#$%")
    opcion = input("Ok -> ")
    if opcion.strip():
        fin()

def fin():
    print("Adios!")

if __name__ == '__main__':
    inicio()