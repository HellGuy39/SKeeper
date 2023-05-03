from data.repository.SettingsRepository import SettingsRepository
from domain.model.Settings import Settings


class GetApplicationSettingsUseCase:

    def __init__(self, repository: SettingsRepository):
        self.__repository = repository

    def invoke(self) -> Settings:
        return self.__repository.get_settings()
