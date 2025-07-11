n = int(input("Introduce el número de intervalos: "))
numeros = []

i = 1
while i <= n:
    print(f"Intervalo {i}:")
    inicio = int(input("  Inicio: "))
    fin = int(input("  Fin: "))
    if inicio >= fin:
        print("  Error: El inicio debe ser menor que el fin.")
    else:
        print(f"  Intervalo válido: [{inicio}, {fin}]")
        for j in range(inicio, fin + 1):
            numeros.append(j)
            print(f"  Procesando número: {j}")
    i += 1

print("Lista de números:", numeros)