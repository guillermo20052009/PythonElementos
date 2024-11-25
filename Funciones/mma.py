def saludar_usuario(*nombre):
    return f'hola {nombre}'

saludar_usuario(input('como te llamas: '))
print(saludar_usuario(input('como te llamas: ')))

usuario=input('como te llamas: ')
while usuario != 'q':
    print(saludar_usuario(usuario))
    usuario=input('como te llamas: ')

print(saludar_usuario('manu','jose'))