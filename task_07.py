from collections import Counter


def combine_anagrams(arr):
    """
    принимает на вход массив слов
    и разбивает их в группы по анаграммам
    """
    res_arr = list()

    def _recursion(arr):
        val = arr[0]
        anag = [i for i in arr if Counter(i.lower()) == Counter(val.lower())]
        res_arr.append(anag)
        arr = list(set(arr) - set(anag))
        return res_arr if len(arr) == 0 else _recursion(arr)

    return _recursion(arr)
