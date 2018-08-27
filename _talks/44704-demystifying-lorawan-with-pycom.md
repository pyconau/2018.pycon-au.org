---
video_url: https://youtu.be/L-fh7PSpPMc
layout: talk
recordingconsent: true
talkid: 44704
title: Demystifying LoRaWAN with PyCom
track: iot
type: talk

speakers:
- bio: "Brian has produced software for over 30 years on lots of different embedded\
    \ projects and still finds it interesting,\r\nand loves learning new things. He\
    \ has been a python user for over 15 of those years, making tools, writing\r\n\
    tests, creating educational robot programming systems, and, at one time, keeping\
    \ his financial books on a\r\npython system. Brian has always been passionate\
    \ about protocols (FlexRay anyone?) so is happy on his current\r\nassignment using\
    \ LoRaWAN to send sensor data to the interweb."
  company: Likeable Software
  name: Brian Danilko
  thumbnailUrl: brian-danilko.png
  twitter: bdanilko
  url: http://www.likeablesoftware.com

abstract: 'Connecting IoT devices using low power over wide area wireless (LoRaWAN)
  makes sense. But how LoRaWAN works, duty cycles, frequency plans, receive windows,
  etc. doesn''t.


  This talk will demystify how LoRaWAN works using PyCom devices.'
---
PyCom devices have made it extremely cheap and easy to create programs and full sensors for the internet of things,
all programmed using the amazing MicroPython. It's very normal for someone to order two PyCom devices and, within hours
of receiving them, have information being transmitted using LoRa between the two devices. LoRa is the low power
and long range wireless system, which is built into the PyCom modules.

But then, you need to scale up from ping-ponging LoRa messages between the two devices, to robust communications
between devices and gateways using LoRaWAN. This talk will look at my experience making this transition, and
LoRaWAN details discovered on the way.

Through this talk you will learn how LoRaWAN networks view the world, the structure of the LoRaWAN packets,
the frequency plans used in Australia, how to minimise air time and therefore power use, and how to be a good
citizens when transmitting (duty cycles/frequency hopping/confirmed messages).
