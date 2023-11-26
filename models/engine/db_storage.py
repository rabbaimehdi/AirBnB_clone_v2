#!/usr/bin/python3
"""DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker



class DBStorage:
    """atabase storage engine.

    Attributes:
        __engine (Engine): SQLAlchemy engine.
        __session (Session): SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of the given class.

        If cls is None, queries all types of objects.

        Return:
            Dict of queried classes <class name>.<obj id> = obj.
        """
        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objects = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objects}

    def new(self, obj):
        """Add obj to the database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the database."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working session."""
        self.__session.close()
