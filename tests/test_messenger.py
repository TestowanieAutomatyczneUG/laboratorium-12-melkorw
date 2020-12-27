import unittest
from unittest.mock import *
from src.messenger.messenger import Messenger


class MessengerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = Messenger()
        self.body = {'name': 'Olek', 'desc': 'test_desc'}
        self.message = 'Message to {}, content: {}'.format(
            self.body['name'],
            self.body['desc'])

    def test_send_message_correct(self):
        self.temp.template_engine = Mock(name='template_engine')
        self.temp.template_engine.return_value = self.message
        self.temp.mail_server = Mock(name='mail_server')
        self.temp.mail_server.send_message.return_value = 'Ok'
        self.assertEqual(self.temp.send_message(self.body), 'Ok')

    def test_send_message_incorrect(self):
        self.temp.template_engine = Mock(name='template_engine')
        self.temp.template_engine.return_value = self.message
        self.temp.mail_server = Mock(name='mail_server')
        self.temp.mail_server.send_message.return_value = 'User {} does not exist'.format(
            self.body['name'])
        self.assertEqual(self.temp.send_message(self.body), 'User {} does not exist'.format(
            self.body['name']))

    def test_get_message_correct(self):
        self.temp.mail_server = Mock(name='mail_server')
        self.temp.mail_server.get_message.return_value = 'test_message'
        self.assertEqual(self.temp.get_message('test'), 'test_message')

    def test_get_message_incorrect(self):
        self.temp.mail_server = Mock(name='mail_server')
        self.temp.mail_server.get_message.return_value = 'Fatal error'
        self.assertEqual(self.temp.get_message('test'), 'Fatal error')

    def tearDown(self) -> None:
        self.temp = None
