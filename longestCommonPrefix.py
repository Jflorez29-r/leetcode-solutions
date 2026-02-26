class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


# --- Bloque de prueba para ejecución local ---
if __name__ == "__main__":
    # 1. Crear una instancia de la clase
    solver = Solution()

    # 2. Definir casos de prueba
    test_case_1 = ["flower", "flow", "flight"]
    test_case_2 = ["dog", "racecar", "car"]

    # 3. Llamar al método e imprimir los resultados
    print(f"Caso 1: {test_case_1} -> Prefijo: '{solver.longestCommonPrefix(test_case_1)}'")  # Salida: 'fl'
    print(f"Caso 2: {test_case_2} -> Prefijo: '{solver.longestCommonPrefix(test_case_2)}'")  # Salida: ''
