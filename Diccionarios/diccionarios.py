alien_stats={'color':'green','points':5}
print(alien_stats['color'])

alien_stats['posicion']=25

print(alien_stats)

del alien_stats['color']

print(alien_stats)

print(alien_stats.get('noexisto','no existe el valor'))

for clave,valor in alien_stats.items():
    print(clave,valor)

for clave in alien_stats.keys():
    print(clave)

for valor in alien_stats.values():
    print(valor)
for valor in set(alien_stats.values()):
    print(valor)

