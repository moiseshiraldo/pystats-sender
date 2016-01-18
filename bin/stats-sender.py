import sys
import time
import argparse

parser = argparse.ArgumentParser(description='Initialize the stats senders.')
parser.add_argument("-c", "--config", help="Specify configuration directory")
args = parser.parse_args()

if args.config:
    conf_dir = args.config
else:
    conf_dir = '/etc/stats-sender'

sys.path.append(conf_dir)

try:
    from settings import *
    from stats_sender.senders import *
except ImportError:
    print(("[Error]: couldn't find settings.py on "+conf_dir))
    sys.exit()


if 'Rabbitmq' in INSTALLED_SENDERS:
    rabbitmq_sender = RabbitmqSender()
    rabbitmq_sender.start()

if 'Diskf' in INSTALLED_SENDERS:
    df_sender = DiskfSender()
    df_sender.start()

while True:
    time.sleep(10)
