def ispalindromo(cadena: str) -> bool:
    filtro = [c.lower() for c in cadena if c.isalnum()]
    result = "".join(filtro)

    left = 0
    right = len(result) - 1

    while left < right:
        if result[left] != result[right]:
            return False
        left += 1
        right -= 1
    return True



if __name__ == "__main__":
  cadena =  "race a car"
  result =  ispalindromo(cadena)
  print(result)







