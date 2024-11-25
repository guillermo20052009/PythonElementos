bicicletas=['bici1','bici2','bici3']
print(bicicletas)
print(bicicletas[0])
print(bicicletas[-1])

bicicletas[0]='bici1 cambiada'
print(bicicletas[0])
bicicletas.append('bici4 añadida')
print(bicicletas)

bicicletas.insert(0,'bici5, añadida primera')
print(bicicletas)

del bicicletas[0]
print(bicicletas)

bici_borrada=bicicletas.pop(0)
print(bicicletas)
print(bici_borrada)


bicicletas.remove('bici2')
print(bicicletas)

bicicletas.append('bici6 añadida')
bicicletas.append('bici7 añadida')
bicicletas.append('abici8 añadida')

bicicletas.sort()
print(bicicletas)

bicicletas.sort(reverse=True)
print(bicicletas)

print(sorted(bicicletas))
print(bicicletas)

bicicletas.reverse()
print(bicicletas)

print(len(bicicletas))

print(bicicletas[-1])
