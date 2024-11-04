from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session

SQLITE_FILE_PATH = "introdex.db"

engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")


def get_db():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
