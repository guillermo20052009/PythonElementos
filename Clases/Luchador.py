class Luchador:
    def __init__(self,nombre,edad,peso,estilo,posicion):
        self.nombre=nombre
        self.edad=edad
        self.peso=peso
        self.estilo=estilo
        self.posicion=posicion

    def perder(self,decremento):
        self.posicion-=decremento

    def ganar(self,incremento):
        self.posicion+=incremento

    def cambio_categoria(self,peso):
        self.peso=peso

    def imprimir(self):
        print(self.nombre,self.edad,self.peso,self.estilo,self.posicion)

class guantes:
    def __init__(self,marca,oz):
        self.marca=marca
        self.oz=oz
    def imprimir(self):
        return f'{self.marca} {self.oz}'

class Boxeador(Luchador):
    def __init__(self,nombre,edad,peso,estilo,posicion,guantes):
        super().__init__(nombre,edad,peso,estilo,posicion)
        self.guantes=guantes

    def imprimir(self):
        print(self.nombre,self.edad,self.peso,self.estilo,self.posicion,self.guantes.imprimir())

    def marca_guantes(self):
        print(self.guantes)

luchador1=Luchador("Topuria",28,66,'completo',1)

luchador1.imprimir()

luchador1.cambio_categoria(70)

luchador1.imprimir()
guantes1= guantes('charlie',10)

boxeador1=Boxeador("Mateus",28,66,'completo',1,guantes1)
boxeador1.imprimir()