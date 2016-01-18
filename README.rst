======================
stats-sender
======================

A Python stats collector and sender for Statsd_ using pystatsd_.

At this moment is just a proof of concept in alpha state, with two senders defined: disk usage and items listed by rabbitmqctl list_queues.



Installation
============

Using pip::

    $ pip install -e git+https://github.com/moiseshiraldo/pystats-sender#egg=stats_sender



Configuration
=============

All the configuration is done on */etc/stats-sender/settings.py*.


.. _Statsd: https://github.com/etsy/statsd
.. _pystatsd: https://github.com/jsocol/pystatsd
