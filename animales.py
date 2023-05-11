class Animales:
    def __init__(self,nombre,alimentacion,entorno):
         self._nombre = nombre
         self.alimentacion = alimentacion
         self.entorno = entorno

    def descripcion(self):
        print(f"el {self._nombre}  es el animal mas grande del mundo,se alimenta de plantas ya que pertenencen al grupo de los {self.alimentacion}")     
    
    def lugar(self):
        print(f"los animales se clasifican segun {self.entorno} donde vivan ")

    def get_nombre(self):
        return self._nombre
    def set_nombre(self,nombre):
        self._nombre = nombre

animal1 = Animales("elefante","hervivoros","entorno") 

animal1.descripcion()
animal1.lugar()
animal1.set_nombre("llamar")
print(animal1.get_nombre())

#-------------------------------------------inherencie-----------------------------------------------------
class Tipo (Animales):
    def __init__(self, nombre,alimentacion,entorno,color):
        super().__init__(nombre, alimentacion, entorno)
        self.color = color 
    def lugar(self):
        print(f"\nnombre:{self._nombre} \nalimentacion:{self.alimentacion} \nentorno:{self.entorno} \ncolor:{self.color}")
    def ecosistema(self):
        print(f"Llamamos ecosistema al sistema físico y biológico formado por una comunidad de seres vivos que habita en un medio físico delimitado")   

animal2 = Tipo ("tiburon","carnivora","acuatico","gris")
animal2.lugar()
animal2.ecosistema()
