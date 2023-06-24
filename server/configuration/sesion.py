from contextvars import ContextVar
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from server.configuration.database import engine_sync

current_session: ContextVar[Optional[AsyncSession]] = ContextVar(
    "current_session", default=None
)

class OneSessionPerRequest:
    @property
    def session(self) -> AsyncSession:
        session = current_session.get()
        if session is not None:
            return session


db = OneSessionPerRequest()


async def get_session():
    return sessionmaker(
        engine_sync,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
        class_=AsyncSession,
    )


def get_session_sync(
    autoflush: bool = True, autocommit: bool = False, expire_on_commit: bool = True
):
    return sessionmaker(
        engine_sync,
        expire_on_commit=expire_on_commit,
        autocommit=autocommit,
        autoflush=autoflush,
    )