class Bebidas:
    def __init__(self, nombres, num_grados, tipo):
        self._nombres = nombres
        self.num_grados = num_grados
        self.tipo = tipo

    def describir(self):
        print(f"la bebida {self._nombres} tiene {self.num_grados} grados de alcohol")

    def el_mas_vendido(self):
        print(f"la {self.tipo} es el licor mas vendido")
    
    def get_nombres(self):
        return self._nombres
    def set_nombres(self,nombres):
        self._nombres = nombres

licor1 = Bebidas("aguila", 5, "cerveza")    

licor1.describir()
licor1.el_mas_vendido()
licor1.set_nombres("marca")
print(licor1.get_nombres())


#-----------------------------inherencia---------------------------------

class Aguardiente(Bebidas):
    def __init__(self,nombre,num_grados,tipo,color):
        super().__init__(nombre,num_grados,tipo)
        self.color=color
    def describir(self):
        print(f"\nnombre:{self._nombres}\nnum_grados:{self.num_grados}\ntipo:{self.tipo}\ncolor:{self.color} ")
    def tantear(self):
        print("la bebida mas tomada es la cerveza")
licor2 = Aguardiente("antioqueño","30 grados","aguardiente","transparente")        
#licor2 = Aguardiente("antioqueño", 30, "aguardiente", "transparente")      
licor2.describir() 
licor2.tantear()      