def lengthOfLastWord(s: str) -> int:
    s = s.strip()  # Eliminar espacios al principio y al final
    if not s:  # Si la cadena está vacía después de eliminar espacios, no hay palabras
        return 0
    return len(
        s.split()[-1]
    )  # Dividir la cadena en palabras y obtener la longitud de la última palabra


# Ejemplo de uso
s = "Hello World"
print(lengthOfLastWord(s))
s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
