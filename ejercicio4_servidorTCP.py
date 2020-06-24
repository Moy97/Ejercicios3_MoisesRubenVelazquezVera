import socket as s

class ServidorTCP():
    __ip = ''
    __puerto = 0
    __contador = 0
    __socket = 0
    __conexionCliente = 0
    __direccionCliente = 0

    def __init__(self, ip, puerto):
        self.__ip = ip
        self.__puerto = puerto
        self.__contador = 0
        self.__socket = s.socket()
        self.__socket.bind((self.__ip, self.__puerto))
        print(f'El socket del servidor esta atado a la direccion ip {self.__ip} y el puerto {self.__puerto}')
        self.__socket.listen()
        while True:
            if self.__contador < 10:
                (self.__conexionCliente, self.__direccionCliente) = self.__socket.accept()
            else:
                continue
            self.__contador += 1
            print(f'Conexion {self.__contador} aceptada de {self.__direccionCliente}')
            break

    def escribirMensaje(self, mensaje):
        mensajeBytes = mensaje.encode()
        self.__conexionCliente.send(mensajeBytes)

    def leerMensaje(self):
        mensaje = self.__conexionCliente.recv(1024)
        return mensaje

    def cerrarConexion(self):
        self.__socket.close()

if __name__ == '__main__':
    eleccion = ''
    while True:
        if eleccion != 'y':
            servidor = ServidorTCP('127.0.0.1', 35491)
            while True:
                mensajeRecibido = servidor.leerMensaje()
                if mensajeRecibido != b'':
                    print(f'Mensaje recibido: {mensajeRecibido}')
                    mensaje = 'Mensaje recibido'
                    servidor.escribirMensaje(mensaje)
                    eleccion = input('          ¿Cerrar conexion? y/n ')
                    if eleccion == 'y':
                        servidor.cerrarConexion()
                        break
                    elif eleccion == 'n':
                        del servidor
                        break
                    else:
                        print('Eleccion invalida, la conexion sigue abierta')
                        del servidor
                        break
        else:
            break