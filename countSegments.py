def countSegments(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """

    nueva_cadena = s.split()
    return len(nueva_cadena)


# prueba
print(countSegments("Hello, my name is John"))
