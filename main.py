from alternativa import Alternativa
from pregunta import Pregunta
from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from usuario import Usuario
from list_respuestas import ListaRespuestas

def main():
    # Crear un usuario
    correo = input("Ingrese el correo del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))
    region = int(input("Ingrese la región del usuario: "))
    usuario = Usuario(correo, edad, region)

    # Crear una alternativa
    contenido = input("Ingrese el contenido de la alternativa: ")
    ayuda = input("Ingrese la ayuda de la alternativa (opcional, presione Enter para omitir): ")
    alternativa = Alternativa(contenido, ayuda if ayuda else None)

    # Crear una pregunta
    enunciado = input("Ingrese el enunciado de la pregunta: ")
    ayuda_pregunta = input("Ingrese la ayuda de la pregunta (opcional, presione Enter para omitir): ")
    es_requerida = input("¿Es la pregunta requerida? (s/n): ").lower() == 's'
    pregunta = Pregunta(enunciado, ayuda_pregunta if ayuda_pregunta else None, es_requerida, [alternativa])

    # Crear una encuesta
    nombre_encuesta = input("Ingrese el nombre de la encuesta: ")
    encuesta = Encuesta(nombre_encuesta, [pregunta])

    # Usuario responde la encuesta
    print(pregunta.mostrar_pregunta())
    respuesta = int(input(f"Seleccione una alternativa (0): "))  # Solo una alternativa en este caso

    usuario.contestar_encuesta(encuesta, [respuesta])

    # Mostrar los resultados
    print("\nResultados de la encuesta:")
    print(encuesta.mostrar_encuesta())
    for listado in encuesta.listados_respuestas:
        print(listado.mostrar_listado_respuestas())

if __name__ == "__main__":
    main()