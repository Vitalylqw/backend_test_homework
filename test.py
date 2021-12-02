from typing import List


def series_sum(incoming: List):
    """Принимает на вход список, приводит его элементы к строкам
    и конкатенирует их.
    """
    result = ''
    for i in incoming:
        result += str(i)
    return result


print(series_sum('Привет'))
