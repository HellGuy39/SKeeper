from data.repository.JournalRepository import JournalRepository
from domain.model.SubjectEvent import SubjectEvent


class RemoveSubjectEventUseCase:

    def __init__(self, repository: JournalRepository):
        self.__repository = repository

    def invoke(self, subject_name: str, subject_event: SubjectEvent):
        return self.__repository.remove_subject_event(subject_name, subject_event)
