# Guión interactivo generado

def menu():
    print("Menu")
    opcion = input("Jugar -> ")
    if opcion.strip():
        juego()
    opcion = input("Menu -> ")
    if opcion.strip():
        menu()

def juego():
    print("Juego")
    opcion = input("Volver -> ")
    if opcion.strip():
        menu()

if __name__ == '__main__':
    menu()