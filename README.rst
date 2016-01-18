======================
stats-sender
======================

A Python stats collector and sender for Statsd_ using pystatsd_.

At this moment is just a proof of concept in alpha state, with two senders defined:
disk usage and items listed by rabbitmqctl list_queues.



Installation
============

Using pip::

    $ pip install -e git+https://github.com/moiseshiraldo/pystats-sender#egg=stats_sender



Configuration
=============

By default the configuration file is expected to be on */etc/stats-sender/settings.py*.

To specify another location use the -c option when launching the process:

    $ stats-sender.py -c DIRECTORY


Senders
=======

For the rabbitmq sender, the user who runs the *stats-sender* process must have permissions
to execute *rabbitmqctl* with *sudo* and no password. To grant that permission, edit the
*/etc/sudoers* file:

    $ sudo visudo

And add the line:

    user ALL=(ALL) NOPASSWD: /usr/sbin/rabbitmqctl
    
.. _Statsd: https://github.com/etsy/statsd
.. _pystatsd: https://github.com/jsocol/pystatsd