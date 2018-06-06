from aiohttp import web
from routes import setup_routes
from settings import config
import aioredis


async def init_db(app):
    conf = app['config']['redis']
    connection = await aioredis.create_connection((conf['host'], conf['port']))
    app['connection'] = connection

app = web.Application()
app.on_startup.append(init_db)
setup_routes(app)
app['config'] = config
web.run_app(app)
