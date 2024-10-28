from sqlmodel import SQLModel, Field, Relationship

class TrainTypeDefault(SQLModel):
    label: str


class TrainType(TrainTypeDefault, table=True):
    __tablename__: str = "train_type"

    id: int = Field(default=None, primary_key=True)
