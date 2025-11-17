from biblioteca import Biblioteca
from libro import Libro

def menu():
    print("""
========== SISTEMA DE BIBLIOTECA ==========
1. Agregar libro
2. Listar libros
3. Prestar libro
4. Devolver libro
5. Salir
""")

def main():
    b = Biblioteca()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = input("Año: ")
            genero = input("Género: ")

            libro = Libro(titulo, autor, anio, genero)
            b.agregar_libro(libro)

        elif opcion == "2":
            b.listar_libros()

        elif opcion == "3":
            titulo = input("Ingrese el título del libro a prestar: ")
            b.prestar_libro(titulo)

        elif opcion == "4":
            titulo = input("Ingrese el título del libro a devolver: ")
            b.devolver_libro(titulo)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("\nOpción inválida.\n")

if __name__ == "__main__":
    main()
