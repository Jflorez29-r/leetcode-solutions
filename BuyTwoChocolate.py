from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Ordenamos los precios
        prices.sort()

        # Tomamos los dos más baratos
        total = prices[0] + prices[1]

        # Verificamos si alcanza el dinero
        if total <= money:
            return money - total
        else:
            return money


if __name__ == "__main__":
    prices = [1, 2, 2]
    money = 3
    solution = Solution()
    # Los dos más baratos son 1 y 2 → total = 3
    print(solution.buyChoco(prices, money))  # Resultado: 0
