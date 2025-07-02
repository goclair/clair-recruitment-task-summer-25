from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

_async_engine: AsyncEngine | None = None
_AsyncSessionLocal: async_sessionmaker[AsyncSession] | None = None


def init_async_engine(
    user: str, password: str, host: str, name: str, port: int = 5432
) -> None:
    db_url = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"

    print(db_url)

    global _async_engine, _AsyncSessionLocal
    _async_engine = create_async_engine(db_url, pool_pre_ping=True)
    _AsyncSessionLocal = async_sessionmaker(
        bind=_async_engine,
        expire_on_commit=False,
        autoflush=False,
        autocommit=False,
    )


def get_async_session() -> AsyncSession:
    if not _AsyncSessionLocal:
        raise RuntimeError(
            "Async session factory not initialized. Call init_async_engine() first."
        )
    return _AsyncSessionLocal()
