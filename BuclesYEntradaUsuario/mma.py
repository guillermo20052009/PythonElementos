print(input("Introduce tu luchador favorito de mma: "))

edad=(int(input("Que edad tiene ese luchador: ")))

while edad > 18:
    print(edad)
    edad-=1

cadena=input("Introduce tu cadena, si quieres salir introduce una 'q': ")
while cadena != 'q':
    print(cadena)
    cadena = input("Introduce tu cadena, si quieres salir introduce una 'q': ")

luchadores=['topuria','volk','merab','topuria']

while 'topuria' in luchadores:
    luchadores.remove('topuria')

while luchadores:
    print(luchadores.pop())

