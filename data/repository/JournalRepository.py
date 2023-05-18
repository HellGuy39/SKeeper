from data.mapper.SubjectEventMapper import subject_event_to_subject_event_entity, subject_event_entity_to_subject_event
from database.dao.JournalDao import JournalDao
from domain.model.SubjectEvent import SubjectEvent


class JournalRepository:

    def __init__(self, dao: JournalDao):
        self.__journal_dao = dao

    def insert_subject_event(self, subject: str, subject_event: SubjectEvent):
        subject_event_entity = subject_event_to_subject_event_entity(subject_event)
        self.__journal_dao.insert_subject_event(subject, subject_event_entity)

    def insert_subject(self, subject_name: str):
        self.__journal_dao.insert_subject(subject_name)

    def remove_subject(self, subject_name: str):
        self.__journal_dao.remove_subject(subject_name)

    def remove_subject_event(self, subject_name: str, subject_event: SubjectEvent):
        subject_event_entity = subject_event_to_subject_event_entity(subject_event)
        self.__journal_dao.remove_subject_event(subject_name, subject_event_entity.id)

    def get_all_subjects(self) -> list[str]:
        return self.__journal_dao.get_all_subjects()

    def get_all_subject_events(self, subject_name: str) -> list[SubjectEvent]:
        subject_event_entities = self.__journal_dao.get_all_subject_events(subject_name)
        subject_events = self.subject_event_entities_to_subject_event(subject_event_entities)
        return subject_events

    def get_subject_event_by_id(self, subject_name, event_id) -> SubjectEvent:
        subject_event_entities = self.__journal_dao.get_subject_event_by_id(subject_name, event_id)
        subject_events = self.subject_event_entities_to_subject_event(subject_event_entities)
        return subject_events[0]

    def update_subject_event(self, subject, subject_event: SubjectEvent):
        subject_event_entity = subject_event_to_subject_event_entity(subject_event)
        self.__journal_dao.update_subject_event(subject, subject_event_entity)

    @staticmethod
    def subject_event_entities_to_subject_event(subject_event_entities):
        subject_events = []
        for subject_event_entity in subject_event_entities:
            subject_event = subject_event_entity_to_subject_event(subject_event_entity)
            subject_events.append(subject_event)
        return subject_events
