---
video_url: https://youtu.be/hHec4qL00x0
layout: talk
recordingconsent: true
talkid: 45358
title: Writing fast and efficient MicroPython
track: iot
type: talk

speakers:
- bio: Damien has a background in theoretical physics, robotics and computer engineering,
    and loves to program and build things. He is the creator of MicroPython and ran
    two very fruitful Kickstarter campaigns to build a community around this microcontroller
    language. He has built a successful company based on MicroPython and the pyboard,
    brought it to makers, teachers and industry developers around the world, worked
    with the BBC on the micro:bit project, and embarked on projects with the European
    Space Agency to bring MicroPython into space. Damien now works full time improving
    and maintaining the MicroPython ecosystem.
  company: George Robotics
  name: Damien George
  thumbnailUrl: damien-george.png
  twitter: micropython
  url: http://dpgeorge.net

abstract: MicroPython is an implementation of Python designed to run on microcontrollers
  and embedded systems. These devices don't have many resources (CPU, RAM) and so
  it's important to write efficient scripts. This talk shows how to make the most
  of your resources in MicroPython, and has some fun demos!
---
MicroPython is a reimplementation of Python which is specifically designed to run on computing devices that have very few resources, such as CPU power, RAM and storage.  Often when you write scripts in MicroPython you want to make the most of your available resources, and have code run as fast as possible (faster code usually saves power, which is important when running from a battery!) and there are certain ways of writing MicroPython code that are more efficient than others.  In this talk I will go over the tricks and techniques for writing fast and efficient Python code in MicroPython.  As part of this I will delve into some technical details of how MicroPython works, in order to better understand what it's doing behind the scenes and how to make the most of it.  I will discuss general techniques for making things run faster (some of which would be applicable to normal Python), as well as ways to completely avoid memory allocation, which is important for both efficiency and making code execution deterministic.  The talk will include some hardware demos to show off the techniques, including five different ways to blink an LED fast.
