from data.repository import JournalRepository
from domain.model.SubjectEvent import SubjectEvent


class InsertSubjectEventUseCase:

    def __init__(self, repository: JournalRepository):
        self.__repository = repository

    def invoke(self, subject: str, subject_event: SubjectEvent):
        return self.__repository.insert_subject_event(subject, subject_event)
