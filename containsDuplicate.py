def containsDuplicate(nums: list[int]) -> bool:
    seen = set()  # Crear un conjunto para almacenar los números vistos
    for num in nums:
        if num in seen:  # Si el número ya está en el conjunto, hay un duplicado
            return True
        seen.add(num)  # Agregar el número al conjunto
    return False  # Si no se encontraron duplicados, devolver False


# Prueba
nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  # True
