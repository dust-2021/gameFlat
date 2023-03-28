"""
Author: li bo
date: 2023/3/22 11:38
"""
from sqlalchemy import Column, VARCHAR, CHAR, INTEGER, FLOAT, DECIMAL, DATETIME, create_engine, BigInteger
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os
from hashlib import md5

if os.path.exists('config/appConfig/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import MYSQL_CONF, APP_ADMIN_PASSWORD
else:
    from config.appConf.flaskConf import MYSQL_CONF, APP_ADMIN_PASSWORD

_Base = declarative_base()


class User(_Base):
    __tablename__ = 'User'

    user_id = Column(BigInteger, index=True)
    phone_number = Column(CHAR(14))
    email_address = Column(VARCHAR(32))
    nickname = Column(VARCHAR(32))
    user_age = Column(INTEGER)
    passwordMD5 = Column(CHAR(32))
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class UserPrivilege(_Base):
    __tablename__ = 'UserPrivilege'

    user_id = Column(BigInteger, index=True)
    privilege_level = Column(INTEGER)
    granted_by = Column(BigInteger)
    level_change_time = Column(DATETIME)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


_engine = create_engine(
    f'mysql_{MYSQL_CONF.get("mysql_engine")}:{MYSQL_CONF.get("host", "127.0.0.1")}:{MYSQL_CONF.get("port", 3306)}/{MYSQL_CONF.get("database")}')
db_session = scoped_session(sessionmaker(_engine))
_Base.metadata.creat_all()


def initial_db():
    if not db_session.query(User.user_id).filter_by(user_id=1).first():
        hasher = md5(APP_ADMIN_PASSWORD.encode('utf-8'))

        admin = User(user_id=1, nickname='admin', passwordMD5=hasher.hexdigest())
        db_session.add(admin)
        db_session.commit()
