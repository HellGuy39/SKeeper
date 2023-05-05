from data.repository.GroupRepository import GroupRepository
from domain.model.Group import Group


class GetAllGroupsUseCase:

    def __init__(self, repository: GroupRepository):
        self.__repository = repository

    def invoke(self) -> list[Group]:
        return self.__repository.get_all_groups()