## Imprime del 3 al 9
for i in range(3,10):
    print(i)
    
print()

## Imprime del 1 al 10
for i in range(1,11):
    print(i)

print()

## Imprime del 1 al 50, sólo los pares
for i in range(2,51,2):
    print(i)

print()

## Imprime del 1 al 10
for i in range(1,11):
    if i<10:
        print(i,"-", sep='', end='')
    else:
        print(i)

print()

## Imprime del 1 al 10
for i in range(1,1100):
    if (i%100 != 0):
        print(i,"-", sep='', end='')
    else:
        print(i)
