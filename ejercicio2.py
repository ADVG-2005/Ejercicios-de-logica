palabra = input("Introduce una palabra: ")

letras_unicas = [letra for letra in palabra if palabra.count(letra) == 1]

max_len = 0
start = 0
seen = {}

for i, letra in enumerate(palabra):
    if letra in seen and seen[letra] >= start:
        start = seen[letra] + 1
    seen[letra] = i
    max_len = max(max_len, i - start + 1)

print("Longitud de la subcadena más larga sin caracteres repetidos:", max_len)