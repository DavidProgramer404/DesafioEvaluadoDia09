from list_respuestas import ListaRespuestas
from encuesta import Encuesta

# La clase Usuario representa un usuario del sistema, con sus datos y métodos para interactuar con encuestas.

class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo  # Correo del usuario
        self.edad = edad  # Edad del usuario
        self.region = region  # Región del usuario

    def modificar_correo(self, nuevo_correo):
        self.correo = nuevo_correo  # Modifica el correo del usuario

    def modificar_edad(self, nueva_edad):
        self.edad = nueva_edad  # Modifica la edad del usuario

    def modificar_region(self, nueva_region):
        self.region = nueva_region  # Modifica la región del usuario

    def contestar_encuesta(self, encuesta, respuestas):
        listado_respuestas = ListaRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(listado_respuestas)  # Permite al usuario contestar una encuesta