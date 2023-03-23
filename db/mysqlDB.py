"""
Author: li bo
date: 2023/3/22 11:38
"""
from sqlalchemy import Column, VARCHAR, CHAR, INTEGER, FLOAT, DECIMAL, DATETIME, create_engine, BigInteger
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

_Base = declarative_base()


class User(_Base):
    __tablename__ = ''

    user_id = Column(BigInteger, index=True)
    phone_number = Column(CHAR(14))
    email_address = Column(VARCHAR(32))
    nickname = Column(VARCHAR(32))
    user_age = Column()
    passwordMD5 = Column(CHAR(32))
    id = Column(BigInteger, autoincrement=True, primary_key=True)


_Base.metadata.creat_all()
