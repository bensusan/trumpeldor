from django.test import TestCase
from Server.tests.DataForTests import *
from Server.tests.ServicesForTests import *


class Unit_Test_GetFeedbacks(TestCase):

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
