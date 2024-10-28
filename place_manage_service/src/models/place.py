from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class PlaceDefault(SQLModel):
    label: str

class PLace(PlaceDefault, table=True):
    id: int = Field(default=None, primary_key=True)
