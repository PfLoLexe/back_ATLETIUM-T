from uuid import uuid4, UUID
from sqlmodel import SQLModel, Field



class ParentToClientLinkDefault(SQLModel):
    parent_id: UUID = Field(nullable=False)
    client_id: UUID = Field(nullable=False)

class ParentToClientLink(ParentToClientLinkDefault, table=True):
    __tablename__: str = "parent_to_client_link"
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
