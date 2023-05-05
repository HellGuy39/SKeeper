from database.entity.SpecialtyEntity import SpecialtyEntity
from domain.model.Specialty import Specialty


def specialty_to_specialty_entity(specialty: Specialty) -> SpecialtyEntity:
    return SpecialtyEntity(
            id=specialty.id,
            name=specialty.name
        )


def specialty_entity_to_specialty(specialtyEntity: SpecialtyEntity) -> Specialty:
    return Specialty(
            id=specialtyEntity.id,
            name=specialtyEntity.name
        )
