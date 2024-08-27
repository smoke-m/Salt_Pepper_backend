def is_palindrome(string):
    """
    Определяет, является ли параметр string палиндромом.
    Способом isalnum().
    """
    string = "".join(el for el in str(string) if el.isalnum()).lower()
    return string == string[::-1]
