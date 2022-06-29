from asyncpgsa import pg
from settings.config import CONFIG


async def init_connection():
    return await pg.init(
        database=CONFIG.database.database,
        user=CONFIG.database.user,
        password=CONFIG.database.password,
        host=CONFIG.database.host,
        port=CONFIG.database.port,
        min_size=2,
        max_size=5
    )


async def get_pg_connection(app) -> None:
    app['connection'] = await init_connection()


async def close_pg_connection(app):
    await app['connection'].close()
