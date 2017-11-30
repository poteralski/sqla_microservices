from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

metadata = MetaData()


class DataBase:
    _scoped_session = None
    Model = declarative_base(metadata=metadata)

    @property
    def session(self):
        return self._scoped_session

    def init(self, app):
        engine = create_engine(app.config['URI'])
        session_factory = sessionmaker(bind=engine, autoflush=False)

        self._scoped_session = scoped_session(session_factory, scopefunc=app.get_current_request)

        self.Model.metadata.bind = engine
