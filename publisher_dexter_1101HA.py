#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
Publish some messages to queue
"""
import paho.mqtt.publish as publish


#msgs = [{'topic': "kids/yolo", 'payload': "jump"},
#        {'topic': "adult/pics", 'payload': "some photo"},
#        {'topic': "adult/news", 'payload': "extra extra"},
#        {'topic': "adult/news", 'payload': "super extra"}]
msgs = [{'topic': "home/door1/state", 'payload': "open"},
        {'topic': "home/door2/state", 'payload': "close"},
        {'topic': "home/window1/state", 'payload': "open"},
        {'topic': "home/window2/state", 'payload': "close"},
        {'topic': "home/light/state", 'payload': "close"},
        {'topic': "home/light/color", 'payload': "white"}]

host = "localhost"


if __name__ == '__main__':
    # publish a single message
    #publish.single(topic="kids/yolo", payload="just do it", hostname=host)
    publish.single(topic="home/light/color", payload="red", hostname="192.168.112.129")

    # publish multiple messages
    publish.multiple(msgs, hostname=host)


# vi: set fileencoding=utf-8 :
