from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

URI = 'sqlite:///scoped_session.db'

engine = create_engine(URI)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

s1 = Session()
s2 = Session()

Session.remove()

s3 = Session()

print(s1 == s2)
print(s1 == s3)
print(s2 == s3)
