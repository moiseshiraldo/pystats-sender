from settings import DISKF
from stats_sender.senders import Sender


class DiskfSender(Sender):

    def __init__(self):
        super(DiskfSender, self).__init__()
        if DISKF.get('interval'):
            self.interval = DISKF['interval']

    def send(self):
        lines = self.command_output("df -k -l -P")
        headers = lines[0].split()
        fs_index = headers.index("Filesystem")
        du_index = headers.index("Capacity")
        for line in lines:
            values = line.split()
            if values[fs_index] in DISKF.get('filesystem'):
                try:
                    disk_usage = int(values[du_index].strip('%'))
                    if values[fs_index][0] == '/':
                        tag = values[fs_index][1:].replace('/','_')
                    else:
                        tag = values[fs_index].replace('/','_')
                    self.send_gauge('diskf.'+tag, disk_usage)
                except ValueError:
                    pass