# En el mundo del espionaje, se utiliza un lenguaje de codificación con símbolos que realizan operaciones matemáticas simples.

# Tu tarea es crear un mini compilador que interprete y ejecute programas escritos en este lenguaje de símbolos.

# Las operaciones del lenguaje son las siguientes:

# '#' Incrementa el valor numérico en 1.
# '@' Decrementa el valor numérico en 1.
# '*' Multiplica el valor numérico por sí mismo.
# '&' Imprime el valor numérico actual.
# El valor numérico inicial es 0 y las operaciones deben aplicarse en el orden en que aparecen en la cadena de símbolos.

symbols: str = input('Digite los símbolos: ')
total: int = 0

for symbol in symbols:
  match symbol:
    case '#':
      total += 1
    case '@':
      total -= 1
    case '*':
      total *= total
    case '&':
      print(total, end='')