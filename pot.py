# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input

# processing
def es_triangulo(a, b, c):
    # Verificamos las desigualdades triangulares
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Ejemplo de uso
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

if es_triangulo(a, b, c):
    print("Sí, los valores pueden formar un triángulo.")
else:
    print("No, los valores no pueden formar un triángulo.")

# output