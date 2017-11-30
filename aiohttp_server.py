from apps.aiohttp.extensions import db
from apps.aiohttp.middlewares import sqla_middleware
from apps.aiohttp.serwer import App, Handler1, Handler2
from aiohttp.web import run_app

app = App()
app.config['URI'] = 'sqlite:///async.db'

db.init(app)
db.Model.metadata.drop_all()
db.Model.metadata.create_all()
app.router.add_route('*', '/1/', Handler1)
app.router.add_route('*', '/2/', Handler2)


app.middlewares.append(sqla_middleware)

run_app(app)
