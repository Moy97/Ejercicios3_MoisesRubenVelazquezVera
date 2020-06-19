class Figura():
    _base = 0
    _altura = 0

    def __init__(self, base, altura):
        self._base = base
        self._altura = altura


class Rectangulo(Figura):

    def __init__(self, _base, _altura):
        super().__init__(_base, _altura)
        pass

    def obtenerArea(self):
        return (self._base * self._altura)

    def obtenerPerimetro(self):
        return ((self._base+self._altura)*2)


class Triangulo(Figura):

    def __init__(self, _base, _altura):
        super().__init__(_base, _base)
        pass

    def obtenerArea(self):
        return ((self._base * self._altura)/2)

    def obtenerPerimetro(self):
        return (self._base*3)



class Estudiante:
    _nombre = ''
    _correoElectronico = ''
    _contraseña = ''

    def __init__(self, nombre, correoElectronico, contraseña):
        self._nombre = nombre
        _correoElectronico = correoElectronico
        _contraseña = contraseña

    def ingresarAtributos(self):
        self._nombre = input("Introducir nombre: ")
        self._correoElectronico = input("Introducir correo: ")
        self._contraseña = input("Introducir contraseña: ")

    def obtenerAtributos(self):
        return (self._nombre, self._correoElectronico, self._contraseña)


if __name__ == '__main__':
    pass

    triangulo = Triangulo(3, 3)
    trianguloArea = triangulo.obtenerArea()
    print('El area del triangulo es: ' + str(trianguloArea))
    trianguloPerimetro = triangulo.obtenerPerimetro()
    print('El perímetro del triangulo es: ' + str(trianguloPerimetro))

    rectangulo = Rectangulo(3, 5)
    rectanguloArea = rectangulo.obtenerArea()
    print('El area del rectangulo es ' + str(rectanguloArea))
    rectanguloPerimetro = rectangulo.obtenerPerimetro()
    print('El perímetro del rectangulo es: ' + str(rectanguloPerimetro))

    nombre = ''
    correo = ''
    contraseña = ''
    alumno = Estudiante(nombre, correo, contraseña)
    alumno.ingresarAtributos()
    print (alumno.obtenerAtributos())


