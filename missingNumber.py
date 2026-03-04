def missingNumber(nums: list[int]) -> int:
    nums = set(nums)  # Convertir la lista a un conjunto para una búsqueda eficiente
    n = len(nums)  # El número total de elementos esperados es n
    for i in range(n + 1):  # Recorrer desde 0 hasta n
        if (
            i not in nums
        ):  # Si el número i no está en el conjunto, es el número faltante
            return i


# Prueba
print(missingNumber([3, 0, 1]))  # Output: 2
# complejidad: O(n) tiempo, O(n) espacio
