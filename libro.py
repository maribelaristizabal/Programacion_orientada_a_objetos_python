class Libros:
    #atributos
    def __init__(self, autor, categoria,editorial,):
        self._autor = autor
        self._categoria = categoria
        self.editorial = editorial

#metodos
    def descripcion(self):
        print(f"quiero saber que libros de {self._categoria} manejas y que {self.editorial} es") 

    def el_mas_vendido(self):
        print(f"cual es el libro de {self._autor} mas vendidos")
    
    def get_autor(self):
        return self._autor
    def set_autor(self,autor):
        self._autor = autor

    def get_categoria(self):
        return self._categoria
    def set_categoria(self,categoria):
        self._categoria = categoria 

#instaciar o crear objeto
persona1 = Libros("william shakespeare", "drama", "editorial")     
# mando a imprimir lo que tengo en los metodos
persona1.descripcion()
persona1.el_mas_vendido()
persona1.set_autor("nombre")
print(persona1.get_autor())
persona1.set_categoria("generos")
print(persona1.get_categoria())
 
#--------------------------------inherencie---------------------------------------------------
#la primera letra de cualquier clase es en mayuscula siempreee
class Revista (Libros):
    def __init__(self, autor, categoria, editorial,numero_paginas):
        #se coloca en remplazo de las lineas de la 4 a 6 
        super().__init__(autor, categoria, editorial)
        #nuevo atributo
        self.numero_paginas=numero_paginas
#polimosfirmo: es cuando en la clase hija repito el nombre de un metodo o de mas metodos si quiero eso seria polimosfirmo faltaria llamarlos con el nuevo objeto creado
    def descripcion(self):
        print(f"\nautor:{self._autor}\ncategoria: {self._categoria}\neditorial: {self.editorial}\nnumero_paginas: {self.numero_paginas}")
    def leer(self):
        print(f"el mas vendido siempre a sido el señor de los anillos")

persona2 = Revista ("gabriel garcia marquez","terror","norma","500")
persona2.descripcion()
persona2.leer()

persona3 = Revista (" miguel de cervantes","suspenso","gatico","250")
persona3.descripcion()
persona3.leer()









 # el encapsulamiento es colocarle una _ a los atributos desoues del self.
 # retum se coloca siempre despues del get

        