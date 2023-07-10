#!/usr/bin/python3
'''unittest module'''
import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class BaseModelTests(unittest.TestCase):
    '''Suites of Console Tests '''

    my_model = BaseModel()

    def test_base_model(self):
        '''Test attributes value of a BaseModel instance '''

        self.my_model.name = 'My First Model'
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])


