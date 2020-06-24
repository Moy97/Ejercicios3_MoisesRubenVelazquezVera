import socket as s

class ServidorUDP():
    __socket = 0
    __ip = ''
    __puerto = 0

    def __init__(self, ip, puerto):
        self.__ip = ip
        self.__puerto = puerto
        self.__socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.__socket.bind((self.__ip, self.__puerto))
        print(f'El socket del servidor esta atado a la direccion ip {self.__ip} y el puerto {self.__puerto}')

    def escribirMensaje(self, mensaje, ip, puerto):
        direccion = ip, puerto
        self.__socket.sendto(mensaje.encode(), direccion)
        print(f'Mensaje enviado: {mensaje}\n A la direccion: {direccion}')

    def leerMensaje(self):
        informacion = self.__socket.recvfrom(1024)
        return informacion

    def cerrarConexion(self):
        self.__socket.close()

if __name__ == '__main__':
    servidor = ServidorUDP('127.0.0.1', 12345)
    while True:
        informacion = servidor.leerMensaje()
        mensajeRecibido, direccion = informacion
        ip, puerto = direccion
        print(f'Mensaje recibido: {mensajeRecibido}\n Desde la direccion: {direccion}')
        if mensajeRecibido != b'':
            mensaje = 'Mensaje recibido'
            servidor.escribirMensaje(mensaje, ip, puerto)
        eleccion = input('          ¿Cerrar conexion? y/n ')
        if eleccion == 'y':
            servidor.cerrarConexion()
            break
        elif eleccion == 'n':
            pass
        else:
            print('Eleccion invalida, la conexion sigue abierta')