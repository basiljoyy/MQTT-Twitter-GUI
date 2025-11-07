# MQTT-Twitter-GUI
# Twitter-like MQTT Pub-Sub Application

## Overview
This project implements a Twitter-like application using MQTT protocol with Python and Tkinter. Users can:
- Publish tweets with hashtags.
- Subscribe/unsubscribe to hashtags to receive real-time tweets.

## Files
- `publisher.py` → GUI to publish tweets.
- `subscriber.py` → GUI to subscribe and view tweets.

## Requirements
- Python 3.x
- `paho-mqtt` library (`pip install paho-mqtt`)
- `tkinter` (usually included with Python)

## How to Run
1. Open a terminal.
2. Run `publisher.py` to start the tweet publisher.
3. Run `subscriber.py` to start the hashtag subscriber.
4. Publish messages and subscribe to hashtags to see tweets in real time.
