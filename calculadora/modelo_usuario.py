class Usuario:
   def __init__(self, nombre, id):
      self.nombre= nombre
      self.id =id
      
   def get_nombre(self):
      return self.nombre
   
   def set_nombre(self, nuevo_nombre):
      self.nombre=nuevo_nombre

   def get_id(self):
      return self.id
   
   def set_id(self, nuevo_id):
      self.id=nuevo_id

   def mostrar_info(self):
      print(f"Nombre= {self.nombre} - ID= {self.id}")