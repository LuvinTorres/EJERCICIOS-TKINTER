class Calculadora:

    def __init__(self, fecha):
        self.resultado = ""
        self.fecha= fecha
        self.operacion = ""
        self.texto_tabla= ""

    
    def hacer_suma(self,num1,num2):
        self.resultado= num1+num2
        return self.resultado
    def hacer_resta(self,num1,num2):
        self.resultado= num1-num2
        return self.resultado
    def hacer_multiplicacion(self,num1,num2):
        self.resultado= num1*num2
        return self.resultado
    def hacer_division(self,num1,num2):
        self.resultado= num1/num2
        return self.resultado
    
    def hacer_operaciones(self, num1, num2):
        if self.operacion == "suma":
            return self.hacer_suma(num1.get_numero(), num2.get_numero())
        
        elif self.operacion == "resta":
            return self.hacer_resta(num1.get_numero(), num2.get_numero())
        
        elif self.operacion == "multiplicar":
            return self.hacer_multiplicacion(num1.get_numero(), num2.get_numero())
        
        elif self.operacion == "dividir":
            return self.hacer_division(num1.get_numero(), num2.get_numero())
        else:
            return "ERROR: Tipo de operacion incorrecta."
        
    def guardar_info(self, obj_usuario):
        self.texto_tabla = self.texto_tabla + f"Nombre: {obj_usuario.get_nombre()} - ID: {obj_usuario.get_id()}\n -"

    def mostrar_tabla(self):
        print(self.texto_tabla)
    
