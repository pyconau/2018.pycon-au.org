---
layout: talk
recordingconsent: true
talkid: 45073
title: End-to-end Energy Monitoring in Python
track: general
type: talk

speakers:
- bio: Non-practicing Electronics Engineer, almost PhD, formerly Remote Sensing and
    GIS developer,Embedded Systems Enthusiast. Currently building the logistics platform
    of the future in Africa.
  company: Lori Systems
  name: Tisham Dhar
  thumbnailUrl: tisham-dhar.png
  twitter: whatnick
  url: http://whatnick.com

abstract: I built an energy monitoring hardware as a hobby. Firmware for configuring,
  reading metering data and pushing out to IoT platform is done in micropython. Server
  for holding the data is Graphite (also python) and analysis of the data is done
  in python ML framework, Keras. End-to-end energy in python.
---
# Energy IoT in Python
This talk presents the development of an open-source (hardware and software) Energy Monitoring system with as much Python as possible. With the firmware written in Micropython (successfully tested on ESP8266 and ESP32 using virtually the same code), Unix port of micropython was used as the dev environment. Data collection platform using the classic Graphite Time-series database and some fun neural-network based analysis of the collected data also in Python with Keras, just to cover AI/ML buzzwords as well.
