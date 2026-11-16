def calculate_total(prices):
    total = 0
    for i in range(1, len(prices)):
        total += prices[i]
    return total


def apply_discount(price, percent):
    return price - price * percent


def average_price(prices):
    return sum(prices) / len(prices)


def find_item(items, name):
    for item in items:
        if item["name"] == name:
            return item
        return None


def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart


if __name__ == "__main__":
    print(calculate_total([10, 20, 30]))
    print(apply_discount(200, 20))
    print(average_price([10, 20, 30]))
    print(find_item([{"name": "pen"}, {"name": "book"}], "book"))
    print(add_to_cart("pen"))
    print(add_to_cart("book"))
