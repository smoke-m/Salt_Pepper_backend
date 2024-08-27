def max_odd(arr):
    """
    Определяет максимальный нечетный элемент.
    """
    odd_numbers = [
        i for i in arr if (type(i) is int or type(i) is float) and i % 2 != 0
    ]
    return max(odd_numbers) if len(odd_numbers) != 0 else None
