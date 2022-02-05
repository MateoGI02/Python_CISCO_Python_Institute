numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

num=int(input())
while  (num!= numeroSecreto):
    num=int(input("¡Ja, ja! ¡Estás atrapado en mi ciclo!\n"))

print ("¡Bien hecho, muggle! Eres libre ahora")