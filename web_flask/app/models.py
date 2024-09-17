"""
users
    | user_name | user_id | email | password | 
    -- one to many relation with tasks
    -- no direct relation with check
tasks
    | user_id | task_id | task_name | task_description | date_added | date_finished | evaluation | task_progress
    -- one to many relation with check
task_checks
    | user_id | task_id | to_check | is_finished | date_updated |
"""


from sqlalchemy import create_engine, Column, String, Integer, Date, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from flask_login import UserMixin
from app import login
import os


path = os.path.abspath(os.path.dirname(__file__))
engine = create_engine("sqlite:///"+path+"/tasker.db")
Session = sessionmaker(bind=engine)
base = declarative_base()

class User(UserMixin, base):
    __tablename__ = "users"

    name = Column(String)
    email = Column(String)
    password = Column(String)
    id = Column(Integer, primary_key=True, autoincrement=True)
    tasks = relationship('Tasks', back_populates='user', cascade='all, delete-orphan')
    def __repr__(self):
        return '<User:{} email:{}>'.format(self.name, self.email)

class Tasks(base):
    __tablename__ = "tasks"
    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    date_added = Column(Date)
    date_finished = Column(Date)
    evaluation = Column(Integer)
    task_progress = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='tasks')
    check = relationship('Check', back_populates='task', cascade='all, delete-orphan')

    def __repr__(self):
        return f"task: {self.name}\ndescription: {self.description}" 

class Check(base):
    __tablename__ = "checks"
    id = Column(String, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    to_check = Column(String)
    description = Column(String)
    is_finished = Column(Boolean)
    date_updated = Column(Date)
    task = relationship('Tasks', back_populates="check")

    def __repr__(self):
        return f"to check: {self.to_check}\ndescription: {self.description}" 

@login.user_loader
def load_user(id):
    s = Session()
    user = s.get(User, int(id))
    s.close()
    return user

base.metadata.create_all(engine)