from sqlmodel import Field, SQLModel, create_engine, Session, select

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    full_name: str
    disabled: bool