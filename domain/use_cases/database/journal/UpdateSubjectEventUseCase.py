from data.repository.JournalRepository import JournalRepository


class UpdateSubjectEventUseCase:

    def __init__(self, repository: JournalRepository):
        self.__repository = repository

    def invoke(self, subject, subject_event):
        return self.__repository.update_subject_event(subject, subject_event)
