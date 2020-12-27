class Messenger:
    def __init__(self):
        self.template_engine = None
        self.mail_server = None

    def send_message(self, body):
        response = self.mail_server.send_message(self.template_engine(body))
        return response

    def get_message(self, client):
        return self.mail_server.get_message(client)
