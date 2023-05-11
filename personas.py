class Personas:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self._edad = edad
        self.profesion = profesion

    def presentarse(self):
        print(f"hola, mi nombre es{self.nombre} y tengo {self._edad} años")

    def esta_es_mi_profesion(self):
        print(f"mi profesion es {self.profesion}")

    def get_edad(self):
        return self._edad
    def set_edad(self,edad):
        self._edad = edad

juan = Personas("juan", 20, "abogado")

juan.presentarse()
juan.esta_es_mi_profesion()
juan.set_edad("años")
print(juan.get_edad())

#------------------------------------------inherencie-------------------------------------
class Gente (Personas):
    def __init__(self, nombre, edad, profesion,lugar_de_nacimiento):
        super().__init__(nombre, edad, profesion)
        self.lugar_de_nacimiento = lugar_de_nacimiento
    def presentarse(self):
        print(f"\nnombre:{self.nombre}\nedad:{self._edad} \nprofesion:{self.profesion } \nlugar_de_nacimiento:{self.lugar_de_nacimiento}")
    def lugar(self):
        print(f"las personas les gusta trabajar en un espacio donde se sienta en hogar")

maria = Gente ("felipe","36","arqitecto","medellin")            
maria.presentarse()
maria.lugar()



