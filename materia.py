class Materia:
    def __init__(self,profesor,salon,horario):
        self.profesor = profesor
        self._salon = salon
        self.horario = horario

    def pensum(self):
        print(F"la clase de matematicas la dicta el {self.profesor} en el {self._salon} 202")

    def tiempo(self): 
        print(f"a las {self.horario} de la tarde ") 

    def get_salon(self):
        return self._salon    
    def set_salon(self,salon):
        self._salon = salon

estudiante1 = Materia("profesor","salon","14:00")

estudiante1.pensum()
estudiante1.tiempo()
estudiante1.set_salon("curso")
print(estudiante1.get_salon())

#-----------------------------------------------------inherencie------------------------------------------

class Estudiante (Materia):
    def __init__(self,profesor,salon,horario,asignatura):
        super().__init__(profesor,salon,horario)
        self.asiganatura=asignatura
    def tiempo(self):
        print(f"\nprofesor:{self.profesor}\nsalon:{self._salon}\nhorario{self.horario}\nasignatura{self.asiganatura}") 
    def cronograma(self):
        print(f"en el cronograma la clase de matematicas esta en la franja de la tarde")

estudiante2 = Estudiante ("andres cortes","202"," 3 pm"," ciencias")
estudiante2.tiempo()
estudiante2.cronograma()

