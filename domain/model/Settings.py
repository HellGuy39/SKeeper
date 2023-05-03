from dataclasses import dataclass

from presentation.ResourceManager import LanguageState


@dataclass(init=True, frozen=True)
class Settings:
    nameOfFacility: str = ""
    language: LanguageState = LanguageState.ru
