"""
Author: li bo
date: 2023/3/22 11:38
"""
from sqlalchemy import Column, VARCHAR, CHAR, INTEGER, FLOAT, DECIMAL, DATETIME, create_engine, BigInteger
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os
from hashlib import md5
import logging

if os.path.exists('config/appConf/flaskPersonalConf.py'):
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
    lock_status = Column(INTEGER)
    release_date = Column(DATETIME)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class UserPrivilege(_Base):
    __tablename__ = 'UserPrivilege'

    user_id = Column(BigInteger, index=True)
    privilege_level = Column(INTEGER)
    granted_by = Column(BigInteger)
    level_change_time = Column(DATETIME)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class ApiRequestCount(_Base):
    __tablename__ = 'ApiRequestCount'

    user_id = Column(BigInteger, index=True, default=None)
    ip_address = Column(CHAR(20))
    api_route = Column(VARCHAR(256))
    times = Column(INTEGER)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


_engine = create_engine(
    f'mysql+{MYSQL_CONF.get("mysql_engine")}://{MYSQL_CONF.get("username")}'
    f':{MYSQL_CONF.get("password")}@{MYSQL_CONF.get("host", "127.0.0.1")}:'
    f'{MYSQL_CONF.get("port", 3306)}/{MYSQL_CONF.get("database")}', pool_size=5)
db_session = scoped_session(sessionmaker(_engine))
_Base.metadata.create_all(_engine)


def initial_db():
    # 初始管理员账号
    if not db_session.query(User.user_id).filter_by(user_id=1).first():
        hasher = md5(APP_ADMIN_PASSWORD.encode('utf-8'))

        admin = User(user_id=1, nickname='admin', passwordMD5=hasher.hexdigest())
        db_session.add(admin)
        db_session.commit()
        db_session.close()


initial_db()
