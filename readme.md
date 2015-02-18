
I played around with [MQTT](http://en.wikipedia.org/wiki/Mqtt) and Python for an upcoming project of mine.

Here are some notes and a simple example code for a subscriber.

<!--more-->

## Requirements
Requires [Mosquitto](http://mosquitto.org/) to be installed.

On Linux with the **apt-get** package manager:

    ::bash
    sudo apt-get install mosquitto
    sudo apt-get install mosquitto-clients

**Note**: ``mosquitto-clients`` is to get the **mosquitto_pub** to make it simple to try stuff from the command line.

Also install [virtualenv](https://pypi.python.org/pypi/virtualenv) if you want to use it (recommended):

    ::bash
    sudo apt-get install python-virtualenv


## Working directory
The use of virtualenv is optional but recommended for playing around with this example code.

    ::bash
    mkdir mqtt-mosquitto-example
    cd mqtt-mosquitto-example
    virtualenv .
    source bin/activate
    pip install -r requirements.txt


## Test the subscriber example
First start the subscriber which will enter a loop waiting for new messages:
    ::bash
    ./subscriber.py

Then open a new terminal and send a message:

    ::bash
    mosquitto_pub -d -h localhost -q 0 -t adult/pics -m "can i haz moar kittenz"

This should generate a message in the terminal running the subscriber.

Take a look at **publisher.py** to see how to publish messages using python. Or just run it from command line while **subscriber.py** is running:

    ::bash
    ./publisher.py


## Configure SSL/TLS

See [mosquitto-tls](http://mosquitto.org/man/mosquitto-tls-7.html) on how to generate certificates and keys.

Once created you need to adjust **/etc/mosquitto/mosquitto.conf** and **subscriber.py** accordingly and then use **mosquitto_pub** with cert and key:

    ::bash
    mosquitto_pub -d -h localhost --cafile root.ca --cert c1.crt --key c1.key -q 0 -t adult/pics -m "can i haz moar kittenz"


## References

    * http://jpmens.net/2013/02/25/lots-of-messages-mqtt-pub-sub-and-the-mosquitto-broker/
    * https://www.justinribeiro.com/chronicle/2012/11/08/securing-mqtt-communication-between-ardruino-and-mosquitto/
    * http://www.instructables.com/id/USB-RFID-Python-Pub-Sub-MQTT/
    * http://mosquitto.org/documentation/python/
    * https://pypi.python.org/pypi/paho-mqtt

