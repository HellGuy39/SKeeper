from data.repository.JournalRepository import JournalRepository
from domain.model.SubjectEvent import SubjectEvent


class GetSubjectEventByIdUseCase:

    def __init__(self, repository: JournalRepository):
        self.__repository = repository

    def invoke(self, subject_name: str, event_id: str) -> SubjectEvent:
        return self.__repository.get_subject_event_by_id(subject_name, event_id)
