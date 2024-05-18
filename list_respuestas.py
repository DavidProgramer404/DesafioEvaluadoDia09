# La clase ListadoRespuestas representa un conjunto de respuestas asociadas a un usuario en una encuesta.

class ListaRespuestas:
    def __init__(self, usuario, respuestas):
        self.usuario = usuario  # Usuario que generó el listado de respuestas
        self.respuestas = respuestas  # Lista de respuestas

    def mostrar_listado_respuestas(self):
        return f"Usuario: {self.usuario.correo}, Respuestas: {self.respuestas}"  # Muestra el listado de respuestas con el usuario
