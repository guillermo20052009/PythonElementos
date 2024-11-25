animals=['perro', 'gato', 'hamster']

for animal in animals:
    print(animal.title())

for value in range(1,11):
    print(value)

numbers=list(range(1,11))
print(numbers)

numbers=list(range(2,11,2))
print(numbers)
squares=[]

for num in numbers:
    squares.append(num*num)
print(squares)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

double=[valor*2 for valor in numbers]
print(double)

print(double[0:2])
print(double[1:2])
print(double[:2])
print(double[2:])
print(double[-2:])

for animal in animals[:1]:
    print(animal)

