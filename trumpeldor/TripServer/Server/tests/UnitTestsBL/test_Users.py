from django.test import TestCase
from Server.tests.DataForTests import *
from Server.tests.ServicesForTests import *


class Unit_Test_InsertAndRetrieveUsers(TestCase):
    user = addUserJson(UserExist)

    def test_getUser_NotExist(self):
        check(
            None,
            bl.getUser(UserNotExist),
            self.assertEquals,
            UserSerializer
        )

    def test_getUser_Exist(self):
        check(
            self.user,
            bl.getUser(UserExist),
            self.assertEquals,
            UserSerializer
        )

    def test_createUser_Exist(self):
        with self.assertRaises(RuntimeError):
            bl.createUser(UserExist)

    def test_createUser_NotExist(self):
        check(
            UserNew,
            bl.createUser(UserNew),
            self.assertEquals,
            UserSerializer
        )


class Unit_Test_SignUp(TestCase):

    def test_signUp_NotExistedUser(self):
        actual = bl.signUp(UserNew)
        check(
            UserNew,
            actual,
            self.assertEquals,
            UserSerializer
        )
        check(
            None,
            actual["lastSeen"],
            self.assertEquals
        )

    def test_signUp_ExistedUser(self):
        actual = bl.signUp(UserExist)
        check(
            UserExist,
            actual,
            self.assertEquals,
            UserSerializer
        )
        check(
            None,
            actual["lastSeen"],
            self.assertNotEquals
        )
