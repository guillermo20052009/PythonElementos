coches=['BMW','Mercedes','Audi']
coches_2=['BMW']
lista_vacia=[]

for coche in coches:
    if coche == 'Mercedes':
        print(coche=='Mercedes')
    else:
        print('Otro tipo')

if 'BMW' in coches:
    print("real")

if 'noestoy' not in coches:
    print("real")
elif 'Tampocoestoy' in coches:
    print('probando las sentencias')
else:
    print("noestoy")


if lista_vacia:
    print(lista_vacia[0])
else:
    print("vacio")


for coche in coches:
    if coche in coches_2:
        print(coche)
    else:
        print('no')

