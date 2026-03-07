def countSubstrings(s: str) -> int:
    count = 0

    def expand(left, right):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res

    for i in range(len(s)):
        count += expand(i, i)  # cadenas impares
        count += expand(i, i + 1)  # cadenas pares
    return count


# prueba

print(countSubstrings("aaa"))
