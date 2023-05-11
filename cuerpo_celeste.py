class Cuerpo_celeste:
   def __init__(self, planeta, estrella, asteroides):
    self.planeta = planeta
    self.estrella = estrella
    self._asteroides = asteroides

   def descripcion(self):
     print(f"la {self.planeta} es un cuerpo celeste solido que gira al rededor del {self.estrella}")

   def lugar(self):
     print(f"los {self._asteroides}es un cuerpo celeste rocorso mas pequeño que un planeta")
  
   def get_asteroides(self):
       return self._asteroides
   def set_asteroides(self,asteroides):
      self._asteroides = asteroides

cuerpo1 = Cuerpo_celeste("tierra","sol","asteroides")

cuerpo1.descripcion()
cuerpo1.lugar()
cuerpo1.set_asteroides("constelacion")
print(cuerpo1.get_asteroides())

#------------------------------------inheritance--------------------------------------
class tierra (Cuerpo_celeste):
  def __init__(self, planeta, estrella, asteroides,metiorito):
    super().__init__(planeta, estrella, asteroides)
    self.metiorito = metiorito 

  def descripcion(self):
      print(f"\nplaneta:{self.planeta} \nestrella:{self.estrella} \nasteroide:{self._asteroides}\nmetiorito:{self.metiorito}")
  def tiempo(self):
      print(f"en el año 2022 cayo un meteorito en la tierra y dejo un crater de unos cuarenta metros de diametro")
cuerpo2 = tierra(" jupiter","alpha","ceres","carpa")
cuerpo2.descripcion()
cuerpo2.tiempo()      