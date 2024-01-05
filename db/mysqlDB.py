import datetime

from sqlalchemy import Column, VARCHAR, CHAR, INTEGER, FLOAT, DECIMAL, DATETIME, create_engine, BigInteger, TEXT, BLOB
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os
from hashlib import md5
from etc.globalVar import AppConfig

if os.path.exists('config/appConf/flaskPersonalConf.py'):
    from config.appConf.flaskPersonalConf import *
else:
    from config.appConf.flaskConf import *

_Base = declarative_base()


class User(_Base):
    """
    user info
    """
    __tablename__ = 'User'

    user_id = Column(BigInteger, index=True)
    phone_number = Column(CHAR(14), index=True)
    email_address = Column(VARCHAR(32), index=True)
    nickname = Column(VARCHAR(32), default=None)
    user_age = Column(INTEGER)
    passwordMD5 = Column(CHAR(32))
    lock_status = Column(INTEGER)
    release_date = Column(DATETIME)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class UserPrivilege(_Base):
    """
    user permission
    """
    __tablename__ = 'UserPrivilege'

    user_id = Column(BigInteger, index=True)
    privilege_level = Column(INTEGER)
    granted_by = Column(BigInteger)
    level_change_time = Column(DATETIME)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class UserBlackList(_Base):
    """
    black list for nat
    """
    __tablename__ = 'UserBlackList'

    user_id = Column(BigInteger, index=True)
    forbidden_by_user = Column(BigInteger, index=True)
    forbid_user_privilege_level = Column(INTEGER)
    forbidden_start_time = Column(DATETIME, default=datetime.datetime.now())
    forbidden_end_time = Column(DATETIME, default=datetime.datetime.now() + datetime.timedelta(days=30))
    forbidden_level = Column(INTEGER, comment='0 means global, 1 means single space, 2 means single person')
    forbidden_global = Column(VARCHAR(16), default=None)
    forbidden_space = Column(VARCHAR(32))
    forbidden_person_user_id = Column(BigInteger)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class ApiRequestCount(_Base):
    """
    api requested count
    """
    __tablename__ = API_PROTECT_INFO_TABLE.get('minute')

    user_id = Column(BigInteger, index=True, default=None)
    ip_address = Column(CHAR(20))
    api_route = Column(VARCHAR(256))
    times = Column(INTEGER)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class ApiRequestCountHour(_Base):
    """
    api requested count
    """
    __tablename__ = API_PROTECT_INFO_TABLE.get('hour')

    user_id = Column(BigInteger, index=True, default=None)
    ip_address = Column(CHAR(20))
    api_route = Column(VARCHAR(256))
    times = Column(INTEGER)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class ApiRequestCountDay(_Base):
    """
    api requested count
    """
    __tablename__ = API_PROTECT_INFO_TABLE.get('day')

    user_id = Column(BigInteger, index=True, default=None)
    ip_address = Column(CHAR(20))
    api_route = Column(VARCHAR(256))
    times = Column(INTEGER)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class ApiRequestCountWeek(_Base):
    """
    api requested count
    """
    __tablename__ = API_PROTECT_INFO_TABLE.get('week')

    user_id = Column(BigInteger, index=True, default=None)
    ip_address = Column(CHAR(20))
    api_route = Column(VARCHAR(256))
    times = Column(INTEGER)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class DeniedIP(_Base):
    """
    IP baned
    """
    __tablename__ = 'DeniedIP'

    ip_address = Column(CHAR(20))
    # level 1 - 10, if level is 10, the level will not auto decrease
    level = Column(INTEGER)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


class SlaveMachine(_Base):
    """

    """
    __tablename__ = 'SlaveMachine'

    ip_address = Column(CHAR(20), index=True)
    key = Column(BLOB())
    # 1 slave with public IP, 2 without public IP.
    machine_type = Column(INTEGER)
    machine_name = Column(VARCHAR(32))
    connect_status = Column(INTEGER)
    add_time = Column(DATETIME)
    id = Column(BigInteger, autoincrement=True, primary_key=True)


def initial_db():
    _engine = create_engine(
        f'mysql+{MYSQL_CONF.get("mysql_engine")}://{MYSQL_CONF.get("username")}'
        f':{MYSQL_CONF.get("password")}@{MYSQL_CONF.get("host", "127.0.0.1")}:'
        f'{MYSQL_CONF.get("port", 3306)}/{MYSQL_CONF.get("database")}', pool_size=5)
    _db_session = scoped_session(sessionmaker(_engine))
    _Base.metadata.create_all(_engine)

    # initial web admin user.
    if _db_session.query(User.user_id).filter_by(user_id=1).first() is None:
        pw = APP_ADMIN_PASSWORD + AppConfig.SECRET_KEY
        hasher = md5(pw.encode('utf-8'))

        admin = User(user_id=1, nickname='admin', passwordMD5=hasher.hexdigest())
        _db_session.add(admin)
        _db_session.commit()

    if _db_session.query(UserPrivilege.user_id).filter_by(user_id=1).first() is None:
        admin = UserPrivilege(user_id=1, privilege_level=10, granted_by=1, level_change_time=datetime.datetime.now())
        _db_session.add(admin)
        _db_session.commit()

    _db_session.close()
    return _db_session


if IS_THE_MASTER_MACHINE:
    db_session = initial_db()
