# La clase Alternativa representa una posible respuesta a una pregunta en una encuesta.

class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido  # Texto de la alternativa
        self.ayuda = ayuda  # Texto de ayuda, opcional

    def modificar_contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido  # Modifica el contenido de la alternativa

    def modificar_ayuda(self, nueva_ayuda):
        self.ayuda = nueva_ayuda  # Modifica la ayuda de la alternativa

    def mostrar_alternativa(self):
        if self.ayuda:
            return f"{self.contenido} (Ayuda: {self.ayuda})"  # Muestra el contenido y la ayuda de la alternativa
        else:
            return self.contenido  # Muestra solo el contenido de la alternativa
