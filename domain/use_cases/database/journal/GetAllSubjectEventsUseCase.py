from data.repository import JournalRepository
from domain.model.SubjectEvent import SubjectEvent


class GetAllSubjectEventsUseCase:

    def __init__(self, repository: JournalRepository):
        self.__repository = repository

    def invoke(self, subject_name: str) -> list[SubjectEvent]:
        return self.__repository.get_all_subject_events(subject_name)
