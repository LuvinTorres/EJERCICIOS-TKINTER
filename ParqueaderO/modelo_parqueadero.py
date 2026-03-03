class Parqueadero:

    def __init__(self, puesto, fecha_entrada):
        self.puesto = puesto
        self.fecha_entrada = fecha_entrada
        self.hora_entrada = ""
        self.hora_salida = ""
        self.estado = "Disponible"
        self.texto_tabla = ""
        self.registros = []   # ← agregado para acumulado

    def registrar_entrada(self, usuario, carro, hora):

        if self.estado == "Ocupado":
            return "El puesto ya está ocupado"

        self.hora_entrada = hora
        self.estado = "Ocupado"

        self.registros.append({
            "usuario": usuario,
            "carro": carro,
            "hora_entrada": hora,
            "hora_salida": ""
        })

        return "Entrada registrada correctamente"

    def registrar_salida(self, hora):

        if self.estado == "Disponible":
            return "El puesto ya está libre"

        self.hora_salida = hora.strip()
        self.estado = "Disponible"

        if self.registros:
            self.registros[-1]["hora_salida"] = hora

        return "Salida registrada correctamente"

    def hay_espacio(self):
        return self.estado == "Disponible"

    def mostrar_acumulado(self):
        return len(self.registros)

    def mostrar_info(self):
        texto = ""

        for r in self.registros:
            texto += (
                r["usuario"].mostrar_info() + " | " +
                r["carro"].mostrar_info() + " | " +
                f"Entrada: {r['hora_entrada']} | "
                f"Salida: {r['hora_salida']}\n"
            )

        return texto