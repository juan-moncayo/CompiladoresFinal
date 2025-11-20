# Guión interactivo generado

def menu():
    print("Menu")
    opcion = input("Jugar -> ")
    if opcion.strip():
        juego()
    opcion = input("Salir -> ")
    if opcion.strip():
        fin()

def juego():
    print("Jugando")

def fin():
    print("Adios")

if __name__ == '__main__':
    menu()