# Entidad Libro
class Libro:
    def _init_(self, isbn, titulo, autor, editorial, anio):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio = anio

# Entidad Autor
class Autor:
    def _init_(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

# Entidad Usuario
class Usuario:
    def _init_(self, id_usuario, nombre, direccion, telefono):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

# Entidad Préstamo
class Prestamo:
    def _init_(self, id_prestamo, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

# Entidad Editorial
class Editorial:
    def _init_(self, id_editorial, nombre, pais):
        self.id_editorial = id_editorial
        self.nombre = nombre
        self.pais = pais


import json
import os

class Repositorio:
    def _init_(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump([], f)

    def guardar(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, default=lambda o: o._dict_, indent=4)

    def cargar(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

class RepositorioLibros(Repositorio):
    def _init_(self):
        super()._init_('libros.json')

class RepositorioAutores(Repositorio):
    def _init_(self):
        super()._init_('autores.json')

class RepositorioUsuarios(Repositorio):
    def _init_(self):
        super()._init_('usuarios.json')

class RepositorioPrestamos(Repositorio):
    def _init_(self):
        super()._init_('prestamos.json')

class RepositorioEditoriales(Repositorio):
    def _init_(self):
        super()._init_('editoriales.json')


class Biblioteca:
    def _init_(self):
        self.repo_libros = RepositorioLibros()
        self.repo_autores = RepositorioAutores()
        self.repo_usuarios = RepositorioUsuarios()
        self.repo_prestamos = RepositorioPrestamos()
        self.repo_editoriales = RepositorioEditoriales()

    def agregar_libro(self, libro):
        libros = self.repo_libros.cargar()
        libros.append(libro)
        self.repo_libros.guardar(libros)

    def eliminar_libro(self, isbn):
        libros = self.repo_libros.cargar()
        libros = [libro for libro in libros if libro['isbn'] != isbn]
        self.repo_libros.guardar(libros)

    def consultar_libro(self, isbn):
        libros = self.repo_libros.cargar()
        for libro in libros:
            if libro['isbn'] == isbn:
                return libro
        return None

    def modificar_libro(self, isbn, nuevo_libro):
        libros = self.repo_libros.cargar()
        for i, libro in enumerate(libros):
            if libro['isbn'] == isbn:
                libros[i] = nuevo_libro
                break
        self.repo_libros.guardar(libros)


class InterfazUsuario:
    def _init_(self):
        self.biblioteca = Biblioteca()

    def mostrar_menu(self):
        while True:
            print("----------------------------------------MENU PRINCIPAL---------------------------------------------------------------------------------------")
            print("Eliga una de las siguientes opciones:")
            print("(1). -Agregar Libro- Si desea agregar un libro a su bliblioteca")
            print("(2). -Eliminar Libro- Si desea eliminar un libro de su bliblioteca")
            print("(3). -Consultar Libro- Si desea consultar la exitencia de un libro en su bliblioteca")
            print("(4). -Modificar Libro- Si desea modificar un libro de su biblioteca")
            print("(5). -Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.eliminar_libro()
            elif opcion == "3":
                self.consultar_libro()
            elif opcion == "4":
                self.modificar_libro()
            elif opcion == "5":
                break

    def agregar_libro(self):
        isbn = input("Ingrese ISBN: ")
        titulo = input("Ingrese Título: ")
        autor = input("Ingrese Autor: ")
        editorial = input("Ingrese Editorial: ")
        anio = input("Ingrese Año: ")
        libro = Libro(isbn, titulo, autor, editorial, anio)
        self.biblioteca.agregar_libro(libro._dict_)

    def eliminar_libro(self):
        isbn = input("Ingrese ISBN del libro a eliminar: ")
        self.biblioteca.eliminar_libro(isbn)

    def consultar_libro(self):
        isbn = input("Ingrese ISBN del libro a consultar: ")
        libro = self.biblioteca.consultar_libro(isbn)
        if libro:
            print(libro)
        else:
            print("Libro no encontrado.")

    def modificar_libro(self):
        isbn = input("Ingrese ISBN del libro a modificar: ")
        titulo = input("Ingrese nuevo Título: ")
        autor = input("Ingrese nuevo Autor: ")
        editorial = input("Ingrese nueva Editorial: ")
        anio = input("Ingrese nuevo Año: ")
        nuevo_libro = Libro(isbn, titulo, autor, editorial, anio)
        self.biblioteca.modificar_libro(isbn, nuevo_libro._dict_)

# Inicializar la interfaz y mostrar el menú
interfaz = InterfazUsuario()
interfaz.mostrar_menu()


class Biblioteca:

    def generar_reporte_libros(self):
        libros = self.repo_libros.cargar()
        with open('reporte_libros.json', 'w') as f:
            json.dump(libros, f, indent=4)
        print("Reporte de libros guardado en reporte_libros.json")

    # Generar reportes similares para autores, usuarios, préstamos y editoriales.2
