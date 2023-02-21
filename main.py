class Asiento:

    def __init__(self):
        self.color = ""
        self.registro = 0
        self.precio = 0

    def cambiarColor(self, nuevo_color):
        if nuevo_color in [ "rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color=nuevo_color


class Motor:

    def __init__(self):
        self.numeroCilindros = 0
        self.registro = 0
        self.tipo = ""

    def cambiarRegistro(self,registro):
        if type(registro)==int:
            self.registro=registro

    def asignarTipo(self, tipo):
        if tipo in ["gasolina","electrio"]:
            self.tipo=tipo
        


class Auto:
    cantidadCreados = 0

    def __init__(self):
        self.modelo = ""
        self.precio = 0
        self.asientos = []
        self.marca = ""
        self.motor = Motor()
        self.registro = 0
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        contar=0
        for elem in self.asientos:
            if type(elem)==Asiento:
                contar += 1
        return contar

    def verificarIntegridad(self):
        msg=["Las piezas no son originales","Auto original"]
        verifica=all([i.registro==self.registro for i in self.asientos])
        verifica=verifica and self.motor.registro==self.registro
        return msg[verifica]


"""
car1=Auto()
car1=Auto()
print(Auto.cantidadCreados)
print(car1.verificarIntegridad())
car1.motor.cambiarRegistro(11)
print(car1.verificarIntegridad())
print(car1.cantidadAsientos())
car1.asientos.append(Asiento())
print(car1.cantidadAsientos())
car1.asientos[0].cambiarColor("Azul")
print(car1.asientos[0].color)
car1.asientos[0].cambiarColor("negro")
print(car1.asientos[0].color)
"""