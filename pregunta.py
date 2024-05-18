from alternativa import Alternativa

# La clase Pregunta representa una pregunta en una encuesta, que puede tener múltiples alternativas.

class Pregunta:
    def __init__(self, enunciado, ayuda=None, es_requerida=False, alternativas=[]):
        self.enunciado = enunciado  # Texto de la pregunta
        self.ayuda = ayuda  # Texto de ayuda, opcional
        self.es_requerida = es_requerida  # Indicador de si la pregunta es requerida
        self.alternativas = alternativas  # Lista de alternativas de la pregunta

    def modificar_enunciado(self, nuevo_enunciado):
        self.enunciado = nuevo_enunciado  # Modifica el enunciado de la pregunta

    def modificar_ayuda(self, nueva_ayuda):
        self.ayuda = nueva_ayuda  # Modifica la ayuda de la pregunta

    def modificar_requerida(self, es_requerida):
        self.es_requerida = es_requerida  # Modifica si la pregunta es requerida

    def mostrar_pregunta(self):
        resultado = f"Pregunta: {self.enunciado}\n"
        if self.ayuda:
            resultado += f"Ayuda: {self.ayuda}\n"
        resultado += "Alternativas:\n"
        for alternativa in self.alternativas:
            resultado += f"- {alternativa.mostrar_alternativa()}\n"  # Muestra el enunciado, ayuda y alternativas de la pregunta
        return resultado
