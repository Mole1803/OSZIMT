import json
import os

from unittest import TestCase

# Create your tests here.

from UmfrageApp.model_queries import create_survey


class Test(TestCase):
    def test_create_survey(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_ = os.path.join(BASE_DIR, "UmfrageApp", "json_templates/create_survey.json")
        f = open(path_,"r")
        create_survey(json.load(f))

