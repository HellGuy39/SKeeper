from database.entity.GroupEntity import GroupEntity
from domain.model.Group import Group


def group_to_group_entity(group: Group) -> GroupEntity:
    return GroupEntity(
            id=group.id,
            name=group.name
        )


def group_entity_to_group(groupEntity: GroupEntity) -> Group:
    return Group(
            id=groupEntity.id,
            name=groupEntity.name
        )
