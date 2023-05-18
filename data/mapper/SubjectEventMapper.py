from database.entity.SubjectEventEntity import SubjectEventEntity
from domain.model.SubjectEvent import SubjectEvent


def subject_event_to_subject_event_entity(subject_event: SubjectEvent) -> SubjectEventEntity:
    return SubjectEventEntity(
            id=subject_event.id,
            name_of_event=subject_event.name_of_event,
            date=subject_event.date,
            marks=subject_event.marks,
        )


def subject_event_entity_to_subject_event(subject_event_entity: SubjectEventEntity) -> SubjectEvent:
    return SubjectEvent(
            id=subject_event_entity.id,
            name_of_event=subject_event_entity.name_of_event,
            date=subject_event_entity.date,
            marks=subject_event_entity.marks,
        )
