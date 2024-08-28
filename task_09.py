def connect_dicts(dict1, dict2):
    """
    Соединит два переданных словаря,
    значениями ключей в которых являются числа,
    и вернет новый словарь.
    """
    res_dict = dict()
    if sum(dict2.values()) >= sum(dict1.values()):
        pr_dict, lo_dict = dict2, dict1
    else:
        pr_dict, lo_dict = dict1, dict2
    for i in pr_dict:
        if i in lo_dict and pr_dict[i] >= 10:
            res_dict[i] = pr_dict[i]
            del lo_dict[i]
        elif pr_dict[i] >= 10:
            res_dict[i] = pr_dict[i]
    for key, value in lo_dict.items():
        if value >= 10:
            res_dict[key] = value
    return {
        k: v for k, v in sorted(res_dict.items(), key=lambda item: item[1])
    }
