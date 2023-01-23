# Урок №6 Задание №3
# Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.

from itertools import groupby

def thesaurus(*args):
    if "" not in args:
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"

print(thesaurus("Нил", "Марфа", "Арсений", "Любовь", "Денис", "Никодим", "Алексей", "Дмитрий"))