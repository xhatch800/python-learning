def fibonacci(n, items=None):
    if items is None:
        items = [0, 1]

    if len(items) != n:
        items.append(items[len(items) - 1] + items[len(items) - 2])
        return fibonacci(n, items)
    else:
        return items


# main
howMany = 10
result = fibonacci(howMany)

print(f"Fibonacci up to {howMany} numbers: {result}")
