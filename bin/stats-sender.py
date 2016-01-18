import sys
import time

sys.path.append('/etc/stats-sender')

from settings import *
from stats_sender.senders import *

if 'Rabbitmq' in INSTALLED_SENDERS:
    rabbitmq_sender = RabbitmqSender()
    rabbitmq_sender.start()

if 'Diskf' in INSTALLED_SENDERS:
    df_sender = DiskfSender()
    df_sender.start()

while True:
    time.sleep(10)
