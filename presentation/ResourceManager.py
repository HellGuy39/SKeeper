import enum


class LanguageState(enum.Enum):
    ru = 1
    en = 2


class ResourceId(enum.Enum):
    back = 1


class ResourceManager:

    __resources_ru = {
        ResourceId.back.value: 'Назад',
    }

    __resources_en = {
        ResourceId.back.value: "Back",
    }

    def __init__(self):
        self.__language = LanguageState.en

    def set_language(self, language_state: LanguageState):
        self.__language = language_state

    def get_localized_string(self, id: ResourceId) -> str:
        if self.__language is LanguageState.ru:
            return self.__resources_ru[id.value]
        else:
            return self.__resources_en[id.value]
