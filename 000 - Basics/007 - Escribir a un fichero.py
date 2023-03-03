import sys

original_stdout = sys.stdout # Guardamos la referencia a la salida original estándar para poder erstauralo después

print('Esta línea se escribirá en la pantalla')

### Con 'w' vacía el fichero y lo crea d enuevo. 
### Con 'a' añade 
with open('filename.txt', 'a') as f:
     sys.stdout = f # Cambiamos la salida estándar al fichero creado
     print('Esta línea se escribirá en el fichero')

     sys.stdout = original_stdout # Volvemos a dejar la salida estándar al valor original
    
print('Esta línea se escribirá en la pantalla')
