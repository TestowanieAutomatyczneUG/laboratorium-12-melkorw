import requests
from mailer import Message
import smtplib


class Subscriber:
    def add_person(self, body):
        response = requests.post('not_specified', data=body)
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        elif response.status_code == 409:
            return 'Person already exists'
        return 'Something went horribly wrong'

    def delete_person(self, person_id):
        response = requests.delete('not_specified_{}'.format(person_id))
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return 'Person does not exists'
        return 'Something went horribly wrong'

    def build_email(self, from_address, to_address, subject, content):
        message = Message()
        message.From = from_address
        message.To = to_address
        message.Subject = subject
        message.Body = content
        return message

    def send_email(self, msg, host='', port=0):
        s = smtplib.SMTP(host, port, local_hostname="smtp.mydomain.com")
        result = s.sendmail(msg.From, msg.To, msg.as_string())
        s.quit()
        return result

    def send_email_to_person(self, person):
        msg = self.build_email('from@domain.com', ['to@domain.com'],
                               'message to {}'.format(person), 'message')
        print(self.send_email(msg, 'localhost', 25))
