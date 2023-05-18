from database.JournalDatabase import JournalDatabase
from database.entity.SubjectEventEntity import SUBJECT_EVENT_SCHEMA, SubjectEventEntity


class JournalDao:

    def __init__(self, database: JournalDatabase):
        self.__database = database

    def get_all_subjects(self) -> list[str]:
        self.__database.cursor.execute(
            f"""
            SELECT * FROM sqlite_master WHERE type = 'table'
            """
        )
        tables = self.__database.cursor.fetchall()
        subjects = []
        for row in tables:
            subjects.append(row[1])
        return subjects

    def insert_subject(self, subject_name: str):
        self.__database.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {subject_name} {SUBJECT_EVENT_SCHEMA}
            """
        )
        self.__database.connection.commit()

    def remove_subject(self, subject_name: str):
        self.__database.cursor.execute(
            f"""
            DROP TABLE IF EXISTS {subject_name}
            """
        )
        self.__database.connection.commit()

    def remove_subject_event(self, subject_name: str, event_id: int):
        self.__database.cursor.execute(
            f"""
            DELETE FROM {subject_name} WHERE `id` = ?
            """,
            (event_id,)
        )
        self.__database.connection.commit()

    def get_all_subject_events(self, subject_name: str):
        self.__database.cursor.execute(
            f"""
            SELECT * FROM {subject_name}
            """
        )
        table_rows = self.__database.cursor.fetchall()
        events = []
        for row in table_rows:
            events.append(self.__table_row_to_subject_event_entity(row))
        return events

    def insert_subject_event(self, subject: str, subject_event_entity: SubjectEventEntity):
        self.__database.cursor.execute(
            f"""
            INSERT INTO {subject} 
            (`name_of_event`, `date`, `marks`) 
            VALUES (?, ?, ?)
            """,
            (subject_event_entity.name_of_event, subject_event_entity.date, subject_event_entity.marks,)
        )
        self.__database.connection.commit()

    def get_subject_event_by_id(self, subject_name: str, event_id: int) -> list[SubjectEventEntity]:
        self.__database.cursor.execute(
            f"""
            SELECT * FROM {subject_name} WHERE `id` = ? 
            """,
            (event_id,)
        )
        table_rows = self.__database.cursor.fetchall()
        events = []
        for row in table_rows:
            events.append(self.__table_row_to_subject_event_entity(row))
        return events

    def update_subject_event(self, subject: str, subject_event_entity: SubjectEventEntity):
        self.__database.cursor.execute(
            f"""
            UPDATE {subject} 
            set `name_of_event` = ?, `date` = ?, `marks` = ? 
            WHERE `id` = ? 
            """,
            (subject_event_entity.name_of_event, subject_event_entity.date,
             subject_event_entity.marks, subject_event_entity.id)
        )

    @staticmethod
    def __table_row_to_subject_event_entity(row):
        return SubjectEventEntity(
            id=row[0],
            name_of_event=row[1],
            date=row[2],
            marks=row[3]
        )
