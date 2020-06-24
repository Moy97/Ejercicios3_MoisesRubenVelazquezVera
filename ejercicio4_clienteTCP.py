import socket as s

class ClienteTCP():
    __ip = ''
    __port = 0
    __socket = 0

    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        self.__socket = s.socket()
        self.__socket.connect((self.__ip, self.__port))
        print(f'Conectado al servidor {self.__ip}, en el puerto {self.__port}.')

    def escribirMensaje(self, mensaje):
        mensajeBytes = mensaje.encode()
        self.__socket.send(mensajeBytes)
        print(f'Mensaje enviado: {mensaje}')

    def leerMensaje(self):
        mensaje = self.__socket.recv(1024)
        return mensaje

if __name__ == '__main__':
    cliente = ClienteTCP('127.0.0.1', 35491)
    mensaje = 'PADTS 2020 / CINVESTAV / Python / Ejercicios 4 (TCP)'
    cliente.escribirMensaje(mensaje)
    while True:
        print(f'Respuesta del servidor: {cliente.leerMensaje()}')
        break



