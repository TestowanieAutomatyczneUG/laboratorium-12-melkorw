import unittest
from assertpy import *
from src.random_user.random_user import RandomUser


class TestRandomUserOne(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    def test_get_single_user(self):
        result = self.temp.get_random_user()
        assert_that(result).contains('gender', 'registered')

    def test_get_random_users(self):
        result = self.temp.get_random_users(2)
        assert_that(result).is_length(2)

    def test_get_random_user_of_given_gender(self):
        result = self.temp.get_random_user_of_given_gender('female')
        assert_that(result['gender']).is_equal_to('female')

    def test_get_random_user_of_given_gender_error(self):
        assert_that(self.temp.get_random_user_of_given_gender).raises(
            ValueError).when_called_with('something')

    def tearDown(self) -> None:
        self.temp = None
