from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DataBase:
    _scoped_session = None

    @property
    def session(self):
        return self._scoped_session

    def init(self, app):
        engine = create_engine(app.config['URI'])
        session_factory = sessionmaker(bind=engine, autoflush=False)

        self._scoped_session = scoped_session(session_factory, scopefunc=app.get_current_request)
