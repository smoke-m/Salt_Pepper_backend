def sort_list(arr):
    """
    Меняет местами все минимальные и максимальные элементы массива,
    а также добавляет в конец массива одно минимальное значение из него.
    """
    if len(arr) == 0:
        return arr
    min_el, max_el = min(arr), max(arr)
    for index, val in enumerate(arr):
        if val == min_el:
            arr[index] = max_el
        elif val == max_el:
            arr[index] = min_el
    arr.append(min_el)
    return arr
