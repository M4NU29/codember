# Un grupo de espías ha descubierto que su sistema de cifrado de mensajes está comprometido.

# Han encontrado algunas contraseñas que no cumplen con la Política de Seguridad de Cifrado que tenían establecida cuando fueron creadas.

# Para solucionar el problema, han creado una lista (tu entrada al desafío) de contraseñas (según la base de datos corrupta) y la política de seguridad cuando esa clave fue establecida.

# Ejemplo de la lista:

# 2-4 f: fgff
# 4-6 z: zzzsg
# 1-6 h: hhhhhh
# Cada línea indica, separado por :, la política de la clave y la clave misma.

# La política de la clave especifica el número mínimo y máximo de veces que un carácter dado debe aparecer para que la clave sea válida. Por ejemplo, 2-4 f significa que la clave debe contener f al menos 2 veces y como máximo 4 veces.

# Sabiendo esto, en el ejemplo anterior, hay 2 claves válidas:

# La segunda clave, zzzsg, no lo es; contiene 3 veces la letra z, pero necesita al menos 4. Las primeras y terceras claves son válidas: contienen la cantidad adecuada de f y h, respectivamente, según sus políticas.

# Función para evaluar contraseñas basado en los parámetros establecidos
def evaluate_password(password):
  array_password = password.split(":")
  parameters = array_password[0]
  key = array_password[1]

  # Obtener los valores mínimo y máximo de la política de la contraseña
  minimum = int(parameters[:parameters.index("-")])
  maximum = int(parameters[(parameters.index("-")+1):parameters.index(" ")])

  # Verificar si el número de ocurrencias de la letra clave está dentro del rango especificado
  if key.count(parameters[-1]) <= minimum and key.count(parameters[-1]) >= maximum:
    return False
    
  return False

valid_keys = []
invalid_keys = []

with open("CHALLENGE_03/keys.txt", "r") as keys:
  for key in keys:
    if evaluate_password(key):
      valid_keys.append(key.strip())
    else:
      invalid_keys.append(key.strip())

print("Claves válidas:")
for i, key in enumerate(valid_keys, 1):
  print(f"{i}. {key}")

print("\nClaves inválidas:")
for i, key in enumerate(invalid_keys, 1):
  print(f"{i}. {key}")