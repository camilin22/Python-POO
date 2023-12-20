import json

class Libro:
    def __init__(self, titulo, autor, año_publicacion, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True
        self.unidades = unidades

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.año_publicacion})"
    
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []

    def mostrar_libros_disponibles(self):
        if not self.libros_disponibles:
            print("No hay libros disponibles en esta biblioteca.")
        else:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros_disponibles:
                print(libro)

    def prestar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                print(f"Se ha prestado el libro '{titulo}'")
                return
        print(f"El libro '{titulo}' no está disponible para ser prestado.")

    def recibir_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                print(f"Se ha recibido el libro '{titulo}' de vuelta")
                return
        print(f"No se puede recibir el libro '{titulo}'.")

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        print(f"Se ha agregado el libro '{libro.titulo}' a la biblioteca.")

    def quitar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo:
                self.libros_disponibles.remove(libro)
                print(f"Se ha quitado el libro '{titulo}' de la biblioteca.")
                return
        print(f"No se puede quitar el libro '{titulo}'.")

def guardar_libros_en_json(biblioteca, nombre_archivo):
    libros_data = []
    for libro in biblioteca.libros_disponibles:
        libro_info = {
            'titulo': libro.titulo,
            'autor': libro.autor,
            'año_publicacion': libro.año_publicacion,
            'disponible': libro.disponible,
            'unidades': libro.unidades
        }
        libros_data.append(libro_info)

    with open(nombre_archivo, 'w') as file:
        json.dump(libros_data, file, indent=4)
    print(f"Datos de la biblioteca guardados en '{nombre_archivo}'.")

def cargar_libros_desde_json(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        libros_data = json.load(file)

    biblioteca = Biblioteca()
    for libro_info in libros_data:
        libro = Libro(libro_info['titulo'], libro_info['autor'], libro_info['año_publicacion'], libro_info['unidades'])
        libro.disponible = libro_info['disponible']
        biblioteca.agregar_libro(libro)

    print(f"Datos de la biblioteca cargados desde '{nombre_archivo}'.")
    return biblioteca

# Ejemplo de uso
biblioteca1 = Biblioteca()
libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 1954, 10)
libro2 = Libro("Harry Potter y la piedra filosofal", "JK ROWLING", 1997, 6)

biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)

biblioteca1.mostrar_libros_disponibles()

biblioteca1.prestar_libro("El señor de los anillos")
biblioteca1.mostrar_libros_disponibles()

biblioteca1.recibir_libro("El señor de los anillos")
biblioteca1.mostrar_libros_disponibles()

guardar_libros_en_json(biblioteca1, "biblioteca1.json")

biblioteca2 = cargar_libros_desde_json("biblioteca1.json")
biblioteca2.mostrar_libros_disponibles()