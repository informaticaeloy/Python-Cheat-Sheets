prueba = ["hola"]
print(prueba)
### Salida: ['hola']

prueba.append(["adios", "hasta luego"])
print(prueba)
### Salida: ['hola', ['adios', 'hasta luego']]

print(prueba[0][3] + prueba[0][2] + prueba[0][1] + prueba[0][0])
### Salida: aloh

'''
                                  [1][1][4] => 'a'
         [0]       [1]            |
prueba = ["hola"], ["adios", "hasta luego"]
          [0][0]    [1][0]   [1][1]
'''

prueba.insert(1, ["Elemento insertado entre el 0 y el 1","Segundo elemento de la lista", "Tercer elemento de la lista"])
print(prueba)
### Salida: ['hola', ['Elemento insertado entre el 0 y el 1', 'Segundo elemento de la lista', 'Tercer elemento de la lista'], ['adios', 'hasta luego']]
###          [0]     [1][0]                                    [1][1]                         [1][2]           |              [2][0]    [2][1]
###                                                                                                            |
###                                                                                                            |-> 'd', [1][2][16]
