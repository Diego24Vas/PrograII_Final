class Cliente:
    def __init__(self, nombre, correo_electronico):
        self.nombre = nombre
        self.correo_electronico = correo_electronico

    def __str__(self):
        return f"Cliente(nombre={self.nombre}, correo_electronico={self.correo_electronico})"