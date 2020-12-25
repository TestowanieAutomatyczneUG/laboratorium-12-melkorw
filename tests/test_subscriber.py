from unittest.mock import patch, Mock
import unittest
from src.subscriber.subscriber import Subscriber
from assertpy import *


class SubscriberTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = Subscriber()
        self.person = {'name': 'Olek', 'email': 'olo@wp.pl'}

    def test_email_sending(self):
        with patch("smtplib.SMTP") as smtp:
            from_address = "from@domain.com"
            to_address = ["to@domain.com"]
            msg = self.temp.build_email(
                from_address, to_address, "subject", "message")
            self.temp.send_email(msg)
            instance = smtp.return_value
            self.assertTrue(instance.sendmail.called)
            self.assertEqual(instance.sendmail.call_count, 1)

    @patch('src.subscriber.subscriber.requests.post')
    def test_add_person_ok(self, mock_post):
        mock_post.return_value = Mock(status_code=201)
        mock_post.return_value.json.return_value = "Added"
        response = self.temp.add_person({})
        assert_that(response).is_equal_to("Added")

    @patch('src.subscriber.subscriber.requests.post')
    def test_add_person_existing_already(self, mock_post):
        mock_post.return_value = Mock(status_code=409)
        response = self.temp.add_person({})
        assert_that(response).is_equal_to('Person already exists')

    @patch('src.subscriber.subscriber.requests.post')
    def test_add_person_something_wrong(self, mock_post):
        mock_post.return_value = Mock(status_code=400)
        response = self.temp.add_person({})
        assert_that(response).is_equal_to('Something went horribly wrong')

    @patch('src.subscriber.subscriber.requests.delete')
    def test_delete_person_ok(self, mock_delete):
        mock_delete.return_value = Mock(status_code=200)
        mock_delete.return_value.json.return_value = "Deleted"
        response = self.temp.delete_person({})
        assert_that(response).is_equal_to("Deleted")

    @patch('src.subscriber.subscriber.requests.delete')
    def test_delete_person_not_existing(self, mock_delete):
        mock_delete.return_value = Mock(status_code=404)
        response = self.temp.delete_person({})
        assert_that(response).is_equal_to('Person does not exists')

    @patch('src.subscriber.subscriber.requests.delete')
    def test_delete_person_something_wrong(self, mock_post):
        mock_post.return_value = Mock(status_code=400)
        response = self.temp.delete_person(0)
        assert_that(response).is_equal_to('Something went horribly wrong')


