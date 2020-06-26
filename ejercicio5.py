import socket as s
import time
from threading import Thread

def recibir(clienteCon, clienteAddr):
    contadorPaquete = 0
    enviando = False
    while True:
        informacion = clienteCon.recv(1024)
        if not enviando:
            e = Thread(target=enviar, args=(clienteCon, clienteAddr))
            e.start()
            enviando = True
        contadorPaquete += 1
        print(f'[RCV {contadorPaquete}] Recibi un mensaje: {informacion} de {clienteAddr}')

def enviar(clienteCon, clienteAddr):
    contadorPaquete = 0
    while True:
        mensaje = f'PADTS 2020 / CINVESTAV / Python / Ejercicios 5 {contadorPaquete+1}'
        clienteCon.send(mensaje.encode())
        print(f'[SND] Paquete {contadorPaquete+1} enviado a {clienteAddr}')
        contadorPaquete += 1
        time.sleep(5)

socket = s.socket()
print('Se ha creado el socket del servidor TCP')
ip = '127.0.0.1'
puerto = 35491
socket.bind((ip, puerto))
print(f'El socket del servidor TCP esta atado a la direccion ip {ip} y el puerto {puerto}')
socket.listen()
while True:
    (clienteCon, clienteAddr) = socket.accept()
    print(f'Conexion aceptada de {clienteAddr}')
    r = Thread(target=recibir, args=(clienteCon, clienteAddr))
    r.start()
