import json
from os.path import exists

from common.FileProvider import FileProvider
from domain.model.Settings import Settings, base_settings
from domain.state.ColorSchema import int_to_color_schema
from domain.state.LanguageState import int_to_language_state


class SettingsRepository:

    SETTINGS_FILE_NAME = "settings.json"

    ARG_NAME_OF_FACILITY = "name_of_facility"
    ARG_LANGUAGE = "language"
    ARG_USER_ID = "user_id"
    ARG_COLOR_SCHEMA = "color_schema"

    ACTION_READ = "r"
    ACTION_WRITE = "w"

    def __init__(self):
        self.__file_path = FileProvider.get_file_path(self.SETTINGS_FILE_NAME)
        if not exists(self.__file_path):
            self.save_settings(base_settings())

    def save_settings(self, settings: Settings):

        dict_data = {
            self.ARG_NAME_OF_FACILITY: settings.nameOfFacility,
            self.ARG_LANGUAGE: settings.language.value,
            self.ARG_USER_ID: settings.userId,
            self.ARG_COLOR_SCHEMA: settings.colorSchema.value
        }

        json_data = json.dumps(dict_data)

        with open(self.__file_path, self.ACTION_WRITE) as file:
            file.write(json_data)

    def get_settings(self) -> Settings:

        with open(self.__file_path, self.ACTION_READ) as file:
            json_data = file.read()

        dict_data = json.loads(json_data)

        return Settings(
            nameOfFacility=dict_data[self.ARG_NAME_OF_FACILITY],
            language=int_to_language_state(dict_data[self.ARG_LANGUAGE]),
            userId=dict_data[self.ARG_USER_ID],
            colorSchema=int_to_color_schema(dict_data[self.ARG_COLOR_SCHEMA])
        )
