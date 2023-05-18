from data.repository.JournalRepository import JournalRepository


class RemoveSubjectUseCase:

    def __init__(self, repository: JournalRepository):
        self.__repository = repository

    def invoke(self, subject_name: str):
        return self.__repository.remove_subject(subject_name)
