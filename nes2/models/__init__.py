"""
Convenience module for accessing nes2 models.

This module re-exports all models from nes2.core.models for easier imports.
Instead of:
    from nes2.core.models.entity import Entity, EntityType
    from nes2.core.models.base import Name, NameKind, NameParts

You can use:
    from nes2.models import Entity, EntityType, Name, NameKind, NameParts
"""

from nes2.core.models import (  # Base models; Entity models; Person models; Organization models; Location models; Relationship models; Version models
    ADMINISTRATIVE_LEVELS,
    Address,
    Attribution,
    Author,
    Candidacy,
    Contact,
    ContactType,
    Education,
    ElectoralDetails,
    Entity,
    EntityPicture,
    EntityPictureType,
    EntitySubType,
    EntityType,
    ExternalIdentifier,
    Gender,
    GovernmentBody,
    GovernmentType,
    IdentifierScheme,
    LangText,
    LangTextValue,
    Location,
    LocationType,
    Name,
    NameKind,
    NameParts,
    Organization,
    Person,
    PersonDetails,
    PoliticalParty,
    Position,
    ProvenanceMethod,
    Relationship,
    RelationshipType,
    Symbol,
    Version,
    VersionSummary,
    VersionType,
)

__all__ = [
    # Base models
    "Address",
    "Attribution",
    "Contact",
    "ContactType",
    "EntityPicture",
    "EntityPictureType",
    "LangText",
    "LangTextValue",
    "Name",
    "NameKind",
    "NameParts",
    "ProvenanceMethod",
    # Entity models
    "Entity",
    "EntitySubType",
    "EntityType",
    "ExternalIdentifier",
    "IdentifierScheme",
    # Person models
    "Person",
    "PersonDetails",
    "Gender",
    "Education",
    "Position",
    "ElectoralDetails",
    "Candidacy",
    "Symbol",
    # Organization models
    "Organization",
    "PoliticalParty",
    "GovernmentBody",
    "GovernmentType",
    # Location models
    "Location",
    "LocationType",
    "ADMINISTRATIVE_LEVELS",
    # Relationship models
    "Relationship",
    "RelationshipType",
    # Version models
    "Author",
    "Version",
    "VersionSummary",
    "VersionType",
]
