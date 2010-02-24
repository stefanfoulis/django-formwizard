from formwizard.tests.storagetests import *
from django.test import TestCase, Client
from formwizard.storage.cookie import CookieStorage

class TestCookieStorage(TestStorage, TestCase):
    def get_storage(self):
        return CookieStorage
