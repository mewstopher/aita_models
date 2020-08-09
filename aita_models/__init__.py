from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    username = Column('username', Text)
    dt_updated = Column('dt_updated', DateTime, server_default=func.now())


class Submission(Base):
    __tablename__ = 'submission'
    id = Column('id', Integer, primary_key=True)
    created = Column('created', DateTime)
    title = Column('title', Text)
    user_id = Column('user_id', Integer, ForeignKey(User.id))
    dt_updated = Column('dt_updated', DateTime, server_default=func.now())


class Vote(Base):
    __tablename__ = 'vote'
    id = Column('id', Integer, primary_key=True)
    code = Column('code', Text)
    description = Column('type', Text)
    dt_updated = Column('dt_updated', DateTime, server_default=func.now())


class SubmissionContent(Base):
    __tablename__ = 'submission_content'
    id = Column('id', Integer, primary_key=True)
    submission_id = Column('submission_id', Integer, ForeignKey(Submission.id))
    body = Column('body', Text)
    vote_id = Column('vote_id', Integer, ForeignKey(Vote.id))
    upvotes = Column('upvotes', Integer)
    dt_updated = Column('dt_updated', DateTime, server_default=func.now())


class Comments(Base):
    __tablename__ = 'comments'
    id = Column('id', Integer, primary_key=True)
    time_submitted = Column('time_submitted', DateTime)
    comment_upvotes = Column('comment_upvotes', Integer)
    user_id = Column('user_id', Integer, ForeignKey(User.id))
    submission_id = Column('submission_id', Integer, ForeignKey(Submission.id))
    dt_updated = Column('dt_updated', DateTime, server_default=func.now())


class CommentContent(Base):
    __tablename__ = 'comment_content'
    id = Column('id', Integer, primary_key=True)
    comments_id = Column('comments_id', Integer, ForeignKey(Comments.id))
    body = Column('body', Text)
    dt_updated = Column('dt_updated', DateTime, server_default=func.now())
