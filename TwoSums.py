def twoSum(nums: list[int], target: int) -> list[int]:
    vistos = {}  # Diccionario para almacenar los números vistos y sus índices
    for i, num in enumerate(nums):  # Iteramos sobre la lista de números con sus índices
        complemento = (
            target - num
        )  # Calculamos el complemento que necesitamos para alcanzar el target
        if complemento in vistos:
            return [
                vistos[complemento],
                i,
            ]  # Si el complemento ya ha sido visto, devolvemos los índices correspondientes
        vistos[num] = (
            i  # Si el número actual no ha sido visto, lo agregamos al diccionario con su índice
        )


# Ejemplo de uso
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]
