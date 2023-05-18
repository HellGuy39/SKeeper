from data.repository.JournalRepository import JournalRepository


class InsertSubjectUseCase:

    def __init__(self, repository: JournalRepository):
        self.__repository = repository

    def invoke(self, subject_name: str):
        return self.__repository.insert_subject(subject_name)
