import socket as s

class ClienteUDP():
    __socket = 0

    def __init__(self):
        self.__socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

    def escribirMensaje(self, mensaje, ip, puerto):
        direccion = ip, puerto
        self.__socket.sendto(mensaje.encode(), direccion)
        print(f'Mensaje enviado: {mensaje}\n A la direccion: {direccion}')

    def leerMensaje(self):
        informacion = self.__socket.recvfrom(1024)
        return informacion

if __name__ == '__main__':
    cliente = ClienteUDP()
    mensaje = 'PADTS 2020 / CINVESTAV / Python / Ejercicios 4 (UDP)'
    cliente.escribirMensaje(mensaje, '127.0.0.1', 12345)
    while True:
        respuesta, direccion = cliente.leerMensaje()
        print(f'Respuesta del servidor: {respuesta}\n Desde la direccion: {direccion}')
        break
