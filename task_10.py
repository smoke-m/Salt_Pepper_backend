import re


def count_words(string):
    """
    Возвращает словарь со статистикой
    частоты употребления входящих в неё слов.
    """
    words_dict = dict()
    for word in re.split(r"\W+", string):
        words_dict.setdefault(word.lower(), 0)
        words_dict[word.lower()] += 1
    return words_dict
