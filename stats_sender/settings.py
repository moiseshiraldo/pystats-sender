# General options

INTERVAL = 10 # default interval in seconds
STATSD_HOST = 'localhost'
STATSD_PREFIX = ''

INSTALLED_SENDERS = (
    'Diskf',
    'Rabbitmq',
)


# Senders options

DISKF = {
    'interval': 60,
    'filesystem': ('/dev/root',),
}

RABBITMQ = {
    'interval': 10,
    'vhost': 'locashost',
    # Items to show by the 'rabbitmq list_queues'' command, separated by space
    # The name of the queue is included by default
    'items': "messages",
    # Names of the queues whose data will be sent to Statsd
    'names': ['celery',],
}