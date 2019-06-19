from django.test import TestCase
from Server.tests.ServicesForTests import *
from Server.tests.DataForTests import *


class Unit_getFeedbacks(TestCase):

    def test_getFeedbacks_NotExist(self):
        check(
            None,
            dal.getFeedbacks(Trip_NotExist),
            self.assertEquals,
            FeedbackInstanceSerializer,
            True
        )

    def test_getFeedbacks_Exist(self):
        check(
            [FeedbackInstance_Text, FeedbackInstance_Rating],
            dal.getFeedbacks(Trip_Empty),
            self.assertEquals,
            FeedbackInstanceSerializer,
            True
        )
