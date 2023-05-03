import json

from os.path import exists
from domain.model.Settings import Settings
from presentation.ResourceManager import int_to_language_state, LanguageState


class SettingsRepository:

    SETTINGS_FILE_NAME = "settings.json"

    ARG_NAME_OF_FACILITY = "name_of_facility"
    ARG_LANGUAGE = "language"

    ACTION_READ = "r"
    ACTION_WRITE = "w"

    def __init__(self):
        if not exists(self.SETTINGS_FILE_NAME):
            self.save_settings(Settings(
                nameOfFacility="No name",
                language=LanguageState.ru
            ))

    def save_settings(self, settings: Settings):
        dict_data = {
            self.ARG_NAME_OF_FACILITY: settings.nameOfFacility,
            self.ARG_LANGUAGE: settings.language.value
        }

        json_data = json.dumps(dict_data)

        with open(self.SETTINGS_FILE_NAME, self.ACTION_WRITE) as file:
            file.write(json_data)

    def get_settings(self) -> Settings:

        with open(self.SETTINGS_FILE_NAME, self.ACTION_READ) as file:
            json_data = file.read()

        dict_data = json.loads(json_data)

        return Settings(
            nameOfFacility=dict_data[self.ARG_NAME_OF_FACILITY],
            language=int_to_language_state(dict_data[self.ARG_LANGUAGE])
        )
