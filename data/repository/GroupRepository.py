from data.mapper.GroupMapper import group_to_group_entity, group_entity_to_group
from database.dao.GroupDao import GroupDao
from database.entity.GroupEntity import GroupEntity
from domain.model.Group import Group


class GroupRepository:

    def __init__(self, dao: GroupDao):
        self.__group_dao = dao

    def insert_group(self, group: Group):
        group_entity = group_to_group_entity(group)
        self.__group_dao.insert_group(group_entity)

    def remove_group(self, group: Group):
        group_entity = group_to_group_entity(group)
        self.__group_dao.delete_group(group_entity)

    def get_all_groups(self):
        group_entities = self.__group_dao.get_groups()
        specialties = self.__map_group_entities_to_group(group_entities)
        return specialties

    @staticmethod
    def __map_group_entities_to_group(group_entities: list[GroupEntity]) -> list[Group]:
        groups = []
        for group_entity in group_entities:
            specialty = group_entity_to_group(group_entity)
            groups.append(specialty)
        return groups

