from data.repository import JournalRepository


class GetAllSubjectsUseCase:

    def __init__(self, repository: JournalRepository):
        self.__repository = repository

    def invoke(self) -> list[str]:
        return self.__repository.get_all_subjects()
