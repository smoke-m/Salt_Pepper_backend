def multiply(arr):
    """Произведение цифр в списке"""
    res = 1
    for el in arr:
        res = res * el
    return res


def multiply_numbers(inputs=None):
    """
    вернет произведение цифр, входящих в inputs.
    """

    if inputs is None:
        return None
    elif type(inputs) is str:
        arr = [int(i) for i in inputs if i.isdigit()]
    elif type(inputs) is float:
        arr = [int(i) for i in str(inputs) if i.isdigit()]
    else:
        arr = [i for i in inputs]
    return None if len(arr) == 0 else multiply(arr)
