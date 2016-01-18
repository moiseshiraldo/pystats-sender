from settings import RABBITMQ
from stats_sender.senders import Sender


class RabbitmqSender(Sender):

    def __init__(self):
        super(RabbitmqSender, self).__init__()
        self.q_size = dict()
        if RABBITMQ.get('interval'):
            self.interval = RABBITMQ['interval']

    def send(self):
        command = "sudo rabbitmqctl list_queues"
        if RABBITMQ.get('vhost'):
            command = command + " -p " + RABBITMQ['vhost']
        if RABBITMQ.get('items'):
            command = command + " name" + RABBITMQ['items']
            items = RABBITMQ['items'].split()
        lines = self.command_output(command)
        for line in lines:
            values = line.split()
            if values[0] in RABBITMQ.get['names']:
                for i,value in enumerate(values[1:]):
                    try:
                        self.send_gauge('rabbitmq.'+items[i], int(value))
                    except ValueError:
                        pass