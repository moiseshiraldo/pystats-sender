import subprocess
import time
import statsd
from threading import Thread

from settings import STATSD_HOST, INTERVAL, STATSD_PREFIX


class Sender(Thread):
    """
    Extend Thread class to implement the base sender. Construct new senders
    extending this class and overriding the send method.
    """

    client = statsd.StatsClient(STATSD_HOST)

    def __init__(self):
        self.interval = INTERVAL
        self.stopped = False
        Thread.__init__(self)
        self.daemon = True

    def send(self):
        pass

    def run(self):
        while not self.stopped:
            self.send()
            time.sleep(self.interval)

    def prefix(self, name):
        if STATSD_PREFIX:
            return STATSD_PREFIX + "." + name
        return name

    def send_gauge(self, name, value):
        name = self.prefix(name)
        self.client.gauge(name, value)

    def send_counter(self, name, decr=False, rate=1):
        name = self.prefix(name)
        if decr:
            self.client.decr(name, rate=rate)
        else:
            self.client.incr(name, rate=rate)

    def send_timing(self, name, seconds):
        name = self.prefix(name)
        self.client.timing(name, seconds*1000)

    def send_set(self, name, key):
        name = self.prefix(name)
        self.client.set(name, key)

    def command_output(self, command):
        command = command.split()
        p = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = p.communicate()
        return out.splitlines()
