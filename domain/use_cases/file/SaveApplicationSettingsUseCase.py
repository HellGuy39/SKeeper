from data.repository.SettingsRepository import SettingsRepository
from domain.model.Settings import Settings


class SaveApplicationSettingsUseCase:

    def __init__(self, repository: SettingsRepository):
        self.__repository = repository

    def invoke(self, settings: Settings):
        self.__repository.save_settings(settings)
