def countSegments(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """

    nueva_cadena = s.split() # covertir la cadena en una lista de cadenas, elimana espacios
    return len(nueva_cadena) # devolver la cantidad de segmentos


# prueba
print(countSegments("Hello, my name is John")) # 5
