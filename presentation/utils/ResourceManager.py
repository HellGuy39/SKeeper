from domain.state.LanguageState import LanguageState
from presentation.resource.En import resources_en
from presentation.resource.Ru import resources_ru


class ResourceManager:

    def __init__(self, language_state):
        self.__language = language_state

    def set_language(self, language_state: LanguageState):
        self.__language = language_state

    def get_localized_string(self, res_id) -> str:
        if self.__language is LanguageState.ru:
            return resources_ru[res_id.value]
        else:
            return resources_en[res_id.value]
