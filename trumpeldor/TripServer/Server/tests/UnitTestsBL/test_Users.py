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


class Unit_Test_GetUsers(TestCase):



    def test_getHints_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getHints(AttractionNotExist)

    def test_getHints_Exist_No_Hints(self):
        check(
            None,
            bl.getHints(AttractionVideo),
            self.assertEquals,
            HintSerializer,
            True
        )

    def test_getHints_Exist_With_Hints(self):
        check(
            [Hint_Text, Hint_Picture, Hint_Video],
            bl.getHints(AttractionSimple),
            self.assertCountEqual,
            HintSerializer,
            True
        )

    def test_getFeedbacks_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getFeedbackInstances(Trip_NotExist)

    def test_getFeedbacks_Exist_No_Feedbacks(self):
        check(
            None,
            bl.getFeedbackInstances(Trip_Short),
            self.assertEquals,
            FeedbackInstanceSerializer,
            True
        )

    def test_getFeedbacks_Exist_With_Feedbacks(self):
        check(
            [FeedbackInstance_Text, FeedbackInstance_Rating],
            bl.getFeedbackInstances(Trip_Empty),
            self.assertCountEqual,
            FeedbackInstanceSerializer,
            True
        )

    def test_getAmericanQuestion_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getAmericanQuestion(AttractionNotExist)

    def test_getAmericanQuestion_No_AQ(self):
        check(
            None,
            bl.getAmericanQuestion(AttractionVideo),
            self.assertEquals,
            AmericanQuestionSerializer,
            True
        )

    def test_getAmericanQuestion_With_AQ(self):
        check(
            [AQ_Simple],
            bl.getAmericanQuestion(AttractionSimple),
            self.assertCountEqual,
            AmericanQuestionSerializer,
            True
        )

    def test_getAttraction_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getAttraction(AttractionNotExist)

    def test_getAttraction_Exist(self):
        check(
            AttractionSimple,
            bl.getAttraction(AttractionSimple),
            self.assertEquals,
            AttractionSerializer
        )

    def test_getTrip_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getTrip(Trip_NotExist)

    def test_getTrip_Exist(self):
        check(
            Trip_Short,
            bl.getTrip(Trip_Short),
            self.assertEquals,
            TripSerializer
        )

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
