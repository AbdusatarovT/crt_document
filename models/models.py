
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime

db = SQLAlchemy()


class Type(db.Model):
    """Тип документа"""
    __tablename__ = 'type'

    id = db.Column(Integer, primary_key=True)
    code = db.Column(String(128))
    name = db.Column(String(128))

    # @staticmethod
    # def create_new_type(arg1, arg2, .....):
    #     pass

    # @property
    # def create_new_type(self):
    #     pass

    # @classmethod
    # def create_new_type(cls):
    #     pass

class Customer(db.Model):
    """Пользователь"""
    __tablename__ = 'customer'

    id = db.Column(Integer, primary_key=True, unique=True)
    name = db.Column(String(128))
    surname = db.Column(String(128))
    patronymic = db.Column(String(128))
    inn = db.Column(String(14))
    birth_date = db.Column(DateTime)
    created_date = db.Column(DateTime, default=datetime.now)


class Document(db.Model):
    """Документ"""
    __tablename__ = 'document'

    id = db.Column(Integer, primary_key=True)
    doc_number = db.Column(Integer)
    customer_id = db.Column(Integer,ForeignKey(Customer.id))
    type_id = db.Column(Integer,ForeignKey(Type.id))
    date = db.Column(DateTime, default=datetime.now)

    type = db.relationship(Type, lazy='joined')
    customer = db.relationship(Customer, lazy='joined')