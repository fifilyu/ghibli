#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from model.init_model import DBModelBase


class Species(DBModelBase):
    __tablename__ = 'species'

    id = Column(Integer(), primary_key=True)
    film_id = Column(String(255))
    url = Column(String(255))
