---
video_url: https://youtu.be/imW-trt0i9I
layout: talk
recordingconsent: true
talkid: 45184
title: You Don't Need That!
track: general
type: talk

speakers:
- bio: "Christopher is an Australian Python developer, speaker, and serial conference\
    \ organizer. He has years of experience running volunteer-led conferences, starting\
    \ with PyCon Australia, then as director of linux.conf.au 2017. Currently he leads\
    \ North Bay Python, a single-track community Python conference run out of a live\
    \ music venue in Petaluma, California, where he now lives. \r\n\r\n
      For his day job, Christopher is a Senior Software Engineer at Shutterstock,
      Inc, building tools that provide organizations with access to knowledge that’s
      dispersed and underutilized. Christopher is an advocate within the Australian
      and International Python communities, is on the steering committee for PyCon
      Australia, serves on the Python Software Foundation’s Grants Working Group, is
      a past board member of Linux Australia, and has been a fellow of the Python
      Software Foundation since 2013."

  company: North Bay Python / Shutterstock, Inc
  name: Christopher Neugebauer
  thumbnailUrl: christopher-neugebauer.png
  twitter: chrisjrn
  url: https://chrisjrn.com

abstract: Not every design pattern makes sense in Python. This talk builds up design
  patterns commonly used in enterprise languages, and shows the features in Python
  that make these approaches unnecessary.
---
Software design is hard. That's why we invented design patterns. Design patterns abstract common approaches to problem solving into generic approaches that can be modified to suit the application at hand.

Many of the design patterns in common use today are inspired by static object-oriented Enterprise languages like Java. These languages have a feature set that is somewhat more restrictive than Python's, and many design patterns are built to provide elegant ways around these restrictions.

Design patterns, like Dependency Injection, and the Visitor Pattern arise from restrictions on how you can pass code around at runtime. Other patterns, like Iterators, have been replaced by first-class language features of their own.

And some patterns, like Threads just never worked at all.

In this talk, we'll build up several design patterns, and then look at the Python features that make each pattern unnecessary. In doing so, you'll get a view into idiomatically translating code into Python, and a greater understanding of design decisions users of other languages need to make.


