from dataclasses import dataclass

from domain.state.ColorSchema import ColorSchema
from domain.state.LanguageState import LanguageState


@dataclass(init=True, frozen=True)
class Settings:
    nameOfFacility: str
    language: LanguageState
    userId: int
    colorSchema: ColorSchema


def base_settings() -> Settings:
    return Settings(
        nameOfFacility="No name",
        language=LanguageState.ru,
        userId=-1,
        colorSchema=ColorSchema.default
    )
