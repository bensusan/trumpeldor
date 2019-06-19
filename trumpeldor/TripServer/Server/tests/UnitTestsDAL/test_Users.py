from django.test import TestCase
from Server.tests.ServicesForTests import *
from Server.tests.DataForTests import *


class Unit_getUsers(TestCase):

    def test_getUser_NotExist(self):
        check(
            None,
            dal.getUser(UserNotExist["name"], UserNotExist["socialNetwork"]),
            self.assertEquals,
            UserSerializer
        )

    def test_getUser_Exist(self):
        check(
            UserExist,
            dal.getUser(UserExist["name"], UserExist["socialNetwork"]),
            self.assertEquals,
            UserSerializer
        )


class Unit_CreateUser(TestCase):

    def test_createUser_Validation(self):
        check(
            {"name": "Create", "socialNetwork": "Test", "lastSeen": None, "email": None},
            dal.createUser("Create", "Test"),
            self.assertEquals,
            UserSerializer
        )

    def test_createUser_Verification(self):
        self.assertEqual(dal.createUser("Create", "Test"), dal.getUser("Create", "Test"))
