import json

import platform
import os
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
        file_path = self.get_settings_file_path()
        if not exists(file_path):
            self.save_settings(Settings(
                nameOfFacility="No name",
                language=LanguageState.ru
            ))

    def save_settings(self, settings: Settings):
        file_path = self.get_settings_file_path()

        dict_data = {
            self.ARG_NAME_OF_FACILITY: settings.nameOfFacility,
            self.ARG_LANGUAGE: settings.language.value
        }

        json_data = json.dumps(dict_data)

        with open(file_path, self.ACTION_WRITE) as file:
            file.write(json_data)

    def get_settings(self) -> Settings:
        file_path = self.get_settings_file_path()

        with open(file_path, self.ACTION_READ) as file:
            json_data = file.read()

        dict_data = json.loads(json_data)

        return Settings(
            nameOfFacility=dict_data[self.ARG_NAME_OF_FACILITY],
            language=int_to_language_state(dict_data[self.ARG_LANGUAGE])
        )

    def get_settings_file_path(self):
        if platform.system() == 'Windows':
            dir = os.getenv('APPDATA')
            path = os.path.join(dir, 'SKeeper')
            os.makedirs(path, exist_ok=True)
            return os.getenv('APPDATA') + '/SKeeper/settings.json'
        else:
            return 'settings.json'
