def coincidence(arr=None, range=None):
    """
    определения элементов из массива list,
    значения которого входят в указанный диапазон range.
    """
    spisok = list()

    if arr is None or range is None:
        return spisok

    for item in arr:
        if (type(item) is int or type(item) is float) and int(item) in range:
            spisok.append(item)

    return spisok
