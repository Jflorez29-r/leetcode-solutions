def buyChoco(prices, money):
    # Ordenamos los precios
    prices.sort()

    # Tomamos los dos más baratos
    total = prices[0] + prices[1]

    # Verificamos si alcanza el dinero
    if total <= money:
        return money - total
    else:
        return money


prices = [1, 2, 2]
money = 3

# Los dos más baratos son 1 y 2 → total = 3
print(buyChoco(prices, money))  # Resultado: 0
