from pregunta import Pregunta
from list_respuestas import ListaRespuestas 

# La clase Encuesta representa una encuesta que contiene múltiples preguntas y listados de respuestas.

class Encuesta:
    def __init__(self, nombre, preguntas=[]):
        self.nombre = nombre  # Nombre de la encuesta
        self.preguntas = preguntas  # Lista de preguntas de la encuesta
        self.listados_respuestas = []  # Lista de listados de respuestas, inicialmente vacío

    def modificar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre  # Modifica el nombre de la encuesta

    def mostrar_encuesta(self):
        resultado = f"Encuesta: {self.nombre}\n"
        for pregunta in self.preguntas:
            resultado += pregunta.mostrar_pregunta() + "\n"  # Muestra el nombre de la encuesta y sus preguntas
        return resultado

    def agregar_listado_respuestas(self, listado_respuestas):
        self.listados_respuestas.append(listado_respuestas)  # Agrega un listado de respuestas a la encuesta


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre, edad_minima, edad_maxima, preguntas=[]):
        super().__init__(nombre, preguntas)
        self.edad_minima = edad_minima  # Edad mínima para responder la encuesta
        self.edad_maxima = edad_maxima  # Edad máxima para responder la encuesta

    def modificar_edad_minima(self, nueva_edad_minima):
        self.edad_minima = nueva_edad_minima  # Modifica la edad mínima

    def modificar_edad_maxima(self, nueva_edad_maxima):
        self.edad_maxima = nueva_edad_maxima  # Modifica la edad máxima

    def agregar_listado_respuestas(self, listado_respuestas):
        if self.edad_minima <= listado_respuestas.usuario.edad <= self.edad_maxima:
            super().agregar_listado_respuestas(listado_respuestas)  # Agrega el listado de respuestas si la edad del usuario está dentro del rango


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre, regiones, preguntas=[]):
        super().__init__(nombre, preguntas)
        self.regiones = regiones  # Lista de regiones permitidas

    def modificar_regiones(self, nuevas_regiones):
        self.regiones = nuevas_regiones  # Modifica la lista de regiones

    def agregar_listado_respuestas(self, listado_respuestas):
        if listado_respuestas.usuario.region in self.regiones:
            super().agregar_listado_respuestas(listado_respuestas)  # Agrega el listado de respuestas si la región del usuario está permitida
