import unittest
from unittest.mock import Mock, patch
from assertpy import *
from src.random_user.random_user import RandomUser
from tests.consts import mock_result, mock_results, mock_result_female


class TestRandomUserMocks(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()

    @patch('src.random_user.random_user.requests.get')
    def test_get_single_user_ok(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mock_result
        response = self.temp.get_random_user()
        assert_that(response).is_equal_to(mock_result['results'][0])

    @patch('src.random_user.random_user.requests.get')
    def test_get_single_user_is_not_ok(self, mock_get):
        mock_get.return_value.ok = False
        response = self.temp.get_random_user()
        assert_that(response).is_none()

    def test_get_random_users_mock(self):
        with patch('src.random_user.random_user.requests.get') as mock_get:
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.json.return_value = mock_results
            response = self.temp.get_random_users(2)
            assert_that(response).is_length(2)

    def test_get_random_user_of_given_gender_mock(self):
        with patch('src.random_user.random_user.requests.get') as mock_get:
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.json.return_value = mock_result_female
            response = self.temp.get_random_user_of_given_gender('female')
            assert_that(response['gender']).is_equal_to('female')
            assert_that(response['name']['first']).ends_with('a')

    def tearDown(self) -> None:
        self.temp = None

