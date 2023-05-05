from data.repository.GroupRepository import GroupRepository
from domain.model.Group import Group


class RemoveGroupUseCase:

    def __init__(self, repository: GroupRepository):
        self.__repository = repository

    def invoke(self, group: Group):
        self.__repository.remove_group(group)
