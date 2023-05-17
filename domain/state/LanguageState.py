import enum


class LanguageState(enum.Enum):
    ru = 1
    en = 2


def int_to_language_state(value):
    if value == 1:
        return LanguageState.ru
    else:
        return LanguageState.en
